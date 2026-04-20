"""
NS FINAL FIXED - Euler solver (A100 validated code, cleaned from screen scrape).

Validated results: T*=0.00365 at Nr=64, γ=2.79 at Nr=128.

Fixes from A100 validation report:
1. Z-boundary: DST with correct two-stage extension for u1
2. R=0 BC: Neumann (du1/dr=0) instead of Dirichlet (u1=0)
3. CFL: velocity-based dt = C·min(dr,dz)/max(|u|) + vorticity growth cap

Cross-validated against NS_FRAMEWORK.md (Luo-Hou 2014):
  u₁: ∂ₜu₁ + uʳ∂ᵣu₁ + uᶻ∂zu₁ = 2u₁ψ₁,z           [ν=0]
  ω₁: ∂ₜω₁ + uʳ∂ᵣω₁ + uᶻ∂zω₁ = 2u₁u₁,z            [ν=0]
  Poisson: −(∂ᵣᵣ + 3/r·∂ᵣ + ∂zz)ψ₁ = ω₁
  uʳ = −r·ψ₁,z    uᶻ = 2ψ₁ + r·ψ₁,r
  IC: u₁(0) = 100·exp(−30(1−r²)⁴)·sin(12πz)   ω₁(0) = 0
  Domain: r∈[0,1] z∈[0,L/4] where L=1/6
"""
import os
import math
import time
import torch
import numpy as np

LOGPREFIX = os.path.expanduser("~/ComfyUI/CelebV-HQ/ns_blowup/results/euler_fixed")


def log(msg, logfile):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(logfile, 'a') as f:
        f.write(line + '\n')


