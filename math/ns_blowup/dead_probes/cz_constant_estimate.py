"""
Numerical estimation of the sharp constant in ||S||_3 <= C ||omega||_3
on T^3 for divergence-free omega vs general omega.

S = sym(nabla u), where u = Biot-Savart(omega): u_hat(k) = i k x omega_hat(k) / |k|^2

Method:
  1. Generate random divergence-free omega on T^3 at resolution N=32
     (omega_hat(k) perpendicular to k for each nonzero k)
  2. Compute u via Biot-Savart in Fourier space
  3. Compute S = (nabla u + nabla u^T) / 2 in Fourier space
  4. Compute ||S||_3 / ||omega||_3 in physical space
  5. Maximize over 1000 random samples

Compare div-free vs general (unconstrained) omega.

All Fourier transforms via torch.fft. Float64 precision.
"""

import torch
import time
import numpy as np

torch.set_default_dtype(torch.float64)
device = torch.device('cpu')

N = 32
N_SAMPLES = 1000

def make_wavenumbers(N):
    """Create wavenumber grids for T^3 = [0, 2pi)^3."""
    freq = torch.fft.fftfreq(N, d=1.0/N)  # integer wavenumbers 0,1,...,N/2,-N/2+1,...,-1
    kx, ky, kz = torch.meshgrid(freq, freq, freq, indexing='ij')
    return kx, ky, kz

def generate_divfree_omega_hat(N, kx, ky, kz):
    """
    Generate a random divergence-free vector field omega in Fourier space.
    For each k != 0, omega_hat(k) is perpendicular to k.

    Method: generate random complex vector a(k), then project:
      omega_hat(k) = a(k) - k (k . a(k)) / |k|^2
    This gives div(omega) = ik . omega_hat = 0.
    """
    # Random complex coefficients
    a_real = torch.randn(3, N, N, N)
    a_imag = torch.randn(3, N, N, N)
    a = torch.complex(a_real, a_imag)  # shape (3, N, N, N)

    # |k|^2
    ksq = kx**2 + ky**2 + kz**2
    ksq[0, 0, 0] = 1.0  # avoid division by zero

    # k . a
    k_dot_a = kx * a[0] + ky * a[1] + kz * a[2]

    # Project: omega_hat = a - k (k.a) / |k|^2
    k_vec = torch.stack([kx, ky, kz])  # (3, N, N, N)
    omega_hat = a - k_vec * (k_dot_a / ksq).unsqueeze(0)

    # Zero mode
    omega_hat[:, 0, 0, 0] = 0.0

    return omega_hat

def generate_general_omega_hat(N):
    """Generate a random (not necessarily div-free) vector field in Fourier space."""
    a_real = torch.randn(3, N, N, N)
    a_imag = torch.randn(3, N, N, N)
    a = torch.complex(a_real, a_imag)
    a[:, 0, 0, 0] = 0.0  # zero mean
    return a

def biot_savart(omega_hat, kx, ky, kz):
    """
    Compute u_hat = i k x omega_hat / |k|^2

    (k x omega)_j = eps_{jlm} k_l omega_m
    u_hat = i (k x omega_hat) / |k|^2
    """
    ksq = kx**2 + ky**2 + kz**2
    ksq[0, 0, 0] = 1.0

    # k x omega_hat
    cross_x = ky * omega_hat[2] - kz * omega_hat[1]
    cross_y = kz * omega_hat[0] - kx * omega_hat[2]
    cross_z = kx * omega_hat[1] - ky * omega_hat[0]

    inv_ksq = 1.0 / ksq
    inv_ksq[0, 0, 0] = 0.0  # zero mode of u is zero

    # u_hat = i (k x omega_hat) / |k|^2
    i = torch.tensor(1j, dtype=torch.complex128)
    u_hat = torch.stack([
        i * cross_x * inv_ksq,
        i * cross_y * inv_ksq,
        i * cross_z * inv_ksq,
    ])

    return u_hat

def compute_strain_hat(u_hat, kx, ky, kz):
    """
    Compute S_hat = sym(nabla u)_hat in Fourier space.
    (nabla u)_{ij} hat = i k_j u_hat_i
    S_{ij} = (nabla u_{ij} + nabla u_{ji}) / 2
    S_hat_{ij} = i (k_j u_hat_i + k_i u_hat_j) / 2

    Returns 6 independent components: S_11, S_22, S_33, S_12, S_13, S_23
    """
    i = torch.tensor(1j, dtype=torch.complex128)
    k = torch.stack([kx, ky, kz])  # (3, N, N, N)

    # S_hat[a,b] = i * (k[b] * u_hat[a] + k[a] * u_hat[b]) / 2
    S_hat = torch.zeros(3, 3, *u_hat.shape[1:], dtype=torch.complex128)
    for a in range(3):
        for b in range(3):
            S_hat[a, b] = i * (k[b] * u_hat[a] + k[a] * u_hat[b]) / 2.0

    return S_hat

