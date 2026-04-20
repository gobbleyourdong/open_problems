"""
Analyze the 4% of cases where the correction is NEGATIVE at the vorticity max.
What structural features cause |S|²_F > |ω|²/2?

Key structural constraint at x* = argmax|ω|:
  ω(x*) = |ω|ê  →  Σ b_k cos(k·x*) = 0  (perpendicular components cancel)
  a_k cos(k·x*) ≥ 0 for all k  (sign-flip constraint)

We decompose v_k = a_k ê + b_k (a_k = v_k·ê, b_k ⊥ ê).
"""
import numpy as np

def compute_S_mode(k, v):
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

def analyze_field(ks, vs, x_star):
    """Full analysis at the vorticity max."""
    N = len(ks)

    omega = sum(v * np.cos(k @ x_star) for k, v in zip(ks, vs))
    om2 = omega @ omega
    if om2 < 1e-10:
        return None

    e_hat = omega / np.sqrt(om2)

    S = sum(compute_S_mode(k, v) * np.cos(k @ x_star) for k, v in zip(ks, vs))
    S2_F = np.sum(S**2)
    Se = S @ e_hat
    S2e = Se @ Se

    # Decompose: a_k = (v_k · ê) cos(k·x*), b_k component
    a_total = 0.0
    b_total_norm = 0.0
    perp_sum = np.zeros(3)
    modes_info = []

    for k, v in zip(ks, vs):
        phase = np.cos(k @ x_star)
        a_k = (v @ e_hat) * phase  # Contribution to |ω| along ê
        b_k = v * phase - a_k * e_hat  # Perpendicular contribution

        a_total += a_k
        perp_sum += b_k
        b_total_norm += np.linalg.norm(b_k)**2

        modes_info.append({
            'k': k, 'v': v, 'phase': phase,
            'a_k': a_k, 'b_k_norm': np.linalg.norm(b_k),
            'cos_gamma': abs(v @ e_hat) / (np.linalg.norm(v) + 1e-15)
        })

    # Compute correction terms
    correction = 0.0
    correction_details = []

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
            phase_prod = np.cos(ks[j] @ x_star) * np.cos(ks[l] @ x_star)
            term = P * phase_prod

            correction += term
            correction_details.append({
                'j': j, 'l': l,
                'P': P, 'phase': phase_prod, 'term': term,
                'theta': np.arccos(np.clip(cos_theta, -1, 1)),
                'vj_n': vs[j] @ n_hat, 'vl_n': vs[l] @ n_hat
            })

    return {
        'om2': om2,
        'S2_F': S2_F,
        'S2e': S2e,
        'ratio_frob': S2_F / om2,
        'ratio_s2e': S2e / om2,
        'correction': correction,
        'a_total': a_total,
        'perp_cancel': np.linalg.norm(perp_sum),
        'b_energy': b_total_norm,
        'N': N,
        'modes': modes_info,
        'terms': correction_details
    }

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("NEGATIVE CORRECTION ANALYSIS")
    print("When does |S|²_F > |ω|²/2 at the vorticity max?")
    print("=" * 70)

    negative_cases = []
    positive_cases = []

    for trial in range(5000):
        N = np.random.choice([2, 3, 4, 5, 6, 8])
        K_max = 2

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
        M = 20
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

        # Refine
        for _ in range(5):
            h = 1e-4
            grad = np.zeros(3)
            omega0 = sum(v * np.cos(k @ best_x) for k, v in zip(ks, vs))
            f0 = omega0 @ omega0
            for d in range(3):
                xp = best_x.copy(); xp[d] += h
                om_p = sum(v * np.cos(k @ xp) for k, v in zip(ks, vs))
                grad[d] = (om_p @ om_p - f0) / h
            for step in [0.1, 0.01, 0.001]:
                xt = best_x + step * grad / (np.linalg.norm(grad) + 1e-12)
                om_t = sum(v * np.cos(k @ xt) for k, v in zip(ks, vs))
                if om_t @ om_t > best_om2:
                    best_om2 = om_t @ om_t
                    best_x = xt

        result = analyze_field(ks, vs, best_x)
        if result is None:
            continue

        if result['correction'] < -1e-10:
            negative_cases.append(result)
        else:
            positive_cases.append(result)

    print(f"\nTotal: {len(positive_cases)} positive, {len(negative_cases)} negative")
    print(f"Rate: {100*len(negative_cases)/(len(positive_cases)+len(negative_cases)):.1f}% negative")

    # Analyze negative cases
    if negative_cases:
        print("\n" + "=" * 70)
        print("NEGATIVE CASE STATISTICS")
        print("=" * 70)

        Ns = [c['N'] for c in negative_cases]
        ratios = [c['ratio_frob'] for c in negative_cases]
        b_energies = [c['b_energy']/c['om2'] for c in negative_cases]
        perp_cancels = [c['perp_cancel']/np.sqrt(c['om2']) for c in negative_cases]

        print(f"  N distribution: {dict(sorted([(n, Ns.count(n)) for n in set(Ns)]))}")
        print(f"  Worst |S|²_F/|ω|²: {max(ratios):.6f}")
        print(f"  Mean  |S|²_F/|ω|²: {np.mean(ratios):.6f}")
        print(f"  Mean b_energy/|ω|²: {np.mean(b_energies):.6f}")
        print(f"  Mean perp cancel: {np.mean(perp_cancels):.6f} (should be ~0)")

        # Compare with positive cases
        Ns_pos = [c['N'] for c in positive_cases]
        ratios_pos = [c['ratio_frob'] for c in positive_cases]
        b_energies_pos = [c['b_energy']/c['om2'] for c in positive_cases]

        print(f"\n  POSITIVE CASES comparison:")
        print(f"  N distribution: {dict(sorted([(n, Ns_pos.count(n)) for n in set(Ns_pos)]))}")
        print(f"  Mean |S|²_F/|ω|²: {np.mean(ratios_pos):.6f}")
        print(f"  Mean b_energy/|ω|²: {np.mean(b_energies_pos):.6f}")

        # Key insight: how much perpendicular energy relative to aligned
        print(f"\n  PERPENDICULAR vs ALIGNED energy:")
        for cases, label in [(negative_cases, "NEG"), (positive_cases[:200], "POS")]:
            align_frac = []
            for c in cases:
                a2_sum = sum(m['a_k']**2 for m in c['modes'])
                total = sum((np.linalg.norm(m['v'])*abs(m['phase']))**2 for m in c['modes'])
                if total > 1e-10:
                    align_frac.append(a2_sum / total)
            print(f"  {label}: aligned fraction mean={np.mean(align_frac):.4f} "
                  f"min={min(align_frac):.4f} max={max(align_frac):.4f}")

        # Show worst case in detail
        print("\n" + "=" * 70)
        print("WORST NEGATIVE CASE DETAIL")
        print("=" * 70)
        worst = max(negative_cases, key=lambda c: c['ratio_frob'])
        print(f"  N={worst['N']}, |S|²_F/|ω|² = {worst['ratio_frob']:.6f}")
        print(f"  Correction = {worst['correction']:.6f}")
        print(f"  |ω|² = {worst['om2']:.6f}")
        print(f"  Modes:")
        for i, m in enumerate(worst['modes']):
            print(f"    {i}: k={m['k'].astype(int)}, a={m['a_k']:.4f}, "
                  f"|b|={m['b_k_norm']:.4f}, cosγ={m['cos_gamma']:.4f}, "
                  f"phase={m['phase']:.4f}")
        print(f"  Correction terms:")
        for t in sorted(worst['terms'], key=lambda t: t['term']):
            print(f"    ({t['j']},{t['l']}): P={t['P']:.4f} × phase={t['phase']:.4f} "
                  f"= {t['term']:.4f}  [θ={np.degrees(t['theta']):.1f}°]")

    # Key analysis: does the ratio DECREASE with N?
    print("\n" + "=" * 70)
    print("FROBENIUS RATIO BY N")
    print("=" * 70)
    all_cases = positive_cases + negative_cases
    for N in sorted(set(c['N'] for c in all_cases)):
        subset = [c for c in all_cases if c['N'] == N]
        ratios = [c['ratio_frob'] for c in subset]
        print(f"  N={N:2d}: count={len(subset):4d}  max={max(ratios):.6f}  "
              f"mean={np.mean(ratios):.6f}  min={min(ratios):.6f}")
