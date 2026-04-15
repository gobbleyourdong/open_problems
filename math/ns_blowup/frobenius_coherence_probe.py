"""
frobenius_coherence_probe.py — measure the off-diagonal / diagonal ratio
of ||S||²_F at the vorticity maximum x*, across N, for attempt_849.

Goal: test the empirical coherence bound

  off_diag := Σ_{j≠k} c_j c_k Tr(S_j S_k)
  diag     := Σ_j c_j² · Tr(S_j²) = (1/2) Σ c_j²  (for unit div-free modes)
  ratio    := (diag + off_diag) / (diag) = ||S||²_F / diag

For the Key Lemma via the unconditional operator-norm route, we want
||S||²_F / |ω|² ≤ 9/8. Empirically ≈ 0.66 (alignment_anatomy.py at N≤26).

The diagonal contribution alone gives ||S||²_F_diag / |ω|²_diag = 1/2 exactly.
If the off-diagonal contribution to ||S||²_F / |ω|² stays below 5/8 at all N,
the full ratio stays below 9/8. This is the coherence bound.

This probe checks: is the ratio off_diag / diag bounded as N grows, and if
so by what? The file does NOT prove anything — it measures the distribution
of the ratio across random samples.
"""
import numpy as np
from scipy.optimize import minimize


def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1., 0., 0.]) if abs(kn[0]) < 0.9 else np.array([0., 1., 0.])
    e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2


def strain_matrix(k, v):
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)


def get_ks(max_k2):
    r = int(np.sqrt(max_k2)) + 1
    ks = []
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            for l in range(-r, r + 1):
                m2 = i * i + j * j + l * l
                if 0 < m2 <= max_k2:
                    ks.append(np.array([i, j, l], float))
    return ks


def one_sample(N, K2_max, seed):
    rng = np.random.RandomState(seed)
    all_ks = get_ks(K2_max)
    n_pool = len(all_ks)
    if n_pool < N:
        return None
    idx = rng.choice(n_pool, N, replace=False)
    ks = [all_ks[i] for i in idx]
    vs = []
    for k in ks:
        e1, e2 = build_perp_basis(k)
        theta = rng.uniform(0, 2 * np.pi)
        vs.append(np.cos(theta) * e1 + np.sin(theta) * e2)

    def neg_om2(x):
        omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
        return -np.dot(omega, omega)

    best_om2 = 0
    best_x = None
    for _ in range(25):
        x0 = rng.uniform(0, 2 * np.pi, 3)
        res = minimize(neg_om2, x0, method='Nelder-Mead',
                       options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 5000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()
    # hard guard against near-zero ω artifacts
    if best_x is None or best_om2 < 0.01 * N:
        return None

    cs = np.array([np.cos(k @ best_x) for k in ks])
    Ss = [strain_matrix(k, v) for k, v in zip(ks, vs)]

    # Total strain at x*
    S_total = sum(c * Sj for c, Sj in zip(cs, Ss))
    # Diagonal part of ||S||²_F: Σ c_j² · Tr(S_j²)
    trS2_list = [np.sum(Sj * Sj) for Sj in Ss]  # = Tr(S_j²)
    diag = float(np.sum(cs ** 2 * np.array(trS2_list)))
    # Full ||S||²_F
    total = float(np.sum(S_total * S_total))
    off_diag = total - diag
    # |ω|² at x*
    omega = sum(v * c for v, c in zip(vs, cs))
    om2 = float(np.dot(omega, omega))

    return {
        'N': N,
        'om2': om2,
        'diag': diag,
        'off_diag': off_diag,
        'total': total,
        'ratio_full_over_om2': total / om2,
        'ratio_diag_over_om2': diag / om2,
        'ratio_off_over_om2': off_diag / om2,
        'off_over_diag': off_diag / diag if diag > 0 else float('nan'),
    }


def main():
    print("# frobenius_coherence_probe — attempt_849 empirical check")
    print("# Target: off_diag/|ω|² ≤ 5/8 (= 0.625)")
    print("# If mean + 3σ stays < 5/8 across N, coherence bound plausible.")
    print()
    print(f"{'N':>3} {'trials':>6} | "
          f"{'mean full/ω²':>14} {'max':>7} | "
          f"{'mean off/ω²':>13} {'max':>7} | "
          f"{'off/diag mean':>15} {'max':>7}")
    print("-" * 90)
    for N in [3, 5, 8, 12, 18, 26, 40, 60]:
        n_trials = max(40, min(300, 2000 // N))
        results = []
        for seed in range(n_trials):
            r = one_sample(N, K2_max=4, seed=seed)
            if r is not None:
                results.append(r)
        if not results:
            continue
        full = np.array([r['ratio_full_over_om2'] for r in results])
        off = np.array([r['ratio_off_over_om2'] for r in results])
        ratio_od = np.array([r['off_over_diag'] for r in results])
        print(f"{N:3d} {len(results):6d} | "
              f"{np.mean(full):14.4f} {np.max(full):7.4f} | "
              f"{np.mean(off):13.4f} {np.max(off):7.4f} | "
              f"{np.mean(ratio_od):15.4f} {np.max(ratio_od):7.4f}")

    print()
    print("Interpretation:")
    print("  Column 'mean full/ω²': empirical ||S||²_F/|ω|², target < 9/8 = 1.125")
    print("  Column 'mean off/ω²':  off-diagonal contribution; target < 5/8 = 0.625")
    print("  Column 'off/diag':     off-diag / diag ratio (scale-free)")


if __name__ == '__main__':
    main()
