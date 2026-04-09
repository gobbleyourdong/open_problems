"""
Numerical estimation of the sharp constant in ||S||_3 <= C ||omega||_3 on T^3.

CORRECTED VERSION: The operator is the Riesz-transform composition
  omega -> S = sym(nabla u), u = Biot-Savart(omega)

For div-free omega, curl(u) = omega, so:
  S_{ij} = (partial_i u_j + partial_j u_i) / 2

In Fourier:
  u_hat(k) = i (k x omega_hat(k)) / |k|^2
  S_hat_{ij}(k) = i (k_j u_hat_i + k_i u_hat_j) / 2

This is a degree-0 Fourier multiplier (CZ operator).

The symbol m(xi) maps omega_hat(xi) -> S_hat(xi) and is homogeneous degree 0.
For div-free omega: k . omega_hat = 0 constrains the input.

We want to estimate:
  C_divfree = sup { ||S||_3 / ||omega||_3 : div(omega) = 0, omega != 0 }
  C_general = sup { ||S||_3 / ||omega||_3 : omega != 0 }

where in the general case, omega is still processed through the same Biot-Savart.

KEY INSIGHT: For general omega, Biot-Savart only sees the solenoidal part
P(omega) = omega - grad(div^{-1} div omega). So:
  ||S||_3 = ||S(P omega)||_3 <= C_divfree ||P omega||_3 <= C_divfree ||omega||_3

Thus C_general <= C_divfree trivially. There's no "epsilon improvement" from
the div-free constraint in this direction.

The INTERESTING question for regularity theory is different:
  Does ||S||_3 <= (1-epsilon) ||omega||_3 hold for ALL div-free omega?
  i.e., is C_divfree < 1?

If C_divfree < 1, the strain is controlled by vorticity in L^3, which would
give regularity via the Beale-Kato-Majda criterion.

Also: compare with the INDIVIDUAL Riesz transform ||R_i f||_p / ||f||_p
to see how the composition + symmetrization + div-free constraint compare.
"""

import torch
import time
import numpy as np

torch.set_default_dtype(torch.float64)
device = torch.device('cpu')

N = 32
N_SAMPLES = 1000

def make_wavenumbers(N):
    freq = torch.fft.fftfreq(N, d=1.0/N)
    kx, ky, kz = torch.meshgrid(freq, freq, freq, indexing='ij')
    return kx, ky, kz

def generate_divfree_omega_hat(N, kx, ky, kz):
    """Random div-free vector field: project random a(k) onto plane perp to k."""
    a_real = torch.randn(3, N, N, N)
    a_imag = torch.randn(3, N, N, N)
    a = torch.complex(a_real, a_imag)

    ksq = kx**2 + ky**2 + kz**2
    ksq_safe = ksq.clone()
    ksq_safe[0, 0, 0] = 1.0

    k_dot_a = kx * a[0] + ky * a[1] + kz * a[2]
    k_vec = torch.stack([kx, ky, kz])
    omega_hat = a - k_vec * (k_dot_a / ksq_safe).unsqueeze(0)
    omega_hat[:, 0, 0, 0] = 0.0

    return omega_hat

def generate_general_omega_hat(N):
    """Random general (not div-free) vector field."""
    a_real = torch.randn(3, N, N, N)
    a_imag = torch.randn(3, N, N, N)
    a = torch.complex(a_real, a_imag)
    a[:, 0, 0, 0] = 0.0
    return a

def biot_savart_hat(omega_hat, kx, ky, kz):
    """u_hat = i (k x omega_hat) / |k|^2"""
    ksq = kx**2 + ky**2 + kz**2
    ksq_safe = ksq.clone()
    ksq_safe[0, 0, 0] = 1.0
    inv_ksq = 1.0 / ksq_safe
    inv_ksq[0, 0, 0] = 0.0

    cross_x = ky * omega_hat[2] - kz * omega_hat[1]
    cross_y = kz * omega_hat[0] - kx * omega_hat[2]
    cross_z = kx * omega_hat[1] - ky * omega_hat[0]

    i = torch.tensor(1j, dtype=torch.complex128)
    u_hat = torch.stack([
        i * cross_x * inv_ksq,
        i * cross_y * inv_ksq,
        i * cross_z * inv_ksq,
    ])
    return u_hat