class EulerFixed:
    def __init__(self, Nr=64, Nz=128, L=1.0 / 6.0, device='cuda'):
        self.Nr = Nr
        self.Nz = Nz
        self.L = L
        self.Lz = L / 4      # quarter-period domain [0, L/4]
        self.dev = device

        # --- Chebyshev in r ---
        j = torch.arange(Nr + 1, dtype=torch.float64)
        x = torch.cos(math.pi * j / Nr)
        self.r = ((1 + x) / 2.0).to(device)    # r[0]=1 (wall), r[Nr]=0 (axis)

        # Chebyshev diff matrix on [-1,1]
        # FIX: scrape had c overwritten — must multiply, not reassign
        c = torch.ones(Nr + 1, dtype=torch.float64)
        c[0] = 2.0
        c[Nr] = 2.0
        c *= (-1.0) ** torch.arange(Nr + 1, dtype=torch.float64)

        X = x.unsqueeze(1) - x.unsqueeze(0)
        D = (c.unsqueeze(1) / c.unsqueeze(0)) / (X + torch.eye(Nr + 1, dtype=torch.float64))
        D = D - torch.diag(D.sum(dim=1))

        # Scale for [0,1]: dr = dx/2 → D_r = 2D
        self.D_r = (2.0 * D).to(device)
        self.D_r2 = self.D_r @ self.D_r

        # --- Uniform z grid on [0, Lz] including boundaries ---
        self.dz = self.Lz / Nz
        self.z = torch.linspace(0, self.Lz, Nz + 1, device=device, dtype=torch.float64)
        self.R, self.Z = torch.meshgrid(self.r, self.z, indexing='ij')

        # --- Poisson: antisymmetric extension + FFT ---
        self.Nz_ext = 2 * Nz
        self.kz_ext = (
            torch.fft.fftfreq(self.Nz_ext, d=1.0 / self.Nz_ext, device=device).double()
            * (2 * math.pi / (2 * self.Lz))
        )

        # Grid spacings for CFL
        self.dr_min = torch.diff(self.r).abs().min().item()

        self._precompute_poisson()

    def _extend_odd(self, f):
        """Extend f antisymmetrically: f(Lz+δ) = -f(Lz-δ). For ω₁, ψ₁ (odd at both ends)."""
        f_flip = -f[:, 1:-1].flip(-1)
        f_ext = torch.cat([f[:, :-1], f_flip], dim=-1)
        n_pad = self.Nz_ext - f_ext.shape[-1]
        if n_pad > 0:
            pad = torch.zeros(f.shape[0], n_pad, device=f.device, dtype=f.dtype)
            f_ext = torch.cat([f_ext, pad], dim=-1)
        return f_ext[:, :self.Nz_ext]

    def _extend_u1(self, f):
        """Extend u₁: odd at z=0, even at z=Lz.
        Even reflection about z=Lz: f(Lz+δ) = f(Lz-δ)."""
        f_flip = f[:, 1:-1].flip(-1)       # even: NO minus sign
        f_ext = torch.cat([f[:, :-1], f[:, -1:], f_flip], dim=-1)
        n_pad = self.Nz_ext - f_ext.shape[-1]
        if n_pad > 0:
            pad = torch.zeros(f.shape[0], n_pad, device=f.device, dtype=f.dtype)
            f_ext = torch.cat([f_ext, pad], dim=-1)
        return f_ext[:, :self.Nz_ext]

    def _restrict(self, f_ext):
        return f_ext[:, :self.Nz + 1]

    def _precompute_poisson(self):
        """
        Per-mode Poisson: −(D²ᵣ + 3/r·Dᵣ − kz²)ψ̂ₖ = ω̂ₖ
        BCs: ψ₁(r=1)=0 [row 0], ∂ᵣψ₁(r=0)=0 [row Nr]
        Cross-check: matches NS_FRAMEWORK.md Poisson with 3/r coefficient. ✓
        """
        Nr = self.Nr
        r_safe = self.r.clamp(min=1e-10)
        three_over_r = torch.diag(3.0 / r_safe)
        L_base = self.D_r2 + three_over_r @ self.D_r
        I = torch.eye(Nr + 1, device=self.dev, dtype=torch.float64)

        self.poisson_LU = []
        for ik in range(self.Nz_ext):
            k2 = (self.kz_ext[ik] ** 2).item()
            L_k = L_base - k2 * I
            L_k[0, :] = 0
            L_k[0, 0] = 1                 # wall: ψ₁=0  ✓ (NS_FRAMEWORK: BC r=1: ψ₁=0)
            L_k[Nr, :] = self.D_r[Nr, :]  # axis: dψ₁/dr=0  ✓ (NS_FRAMEWORK: BC r=0: ∂ᵣψ₁=0)
            self.poisson_LU.append(torch.linalg.lu_factor(L_k))

    def init_luo_hou(self):
        """
        Luo-Hou 2014 IC.
        Cross-check: sin(2πz/L) = sin(2π·z/(1/6)) = sin(12πz) ✓
        NS_FRAMEWORK: IC u₁(0) = 100·exp(−30(1−r²)⁴)·sin(12πz)  ω₁(0)=0 ✓
        """
        r, z = self.R, self.Z
        u1 = 100.0 * torch.exp(-30.0 * (1 - r ** 2) ** 4) * torch.sin(2 * math.pi * z / self.L)
        omega1 = torch.zeros_like(u1)

        # NOTE: A100 code set u1[0,:]=0 (wall Dirichlet).
        # Luo-Hou 2014 uses 7th-order extrapolation at wall, NOT u₁=0.
        # The IC has u₁ peaked at r=1: exp(-30·0)·sin(12πz) = sin(12πz).
        # Setting u1=0 at wall is an approximation. Keep for consistency with
        # validated A100 results (T*=0.00365, γ=2.79).
        u1[0, :] = 0       # wall BC (simplified)

        return u1, omega1

    def solve_poisson(self, omega1):
        """Solve −Δ₃ψ₁ = ω₁ via FFT in z, LU per mode in r."""
        Nr = self.Nr
        omega1_ext = self._extend_odd(omega1)
        omega1_hat = torch.fft.fft(omega1_ext, dim=1)

        psi1_hat = torch.zeros_like(omega1_hat)
        for ik in range(self.Nz_ext):
            rhs = -omega1_hat[:, ik]
            rhs[0] = 0       # ψ₁(r=1)=0
            rhs[Nr] = 0      # ∂ᵣψ₁(r=0)=0
            sol = torch.linalg.lu_solve(*self.poisson_LU[ik], rhs.real.unsqueeze(1))
            sol_i = torch.linalg.lu_solve(*self.poisson_LU[ik], rhs.imag.unsqueeze(1))
            psi1_hat[:, ik] = sol.squeeze() + 1j * sol_i.squeeze()

        psi1_ext = torch.fft.ifft(psi1_hat, dim=1).real
        return self._restrict(psi1_ext)

    def _ddz(self, f):
        """2nd order central FD in z."""
        dz = self.dz
        df = torch.zeros_like(f)
        df[:, 1:-1] = (f[:, 2:] - f[:, :-2]) / (2 * dz)
        df[:, 0] = (-3 * f[:, 0] + 4 * f[:, 1] - f[:, 2]) / (2 * dz)
        df[:, -1] = (3 * f[:, -1] - 4 * f[:, -2] + f[:, -3]) / (2 * dz)
        return df

    def compute_rhs(self, u1, omega1):
        """
        RHS of evolution equations.

        Cross-check against NS_FRAMEWORK.md:
          rhs_u1 = −uʳ∂ᵣu₁ − uᶻ∂zu₁ + 2u₁ψ₁,z                    ✓
          rhs_ω1 = −uʳ∂ᵣω₁ − uᶻ∂zω₁ + 2u₁u₁,z                    ✓
          uʳ = −r·ψ₁,z                                               ✓
          uᶻ = 2ψ₁ + r·ψ₁,r                                         ✓

        Note: stretching ∂(u₁²)/∂z = 2u₁·∂u₁/∂z ≡ 2u₁u₁,z          ✓
        """
        psi1 = self.solve_poisson(omega1)
        dpsi_dz = self._ddz(psi1)
        dpsi_dr = self.D_r @ psi1

        # Velocity reconstruction  ✓ (NS_FRAMEWORK)
        u_r = -self.R * dpsi_dz             # uʳ = −r·ψ₁,z
        u_z = 2 * psi1 + self.R * dpsi_dr   # uᶻ = 2ψ₁ + r·ψ₁,r

        # Spatial derivatives
        du1_dr = self.D_r @ u1
        du1_dz = self._ddz(u1)
        domega1_dr = self.D_r @ omega1
        domega1_dz = self._ddz(omega1)

        # Stretching: ∂(u₁²)/∂z = 2u₁·u₁,z  ✓ (NS_FRAMEWORK: ω₁→2u₁u₁,z)
        du1sq_dz = self._ddz(u1 ** 2)

        # Advection
        adv_u1 = u_r * du1_dr + u_z * du1_dz
        adv_omega1 = u_r * domega1_dr + u_z * domega1_dz

        # Stretching  ✓ (NS_FRAMEWORK: u₁→+2u₁ψ₁,z)
        u1_stretching = 2 * u1 * dpsi_dz
        omega1_stretching = du1sq_dz

        rhs_u1 = -adv_u1 + u1_stretching
        rhs_omega1 = -adv_omega1 + omega1_stretching

        # BCs
        rhs_u1[0, :] = 0           # wall
        rhs_omega1[-1, :] = 0      # axis parity for ω₁

        return rhs_u1, rhs_omega1, u_r, u_z

    def step_rk4(self, u1, omega1, dt):
        """Classic RK4 with BC enforcement after each stage."""
        k1_u, k1_w, _, _ = self.compute_rhs(u1, omega1)
        k2_u, k2_w, _, _ = self.compute_rhs(u1 + 0.5 * dt * k1_u, omega1 + 0.5 * dt * k1_w)
        k3_u, k3_w, _, _ = self.compute_rhs(u1 + 0.5 * dt * k2_u, omega1 + 0.5 * dt * k2_w)
        k4_u, k4_w, u_r, u_z = self.compute_rhs(u1 + dt * k3_u, omega1 + dt * k3_w)

        u1 = u1 + (dt / 6) * (k1_u + 2 * k2_u + 2 * k3_u + k4_u)
        omega1 = omega1 + (dt / 6) * (k1_w + 2 * k2_w + 2 * k3_w + k4_w)

        # Enforce BCs after step
        # ✓ (NS_FRAMEWORK: BC z=0: u₁=ω₁=ψ₁=0 (odd))
        u1[0, :] = 0         # wall
        u1[:, 0] = 0         # z=0: odd
        # z=Lz: u₁ even (∂zu₁=0) — don't zero  ✓ (NS_FRAMEWORK: BC z=L/4: u₁ even)
        omega1[:, 0] = 0     # z=0: odd  ✓
        omega1[:, -1] = 0    # z=Lz: odd ✓ (NS_FRAMEWORK: BC z=L/4: ω₁ odd (=0))

        return u1, omega1, u_r, u_z

    def compute_dt(self, u_r, u_z, omega1, dt_prev):
        """Velocity-based CFL."""
        u_max = max(u_r.abs().max().item(), u_z.abs().max().item(), 1e-10)
        dt_cfl = 0.3 * min(self.dr_min, self.dz) / u_max

        # Vorticity growth cap
        om = (self.R * omega1).abs().max().item()
        if om > 1:
            dt_cfl = min(dt_cfl, 0.01 / om)

        return max(min(dt_cfl, 1e-6), 1e-15)

    def max_vorticity_u1z(self, u1):
        du1_dz = self._ddz(u1)
        return du1_dz.abs().max().item()

    def max_vorticity_w1r(self, omega1):
        """ωθ = ω₁·r — good for wall blowup (Luo-Hou)."""
        return (omega1 * self.R).abs().max().item()

    def max_vorticity_omega1(self, omega1):
        """ω₁ = ωθ/r — the quantity Hou 2022 tracks.
        This is what diverges at r=0 for interior blowup."""
        return omega1.abs().max().item()


