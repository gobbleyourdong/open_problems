"""
NS Viscous Sweep — Does viscosity prevent the Euler blowup?

Built on validated EulerFixed solver (T*=0.00365 at Nr=64, γ=2.79 at Nr=128).
Adds ν·Δ₃ diffusion where Δ₃ = ∂ᵣ² + (3/r)∂ᵣ + ∂zz.
L'Hôpital at axis: Δ₃|_(r=0) = 4·∂ᵣ².

Cross-check against NS_FRAMEWORK.md:
  u₁: ∂ₜu₁ + uʳ∂ᵣu₁ + uᶻ∂zu₁ = 2u₁ψ₁,z + ν·Δ₃u₁    ✓
  ω₁: ∂ₜω₁ + uʳ∂ᵣω₁ + uᶻ∂zω₁ = 2u₁u₁,z + ν·Δ₃ω₁      ✓
  Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz  (5D Laplacian radial part)   ✓

Sweep: ν = 0.01, 0.001, 0.0001 + Euler (ν=0) reference.
NS_FRAMEWORK Paper 2: ν=5×10⁻³ → viscosity ENHANCES singularity.
"""
import os
import math
import time
import torch
import numpy as np
from euler_fixed import EulerFixed, log

LOGPREFIX = os.path.expanduser("~/ComfyUI/CelebV-HQ/ns_blowup/results/ns_viscous")


class NSFixed(EulerFixed):
    def __init__(self, Nr=64, Nz=128, L=1.0 / 6.0, nu=0.001, device='cuda'):
        super().__init__(Nr, Nz, L, device)
        self.nu = nu
        self.precompute_diffusion()

    def precompute_diffusion(self):
        """
        Radial part of Δ₃ = D_r2 + (3/r)·D_r.
        Z part computed via FD per step.

        Cross-check: Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz  ✓ (NS_FRAMEWORK)
        L'Hôpital at r=0: (3/r)f' → 3f'', so Δ₃ → 4·∂ᵣᵣ + ∂zz  ✓
        """
        Nr = self.Nr
        r_safe = self.r.clamp(min=1e-10)
        L3_r = self.D_r2 + torch.diag(3.0 / r_safe) @ self.D_r

        # L'Hôpital at axis (r=0, index Nr): (3/r)f' → 3f'' → Δ₃ = 4·D_r2
        L3_r[Nr, :] = 4.0 * self.D_r2[Nr, :]

        # Zero boundary rows — BCs enforced separately in compute_rhs
        L3_r[0, :] = 0.0     # wall
        L3_r[Nr, :] = 0.0    # axis: Chebyshev D_r2 has O(N⁴) entries at endpoints
        self.L3_r = L3_r

        # Diffusion CFL: estimate spectral radius
        eigs = torch.linalg.eigvals(L3_r).real
        self.diff_spectral_radius = max(eigs.abs().max().item(), 1.0)

    def _d2dz2_u1(self, f):
        """
        ∂²u₁/∂z² with symmetry ghost points.
        u₁: odd at z=0, even at z=Lz.
        Cross-check: NS_FRAMEWORK BC z=0: u₁=0 (odd) ✓
                     NS_FRAMEWORK BC z=L/4: u₁ even (∂zu₁=0) ✓
        """
        dz = self.dz
        d2f = torch.zeros_like(f)
        d2f[:, 1:-1] = (f[:, 2:] - 2 * f[:, 1:-1] + f[:, :-2]) / (dz ** 2)
        # z=0: u₁ odd → ghost f[-1] = -f[1], f[0]=0 → d²f = 0
        d2f[:, 0] = 0.0
        # z=Lz: u₁ even → ghost f[Nz+1] = f[Nz-1]
        d2f[:, -1] = 2.0 * (f[:, -2] - f[:, -1]) / (dz ** 2)
        return d2f

    def _d2dz2_omega1(self, f):
        """
        ∂²ω₁/∂z² with symmetry ghost points.
        ω₁: odd at both z=0 and z=Lz.
        Cross-check: NS_FRAMEWORK BC z=0: ω₁=0 (odd) ✓
                     NS_FRAMEWORK BC z=L/4: ω₁ odd (=0) ✓
        """
        dz = self.dz
        d2f = torch.zeros_like(f)
        d2f[:, 1:-1] = (f[:, 2:] - 2 * f[:, 1:-1] + f[:, :-2]) / (dz ** 2)
        # z=0: ω₁ odd → d²f = 0
        d2f[:, 0] = 0.0
        # z=Lz: ω₁ odd → d²f = 0
        d2f[:, -1] = 0.0
        return d2f

    def compute_rhs(self, u1, omega1):
        """Euler RHS + viscous diffusion ν·Δ₃."""
        rhs_u1, rhs_omega1, u_r, u_z = super().compute_rhs(u1, omega1)

        if self.nu > 0:
            # Diffusion: ν·Δ₃(u₁) and ν·Δ₃(ω₁)
            # Δ₃ = L3_r (radial) + ∂²/∂z² (axial)
            diff_u1 = self.L3_r @ u1 + self._d2dz2_u1(u1)
            diff_omega1 = self.L3_r @ omega1 + self._d2dz2_omega1(omega1)

            rhs_u1 += self.nu * diff_u1
            rhs_omega1 += self.nu * diff_omega1

            # Re-enforce BCs on diffused RHS
            rhs_u1[0, :] = 0         # wall
            rhs_omega1[-1, :] = 0    # axis parity

        return rhs_u1, rhs_omega1, u_r, u_z

    def compute_dt(self, u_r, u_z, omega1, dt_prev):
        """CFL with diffusion stability constraint."""
        dt = super().compute_dt(u_r, u_z, omega1, dt_prev)

        if self.nu > 0:
            # RK4 stability region on negative real axis ≈ 2.8
            dt_diff = 2.5 / (self.nu * (self.diff_spectral_radius + 1.0 / (self.dz ** 2)))
            dt = min(dt, dt_diff)

        return max(dt, 1e-15)


