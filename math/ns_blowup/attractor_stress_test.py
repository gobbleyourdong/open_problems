"""
Attractor stress test: Is alpha always < |omega|/2 at the vorticity maximum?

At the grid point where |omega| is maximum, we measure:
  - r^2 = |omega|^2 / |S|^2  (attractor ratio, expecting ~4)
  - alpha / |omega|            (stretching rate / vorticity, must be < 0.5)
  - lambda_1 / |omega|         (max eigenvalue of S / vorticity)
  - Var / |omega|^2            (alignment variance)
  - Q / |omega|^2              (second invariant of velocity gradient)

Tests many ICs including adversarial ones (anti-parallel tubes, high-k modes).
All on 3D Euler (nu=0), N=32, T^3 periodic.

Usage:
    python attractor_stress_test.py [--device cpu|cuda]
"""

import torch
import numpy as np
import math
import time
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from ns3d_spectral import NS3DSpectral


# ============================================================
# Diagnostics at the vorticity maximum
# ============================================================

def compute_velocity_gradient_tensor(solver, wx_hat, wy_hat, wz_hat):
    """
    Compute full velocity gradient tensor A_ij = du_i/dx_j in physical space.
    Returns 9 fields (N,N,N) each.
    """
    ux_hat, uy_hat, uz_hat = solver.velocity_from_vorticity(wx_hat, wy_hat, wz_hat)

    I = 1j
    # du_i / dx_j  (i=row, j=col)
    A = {}
    for i, u_hat in enumerate([ux_hat, uy_hat, uz_hat]):
        for j, k_comp in enumerate([solver.kx, solver.ky, solver.kz]):
            A[(i, j)] = solver.ifft(I * k_comp * solver.dealias_field(u_hat))

    return A


def diagnostics_at_omega_max(solver, wx_hat, wy_hat, wz_hat):
    """
    At the grid point where |omega| is maximum, compute:
      - |omega|
      - |S|^2  (Frobenius norm squared of strain rate tensor)
      - alpha   (vortex stretching rate = omega_hat . S . omega_hat)
      - lambda_1 (max eigenvalue of S)
      - Var     (alignment variance)
      - Q       (second invariant = (|omega|^2 - 2|S|^2) / 4)
    """
    # Vorticity in physical space
    wx = solver.ifft(solver.dealias_field(wx_hat))
    wy = solver.ifft(solver.dealias_field(wy_hat))
    wz = solver.ifft(solver.dealias_field(wz_hat))

    omega_mag_sq = wx**2 + wy**2 + wz**2
    omega_mag = omega_mag_sq.sqrt()

    # Find the maximum point
    flat_idx = omega_mag.argmax()
    idx = np.unravel_index(flat_idx.cpu().item(), omega_mag.shape)

    omega_val = omega_mag[idx].item()
    if omega_val < 1e-12:
        return None  # degenerate

    # Vorticity unit vector at max point
    w_vec = torch.tensor([wx[idx].item(), wy[idx].item(), wz[idx].item()], dtype=torch.float64)
    w_hat = w_vec / omega_val

    # Velocity gradient tensor at max point
    A = compute_velocity_gradient_tensor(solver, wx_hat, wy_hat, wz_hat)
    A_mat = torch.zeros(3, 3, dtype=torch.float64)
    for i in range(3):
        for j in range(3):
            A_mat[i, j] = A[(i, j)][idx].item()

    # Strain rate tensor S = (A + A^T) / 2
    S = 0.5 * (A_mat + A_mat.T)

    # |S|^2 (Frobenius)
    S_sq = (S * S).sum().item()

    # Stretching rate: alpha = w_hat . S . w_hat
    alpha = (w_hat @ S @ w_hat).item()

    # Eigenvalues of S
    eigvals = torch.linalg.eigvalsh(S)
    lambda_1 = eigvals[-1].item()  # max eigenvalue

    # Q = (|omega|^2 - 2|S|^2) / 4
    Q = (omega_val**2 - 2 * S_sq) / 4.0

    # Alignment variance: Var = sum_i (lambda_i - alpha)^2 * cos^2(theta_i)
    # where theta_i is angle between eigenvector i and omega_hat
    eigvals_full, eigvecs = torch.linalg.eigh(S)
    cos_sq = (eigvecs.T @ w_hat) ** 2  # cos^2(theta_i) for each eigenvector
    var_alignment = ((eigvals_full - alpha) ** 2 * cos_sq).sum().item()

    # r^2 = |omega|^2 / |S|^2
    r_sq = omega_val**2 / max(S_sq, 1e-30)

    return {
        'omega': omega_val,
        'S_sq': S_sq,
        'r_sq': r_sq,
        'alpha': alpha,
        'alpha_over_omega': alpha / omega_val,
        'lambda1': lambda_1,
        'lambda1_over_omega': lambda_1 / omega_val,
        'var': var_alignment,
        'var_over_omega_sq': var_alignment / (omega_val**2),
        'Q': Q,
        'Q_over_omega_sq': Q / (omega_val**2),
    }


