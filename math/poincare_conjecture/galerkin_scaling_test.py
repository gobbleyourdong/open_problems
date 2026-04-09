"""
Galerkin truncation scaling: does c₃ ≥ 1/3 require multi-scale interactions?

Experiment: Run full NS dynamics at N=64. At each diagnostic step:
1. Compute c₁, c₂, c₃ alignment at top 10% |ω| points using ALL modes
2. Galerkin-truncate to k_retain = 2, 4, 8, 16, 21 (full) and recompute c₁, c₂, c₃
3. Also compute the PRESSURE HESSIAN's contribution to alignment at high |ω|

The question: does c₃ ≥ 1/3 emerge only when enough shells interact,
or does it appear even in the lowest modes?

File 149 showed STATIC random fields converge to 1/3 with N modes.
This test: does DYNAMICALLY EVOLVED NS preserve or break that?
"""
import torch
import numpy as np
import math
import time

# Use CPU since Spark CUDA is problematic
DEVICE = 'cpu'
DTYPE = torch.float64


class NS3DLight:
    """Minimal 3D NS solver for alignment experiments."""

    def __init__(self, N=64, nu=1e-3, device=DEVICE):
        self.N = N
        self.nu = nu
        self.device = device
        self.Lx = 2 * math.pi
        dx = self.Lx / N

        x = torch.linspace(0, self.Lx - dx, N, device=device, dtype=DTYPE)
        self.X, self.Y, self.Z = torch.meshgrid(x, x, x, indexing='ij')

        k = torch.fft.fftfreq(N, d=dx / (2 * math.pi)).to(device=device, dtype=DTYPE)
        self.kx, self.ky, self.kz = torch.meshgrid(k, k, k, indexing='ij')
        self.ksq = self.kx**2 + self.ky**2 + self.kz**2
        self.ksq[0, 0, 0] = 1.0
        self.kmag = self.ksq.sqrt()

        kmax = N // 3
        self.dealias = ((self.kx.abs() < kmax) &
                        (self.ky.abs() < kmax) &
                        (self.kz.abs() < kmax)).to(DTYPE)

    def fft(self, f):
        return torch.fft.fftn(f)

    def ifft(self, fh):
        return torch.fft.ifftn(fh).real

    def curl(self, ux_h, uy_h, uz_h):
        I = 1j
        return (I*self.ky*uz_h - I*self.kz*uy_h,
                I*self.kz*ux_h - I*self.kx*uz_h,
                I*self.kx*uy_h - I*self.ky*ux_h)

    def vel_from_vort(self, wx_h, wy_h, wz_h):
        px = wx_h / self.ksq; py = wy_h / self.ksq; pz = wz_h / self.ksq
        px[0,0,0] = 0; py[0,0,0] = 0; pz[0,0,0] = 0
        I = 1j
        return (I*self.ky*pz - I*self.kz*py,
                I*self.kz*px - I*self.kx*pz,
                I*self.kx*py - I*self.ky*px)

    def rhs(self, wx_h, wy_h, wz_h):
        D = self.dealias
        ux_h, uy_h, uz_h = self.vel_from_vort(wx_h, wy_h, wz_h)

        ux = self.ifft(D*ux_h); uy = self.ifft(D*uy_h); uz = self.ifft(D*uz_h)
        wx = self.ifft(D*wx_h); wy = self.ifft(D*wy_h); wz = self.ifft(D*wz_h)

        # Velocity gradients
        grads = {}
        for name, fh in [('ux', ux_h), ('uy', uy_h), ('uz', uz_h)]:
            for d, kd in [('x', self.kx), ('y', self.ky), ('z', self.kz)]:
                grads[f'd{name}_d{d}'] = self.ifft(1j * kd * D * fh)

        # Stretching (ω·∇)u
        sx = wx*grads['dux_dx'] + wy*grads['dux_dy'] + wz*grads['dux_dz']
        sy = wx*grads['duy_dx'] + wy*grads['duy_dy'] + wz*grads['duy_dz']
        sz = wx*grads['duz_dx'] + wy*grads['duz_dy'] + wz*grads['duz_dz']

        # Advection (u·∇)ω
        wgrads = {}
        for name, fh in [('wx', wx_h), ('wy', wy_h), ('wz', wz_h)]:
            for d, kd in [('x', self.kx), ('y', self.ky), ('z', self.kz)]:
                wgrads[f'd{name}_d{d}'] = self.ifft(1j * kd * D * fh)

        ax = ux*wgrads['dwx_dx'] + uy*wgrads['dwx_dy'] + uz*wgrads['dwx_dz']
        ay = ux*wgrads['dwy_dx'] + uy*wgrads['dwy_dy'] + uz*wgrads['dwy_dz']
        az = ux*wgrads['dwz_dx'] + uy*wgrads['dwz_dy'] + uz*wgrads['dwz_dz']

        rhs_x = D * self.fft(sx - ax) - self.nu * self.ksq * wx_h
        rhs_y = D * self.fft(sy - ay) - self.nu * self.ksq * wy_h
        rhs_z = D * self.fft(sz - az) - self.nu * self.ksq * wz_h
        return rhs_x, rhs_y, rhs_z

    def step_rk4(self, wx_h, wy_h, wz_h, dt):
        def add(s1, s2, a):
            return (s1[0]+a*s2[0], s1[1]+a*s2[1], s1[2]+a*s2[2])
        w = (wx_h, wy_h, wz_h)
        k1 = self.rhs(*w)
        k2 = self.rhs(*add(w, k1, 0.5*dt))
        k3 = self.rhs(*add(w, k2, 0.5*dt))
        k4 = self.rhs(*add(w, k3, dt))
        D = self.dealias
        return (D*(wx_h + dt/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0])),
                D*(wy_h + dt/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1])),
                D*(wz_h + dt/6*(k1[2]+2*k2[2]+2*k3[2]+k4[2])))

    def galerkin_truncate(self, fh, k_retain):
        """Zero out all modes with |k| > k_retain."""
        mask = (self.kmag <= k_retain + 0.5).to(DTYPE)
        return fh * mask

    def omega_max(self, wx_h, wy_h, wz_h):
        wx = self.ifft(wx_h); wy = self.ifft(wy_h); wz = self.ifft(wz_h)
        return (wx**2 + wy**2 + wz**2).sqrt().max().item()


