"""
ODD INSTANCE — Per-Pair Mechanism Analysis

For each pair (j,k) of modes, compute:
  strain_cross_jk = Tr(Ŝ_j^T Ŝ_k) at x*
  vorticity_cross_jk = (ω̂_j · ω̂_k) at x*

The ratio strain_cross_jk / vorticity_cross_jk tells us HOW MUCH
the Biot-Savart projection depletes each pair.

HYPOTHESIS: The ratio depends on the ANGLE between k_j and k_k.
If k_j ∥ k_k: ratio = 1/2 (same projection, no extra cancellation)
If k_j ⊥ k_k: ratio → 0 (orthogonal projections cancel)
If k_j anti-parallel k_k: ratio = 1/2 (same as parallel)

If this is true: the average ratio over many random pairs → 0 as N → ∞
because most pairs have non-parallel wavevectors.

This would be the ANALYTICAL MECHANISM for c(N) → 0.
"""
import numpy as np
from itertools import combinations

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def strain_matrix(k, v):
    """Strain from single mode: S = -(1/2|k|²)(k⊗w + w⊗k), w = k×v"""
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

def analyze_pair(k1, k2, n_angles=500):
    """
    For a pair of wavevectors k1, k2:
    Average over all polarization angles the ratio
      Tr(S1^T S2) / (v1 · v2)
    at x = 0 (where cos(k·x) = 1 for all k).
    """
    e1_1, e2_1 = build_perp_basis(k1)
    e1_2, e2_2 = build_perp_basis(k2)

    cos_angle = abs((k1 @ k2) / (np.linalg.norm(k1) * np.linalg.norm(k2)))

    strain_crosses = []
    vort_crosses = []
    ratios = []

    for _ in range(n_angles):
        t1 = np.random.uniform(0, 2*np.pi)
        t2 = np.random.uniform(0, 2*np.pi)
        v1 = np.cos(t1)*e1_1 + np.sin(t1)*e2_1
        v2 = np.cos(t2)*e1_2 + np.sin(t2)*e2_2

        S1 = strain_matrix(k1, v1)
        S2 = strain_matrix(k2, v2)

        # Cross-terms at x=0 (where cos(k·x) = 1 for all modes)
        sc = np.sum(S1 * S2)  # Tr(S1^T S2) = Frobenius inner product
        vc = v1 @ v2

        strain_crosses.append(sc)
        vort_crosses.append(vc)
        if abs(vc) > 1e-10:
            ratios.append(sc / vc)

    return {
        'cos_angle_kk': cos_angle,
        'mean_strain_cross': np.mean(strain_crosses),
        'mean_vort_cross': np.mean(vort_crosses),
        'mean_ratio': np.mean(ratios) if ratios else float('nan'),
        'std_ratio': np.std(ratios) if ratios else float('nan'),
        'rms_strain': np.sqrt(np.mean(np.array(strain_crosses)**2)),
        'rms_vort': np.sqrt(np.mean(np.array(vort_crosses)**2)),
        'rms_ratio': np.sqrt(np.mean(np.array(strain_crosses)**2)) /
                     max(np.sqrt(np.mean(np.array(vort_crosses)**2)), 1e-15),
    }

def get_ks(max_k2=3):
    ks = []
    r = int(np.sqrt(max_k2)) + 1
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            for l in range(-r, r+1):
                mag2 = i*i + j*j + l*l
                if 0 < mag2 <= max_k2:
                    ks.append(np.array([i, j, l], float))
    return ks