# ============================================================
# Initial conditions
# ============================================================

def ic_taylor_green(solver):
    """Taylor-Green vortex."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    ux = torch.cos(X) * torch.sin(Y) * torch.cos(Z)
    uy = -torch.sin(X) * torch.cos(Y) * torch.cos(Z)
    uz = torch.zeros_like(X)
    ux_hat = solver.fft(ux)
    uy_hat = solver.fft(uy)
    uz_hat = solver.fft(uz)
    return solver.curl(ux_hat, uy_hat, uz_hat)


def ic_kida_pelz(solver):
    """Kida-Pelz high-symmetry IC."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    ux = torch.sin(X) * (torch.cos(3*Y) * torch.cos(Z) - torch.cos(Y) * torch.cos(3*Z))
    uy = torch.sin(Y) * (torch.cos(3*Z) * torch.cos(X) - torch.cos(Z) * torch.cos(3*X))
    uz = torch.sin(Z) * (torch.cos(3*X) * torch.cos(Y) - torch.cos(X) * torch.cos(3*Y))
    ux_hat = solver.fft(ux)
    uy_hat = solver.fft(uy)
    uz_hat = solver.fft(uz)
    return solver.curl(ux_hat, uy_hat, uz_hat)


def ic_random_divfree(solver, seed=42):
    """Random divergence-free field via curl of random potential."""
    torch.manual_seed(seed)
    N = solver.N
    dev = solver.device
    dt = solver.dtype

    # Random smooth potential in Fourier
    Ax_hat = torch.zeros(N, N, N, device=dev, dtype=torch.complex128)
    Ay_hat = torch.zeros_like(Ax_hat)
    Az_hat = torch.zeros_like(Ax_hat)

    k_max = 4
    for i in range(-k_max, k_max + 1):
        for j in range(-k_max, k_max + 1):
            for k in range(-k_max, k_max + 1):
                ksq = i*i + j*j + k*k
                if ksq == 0 or ksq > k_max**2:
                    continue
                mag = 3.0 / ksq
                ii, jj, kk = i % N, j % N, k % N
                Ax_hat[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).to(dev).item()
                Ay_hat[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).to(dev).item()
                Az_hat[ii,jj,kk] += mag * (torch.randn(1) + 1j*torch.randn(1)).to(dev).item()

    I = 1j
    ux_hat = I * solver.ky * Az_hat - I * solver.kz * Ay_hat
    uy_hat = I * solver.kz * Ax_hat - I * solver.kx * Az_hat
    uz_hat = I * solver.kx * Ay_hat - I * solver.ky * Ax_hat

    wx_hat, wy_hat, wz_hat = solver.curl(ux_hat, uy_hat, uz_hat)
    return solver.dealias_field(wx_hat), solver.dealias_field(wy_hat), solver.dealias_field(wz_hat)


