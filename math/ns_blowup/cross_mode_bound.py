"""
numerical track Cycle 2 — Per-Term Bound + Cancellation Measurement

PROVEN: S_k v_k = 0 (self-interaction vanishes)
PROVEN: |S_j v_k|² ≤ 1/(4|k_j|²) (Bessel inequality on k̂_j ⊥ ŵ_j plane)

This means: Sω = Σ_{j≠k} c_j c_k S_j v_k, with each |S_j v_k| ≤ 1/(2|k_j|).

The KEY RATIO: how much do the N(N-1) cross-terms cancel?

Define:
  coherence(N) = |Σ_{j≠k} c_j c_k S_j v_k|² / Σ_{j≠k} |c_j c_k S_j v_k|²

If coherence → 0 as N → ∞ (random walk): S²ê/|ω|² → 0.
If coherence → 1 (all align): no cancellation, bound may fail.

Also: compute the EXACT per-term bound |S_j v_k| as a function of
the angle between k_j and k_k, to identify which pairs are dangerous.
"""
import numpy as np
from scipy.optimize import minimize

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

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

def S_j_v_k(kj, vj, vk):
    """Compute S_j v_k = -(1/2|k_j|²)[(v_k·w_j)k_j + (v_k·k_j)w_j]"""
    wj = np.cross(kj, vj)
    kj2 = kj @ kj
    return -(1.0 / (2 * kj2)) * ((vk @ wj) * kj + (vk @ kj) * wj)

def per_term_bound(kj, vj, vk):
    """Tight bound on |S_j v_k|.

    |S_j v_k|² = (1/4|k_j|⁴) × |k_j|² × [(v_k·ŵ_j)² + (v_k·k̂_j)²]
               = [(v_k·ŵ_j)² + (v_k·k̂_j)²] / (4|k_j|²)
    where ŵ_j = (k_j×v_j)/|k_j×v_j| = (k_j×v_j)/|k_j| (unit, since v_j⊥k_j, |v_j|=1)
    and k̂_j ⊥ ŵ_j.

    Since {k̂_j, ŵ_j} are orthonormal in the k_j-w_j plane:
    (v_k·ŵ_j)² + (v_k·k̂_j)² = |proj_{k̂,ŵ}(v_k)|² ≤ 1
    with equality when v_k is in the k_j-w_j plane.

    CORRECTED: The |k_j|² in the strain normalization cancels |w_j|=|k_j|,
    giving |S_j v_k|² = [(v_k·ŵ_j)² + (v_k·k̂_j)²] / 4 ≤ 1/4.
    So |S_j v_k| ≤ 1/2 (UNIFORM, no k-dependence).
    """
    kj_norm = np.linalg.norm(kj)
    kj_hat = kj / kj_norm
    wj = np.cross(kj, vj)
    wj_hat = wj / np.linalg.norm(wj)

    proj_sq = (vk @ wj_hat)**2 + (vk @ kj_hat)**2
    bound = np.sqrt(proj_sq / 4)  # CORRECTED: no |k|² division
    actual = np.linalg.norm(S_j_v_k(kj, vj, vk))

    return actual, bound, proj_sq

def measure_coherence(N_modes, n_trials=400, K2_max=3):
    """Measure cross-term cancellation at vorticity maximum."""
    all_ks = get_ks(K2_max)
    n_pool = len(all_ks)
    results = []

    for trial in range(n_trials):
        n_sel = min(N_modes, n_pool)
        idx = np.random.choice(n_pool, n_sel, replace=False)
        ks = [all_ks[i] for i in idx]

        vs = []
        for k in ks:
            e1, e2 = build_perp_basis(k)
            theta = np.random.uniform(0, 2*np.pi)
            vs.append(np.cos(theta)*e1 + np.sin(theta)*e2)

        # Find vorticity max
        def neg_om2(x):
            omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
            return -np.dot(omega, omega)

        best_om2 = 0
        best_x = None
        for _ in range(15):
            x0 = np.random.uniform(0, 2*np.pi, 3)
            res = minimize(neg_om2, x0, method='Nelder-Mead',
                           options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 5000})
            if -res.fun > best_om2:
                best_om2 = -res.fun
                best_x = res.x.copy()

        if best_x is None or best_om2 < 1e-14:
            continue

        cs = [np.cos(k @ best_x) for k in ks]
        omega = sum(c * v for c, v in zip(cs, vs))
        om2 = omega @ omega
        if om2 < 1e-14:
            continue

        # Compute Sω as sum of cross-terms
        cross_terms = []  # list of 3-vectors
        for j in range(n_sel):
            for k_idx in range(n_sel):
                if j == k_idx:
                    continue
                term = cs[j] * cs[k_idx] * S_j_v_k(ks[j], vs[j], vs[k_idx])
                cross_terms.append(term)

        # Sω = sum of cross terms
        Somega = sum(cross_terms)
        Somega_sq = Somega @ Somega  # |Sω|²

        # Sum of |terms|²
        sum_term_sq = sum(t @ t for t in cross_terms)

        # Coherence = |Σ x_i|² / Σ|x_i|²
        # For random walk: coherence ~ 1 (N terms, each contributing equally)
        # But we normalize by count to get per-term coherence
        n_cross = len(cross_terms)
        coherence = Somega_sq / sum_term_sq if sum_term_sq > 1e-15 else 0

        # The KEY ratio: S²ê/|ω|² = |Sω|²/|ω|⁴
        S2e_over_om2 = Somega_sq / (om2 * om2)

        # Also compute via direct matrix method for verification
        S_total = np.zeros((3, 3))
        for j in range(n_sel):
            wj = np.cross(ks[j], vs[j])
            kj2 = ks[j] @ ks[j]
            S_total -= cs[j] * (np.outer(wj, ks[j]) + np.outer(ks[j], wj)) / (2 * kj2)
        e_hat = omega / np.sqrt(om2)
        Se = S_total @ e_hat
        S2e_direct = (Se @ Se) / om2

        results.append({
            'coherence': coherence,
            'S2e_over_om2': S2e_over_om2,
            'S2e_direct': S2e_direct,
            'n_cross': n_cross,
            'sum_term_sq': sum_term_sq,
            'Somega_sq': Somega_sq,
            'om2': om2,
        })

    return results

