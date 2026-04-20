"""
Re-converge Chen-Hou steady state on OUR grid.

Step 1: Load interpolated profile (residual ~1e3)
Step 2: Run ν=0 Chen-Hou equations until residual drops to ~1e-8
Step 3: Save the converged profile
Step 4: Run with increasing ν to test survival

This gives us a steady state that's EXACT for our discretization.
"""
import sys, os, math, time, json
import torch
import numpy as np
import scipy.io as sio

sys.path.insert(0, os.path.dirname(__file__))
from chen_hou_viscous import ChenHouSolver, load_chen_hou_profile


def reconverge(Nr=64, Nz=128, device='cuda', r_scale=5.0,
               max_steps=50000, target_residual=1e-6):
    """
    Run ν=0 Chen-Hou equations from interpolated IC until residual converges.
    """
    v_init, w_init, cl, cw = load_chen_hou_profile(Nr, Nz, r_scale=r_scale)

    print(f"RECONVERGE Chen-Hou on Nr={Nr} Nz={Nz}")
    print(f"cl={cl:.4f}, cw={cw:.4f}, r_scale={r_scale}")
    print(f"IC: |v|={abs(v_init).max():.4f}, |w|={abs(w_init).max():.4f}")

    solver = ChenHouSolver(Nr=Nr, Nz=Nz, nu=0, device=device, cl=cl, cw=cw)

    v = torch.tensor(v_init, dtype=torch.float64, device=device)
    w = torch.tensor(w_init, dtype=torch.float64, device=device)
    v[0, :] = 0; v[:, 0] = 0
    w[:, 0] = 0; w[:, -1] = 0

    tau, dt = 0.0, 1e-8  # small initial dt for stability
    t0 = time.time()
    best_residual = 1e30
    best_v, best_w = v.clone(), w.clone()

    print(f"\n{'step':>6} {'τ':>10} {'|v|':>8} {'|w|':>8} {'residual':>12} {'spec':>8} {'dt':>10}")
    print("-" * 75)

    for step in range(max_steps + 1):
        if step % 500 == 0:
            Fv, Fw, _, _ = solver.compute_rhs(v, w)
            res = max(Fv.abs().max().item(), Fw.abs().max().item())
            v_max = v.abs().max().item()
            w_max = w.abs().max().item()

            mid_z = w.shape[1] // 2
            w_slice = w[:, mid_z].cpu().numpy()
            coeffs = np.abs(np.fft.rfft(w_slice))
            n = len(coeffs)
            low = coeffs[:n//4].mean() + 1e-30
            high = coeffs[3*n//4:].mean()
            spec = high / low

            status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")
            elapsed = time.time() - t0

            if res < best_residual:
                best_residual = res
                best_v = v.clone()
                best_w = w.clone()

            print(f"{step:6d} {tau:10.6f} {v_max:8.4f} {w_max:8.4e} "
                  f"{res:12.2e} {spec:8.4f} {dt:10.2e} [{status}] [{elapsed:.0f}s]")

            if res < target_residual:
                print(f"\nCONVERGED! Residual {res:.2e} < {target_residual:.2e}")
                break

            if status == "UNDER" and step > 1000:
                print(f"\nSPECTRAL UNDER — stopping. Best residual: {best_residual:.2e}")
                break

            if v_max > 100 or w_max > 100:
                print(f"\nDIVERGING — stopping. Best residual: {best_residual:.2e}")
                break

        v, w, _, _ = solver.step_rk4(v, w, dt)
        tau += dt
        u_r_dummy = torch.zeros_like(v)
        dt = solver.compute_dt(u_r_dummy, u_r_dummy, w, dt)

    print(f"\nFinal: |v|={v.abs().max().item():.4f}, |w|={w.abs().max().item():.4e}")
    print(f"Best residual achieved: {best_residual:.2e}")

    # Save converged state
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    save_path = os.path.join(out_dir, f"chen_hou_converged_nr{Nr}.pt")
    torch.save({
        'v': best_v.cpu(), 'w': best_w.cpu(),
        'cl': cl, 'cw': cw, 'Nr': Nr, 'Nz': Nz,
        'residual': best_residual, 'r_scale': r_scale,
    }, save_path)
    print(f"Saved: {save_path}")

    return best_v, best_w, best_residual, cl, cw


def viscous_test(Nr, Nz, v_steady, w_steady, cl, cw,
                 nu_values=None, n_steps=10000, device='cuda'):
    """
    From the converged ν=0 steady state, add viscosity and track drift.
    """
    if nu_values is None:
        nu_values = [1e-6, 1e-5, 1e-4, 1e-3]

    v_init_max = v_steady.abs().max().item()
    w_init_max = w_steady.abs().max().item()

    print(f"\n{'='*60}")
    print(f"VISCOUS PERTURBATION TEST")
    print(f"Starting from converged ν=0 state")
    print(f"|v|={v_init_max:.6f}, |w|={w_init_max:.6e}")
    print(f"{'='*60}")

    all_results = {}

    for nu in nu_values:
        print(f"\n--- ν = {nu:.1e} ---")

        solver = ChenHouSolver(Nr=Nr, Nz=Nz, nu=nu, device=device, cl=cl, cw=cw)

        v = v_steady.clone().to(device)
        w = w_steady.clone().to(device)

        tau, dt = 0.0, 1e-8
        t0 = time.time()
        history = []

        for step in range(n_steps + 1):
            if step % 500 == 0:
                v_max = v.abs().max().item()
                w_max = w.abs().max().item()
                Fv, Fw, _, _ = solver.compute_rhs(v, w)
                res = max(Fv.abs().max().item(), Fw.abs().max().item())
                v_ratio = v_max / (v_init_max + 1e-30)
                w_ratio = w_max / (w_init_max + 1e-30)

                mid_z = w.shape[1] // 2
                w_slice = w[:, mid_z].cpu().numpy()
                coeffs = np.abs(np.fft.rfft(w_slice))
                n = len(coeffs)
                low = coeffs[:n//4].mean() + 1e-30
                high = coeffs[3*n//4:].mean()
                spec = high / low
                status = "OK" if spec < 0.01 else ("MARG" if spec < 0.1 else "UNDER")

                elapsed = time.time() - t0
                history.append({
                    'step': step, 'tau': tau,
                    'v_max': v_max, 'w_max': w_max,
                    'v_ratio': v_ratio, 'w_ratio': w_ratio,
                    'residual': res, 'spectral': spec,
                })

                if step % 2000 == 0:
                    print(f"  step={step:5d} τ={tau:.6f} "
                          f"|v|={v_max:.4f}({v_ratio:.4f}×) "
                          f"res={res:.2e} [{status}] [{elapsed:.0f}s]")

            if v.abs().max().item() > 1e6:
                print(f"  BLOWUP at step {step}")
                break
            if v.abs().max().item() < 1e-10 and step > 500:
                print(f"  DECAYED at step {step}")
                break

            v, w, _, _ = solver.step_rk4(v, w, dt)
            tau += dt
            u_r_dummy = torch.zeros_like(v)
            dt = solver.compute_dt(u_r_dummy, u_r_dummy, w, dt)

        if history:
            final = history[-1]
            if final['v_ratio'] > 0.95 and final['v_ratio'] < 1.05:
                outcome = "STEADY"
            elif final['v_ratio'] > 1.05:
                outcome = "GROWING"
            elif final['v_ratio'] < 0.5:
                outcome = "DECAYING"
            else:
                outcome = "DRIFTING"

            print(f"  → {outcome}: |v| {v_init_max:.4f} → {final['v_max']:.4f} ({final['v_ratio']:.4f}×)")
            all_results[nu] = {'outcome': outcome, 'v_ratio': final['v_ratio'],
                               'w_ratio': final['w_ratio'], 'residual': final['residual']}

    # Summary
    print(f"\n{'='*60}")
    print(f"VISCOUS HOMOTOPY RESULTS")
    print(f"{'='*60}")
    print(f"{'ν':>10} {'outcome':>10} {'|v| ratio':>10} {'residual':>12}")
    for nu, res in all_results.items():
        print(f"{nu:10.1e} {res['outcome']:>10} {res['v_ratio']:10.4f} {res['residual']:12.2e}")

    print(f"\n  STEADY → fixed point survives viscosity → NS BLOWUP CANDIDATE")
    print(f"  DECAYING → viscosity wins → regularity for this profile")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    out_path = os.path.join(out_dir, f"chen_hou_viscous_nr{Nr}.json")
    with open(out_path, "w") as f:
        json.dump({str(k): v for k, v in all_results.items()}, f, indent=2)
    print(f"Saved: {out_path}")

    return all_results


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nr', type=int, default=64)
    parser.add_argument('--nz', type=int, default=128)
    parser.add_argument('--r-scale', type=float, default=5.0)
    parser.add_argument('--converge-steps', type=int, default=50000)
    parser.add_argument('--test-steps', type=int, default=10000)
    parser.add_argument('--target-res', type=float, default=1e-4)
    parser.add_argument('--device', type=str, default='cuda')
    args = parser.parse_args()

    # Step 1: Re-converge at ν=0
    v_ss, w_ss, res, cl, cw = reconverge(
        Nr=args.nr, Nz=args.nz, device=args.device,
        r_scale=args.r_scale, max_steps=args.converge_steps,
        target_residual=args.target_res)

    # Step 2: Test with viscosity (only if converged reasonably)
    if res < 1.0:  # residual below 1 is "good enough" to test
        viscous_test(args.nr, args.nz, v_ss, w_ss, cl, cw,
                     n_steps=args.test_steps, device=args.device)
    else:
        print(f"\nResidual {res:.2e} too high for viscous test.")
        print(f"Try: --nr 128 or --r-scale 10")