def compute_alignment_stats(solver, wx_h, wy_h, wz_h, k_retain=None):
    """
    Compute c₁, c₂, c₃ alignment at top 10% |ω| points.
    If k_retain is given, Galerkin-truncate first.
    """
    D = solver.dealias

    # Optionally truncate
    if k_retain is not None:
        wx_h = solver.galerkin_truncate(wx_h, k_retain)
        wy_h = solver.galerkin_truncate(wy_h, k_retain)
        wz_h = solver.galerkin_truncate(wz_h, k_retain)

    # Get velocity from (possibly truncated) vorticity
    ux_h, uy_h, uz_h = solver.vel_from_vort(wx_h, wy_h, wz_h)

    # Compute strain tensor S_ij = (∂u_i/∂x_j + ∂u_j/∂x_i)/2
    N = solver.N
    duidxj = torch.zeros(3, 3, N, N, N, dtype=DTYPE, device=solver.device)
    u_hats = [ux_h, uy_h, uz_h]
    k_dirs = [solver.kx, solver.ky, solver.kz]

    for i in range(3):
        for j in range(3):
            duidxj[i, j] = solver.ifft(1j * k_dirs[j] * D * u_hats[i])

    S = 0.5 * (duidxj + duidxj.transpose(0, 1))

    # Vorticity in physical space
    wx = solver.ifft(D * wx_h)
    wy = solver.ifft(D * wy_h)
    wz = solver.ifft(D * wz_h)
    om_mag = (wx**2 + wy**2 + wz**2).sqrt()

    # Top 10% threshold
    om_flat = om_mag.flatten()
    threshold = torch.quantile(om_flat, 0.90)
    if threshold < 1e-10:
        return {'c1': 0.33, 'c2': 0.33, 'c3': 0.33, 'alpha': 0.0, 'n_pts': 0, 'om_max': 0.0}

    mask = om_mag > threshold
    idx = mask.nonzero(as_tuple=False)  # [M, 3]

    c1_sum = 0.0
    c2_sum = 0.0
    c3_sum = 0.0
    alpha_sum = 0.0
    count = 0

    # Sample up to 2000 points for speed
    n_pts = min(len(idx), 2000)
    if n_pts == 0:
        return {'c1': 0.33, 'c2': 0.33, 'c3': 0.33, 'alpha': 0.0, 'n_pts': 0, 'om_max': 0.0}

    perm = torch.randperm(len(idx))[:n_pts]
    sampled = idx[perm]

    for pt in sampled:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()

        # Local strain matrix
        Slocal = S[:, :, ix, iy, iz].clone()

        # Local vorticity direction
        w_vec = torch.tensor([wx[ix,iy,iz], wy[ix,iy,iz], wz[ix,iy,iz]], dtype=DTYPE)
        w_norm = w_vec.norm()
        if w_norm < 1e-12:
            continue
        w_hat = w_vec / w_norm

        # Eigendecomposition of strain
        eigvals, eigvecs = torch.linalg.eigh(Slocal)
        # eigh returns sorted ascending: λ₃ (most compressive) first, λ₁ (most stretching) last
        # Convention: λ₁ ≥ λ₂ ≥ λ₃ (so reverse)
        lam1, lam2, lam3 = eigvals[2].item(), eigvals[1].item(), eigvals[0].item()
        e1 = eigvecs[:, 2]  # most stretching
        e2 = eigvecs[:, 1]  # intermediate
        e3 = eigvecs[:, 0]  # most compressive

        # Alignment: c_i = cos²(ω, e_i)
        c1 = (w_hat @ e1).item()**2
        c2 = (w_hat @ e2).item()**2
        c3 = (w_hat @ e3).item()**2

        # Stretching rate α = Σ λ_i c_i
        alpha = lam1 * c1 + lam2 * c2 + lam3 * c3

        c1_sum += c1
        c2_sum += c2
        c3_sum += c3
        alpha_sum += alpha
        count += 1

    if count == 0:
        return {'c1': 0.33, 'c2': 0.33, 'c3': 0.33, 'alpha': 0.0, 'n_pts': 0, 'om_max': 0.0}

    return {
        'c1': c1_sum / count,
        'c2': c2_sum / count,
        'c3': c3_sum / count,
        'alpha': alpha_sum / count,
        'n_pts': count,
        'om_max': om_flat.max().item(),
    }