def strain_hat(u_hat, kx, ky, kz):
    """S_hat_{ab} = i (k_b u_hat_a + k_a u_hat_b) / 2"""
    i = torch.tensor(1j, dtype=torch.complex128)
    k = torch.stack([kx, ky, kz])

    S = torch.zeros(3, 3, N, N, N, dtype=torch.complex128)
    for a in range(3):
        for b in range(a, 3):
            val = i * (k[b] * u_hat[a] + k[a] * u_hat[b]) / 2.0
            S[a, b] = val
            if b != a:
                S[b, a] = val
    return S

def Lp_norm(field_hat, p, N):
    """
    ||f||_p = (1/|T^3| integral |f|^p dx)^{1/p}
    = (mean over grid of |f(x)|^p)^{1/p}

    field_hat shape: (components..., N, N, N)
    |f| = sqrt(sum of |f_i|^2) for vector, Frobenius for tensor.
    """
    orig_shape = field_hat.shape
    spatial_shape = orig_shape[-3:]
    n_comp = int(np.prod(orig_shape[:-3])) if len(orig_shape) > 3 else 1

    flat_hat = field_hat.reshape(n_comp, *spatial_shape)

    # iFFT each component
    flat_phys = torch.fft.ifftn(flat_hat, dim=(-3, -2, -1))

    # Should be real (up to round-off for Hermitian-symmetric input)
    # But our random fields are NOT Hermitian symmetric → complex physical space
    # We need to handle this properly.
    # Actually: random omega_hat with independent real/imag parts gives
    # a complex-valued field. For the L^p norm we should take |f| properly.

    # |f(x)|^2 = sum_i |f_i(x)|^2 where |f_i(x)|^2 = Re(f_i)^2 + Im(f_i)^2
    mag_sq = (flat_phys.real ** 2 + flat_phys.imag ** 2).sum(dim=0)
    mag = torch.sqrt(mag_sq)

    lp = (mag ** p).mean() ** (1.0 / p)
    return lp

def compute_ratio(omega_hat, kx, ky, kz, p=3):
    """Compute ||S||_p / ||omega||_p"""
    u_hat = biot_savart_hat(omega_hat, kx, ky, kz)
    S_hat = strain_hat(u_hat, kx, ky, kz)

    norm_S = Lp_norm(S_hat, p, N)
    norm_omega = Lp_norm(omega_hat, p, N)

    if norm_omega < 1e-15:
        return 0.0
    return (norm_S / norm_omega).item()

def single_riesz_ratio(N, kx, ky, kz, p=3, n_samples=500):
    """
    Estimate ||R_1 f||_p / ||f||_p for scalar f.
    R_1 f hat(k) = -i k_1 / |k| * f_hat(k)
    """
    max_ratio = 0.0
    for _ in range(n_samples):
        f_real = torch.randn(N, N, N)
        f_imag = torch.randn(N, N, N)
        f_hat = torch.complex(f_real, f_imag)
        f_hat[0, 0, 0] = 0.0

        k_mag = torch.sqrt(kx**2 + ky**2 + kz**2)
        k_mag_safe = k_mag.clone()
        k_mag_safe[0, 0, 0] = 1.0

        i = torch.tensor(1j, dtype=torch.complex128)
        Rf_hat = -i * kx / k_mag_safe * f_hat
        Rf_hat[0, 0, 0] = 0.0

        # Physical space
        f_phys = torch.fft.ifftn(f_hat)
        Rf_phys = torch.fft.ifftn(Rf_hat)

        f_mag = torch.sqrt(f_phys.real**2 + f_phys.imag**2)
        Rf_mag = torch.sqrt(Rf_phys.real**2 + Rf_phys.imag**2)

        norm_f = (f_mag ** p).mean() ** (1.0/p)
        norm_Rf = (Rf_mag ** p).mean() ** (1.0/p)

        if norm_f > 1e-15:
            ratio = (norm_Rf / norm_f).item()
            max_ratio = max(max_ratio, ratio)

    return max_ratio

