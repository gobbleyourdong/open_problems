"""
Sparse sweep: coarse grid of IC parameters, short runs (1000 steps),
classify as GROWING/DECAYING/STABLE. Then refine the interesting ones.
"""
import sys, os, math, time, json
import torch
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from leray_solver import LeraySolver


def make_ic(solver, amp_v, amp_w, r_peak, sigma):
    XI, ZETA = solver.R, solver.Z
    radial = torch.exp(-((XI - r_peak)**2) / sigma**2)
    z_mode = torch.sin(2 * math.pi * ZETA / solver.Lz)
    U1 = amp_v * radial * z_mode
    W1 = amp_w * radial * z_mode
    U1[0, :] = 0; U1[:, 0] = 0
    W1[:, 0] = 0; W1[:, -1] = 0
    return U1, W1


def quick_run(solver, U1, W1, n_steps=1000):
    dt = 1e-7
    tau = 0.0
    u0 = U1.abs().max().item()
    w0 = W1.abs().max().item()

    for step in range(n_steps):
        U1, W1, _, _ = solver.step_rk4(U1, W1, dt)
        tau += dt
        u_r_dummy = torch.zeros_like(U1)
        dt = solver.compute_dt(u_r_dummy, u_r_dummy, W1, dt)

        if U1.abs().max().item() > 1e6:
            return 'BLOWUP', step, 0, 0

        # Check spectral every 200
        if step % 200 == 0 and step > 0:
            mid_z = W1.shape[1] // 2
            w_slice = W1[:, mid_z].cpu().numpy()
            coeffs = np.abs(np.fft.rfft(w_slice))
            n = len(coeffs)
            low = coeffs[:n//4].mean() + 1e-30
            high = coeffs[3*n//4:].mean()
            if high / low > 0.1:
                return 'UNDER', step, U1.abs().max().item(), W1.abs().max().item()

    uf = U1.abs().max().item()
    wf = W1.abs().max().item()
    u_ratio = uf / (u0 + 1e-30)
    w_ratio = wf / (w0 + 1e-30) if w0 > 1e-15 else 0

    if u_ratio > 1.5:
        return 'GROWING', n_steps, uf, wf
    elif u_ratio < 0.5:
        return 'DECAYING', n_steps, uf, wf
    else:
        return 'STABLE', n_steps, uf, wf


def main():
    Nr, Nz = 64, 128
    nu = 1e-4
    device = 'cuda'
    n_steps = 1000  # ~15s per run

    solver = LeraySolver(Nr=Nr, Nz=Nz, nu=nu, device=device,
                         ic_type='luo_hou', amplitude=1.0)

    # SPARSE GRID: wide parameter range
    amp_vs = [0.1, 0.5, 1.0, 5.0, 20.0, 100.0]
    amp_ws = [0.0, 0.1, 0.5, 1.0, 5.0, 20.0]
    r_peaks = [0.1, 0.3, 0.5, 0.8]
    sigmas = [0.05, 0.1, 0.2]

    configs = []
    for av in amp_vs:
        for aw in amp_ws:
            for rp in r_peaks:
                for sig in sigmas:
                    configs.append((av, aw, rp, sig))

    print(f"SPARSE SWEEP: {len(configs)} configs, {n_steps} steps each")
    print(f"Nr={Nr} Nz={Nz} ν={nu}")
    print()

    results = []
    t0 = time.time()

    for i, (av, aw, rp, sig) in enumerate(configs):
        U1, W1 = make_ic(solver, av, aw, rp, sig)
        status, final_step, uf, wf = quick_run(solver, U1.clone(), W1.clone(), n_steps)

        elapsed = time.time() - t0
        marker = ' ***' if status == 'STABLE' else ''
        print(f"[{i+1}/{len(configs)}] Av={av:6.1f} Aw={aw:5.1f} r={rp:.1f} σ={sig:.2f} "
              f"→ {status:>8} U₁f={uf:.3e} W₁f={wf:.3e}{marker} [{elapsed:.0f}s]",
              flush=True)

        results.append({
            'amp_v': av, 'amp_w': aw, 'r_peak': rp, 'sigma': sig,
            'status': status, 'u_final': uf, 'w_final': wf, 'final_step': final_step,
        })

    elapsed = time.time() - t0
    print(f"\n{'='*70}")
    print(f"SPARSE SWEEP DONE: {len(configs)} configs in {elapsed:.0f}s")
    print(f"{'='*70}")

    counts = {}
    for r in results:
        s = r['status']
        counts[s] = counts.get(s, 0) + 1
    for s, c in sorted(counts.items()):
        print(f"  {s}: {c}")

    # Find STABLE regions
    stable = [r for r in results if r['status'] == 'STABLE']
    if stable:
        print(f"\n*** {len(stable)} STABLE configs ***")
        print(f"{'Av':>6} {'Aw':>6} {'r':>5} {'σ':>5} {'U₁f':>10} {'W₁f':>10}")
        for r in stable:
            print(f"{r['amp_v']:6.1f} {r['amp_w']:6.1f} {r['r_peak']:5.2f} "
                  f"{r['sigma']:5.2f} {r['u_final']:10.3e} {r['w_final']:10.3e}")

        # Find the HIGHEST amplitude stable config
        stable.sort(key=lambda r: r['amp_v'], reverse=True)
        best = stable[0]
        print(f"\nHighest-amplitude stable: Av={best['amp_v']}, Aw={best['amp_w']}")
        print(f"→ This is the best candidate for Newton-Krylov refinement")
    else:
        print(f"\nNo stable configs. Looking for GROWING (potential blowup):")
        growing = [r for r in results if r['status'] == 'GROWING']
        growing.sort(key=lambda r: r['u_final'] / r['amp_v'] if r['amp_v'] > 0 else 0, reverse=True)
        for r in growing[:10]:
            ratio = r['u_final'] / r['amp_v'] if r['amp_v'] > 0 else 0
            print(f"  Av={r['amp_v']:6.1f} Aw={r['amp_w']:5.1f} r={r['r_peak']:.1f} "
                  f"σ={r['sigma']:.2f} growth={ratio:.2f}×")

    # Save
    out_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "orbit_sparse_sweep.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    main()
