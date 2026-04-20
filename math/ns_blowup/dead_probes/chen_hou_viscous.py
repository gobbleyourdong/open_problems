"""
Chen-Hou dynamic rescaling equations + viscosity.

Their EXACT equations (F_pertb_2lev.m lines 139-140):

  Fv = -(c_l*x1 + u1).*vx1 - (c_l*x2 + u2).*vx2 + (2*c_w - u1dx1).*v
  Fw = -(c_l*x1 + u1).*wx1 - (c_l*x2 + u2).*wx2 + c_w*w + v + x1.*vx1

Where:
  v = u₁ (azimuthal velocity / r)
  w = ω₁ (azimuthal vorticity / r)
  x1 = r, x2 = z (self-similar coordinates)
  u1, u2 = radial/axial velocity from Poisson solve
  c_l = 3.0065 (spatial rescaling rate)
  c_w = -1.0294 (vorticity rescaling rate)
  u1dx1 = ∂u_r/∂r at axis

The normalization (line 136-137):
  c_l = 4 * vx1(0,0) / wx1(0,0)
  c_w = u1dx1(0,0) + c_l/2

WE ADD: ν * (L3_r + ∂²z) to both Fv and Fw.

At ν=0 and the saved profile, Fv ≈ Fw ≈ 3e-10 (nearly exact steady state).
At ν>0, the viscous term perturbs the fixed point. Does it survive?

NOTE: We use FIXED c_l, c_w (no dynamic renormalization) so we can
cleanly see whether viscosity pushes the profile away from equilibrium.
Dynamic renormalization would track the profile but mask the viscous effect.
"""
import sys, os, math, time, json
import torch
import numpy as np
import scipy.io as sio

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver


class ChenHouSolver(SweepSolver):
    """
    Chen-Hou dynamic rescaling equations with optional viscosity.

    Overrides compute_rhs to use their equations instead of physical-frame NS.
    Uses FIXED c_l, c_w from their steady state.
    """

    def __init__(self, Nr=64, Nz=128, L=1.0/6.0, nu=0.0, device='cuda',
                 cl=3.006498, cw=-1.029425, **kwargs):
        self.cl_ch = cl
        self.cw_ch = cw
        super().__init__(Nr=Nr, Nz=Nz, L=L, nu=nu, device=device,
                         ic_type='luo_hou', amplitude=1.0)

        # Precompute coordinate grids for drift terms
        self.x1_2d = self.R   # r grid, shape (Nr+1, Nz+1)
        self.x2_2d = self.Z   # z grid, shape (Nr+1, Nz+1)

    def compute_rhs(self, v, w):
        """
        Chen-Hou RHS (lines 139-140) + viscous diffusion.

        Fv = -(c_l*r + u_r) * ∂v/∂r - (c_l*z + u_z) * ∂v/∂z + (2*c_w - ∂u_r/∂r) * v
        Fw = -(c_l*r + u_r) * ∂w/∂r - (c_l*z + u_z) * ∂w/∂z + c_w*w + v + r*∂v/∂r

        + ν * Δ(v) and ν * Δ(w) if nu > 0
        """
        # Solve Poisson: -Δψ₁ = w
        psi1 = self.solve_poisson(w)

        # Velocity from stream function
        dpsi_dz = self._ddz(psi1)
        dpsi_dr = self.D_r @ psi1
        u_r = -self.R * dpsi_dz       # radial velocity
        u_z = 2 * psi1 + self.R * dpsi_dr  # axial velocity

        # Spatial derivatives of v and w
        vx1 = self.D_r @ v             # ∂v/∂r
        vx2 = self._ddz(v)             # ∂v/∂z
        wx1 = self.D_r @ w             # ∂w/∂r
        wx2 = self._ddz(w)             # ∂w/∂z

        # ∂u_r/∂r — need this for the stretching term
        # u_r = -r * ∂ψ₁/∂z, so ∂u_r/∂r = -∂ψ₁/∂z - r * ∂²ψ₁/∂r∂z
        # Simpler: just differentiate u_r directly
        u1dx1 = self.D_r @ u_r         # ∂u_r/∂r

        cl = self.cl_ch
        cw = self.cw_ch

        # Chen-Hou equations (lines 139-140)
        Fv = -(cl * self.x1_2d + u_r) * vx1 \
             - (cl * self.x2_2d + u_z) * vx2 \
             + (2 * cw - u1dx1) * v

        Fw = -(cl * self.x1_2d + u_r) * wx1 \
             - (cl * self.x2_2d + u_z) * wx2 \
             + cw * w + v + self.x1_2d * vx1

        # Add viscous diffusion if nu > 0
        if self.nu > 0:
            diff_r_v = self.L3_r @ v
            diff_r_w = self.L3_r @ w

            dz = self.dz
            # v: z-diffusion (odd at z=0, even at z=Lz for Luo-Hou convention)
            v_zz = torch.zeros_like(v)
            v_zz[:, 1:-1] = (v[:, 2:] - 2*v[:, 1:-1] + v[:, :-2]) / dz**2
            v_zz[:, 0] = 0.0
            v_zz[:, -1] = 2.0 * (v[:, -2] - v[:, -1]) / dz**2

            w_zz = torch.zeros_like(w)
            w_zz[:, 1:-1] = (w[:, 2:] - 2*w[:, 1:-1] + w[:, :-2]) / dz**2

            Fv += self.nu * (diff_r_v + v_zz)
            Fw += self.nu * (diff_r_w + w_zz)

        # Boundary conditions
        Fv[0, :] = 0    # r=1 (wall/far-field)
        Fw[-1, :] = 0   # r=0 (axis parity)

        return Fv, Fw, u_r, u_z


