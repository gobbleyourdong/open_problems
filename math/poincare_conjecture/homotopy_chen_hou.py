"""
HOMOTOPY: Load Chen-Hou Euler steady state, interpolate to our grid,
run in Leray frame with increasing ν.

If the profile survives at any ν > 0 → NS blows up → Millennium Prize.
If it dies → regularity evidence.

Chen-Hou scaling: c_l=3.0065 (Euler self-similar)
Our Leray scaling: c_l=0.5

The profile SHAPE is the same — just need to:
1. Interpolate from their 720×720 non-uniform grid to our Chebyshev grid
2. Rescale coordinates: their self-similar coords → our ξ,ζ domain [0,1]×[0,L/4]
3. Run Leray solver and track whether profile persists or decays
"""
import sys, os, math, time, json
import torch
import numpy as np
from scipy.interpolate import RegularGridInterpolator
import scipy.io as sio

sys.path.insert(0, os.path.dirname(__file__))
from leray_solver import LeraySolver


def load_chen_hou():
    """Load the Chen-Hou approximate steady state."""
    mat_path = os.path.join(os.path.dirname(__file__),
        "chen_hou_matlab", "ASS_data", "Steady_state_pertb720_Nlevcor4.mat")
    mat = sio.loadmat(mat_path)

    v = mat['v']  # u₁ profile, 720×720
    w = mat['w']  # ω₁ profile, 720×720

    mesh = mat['Mesh'][0, 0]
    r_grid = mesh['x'][0, 0].flatten()  # 720 points, non-uniform
    z_grid = mesh['x'][0, 1].flatten()  # 720 points, non-uniform

    solu = mat['solu'][0, 0]
    cl = solu['cl'].item()
    cw = solu['cw'].item()

    print(f"Chen-Hou profile loaded: {v.shape}")
    print(f"  c_l={cl:.4f}, c_ω={cw:.4f}")
    print(f"  |v|_max={v.max():.4f}, |w|_max={w.max():.4f}")
    print(f"  r range: [{r_grid[0]:.4f}, {r_grid[-1]:.4e}]")
    print(f"  z range: [{z_grid[0]:.4f}, {z_grid[-1]:.4e}]")

    return v, w, r_grid, z_grid, cl, cw


def interpolate_to_chebyshev(v_ch, w_ch, r_ch, z_ch, Nr, Nz, L=1.0/6.0,
                              r_scale=1.0, z_scale=1.0):
    """
    Interpolate Chen-Hou profile onto our Chebyshev grid.

    r_scale, z_scale: map our domain [0,1]×[0,L/4] to Chen-Hou's domain.
    Our ξ=1 maps to r_ch = r_scale in Chen-Hou coords.
    Our ζ=L/4 maps to z_ch = z_scale in Chen-Hou coords.
    """
    # Our Chebyshev grid
    j = np.arange(Nr + 1)
    x = np.cos(np.pi * j / Nr)
    r_our = (1 + x) / 2  # [0, 1], r[0]=1, r[Nr]=0

    Lz = L / 4.0
    z_our = np.linspace(0, Lz, Nz + 1)

    # Map our coords to Chen-Hou's coords
    r_query = r_our * r_scale  # our [0,1] → [0, r_scale]
    z_query = z_our * (z_scale / Lz)  # our [0, L/4] → [0, z_scale]

    # Build interpolator on Chen-Hou grid
    # Their grid is non-uniform but sorted — use 1D interpolation
    v_interp = np.zeros((Nr + 1, Nz + 1))
    w_interp = np.zeros((Nr + 1, Nz + 1))

    # For each z in our grid, interpolate the radial profile
    for j_z, zq in enumerate(z_query):
        # Find z index in Chen-Hou grid
        z_idx = np.searchsorted(z_ch, zq)
        z_idx = min(z_idx, len(z_ch) - 2)

        # Linear interpolation in z
        z_frac = (zq - z_ch[z_idx]) / (z_ch[z_idx + 1] - z_ch[z_idx] + 1e-30)
        z_frac = np.clip(z_frac, 0, 1)

        v_at_z = (1 - z_frac) * v_ch[:, z_idx] + z_frac * v_ch[:, z_idx + 1]
        w_at_z = (1 - z_frac) * w_ch[:, z_idx] + z_frac * w_ch[:, z_idx + 1]

        # Interpolate in r
        for i_r, rq in enumerate(r_query):
            r_idx = np.searchsorted(r_ch, rq)
            r_idx = min(r_idx, len(r_ch) - 2)
            r_frac = (rq - r_ch[r_idx]) / (r_ch[r_idx + 1] - r_ch[r_idx] + 1e-30)
            r_frac = np.clip(r_frac, 0, 1)

            v_interp[i_r, j_z] = (1 - r_frac) * v_at_z[r_idx] + r_frac * v_at_z[r_idx + 1]
            w_interp[i_r, j_z] = (1 - r_frac) * w_at_z[r_idx] + r_frac * w_at_z[r_idx + 1]

    return v_interp, w_interp, r_our, z_our


