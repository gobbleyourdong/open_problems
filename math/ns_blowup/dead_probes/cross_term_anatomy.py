"""
numerical track — Cross-Term Anatomy

Decompose ||S||²_F at the vorticity maximum into:
  diagonal: Σ_k ||Ŝ_k||²_F cos²(k·x*)     [= |ω|²/2 by single-mode theorem]
  cross:    2 Σ_{j<k} Tr(Ŝ_j^T Ŝ_k) cos(k_j·x*) cos(k_k·x*)

And similarly for |ω|²:
  diagonal: Σ_k |ω̂_k|² cos²(k·x*)
  cross:    2 Σ_{j<k} (ω̂_j · ω̂_k) cos(k_j·x*) cos(k_k·x*)

The ratio (strain_cross / vorticity_cross) tells us HOW MUCH the Biot-Savart
projection depletes the cross-terms relative to the vorticity.

If strain_cross / vorticity_cross < 1/2 (matching the diagonal ratio):
  then ||S||²_F / |ω|² = 1/2 everywhere → Key Lemma trivially.

If strain_cross / vorticity_cross varies but stays < 3/4:
  then Key Lemma still holds.

The MECHANISM should be visible in this decomposition.
"""
import numpy as np
from itertools import combinations, product as iprod
from scipy.optimize import minimize

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def get_ks(max_k2=3):
    """All integer k with 0 < |k|² ≤ max_k2."""
    ks = []
    r = int(np.sqrt(max_k2)) + 1
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            for l in range(-r, r+1):
                mag2 = i*i + j*j + l*l
                if 0 < mag2 <= max_k2:
                    ks.append(np.array([i, j, l], float))
    return ks

def strain_matrix_single(k, v):
    """Strain tensor for one mode: S = -(1/2|k|²)(k⊗w + w⊗k) where w = k×v."""
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

def decompose_at_xstar(ks_sel, vs, x):
    """Compute diagonal and cross contributions at point x."""
    N = len(ks_sel)

    # Individual mode contributions at x
    cos_kx = [np.cos(k @ x) for k in ks_sel]
    omega_modes = [v * c for v, c in zip(vs, cos_kx)]
    strain_modes = [strain_matrix_single(k, v) * c for k, v, c in zip(ks_sel, vs, cos_kx)]

    # Total fields
    omega_total = sum(omega_modes)
    S_total = sum(strain_modes)

    om2 = omega_total @ omega_total
    S2_F = np.sum(S_total * S_total)

    if om2 < 1e-15:
        return None

    # Diagonal terms: Σ ||S_k||² cos²(k·x)
    S_diag = sum(np.sum(Sk * Sk) for Sk in strain_modes)
    om_diag = sum(np.dot(ok, ok) for ok in omega_modes)

    # Cross terms = total - diagonal
    S_cross = S2_F - S_diag
    om_cross = om2 - om_diag

    # Directional: S²ê at this point
    if om2 > 1e-15:
        e_hat = omega_total / np.sqrt(om2)
        Se = S_total @ e_hat
        S2e = Se @ Se
    else:
        S2e = 0

    return {
        'om2': om2,
        'S2_F': S2_F,
        'S2e': S2e,
        'S_diag': S_diag,
        'om_diag': om_diag,
        'S_cross': S_cross,
        'om_cross': om_cross,
        'ratio_total': S2_F / om2 if om2 > 0 else 0,
        'ratio_diag': S_diag / om_diag if om_diag > 0 else 0,
        'ratio_cross': S_cross / om_cross if abs(om_cross) > 1e-15 else float('nan'),
        'ratio_S2e': S2e / om2 if om2 > 0 else 0,
    }

def find_xstar(ks_sel, vs, n_starts=30):
    """Find the point that maximizes |ω(x)|²."""
    best_om2 = 0
    best_x = None
    for _ in range(n_starts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def neg_om2(x):
            omega = sum(v * np.cos(k @ x) for k, v in zip(ks_sel, vs))
            return -np.dot(omega, omega)
        res = minimize(neg_om2, x0, method='Nelder-Mead',
                       options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 10000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()
    return best_x

def run_anatomy(N_modes, n_trials=200, K2_max=3):
    """For random N-mode configurations, decompose the ratio at vorticity max."""
    all_ks = get_ks(K2_max)
    n_pool = len(all_ks)

    results = []
    for trial in range(n_trials):
        # Random selection of N modes
        if N_modes > n_pool:
            idx = np.arange(n_pool)
        else:
            idx = np.random.choice(n_pool, N_modes, replace=False)
        ks_sel = [all_ks[i] for i in idx]

        # Random polarizations perpendicular to k
        vs = []
        for k in ks_sel:
            e1, e2 = build_perp_basis(k)
            theta = np.random.uniform(0, 2*np.pi)
            vs.append(np.cos(theta)*e1 + np.sin(theta)*e2)

        # Find vorticity max
        x_star = find_xstar(ks_sel, vs, n_starts=15)
        if x_star is None:
            continue

        d = decompose_at_xstar(ks_sel, vs, x_star)
        if d is not None:
            results.append(d)

    return results

def main():
    print("=" * 70)
    print("CROSS-TERM ANATOMY: Understanding c(N) → 0")
    print("=" * 70)
    print()

    for N in [3, 4, 5, 6, 8, 10, 13, 16, 20]:
        n_trials = max(30, min(300, 3000 // N))
        results = run_anatomy(N, n_trials=n_trials)

        if not results:
            print(f"N={N}: no valid results")
            continue

        # Statistics
        ratio_total = [r['ratio_total'] for r in results]
        ratio_diag = [r['ratio_diag'] for r in results]
        ratio_cross = [r['ratio_cross'] for r in results if not np.isnan(r['ratio_cross'])]
        ratio_S2e = [r['ratio_S2e'] for r in results]

        # How much do cross-terms contribute?
        frac_cross_S = [r['S_cross'] / r['S2_F'] if r['S2_F'] > 1e-15 else 0 for r in results]
        frac_cross_om = [r['om_cross'] / r['om2'] if r['om2'] > 1e-15 else 0 for r in results]

        print(f"N = {N:3d} | trials = {len(results):4d}")
        print(f"  ||S||²_F / |ω|² : mean={np.mean(ratio_total):.4f}  max={np.max(ratio_total):.4f}")
        print(f"  S²ê / |ω|²      : mean={np.mean(ratio_S2e):.4f}  max={np.max(ratio_S2e):.4f}")
        print(f"  Diagonal ratio   : mean={np.mean(ratio_diag):.4f}  (should be ~0.5)")
        if ratio_cross:
            rc = np.array(ratio_cross)
            rc_finite = rc[np.isfinite(rc)]
            if len(rc_finite) > 0:
                print(f"  Cross-term ratio : mean={np.mean(rc_finite):.4f}  max={np.max(rc_finite):.4f}")
        print(f"  Cross fraction S : mean={np.mean(frac_cross_S):.4f}")
        print(f"  Cross fraction ω : mean={np.mean(frac_cross_om):.4f}")
        print(f"  Depletion factor : {np.mean(frac_cross_S) - np.mean(frac_cross_om):.4f}")
        print()

    print("=" * 70)
    print("KEY QUESTION: Does the cross-term ratio decrease with N?")
    print("If cross_ratio < 0.5 and decreasing → c(N) → 0 is algebraic.")
    print("If cross_fraction_S < cross_fraction_ω → depletion is geometric.")
    print("=" * 70)

if __name__ == '__main__':
    main()
