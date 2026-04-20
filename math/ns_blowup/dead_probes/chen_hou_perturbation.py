"""
Perturbation analysis: Chen-Hou steady state + viscosity.

Strategy: Split v = v_ss + δv, w = w_ss + δw.
At the steady state, the inviscid RHS ≈ 0 (residual 3e-10).
With viscosity, the perturbation evolves as:

  d(δv)/dt = J·δv + ν·Δ(v_ss + δv)
  d(δw)/dt = J·δw + ν·Δ(w_ss + δw)

where J is the linearized operator around the steady state.

For SMALL δ, the viscous term ν·Δ(v_ss) dominates.
We track the FULL fields v = v_ss + δv using:
  - SAVED velocity (exact) for the inviscid advection
  - FD Laplacian (accurate enough) for the viscous term
  - NO Poisson solve needed — velocity stays frozen at saved value

This is the same as our frozen-velocity test but with PROPER RHS
(using saved velocity, not our FD approximation).

The key diagnostic: the RESIDUAL of the inviscid part.
At t=0, residual ≈ 0 (their 3e-10). As δ grows, residual grows.
When residual >> ν·Δv, viscosity has lost — the profile is unstable.
When residual stays < ν·Δv, viscosity controls — the profile may survive.
"""
import sys, os, math, time, json
import numpy as np
import scipy.io as sio

sys.path.insert(0, os.path.dirname(__file__))


