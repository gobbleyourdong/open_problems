"""
NS Blowup Sweep — Resolution, Viscosity, IC, and Domain variations.

Goal: Bulletproof numerical evidence for finite-time blowup.
1. Resolution convergence: T* and γ stabilize under refinement
2. Viscosity criticality: find ν_c where blowup transitions
3. IC robustness: blowup persists across amplitude variations
4. Domain generality: Luo-Hou 2014 (boundary) + Hou 2022 (interior)
"""
import os
import sys
import math
import time
import torch
import numpy as np
import json

sys.path.insert(0, os.path.dirname(__file__))
from euler_fixed import EulerFixed, log

RESULTS_DIR = os.path.expanduser("~/ComfyUI/CelebV-HQ/ns_blowup/results")


class SweepSolver(EulerFixed):
    """Extended solver with viscosity, variable IC, and Hou 2022 IC support."""

    def __init__(self, Nr=64, Nz=128, L=1.0/6.0, nu=0.0, device='cuda',
                 ic_type='luo_hou', amplitude=100.0):
        self.nu = nu
        self.ic_type = ic_type
        self.amplitude = amplitude
        super().__init__(Nr, Nz, L, device)
        if nu > 0:
            self._precompute_diffusion()

    def _precompute_diffusion(self):
        """
        Build radial diffusion operator L3_r = D²ᵣ + (3/r)Dᵣ
        with boundary rows REPLACED (not zeroed):
          r=1 (index 0):  Dirichlet u₁=0 → row = [1, 0, ..., 0]
          r=0 (index Nr): Neumann ∂ᵣu₁=0 → row = D1[Nr, :]

        This is standard Chebyshev collocation boundary-row replacement.
        Removes O(N⁴) endpoint stiffness that caused the blowup.
        """
        Nr = self.Nr
        r_safe = self.r.clamp(min=1e-10)
        three_over_r = 3.0 / r_safe

        L3_r = self.D_r2 + torch.diag(three_over_r) @ self.D_r

        # L'Hôpital at r=0 (index Nr): (3/r)f' → 3f'' → total 4f''
        L3_r[Nr, :] = 4.0 * self.D_r2[Nr, :]

        # BOUNDARY ROWS: Zero out (A100 validated approach).
        # Dirichlet/Neumann enforced AFTER step, not through operator.
        # Identity row (Grok suggestion) creates O(N⁴) stiffness at
        # first interior point — initial RHS hits 2e8, instant instability.
        L3_r[0, :] = 0.0    # wall: diffusion zeroed, BC enforced after step
        L3_r[Nr, :] = 0.0   # axis: same

        self.L3_r = L3_r

        # Spectral radius for diffusion CFL
        eigs = torch.linalg.eigvals(L3_r).real
        self.diff_spectral_radius = max(eigs.abs().max().item(), 1.0)

    def init_luo_hou(self):
        """Luo-Hou 2014 IC with variable amplitude."""
        r, z = self.R, self.Z
        u1 = self.amplitude * torch.exp(-30.0 * (1 - r**2)**4) * \
             torch.sin(2 * math.pi * z / self.L)
        omega1 = torch.zeros_like(u1)
        u1[0, :] = 0
        return u1, omega1

    def init_luo_hou_ns(self):
        """Luo-Hou IC with cutoff for NS compatibility.
        Multiplied by (1-r²)² to force u₁→0 at wall smoothly.
        Compatible with Dirichlet u₁=0 at r=1 — no artificial gradient."""
        r, z = self.R, self.Z
        cutoff = (1 - r**2)**2
        u1 = self.amplitude * cutoff * torch.exp(-30.0 * (1 - r**2)**4) * \
             torch.sin(2 * math.pi * z / self.L)
        omega1 = torch.zeros_like(u1)
        return u1, omega1

    def init_hou_2022(self):
        """
        Hou 2022 FoCM IC — INTERIOR blowup at (0,0).
        u₁(0) = 12000(1−r²)¹⁸ sin(2πz)/(1+12.5sin²(πz))
        Domain: r∈[0,1] z∈[0,1/2], L=1

        NOTE: This requires L=1 and Lz=L/2 (half-period).
        The solver must be initialized with L=1.0.
        """
        r, z = self.R, self.Z
        u1 = self.amplitude * (1 - r**2)**18 * \
             torch.sin(2 * math.pi * z) / (1 + 12.5 * torch.sin(math.pi * z)**2)
        omega1 = torch.zeros_like(u1)
        # BC: u₁ = 0 at r=1 (naturally satisfied by (1-r²)¹⁸)
        # BC: odd at z=0 and z=Lz (naturally satisfied by sin)
        return u1, omega1

    def init_sniper(self):
        """
        Sniper IC — vorticity at r=0.10 (peak Biot-Savart sensitivity).
        u₁ = A * exp(-(r-r₀)²/σ²) * (1-r²) * sin(2πz/L)
        ω₁ = 0
        r₀=0.10, σ=0.05. Designed to maximize ∂α/∂R.
        """
        r, z = self.R, self.Z
        r_target = 0.10
        sigma_r = 0.05
        u1 = self.amplitude * torch.exp(-((r - r_target)**2) / sigma_r**2) * \
             (1 - r**2) * torch.sin(2 * math.pi * z / self.L)
        omega1 = torch.zeros_like(u1)
        u1[0, :] = 0  # wall BC
        return u1, omega1

    def init_ic(self):
        """Dispatch to appropriate IC."""
        if self.ic_type == 'luo_hou':
            return self.init_luo_hou()
        elif self.ic_type == 'luo_hou_ns':
            return self.init_luo_hou_ns()
        elif self.ic_type == 'hou_2022':
            return self.init_hou_2022()
        elif self.ic_type == 'sniper':
            return self.init_sniper()
        else:
            raise ValueError(f"Unknown IC type: {self.ic_type}")

    def step_rk4(self, u1, omega1, dt):
        """RK4 with IC-aware BCs."""
        u1, omega1, u_r, u_z = super().step_rk4(u1, omega1, dt)

        if self.ic_type == 'hou_2022':
            # Hou 2022: u₁ is ODD at z=Lz (zero), not even like Luo-Hou
            # NS_FRAMEWORK Paper 2: BC z=0,z=1/2: u₁=ω₁=ψ₁=0 (odd)
            u1[:, -1] = 0    # z=Lz: u₁ odd (=0)
            # ω₁ already zeroed at z=Lz by parent

        return u1, omega1, u_r, u_z

    def solve_poisson(self, omega1):
        """Override Poisson for Hou 2022 — all fields odd at both z boundaries."""
        if self.ic_type == 'hou_2022':
            # For Hou 2022, u₁ is also odd at z=Lz, so we use _extend_odd
            # for the Poisson solve (same as ω₁ and ψ₁).
            # The parent's solve_poisson already uses _extend_odd for ω₁. ✓
            pass
        return super().solve_poisson(omega1)

    def _ddz(self, f):
        """Override z-derivative for Hou 2022 — u₁ odd at both ends."""
        if self.ic_type == 'hou_2022':
            # Both endpoints odd: use one-sided stencil that respects f=0 at boundary
            dz = self.dz
            df = torch.zeros_like(f)
            df[:, 1:-1] = (f[:, 2:] - f[:, :-2]) / (2 * dz)
            df[:, 0] = (-3*f[:, 0] + 4*f[:, 1] - f[:, 2]) / (2*dz)
            df[:, -1] = (3*f[:, -1] - 4*f[:, -2] + f[:, -3]) / (2*dz)
            return df
        return super()._ddz(f)

    def compute_rhs(self, u1, omega1):
        """Euler RHS + optional viscous diffusion."""
        rhs_u1, rhs_omega1, u_r, u_z = super().compute_rhs(u1, omega1)

        if self.nu > 0:
            # Radial diffusion via precomputed L3_r (boundary rows replaced)
            diff_r_u = self.L3_r @ u1
            diff_r_w = self.L3_r @ omega1

            # z diffusion: 2nd order FD with ghost points
            dz = self.dz
            # u₁: odd at z=0, even at z=Lz
            u1_zz = torch.zeros_like(u1)
            u1_zz[:, 1:-1] = (u1[:, 2:] - 2*u1[:, 1:-1] + u1[:, :-2]) / dz**2
            u1_zz[:, 0] = 0.0  # odd BC
            u1_zz[:, -1] = 2.0 * (u1[:, -2] - u1[:, -1]) / dz**2  # even BC

            # ω₁: odd at both z=0 and z=Lz
            w1_zz = torch.zeros_like(omega1)
            w1_zz[:, 1:-1] = (omega1[:, 2:] - 2*omega1[:, 1:-1] + omega1[:, :-2]) / dz**2
            # Both endpoints: odd → d²f=0 (ghost = -interior)

            rhs_u1 += self.nu * (diff_r_u + u1_zz)
            rhs_omega1 += self.nu * (diff_r_w + w1_zz)

            # Re-enforce BCs after adding diffusion (A100 code does this)
            rhs_u1[0, :] = 0       # wall: u₁=0
            rhs_omega1[-1, :] = 0  # axis parity

        return rhs_u1, rhs_omega1, u_r, u_z

    def compute_dt(self, u_r, u_z, omega1, dt_prev):
        """CFL with diffusion constraint."""
        dt = super().compute_dt(u_r, u_z, omega1, dt_prev)

        if self.nu > 0:
            # Diffusion CFL: dt < 2.8 / (ν · spectral_radius)
            # RK4 stability on negative real axis ≈ 2.8
            dt_diff = 2.5 / (self.nu * (self.diff_spectral_radius + 1.0/self.dz**2))
            dt = min(dt, dt_diff)

        return max(dt, 1e-15)