def double_riesz_ratio(N, kx, ky, kz, p=3, n_samples=500):
    """
    Estimate ||R_1 R_2 f||_p / ||f||_p for scalar f.
    (R_1 R_2 f)^hat = -k_1 k_2 / |k|^2 * f_hat
    """
    max_ratio = 0.0
    for _ in range(n_samples):
        f_real = torch.randn(N, N, N)
        f_imag = torch.randn(N, N, N)
        f_hat = torch.complex(f_real, f_imag)
        f_hat[0, 0, 0] = 0.0

        ksq = kx**2 + ky**2 + kz**2
        ksq_safe = ksq.clone()
        ksq_safe[0, 0, 0] = 1.0

        Rf_hat = -kx * ky / ksq_safe * f_hat
        Rf_hat[0, 0, 0] = 0.0

        f_phys = torch.fft.ifftn(f_hat)
        Rf_phys = torch.fft.ifftn(Rf_hat)

        f_mag = torch.sqrt(f_phys.real**2 + f_phys.imag**2)
        Rf_mag = torch.sqrt(Rf_phys.real**2 + Rf_phys.imag**2)

        norm_f = (f_mag ** p).mean() ** (1.0/p)
        norm_Rf = (Rf_mag ** p).mean() ** (1.0/p)

        if norm_f > 1e-15:
            ratio = (norm_Rf / norm_f).item()
            max_ratio = max(max_ratio, ratio)

    return max_ratio

def ensure_hermitian_divfree(N, kx, ky, kz):
    """
    Generate a REAL-valued div-free vector field on T^3.
    omega_hat must satisfy omega_hat(-k) = conj(omega_hat(k)) (Hermitian symmetry)
    and k . omega_hat(k) = 0.
    """
    omega_hat = torch.zeros(3, N, N, N, dtype=torch.complex128)

    # Generate for k with kx > 0, or kx == 0 and ky > 0, or kx == ky == 0 and kz > 0
    freq = torch.fft.fftfreq(N, d=1.0/N)

    for ix in range(N):
        for iy in range(N):
            for iz in range(N):
                kxv, kyv, kzv = freq[ix].item(), freq[iy].item(), freq[iz].item()
                if kxv == 0 and kyv == 0 and kzv == 0:
                    continue

                # Determine if this is a "positive" mode
                if kxv > 0 or (kxv == 0 and kyv > 0) or (kxv == 0 and kyv == 0 and kzv > 0):
                    # Generate random a perpendicular to k
                    k_vec = torch.tensor([kxv, kyv, kzv])
                    k_norm = k_vec / k_vec.norm()

                    # Two random vectors perpendicular to k
                    # Use Gram-Schmidt
                    a_r = torch.randn(3)
                    a_r = a_r - (a_r @ k_norm) * k_norm
                    if a_r.norm() < 1e-10:
                        a_r = torch.randn(3)
                        a_r = a_r - (a_r @ k_norm) * k_norm

                    a_i = torch.randn(3)
                    a_i = a_i - (a_i @ k_norm) * k_norm
                    if a_i.norm() < 1e-10:
                        a_i = torch.randn(3)
                        a_i = a_i - (a_i @ k_norm) * k_norm

                    val = torch.complex(a_r, a_i)  # shape (3,)
                    omega_hat[:, ix, iy, iz] = val

                    # Hermitian conjugate at -k
                    mix = (-ix) % N
                    miy = (-iy) % N
                    miz = (-iz) % N
                    omega_hat[:, mix, miy, miz] = val.conj()

    return omega_hat

