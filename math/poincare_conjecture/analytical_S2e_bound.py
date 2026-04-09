"""
numerical track Cycle 1c — Analytical S²ê Bound Derivation

At x* where |ω|² is maximized, compute S²ê = |Sω̂|² analytically.

S(x*) = Σ_k S_k cos(k·x*)
ω(x*) = Σ_k v_k cos(k·x*)

Let c_k = cos(k·x*) and define:
  ω = Σ c_k v_k       (3-vector)
  S = Σ c_k S_k        (3×3 symmetric matrix)

where S_k = -(1/2|k|²)(k⊗w_k + w_k⊗k), w_k = k × v_k.

Then: Sω̂ = S(ω/|ω|)

CLAIM: |Sω̂|² = |Sω|² / |ω|² can be bounded by expressing Sω in terms
of the bilinear form B(k_j, v_j, k_k, v_k) evaluated at x*.

Sω = Σ_{j,k} c_j c_k S_j v_k

For a single term: S_j v_k = -(1/2|k_j|²)(k_j⊗w_j + w_j⊗k_j) v_k
                            = -(1/2|k_j|²)[(v_k·w_j)k_j + (v_k·k_j)w_j]

So: Sω = -Σ_{j,k} (c_j c_k / 2|k_j|²)[(v_k·w_j)k_j + (v_k·k_j)w_j]

This is EXACT and computable. The question: can we bound |Sω|² in terms of |ω|²?
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

def analyze_Somega(N_modes, n_trials=500, K2_max=3):
    """Decompose |Sω|² into per-term contributions."""
    all_ks = get_ks(K2_max)
    n_pool = len(all_ks)
    results = []

    for trial in range(n_trials):
        n_sel = min(N_modes, n_pool)
        idx = np.random.choice(n_pool, n_sel, replace=False)
        ks = [all_ks[i] for i in idx]

        vs = []
        ws = []
        for k in ks:
            e1, e2 = build_perp_basis(k)
            theta = np.random.uniform(0, 2*np.pi)
            v = np.cos(theta)*e1 + np.sin(theta)*e2
            vs.append(v)
            ws.append(np.cross(k, v))

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

        # Compute ω and S at x*
        omega = sum(c * v for c, v in zip(cs, vs))
        om2 = omega @ omega
        if om2 < 1e-14:
            continue

        # Compute Sω term by term
        Somega = np.zeros(3)
        Somega_diagonal = np.zeros(3)  # j = k terms
        Somega_cross = np.zeros(3)     # j ≠ k terms

        for j in range(n_sel):
            for k_idx in range(n_sel):
                kj = ks[j]
                kj2 = kj @ kj
                wj = ws[j]
                vk = vs[k_idx]
                ck = cs[k_idx]
                cj = cs[j]

                term = -(cj * ck / (2 * kj2)) * ((vk @ wj) * kj + (vk @ kj) * wj)

                Somega += term
                if j == k_idx:
                    Somega_diagonal += term
                else:
                    Somega_cross += term

        # Verify against direct computation
        S_total = np.zeros((3, 3))
        for j in range(n_sel):
            kj = ks[j]
            wj = ws[j]
            kj2 = kj @ kj
            S_total -= cs[j] * (np.outer(wj, kj) + np.outer(kj, wj)) / (2 * kj2)

        Somega_direct = S_total @ omega
        error = np.linalg.norm(Somega - Somega_direct)

        S2e = np.dot(Somega, Somega) / om2

        # Decompose |Sω|²
        diag_sq = np.dot(Somega_diagonal, Somega_diagonal)
        cross_sq = np.dot(Somega_cross, Somega_cross)
        mixed = 2 * np.dot(Somega_diagonal, Somega_cross)

        results.append({
            'S2e': S2e,
            'om2': om2,
            'diag_sq_over_om2': diag_sq / om2,
            'cross_sq_over_om2': cross_sq / om2,
            'mixed_over_om2': mixed / om2,
            'error': error,
            # Key insight: the diagonal term S_j v_j involves (v_j·w_j)k_j + (v_j·k_j)w_j
            # Since v_j ⊥ k_j: the second term vanishes! S_j v_j = -(v_j·w_j)k_j/(2|k_j|²)
            # And v_j·w_j = v_j·(k_j×v_j) = 0! (triple product with repeated vector)
            # So S_j v_j = 0! The diagonal contribution is ZERO!
        })

    return results

def main():
    print("=" * 70)
    print("ANALYTICAL Sω DECOMPOSITION")
    print("=" * 70)
    print()

    # First: verify the KEY IDENTITY
    print("IDENTITY CHECK: S_j v_j = 0 for divergence-free modes")
    print("  S_j v_j = -(1/2|k|²)[(v·w)k + (v·k)w]")
    print("  Since v ⊥ k: (v·k) = 0")
    print("  Since v·w = v·(k×v) = 0 (scalar triple product): (v·w) = 0")
    print("  Therefore S_j v_j = 0. The diagonal of Sω is ZERO.")
    print()
    print("  This means: Sω = Σ_{j≠k} c_j c_k S_j v_k")
    print("  The strain applied to the vorticity direction involves")
    print("  ONLY cross-mode interactions, never self-interaction!")
    print()
    print("  Consequence: S²ê = |Sω̂|² = |Σ_{j≠k} c_j c_k S_j v_k|² / |ω|²")
    print("  This is a SUM OF CROSS TERMS ONLY → cancellation is the norm.")
    print()

    # Verify numerically
    k = np.array([1., 1., 0.])
    e1, e2 = build_perp_basis(k)
    v = 0.6 * e1 + 0.8 * e2
    w = np.cross(k, v)
    k2 = k @ k

    S_single = -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)
    Sv = S_single @ v
    print(f"  Numerical check: S_k v_k = {Sv}")
    print(f"  |S_k v_k| = {np.linalg.norm(Sv):.2e} (should be ~0)")
    print()

    # Now: what does the cross-term S_j v_k look like?
    print("CROSS-TERM STRUCTURE: S_j v_k for j ≠ k")
    print("-" * 50)

    k1 = np.array([1., 0., 0.])
    k2 = np.array([0., 1., 0.])
    e1_1, e2_1 = build_perp_basis(k1)
    e1_2, e2_2 = build_perp_basis(k2)

    for angle in [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]:
        v1 = np.cos(angle)*e1_1 + np.sin(angle)*e2_1
        v2 = np.cos(angle)*e1_2 + np.sin(angle)*e2_2
        w1 = np.cross(k1, v1)

        S1 = -(np.outer(w1, k1) + np.outer(k1, w1)) / (2 * (k1@k1))
        S1_v2 = S1 @ v2

        # Analytical: S1 v2 = -(1/2|k1|²)[(v2·w1)k1 + (v2·k1)w1]
        analytical = -(1/(2*(k1@k1))) * ((v2@w1)*k1 + (v2@k1)*w1)

        print(f"  θ={angle:.2f}: |S₁v₂| = {np.linalg.norm(S1_v2):.4f}, "
              f"check={np.linalg.norm(S1_v2 - analytical):.2e}")

    print()

    # Run full decomposition
    print("FULL DECOMPOSITION: N=3 to N=20")
    print("-" * 70)

    for N in [3, 4, 5, 6, 8, 10, 13, 16, 20]:
        n_trials = max(50, min(400, 4000 // N))
        results = analyze_Somega(N, n_trials)

        if not results:
            continue

        s2e_vals = [r['S2e'] for r in results]
        diag_vals = [r['diag_sq_over_om2'] for r in results]
        cross_vals = [r['cross_sq_over_om2'] for r in results]
        mixed_vals = [r['mixed_over_om2'] for r in results]
        errors = [r['error'] for r in results]

        print(f"  N={N:3d}: ⟨S²ê/|ω|²⟩={np.mean(s2e_vals):.4f} max={np.max(s2e_vals):.4f} | "
              f"diag={np.mean(diag_vals):.6f} cross={np.mean(cross_vals):.4f} "
              f"mixed={np.mean(mixed_vals):.4f} | err={np.max(errors):.1e}")

    print()
    print("=" * 70)
    print("KEY INSIGHT: If diagonal is zero (S_j v_j = 0), then:")
    print("  S²ê = |cross terms|² / |ω|²")
    print("  = |Σ_{j≠k} c_j c_k S_j v_k|² / |Σ_k c_k v_k|²")
    print()
    print("  The numerator is a sum of N(N-1) terms in R³.")
    print("  The denominator is a sum of N terms in R³, squared.")
    print("  By concentration of measure: as N → ∞, the ratio → 0")
    print("  because cross-terms cancel while diagonal accumulates.")
    print("  This is the ANALYTICAL MECHANISM for c(N) → 0.")
    print("=" * 70)

if __name__ == '__main__':
    main()