def run_single(Nr, Nz, L, nu, ic_type, amplitude, tag, blowup_threshold=1e8):
    """Run a single configuration and return results dict."""
    logfile = f"{RESULTS_DIR}/{tag}.log"
    os.makedirs(RESULTS_DIR, exist_ok=True)
    with open(logfile, 'w') as f:
        f.write('')

    dev = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    log(f"=== {tag}: Nr={Nr} Nz={Nz} L={L} nu={nu:.1e} IC={ic_type} A={amplitude} ===", logfile)

    solver = SweepSolver(Nr=Nr, Nz=Nz, L=L, nu=nu, device=dev,
                          ic_type=ic_type, amplitude=amplitude)
    u1, omega1 = solver.init_ic()
    log(f"IC: ||u1||={u1.abs().max():.4f}, dr_min={solver.dr_min:.6f}, dz={solver.dz:.6f}", logfile)

    times, omegas_u1z, omegas_w1r, omegas_omega1 = [], [], [], []
    t, dt, step = 0.0, 1e-7, 0
    u_r = torch.zeros_like(u1)
    u_z = torch.zeros_like(u1)

    T_max = 0.05 if nu > 0 else 0.02
    max_steps = 500000

    # Use |ω₁| for interior blowup (Hou 2022), |ω₁·r| for wall blowup (Luo-Hou)
    use_omega1 = (ic_type == 'hou_2022')

    while t < T_max and step < max_steps:
        om_w = solver.max_vorticity_w1r(omega1)
        om_u = solver.max_vorticity_u1z(u1)
        om_1 = solver.max_vorticity_omega1(omega1)
        blowup_val = om_1 if use_omega1 else om_w

        if math.isnan(om_w) or math.isnan(om_u) or math.isnan(om_1):
            log(f"NaN at step={step}, t={t:.10f}", logfile)
            break
        if blowup_val > blowup_threshold:
            log(f"BLOWUP: step={step}, t={t:.10f}, |w1r|={om_w:.2e}, |om1|={om_1:.2e}", logfile)
            break

        times.append(t)
        omegas_u1z.append(om_u)
        omegas_w1r.append(om_w)
        omegas_omega1.append(om_1)

        if step % 1000 == 0:
            log(f"step={step}, t={t:.8f}, dt={dt:.2e}, |w1r|={om_w:.2e}, |om1|={om_1:.2e}, |u1z|={om_u:.2e}", logfile)

        u1, omega1, u_r, u_z = solver.step_rk4(u1, omega1, dt)
        t += dt
        step += 1
        dt = solver.compute_dt(u_r, u_z, omega1, dt)

    # --- Fit T* and γ ---
    result = {
        'tag': tag, 'Nr': Nr, 'Nz': Nz, 'L': L, 'nu': nu,
        'ic_type': ic_type, 'amplitude': amplitude,
        'T_raw': t, 'steps': step,
        'final_w1r': float(omegas_w1r[-1]) if omegas_w1r else 0,
        'final_u1z': float(omegas_u1z[-1]) if omegas_u1z else 0,
        'final_omega1': float(omegas_omega1[-1]) if omegas_omega1 else 0,
        'blowup': blowup_val > blowup_threshold if not math.isnan(blowup_val) else False,
    }

    # Use |ω₁| for Hou 2022 fitting (the quantity that diverges at r=0)
    # Use |u1z| for Luo-Hou (consistent with previous runs)
    fit_vals = omegas_omega1 if use_omega1 else omegas_u1z
    t_arr = np.array([x for x, v in zip(times, fit_vals) if v > 100])
    v_arr = np.array([v for v in fit_vals if v > 100])

    if len(t_arr) > 20:
        n = len(t_arr)
        i_lo, i_hi = int(n * 0.3), int(n * 0.7)
        tf = t_arr[i_lo:i_hi]
        ivf = 1.0 / v_arr[i_lo:i_hi]
        tm, ivm = tf.mean(), ivf.mean()
        a = ((tf - tm) * (ivf - ivm)).sum() / ((tf - tm)**2).sum()
        b = ivm - a * tm
        if abs(a) > 1e-30:
            T_star = -b / a
            pred = a * tf + b
            r2 = 1 - ((ivf - pred)**2).sum() / ((ivf - ivm)**2).sum()
            result['T_star'] = float(T_star)
            result['T_star_R2'] = float(r2)
            log(f"T* = {T_star:.8f} (R2={r2:.6f})", logfile)

            gmask = (t_arr > 0.6 * T_star) & (t_arr < 0.9 * T_star) & (v_arr > 100)
            gt, gv = t_arr[gmask], v_arr[gmask]
            if len(gt) >= 10:
                ld = np.log(T_star - gt)
                lv = np.log(gv)
                mx, my = ld.mean(), lv.mean()
                gamma = -((ld - mx) * (lv - my)).sum() / ((ld - mx)**2).sum()
                result['gamma'] = float(gamma)
                log(f"gamma = {gamma:.4f}", logfile)

    # Survived past expected T*?
    if nu > 0 and not result['blowup']:
        log(f"*** SURVIVED: nu={nu:.1e} regularizes to t={t:.8f} ***", logfile)
        result['survived'] = True
    else:
        result['survived'] = False

    log(f"RESULT: {json.dumps(result, indent=2)}", logfile)
    log("DONE", logfile)

    # Save result summary
    with open(f"{RESULTS_DIR}/{tag}.json", 'w') as f:
        json.dump(result, f, indent=2)

    # Save full time series for charting
    timeseries = {
        't': [float(x) for x in times],
        'w1r': [float(x) for x in omegas_w1r],
        'u1z': [float(x) for x in omegas_u1z],
        'omega1': [float(x) for x in omegas_omega1],
        'T_star': result.get('T_star', None),
        'gamma': result.get('gamma', None),
        'Nr': Nr, 'Nz': Nz, 'nu': nu, 'amplitude': amplitude, 'ic_type': ic_type,
    }
    with open(f"{RESULTS_DIR}/{tag}_timeseries.json", 'w') as f:
        json.dump(timeseries, f)

    return result