def L3_norm(field_hat, N):
    """
    Compute ||f||_3 = (1/(2pi)^3 integral |f|^3 dx)^{1/3}
    where f is a vector/tensor field given by its Fourier coefficients.

    For a vector field (3, N, N, N): |f|^2 = sum_i |f_i|^2
    For a tensor field (3, 3, N, N, N): |f|^2 = sum_{ij} |f_{ij}|^2 (Frobenius)

    We compute in physical space via iFFT.
    """
    orig_shape = field_hat.shape
    spatial_shape = orig_shape[-3:]
    n_components = int(np.prod(orig_shape[:-3])) if len(orig_shape) > 3 else 1

    # Reshape to (n_components, N, N, N) for batch iFFT
    flat_hat = field_hat.reshape(n_components, *spatial_shape)

    # iFFT to physical space (unnormalized: torch uses 1/N^3 for backward)
    flat_phys = torch.fft.ifftn(flat_hat, dim=(-3, -2, -1))

    # |f(x)|^2 = sum over components of |f_i(x)|^2
    # flat_phys is complex but should be real for real fields
    # Take real part (imaginary should be ~0 for properly Hermitian input)
    flat_phys_real = flat_phys.real

    # Pointwise squared magnitude summed over components
    mag_sq = (flat_phys_real ** 2).sum(dim=0)  # (N, N, N)
    mag = torch.sqrt(mag_sq)  # |f(x)| at each grid point

    # L^3 norm: (mean |f|^3)^{1/3} where mean is over the grid
    # (The domain is T^3 = [0,2pi)^3 with volume (2pi)^3, grid has N^3 points)
    l3 = (mag ** 3).mean() ** (1.0/3.0)

    return l3

def compute_ratio(omega_hat, kx, ky, kz, N):
    """Compute ||S||_3 / ||omega||_3 for given omega_hat."""
    u_hat = biot_savart(omega_hat, kx, ky, kz)
    S_hat = compute_strain_hat(u_hat, kx, ky, kz)

    norm_S = L3_norm(S_hat, N)
    norm_omega = L3_norm(omega_hat, N)

    if norm_omega < 1e-15:
        return 0.0

    return (norm_S / norm_omega).item()