def ic_trefoil_knot(solver, amp=10.0, core_width=0.4):
    """Trefoil knotted vortex tube."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    wx = torch.zeros_like(X)
    wy = torch.zeros_like(X)
    wz = torch.zeros_like(X)

    n_pts = 200
    s = torch.linspace(0, 2*pi, n_pts, device=solver.device, dtype=solver.dtype)
    ds = 2*pi / n_pts

    cx = (torch.sin(s) + 2*torch.sin(2*s)) * 0.5 + pi
    cy = (torch.cos(s) - 2*torch.cos(2*s)) * 0.5 + pi
    cz = (-torch.sin(3*s)) * 0.5 + pi

    tx = torch.cos(s) + 4*torch.cos(2*s)
    ty = -torch.sin(s) + 4*torch.sin(2*s)
    tz = -3*torch.cos(3*s)

    sigma = core_width
    for i in range(n_pts):
        dist_sq = (X - cx[i])**2 + (Y - cy[i])**2 + (Z - cz[i])**2
        gaussian = amp * torch.exp(-dist_sq / (2*sigma**2)) * ds
        wx += gaussian * tx[i]
        wy += gaussian * ty[i]
        wz += gaussian * tz[i]

    return (solver.dealias_field(solver.fft(wx)),
            solver.dealias_field(solver.fft(wy)),
            solver.dealias_field(solver.fft(wz)))


def ic_anti_parallel_tubes(solver, sep=0.6, amp=8.0, core_width=0.25):
    """
    Anti-parallel vortex tubes — THE most adversarial IC for blowup.
    Two parallel tubes with opposite-sign vorticity, close together.
    The induced strain between them drives reconnection.
    """
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    # Two tubes along z-axis, separated in y, opposite circulation
    y1 = pi - sep / 2
    y2 = pi + sep / 2

    # Gaussian tubes
    r1_sq = (X - pi)**2 + (Y - y1)**2
    r2_sq = (X - pi)**2 + (Y - y2)**2
    sigma = core_width

    # Tube 1: +z vorticity, Tube 2: -z vorticity
    wz = amp * torch.exp(-r1_sq / (2*sigma**2)) - amp * torch.exp(-r2_sq / (2*sigma**2))
    wx = torch.zeros_like(X)
    wy = torch.zeros_like(X)

    # Add a perturbation to break translational symmetry along z
    # This triggers the Crow instability
    perturbation = 0.3 * amp * torch.sin(2*Z)
    wz = wz * (1.0 + 0.1 * torch.cos(2*Z))  # amplitude modulation
    # Cross-component perturbation (tilts tubes toward each other)
    wy = perturbation * (torch.exp(-r1_sq / (2*sigma**2)) + torch.exp(-r2_sq / (2*sigma**2)))

    return (solver.dealias_field(solver.fft(wx)),
            solver.dealias_field(solver.fft(wy)),
            solver.dealias_field(solver.fft(wz)))


def ic_single_fourier_mode(solver, k=1):
    """Single Fourier mode — simplest possible IC."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    # Beltrami wave: omega = k * u (eigenfunction of curl)
    ux = torch.cos(k*Y) + torch.sin(k*Z)
    uy = torch.sin(k*X) + torch.cos(k*Z)
    uz = torch.cos(k*X) + torch.sin(k*Y)

    ux_hat = solver.fft(ux)
    uy_hat = solver.fft(uy)
    uz_hat = solver.fft(uz)
    return solver.curl(ux_hat, uy_hat, uz_hat)


def ic_high_wavenumber(solver, k=4):
    """High-wavenumber ABC-like flow — small-scale vorticity."""
    X, Y, Z = solver.X, solver.Y, solver.Z
    A, B, C = 1.0, 0.9, 1.1  # slightly asymmetric
    ux = A * torch.sin(k*Z) + C * torch.cos(k*Y)
    uy = B * torch.sin(k*X) + A * torch.cos(k*Z)
    uz = C * torch.sin(k*Y) + B * torch.cos(k*X)

    ux_hat = solver.fft(ux)
    uy_hat = solver.fft(uy)
    uz_hat = solver.fft(uz)
    return solver.curl(ux_hat, uy_hat, uz_hat)