def run_homotopy(Nr=64, Nz=128, nu_values=None, n_steps=5000, device='cuda'):
    """
    Run the Chen-Hou profile at increasing viscosity values.
    Track whether the profile survives (steady in Leray frame) or decays.
    """
    if nu_values is None:
        nu_values = [0, 1e-6, 1e-5, 1e-4, 1e-3]

    # Load Chen-Hou
    v_ch, w_ch, r_ch, z_ch, cl, cw = load_chen_hou()

    # The profile lives in self-similar coords with r_peak ≈ 2.
    # Our domain is [0, 1]. We need r_scale so that the profile
    # fits in our domain. Profile 50% width is r ∈ [0.4, 19].
    # Let's try r_scale = 5 so our ξ=1 → r_ch=5 (captures the core).
    # And z_scale = 5 (profile is nearly z-independent near origin).
    r_scale = 5.0
    z_scale = 5.0

    print(f"\nInterpolating to Nr={Nr}, Nz={Nz}")
    print(f"Domain mapping: ξ∈[0,1] → r_ch∈[0,{r_scale}], ζ∈[0,{1/24:.4f}] → z_ch∈[0,{z_scale}]")

    v_interp, w_interp, r_our, z_our = interpolate_to_chebyshev(
        v_ch, w_ch, r_ch, z_ch, Nr, Nz, r_scale=r_scale, z_scale=z_scale)

    print(f"Interpolated: |v|_max={abs(v_interp).max():.4f}, |w|_max={abs(w_interp).max():.4f}")

    all_results = {}

    for nu in nu_values:
        print(f"\n{'='*60}")
        print(f"ν = {nu:.1e}")
        print(f"{'='*60}")

        solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=device,
                             ic_type='luo_hou', amplitude=1.0)

        # Set IC from interpolated Chen-Hou profile
        U1 = torch.tensor(v_interp, dtype=torch.float64, device=device)
        W1 = torch.tensor(w_interp, dtype=torch.float64, device=device)

        # Enforce BCs
        U1[0, :] = 0   # far-field
        U1[:, 0] = 0   # z=0 odd BC
        W1[:, 0] = 0
        W1[:, -1] = 0

        U1_init_max = U1.abs().max().item()
        W1_init_max = W1.abs().max().item()

        tau, dt = 0.0, 1e-7
        results = []
        t0 = time.time()

        for step in range(n_steps + 1):
            if step % 200 == 0:
                u_max = U1.abs().max().item()
                w_max = W1.abs().max().item()

                # Spectral check
                mid_z = W1.shape[1] // 2
                if w_max > 1e-15:
                    w_slice = W1[:, mid_z].cpu().numpy()
                    coeffs = np.abs(np.fft.rfft(w_slice))
                    n = len(coeffs)
                    low = coeffs[:n//4].mean() + 1e-30
                    high = coeffs[3*n//4:].mean()
                    spec = high / low
                else:
                    spec = 0

                # Relative change from initial
                u_ratio = u_max / (U1_init_max + 1e-30)
                w_ratio = w_max / (W1_init_max + 1e-30)

                status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")
                elapsed = time.time() - t0

                results.append({
                    'step': step, 'tau': tau,
                    'U1_max': u_max, 'W1_max': w_max,
                    'u_ratio': u_ratio, 'w_ratio': w_ratio,
                    'spectral': spec, 'dt': dt,
                })

                if step % 1000 == 0:
                    print(f"  step={step:5d} τ={tau:.6f} "
                          f"|U₁|={u_max:.4f}({u_ratio:.3f}×) "
                          f"|W₁|={w_max:.4e}({w_ratio:.3f}×) "
                          f"spec={spec:.4f} [{status}] [{elapsed:.0f}s]")

            if U1.abs().max().item() > 1e8:
                print(f"  BLOWUP at step {step}")
                break
            if U1.abs().max().item() < 1e-15 and step > 100:
                print(f"  DECAYED at step {step}")
                break

            U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
            tau += dt
            u_r_dummy = torch.zeros_like(U1)
            dt = solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

        # Classify outcome
        if results:
            final_u_ratio = results[-1]['u_ratio']
            final_w_ratio = results[-1]['w_ratio']
            if final_u_ratio > 0.9 and final_w_ratio > 0.9:
                outcome = "SURVIVED"
            elif final_u_ratio < 0.1:
                outcome = "DECAYED"
            else:
                outcome = "EVOLVING"
        else:
            outcome = "UNKNOWN"

        print(f"\n  OUTCOME: {outcome}")
        print(f"  |U₁|: {U1_init_max:.4f} → {results[-1]['U1_max']:.4f} ({final_u_ratio:.3f}×)")
        print(f"  |W₁|: {W1_init_max:.4e} → {results[-1]['W1_max']:.4e} ({final_w_ratio:.3f}×)")

        all_results[f'nu_{nu}'] = {
            'nu': nu, 'outcome': outcome,
            'final_u_ratio': final_u_ratio,
            'final_w_ratio': final_w_ratio,
            'history': results,
        }

    # Summary
    print(f"\n{'='*60}")
    print(f"HOMOTOPY SUMMARY")
    print(f"{'='*60}")
    print(f"{'ν':>10} {'outcome':>12} {'|U₁| ratio':>12} {'|W₁| ratio':>12}")
    for key, res in all_results.items():
        print(f"{res['nu']:10.1e} {res['outcome']:>12} "
              f"{res['final_u_ratio']:12.4f} {res['final_w_ratio']:12.4f}")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)

    # Can't json-dump everything, save summary
    summary = []
    for key, res in all_results.items():
        summary.append({
            'nu': res['nu'], 'outcome': res['outcome'],
            'final_u_ratio': res['final_u_ratio'],
            'final_w_ratio': res['final_w_ratio'],
            'n_steps': len(res['history']),
        })
    out_path = os.path.join(out_dir, f"homotopy_nr{Nr}.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved: {out_path}")

    return all_results


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nr', type=int, default=64)
    parser.add_argument('--nz', type=int, default=128)
    parser.add_argument('--steps', type=int, default=5000)
    parser.add_argument('--device', type=str, default='cuda')
    args = parser.parse_args()

    run_homotopy(Nr=args.nr, Nz=args.nz, n_steps=args.steps, device=args.device,
                 nu_values=[0, 1e-6, 1e-5, 1e-4])