def compute_pressure_hessian_alignment(solver, wx_h, wy_h, wz_h):
    """
    Compute the pressure Hessian H_ij = ∂²p/∂x_i∂x_j at top |ω| points.
    Pressure solves: Δp = -Σ_{ij} (∂u_i/∂x_j)(∂u_j/∂x_i)
    Then measure: how does H project onto the ω direction?

    Key test of Yang's formula: H_dev should have degenerate ⊥ω eigenvalues.
    """
    D = solver.dealias
    N = solver.N

    # Velocity and its gradient
    ux_h, uy_h, uz_h = solver.vel_from_vort(wx_h, wy_h, wz_h)
    k_dirs = [solver.kx, solver.ky, solver.kz]
    u_hats = [ux_h, uy_h, uz_h]

    duidxj = torch.zeros(3, 3, N, N, N, dtype=DTYPE, device=solver.device)
    for i in range(3):
        for j in range(3):
            duidxj[i, j] = solver.ifft(1j * k_dirs[j] * D * u_hats[i])

    # Pressure source: -Σ (∂u_i/∂x_j)(∂u_j/∂x_i) = -tr(A^T A) where A=∇u
    # Actually: Δp = -Σ_{ij} A_{ij} A_{ji}
    source = torch.zeros(N, N, N, dtype=DTYPE, device=solver.device)
    for i in range(3):
        for j in range(3):
            source -= duidxj[i, j] * duidxj[j, i]

    # Solve: p_hat = source_hat / (-|k|²)
    source_h = solver.fft(source)
    p_hat = -source_h / solver.ksq
    p_hat[0, 0, 0] = 0

    # Pressure Hessian: H_ij = ∂²p/∂x_i∂x_j = -k_i k_j p_hat (Fourier)
    H = torch.zeros(3, 3, N, N, N, dtype=DTYPE, device=solver.device)
    for i in range(3):
        for j in range(3):
            H[i, j] = solver.ifft(-k_dirs[i] * k_dirs[j] * p_hat)

    # Vorticity
    wx = solver.ifft(D * wx_h)
    wy = solver.ifft(D * wy_h)
    wz = solver.ifft(D * wz_h)
    om_mag = (wx**2 + wy**2 + wz**2).sqrt()

    threshold = torch.quantile(om_mag.flatten(), 0.90)
    if threshold < 1e-10:
        return {'yang_degeneracy': 0.0, 'H_omega_proj': 0.0}

    mask = om_mag > threshold
    idx = mask.nonzero(as_tuple=False)
    n_pts = min(len(idx), 1000)
    perm = torch.randperm(len(idx))[:n_pts]
    sampled = idx[perm]

    degen_sum = 0.0
    h_proj_sum = 0.0
    count = 0

    for pt in sampled:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()

        Hlocal = H[:, :, ix, iy, iz].clone()
        w_vec = torch.tensor([wx[ix,iy,iz], wy[ix,iy,iz], wz[ix,iy,iz]], dtype=DTYPE)
        w_norm = w_vec.norm()
        if w_norm < 1e-12:
            continue
        w_hat = w_vec / w_norm

        # Project H onto ω direction
        h_omega = (w_hat @ Hlocal @ w_hat).item()

        # Deviatoric part: H_dev = H - (tr(H)/3)I
        tr_H = Hlocal.trace().item()
        H_dev = Hlocal - (tr_H / 3) * torch.eye(3, dtype=DTYPE)

        # Eigenvalues of H_dev
        eigvals_H = torch.linalg.eigvalsh(H_dev)
        # Sort by magnitude
        eigvals_sorted = eigvals_H.sort(descending=True).values

        # Yang predicts: 2 degenerate eigenvalues in ⊥ω plane
        # Measure: |λ₂ - λ₃| / max(|λ₁|, 1e-10)
        degen = abs(eigvals_sorted[1].item() - eigvals_sorted[2].item()) / \
                max(abs(eigvals_sorted[0].item()), 1e-10)

        degen_sum += degen
        h_proj_sum += h_omega
        count += 1

    if count == 0:
        return {'yang_degeneracy': 0.0, 'H_omega_proj': 0.0}

    return {
        'yang_degeneracy': degen_sum / count,  # 0 = perfectly degenerate (Yang prediction)
        'H_omega_proj': h_proj_sum / count,    # positive = pressure opposes stretching
        'n_pts': count,
    }


