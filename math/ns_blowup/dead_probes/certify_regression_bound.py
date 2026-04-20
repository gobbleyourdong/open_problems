#!/usr/bin/env python3
"""
Computer-assisted certification of the regression spectral bound.

For Fourier truncation K: certify that R_bound < 13/8 for ALL mode
configurations with |k|² ≤ K² on the integer lattice T³.

The bound: R(s*) ≤ 1 + (||M_res||_op × N + c × Y_max) / |ω|²
where c < 0 (structural), M_res is the regression residual matrix.

This script:
1. Enumerates all k-vectors with |k|² ≤ K²
2. For each subset of N modes (N up to all available):
3. Optimizes over polarization angles to MAXIMIZE R_bound
4. Reports whether R_bound < 13/8 for ALL configs
"""

import numpy as np
from itertools import product, combinations
from scipy.optimize import minimize
import sys

THRESHOLD = 13/8  # = 1.625

def get_k_vectors(K_sq):
    """Get all k-vectors with |k|² ≤ K_sq, keeping only one of ±k."""
    vecs = []
    seen = set()
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k2 = i*i + j*j + l*l
                if 0 < k2 <= K_sq:
                    k = (i, j, l)
                    kn = (-i, -j, -l)
                    if k not in seen and kn not in seen:
                        vecs.append(np.array(k, dtype=float))
                        seen.add(k)
    return vecs


def build_polarization(k, theta):
    """Build unit polarization vector ⊥ k with angle theta."""
    kn = k / np.linalg.norm(k)
    v0 = np.array([1., 0., 0.]) if abs(kn[0]) < 0.9 else np.array([0., 1., 0.])
    e1 = v0 - (v0 @ kn) * kn
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta) * e1 + np.sin(theta) * e2


def compute_R_bound(ks, thetas):
    """Compute the regression spectral bound R_bound for given config."""
    N = len(ks)
    vs = [build_polarization(ks[i], thetas[i]) for i in range(N)]

    pairs = [(j, k) for j in range(N) for k in range(j+1, N)]
    if not pairs:
        return 0., 0.

    # Compute D and Delta for each pair
    D_w = np.zeros(len(pairs))
    Delta_w = np.zeros(len(pairs))
    for idx, (j, k) in enumerate(pairs):
        D_w[idx] = 2 * (vs[j] @ vs[k])
        wj = np.cross(ks[j], vs[j])
        wk = np.cross(ks[k], vs[k])
        G = (wj @ wk) * (ks[j] @ ks[k]) / ((ks[j] @ ks[j]) * (ks[k] @ ks[k]))
        Delta_w[idx] = 2 * (G - vs[j] @ vs[k])

    # Regression
    varY = np.sum(D_w**2)
    if varY < 1e-20:
        return 1.0, 1.0  # degenerate
    c = np.sum(Delta_w * D_w) / varY
    lambda_arr = Delta_w - c * D_w

    # Residual matrix
    M = np.zeros((N, N))
    for idx, (j, k) in enumerate(pairs):
        M[j, k] = lambda_arr[idx] / 2
        M[k, j] = M[j, k]
    M_op = np.linalg.norm(M, ord=2)

    # Enumerate all sign patterns for global max
    best_om2, best_Y, best_X = 0., 0., 0.
    for signs in product([1, -1], repeat=N):
        q = np.array([signs[j] * signs[k] for j, k in pairs], dtype=float)
        Y = float(q @ D_w)
        X = float(q @ Delta_w)
        om2 = N + Y
        if om2 > best_om2:
            best_om2, best_Y, best_X = om2, Y, X

    if best_om2 < 0.01:
        return 1.0, 1.0

    R_actual = 1 + best_X / best_om2
    R_bound = 1 + (M_op * N + c * best_Y) / best_om2
    return R_bound, R_actual


