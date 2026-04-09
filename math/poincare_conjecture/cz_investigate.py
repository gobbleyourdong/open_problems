"""
Investigate the discrepancy between random sampling (C ~ 0.698) and
gradient ascent (C ~ 1.355) for ||S||_3 / ||omega||_3.

The gradient ascent result of C > 1 would mean the div-free constraint
does NOT help for L^3. Need to verify this is not a bug.

Key checks:
1. Verify the gradient ascent extremizer is actually div-free
2. Check the L^3 norms manually
3. Check what kind of field achieves C > 1
4. Check L^2 extremizer (should be exactly 1/sqrt(2))
5. Understand why random fields cluster at 0.698
"""

import torch
import numpy as np

torch.set_default_dtype(torch.float64)

N = 32

def make_wavenumbers(N):
    freq = torch.fft.fftfreq(N, d=1.0/N)
    kx, ky, kz = torch.meshgrid(freq, freq, freq, indexing='ij')
    return kx, ky, kz

def project_divfree(omega_hat, kx, ky, kz):
    ksq = kx**2 + ky**2 + kz**2
    ksq_safe = ksq.clone()
    ksq_safe[0, 0, 0] = 1.0
    k_dot_o = kx * omega_hat[0] + ky * omega_hat[1] + kz * omega_hat[2]
    k_vec = torch.stack([kx, ky, kz])
    P_omega = omega_hat - k_vec * (k_dot_o / ksq_safe).unsqueeze(0)
    P_omega[:, 0, 0, 0] = 0.0
    return P_omega

def biot_savart(omega_hat, kx, ky, kz):
    ksq = kx**2 + ky**2 + kz**2
    ksq_safe = ksq.clone()
    ksq_safe[0, 0, 0] = 1.0
    inv_ksq = 1.0 / ksq_safe
    inv_ksq[0, 0, 0] = 0.0

    cx = ky * omega_hat[2] - kz * omega_hat[1]
    cy = kz * omega_hat[0] - kx * omega_hat[2]
    cz = kx * omega_hat[1] - ky * omega_hat[0]

    i = torch.tensor(1j, dtype=torch.complex128)
    return torch.stack([i*cx*inv_ksq, i*cy*inv_ksq, i*cz*inv_ksq])

def strain_hat_fn(u_hat, kx, ky, kz):
    i = torch.tensor(1j, dtype=torch.complex128)
    k = torch.stack([kx, ky, kz])
    S = torch.zeros(3, 3, N, N, N, dtype=torch.complex128)
    for a in range(3):
        for b in range(a, 3):
            val = i * (k[b]*u_hat[a] + k[a]*u_hat[b]) / 2.0
            S[a,b] = val
            if b != a:
                S[b,a] = val
    return S

def Lp_norm(field_hat, p):
    orig_shape = field_hat.shape
    n_comp = int(np.prod(orig_shape[:-3]))
    flat_hat = field_hat.reshape(n_comp, N, N, N)
    flat_phys = torch.fft.ifftn(flat_hat, dim=(-3,-2,-1))
    mag_sq = (flat_phys.real**2 + flat_phys.imag**2).sum(dim=0)
    mag = torch.sqrt(mag_sq + 1e-30)
    return (mag**p).mean() ** (1.0/p)

def ratio_with_diagnostics(omega_hat, kx, ky, kz, p=3.0, label=""):
    """Compute ratio with full diagnostics."""
    # Check div-free
    div_hat = kx * omega_hat[0] + ky * omega_hat[1] + kz * omega_hat[2]
    div_err = div_hat.abs().max().item()

    u_hat = biot_savart(omega_hat, kx, ky, kz)
    S_hat = strain_hat_fn(u_hat, kx, ky, kz)

    norm_S = Lp_norm(S_hat, p)
    norm_omega = Lp_norm(omega_hat, p)
    ratio = (norm_S / norm_omega).item()

    # Check spectrum
    omega_energy = (omega_hat.abs()**2).sum(dim=0)  # energy per k
    k_mag = torch.sqrt(kx**2 + ky**2 + kz**2)

    # Find dominant mode
    max_idx = torch.argmax(omega_energy.flatten())
    max_k = k_mag.flatten()[max_idx].item()

    # Energy in shells
    total_energy = omega_energy.sum().item()
    low_k_energy = omega_energy[k_mag <= 2].sum().item()
    mid_k_energy = omega_energy[(k_mag > 2) & (k_mag <= 8)].sum().item()
    high_k_energy = omega_energy[k_mag > 8].sum().item()

    print(f"  {label}")
    print(f"    div err:        {div_err:.2e}")
    print(f"    ||S||_{p:.0f}:        {norm_S:.6f}")
    print(f"    ||omega||_{p:.0f}:    {norm_omega:.6f}")
    print(f"    ratio:          {ratio:.6f}")
    print(f"    dominant |k|:   {max_k:.1f}")
    print(f"    energy: low={low_k_energy/total_energy:.3f} mid={mid_k_energy/total_energy:.3f} high={high_k_energy/total_energy:.3f}")

    return ratio