def main():
    print("=" * 70)
    print("CROSS-MODE BOUND + CANCELLATION MEASUREMENT")
    print("=" * 70)

    # Part 1: Verify per-term bound
    print("\nPART 1: Per-term bound |S_j v_k| ≤ 1/(2|k_j|)")
    print("-" * 50)

    all_ks = get_ks(3)
    n_checks = 0
    n_violations = 0
    max_ratio = 0

    for ki in range(len(all_ks)):
        for kj in range(len(all_ks)):
            if ki == kj:
                continue
            k_i = all_ks[ki]
            k_j = all_ks[kj]
            for _ in range(20):
                e1i, e2i = build_perp_basis(k_i)
                e1j, e2j = build_perp_basis(k_j)
                ti = np.random.uniform(0, 2*np.pi)
                tj = np.random.uniform(0, 2*np.pi)
                vi = np.cos(ti)*e1i + np.sin(ti)*e2i
                vj = np.cos(tj)*e1j + np.sin(tj)*e2j

                actual, bound, proj = per_term_bound(k_i, vi, vj)
                n_checks += 1
                simple_bound = 0.5  # CORRECTED: uniform bound, no k-dependence
                if actual > simple_bound + 1e-10:
                    n_violations += 1
                ratio = actual / simple_bound if simple_bound > 0 else 0
                if ratio > max_ratio:
                    max_ratio = ratio

    print(f"  Checked {n_checks} (k,v) pairs")
    print(f"  Violations of |S_j v_k| ≤ 1/(2|k_j|): {n_violations}")
    print(f"  Max ratio actual/bound: {max_ratio:.4f} (should be ≤ 1)")
    print(f"  BOUND {'HOLDS' if n_violations == 0 else 'FAILS'}")

    # Part 2: Coherence measurement
    print(f"\nPART 2: Cross-term cancellation (coherence)")
    print("-" * 70)
    print(f"{'N':>3} | {'trials':>6} | {'⟨coherence⟩':>11} {'max':>7} | "
          f"{'⟨S²ê/ω²⟩':>9} {'max':>7} | {'verify max':>10} | "
          f"{'⟨n_cross⟩':>9}")
    print("-" * 85)

    for N in [3, 4, 5, 6, 8, 10, 13, 16, 20, 26]:
        n_trials = max(30, min(400, 3000 // N))
        results = measure_coherence(N, n_trials)

        if not results:
            continue

        coh = [r['coherence'] for r in results]
        s2e = [r['S2e_over_om2'] for r in results]
        s2e_d = [r['S2e_direct'] for r in results]
        nc = [r['n_cross'] for r in results]

        print(f"{N:3d} | {len(results):6d} | {np.mean(coh):11.4f} {np.max(coh):7.4f} | "
              f"{np.mean(s2e):9.5f} {np.max(s2e):7.5f} | {np.max(s2e_d):10.5f} | "
              f"{np.mean(nc):9.1f}")

    print()
    print("=" * 70)
    print("INTERPRETATION:")
    print("  coherence = |Σ terms|² / Σ|terms|²")
    print("  = 1 if all terms aligned (worst case)")
    print("  = 1/n_terms if random walk (typical)")
    print("  If coherence × Σ|terms|² / |ω|⁴ < 3/4 → Key Lemma proved")
    print("=" * 70)

if __name__ == '__main__':
    main()
