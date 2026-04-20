"""
Overnight orbit sweep: Run Leray solver with many different ICs,
looking for profiles that show stability or recurrence in Leray frame.

Key insight from today: Chen-Hou profile has BOTH u₁ and ω₁ nonzero
and in balance. Previous orbit search failed because W₁=0 ICs diverge.

Strategy: Initialize with Chen-Hou-INSPIRED profiles (smooth humps
with both U₁ and W₁ nonzero at various amplitudes and positions).
Run each for a warmup period, then track stability metrics.

A profile that stabilizes (|U₁|, |W₁| become approximately constant)
in Leray frame is a candidate periodic orbit.
"""
import sys, os, math, time, json
import torch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from leray_solver import LeraySolver


def chen_hou_inspired_ic(solver, amp_v=0.5, amp_w=0.5, r_peak=0.3, sigma=0.1):
    """
    IC inspired by Chen-Hou profile shape:
    - Smooth Gaussian hump in both U₁ and W₁
    - Peaked away from axis and wall
    - Both fields nonzero (self-consistent)
    """
    XI, ZETA = solver.R, solver.Z
    Lz = solver.Lz

    # Radial profile: Gaussian centered at r_peak
    radial = torch.exp(-((XI - r_peak)**2) / sigma**2)

    # z profile: sin mode (odd at z=0)
    z_mode = torch.sin(2 * math.pi * ZETA / Lz)

    U1 = amp_v * radial * z_mode
    W1 = amp_w * radial * z_mode

    # BCs
    U1[0, :] = 0   # far field
    U1[:, 0] = 0   # z=0 odd
    W1[:, 0] = 0
    W1[:, -1] = 0

    return U1, W1


def run_one(Nr, Nz, nu, amp_v, amp_w, r_peak, sigma, n_steps, device):
    """Run one IC and return stability metrics."""
    solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=device,
                         ic_type='luo_hou', amplitude=1.0)

    U1, W1 = chen_hou_inspired_ic(solver, amp_v, amp_w, r_peak, sigma)

    dt = 1e-7
    tau = 0.0
    t0 = time.time()

    # Track evolution
    u_history = []
    w_history = []

    for step in range(n_steps + 1):
        if step % 500 == 0:
            u_max = U1.abs().max().item()
            w_max = W1.abs().max().item()
            u_history.append(u_max)
            w_history.append(w_max)

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

            if spec > 0.1:
                return {
                    'status': 'UNDER',
                    'final_step': step,
                    'u_history': u_history,
                    'w_history': w_history,
                }

        if U1.abs().max().item() > 1e6 or W1.abs().max().item() > 1e6:
            return {
                'status': 'BLOWUP',
                'final_step': step,
                'u_history': u_history,
                'w_history': w_history,
            }

        if U1.abs().max().item() < 1e-12 and step > 500:
            return {
                'status': 'DECAYED',
                'final_step': step,
                'u_history': u_history,
                'w_history': w_history,
            }

        U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
        tau += dt
        u_r_dummy = torch.zeros_like(U1)
        dt = solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

    # Analyze stability
    u_arr = np.array(u_history)
    w_arr = np.array(w_history)

    # Check if approximately stable in second half
    if len(u_arr) > 10:
        half = len(u_arr) // 2
        u_late = u_arr[half:]
        w_late = w_arr[half:]
        u_cv = u_late.std() / (u_late.mean() + 1e-30)
        w_cv = w_late.std() / (w_late.mean() + 1e-30)

        if u_cv < 0.05 and w_cv < 0.05:
            status = 'STABLE'
        elif u_arr[-1] > u_arr[0] * 2:
            status = 'GROWING'
        elif u_arr[-1] < u_arr[0] * 0.5:
            status = 'SHRINKING'
        else:
            status = 'EVOLVING'
    else:
        status = 'SHORT'
        u_cv = w_cv = 0

    return {
        'status': status,
        'final_step': n_steps,
        'u_history': u_history,
        'w_history': w_history,
        'u_cv': float(u_cv) if 'u_cv' in dir() else 0,
        'w_cv': float(w_cv) if 'w_cv' in dir() else 0,
        'u_final': float(u_arr[-1]) if len(u_arr) > 0 else 0,
        'w_final': float(w_arr[-1]) if len(w_arr) > 0 else 0,
    }