def load_chen_hou_profile(Nr, Nz, L=1.0/6.0, r_scale=5.0, z_scale=5.0):
    """Load and interpolate Chen-Hou profile to our grid."""
    mat_path = os.path.join(os.path.dirname(__file__),
        "chen_hou_matlab", "ASS_data", "Steady_state_pertb720_Nlevcor4.mat")
    mat = sio.loadmat(mat_path)

    v_ch = mat['v']
    w_ch = mat['w']
    mesh = mat['Mesh'][0, 0]
    r_ch = mesh['x'][0, 0].flatten()
    z_ch = mesh['x'][0, 1].flatten()
    solu = mat['solu'][0, 0]
    cl = solu['cl'].item()
    cw = solu['cw'].item()

    # Our grid
    j_arr = np.arange(Nr + 1)
    x = np.cos(np.pi * j_arr / Nr)
    r_our = (1 + x) / 2
    Lz = L / 4.0
    z_our = np.linspace(0, Lz, Nz + 1)

    # Map our coords to Chen-Hou coords
    r_query = r_our * r_scale
    z_query = z_our * (z_scale / Lz)

    # Interpolate
    v_interp = np.zeros((Nr + 1, Nz + 1))
    w_interp = np.zeros((Nr + 1, Nz + 1))

    for j_z, zq in enumerate(z_query):
        z_idx = min(np.searchsorted(z_ch, zq), len(z_ch) - 2)
        z_frac = np.clip((zq - z_ch[z_idx]) / (z_ch[z_idx+1] - z_ch[z_idx] + 1e-30), 0, 1)
        v_at_z = (1 - z_frac) * v_ch[:, z_idx] + z_frac * v_ch[:, z_idx + 1]
        w_at_z = (1 - z_frac) * w_ch[:, z_idx] + z_frac * w_ch[:, z_idx + 1]

        for i_r, rq in enumerate(r_query):
            r_idx = min(np.searchsorted(r_ch, rq), len(r_ch) - 2)
            r_frac = np.clip((rq - r_ch[r_idx]) / (r_ch[r_idx+1] - r_ch[r_idx] + 1e-30), 0, 1)
            v_interp[i_r, j_z] = (1 - r_frac) * v_at_z[r_idx] + r_frac * v_at_z[r_idx + 1]
            w_interp[i_r, j_z] = (1 - r_frac) * w_at_z[r_idx] + r_frac * w_at_z[r_idx + 1]

    return v_interp, w_interp, cl, cw