def main():
    # Load everything
    mat_path = os.path.join(os.path.dirname(__file__),
        "chen_hou_matlab", "ASS_data", "Steady_state_pertb720_Nlevcor4.mat")
    mat = sio.loadmat(mat_path)

    v_ss = mat['v'].copy()       # 720×720 steady state
    w_ss = mat['w'].copy()
    Fv_ss = mat['Fv']            # inviscid residual (~3e-10)
    Fw_ss = mat['Fw']

    mesh = mat['Mesh'][0, 0]
    r = mesh['x'][0, 0].flatten()
    z = mesh['x'][0, 1].flatten()
    Nr, Nz = len(r), len(z)

    solu = mat['solu'][0, 0]
    cl = solu['cl'].item()
    cw = solu['cw'].item()

    # Saved velocity and derivatives (EXACT at steady state)
    u_r = solu['u1'][0, 0]       # 720×720
    u_z = solu['u2'][0, 0]
    u1dx1 = solu['u1_dx']        # ∂u_r/∂r
    v_dx = solu['v_dx']          # ∂v/∂r (saved, B-spline accurate)

    R = r[:, np.newaxis] * np.ones((1, Nz))
    Z = np.ones((Nr, 1)) * z[np.newaxis, :]

    print("=" * 70)
    print("CHEN-HOU PERTURBATION ANALYSIS")
    print("=" * 70)
    print(f"Grid: {Nr}×{Nz}")
    print(f"cl={cl:.6f}, cw={cw:.6f}")
    print(f"|v_ss|_max = {abs(v_ss).max():.6f}")
    print(f"|w_ss|_max = {abs(w_ss).max():.6f}")
    print(f"Inviscid residual: |Fv|={abs(Fv_ss).max():.2e}, |Fw|={abs(Fw_ss).max():.2e}")

    # Compute Laplacian of steady state using FD
    # We already validated this gives |Δv|_max ≈ 690
    def fd_deriv(f, x, axis):
        """Vectorized 2nd-order centered FD derivative on non-uniform grid."""
        dx = np.diff(x)
        if axis == 0:
            hm = dx[:-1, np.newaxis]  # (N-2, 1)
            hp = dx[1:, np.newaxis]
            df = np.zeros_like(f)
            df[1:-1] = (-hp**2 * f[:-2] + (hp**2 - hm**2) * f[1:-1] + hm**2 * f[2:]) / (hm * hp * (hm + hp))
        else:
            hm = dx[np.newaxis, :-1]  # (1, N-2)
            hp = dx[np.newaxis, 1:]
            df = np.zeros_like(f)
            df[:, 1:-1] = (-hp**2 * f[:, :-2] + (hp**2 - hm**2) * f[:, 1:-1] + hm**2 * f[:, 2:]) / (hm * hp * (hm + hp))
        return df

    def fd_d2(f, x, axis):
        """Vectorized 2nd derivative on non-uniform grid."""
        dx = np.diff(x)
        d2f = np.zeros_like(f)
        if axis == 0:
            hm = dx[:-1, np.newaxis]
            hp = dx[1:, np.newaxis]
            d2f[1:-1] = 2.0 * (f[2:] / (hp*(hm+hp)) - f[1:-1] / (hm*hp) + f[:-2] / (hm*(hm+hp)))
            d2f[0] = 2.0 * (f[1] - f[0]) / (dx[0]**2)  # symmetry at r=0
        else:
            hm = dx[np.newaxis, :-1]
            hp = dx[np.newaxis, 1:]
            d2f[:, 1:-1] = 2.0 * (f[:, 2:] / (hp*(hm+hp)) - f[:, 1:-1] / (hm*hp) + f[:, :-2] / (hm*(hm+hp)))
        return d2f

    def laplacian_hou_li(f):
        """Hou-Li Laplacian: Δf = d²f/dr² + (3/r)df/dr + d²f/dz²"""
        d2f_dr2 = fd_d2(f, r, 0)
        df_dr = fd_deriv(f, r, 0)
        d2f_dz2 = fd_d2(f, z, 1)

        three_over_r = np.zeros(Nr)
        three_over_r[1:] = 3.0 / r[1:]

        lap = d2f_dr2 + three_over_r[:, np.newaxis] * df_dr + d2f_dz2
        # r=0: L'Hôpital → 4*d²f/dr²
        lap[0, :] = 4.0 * d2f_dr2[0, :] + d2f_dz2[0, :]
        return lap

    Lap_v = laplacian_hou_li(v_ss)
    Lap_w = laplacian_hou_li(w_ss)
    print(f"|Δv_ss|_max = {abs(Lap_v).max():.2f}")
    print(f"|Δw_ss|_max = {abs(Lap_w).max():.2f}")

    # Compute the FULL inviscid RHS using saved derivatives and velocity
    # to verify our derivatives match
    # We need dv/dz and dw/dr, dw/dz (not saved — compute with FD)
    vx2 = fd_deriv(v_ss, z, 1)  # ∂v/∂z
    wx1 = fd_deriv(w_ss, r, 0)  # ∂w/∂r
    wx2 = fd_deriv(w_ss, z, 1)  # ∂w/∂z

    # Use SAVED v_dx for ∂v/∂r (B-spline accurate)
    vx1_saved = v_dx

    # Chen-Hou RHS with saved velocity and saved ∂v/∂r
    Fv_check = -(cl*R + u_r) * vx1_saved - (cl*Z + u_z) * vx2 + (2*cw - u1dx1) * v_ss
    Fw_check = -(cl*R + u_r) * wx1 - (cl*Z + u_z) * wx2 + cw*w_ss + v_ss + R*vx1_saved

    Fv_check[0, :] = 0
    Fw_check[0, :] = 0

    print(f"\nRHS verification (saved velocity + saved ∂v/∂r + FD for rest):")
    print(f"  |Fv|_max = {abs(Fv_check).max():.4e}  (saved: {abs(Fv_ss).max():.4e})")
    print(f"  |Fw|_max = {abs(Fw_check).max():.4e}  (saved: {abs(Fw_ss).max():.4e})")
    print(f"  |Fv - Fv_saved|_max = {abs(Fv_check - Fv_ss).max():.4e}")
    print(f"  |Fw - Fw_saved|_max = {abs(Fw_check - Fw_ss).max():.4e}")

    rhs_error = max(abs(Fv_check - Fv_ss).max(), abs(Fw_check - Fw_ss).max())
    print(f"  Baseline RHS error: {rhs_error:.4e}")

    # Now: time-step with viscosity using FROZEN saved velocity
    # RHS = Fv_inviscid + ν * Δv
    # Since Fv_inviscid ≈ 3e-10 at steady state, total RHS ≈ ν * Δv

    # But as v evolves, we need to recompute derivatives of v (not velocity).
    # We use FD derivatives for v,w and SAVED velocity (frozen).
    # The inviscid RHS drifts from zero as v departs from v_ss.

    nu_values = [0, 1e-5, 1e-4, 1e-3]
    n_steps = 10000
    dt = 1e-5  # small enough for CFL with cl=3 on their grid

    # CFL estimate: cl*r[i]/dr[i] — find max
    dr = np.diff(r)
    cfl_r = np.zeros(Nr-1)
    for i in range(Nr-1):
        vel = abs(cl * r[i] + u_r[i, :].max())
        cfl_r[i] = vel / dr[i]
    cfl_z = np.zeros(Nz-1)
    dz_arr = np.diff(z)
    for j in range(Nz-1):
        vel = abs(cl * z[j] + u_z[:, j].max())
        cfl_z[j] = vel / dz_arr[j]

    cfl_max = max(cfl_r.max(), cfl_z.max())
    dt = min(0.3 / cfl_max, 1e-4)
    print(f"\nCFL max: {cfl_max:.2e}, dt = {dt:.4e}")

    results = {}

    for nu in nu_values:
        print(f"\n{'='*60}")
        print(f"ν = {nu:.1e}")
        print(f"{'='*60}")

        visc_force = nu * abs(Lap_v).max()
        print(f"Viscous force: ν|Δv| = {visc_force:.4e}")
        print(f"Baseline error: {rhs_error:.4e}")
        if visc_force < rhs_error and nu > 0:
            print(f"WARNING: Viscous force < baseline error. Result may not be meaningful.")

        v = v_ss.copy()
        w = w_ss.copy()
        t0 = time.time()

        history = []

        for step in range(n_steps + 1):
            if step % 1000 == 0:
                v_max = abs(v).max()
                w_max = abs(w).max()
                dv = abs(v - v_ss).max()
                dw = abs(w - w_ss).max()

                # Compute inviscid RHS with current v,w but SAVED velocity
                vx1_curr = fd_deriv(v, r, 0)
                vx2_curr = fd_deriv(v, z, 1)
                wx1_curr = fd_deriv(w, r, 0)
                wx2_curr = fd_deriv(w, z, 1)

                Fv_curr = -(cl*R + u_r) * vx1_curr - (cl*Z + u_z) * vx2_curr + (2*cw - u1dx1) * v
                Fw_curr = -(cl*R + u_r) * wx1_curr - (cl*Z + u_z) * wx2_curr + cw*w + v + R*vx1_curr
                Fv_curr[0, :] = 0
                Fw_curr[0, :] = 0

                inviscid_res = max(abs(Fv_curr).max(), abs(Fw_curr).max())

                elapsed = time.time() - t0
                print(f"  step={step:5d} |v|={v_max:.6f} |w|={w_max:.6e} "
                      f"δv={dv:.4e} δw={dw:.4e} "
                      f"res={inviscid_res:.4e} [{elapsed:.0f}s]")

                history.append({
                    'step': step, 'v_max': v_max, 'w_max': w_max,
                    'dv': dv, 'dw': dw, 'residual': inviscid_res,
                })

            # Time-step: forward Euler with SAVED velocity
            vx1 = fd_deriv(v, r, 0)
            vx2 = fd_deriv(v, z, 1)
            wx1 = fd_deriv(w, r, 0)
            wx2 = fd_deriv(w, z, 1)

            Fv = -(cl*R + u_r) * vx1 - (cl*Z + u_z) * vx2 + (2*cw - u1dx1) * v
            Fw = -(cl*R + u_r) * wx1 - (cl*Z + u_z) * wx2 + cw*w + v + R*vx1

            if nu > 0:
                Fv += nu * laplacian_hou_li(v)
                Fw += nu * laplacian_hou_li(w)

            Fv[0, :] = 0
            Fw[0, :] = 0

            v += dt * Fv
            w += dt * Fw

            # BC enforcement
            v[0, :] = 0  # axis
            w[0, :] = 0

            if abs(v).max() > 1e3 or abs(w).max() > 1e3:
                print(f"  DIVERGED at step {step}")
                break

        # Summary for this nu
        if history:
            final = history[-1]
            v_change = (final['v_max'] - abs(v_ss).max()) / abs(v_ss).max() * 100
            w_change = (final['w_max'] - abs(w_ss).max()) / abs(w_ss).max() * 100

            if abs(v_change) < 1:
                status = "STEADY"
            elif v_change > 0:
                status = "GROWING"
            else:
                status = "DECAYING"

            results[nu] = {
                'v_change': v_change, 'w_change': w_change,
                'final_residual': final['residual'],
                'status': status,
            }
            print(f"  → {status}: v {v_change:+.4f}%, w {w_change:+.4f}%, res={final['residual']:.4e}")

    # Final summary
    print(f"\n{'='*70}")
    print(f"PERTURBATION ANALYSIS SUMMARY")
    print(f"{'='*70}")
    print(f"Baseline error (FD vs B-spline): {rhs_error:.4e}")
    print(f"{'ν':>10} {'status':>10} {'v change':>10} {'w change':>10} {'final res':>12}")
    print("-" * 55)
    for nu, res in results.items():
        print(f"{nu:10.1e} {res['status']:>10} {res['v_change']:+9.4f}% {res['w_change']:+9.4f}% {res['final_residual']:12.4e}")

    print(f"\nKey question: Does the profile survive at ν=1e-4?")
    if 1e-4 in results:
        r14 = results[1e-4]
        if r14['status'] == 'STEADY':
            print(f"  → YES. v changed {r14['v_change']:+.4f}%. Profile is IMMUNE to viscosity.")
            print(f"  → This is evidence for NS blowup.")
        elif r14['status'] == 'DECAYING':
            print(f"  → NO. Profile decays. Viscosity wins.")
        else:
            print(f"  → GROWING. Profile changes. Need longer run or nonlinear test.")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "chen_hou_perturbation.json")
    with open(out_path, "w") as f:
        json.dump({str(k): v for k, v in results.items()}, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    main()