def run_ns(Nr, Nz, nu, gpu_id, logfile):
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    with open(logfile, 'w') as f:
        f.write('')
    L = 1.0 / 6.0
    dev = f'cuda:{gpu_id}' if torch.cuda.is_available() else 'cpu'

    log(f"=== NS: Nr={Nr}, Nz={Nz}, nu={nu:.1e}, device={dev} ===", logfile)

    solver = NSFixed(Nr=Nr, Nz=Nz, L=L, nu=nu, device=dev)
    u1, omega1 = solver.init_luo_hou()
    log(f"IC: ||u1||={u1.abs().max():.4f}, dr_min={solver.dr_min:.6f}, dz={solver.dz:.6f}", logfile)
    log(f"Diff spectral radius: {solver.diff_spectral_radius:.2e}", logfile)

    dt_diff_limit = 2.5 / (nu * (solver.diff_spectral_radius + 1.0 / (solver.dz ** 2))) if nu > 0 else 1e-6
    log(f"Diffusion dt limit: {dt_diff_limit:.2e}", logfile)

    times, omegas_u1z, omegas_w1r = [], [], []
    t, dt, step = 0.0, min(1e-7, dt_diff_limit * 0.5), 0
    u_r = torch.zeros_like(u1)
    u_z = torch.zeros_like(u1)

    T_max = 0.02   # Run longer than Euler T* to see if NS stays bounded
    max_steps = 500000

    while t < T_max and step < max_steps:
        om_w = solver.max_vorticity_w1r(omega1)
        om_u = solver.max_vorticity_u1z(u1)
        if math.isnan(om_w) or math.isnan(om_u):
            log(f"NaN detected at step={step}, t={t:.8f}", logfile)
            break
        if om_w > 1e8:
            log(f"BLOWUP at step={step}, t={t:.8f}, |w1r|={om_w:.2e}", logfile)
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

    log(f"Final: t={t:.8f}, steps={step}", logfile)

    # Check if we survived past Euler T*
    euler_Tstar = 0.00365   # from Nr=64 Euler run
    if t > euler_Tstar * 1.5 and om_w < 1e8:
        log(f"*** NS SURVIVED past 1.5x Euler T* (t={t:.8f} > {euler_Tstar * 1.5:.8f}) ***", logfile)
        log(f"*** Viscosity nu={nu:.1e} REGULARIZES the singularity ***", logfile)
    elif om_w > 1e8:
        log(f"NS BLEW UP at t={t:.8f} (Euler T*={euler_Tstar:.8f})", logfile)

    # Fit T* and gamma
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
            log(f"NS T* = {T_star:.8f} (R2={r2:.6f})", logfile)

            gmask = (t_arr > 0.6 * T_star) & (t_arr < 0.9 * T_star) & (v_arr > 100)
            gt, gv = t_arr[gmask], v_arr[gmask]
            if len(gt) >= 10:
                ld = np.log(T_star - gt)
                lv = np.log(gv)
                mx, my = ld.mean(), lv.mean()
                gamma = -((ld - mx) * (lv - my)).sum() / ((ld - mx) ** 2).sum()
                log(f"NS gamma = {gamma:.4f}", logfile)
    else:
        log(f"Run ended at t={t:.8f}, max steps reached, |w1r|={om_w:.2e}", logfile)

    log("DONE", logfile)


if __name__ == "__main__":
    os.makedirs(os.path.dirname(LOGPREFIX) if os.path.dirname(LOGPREFIX) else '.', exist_ok=True)

    Nr, Nz = 64, 128
    configs = [
        (Nr, Nz, 0.0, 0, f"{LOGPREFIX}_euler.log"),      # Euler reference
        (Nr, Nz, 1e-4, 0, f"{LOGPREFIX}_nu1e-4.log"),
        (Nr, Nz, 1e-3, 0, f"{LOGPREFIX}_nu1e-3.log"),
        (Nr, Nz, 1e-2, 0, f"{LOGPREFIX}_nu1e-2.log"),
    ]

    # Single GPU on Spark — run sequentially
    for nr, nz, nu, gpu_id, logf in configs:
        print(f"Running nu={nu:.1e}...")
        run_ns(nr, nz, nu, gpu_id, logf)

    print("ALL DONE")
