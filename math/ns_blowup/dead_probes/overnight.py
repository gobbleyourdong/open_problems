"""
Overnight batch — dense Euler data under multiple ICs and resolutions.
All ν=0 (no diffusion operator needed — clean data only).

Runs:
1. Luo-Hou 2014 IC at Nr=64, 128 (boundary blowup, wall)
2. Hou 2022 IC at Nr=64, 128 (interior blowup, axis)
3. Amplitude sweep: A=50, 100, 200, 500 at Nr=64 (Luo-Hou)
4. Amplitude sweep: A=6000, 12000, 24000 at Nr=64 (Hou 2022)

Each run saves full timeseries for PySR analysis.

Expected paper validation targets:
  Luo-Hou 2014: T*≈0.0035, γ≈2.5, blowup at (r,z)=(1,0)
  Hou 2022:     T*≈0.00228, γ≈1.0, blowup at (r,z)=(0,0)

NOTE: Hou 2022 IC uses L=1 (not 1/6), domain z∈[0,1/2].
  BCs: u₁,ω₁,ψ₁ all odd at z=0 AND z=L/2 (no even symmetry for u₁).
"""
import os
import sys
import time
import json

sys.path.insert(0, os.path.dirname(__file__))
from sweep import SweepSolver, run_single

RESULTS_DIR = os.path.expanduser("~/ComfyUI/CelebV-HQ/ns_blowup/results")


def run_batch():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    start = time.time()
    results = []

    configs = [
        # === RESOLUTION CONVERGENCE: Luo-Hou ===
        # Nr=64 already done (euler_dense_nr64), skip
        dict(Nr=128, Nz=256, L=1/6, nu=0.0, ic_type='luo_hou',
             amplitude=100.0, tag='luohou_nr128'),

        # === RESOLUTION CONVERGENCE: Hou 2022 ===
        dict(Nr=64, Nz=128, L=1.0, nu=0.0, ic_type='hou_2022',
             amplitude=12000.0, tag='hou2022_nr64'),
        dict(Nr=128, Nz=256, L=1.0, nu=0.0, ic_type='hou_2022',
             amplitude=12000.0, tag='hou2022_nr128'),

        # === AMPLITUDE SWEEP: Luo-Hou ===
        dict(Nr=64, Nz=128, L=1/6, nu=0.0, ic_type='luo_hou',
             amplitude=50.0, tag='luohou_A50'),
        dict(Nr=64, Nz=128, L=1/6, nu=0.0, ic_type='luo_hou',
             amplitude=200.0, tag='luohou_A200'),
        dict(Nr=64, Nz=128, L=1/6, nu=0.0, ic_type='luo_hou',
             amplitude=500.0, tag='luohou_A500'),

        # === AMPLITUDE SWEEP: Hou 2022 ===
        dict(Nr=64, Nz=128, L=1.0, nu=0.0, ic_type='hou_2022',
             amplitude=6000.0, tag='hou2022_A6000'),
        dict(Nr=64, Nz=128, L=1.0, nu=0.0, ic_type='hou_2022',
             amplitude=24000.0, tag='hou2022_A24000'),
    ]

    total = len(configs)
    for i, cfg in enumerate(configs):
        elapsed = time.time() - start
        print(f"\n{'='*60}")
        print(f"RUN {i+1}/{total}: {cfg['tag']}  [{elapsed/60:.1f} min elapsed]")
        print(f"{'='*60}")

        try:
            r = run_single(**cfg, blowup_threshold=1e8)
            results.append(r)

            status = "BLOWUP" if r['blowup'] else "SURVIVED"
            T_star = r.get('T_star', 'N/A')
            gamma = r.get('gamma', 'N/A')
            if isinstance(T_star, float):
                T_star = f"{T_star:.8f}"
            if isinstance(gamma, float):
                gamma = f"{gamma:.4f}"
            print(f"  => {status}  T*={T_star}  γ={gamma}")
        except Exception as e:
            print(f"  => ERROR: {e}")
            results.append({'tag': cfg['tag'], 'error': str(e)})

    # === SUMMARY ===
    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"OVERNIGHT BATCH COMPLETE — {elapsed/3600:.1f} hours")
    print(f"{'='*60}")

    print(f"\n{'Tag':30s} {'T*':>12s} {'γ':>8s} {'Status':>10s}")
    print("-" * 65)
    for r in results:
        if 'error' in r:
            print(f"{r['tag']:30s} {'ERROR':>12s}")
            continue
        status = "BLOWUP" if r.get('blowup') else "SURVIVED"
        T_star = r.get('T_star', '---')
        gamma = r.get('gamma', '---')
        if isinstance(T_star, float):
            T_star = f"{T_star:.8f}"
        if isinstance(gamma, float):
            gamma = f"{gamma:.4f}"
        print(f"{r['tag']:30s} {T_star:>12s} {gamma:>8s} {status:>10s}")

    # Paper validation
    print(f"\n--- Paper validation ---")
    for r in results:
        tag = r.get('tag', '')
        if 'hou2022_nr64' in tag and 'T_star' in r:
            print(f"  Hou 2022 Nr=64:  T*={r['T_star']:.6f} (paper: 0.002276)")
            print(f"                   γ={r.get('gamma','N/A')} (paper: 1.0)")
        if 'luohou_nr128' in tag and 'T_star' in r:
            print(f"  Luo-Hou Nr=128:  T*={r['T_star']:.6f} (paper: 0.003506)")
            print(f"                   γ={r.get('gamma','N/A')} (paper: 2.5)")

    with open(f"{RESULTS_DIR}/overnight_summary.json", 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nAll results saved to {RESULTS_DIR}/")


if __name__ == '__main__':
    run_batch()