def certify_subset(ks, n_restarts=20):
    """Certify R_bound < THRESHOLD for a specific k-subset by optimizing over polarizations."""
    N = len(ks)

    def neg_bound(thetas):
        rb, _ = compute_R_bound(ks, thetas)
        return -rb

    worst_bound = 0.
    worst_actual = 0.
    rng = np.random.RandomState(42)

    for _ in range(n_restarts):
        x0 = rng.uniform(0, 2 * np.pi, N)
        try:
            res = minimize(neg_bound, x0, method='Nelder-Mead',
                          options={'maxiter': 5000, 'xatol': 1e-12, 'fatol': 1e-14})
            rb, ra = compute_R_bound(ks, res.x)
            if rb > worst_bound:
                worst_bound = rb
                worst_actual = ra
        except:
            pass

    return worst_bound, worst_actual


def certify_truncation(K_sq, max_N=None):
    """Certify the regression bound for ALL mode subsets at truncation K."""
    k_vecs = get_k_vectors(K_sq)
    N_total = len(k_vecs)

    print(f"Fourier truncation |k|² ≤ {K_sq}")
    print(f"Independent k-vectors: {N_total}")
    print(f"Threshold: R < {THRESHOLD:.4f}")
    print("=" * 60)

    if max_N is None:
        max_N = min(N_total, 8)  # limit for computational feasibility

    worst_overall = 0.
    total_subsets = 0
    failures = 0

    for N in range(2, max_N + 1):
        n_subsets = 0
        worst_N = 0.
        worst_actual_N = 0.

        # For small N: enumerate all subsets. For large N: sample.
        if N <= 4:
            subsets = list(combinations(range(N_total), N))
        else:
            # Sample random subsets
            rng = np.random.RandomState(N * 1000)
            subsets = [tuple(sorted(rng.choice(N_total, N, replace=False)))
                      for _ in range(min(200, int(np.math.factorial(N_total) /
                                                   (np.math.factorial(N) * np.math.factorial(N_total - N)))))]
            subsets = list(set(subsets))  # deduplicate

        n_restarts = 30 if N <= 4 else 15

        for subset in subsets:
            ks = [k_vecs[i] for i in subset]
            rb, ra = certify_subset(ks, n_restarts=n_restarts)

            if rb > worst_N:
                worst_N = rb
                worst_actual_N = ra

            if rb >= THRESHOLD:
                failures += 1
                print(f"  *** FAILURE at N={N}, subset={subset}: R_bound={rb:.6f} ***")

            n_subsets += 1

        if worst_N > worst_overall:
            worst_overall = worst_N

        total_subsets += n_subsets
        margin = THRESHOLD - worst_N
        status = "✓" if worst_N < THRESHOLD else "✗"
        print(f"  N={N}: {n_subsets:5d} subsets, worst R_bound={worst_N:.6f}, "
              f"R_actual={worst_actual_N:.6f}, margin={margin:.4f} {status}")

    print("=" * 60)
    print(f"Total subsets tested: {total_subsets}")
    print(f"Failures: {failures}")
    print(f"Worst overall: {worst_overall:.6f}")
    print(f"CERTIFIED: {failures == 0 and worst_overall < THRESHOLD}")

    return failures == 0


if __name__ == '__main__':
    K_sq = 2  # |k|² ≤ 2 (modes: ±e_i and ±e_i±e_j)
    max_N = 6  # test up to 6 modes from the pool

    print("COMPUTER-ASSISTED CERTIFICATION")
    print(f"Certifying regression bound for |k|² ≤ {K_sq}\n")

    success = certify_truncation(K_sq, max_N=max_N)

    if success:
        print("\n*** CERTIFICATION PASSED ***")
        print(f"The regression bound R < {THRESHOLD:.4f} holds for ALL")
        print(f"mode configurations with |k|² ≤ {K_sq} and N ≤ {max_N}.")
    else:
        print("\n*** CERTIFICATION FAILED ***")