def main():
    print("=" * 70)
    print("PER-PAIR MECHANISM: How Biot-Savart depletes strain cross-terms")
    print("=" * 70)

    all_ks = get_ks(3)
    print(f"Pool: {len(all_ks)} k-vectors with K²≤3\n")

    # Bin by cos(angle between k-vectors)
    angle_bins = {}

    pairs = list(combinations(range(len(all_ks)), 2))
    print(f"Analyzing {len(pairs)} pairs...")

    for i, j in pairs:
        k1, k2 = all_ks[i], all_ks[j]
        result = analyze_pair(k1, k2, n_angles=300)

        # Bin by cos_angle
        ca = round(result['cos_angle_kk'], 2)
        if ca not in angle_bins:
            angle_bins[ca] = []
        angle_bins[ca].append(result)

    print()
    print(f"{'cos∠(k1,k2)':>12} | {'N_pairs':>8} | {'⟨strain⟩':>10} | {'⟨vort⟩':>10} | "
          f"{'rms_ratio':>10} | {'⟨ratio⟩':>10}")
    print("-" * 80)

    for ca in sorted(angle_bins.keys(), reverse=True):
        results = angle_bins[ca]
        n = len(results)
        ms = np.mean([r['mean_strain_cross'] for r in results])
        mv = np.mean([r['mean_vort_cross'] for r in results])
        rr = np.mean([r['rms_ratio'] for r in results])
        mr = np.nanmean([r['mean_ratio'] for r in results])
        print(f"{ca:>12.2f} | {n:>8d} | {ms:>10.6f} | {mv:>10.6f} | {rr:>10.4f} | {mr:>10.4f}")

    print()
    print("=" * 70)
    print("HYPOTHESIS TEST:")
    print("  If rms_ratio < 0.5 for non-parallel pairs → depletion is geometric")
    print("  If rms_ratio → 0 as angle → 90° → mechanism is angular cancellation")
    print("=" * 70)

    # Also: compute the ANALYTICAL formula
    print()
    print("ANALYTICAL CROSS-TERM FORMULA")
    print("=" * 70)
    print()
    print("For modes (k1, v1) and (k2, v2):")
    print("  S1 = -(1/2|k1|²)(k1⊗w1 + w1⊗k1),  w1 = k1×v1")
    print("  S2 = -(1/2|k2|²)(k2⊗w2 + w2⊗k2),  w2 = k2×v2")
    print()
    print("  Tr(S1^T S2) = (1/4|k1|²|k2|²) × ")
    print("    [(k1·k2)(w1·w2) + (k1·w2)(w1·k2) + (w1·k2)(k1·w2) + (w1·w2)(k1·k2)]")
    print("  = (1/4|k1|²|k2|²) × [2(k1·k2)(w1·w2) + 2(k1·w2)(w1·k2)]")
    print()

    # Verify the formula numerically
    print("Verifying analytical formula...")
    k1 = np.array([1., 0., 0.])
    k2 = np.array([0., 1., 0.])
    v1 = np.array([0., 1., 0.])  # v1 ⊥ k1
    v2 = np.array([0., 0., 1.])  # v2 ⊥ k2
    w1 = np.cross(k1, v1)  # = (0, 0, 1)
    w2 = np.cross(k2, v2)  # = (1, 0, 0)

    S1 = strain_matrix(k1, v1)
    S2 = strain_matrix(k2, v2)
    numerical = np.sum(S1 * S2)

    k1k2 = k1 @ k2
    w1w2 = w1 @ w2
    k1w2 = k1 @ w2
    w1k2 = w1 @ k2
    analytical = (2*k1k2*w1w2 + 2*k1w2*w1k2) / (4 * (k1@k1) * (k2@k2))

    print(f"  k1={k1}, k2={k2}, v1={v1}, v2={v2}")
    print(f"  w1={w1}, w2={w2}")
    print(f"  Numerical:  Tr(S1^T S2) = {numerical:.6f}")
    print(f"  Analytical: formula     = {analytical:.6f}")
    print(f"  Match: {'YES' if abs(numerical - analytical) < 1e-10 else 'NO'}")
    print(f"  v1·v2 = {v1@v2:.4f}")
    print(f"  Ratio (strain/vort) = {analytical / (v1@v2) if abs(v1@v2) > 1e-10 else 'N/A'}")
    print()

    # More examples
    print("More examples:")
    test_cases = [
        ([1,0,0], [1,0,0], [0,1,0], [0,0,1]),  # parallel k, orthogonal v
        ([1,0,0], [1,0,0], [0,1,0], [0,1,0]),  # parallel k, parallel v
        ([1,0,0], [0,1,0], [0,1,0], [1,0,0]),  # orthogonal k, swapped v
        ([1,0,0], [0,0,1], [0,1,0], [1,0,0]),  # orthogonal k
        ([1,1,0], [1,-1,0], [0,0,1], [0,0,1]), # anti-correlated k
    ]
    for k1c, k2c, v1c, v2c in test_cases:
        k1 = np.array(k1c, float)
        k2 = np.array(k2c, float)
        v1 = np.array(v1c, float)
        v2 = np.array(v2c, float)
        w1 = np.cross(k1, v1)
        w2 = np.cross(k2, v2)
        S1 = strain_matrix(k1, v1)
        S2 = strain_matrix(k2, v2)
        sc = np.sum(S1 * S2)
        vc = v1 @ v2
        cos_kk = (k1@k2) / (np.linalg.norm(k1)*np.linalg.norm(k2))
        print(f"  k1={k1c}, k2={k2c}, cos∠={cos_kk:.2f} | "
              f"strain_cross={sc:.4f}, vort_cross={vc:.4f}, "
              f"ratio={'N/A' if abs(vc)<1e-10 else f'{sc/vc:.4f}'}")

if __name__ == '__main__':
    main()