def run_viscous_homotopy(Nr=64, Nz=128, nu_values=None, n_steps=10000,
                          device='cuda', r_scale=5.0):
    """
    The clean experiment:
    1. Load Chen-Hou exact steady state
    2. Run their equations with ν=0 → should stay at residual ~1e-10
    3. Increase ν → does the fixed point survive?
    """
    if nu_values is None:
        nu_values = [0, 1e-6, 1e-5, 1e-4, 1e-3]

    v_init, w_init, cl, cw = load_chen_hou_profile(Nr, Nz, r_scale=r_scale)

    print(f"Chen-Hou profile: cl={cl:.4f}, cw={cw:.4f}")
    print(f"Interpolated: |v|={abs(v_init).max():.4f}, |w|={abs(w_init).max():.4f}")
    print(f"Domain: r_scale={r_scale}")

    all_results = {}

    for nu in nu_values:
        print(f"\n{'='*60}")
        print(f"ν = {nu:.1e} (Chen-Hou equations + viscosity)")
        print(f"{'='*60}")

        solver = ChenHouSolver(Nr=Nr, Nz=Nz, nu=nu, device=device, cl=cl, cw=cw)

        v = torch.tensor(v_init, dtype=torch.float64, device=device)
        w = torch.tensor(w_init, dtype=torch.float64, device=device)

        # Enforce BCs
        v[0, :] = 0
        v[:, 0] = 0
        w[:, 0] = 0
        w[:, -1] = 0

        v_init_max = v.abs().max().item()
        w_init_max = w.abs().max().item()

        tau, dt = 0.0, 1e-7
        results = []
        t0 = time.time()

        for step in range(n_steps + 1):
            if step % 200 == 0:
                v_max = v.abs().max().item()
                w_max = w.abs().max().item()

                # Compute residual: how far from steady state?
                Fv, Fw, _, _ = solver.compute_rhs(v, w)
                residual_v = Fv.abs().max().item()
                residual_w = Fw.abs().max().item()
                residual = max(residual_v, residual_w)

                # Relative change
                v_ratio = v_max / (v_init_max + 1e-30)
                w_ratio = w_max / (w_init_max + 1e-30)

                # Spectral
                mid_z = w.shape[1] // 2
                if w_max > 1e-15:
                    w_slice = w[:, mid_z].cpu().numpy()
                    coeffs = np.abs(np.fft.rfft(w_slice))
                    n = len(coeffs)
                    low = coeffs[:n//4].mean() + 1e-30
                    high = coeffs[3*n//4:].mean()
                    spec = high / low
                else:
                    spec = 0

                status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")
                elapsed = time.time() - t0

                results.append({
                    'step': step, 'tau': tau,
                    'v_max': v_max, 'w_max': w_max,
                    'v_ratio': v_ratio, 'w_ratio': w_ratio,
                    'residual': residual, 'spectral': spec, 'dt': dt,
                })

                if step % 1000 == 0:
                    print(f"  step={step:5d} τ={tau:.6f} "
                          f"|v|={v_max:.4f}({v_ratio:.4f}×) "
                          f"|w|={w_max:.4e}({w_ratio:.4f}×) "
                          f"res={residual:.2e} spec={spec:.4f} [{status}] [{elapsed:.0f}s]")

            if v.abs().max().item() > 1e6:
                print(f"  BLOWUP at step {step}")
                break
            if v.abs().max().item() < 1e-10 and step > 100:
                print(f"  DECAYED at step {step}")
                break

            v, w, _, _ = solver.step_rk4(v, w, dt)
            tau += dt
            u_r_dummy = torch.zeros_like(v)
            dt = solver.compute_dt(u_r_dummy, u_r_dummy, w, dt)

        # Classify
        if results:
            final = results[-1]
            if final['v_ratio'] > 0.95 and final['v_ratio'] < 1.05:
                outcome = "STEADY"
            elif final['v_ratio'] > 1.05:
                outcome = "GROWING"
            elif final['v_ratio'] < 0.5:
                outcome = "DECAYING"
            else:
                outcome = "DRIFTING"

            print(f"\n  OUTCOME: {outcome}")
            print(f"  |v|: {v_init_max:.4f} → {final['v_max']:.4f} ({final['v_ratio']:.4f}×)")
            print(f"  |w|: {w_init_max:.4e} → {final['w_max']:.4e} ({final['w_ratio']:.4f}×)")
            print(f"  Residual: {final['residual']:.2e}")

            all_results[f'nu_{nu}'] = {
                'nu': nu, 'outcome': outcome,
                'v_ratio': final['v_ratio'], 'w_ratio': final['w_ratio'],
                'residual': final['residual'],
            }

    # Summary
    print(f"\n{'='*60}")
    print(f"HOMOTOPY SUMMARY — Chen-Hou equations + viscosity")
    print(f"{'='*60}")
    print(f"{'ν':>10} {'outcome':>10} {'|v| ratio':>10} {'|w| ratio':>10} {'residual':>12}")
    for key, res in all_results.items():
        print(f"{res['nu']:10.1e} {res['outcome']:>10} "
              f"{res['v_ratio']:10.4f} {res['w_ratio']:10.4f} {res['residual']:12.2e}")

    print(f"\nINTERPRETATION:")
    print(f"  STEADY at ν>0 → fixed point SURVIVES viscosity → NS BLOWUP")
    print(f"  DECAYING at ν>0 → viscosity KILLS the fixed point → regularity")
    print(f"  ν_c where transition happens = critical viscosity")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    summary = [{'nu': r['nu'], 'outcome': r['outcome'],
                'v_ratio': r['v_ratio'], 'w_ratio': r['w_ratio'],
                'residual': r['residual']} for r in all_results.values()]
    out_path = os.path.join(out_dir, f"chen_hou_homotopy_nr{Nr}.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nr', type=int, default=64)
    parser.add_argument('--nz', type=int, default=128)
    parser.add_argument('--steps', type=int, default=10000)
    parser.add_argument('--device', type=str, default='cuda')
    parser.add_argument('--r-scale', type=float, default=5.0)
    args = parser.parse_args()

    run_viscous_homotopy(Nr=args.nr, Nz=args.nz, n_steps=args.steps,
                         device=args.device, r_scale=args.r_scale,
                         nu_values=[0, 1e-6, 1e-5, 1e-4, 1e-3])