def ic_strain_dominated(solver, amp=5.0):
    """
    Strain-dominated IC — designed to have |S| >> |omega| initially.
    Pure strain field + tiny vorticity perturbation.
    This is the Vieillefosse-like adversarial case.
    """
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    # Velocity field with strong strain (hyperbolic flow pattern)
    # u = amp * (sin(x)cos(y), -cos(x)sin(y), 0) has strong strain
    # Plus a small-scale vorticity perturbation
    ux = amp * torch.sin(X) * torch.cos(Y) * torch.cos(Z)
    uy = -amp * torch.cos(X) * torch.sin(Y) * torch.cos(Z)
    uz = amp * 0.1 * torch.sin(3*X) * torch.sin(3*Y) * torch.sin(3*Z)  # small perturbation

    ux_hat = solver.fft(ux)
    uy_hat = solver.fft(uy)
    uz_hat = solver.fft(uz)

    # Project to div-free
    kdotu = solver.kx * ux_hat + solver.ky * uy_hat + solver.kz * uz_hat
    ux_hat -= solver.kx * kdotu / solver.ksq
    uy_hat -= solver.ky * kdotu / solver.ksq
    uz_hat -= solver.kz * kdotu / solver.ksq
    ux_hat[0,0,0] = 0; uy_hat[0,0,0] = 0; uz_hat[0,0,0] = 0

    return solver.curl(ux_hat, uy_hat, uz_hat)


def ic_anti_parallel_tight(solver, sep=0.35, amp=12.0, core_width=0.18):
    """
    Ultra-tight anti-parallel tubes — maximally adversarial.
    Tubes so close their cores almost overlap. Maximum induced strain.
    """
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi

    y1 = pi - sep / 2
    y2 = pi + sep / 2
    sigma = core_width

    r1_sq = (X - pi)**2 + (Y - y1)**2
    r2_sq = (X - pi)**2 + (Y - y2)**2

    wz = amp * torch.exp(-r1_sq / (2*sigma**2)) - amp * torch.exp(-r2_sq / (2*sigma**2))
    wx = torch.zeros_like(X)
    wy = torch.zeros_like(X)

    # Strong Crow-instability perturbation
    wy = 0.5 * amp * torch.sin(Z) * (torch.exp(-r1_sq / (2*sigma**2)) + torch.exp(-r2_sq / (2*sigma**2)))

    return (solver.dealias_field(solver.fft(wx)),
            solver.dealias_field(solver.fft(wy)),
            solver.dealias_field(solver.fft(wz)))


def ic_orthogonal_tubes(solver, amp=8.0, core_width=0.3):
    """
    Orthogonal vortex tubes — one along x, one along z, crossing.
    Generates strong strain at the intersection.
    """
    X, Y, Z = solver.X, solver.Y, solver.Z
    pi = math.pi
    sigma = core_width

    # Tube 1: along z-axis at (pi, pi)
    r1_sq = (X - pi)**2 + (Y - pi)**2
    wz1 = amp * torch.exp(-r1_sq / (2*sigma**2))

    # Tube 2: along x-axis at (pi, pi) in (y,z) plane
    r2_sq = (Y - pi)**2 + (Z - pi)**2
    wx2 = amp * torch.exp(-r2_sq / (2*sigma**2))

    wx = wx2
    wy = torch.zeros_like(X)
    wz = wz1

    return (solver.dealias_field(solver.fft(wx)),
            solver.dealias_field(solver.fft(wy)),
            solver.dealias_field(solver.fft(wz)))


# ============================================================
# Main stress test
# ============================================================

def run_ic(solver, name, wx_hat, wy_hat, wz_hat, t_final=2.0, diag_dt=0.01):
    """
    Evolve one IC to t_final, collecting diagnostics every ~diag_dt.
    Returns list of diagnostic dicts.
    """
    t = 0.0
    step = 0
    next_diag_t = 0.0
    all_diags = []
    max_steps = 200000  # safety

    while t < t_final and step < max_steps:
        dt = solver.compute_dt(wx_hat, wy_hat, wz_hat)
        dt = min(dt, t_final - t + 1e-15)

        # Collect diagnostics
        if t >= next_diag_t - 1e-10:
            d = diagnostics_at_omega_max(solver, wx_hat, wy_hat, wz_hat)
            if d is not None:
                d['t'] = t
                d['step'] = step
                all_diags.append(d)
            next_diag_t += diag_dt

        # Check for resolution issues
        omega = solver.omega_max(wx_hat, wy_hat, wz_hat)
        if omega > 1e6:
            print(f"    [{name}] WARNING: omega blowup at t={t:.4f}, step={step}")
            break
        spec = solver.spectral_ratio(wx_hat)
        if spec > 0.1:
            print(f"    [{name}] WARNING: under-resolved at t={t:.4f}, step={step}, spec={spec:.3e}")
            break

        # Step
        wx_hat, wy_hat, wz_hat = solver.step_rk4(wx_hat, wy_hat, wz_hat, dt)
        t += dt
        step += 1

    # Final diagnostic
    d = diagnostics_at_omega_max(solver, wx_hat, wy_hat, wz_hat)
    if d is not None:
        d['t'] = t
        d['step'] = step
        all_diags.append(d)

    return all_diags