def ic_taylor_green(solver):
    X, Y, Z = solver.X, solver.Y, solver.Z
    ux = torch.cos(X) * torch.sin(Y) * torch.cos(Z)
    uy = -torch.sin(X) * torch.cos(Y) * torch.cos(Z)
    uz = torch.zeros_like(X)
    ux_h, uy_h, uz_h = solver.fft(ux), solver.fft(uy), solver.fft(uz)
    return solver.curl(ux_h, uy_h, uz_h)


def ic_kida_pelz(solver):
    X, Y, Z = solver.X, solver.Y, solver.Z
    ux = torch.sin(X) * (torch.cos(3*Y) * torch.cos(Z) - torch.cos(Y) * torch.cos(3*Z))
    uy = torch.sin(Y) * (torch.cos(3*Z) * torch.cos(X) - torch.cos(Z) * torch.cos(3*X))
    uz = torch.sin(Z) * (torch.cos(3*X) * torch.cos(Y) - torch.cos(X) * torch.cos(3*Y))
    ux_h, uy_h, uz_h = solver.fft(ux), solver.fft(uy), solver.fft(uz)
    return solver.curl(ux_h, uy_h, uz_h)


def main():
    print("=" * 70)
    print("GALERKIN TRUNCATION SCALING: c₃ vs mode count in EVOLVED NS")
    print("=" * 70)

    N = 32  # Start small for speed — N=32 gives 21 dealiased modes
    nu = 1e-3  # Higher viscosity for stability at low N
    n_evolve_steps = 800  # Evolve to get strong nonlinear dynamics
    dt = 5e-4
    k_retains = [2, 4, 6, 8, 10, 21]  # Galerkin truncation levels (21 = full for N=32)

    for ic_name, ic_func in [('TG', ic_taylor_green), ('KP', ic_kida_pelz)]:
        print(f"\n{'='*70}")
        print(f"IC: {ic_name}, N={N}, ν={nu}")
        print(f"{'='*70}")

        solver = NS3DLight(N=N, nu=nu, device=DEVICE)
        wx_h, wy_h, wz_h = ic_func(solver)

        print(f"  t=0: |ω|_max = {solver.omega_max(wx_h, wy_h, wz_h):.3f}")

        # Evolve
        t = 0.0
        diag_interval = 200
        t0 = time.time()

        for step in range(n_evolve_steps + 1):
            if step % diag_interval == 0:
                om_max = solver.omega_max(wx_h, wy_h, wz_h)
                elapsed = time.time() - t0

                print(f"\n  step={step}, t={t:.4f}, |ω|_max={om_max:.3f} [{elapsed:.0f}s]")

                # Full alignment (no truncation)
                stats_full = compute_alignment_stats(solver, wx_h, wy_h, wz_h)
                print(f"    FULL: c₁={stats_full['c1']:.3f} c₂={stats_full['c2']:.3f} "
                      f"c₃={stats_full['c3']:.3f} α={stats_full['alpha']:.4f} "
                      f"[{stats_full['n_pts']} pts]")

                # Galerkin truncated
                for kr in k_retains:
                    stats = compute_alignment_stats(solver, wx_h, wy_h, wz_h, k_retain=kr)
                    c3_marker = "✓" if stats['c3'] >= 0.333 else " "
                    print(f"    k≤{kr:2d}: c₁={stats['c1']:.3f} c₂={stats['c2']:.3f} "
                          f"c₃={stats['c3']:.3f} α={stats['alpha']:.4f} {c3_marker}")

                # Pressure Hessian analysis at evolved state
                if step > 0:
                    ph = compute_pressure_hessian_alignment(solver, wx_h, wy_h, wz_h)
                    print(f"    Pressure H: degeneracy={ph['yang_degeneracy']:.3f} "
                          f"ω-projection={ph['H_omega_proj']:.4f}")

            # RK4 step
            if step < n_evolve_steps:
                wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
                t += dt

    # =====================================================================
    # EXPERIMENT 2: Mode count vs c₃ with FULL NS dynamics
    # Run NS at different Galerkin truncations FROM THE START
    # =====================================================================
    print(f"\n\n{'='*70}")
    print("EXPERIMENT 2: NS DYNAMICS WITH GALERKIN TRUNCATION DURING EVOLUTION")
    print("Does c₃ require multi-scale coupling to reach 1/3?")
    print(f"{'='*70}")

    truncation_levels = [4, 8, 16, 21]  # k_max during evolution

    for ic_name, ic_func in [('TG', ic_taylor_green)]:
        for k_trunc in truncation_levels:
            solver = NS3DLight(N=N, nu=nu, device=DEVICE)
            wx_h, wy_h, wz_h = ic_func(solver)

            # Truncate IC
            wx_h = solver.galerkin_truncate(wx_h, k_trunc)
            wy_h = solver.galerkin_truncate(wy_h, k_trunc)
            wz_h = solver.galerkin_truncate(wz_h, k_trunc)

            print(f"\n  {ic_name} k_trunc={k_trunc}: |ω|₀ = {solver.omega_max(wx_h, wy_h, wz_h):.3f}")

            t = 0.0
            for step in range(n_evolve_steps + 1):
                if step % diag_interval == 0 and step > 0:
                    # Re-truncate (Galerkin projection at each step)
                    wx_h = solver.galerkin_truncate(wx_h, k_trunc)
                    wy_h = solver.galerkin_truncate(wy_h, k_trunc)
                    wz_h = solver.galerkin_truncate(wz_h, k_trunc)

                    om_max = solver.omega_max(wx_h, wy_h, wz_h)
                    stats = compute_alignment_stats(solver, wx_h, wy_h, wz_h)
                    c3_marker = "✓" if stats['c3'] >= 0.333 else " "
                    print(f"    t={t:.4f} |ω|={om_max:.3f} c₁={stats['c1']:.3f} "
                          f"c₂={stats['c2']:.3f} c₃={stats['c3']:.3f} "
                          f"α={stats['alpha']:.4f} {c3_marker}")

                if step < n_evolve_steps:
                    # Truncate the RHS too (Galerkin dynamics)
                    wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
                    # Re-truncate after step
                    wx_h = solver.galerkin_truncate(wx_h, k_trunc)
                    wy_h = solver.galerkin_truncate(wy_h, k_trunc)
                    wz_h = solver.galerkin_truncate(wz_h, k_trunc)
                    t += dt

    # =====================================================================
    # EXPERIMENT 3: Pressure vs no-pressure alignment
    # Restricted Euler (no pressure) vs full NS
    # =====================================================================
    print(f"\n\n{'='*70}")
    print("EXPERIMENT 3: RESTRICTED EULER (no pressure) vs FULL NS")
    print("Does pressure push c₃ toward 1/3?")
    print(f"{'='*70}")

    solver_full = NS3DLight(N=N, nu=nu, device=DEVICE)
    solver_re = NS3DLight(N=N, nu=0, device=DEVICE)  # inviscid

    wx_h_f, wy_h_f, wz_h_f = ic_taylor_green(solver_full)
    wx_h_r, wy_h_r, wz_h_r = ic_taylor_green(solver_re)

    # For restricted Euler, we need to modify the RHS to remove pressure
    # The vorticity equation without pressure: dω/dt = (ω·∇)u only
    # Actually in vorticity form, pressure doesn't appear explicitly!
    # The pressure enters through the Biot-Savart law (incompressibility).
    # So "restricted Euler" in the strain formulation is different from
    # the vorticity formulation.
    #
    # In vorticity form: dω/dt = (ω·∇)u - (u·∇)ω + ν∇²ω
    # The pressure is IMPLICIT in the fact that u is divergence-free (Biot-Savart).
    #
    # To truly remove pressure, we'd need to use the velocity gradient tensor A
    # and evolve dA/dt = -A² (restricted Euler).
    #
    # Instead, let's compare: full NS (divergence-free u via Biot-Savart)
    # vs "compressible": u = ∇⁻² × ω + ε·ω (add a compressible part)
    #
    # Actually, a cleaner test: evolve the STRAIN TENSOR directly.
    #
    # For now, let's just evolve full NS and measure pressure Hessian stats
    # at different times.

    print("\n  Evolving TG with full NS, tracking pressure contribution...")
    t = 0.0
    for step in range(n_evolve_steps + 1):
        if step % diag_interval == 0:
            om_max = solver_full.omega_max(wx_h_f, wy_h_f, wz_h_f)
            stats = compute_alignment_stats(solver_full, wx_h_f, wy_h_f, wz_h_f)

            # Pressure Hessian analysis
            if step > 0 and om_max > 0.1:
                ph = compute_pressure_hessian_alignment(solver_full, wx_h_f, wy_h_f, wz_h_f)
                print(f"    t={t:.4f} |ω|={om_max:.3f} "
                      f"c₁={stats['c1']:.3f} c₃={stats['c3']:.3f} "
                      f"H_deg={ph['yang_degeneracy']:.3f} H_ω={ph['H_omega_proj']:.4f}")
            else:
                print(f"    t={t:.4f} |ω|={om_max:.3f} "
                      f"c₁={stats['c1']:.3f} c₃={stats['c3']:.3f}")

        if step < n_evolve_steps:
            wx_h_f, wy_h_f, wz_h_f = solver_full.step_rk4(wx_h_f, wy_h_f, wz_h_f, dt)
            t += dt

    # =====================================================================
    # EXPERIMENT 4: LOCAL STRAIN ODE vs FULL PDE
    # Track individual fluid elements — does the local ODE give c₃ < 1/3
    # while the full PDE gives c₃ ≥ 1/3?
    # =====================================================================
    print(f"\n\n{'='*70}")
    print("EXPERIMENT 4: LOCAL vs GLOBAL — why local ODE fails but full PDE works")
    print("Track individual Lagrangian trajectories through the flow")
    print(f"{'='*70}")

    solver = NS3DLight(N=N, nu=nu, device=DEVICE)
    wx_h, wy_h, wz_h = ic_taylor_green(solver)

    # Evolve to t=0.2 first (develop nonlinearity)
    t = 0.0
    for step in range(400):
        wx_h, wy_h, wz_h = solver.step_rk4(wx_h, wy_h, wz_h, dt)
        t += dt

    print(f"  Evolved to t={t:.4f}, |ω|={solver.omega_max(wx_h, wy_h, wz_h):.3f}")

    # Now compute the velocity gradient A = ∇u at top |ω| points
    # Compare: actual c₃ from full PDE vs what -A² predicts (restricted Euler)
    D = solver.dealias
    ux_h, uy_h, uz_h = solver.vel_from_vort(wx_h, wy_h, wz_h)

    A = torch.zeros(3, 3, N, N, N, dtype=DTYPE, device=DEVICE)
    k_dirs = [solver.kx, solver.ky, solver.kz]
    u_hats = [ux_h, uy_h, uz_h]
    for i in range(3):
        for j in range(3):
            A[i, j] = solver.ifft(1j * k_dirs[j] * D * u_hats[i])

    wx = solver.ifft(D * wx_h)
    wy = solver.ifft(D * wy_h)
    wz = solver.ifft(D * wz_h)
    om_mag = (wx**2 + wy**2 + wz**2).sqrt()

    threshold = torch.quantile(om_mag.flatten(), 0.90)
    mask = om_mag > threshold
    idx = mask.nonzero(as_tuple=False)

    n_sample = min(500, len(idx))
    perm = torch.randperm(len(idx))[:n_sample]
    sampled = idx[perm]

    # For each sample point, compute:
    # 1. Actual S eigenstructure → c₁, c₃
    # 2. -A² → what restricted Euler would predict for dS/dt
    # 3. The pressure Hessian H → what pressure adds to dS/dt
    c3_full = []
    c3_re_pred = []  # restricted Euler prediction for NEXT-STEP c₃

    print(f"  Sampling {n_sample} high-|ω| points...")

    for pt in sampled:
        ix, iy, iz = pt[0].item(), pt[1].item(), pt[2].item()

        A_local = A[:, :, ix, iy, iz].clone()
        S_local = 0.5 * (A_local + A_local.T)

        w_vec = torch.tensor([wx[ix,iy,iz], wy[ix,iy,iz], wz[ix,iy,iz]], dtype=DTYPE)
        w_norm = w_vec.norm()
        if w_norm < 1e-12:
            continue
        w_hat = w_vec / w_norm

        # Full PDE alignment
        eigvals, eigvecs = torch.linalg.eigh(S_local)
        e3 = eigvecs[:, 0]  # most compressive
        c3 = (w_hat @ e3).item()**2
        c3_full.append(c3)

        # Restricted Euler: dS/dt ≈ -S² - (1/4)Ω² (ignoring pressure)
        # Actually dA/dt = -A² in RE, so dS/dt = -(A²)_symmetric
        A2 = A_local @ A_local
        dSdt_re = -0.5 * (A2 + A2.T)

        # Predicted S at next step: S_new ≈ S + dSdt_re * dt
        S_next_re = S_local + dSdt_re * dt * 100  # amplify to see effect
        eigvals_next, eigvecs_next = torch.linalg.eigh(S_next_re)
        e3_next = eigvecs_next[:, 0]
        c3_next = (w_hat @ e3_next).item()**2
        c3_re_pred.append(c3_next)

    c3_full = np.array(c3_full)
    c3_re_pred = np.array(c3_re_pred)

    print(f"\n  Results at high-|ω| points (t={t:.4f}):")
    print(f"    Full PDE c₃:        mean={c3_full.mean():.4f}  median={np.median(c3_full):.4f}")
    print(f"    RE next-step c₃:    mean={c3_re_pred.mean():.4f}  median={np.median(c3_re_pred):.4f}")
    print(f"    Full PDE c₃ ≥ 1/3:  {(c3_full >= 0.333).mean()*100:.1f}%")
    print(f"    RE pred c₃ ≥ 1/3:   {(c3_re_pred >= 0.333).mean()*100:.1f}%")
    print(f"    Pressure pushes c₃: {'YES' if c3_full.mean() > c3_re_pred.mean() else 'NO'} "
          f"(Δ = {c3_full.mean() - c3_re_pred.mean():.4f})")

    print(f"\n{'='*70}")
    print("DONE. Summary of mechanisms tested:")
    print("  1. Galerkin truncation: does c₃ need many modes?")
    print("  2. Truncated dynamics: does c₃ emerge even at low k_max?")
    print("  3. Pressure Hessian: degeneracy test (Yang ⊥ω symmetry)")
    print("  4. Local RE vs full PDE: pressure's role in c₃")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
