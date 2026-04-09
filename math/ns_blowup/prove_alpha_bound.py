"""
BARRIER ARGUMENT for alpha < |omega|/2 at the vorticity maximum.

Approach: measure the empirical relationship between alpha/|omega| and
Q = Var - H_ww (where Var = S^2_ee - alpha^2) across the full grid and
at the max-|omega| point.

Key identity at the max of |omega|:
  D(alpha/|omega|)/Dt = (Dalpha - alpha^2) / |omega|
                      = (Var - Hww) / |omega| - alpha^2/|omega|
  Wait — more carefully:
    Dalpha = S^2_ee - 2*alpha^2 - Hww  (Euler, inviscid, at max where O2ee=0)
    D|omega|/Dt = alpha * |omega|  (at the max)
    D(alpha/|omega|)/Dt = Dalpha/|omega| - alpha * (D|omega|/Dt)/|omega|^2
                        = Dalpha/|omega| - alpha^2/|omega|
                        = (Dalpha - alpha^2)/|omega|
                        = (S^2_ee - 3*alpha^2 - Hww)/|omega|

  Define R = alpha/|omega|. Then:
    DR/Dt = (Var - Hww - alpha^2)/|omega| = (S^2_ee - 3*alpha^2 - Hww)/|omega|

  For the barrier at R = beta: is DR/Dt < 0 when R = beta?
  This requires: S^2_ee - 3*alpha^2 < Hww  when alpha/|omega| = beta.

ACTUAL APPROACH (more direct):
  Just measure Q = Var - Hww and Dalpha = S^2_ee - 2*alpha^2 - Hww
  as a function of alpha/|omega| across:
  (a) ALL grid points (2D histogram)
  (b) The max-|omega| point over time

  Also measure the barrier function quantity:
    B = S^2_ee - 3*alpha^2 - Hww
  which controls D(alpha/|omega|)/Dt.

This is a MEASUREMENT script — empirical data to guide the proof.
"""
import torch
import numpy as np
import math
import time
import os

DTYPE = torch.float64
pi = math.pi


# ============================================================
# Compact 3D Euler solver (inviscid, periodic, spectral)
# ============================================================
class NS3D:
    def __init__(s, N=32, nu=0.):
        s.N = N; s.nu = nu; s.Lx = 2*pi; dx = s.Lx / N
        x = torch.linspace(0, s.Lx - dx, N, dtype=DTYPE)
        s.X, s.Y, s.Z = torch.meshgrid(x, x, x, indexing='ij')
        k = torch.fft.fftfreq(N, d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx, s.ky, s.kz = torch.meshgrid(k, k, k, indexing='ij')
        s.ksq = s.kx**2 + s.ky**2 + s.kz**2; s.ksq[0,0,0] = 1
        s.D = ((s.kx.abs() < N//3) & (s.ky.abs() < N//3) & (s.kz.abs() < N//3)).to(DTYPE)
        s.dx = dx

    def fft(s, f): return torch.fft.fftn(f)
    def ifft(s, f): return torch.fft.ifftn(f).real

    def curl(s, a, b, c):
        I = 1j
        return (I*s.ky*c - I*s.kz*b, I*s.kz*a - I*s.kx*c, I*s.kx*b - I*s.ky*a)

    def vel(s, a, b, c):
        p = a/s.ksq; q = b/s.ksq; r = c/s.ksq
        p[0,0,0] = 0; q[0,0,0] = 0; r[0,0,0] = 0
        I = 1j
        return (I*s.ky*r - I*s.kz*q, I*s.kz*p - I*s.kx*r, I*s.kx*q - I*s.ky*p)

    def rhs(s, w):
        D = s.D; u = s.vel(*w); f = {}
        for n, h in zip(['ux','uy','uz','wx','wy','wz'], [*u, *w]):
            f[n] = s.ifft(D*h)
            for d, kd in zip('xyz', [s.kx, s.ky, s.kz]):
                f[f'd{n}_d{d}'] = s.ifft(1j*kd*D*h)
        r = []
        for c in 'xyz':
            st = f['wx']*f[f'du{c}_dx'] + f['wy']*f[f'du{c}_dy'] + f['wz']*f[f'du{c}_dz']
            ad = f['ux']*f[f'dw{c}_dx'] + f['uy']*f[f'dw{c}_dy'] + f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st - ad) - s.nu*s.ksq*w['xyz'.index(c)])
        return tuple(r)

    def step(s, w, dt):
        def add(a, b, c): return tuple(a[i] + c*b[i] for i in range(3))
        k1 = s.rhs(w)
        k2 = s.rhs(add(w, k1, .5*dt))
        k3 = s.rhs(add(w, k2, .5*dt))
        k4 = s.rhs(add(w, k3, dt))
        return tuple(s.D*(w[i] + dt/6*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])) for i in range(3))

    def compute_dt(s, w):
        u_h = s.vel(*w)
        ux = s.ifft(u_h[0]); uy = s.ifft(u_h[1]); uz = s.ifft(u_h[2])
        u_max = max(ux.abs().max().item(), uy.abs().max().item(), uz.abs().max().item())
        if u_max < 1e-10: return 1e-3
        return min(0.5 * s.dx / u_max, 0.01)