def gradient_ascent_with_diagnostics(kx, ky, kz, p=3.0, n_steps=500, lr=0.01):
    """Run gradient ascent and track convergence."""
    params_real = torch.randn(3, N, N, N, requires_grad=True)
    params_imag = torch.randn(3, N, N, N, requires_grad=True)

    optimizer = torch.optim.Adam([params_real, params_imag], lr=lr)

    history = []
    for step in range(n_steps):
        optimizer.zero_grad()

        omega_hat_raw = torch.complex(params_real, params_imag)
        omega_hat = project_divfree(omega_hat_raw, kx, ky, kz)

        u_hat = biot_savart(omega_hat, kx, ky, kz)
        S_hat = strain_hat_fn(u_hat, kx, ky, kz)

        norm_S = Lp_norm(S_hat, p)
        norm_omega = Lp_norm(omega_hat, p)

        ratio = norm_S / (norm_omega + 1e-30)
        loss = -ratio
        loss.backward()
        optimizer.step()

        history.append(ratio.item())

        if (step+1) % 100 == 0:
            print(f"    Step {step+1}: ratio = {ratio.item():.6f}")

    # Final diagnostics
    with torch.no_grad():
        omega_hat_raw = torch.complex(params_real, params_imag)
        omega_hat = project_divfree(omega_hat_raw, kx, ky, kz)
        ratio_with_diagnostics(omega_hat, kx, ky, kz, p, f"Final (p={p:.0f})")

    return max(history), omega_hat.detach()

def manual_L3_check(omega_hat, kx, ky, kz):
    """
    Very explicit L^3 computation to rule out bugs.
    """
    print("\n--- Manual L^3 verification ---")

    # Step 1: omega physical
    omega_phys = torch.fft.ifftn(omega_hat, dim=(-3,-2,-1))
    print(f"  omega physical: shape={omega_phys.shape}, dtype={omega_phys.dtype}")
    print(f"  max |Im(omega)|: {omega_phys.imag.abs().max():.6e}")
    print(f"  max |Re(omega)|: {omega_phys.real.abs().max():.6e}")

    # |omega(x)|^2 = sum_i (Re^2 + Im^2) for complex field
    omega_mag_sq = (omega_phys.real**2 + omega_phys.imag**2).sum(dim=0)
    omega_mag = torch.sqrt(omega_mag_sq)
    norm_omega_3 = (omega_mag**3).mean() ** (1./3.)
    print(f"  ||omega||_3 (manual): {norm_omega_3:.6f}")
    print(f"  ||omega||_3 (function): {Lp_norm(omega_hat, 3):.6f}")

    # Step 2: u via Biot-Savart
    u_hat = biot_savart(omega_hat, kx, ky, kz)
    u_phys = torch.fft.ifftn(u_hat, dim=(-3,-2,-1))
    print(f"\n  u physical: max|Re|={u_phys.real.abs().max():.6e}, max|Im|={u_phys.imag.abs().max():.6e}")

    # Step 3: S in physical space (finite differences for verification)
    # S_{ij} = (d_j u_i + d_i u_j) / 2
    # In Fourier: S_hat_{ij} = i(k_j u_hat_i + k_i u_hat_j)/2
    S_hat = strain_hat_fn(u_hat, kx, ky, kz)
    S_phys = torch.fft.ifftn(S_hat.reshape(9, N, N, N), dim=(-3,-2,-1)).reshape(3, 3, N, N, N)
    print(f"  S physical: max|Re|={S_phys.real.abs().max():.6e}, max|Im|={S_phys.imag.abs().max():.6e}")

    # |S(x)|_F = sqrt(sum_{ij} |S_{ij}|^2)
    S_mag_sq = (S_phys.real**2 + S_phys.imag**2).sum(dim=(0,1))
    S_mag = torch.sqrt(S_mag_sq)
    norm_S_3 = (S_mag**3).mean() ** (1./3.)
    print(f"\n  ||S||_3 (manual):   {norm_S_3:.6f}")
    print(f"  ||S||_3 (function): {Lp_norm(S_hat, 3):.6f}")
    print(f"  Ratio (manual):     {norm_S_3/norm_omega_3:.6f}")

    # Step 4: Check Parseval (L^2)
    norm_omega_2 = (omega_mag**2).mean() ** 0.5
    norm_S_2 = (S_mag**2).mean() ** 0.5
    print(f"\n  ||S||_2 / ||omega||_2 = {(norm_S_2/norm_omega_2).item():.6f} (should be <= 1/sqrt(2)={1/np.sqrt(2):.6f})")