def summarize(name, diags):
    """Summarize diagnostics for one IC."""
    if not diags:
        return {'name': name, 'status': 'NO DATA'}

    r_sq_vals = [d['r_sq'] for d in diags]
    alpha_norm = [d['alpha_over_omega'] for d in diags]
    lambda1_norm = [d['lambda1_over_omega'] for d in diags]
    q_norm = [d['Q_over_omega_sq'] for d in diags]
    var_norm = [d['var_over_omega_sq'] for d in diags]

    min_r_sq = min(r_sq_vals)
    max_alpha = max(alpha_norm)
    max_lambda1 = max(lambda1_norm)
    exceeds_445 = any(a > 0.445 for a in alpha_norm)
    exceeds_500 = any(a > 0.500 for a in alpha_norm)

    # Find the worst-case timestep
    worst_idx = alpha_norm.index(max_alpha)
    worst_t = diags[worst_idx]['t']

    return {
        'name': name,
        'n_steps': diags[-1]['step'],
        't_final': diags[-1]['t'],
        'min_r_sq': min_r_sq,
        'max_alpha_over_omega': max_alpha,
        'max_lambda1_over_omega': max_lambda1,
        'worst_t': worst_t,
        'exceeds_445': exceeds_445,
        'exceeds_500': exceeds_500,
        'max_var_norm': max(var_norm),
        'min_Q_norm': min(q_norm),
        'max_Q_norm': max(q_norm),
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Attractor stress test')
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument('--N', type=int, default=32)
    parser.add_argument('--t-final', type=float, default=2.0)
    args = parser.parse_args()

    device = args.device
    N = args.N
    t_final = args.t_final

    print("=" * 80)
    print("ATTRACTOR STRESS TEST: Is alpha < |omega|/2 at the vorticity maximum?")
    print("=" * 80)
    print(f"  N={N}, nu=0 (Euler), T^3 periodic, t_final={t_final}")
    print(f"  Device: {device}")
    print()

    # Build solver (nu=0 for Euler)
    solver = NS3DSpectral(N=N, nu=0.0, device=device)
    print()

    # Define all ICs
    ic_list = [
        ("Taylor-Green",       lambda s: ic_taylor_green(s)),
        ("Kida-Pelz",          lambda s: ic_kida_pelz(s)),
        ("Random seed=42",     lambda s: ic_random_divfree(s, seed=42)),
        ("Random seed=123",    lambda s: ic_random_divfree(s, seed=123)),
        ("Random seed=7",      lambda s: ic_random_divfree(s, seed=7)),
        ("Random seed=999",    lambda s: ic_random_divfree(s, seed=999)),
        ("Random seed=2025",   lambda s: ic_random_divfree(s, seed=2025)),
        ("Trefoil knot",       lambda s: ic_trefoil_knot(s)),
        ("Anti-parallel tubes",     lambda s: ic_anti_parallel_tubes(s)),
        ("Anti-parallel TIGHT",     lambda s: ic_anti_parallel_tight(s)),
        ("Orthogonal tubes",        lambda s: ic_orthogonal_tubes(s)),
        ("Single Fourier k=1",      lambda s: ic_single_fourier_mode(s, k=1)),
        ("High-k ABC k=4",          lambda s: ic_high_wavenumber(s, k=4)),
        ("High-k ABC k=8",          lambda s: ic_high_wavenumber(s, k=8)),
        ("Strain-dominated",        lambda s: ic_strain_dominated(s)),
    ]

    all_summaries = []
    t0_total = time.time()

    for ic_name, ic_func in ic_list:
        print(f"\n{'─'*60}")
        print(f"  IC: {ic_name}")
        print(f"{'─'*60}")

        t0 = time.time()
        wx_hat, wy_hat, wz_hat = ic_func(solver)

        omega0 = solver.omega_max(wx_hat, wy_hat, wz_hat)
        print(f"  |omega|_0 = {omega0:.4f}")

        diags = run_ic(solver, ic_name, wx_hat, wy_hat, wz_hat, t_final=t_final)
        elapsed = time.time() - t0

        summary = summarize(ic_name, diags)
        all_summaries.append(summary)

        flag_445 = " *** EXCEEDS 0.445 ***" if summary.get('exceeds_445') else ""
        flag_500 = " *** EXCEEDS 0.500 ***" if summary.get('exceeds_500') else ""

        print(f"  Completed: {summary.get('n_steps', '?')} steps, "
              f"t={summary.get('t_final', '?'):.3f}, {elapsed:.1f}s")
        print(f"  min(r^2) = {summary.get('min_r_sq', '?'):.4f}  "
              f"(r^2=4 means |S|^2 = |omega|^2/4)")
        print(f"  max(alpha/|omega|) = {summary.get('max_alpha_over_omega', '?'):.6f}  "
              f"at t={summary.get('worst_t', '?'):.3f}{flag_445}{flag_500}")
        print(f"  max(lambda1/|omega|) = {summary.get('max_lambda1_over_omega', '?'):.6f}")

    total_elapsed = time.time() - t0_total

    # ============================================================
    # Summary table
    # ============================================================
    print("\n\n" + "=" * 100)
    print("SUMMARY TABLE")
    print("=" * 100)
    print(f"{'IC':<28} {'min(r^2)':>10} {'max(a/w)':>10} {'max(l1/w)':>10} "
          f"{'worst_t':>8} {'a>0.445':>8} {'a>0.5':>6} {'steps':>7}")
    print("-" * 100)

    any_exceeds_445 = False
    any_exceeds_500 = False

    for s in all_summaries:
        if 'min_r_sq' not in s:
            print(f"{s['name']:<28} {'NO DATA':>10}")
            continue

        flag_445 = "YES" if s['exceeds_445'] else "no"
        flag_500 = "YES" if s['exceeds_500'] else "no"
        if s['exceeds_445']:
            any_exceeds_445 = True
        if s['exceeds_500']:
            any_exceeds_500 = True

        print(f"{s['name']:<28} {s['min_r_sq']:>10.4f} {s['max_alpha_over_omega']:>10.6f} "
              f"{s['max_lambda1_over_omega']:>10.6f} {s['worst_t']:>8.3f} "
              f"{flag_445:>8} {flag_500:>6} {s['n_steps']:>7}")

    print("-" * 100)

    # ============================================================
    # Verdict
    # ============================================================
    print("\n" + "=" * 80)
    print("VERDICT")
    print("=" * 80)

    global_max_alpha = max(s.get('max_alpha_over_omega', 0) for s in all_summaries)
    global_min_r_sq = min(s.get('min_r_sq', 999) for s in all_summaries)

    print(f"  Global max(alpha/|omega|) = {global_max_alpha:.6f}")
    print(f"  Global min(r^2)           = {global_min_r_sq:.4f}")
    print()

    if any_exceeds_500:
        print("  *** ATTRACTOR FAILS: alpha > |omega|/2 found. ***")
        print("  The bound |S|^2 < |omega|^2/4 is VIOLATED.")
    elif any_exceeds_445:
        print("  *** WARNING: alpha > 0.445|omega| found. ***")
        print("  The DMP cutoff is breached. Attractor may be marginal.")
    else:
        print("  ATTRACTOR HOLDS: alpha/|omega| never exceeds 0.445 across all ICs.")
        print(f"  Margin to DMP cutoff: {0.445 - global_max_alpha:.6f}")
        print(f"  Margin to |omega|/2:  {0.500 - global_max_alpha:.6f}")

    print()
    if global_min_r_sq > 3.5:
        print(f"  r^2 stays above {global_min_r_sq:.2f} (close to attractor value 4).")
    elif global_min_r_sq > 2.0:
        print(f"  r^2 dips to {global_min_r_sq:.2f} — strain is significant but bounded.")
    else:
        print(f"  r^2 dips to {global_min_r_sq:.2f} — strain-dominated regime detected!")

    print(f"\n  Total time: {total_elapsed:.0f}s for {len(ic_list)} ICs on {device}")
    print("=" * 80)


if __name__ == '__main__':
    main()