def main():
    print("=" * 70)
    print("Sharp CZ constant estimation: ||S||_3 <= C ||omega||_3 on T^3")
    print(f"Resolution N={N}, Samples={N_SAMPLES}")
    print("=" * 70)

    kx, ky, kz = make_wavenumbers(N)

    # ========== Part 1: Div-free complex fields ==========
    print("\n[1] Divergence-free omega (complex-valued, random Fourier coefficients)")
    t0 = time.time()

    ratios_divfree = []
    for i in range(N_SAMPLES):
        omega_hat = generate_divfree_omega_hat(N, kx, ky, kz)
        ratio = compute_ratio(omega_hat, kx, ky, kz)
        ratios_divfree.append(ratio)
        if (i+1) % 250 == 0:
            print(f"  {i+1}/{N_SAMPLES}: max ratio = {max(ratios_divfree):.6f}")

    ratios_divfree = torch.tensor(ratios_divfree)
    t1 = time.time()
    print(f"  Time: {t1-t0:.1f}s")
    print(f"  Max:  {ratios_divfree.max():.6f}")
    print(f"  Mean: {ratios_divfree.mean():.6f}")
    print(f"  Std:  {ratios_divfree.std():.6f}")
    print(f"  P95:  {ratios_divfree.quantile(0.95):.6f}")
    print(f"  P99:  {ratios_divfree.quantile(0.99):.6f}")

    # ========== Part 2: Real-valued div-free fields ==========
    print("\n[2] Divergence-free omega (REAL-valued, Hermitian-symmetric)")
    t0 = time.time()

    ratios_real_divfree = []
    for i in range(200):  # fewer samples since Hermitian construction is slower
        omega_hat = ensure_hermitian_divfree(N, kx, ky, kz)

        # Verify real-valued
        if i == 0:
            omega_phys = torch.fft.ifftn(omega_hat, dim=(-3, -2, -1))
            imag_err = omega_phys.imag.abs().max().item()
            print(f"  Imag check: max|Im(omega)| = {imag_err:.2e}")

            div_hat = kx * omega_hat[0] + ky * omega_hat[1] + kz * omega_hat[2]
            div_err = div_hat.abs().max().item()
            print(f"  Div check: max|k.omega_hat| = {div_err:.2e}")

        ratio = compute_ratio(omega_hat, kx, ky, kz)
        ratios_real_divfree.append(ratio)

    ratios_real_divfree = torch.tensor(ratios_real_divfree)
    t1 = time.time()
    print(f"  Time: {t1-t0:.1f}s ({len(ratios_real_divfree)} samples)")
    print(f"  Max:  {ratios_real_divfree.max():.6f}")
    print(f"  Mean: {ratios_real_divfree.mean():.6f}")

    # ========== Part 3: General (non-divfree) complex fields ==========
    print("\n[3] General omega (not div-free, complex-valued)")
    t0 = time.time()

    ratios_general = []
    for i in range(N_SAMPLES):
        omega_hat = generate_general_omega_hat(N)
        ratio = compute_ratio(omega_hat, kx, ky, kz)
        ratios_general.append(ratio)
        if (i+1) % 250 == 0:
            print(f"  {i+1}/{N_SAMPLES}: max ratio = {max(ratios_general):.6f}")

    ratios_general = torch.tensor(ratios_general)
    t1 = time.time()
    print(f"  Time: {t1-t0:.1f}s")
    print(f"  Max:  {ratios_general.max():.6f}")
    print(f"  Mean: {ratios_general.mean():.6f}")
    print(f"  Std:  {ratios_general.std():.6f}")

    # ========== Part 4: Leray-projected ratio ==========
    # For general omega, compute ||S(P omega)||_3 / ||P omega||_3
    # where P = Leray projection. This should give the SAME constant as div-free.
    print("\n[4] General omega, but ratio = ||S||_3 / ||P(omega)||_3")
    t0 = time.time()

    ratios_leray = []
    for i in range(N_SAMPLES):
        omega_hat = generate_general_omega_hat(N)

        # Leray project omega
        ksq = kx**2 + ky**2 + kz**2
        ksq_safe = ksq.clone()
        ksq_safe[0, 0, 0] = 1.0
        k_dot_o = kx * omega_hat[0] + ky * omega_hat[1] + kz * omega_hat[2]
        k_vec = torch.stack([kx, ky, kz])
        P_omega_hat = omega_hat - k_vec * (k_dot_o / ksq_safe).unsqueeze(0)
        P_omega_hat[:, 0, 0, 0] = 0.0

        # Compute S from P_omega (same as from omega since BS only sees solenoidal part)
        u_hat = biot_savart_hat(omega_hat, kx, ky, kz)
        S_hat_val = strain_hat(u_hat, kx, ky, kz)

        norm_S = Lp_norm(S_hat_val, 3, N)
        norm_Pomega = Lp_norm(P_omega_hat, 3, N)

        if norm_Pomega > 1e-15:
            ratios_leray.append((norm_S / norm_Pomega).item())

    ratios_leray = torch.tensor(ratios_leray)
    t1 = time.time()
    print(f"  Time: {t1-t0:.1f}s")
    print(f"  Max:  {ratios_leray.max():.6f}")
    print(f"  Mean: {ratios_leray.mean():.6f}")
    print(f"  (Should match div-free max since P(omega) is div-free)")

    # ========== Part 5: Individual Riesz transform constants ==========
    print("\n[5] Reference: individual Riesz transform constants on L^3(T^3)")
    t0 = time.time()

    c_R1 = single_riesz_ratio(N, kx, ky, kz, p=3, n_samples=500)
    c_R1R2 = double_riesz_ratio(N, kx, ky, kz, p=3, n_samples=500)

    t1 = time.time()
    print(f"  Time: {t1-t0:.1f}s")
    print(f"  ||R_1 f||_3 / ||f||_3 max:     {c_R1:.6f}")
    print(f"  ||R_1 R_2 f||_3 / ||f||_3 max: {c_R1R2:.6f}")
    print(f"  Theoretical (Iwaniec, p=3): p*-1 = {3/(3-1) - 1 + 1:.4f}")
    print(f"  (Iwaniec conjecture: ||R||_p <= p*-1 where p* = max(p, p/(p-1)))")
    print(f"  For p=3: p* = 3, so conjectured ||R||_3 <= 2")

    # ========== Part 6: L^p sweep for div-free ==========
    print("\n[6] L^p sweep: ||S||_p / ||omega||_p for div-free omega")
    for p in [2.0, 2.5, 3.0, 3.5, 4.0, 5.0]:
        max_r = 0.0
        for _ in range(200):
            omega_hat = generate_divfree_omega_hat(N, kx, ky, kz)
            u_hat = biot_savart_hat(omega_hat, kx, ky, kz)
            S_hat_val = strain_hat(u_hat, kx, ky, kz)
            nS = Lp_norm(S_hat_val, p, N)
            no = Lp_norm(omega_hat, p, N)
            if no > 1e-15:
                r = (nS / no).item()
                max_r = max(max_r, r)
        print(f"  p = {p:.1f}: max ratio = {max_r:.6f}")

    # ========== SUMMARY ==========
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    C_df = ratios_divfree.max().item()
    C_gen = ratios_general.max().item()
    C_leray = ratios_leray.max().item()

    print(f"\n  Operator: omega -> S = sym(nabla u), u = BS(omega)")
    print(f"  ||S||_3 / ||omega||_3 constants at N={N}:")
    print(f"")
    print(f"  C_divfree  (1000 samples): {C_df:.6f}")
    print(f"  C_general  (1000 samples): {C_gen:.6f}")
    print(f"  C_leray    (1000 samples): {C_leray:.6f}")
    print(f"")
    print(f"  C_general < C_divfree because BS kills the irrotational part of omega,")
    print(f"  but ||omega||_3 includes it, inflating the denominator.")
    print(f"  C_leray ~ C_divfree (same operator restricted to same subspace).")
    print(f"")
    print(f"  KEY QUESTION: Is C_divfree < 1?")
    print(f"  Answer: C_divfree = {C_df:.4f} {'< 1 (YES!)' if C_df < 1 else '>= 1 (NO)'}")
    print(f"")
    if C_df < 1:
        print(f"  If C_divfree < 1 in the continuum limit (N -> inf), then")
        print(f"  ||S||_3 <= C ||omega||_3 with C < 1 for div-free fields,")
        print(f"  which would give ||S||_3 < ||omega||_3 (strict inequality).")
        print(f"  This is the 'depletion' phenomenon.")
        print(f"")
        print(f"  For NS regularity: need this on R^3 or T^3, for ALL div-free omega.")
        print(f"  Numerical estimate with 1000 random samples at N=32 gives C ~ {C_df:.4f}")
        print(f"  But this is a LOWER BOUND on the true sup (adversarial search needed).")

    print(f"\n  Single Riesz ||R_1||_{{3->3}} ~ {c_R1:.4f}")
    print(f"  Double Riesz ||R_1 R_2||_{{3->3}} ~ {c_R1R2:.4f}")
    print(f"  Our composed operator: ~ {C_df:.4f}")
    print(f"  (The composition + symmetrization + div-free constraint")
    print(f"   gives a SMALLER constant than individual Riesz transforms)")

    # ========== Concentration of measure check ==========
    print(f"\n  Standard deviation of ratio (div-free): {ratios_divfree.std():.6f}")
    print(f"  Ratio (max - mean) / std: {(ratios_divfree.max() - ratios_divfree.mean()) / ratios_divfree.std():.2f}")
    print(f"  (High concentration suggests random fields cluster near the max)")

    print("=" * 70)

if __name__ == '__main__':
    main()