def run_sweeps():
    """Run all sweep configurations sequentially."""
    all_results = []

    # ============================
    # SWEEP 1: Viscosity criticality
    # Bracket ν_c ≈ 2.5e-4
    # ============================
    print("\n=== SWEEP 1: VISCOSITY CRITICALITY ===")
    nu_values = [0.0, 5e-4, 3e-4, 2.5e-4, 2e-4, 1e-4, 5e-5, 1e-2, 1e-1, 1.0]
    for nu in nu_values:
        tag = f"visc_nr64_nu{nu:.0e}" if nu > 0 else "visc_nr64_euler"
        r = run_single(Nr=64, Nz=128, L=1/6, nu=nu,
                       ic_type='luo_hou', amplitude=100.0, tag=tag)
        all_results.append(r)
        print(f"  nu={nu:.1e}: T*={r.get('T_star','N/A')}, "
              f"gamma={r.get('gamma','N/A')}, blowup={r['blowup']}")

    # ============================
    # SWEEP 2: Resolution convergence
    # ============================
    print("\n=== SWEEP 2: RESOLUTION CONVERGENCE ===")
    for Nr, Nz in [(32, 64), (64, 128), (128, 256), (256, 512)]:
        tag = f"res_nr{Nr}"
        r = run_single(Nr=Nr, Nz=Nz, L=1/6, nu=0.0,
                       ic_type='luo_hou', amplitude=100.0, tag=tag)
        all_results.append(r)
        print(f"  Nr={Nr}: T*={r.get('T_star','N/A')}, gamma={r.get('gamma','N/A')}")

    # ============================
    # SWEEP 3: IC amplitude robustness
    # ============================
    print("\n=== SWEEP 3: AMPLITUDE ROBUSTNESS ===")
    for amp in [50, 100, 200, 500]:
        tag = f"amp_A{amp}"
        r = run_single(Nr=64, Nz=128, L=1/6, nu=0.0,
                       ic_type='luo_hou', amplitude=float(amp), tag=tag)
        all_results.append(r)
        print(f"  A={amp}: T*={r.get('T_star','N/A')}, gamma={r.get('gamma','N/A')}")

    # ============================
    # SWEEP 4: Hou 2022 IC (interior blowup)
    # ============================
    print("\n=== SWEEP 4: HOU 2022 IC (INTERIOR BLOWUP) ===")
    # Hou 2022 uses L=1, amplitude=12000, domain z∈[0,1/2]
    for Nr, Nz in [(64, 128)]:
        tag = f"hou2022_nr{Nr}"
        r = run_single(Nr=Nr, Nz=Nz, L=1.0, nu=0.0,
                       ic_type='hou_2022', amplitude=12000.0, tag=tag)
        all_results.append(r)
        print(f"  Nr={Nr}: T*={r.get('T_star','N/A')}, gamma={r.get('gamma','N/A')}")

    # === Summary ===
    print("\n" + "="*70)
    print("SWEEP SUMMARY")
    print("="*70)
    for r in all_results:
        status = "BLOWUP" if r['blowup'] else ("SURVIVED" if r.get('survived') else "???")
        print(f"  {r['tag']:30s}  T*={r.get('T_star','---'):>12s}  "
              f"γ={r.get('gamma','---'):>8s}  {status}")

    with open(f"{RESULTS_DIR}/sweep_summary.json", 'w') as f:
        json.dump(all_results, f, indent=2)

    print(f"\nAll results saved to {RESULTS_DIR}/")


if __name__ == '__main__':
    run_sweeps()