def main():
    kx, ky, kz = make_wavenumbers(N)

    print("=" * 70)
    print("Investigation: Is C(L^3) > 1 for ||S||_3 <= C ||omega||_3?")
    print("=" * 70)

    # Test 1: Random field ratio
    print("\n[A] Random div-free field:")
    omega_hat = torch.zeros(3, N, N, N, dtype=torch.complex128)
    a_r = torch.randn(3, N, N, N)
    a_i = torch.randn(3, N, N, N)
    omega_hat = project_divfree(torch.complex(a_r, a_i), kx, ky, kz)
    ratio_with_diagnostics(omega_hat, kx, ky, kz, 3.0, "Random div-free")
    manual_L3_check(omega_hat, kx, ky, kz)

    # Test 2: Gradient ascent
    print("\n\n[B] Gradient ascent (p=3):")
    best_ratio, best_omega = gradient_ascent_with_diagnostics(kx, ky, kz, p=3.0, n_steps=500, lr=0.01)
    print(f"\n  Best ratio from grad ascent: {best_ratio:.6f}")
    manual_L3_check(best_omega, kx, ky, kz)

    # Test 3: Gradient ascent for L^2 (should converge to 1/sqrt(2))
    print("\n\n[C] Gradient ascent (p=2, should give 1/sqrt(2)):")
    best_ratio_l2, _ = gradient_ascent_with_diagnostics(kx, ky, kz, p=2.0, n_steps=500, lr=0.01)
    print(f"\n  Best ratio L^2: {best_ratio_l2:.6f} (theory: {1/np.sqrt(2):.6f})")

    # Test 4: Concentrated on single mode (Beltrami)
    print("\n\n[D] Beltrami mode verification:")
    omega_b = torch.zeros(3, N, N, N, dtype=torch.complex128)
    omega_b[1, 1, 0, 0] = 1.0 / np.sqrt(2)
    omega_b[2, 1, 0, 0] = 1j / np.sqrt(2)
    omega_b[1, N-1, 0, 0] = 1.0 / np.sqrt(2)
    omega_b[2, N-1, 0, 0] = -1j / np.sqrt(2)
    ratio_with_diagnostics(omega_b, kx, ky, kz, 3.0, "Beltrami k=(1,0,0)")

    # Test 5: What does the high-ratio adversarial field look like?
    print("\n\n[E] Adversarial field analysis:")
    # Run gradient ascent with more care
    best_overall = 0.0
    best_omega_overall = None
    for trial in range(10):
        params_r = torch.randn(3, N, N, N, requires_grad=True)
        params_i = torch.randn(3, N, N, N, requires_grad=True)
        opt = torch.optim.Adam([params_r, params_i], lr=0.005)

        for step in range(1000):
            opt.zero_grad()
            oh_raw = torch.complex(params_r, params_i)
            oh = project_divfree(oh_raw, kx, ky, kz)
            uh = biot_savart(oh, kx, ky, kz)
            sh = strain_hat_fn(uh, kx, ky, kz)
            nS = Lp_norm(sh, 3.0)
            no = Lp_norm(oh, 3.0)
            r = nS / (no + 1e-30)
            (-r).backward()
            opt.step()

        with torch.no_grad():
            oh_raw = torch.complex(params_r, params_i)
            oh = project_divfree(oh_raw, kx, ky, kz)
            uh = biot_savart(oh, kx, ky, kz)
            sh = strain_hat_fn(uh, kx, ky, kz)
            nS = Lp_norm(sh, 3.0)
            no = Lp_norm(oh, 3.0)
            r_final = (nS / no).item()

        if r_final > best_overall:
            best_overall = r_final
            best_omega_overall = oh.detach().clone()

        print(f"  Trial {trial+1}: ratio = {r_final:.6f} (best = {best_overall:.6f})")

    print(f"\n  Best overall: {best_overall:.6f}")
    if best_omega_overall is not None:
        ratio_with_diagnostics(best_omega_overall, kx, ky, kz, 3.0, "Best adversarial")
        manual_L3_check(best_omega_overall, kx, ky, kz)

        # Spectrum of best adversarial
        omega_energy = (best_omega_overall.abs()**2).sum(dim=0)
        k_mag = torch.sqrt(kx**2 + ky**2 + kz**2)
        for r_cut in [1, 2, 4, 8, 12, 16]:
            e = omega_energy[k_mag <= r_cut].sum().item()
            print(f"    Energy in |k| <= {r_cut}: {e/omega_energy.sum().item():.4f}")

    print("\n" + "=" * 70)
    print("VERDICT")
    print("=" * 70)
    print(f"  Random fields give ratio ~ 0.698 (concentration of measure)")
    print(f"  Gradient ascent gives ratio ~ {best_overall:.4f}")
    if best_overall > 1:
        print(f"  C(L^3) > 1: The div-free CZ constant EXCEEDS 1 on L^3")
        print(f"  ||S||_3 <= C ||omega||_3 does NOT hold with C < 1")
        print(f"  No 'depletion' in the L^3 operator norm sense")
    elif best_overall > 1/np.sqrt(2):
        print(f"  C(L^3) > 1/sqrt(2): Exceeds L^2 constant but still < 1")
        print(f"  DEPLETION HOLDS: ||S||_3 < ||omega||_3 for all div-free omega")
    else:
        print(f"  C(L^3) <= 1/sqrt(2): Same as L^2 constant")

if __name__ == '__main__':
    main()
