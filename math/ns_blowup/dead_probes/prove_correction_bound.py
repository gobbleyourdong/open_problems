"""
Try to prove: at x* = argmax|ω|, the correction C satisfies C > -|ω|²/4.

The identity: |S|²_F = |ω|²/2 - 2C
where C = Σ_{j<k} (v_j·n̂)(v_k·n̂)sin²θ cos(k_j·x*)cos(k_k·x*)

If C > -|ω|²/4: |S|²_F < |ω|² → S²ê ≤ (2/3)|S|²_F < (2/3)|ω|² = 0.667|ω|² < 0.75|ω|²

Strategy: decompose C using the max condition and show each part is bounded.

Key insight to test: can we express C in terms of a BILINEAR FORM
that is constrained by the max condition?
"""
import numpy as np
from itertools import product as iprod

def compute_S_mode(k, v):
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

def analyze_correction(ks, vs, x_star):
    """Detailed analysis of correction term structure at the max."""
    N = len(ks)

    omega = sum(v * np.cos(k @ x_star) for k, v in zip(ks, vs))
    om2 = omega @ omega
    if om2 < 1e-10:
        return None

    e_hat = omega / np.sqrt(om2)

    # Decompose: v_k = a_k ê + b_k, with phases
    phases = [np.cos(k @ x_star) for k in ks]
    a_vals = [(v @ e_hat) * p for v, p in zip(vs, phases)]  # a_k cos(k·x*)
    b_vecs = [v * p - a * e_hat for v, p, a in zip(vs, phases, a_vals)]  # b_k cos(k·x*)

    # Verify: Σa_k = |ω|, Σb_k = 0
    a_sum = sum(a_vals)
    b_sum = sum(b_vecs)

    # Correction per pair
    correction = 0.0
    pair_data = []

    for j in range(N):
        for l in range(j+1, N):
            n = np.cross(ks[j], ks[l])
            n_norm = np.linalg.norm(n)
            if n_norm < 1e-12:
                continue
            n_hat = n / n_norm
            cos_theta = (ks[j] @ ks[l]) / (np.linalg.norm(ks[j]) * np.linalg.norm(ks[l]))
            sin2_theta = 1 - cos_theta**2

            P = (vs[j] @ n_hat) * (vs[l] @ n_hat) * sin2_theta
            phase_prod = phases[j] * phases[l]
            term = P * phase_prod
            correction += term

            # Also decompose P into aligned and perpendicular contributions
            # v_j·n̂ = a_j(ê·n̂) + b_j·n̂ (at x*, after phase)
            vj_eff = vs[j] * phases[j]
            vl_eff = vs[l] * phases[l]
            pj = vj_eff @ n_hat
            pl = vl_eff @ n_hat

            pair_data.append({
                'j': j, 'l': l,
                'P': P, 'phase': phase_prod, 'term': term,
                'pj': pj, 'pl': pl,
                'sin2': sin2_theta
            })

    # Compute |S|²_F and S²ê
    S = sum(compute_S_mode(k, v) * np.cos(k @ x_star) for k, v in zip(ks, vs))
    S2_F = np.sum(S**2)
    Se = S @ e_hat
    S2e = Se @ Se

    return {
        'om2': om2,
        'S2_F': S2_F,
        'S2e': S2e,
        'correction': correction,
        'a_sum': a_sum,
        'b_sum_norm': np.linalg.norm(b_sum),
        'pairs': pair_data,
        'frob_ratio': S2_F / om2,
        's2e_ratio': S2e / om2,
        'corr_ratio': correction / om2,
        'N': N
    }

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("CORRECTION BOUND ANALYSIS")
    print("Need: C > -|ω|²/4 at the max")
    print("This gives |S|²_F < |ω|² → S²ê < (2/3)|ω|² < 3|ω|²/4")
    print("=" * 70)

    worst_corr_ratio = 0  # Most negative C/|ω|²
    worst_frob = 0
    worst_s2e = 0
    n_total = 0

    for trial in range(10000):
        N = np.random.choice([2, 3, 4, 5, 6, 8, 12])
        K_max = 3

        all_modes = []
        for i in range(-K_max, K_max+1):
            for j in range(-K_max, K_max+1):
                for l in range(-K_max, K_max+1):
                    k = np.array([i, j, l], float)
                    if 0 < k @ k <= K_max**2:
                        all_modes.append(k)

        if N > len(all_modes):
            N = len(all_modes)
        idx = np.random.choice(len(all_modes), min(N, len(all_modes)), replace=False)
        ks = [all_modes[i] for i in idx]
        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= k * (v @ k) / (k @ k)
            vs.append(v)

        # Find max |ω|
        best_x = np.zeros(3)
        best_om2 = 0
        M = 16
        xs_grid = np.linspace(0, 2*np.pi, M, endpoint=False)
        for i in range(M):
            for j in range(M):
                for l in range(M):
                    x = np.array([xs_grid[i], xs_grid[j], xs_grid[l]])
                    om = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
                    om2 = om @ om
                    if om2 > best_om2:
                        best_om2 = om2
                        best_x = x.copy()

        result = analyze_correction(ks, vs, best_x)
        if result is None:
            continue

        n_total += 1
        cr = result['corr_ratio']
        if cr < worst_corr_ratio:
            worst_corr_ratio = cr
        worst_frob = max(worst_frob, result['frob_ratio'])
        worst_s2e = max(worst_s2e, result['s2e_ratio'])

        if trial % 2000 == 0:
            print(f"  {trial}/10000: worst C/|ω|² = {worst_corr_ratio:.6f} "
                  f"(need > -0.250) | "
                  f"|S|²_F/|ω|² = {worst_frob:.6f} | "
                  f"S²ê/|ω|² = {worst_s2e:.6f}")

    print()
    print(f"Final ({n_total} trials):")
    print(f"  Worst C/|ω|²:      {worst_corr_ratio:.6f} (need > -0.250)")
    print(f"  Worst |S|²_F/|ω|²: {worst_frob:.6f} (need < 1.000 for path 1)")
    print(f"  Worst S²ê/|ω|²:    {worst_s2e:.6f} (need < 0.750)")
    print()

    holds = worst_corr_ratio > -0.25
    print(f"  C > -|ω|²/4? {holds}")
    if holds:
        print(f"  → |S|²_F < |ω|² ✓")
        print(f"  → S²ê ≤ (2/3)|S|²_F < (2/3)|ω|² = 0.667|ω|² < 0.75|ω|² ✓")
        print(f"  → KEY LEMMA HOLDS (if we can prove C > -|ω|²/4)")
    else:
        print(f"  C can be < -|ω|²/4. Need tighter analysis.")
        print(f"  But S²ê still < 0.75 (worst = {worst_s2e:.6f})")