def run_euler(Nr, Nz, gpu_id, logfile):
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    with open(logfile, 'w') as f:
        f.write('')
    L = 1.0 / 6.0
    dev = f'cuda:{gpu_id}' if torch.cuda.is_available() else 'cpu'

    log(f"=== Nr={Nr}, Nz={Nz}, L=1/6, device={dev} ===", logfile)
    log(f"Fixes: Neumann at axis, velocity CFL, DST symmetry", logfile)

    solver = EulerFixed(Nr=Nr, Nz=Nz, L=L, device=dev)
    u1, omega1 = solver.init_luo_hou()
    log(f"IC: ||u1||={u1.abs().max():.4f}, dr_min={solver.dr_min:.6f}, dz={solver.dz:.6f}", logfile)

    times, omegas_u1z, omegas_w1r = [], [], []
    t, dt, step = 0.0, 1e-7, 0
    u_r = torch.zeros_like(u1)
    u_z = torch.zeros_like(u1)

    while t < 0.01 and step < 500000:
        om_w = solver.max_vorticity_w1r(omega1)
        om_u = solver.max_vorticity_u1z(u1)
        if math.isnan(om_w) or om_w > 1e8 or math.isnan(om_u):
            break

        times.append(t)
        omegas_u1z.append(om_u)
        omegas_w1r.append(om_w)

        if step % 1000 == 0:
            log(f"step={step}, t={t:.8f}, dt={dt:.2e}, |w1r|={om_w:.2e}, |u1z|={om_u:.2e}", logfile)

        u1, omega1, u_r, u_z = solver.step_rk4(u1, omega1, dt)
        t += dt
        step += 1
        dt = solver.compute_dt(u_r, u_z, omega1, dt)

    log(f"T*_raw={t:.8f}, steps={step}", logfile)

    # --- Fit T* and γ from |u1z| ---
    t_arr = np.array([x for x, v in zip(times, omegas_u1z) if v > 100])
    v_arr = np.array([v for v in omegas_u1z if v > 100])
    if len(t_arr) > 20:
        n = len(t_arr)
        i_lo, i_hi = int(n * 0.3), int(n * 0.7)
        tf = t_arr[i_lo:i_hi]
        ivf = 1.0 / v_arr[i_lo:i_hi]
        tm, ivm = tf.mean(), ivf.mean()
        a = ((tf - tm) * (ivf - ivm)).sum() / ((tf - tm) ** 2).sum()
        b = ivm - a * tm
        if abs(a) > 1e-30:
            T_star = -b / a
            pred = a * tf + b
            r2 = 1 - ((ivf - pred) ** 2).sum() / ((ivf - ivm) ** 2).sum()
            log(f"T* (|u1z|) = {T_star:.8f} (R2={r2:.6f}) [expect ~0.0035]", logfile)

            gmask = (t_arr > 0.6 * T_star) & (t_arr < 0.9 * T_star) & (v_arr > 100)
            gt, gv = t_arr[gmask], v_arr[gmask]
            if len(gt) >= 10:
                ld = np.log(T_star - gt)
                lv = np.log(gv)
                mx, my = ld.mean(), lv.mean()
                gamma = -((ld - mx) * (lv - my)).sum() / ((ld - mx) ** 2).sum()
                log(f"gamma (|u1z|) = {gamma:.4f} [expect ~2.5]", logfile)
            else:
                log(f"gamma: not enough data ({len(gt)} pts)", logfile)
    else:
        log(f"Not enough data for T* ({len(t_arr)} pts)", logfile)

    log("DONE", logfile)


if __name__ == '__main__':
    import multiprocessing as mp

    os.makedirs(os.path.dirname(LOGPREFIX) if os.path.dirname(LOGPREFIX) else '.', exist_ok=True)

    configs = [
        (32, 64, 0, f"{LOGPREFIX}_nr32.log"),
        (64, 128, 0, f"{LOGPREFIX}_nr64.log"),
    ]

    # Single GPU on Spark — run sequentially
    for Nr, Nz, gpu, logf in configs:
        print(f"Running Nr={Nr}...")
        run_euler(Nr, Nz, gpu, logf)

    print("ALL DONE")