def main():
    Nr, Nz = 64, 128
    nu = 1e-4
    n_steps = 5000  # ~80s per run at Nr=64
    device = 'cuda'

    # Sweep over IC parameters
    configs = []

    # Vary amplitude ratio (v vs w)
    for amp_v in [0.1, 0.3, 0.5, 1.0, 2.0]:
        for amp_w in [0.1, 0.3, 0.5, 1.0, 2.0]:
            configs.append({'amp_v': amp_v, 'amp_w': amp_w, 'r_peak': 0.3, 'sigma': 0.1})

    # Vary position
    for r_peak in [0.1, 0.2, 0.3, 0.5, 0.7]:
        configs.append({'amp_v': 0.5, 'amp_w': 0.5, 'r_peak': r_peak, 'sigma': 0.1})

    # Vary width
    for sigma in [0.03, 0.05, 0.1, 0.2, 0.3]:
        configs.append({'amp_v': 0.5, 'amp_w': 0.5, 'r_peak': 0.3, 'sigma': sigma})

    # Vary nu
    for nu_test in [0, 1e-6, 1e-5, 1e-4, 1e-3]:
        configs.append({'amp_v': 0.5, 'amp_w': 0.5, 'r_peak': 0.3, 'sigma': 0.1, 'nu': nu_test})

    # Remove duplicates
    unique = []
    seen = set()
    for c in configs:
        key = (c['amp_v'], c['amp_w'], c['r_peak'], c['sigma'], c.get('nu', nu))
        if key not in seen:
            seen.add(key)
            unique.append(c)
    configs = unique

    print(f"ORBIT SWEEP: {len(configs)} configurations")
    print(f"Nr={Nr}, Nz={Nz}, default ν={nu}, {n_steps} steps each")
    print(f"Device: {device}")
    print()

    results = []
    stable_count = 0
    t0 = time.time()

    for i, config in enumerate(configs):
        nu_run = config.get('nu', nu)
        amp_v = config['amp_v']
        amp_w = config['amp_w']
        r_peak = config['r_peak']
        sigma = config['sigma']

        result = run_one(Nr, Nz, nu_run, amp_v, amp_w, r_peak, sigma, n_steps, device)

        status = result['status']
        if status == 'STABLE':
            stable_count += 1
            marker = ' *** STABLE ***'
        else:
            marker = ''

        elapsed = time.time() - t0
        print(f"[{i+1}/{len(configs)}] A_v={amp_v:.1f} A_w={amp_w:.1f} "
              f"r={r_peak:.2f} σ={sigma:.2f} ν={nu_run:.1e} → {status:>10} "
              f"U₁={result.get('u_final',0):.4f} W₁={result.get('w_final',0):.4e}"
              f"{marker} [{elapsed:.0f}s]", flush=True)

        results.append({
            'config': config, 'status': status,
            'u_final': result.get('u_final', 0),
            'w_final': result.get('w_final', 0),
            'u_cv': result.get('u_cv', 0),
            'w_cv': result.get('w_cv', 0),
            'final_step': result['final_step'],
        })

    # Summary
    elapsed = time.time() - t0
    print(f"\n{'='*70}")
    print(f"SWEEP COMPLETE: {len(configs)} configs in {elapsed:.0f}s")
    print(f"{'='*70}")

    status_counts = {}
    for r in results:
        s = r['status']
        status_counts[s] = status_counts.get(s, 0) + 1

    for s, c in sorted(status_counts.items()):
        print(f"  {s}: {c}")

    if stable_count > 0:
        print(f"\n*** {stable_count} STABLE CONFIGURATIONS FOUND ***")
        for r in results:
            if r['status'] == 'STABLE':
                c = r['config']
                print(f"  A_v={c['amp_v']:.1f} A_w={c['amp_w']:.1f} "
                      f"r={c['r_peak']:.2f} σ={c['sigma']:.2f} "
                      f"ν={c.get('nu', nu):.1e} "
                      f"U₁={r['u_final']:.4f} W₁={r['w_final']:.4e} "
                      f"CV(U₁)={r['u_cv']:.4f}")
    else:
        print(f"\nNo stable configurations found. All profiles either grew, shrank, or went UNDER.")
        print(f"Best candidates (lowest CV):")
        evolving = [r for r in results if r['status'] == 'EVOLVING']
        evolving.sort(key=lambda r: r['u_cv'])
        for r in evolving[:5]:
            c = r['config']
            print(f"  A_v={c['amp_v']:.1f} A_w={c['amp_w']:.1f} "
                  f"r={c['r_peak']:.2f} σ={c['sigma']:.2f} "
                  f"CV(U₁)={r['u_cv']:.4f} CV(W₁)={r['w_cv']:.4f}")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"orbit_sweep_nr{Nr}.json")
    # Strip history arrays for JSON size
    save_results = [{k: v for k, v in r.items()
                     if k not in ('u_history', 'w_history')} for r in results]
    with open(out_path, "w") as f:
        json.dump(save_results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    main()