def main():
    print(f"=" * 70)
    print(f"Sharp constant estimation: ||S||_3 <= C ||omega||_3 on T^3")
    print(f"Resolution N={N}, Samples={N_SAMPLES}")
    print(f"=" * 70)

    kx, ky, kz = make_wavenumbers(N)

    # ========== DIVERGENCE-FREE FIELDS ==========
    print(f"\n--- Divergence-free omega (Leray-projected) ---")
    t0 = time.time()

    ratios_divfree = []
    max_ratio_divfree = 0.0

    for i in range(N_SAMPLES):
        omega_hat = generate_divfree_omega_hat(N, kx, ky, kz)

        # Verify div-free: k . omega_hat should be ~0
        if i == 0:
            div_hat = kx * omega_hat[0] + ky * omega_hat[1] + kz * omega_hat[2]
            div_err = div_hat.abs().max().item()
            print(f"  Div-free check (sample 0): max |k . omega_hat| = {div_err:.2e}")

        ratio = compute_ratio(omega_hat, kx, ky, kz, N)
        ratios_divfree.append(ratio)
        if ratio > max_ratio_divfree:
            max_ratio_divfree = ratio

        if (i+1) % 200 == 0:
            print(f"  {i+1}/{N_SAMPLES}: current max ratio = {max_ratio_divfree:.6f}")

    t_divfree = time.time() - t0
    ratios_divfree = torch.tensor(ratios_divfree)

    print(f"\n  Time: {t_divfree:.1f}s")
    print(f"  Max  ratio: {ratios_divfree.max():.6f}")
    print(f"  Mean ratio: {ratios_divfree.mean():.6f}")
    print(f"  Std  ratio: {ratios_divfree.std():.6f}")
    print(f"  P99  ratio: {ratios_divfree.quantile(0.99):.6f}")
    print(f"  P999 ratio: {ratios_divfree.quantile(0.999):.6f}")

    # ========== GENERAL (UNCONSTRAINED) FIELDS ==========
    print(f"\n--- General omega (not div-free) ---")
    t0 = time.time()

    ratios_general = []
    max_ratio_general = 0.0

    for i in range(N_SAMPLES):
        omega_hat = generate_general_omega_hat(N)
        ratio = compute_ratio(omega_hat, kx, ky, kz, N)
        ratios_general.append(ratio)
        if ratio > max_ratio_general:
            max_ratio_general = ratio

        if (i+1) % 200 == 0:
            print(f"  {i+1}/{N_SAMPLES}: current max ratio = {max_ratio_general:.6f}")

    t_general = time.time() - t0
    ratios_general = torch.tensor(ratios_general)

    print(f"\n  Time: {t_general:.1f}s")
    print(f"  Max  ratio: {ratios_general.max():.6f}")
    print(f"  Mean ratio: {ratios_general.mean():.6f}")
    print(f"  Std  ratio: {ratios_general.std():.6f}")
    print(f"  P99  ratio: {ratios_general.quantile(0.99):.6f}")
    print(f"  P999 ratio: {ratios_general.quantile(0.999):.6f}")

    # ========== COMPARISON ==========
    print(f"\n{'=' * 70}")
    print(f"RESULTS SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Max ||S||_3 / ||omega||_3 (div-free):  {ratios_divfree.max():.6f}")
    print(f"  Max ||S||_3 / ||omega||_3 (general):   {ratios_general.max():.6f}")
    gap = ratios_general.max() - ratios_divfree.max()
    ratio_improvement = 1.0 - ratios_divfree.max() / ratios_general.max()
    print(f"  Gap (general - divfree):                {gap:.6f}")
    print(f"  Relative improvement:                   {ratio_improvement*100:.2f}%")

    if ratios_divfree.max() < ratios_general.max():
        print(f"\n  >>> DIV-FREE CONSTRAINT HELPS: max ratio is {ratio_improvement*100:.2f}% smaller")
        print(f"  >>> This is the 'epsilon' for the div-free improvement")
    else:
        print(f"\n  >>> NO IMPROVEMENT detected from div-free constraint at this resolution")

    # ========== THEORETICAL REFERENCE ==========
    print(f"\n--- Theoretical reference ---")
    print(f"  CZ operator S = sym(nabla) * (-Delta)^{{-1}} curl")
    print(f"  This is a composition of Riesz transforms: R_i R_j type")
    print(f"  On L^p (1 < p < inf), ||R_i R_j||_{{p->p}} ~ p*/(p-1) (Iwaniec-Martin)")
    print(f"  For p=3: ||R||_{{3->3}} <= 3* - 1 = 2 (Iwaniec conjecture)")
    print(f"  Our numerical estimate is for the COMPOSED operator, not individual Riesz transforms")
    print(f"  The strain involves (R_i R_j + R_j R_i)/2 applied to curl components")

    # Also try: what if we optimize over spectrally concentrated fields?
    print(f"\n--- Spectral concentration test (low-k fields) ---")
    max_ratio_lowk = 0.0
    for i in range(200):
        omega_hat = generate_divfree_omega_hat(N, kx, ky, kz)
        # Zero out high frequencies (keep only |k| <= 4)
        k_mag = torch.sqrt(kx**2 + ky**2 + kz**2)
        mask = (k_mag <= 4).float()
        omega_hat = omega_hat * mask.unsqueeze(0)
        ratio = compute_ratio(omega_hat, kx, ky, kz, N)
        if ratio > max_ratio_lowk:
            max_ratio_lowk = ratio

    max_ratio_highk = 0.0
    for i in range(200):
        omega_hat = generate_divfree_omega_hat(N, kx, ky, kz)
        k_mag = torch.sqrt(kx**2 + ky**2 + kz**2)
        mask = (k_mag >= 8).float()
        omega_hat = omega_hat * mask.unsqueeze(0)
        ratio = compute_ratio(omega_hat, kx, ky, kz, N)
        if ratio > max_ratio_highk:
            max_ratio_highk = ratio

    print(f"  Max ratio (div-free, |k| <= 4):   {max_ratio_lowk:.6f}")
    print(f"  Max ratio (div-free, |k| >= 8):   {max_ratio_highk:.6f}")
    print(f"  (CZ constants are frequency-independent on R^n,")
    print(f"   but periodic domain introduces edge effects)")

    print(f"\n{'=' * 70}")
    print(f"BOTTOM LINE")
    print(f"{'=' * 70}")
    C_divfree = ratios_divfree.max().item()
    C_general = ratios_general.max().item()
    print(f"  Estimated C (div-free):  {C_divfree:.4f}")
    print(f"  Estimated C (general):   {C_general:.4f}")
    if C_divfree < C_general:
        eps = C_general - C_divfree
        print(f"  epsilon = C_general - C_divfree = {eps:.4f}")
        print(f"  The div-free constraint provides a {ratio_improvement*100:.1f}% reduction in the operator norm.")
    print(f"{'=' * 70}")

if __name__ == '__main__':
    main()