# ============================================================
# Full-field diagnostic computation
# ============================================================
def compute_all_fields(s, w):
    """
    At EVERY grid point, compute:
      |omega|, alpha, Var, Hww, Q, Dalpha, alpha/|omega|
    Returns flat arrays (filtered for |omega| > threshold).
    Also returns max-point diagnostics separately.
    """
    D = s.D; N = s.N; kd = [s.kx, s.ky, s.kz]
    u_h = s.vel(*w)

    # Velocity gradient tensor A_ij = du_i/dx_j
    A = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            A[i,j] = s.ifft(1j*kd[j]*D*u_h[i])

    S = 0.5 * (A + A.transpose(0, 1))  # strain

    # Pressure Hessian
    source = torch.zeros(N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            source -= A[i,j] * A[j,i]
    p_hat = -s.fft(source) / s.ksq; p_hat[0,0,0] = 0
    H = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            H[i,j] = s.ifft(-kd[i]*kd[j]*p_hat)

    # Vorticity in physical space
    wf = [s.ifft(D*w[i]) for i in range(3)]
    om_sq = wf[0]**2 + wf[1]**2 + wf[2]**2
    om = om_sq.sqrt()

    # alpha = (w^T S w) / |w|^2
    alpha_f = torch.zeros(N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            alpha_f += wf[i] * S[i,j] * wf[j]
    alpha_f = alpha_f / (om_sq + 1e-30)

    # S^2_ee = |S . ehat|^2 = (w^T S^2 w) / |w|^2
    S2ee_f = torch.zeros(N, N, N, dtype=DTYPE)
    for i in range(3):
        Si_w = torch.zeros(N, N, N, dtype=DTYPE)
        for j in range(3):
            Si_w += S[i,j] * wf[j]
        S2ee_f += Si_w**2
    S2ee_f = S2ee_f / (om_sq + 1e-30)

    # Hww = (w^T H w) / |w|^2
    Hww_f = torch.zeros(N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            Hww_f += wf[i] * H[i,j] * wf[j]
    Hww_f = Hww_f / (om_sq + 1e-30)

    # Var = S^2_ee - alpha^2
    Var_f = S2ee_f - alpha_f**2

    # Q = Var - Hww
    Q_f = Var_f - Hww_f

    # Dalpha/Dt = S^2_ee - 2*alpha^2 - Hww (at max, where Omega^2_ee = 0 approx)
    Dalpha_f = S2ee_f - 2*alpha_f**2 - Hww_f

    # Barrier function: B = S^2_ee - 3*alpha^2 - Hww = D(alpha/|omega|)/Dt * |omega|
    B_f = S2ee_f - 3*alpha_f**2 - Hww_f

    # alpha / |omega|
    R_f = alpha_f / (om + 1e-30)

    # |S| = sqrt(S_ij S_ij)
    S_norm_f = torch.zeros(N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            S_norm_f += S[i,j]**2
    S_norm_f = S_norm_f.sqrt()

    # Max-point diagnostics
    flat = om.flatten()
    idx = flat.argmax().item()
    iz = idx % N; iy = (idx // N) % N; ix = idx // (N*N)

    max_pt = {
        'om': om[ix,iy,iz].item(),
        'alpha': alpha_f[ix,iy,iz].item(),
        'Var': Var_f[ix,iy,iz].item(),
        'Hww': Hww_f[ix,iy,iz].item(),
        'Q': Q_f[ix,iy,iz].item(),
        'Dalpha': Dalpha_f[ix,iy,iz].item(),
        'B': B_f[ix,iy,iz].item(),
        'S2ee': S2ee_f[ix,iy,iz].item(),
        'R': R_f[ix,iy,iz].item(),
        'S_norm': S_norm_f[ix,iy,iz].item(),
    }

    # Filter for |omega| > threshold (say 5% of max)
    om_max = om.max().item()
    threshold = max(0.5, 0.05 * om_max)
    mask = om > threshold

    grid = {
        'om': om[mask].numpy(),
        'alpha': alpha_f[mask].numpy(),
        'Var': Var_f[mask].numpy(),
        'Hww': Hww_f[mask].numpy(),
        'Q': Q_f[mask].numpy(),
        'Dalpha': Dalpha_f[mask].numpy(),
        'B': B_f[mask].numpy(),
        'R': R_f[mask].numpy(),
        'S2ee': S2ee_f[mask].numpy(),
        'S_norm': S_norm_f[mask].numpy(),
    }

    return max_pt, grid


# ============================================================
# Initial conditions
# ============================================================
def make_ic(s, name, seed=None):
    X, Y, Z = s.X, s.Y, s.Z
    if name == 'TG':
        ux = torch.cos(X)*torch.sin(Y)*torch.cos(Z)
        uy = -torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        return s.curl(s.fft(ux), s.fft(uy), s.fft(torch.zeros_like(X)))

    elif name == 'KP':
        ux = torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z) - torch.cos(Y)*torch.cos(3*Z))
        uy = torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X) - torch.cos(Z)*torch.cos(3*X))
        uz = torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y) - torch.cos(X)*torch.cos(3*Y))
        return s.curl(s.fft(ux), s.fft(uy), s.fft(uz))

    elif name == 'trefoil':
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        tp = torch.linspace(0, 2*pi, 200, dtype=DTYPE)
        cx = (torch.sin(tp) + 2*torch.sin(2*tp))*0.5 + pi
        cy = (torch.cos(tp) - 2*torch.cos(2*tp))*0.5 + pi
        cz = (-torch.sin(3*tp))*0.5 + pi
        tx = torch.cos(tp) + 4*torch.cos(2*tp)
        ty = -torch.sin(tp) + 4*torch.sin(2*tp)
        tz = -3*torch.cos(3*tp)
        ds = 2*pi/200
        for i in range(200):
            g = 10.*torch.exp(-((X-cx[i])**2 + (Y-cy[i])**2 + (Z-cz[i])**2)/(2*0.3**2))*ds
            wx += g*tx[i]; wy += g*ty[i]; wz += g*tz[i]
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    elif name == 'thin_trefoil':
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        tp = torch.linspace(0, 2*pi, 200, dtype=DTYPE)
        cx = (torch.sin(tp) + 2*torch.sin(2*tp))*0.5 + pi
        cy = (torch.cos(tp) - 2*torch.cos(2*tp))*0.5 + pi
        cz = (-torch.sin(3*tp))*0.5 + pi
        tx = torch.cos(tp) + 4*torch.cos(2*tp)
        ty = -torch.sin(tp) + 4*torch.sin(2*tp)
        tz = -3*torch.cos(3*tp)
        ds = 2*pi/200; sigma = 0.15; amp = 40.
        for i in range(200):
            g = amp*torch.exp(-((X-cx[i])**2 + (Y-cy[i])**2 + (Z-cz[i])**2)/(2*sigma**2))*ds
            wx += g*tx[i]; wy += g*ty[i]; wz += g*tz[i]
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    elif name == 'antiparallel':
        # Two antiparallel vortex tubes — classic reconnection setup
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        sigma = 0.3; amp = 8.0
        # Tube 1: along z at (pi-0.5, pi), positive z-vorticity
        r1_sq = (X - (pi - 0.5))**2 + (Y - pi)**2
        wz += amp * torch.exp(-r1_sq / (2*sigma**2))
        # Tube 2: along z at (pi+0.5, pi), negative z-vorticity
        r2_sq = (X - (pi + 0.5))**2 + (Y - pi)**2
        wz -= amp * torch.exp(-r2_sq / (2*sigma**2))
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    elif name.startswith('random'):
        if seed is not None:
            torch.manual_seed(seed)
        N = s.N
        wx_hat = torch.zeros(N, N, N, dtype=torch.complex128)
        wy_hat = torch.zeros_like(wx_hat)
        wz_hat = torch.zeros_like(wx_hat)
        k_max = 4; amp = 5.0
        for i in range(-k_max, k_max+1):
            for j in range(-k_max, k_max+1):
                for k in range(-k_max, k_max+1):
                    ksq = i*i + j*j + k*k
                    if ksq == 0 or ksq > k_max**2: continue
                    mag = amp / ksq
                    ii, jj, kk = i % N, j % N, k % N
                    wx_hat[ii,jj,kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
                    wy_hat[ii,jj,kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
                    wz_hat[ii,jj,kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
        # Project to divergence-free
        kdotw = s.kx*wx_hat + s.ky*wy_hat + s.kz*wz_hat
        wx_hat -= s.kx * kdotw / s.ksq
        wy_hat -= s.ky * kdotw / s.ksq
        wz_hat -= s.kz * kdotw / s.ksq
        wx_hat[0,0,0] = 0; wy_hat[0,0,0] = 0; wz_hat[0,0,0] = 0
        return (s.D*wx_hat, s.D*wy_hat, s.D*wz_hat)

    elif name == 'colliding_rings':
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        R = 0.8; sep = 1.5; amp = 5.0; sigma = 0.2
        for sign in [+1, -1]:
            z0 = pi + sign * sep
            rho = torch.sqrt((X - pi)**2 + (Y - pi)**2)
            core_dist = torch.sqrt((rho - R)**2 + (Z - z0)**2)
            strength = amp * torch.exp(-core_dist**2 / (2*sigma**2))
            theta_x = -(Y - pi) / (rho + 1e-10)
            theta_y = (X - pi) / (rho + 1e-10)
            wx += sign * strength * theta_x
            wy += sign * strength * theta_y
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    elif name == 'high_strain':
        # Designed for high strain: superposition of orthogonal vortices
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        amp = 8.0; sigma = 0.3
        # Cross-oriented tubes
        r1 = (Y - pi)**2 + (Z - pi)**2
        wx += amp * torch.exp(-r1 / (2*sigma**2))
        r2 = (X - pi)**2 + (Z - pi)**2
        wy += amp * torch.exp(-r2 / (2*sigma**2))
        r3 = (X - pi)**2 + (Y - pi)**2
        wz += amp * torch.exp(-r3 / (2*sigma**2))
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    else:
        raise ValueError(f"Unknown IC: {name}")


# ============================================================
# Main measurement
# ============================================================
def main():
    N = 32
    dt_base = 1e-4
    t0 = time.time()

    print("=" * 80, flush=True)
    print("BARRIER ARGUMENT: alpha/|omega| measurement", flush=True)
    print("  At every grid point and at the max-|omega| point:", flush=True)
    print("  Q = Var - Hww, Dalpha, B = S2ee - 3*alpha^2 - Hww", flush=True)
    print("  B < 0 => D(alpha/|omega|)/Dt < 0 => barrier holds", flush=True)
    print("=" * 80, flush=True)

    # ICs to test
    ic_configs = [
        ('TG',              0.5, 2.0, None),
        ('KP',              0.05, 0.6, None),
        ('trefoil',         0.01, 0.3, None),
        ('thin_trefoil',    0.005, 0.15, None),
        ('antiparallel',    0.02, 0.3, None),
        ('random_1',        0.05, 0.5, 42),
        ('random_2',        0.05, 0.5, 137),
        ('random_3',        0.05, 0.5, 2024),
        ('random_4',        0.05, 0.5, 7777),
        ('random_5',        0.05, 0.5, 31415),
        ('colliding_rings', 0.02, 0.3, None),
        ('high_strain',     0.01, 0.2, None),
    ]

    # ========== ACCUMULATORS ==========
    # Grid-level histogram bins for R = alpha/|omega|
    R_bins = np.linspace(-0.5, 0.5, 101)
    R_centers = 0.5*(R_bins[:-1] + R_bins[1:])
    n_bins = len(R_centers)

    # For each R bin: count Q<0, total, sum(Q/|omega|^2), sum(B/|omega|^2)
    grid_Q_neg = np.zeros(n_bins)
    grid_Q_total = np.zeros(n_bins)
    grid_B_neg = np.zeros(n_bins)
    grid_B_total = np.zeros(n_bins)
    grid_Q_sum = np.zeros(n_bins)
    grid_B_sum = np.zeros(n_bins)

    # Max-point track
    max_track = []  # list of dicts per IC

    # Scatter data for max point
    scatter_R = []
    scatter_Var_norm = []
    scatter_Hww_norm = []
    scatter_Q_norm = []
    scatter_B_norm = []
    scatter_ic = []

    total_grid_pts = 0

    for ic_name, t_start, t_end, seed in ic_configs:
        print(f"\n{'='*60}", flush=True)
        name_for_ic = ic_name.split('_')[0] if ic_name.startswith('random') else ic_name
        print(f"  IC: {ic_name}  t=[{t_start}, {t_end}]", flush=True)

        s = NS3D(N, 0.)
        w = make_ic(s, ic_name, seed=seed)

        # Evolve to t_start
        t = 0.0
        while t < t_start - 1e-15:
            dt = min(s.compute_dt(w), t_start - t, 0.002)
            w = s.step(w, dt); t += dt

        wf_check = [s.ifft(s.D*w[i]) for i in range(3)]
        om_check = (wf_check[0]**2 + wf_check[1]**2 + wf_check[2]**2).sqrt().max().item()
        if om_check < 0.1:
            print(f"  SKIP: |omega|_max = {om_check:.4f} too small", flush=True)
            continue

        # Number of diagnostics per IC: ~100 timesteps
        n_diag = 100
        diag_dt = (t_end - t_start) / n_diag

        ic_max_track = []
        print(f"  {'t':>6s}  {'|om|':>7s}  {'alpha':>7s}  {'R=a/|o|':>8s}  "
              f"{'Var':>8s}  {'Hww':>8s}  {'Q':>8s}  {'B':>8s}  "
              f"{'Q<0':>4s}  {'B<0':>4s}", flush=True)

        diag_count = 0
        for step_i in range(n_diag):
            # Advance one diagnostic interval
            t_target = min(t + diag_dt, t_end)
            while t < t_target - 1e-15:
                dt = min(s.compute_dt(w), t_target - t, 0.002)
                if dt < 1e-15: break
                w = s.step(w, dt); t += dt

            # Compute diagnostics
            max_pt, grid = compute_all_fields(s, w)

            if max_pt['om'] < 0.1:
                continue

            diag_count += 1
            ic_max_track.append({'t': t, **max_pt})

            # Scatter data at max point (normalized by |omega|^2)
            om2 = max_pt['om']**2
            scatter_R.append(max_pt['R'])
            scatter_Var_norm.append(max_pt['Var'] / (om2 + 1e-30))
            scatter_Hww_norm.append(max_pt['Hww'] / (om2 + 1e-30))
            scatter_Q_norm.append(max_pt['Q'] / (om2 + 1e-30))
            scatter_B_norm.append(max_pt['B'] / (om2 + 1e-30))
            scatter_ic.append(ic_name)

            # Grid-level histogram
            R_grid = grid['R']
            Q_grid = grid['Q']
            B_grid = grid['B']
            om_grid = grid['om']

            total_grid_pts += len(R_grid)

            # Bin by R
            bin_idx = np.digitize(R_grid, R_bins) - 1
            for bi in range(n_bins):
                mask_bin = (bin_idx == bi)
                if mask_bin.sum() == 0:
                    continue
                n_in_bin = mask_bin.sum()
                grid_Q_total[bi] += n_in_bin
                grid_Q_neg[bi] += (Q_grid[mask_bin] < 0).sum()
                grid_B_total[bi] += n_in_bin
                grid_B_neg[bi] += (B_grid[mask_bin] < 0).sum()
                grid_Q_sum[bi] += Q_grid[mask_bin].sum()
                grid_B_sum[bi] += B_grid[mask_bin].sum()

            # Print every 10th
            if step_i % 10 == 0:
                qok = "Y" if max_pt['Q'] < 0 else "N"
                bok = "Y" if max_pt['B'] < 0 else "N"
                print(f"  {t:6.4f}  {max_pt['om']:7.2f}  {max_pt['alpha']:+7.3f}  "
                      f"{max_pt['R']:+8.5f}  {max_pt['Var']:8.4f}  {max_pt['Hww']:+8.4f}  "
                      f"{max_pt['Q']:+8.4f}  {max_pt['B']:+8.4f}  "
                      f"{qok:>4s}  {bok:>4s}", flush=True)

            # Blowup check
            if max_pt['om'] > 1e5:
                print(f"  BLOWUP at t={t:.6f}", flush=True)
                break

        max_track.append((ic_name, ic_max_track))
        print(f"  Collected {diag_count} diagnostics for {ic_name}", flush=True)

    elapsed = time.time() - t0
    print(f"\n\nTotal time: {elapsed:.0f}s, Total grid points sampled: {total_grid_pts:,}", flush=True)

    # ========== ANALYSIS ==========

    # --- 1. Grid-level histogram: fraction Q<0 vs R ---
    print(f"\n{'='*80}", flush=True)
    print(f"  GRID-LEVEL: Q < 0 fraction vs alpha/|omega|", flush=True)
    print(f"  (across all ICs, all times, all grid points with |omega| > threshold)", flush=True)
    print(f"{'='*80}", flush=True)
    print(f"  {'R=a/|o|':>10s}  {'Q<0%':>7s}  {'B<0%':>7s}  {'<Q>':>10s}  {'<B>':>10s}  {'n':>8s}", flush=True)
    print(f"  " + "-"*65, flush=True)

    for bi in range(n_bins):
        if grid_Q_total[bi] < 10:
            continue
        q_frac = 100.0 * grid_Q_neg[bi] / grid_Q_total[bi]
        b_frac = 100.0 * grid_B_neg[bi] / grid_B_total[bi]
        q_mean = grid_Q_sum[bi] / grid_Q_total[bi]
        b_mean = grid_B_sum[bi] / grid_B_total[bi]
        n = int(grid_Q_total[bi])
        # Only print every 5th bin and all bins with R > 0.2
        if bi % 5 == 0 or R_centers[bi] > 0.2:
            print(f"  {R_centers[bi]:+10.4f}  {q_frac:6.1f}%  {b_frac:6.1f}%  "
                  f"{q_mean:+10.4f}  {b_mean:+10.4f}  {n:8d}", flush=True)

    # --- 2. Focus on HIGH R region (the critical zone for the barrier) ---
    print(f"\n{'='*80}", flush=True)
    print(f"  CRITICAL ZONE: R = alpha/|omega| > various thresholds", flush=True)
    print(f"{'='*80}", flush=True)

    for R_thresh in [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45]:
        mask_high = R_centers > R_thresh
        q_total_hi = grid_Q_total[mask_high].sum()
        if q_total_hi < 5:
            print(f"  R > {R_thresh:.2f}: insufficient data ({int(q_total_hi)} points)", flush=True)
            continue
        q_neg_hi = grid_Q_neg[mask_high].sum()
        b_neg_hi = grid_B_neg[mask_high].sum()
        b_total_hi = grid_B_total[mask_high].sum()
        print(f"  R > {R_thresh:.2f}: Q<0 at {100*q_neg_hi/q_total_hi:.1f}%  "
              f"B<0 at {100*b_neg_hi/b_total_hi:.1f}%  "
              f"({int(q_total_hi)} grid points)", flush=True)

    # --- 3. Max-point analysis ---
    print(f"\n{'='*80}", flush=True)
    print(f"  MAX-POINT ANALYSIS: alpha/|omega| vs Q, B across all ICs", flush=True)
    print(f"{'='*80}", flush=True)

    scatter_R = np.array(scatter_R)
    scatter_Var_norm = np.array(scatter_Var_norm)
    scatter_Hww_norm = np.array(scatter_Hww_norm)
    scatter_Q_norm = np.array(scatter_Q_norm)
    scatter_B_norm = np.array(scatter_B_norm)

    n_max = len(scatter_R)
    print(f"  Total max-point measurements: {n_max}", flush=True)
    print(f"  R range: [{scatter_R.min():.5f}, {scatter_R.max():.5f}]", flush=True)
    print(f"  |R| range: [{np.abs(scatter_R).min():.5f}, {np.abs(scatter_R).max():.5f}]", flush=True)

    q_neg_max = (scatter_Q_norm < 0).sum()
    b_neg_max = (scatter_B_norm < 0).sum()
    print(f"  Q < 0: {q_neg_max}/{n_max} ({100*q_neg_max/n_max:.1f}%)", flush=True)
    print(f"  B < 0: {b_neg_max}/{n_max} ({100*b_neg_max/n_max:.1f}%)", flush=True)
    print(f"  Hww > Var: {(scatter_Hww_norm > scatter_Var_norm).sum()}/{n_max} "
          f"({100*(scatter_Hww_norm > scatter_Var_norm).sum()/n_max:.1f}%)", flush=True)

    # R-binned at max point
    print(f"\n  Max-point R-binned:", flush=True)
    print(f"  {'R range':>14s}  {'Q<0%':>6s}  {'B<0%':>6s}  {'<Q/o2>':>10s}  {'<Var/o2>':>10s}  "
          f"{'<Hww/o2>':>10s}  {'n':>4s}", flush=True)
    for lo, hi in [(-0.5, -0.2), (-0.2, -0.1), (-0.1, 0.0), (0.0, 0.1),
                   (0.1, 0.2), (0.2, 0.3), (0.3, 0.4), (0.4, 0.5)]:
        m = (scatter_R >= lo) & (scatter_R < hi)
        if m.sum() < 2:
            continue
        qf = 100*(scatter_Q_norm[m] < 0).sum() / m.sum()
        bf = 100*(scatter_B_norm[m] < 0).sum() / m.sum()
        print(f"  [{lo:+.1f}, {hi:+.1f})  {qf:5.1f}%  {bf:5.1f}%  "
              f"{scatter_Q_norm[m].mean():+10.6f}  {scatter_Var_norm[m].mean():10.6f}  "
              f"{scatter_Hww_norm[m].mean():+10.6f}  {m.sum():4d}", flush=True)

    # --- 4. Per-IC summary ---
    print(f"\n{'='*80}", flush=True)
    print(f"  PER-IC SUMMARY at the max-|omega| point", flush=True)
    print(f"{'='*80}", flush=True)
    print(f"  {'IC':>15s}  {'n':>4s}  {'max|R|':>7s}  {'Q<0%':>6s}  {'B<0%':>6s}  "
          f"{'Hww>Var%':>8s}  {'<alpha>':>8s}  {'<|omega|>':>9s}", flush=True)

    for ic_name, track in max_track:
        if not track:
            continue
        n = len(track)
        Rs = np.array([d['R'] for d in track])
        Qs = np.array([d['Q'] for d in track])
        Bs = np.array([d['B'] for d in track])
        Vars = np.array([d['Var'] for d in track])
        Hwws = np.array([d['Hww'] for d in track])
        alphas = np.array([d['alpha'] for d in track])
        oms = np.array([d['om'] for d in track])

        q_pct = 100*(Qs < 0).sum() / n
        b_pct = 100*(Bs < 0).sum() / n
        hw_pct = 100*(Hwws > Vars).sum() / n
        print(f"  {ic_name:>15s}  {n:4d}  {np.abs(Rs).max():.5f}  {q_pct:5.1f}%  "
              f"{b_pct:5.1f}%  {hw_pct:7.1f}%  {alphas.mean():+8.3f}  "
              f"{oms.mean():9.2f}", flush=True)

    # --- 5. THE KEY QUESTION ---
    print(f"\n{'='*80}", flush=True)
    print(f"  THE KEY QUESTION: For R > 0.35, is Q < 0 always?", flush=True)
    print(f"{'='*80}", flush=True)

    # At grid level
    mask_high = R_centers > 0.35
    q_total_hi = grid_Q_total[mask_high].sum()
    if q_total_hi > 0:
        q_neg_hi = grid_Q_neg[mask_high].sum()
        print(f"  GRID LEVEL (R > 0.35): Q < 0 at {100*q_neg_hi/q_total_hi:.2f}% "
              f"of {int(q_total_hi)} points", flush=True)
    else:
        print(f"  GRID LEVEL (R > 0.35): no data points!", flush=True)

    # At max point
    mask_max_hi = np.abs(scatter_R) > 0.35
    if mask_max_hi.sum() > 0:
        q_neg_max_hi = (scatter_Q_norm[mask_max_hi] < 0).sum()
        print(f"  MAX POINT (|R| > 0.35): Q < 0 at {100*q_neg_max_hi/mask_max_hi.sum():.2f}% "
              f"of {mask_max_hi.sum()} points", flush=True)
    else:
        print(f"  MAX POINT (|R| > 0.35): no data points!", flush=True)

    # --- 6. STRONGEST BARRIER ---
    # Find the highest R threshold where Q<0 at 100%
    print(f"\n  Searching for strongest barrier beta where Q<0 at 100%:", flush=True)
    for beta in [0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05]:
        mask_b = R_centers > beta
        qt = grid_Q_total[mask_b].sum()
        if qt < 10:
            print(f"    beta={beta:.2f}: insufficient data ({int(qt)} pts)", flush=True)
            continue
        qn = grid_Q_neg[mask_b].sum()
        pct = 100*qn/qt
        status = "BARRIER HOLDS" if pct > 99.9 else "FAILS"
        print(f"    beta={beta:.2f}: Q<0 at {pct:.2f}% of {int(qt)} pts [{status}]", flush=True)
        if pct > 99.9:
            print(f"\n    >>> EMPIRICAL BARRIER at R = {beta:.2f}: alpha/|omega| < {beta:.2f}", flush=True)
            print(f"    >>> This is {'BELOW' if beta < 0.5 else 'AT'} the critical 1/2 threshold.", flush=True)
            break

    # --- 7. Scatter: Hww vs Var at max point ---
    print(f"\n{'='*80}", flush=True)
    print(f"  SCATTER: Hww vs Var at the max-|omega| point", flush=True)
    print(f"  Is Hww > Var always? (This means Q < 0 always)", flush=True)
    print(f"{'='*80}", flush=True)

    hww_above = scatter_Hww_norm > scatter_Var_norm
    print(f"  Hww/|om|^2 > Var/|om|^2: {hww_above.sum()}/{n_max} ({100*hww_above.sum()/n_max:.1f}%)", flush=True)

    # Stats
    gap = scatter_Hww_norm - scatter_Var_norm
    print(f"  Gap (Hww - Var)/|om|^2: mean={gap.mean():.6f}, min={gap.min():.6f}, "
          f"max={gap.max():.6f}", flush=True)
    if gap.min() > 0:
        print(f"  >>> Hww > Var at ALL max-point measurements!", flush=True)
        print(f"  >>> This means Q < 0 ALWAYS at the vorticity maximum.", flush=True)
    else:
        n_fail = (gap < 0).sum()
        print(f"  {n_fail} violations where Var > Hww at the max point.", flush=True)

    # ========== PLOTS ==========
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        out_dir = os.path.dirname(os.path.abspath(__file__))

        # --- Plot 1: Grid-level Q<0 fraction vs R ---
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        ax = axes[0, 0]
        valid = grid_Q_total > 10
        frac_q = np.where(valid, 100*grid_Q_neg / np.maximum(grid_Q_total, 1), np.nan)
        frac_b = np.where(valid, 100*grid_B_neg / np.maximum(grid_B_total, 1), np.nan)
        ax.plot(R_centers, frac_q, 'b-', lw=2, label='Q<0 %')
        ax.plot(R_centers, frac_b, 'r--', lw=2, label='B<0 %')
        ax.axhline(100, color='gray', ls=':', alpha=0.5)
        ax.axvline(0.5, color='green', ls='--', alpha=0.7, label='R=0.5 (critical)')
        ax.axvline(0.445, color='orange', ls='--', alpha=0.7, label='R=0.445 (barrier?)')
        ax.set_xlabel('R = alpha/|omega|')
        ax.set_ylabel('Fraction Q<0 or B<0 (%)')
        ax.set_title('Grid-level: fraction with Q<0 and B<0 vs R')
        ax.legend(fontsize=8)
        ax.set_xlim(-0.5, 0.5)
        ax.set_ylim(0, 105)
        ax.grid(True, alpha=0.3)

        # --- Plot 2: Mean Q and B vs R ---
        ax = axes[0, 1]
        mean_q = np.where(valid, grid_Q_sum / np.maximum(grid_Q_total, 1), np.nan)
        mean_b = np.where(valid, grid_B_sum / np.maximum(grid_B_total, 1), np.nan)
        ax.plot(R_centers, mean_q, 'b-', lw=2, label='<Q>')
        ax.plot(R_centers, mean_b, 'r--', lw=2, label='<B>')
        ax.axhline(0, color='gray', ls='-', alpha=0.5)
        ax.axvline(0.5, color='green', ls='--', alpha=0.7)
        ax.axvline(0.445, color='orange', ls='--', alpha=0.7)
        ax.set_xlabel('R = alpha/|omega|')
        ax.set_ylabel('Mean value')
        ax.set_title('Grid-level: mean Q and B vs R')
        ax.legend(fontsize=8)
        ax.set_xlim(-0.5, 0.5)
        ax.grid(True, alpha=0.3)

        # --- Plot 3: Scatter at max point: Hww/om^2 vs Var/om^2 ---
        ax = axes[1, 0]
        ax.scatter(scatter_Var_norm, scatter_Hww_norm, c=scatter_R, cmap='coolwarm',
                   s=15, alpha=0.7, edgecolors='none')
        lims = [min(scatter_Var_norm.min(), scatter_Hww_norm.min()),
                max(scatter_Var_norm.max(), scatter_Hww_norm.max())]
        ax.plot(lims, lims, 'k--', lw=1, label='Hww = Var (Q=0 line)')
        ax.set_xlabel('Var/|omega|^2')
        ax.set_ylabel('Hww/|omega|^2')
        ax.set_title('Max-point scatter: Hww vs Var\n(above line = Q<0)')
        ax.legend(fontsize=8)
        cb = plt.colorbar(ax.collections[0], ax=ax)
        cb.set_label('R = alpha/|omega|')
        ax.grid(True, alpha=0.3)

        # --- Plot 4: Max point R vs Q/|omega|^2 over time ---
        ax = axes[1, 1]
        # Color by IC
        ic_names_unique = list(dict.fromkeys(scatter_ic))
        colors = plt.cm.tab10(np.linspace(0, 1, len(ic_names_unique)))
        for i, ic_n in enumerate(ic_names_unique):
            mask_ic = np.array([x == ic_n for x in scatter_ic])
            ax.scatter(scatter_R[mask_ic], scatter_Q_norm[mask_ic],
                       c=[colors[i]], s=12, alpha=0.7, label=ic_n, edgecolors='none')
        ax.axhline(0, color='gray', ls='-', alpha=0.5)
        ax.axvline(0.5, color='green', ls='--', alpha=0.5)
        ax.set_xlabel('R = alpha/|omega|')
        ax.set_ylabel('Q/|omega|^2')
        ax.set_title('Max-point: Q/|omega|^2 vs R\n(below zero = barrier holds)')
        ax.legend(fontsize=6, ncol=2, loc='upper left')
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        fig_path = os.path.join(out_dir, 'barrier_alpha_bound.png')
        plt.savefig(fig_path, dpi=150, bbox_inches='tight')
        print(f"\n  Saved plot: {fig_path}", flush=True)
        plt.close()

        # --- Plot 5: Per-IC time series of R at max point ---
        fig, axes = plt.subplots(2, 1, figsize=(12, 8))

        ax = axes[0]
        for ic_name, track in max_track:
            if not track:
                continue
            ts = [d['t'] for d in track]
            Rs = [d['R'] for d in track]
            ax.plot(ts, Rs, '-', lw=1.2, alpha=0.8, label=ic_name)
        ax.axhline(0.5, color='red', ls='--', lw=2, label='R=0.5 (blowup)')
        ax.axhline(0.445, color='orange', ls='--', lw=1.5, label='R=0.445')
        ax.axhline(-0.5, color='red', ls='--', lw=2)
        ax.set_xlabel('t')
        ax.set_ylabel('R = alpha/|omega| at max')
        ax.set_title('Time evolution of alpha/|omega| at the vorticity maximum')
        ax.legend(fontsize=7, ncol=3)
        ax.grid(True, alpha=0.3)

        ax = axes[1]
        for ic_name, track in max_track:
            if not track:
                continue
            ts = [d['t'] for d in track]
            Qs = [d['Q'] for d in track]
            ax.plot(ts, Qs, '-', lw=1.2, alpha=0.8, label=ic_name)
        ax.axhline(0, color='gray', ls='-', lw=1)
        ax.set_xlabel('t')
        ax.set_ylabel('Q at max')
        ax.set_title('Time evolution of Q = Var - Hww at the vorticity maximum')
        ax.legend(fontsize=7, ncol=3)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        fig_path2 = os.path.join(out_dir, 'barrier_timeseries.png')
        plt.savefig(fig_path2, dpi=150, bbox_inches='tight')
        print(f"  Saved plot: {fig_path2}", flush=True)
        plt.close()

    except ImportError:
        print("  matplotlib not available, skipping plots.", flush=True)

    # ========== FINAL VERDICT ==========
    print(f"\n{'='*80}", flush=True)
    print(f"  FINAL SUMMARY", flush=True)
    print(f"{'='*80}", flush=True)

    print(f"\n  Total grid point samples: {total_grid_pts:,}", flush=True)
    print(f"  Total max-point samples: {n_max}", flush=True)
    print(f"  ICs tested: {len(max_track)}", flush=True)

    print(f"\n  AT THE VORTICITY MAXIMUM:", flush=True)
    print(f"    Q < 0: {q_neg_max}/{n_max} ({100*q_neg_max/n_max:.1f}%)", flush=True)
    print(f"    Hww > Var: {hww_above.sum()}/{n_max} ({100*hww_above.sum()/n_max:.1f}%)", flush=True)
    print(f"    max |R| observed: {np.abs(scatter_R).max():.5f}", flush=True)
    print(f"    max R observed: {scatter_R.max():.5f}", flush=True)

    print(f"\n  ACROSS ALL GRID POINTS:", flush=True)
    # Integrated stats for R > 0.2
    mask_02 = R_centers > 0.2
    qt02 = grid_Q_total[mask_02].sum()
    if qt02 > 0:
        qn02 = grid_Q_neg[mask_02].sum()
        print(f"    R > 0.2: Q<0 at {100*qn02/qt02:.2f}% of {int(qt02)} grid points", flush=True)
    mask_03 = R_centers > 0.3
    qt03 = grid_Q_total[mask_03].sum()
    if qt03 > 0:
        qn03 = grid_Q_neg[mask_03].sum()
        print(f"    R > 0.3: Q<0 at {100*qn03/qt03:.2f}% of {int(qt03)} grid points", flush=True)

    print(f"\n  INTERPRETATION:", flush=True)
    print(f"    If Q < 0 when alpha/|omega| > beta for some beta < 0.5,", flush=True)
    print(f"    then alpha/|omega| cannot exceed beta (barrier argument).", flush=True)
    print(f"    Since d|omega|/dt = alpha*|omega| and alpha < beta*|omega|,", flush=True)
    print(f"    we get d|omega|/dt < beta*|omega|^2 with beta < 1/2.", flush=True)
    print(f"    This is NOT sufficient for blowup (need beta >= 1/2).", flush=True)

    print(f"\n{'='*80}", flush=True)
    print(f"DONE in {time.time()-t0:.0f}s", flush=True)


if __name__ == '__main__':
    main()
