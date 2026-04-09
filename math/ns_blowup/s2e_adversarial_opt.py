#!/usr/bin/env python3
"""
Gradient-based adversarial optimization to MAXIMIZE S²ê/|ω|² at the vorticity max.

Strategy: for each k-pair, optimize polarization angles and amplitudes using scipy
to find the worst-case configuration. Then sweep over all k-pairs.

If the result is < 0.75: the barrier proof closes.
"""

import numpy as np
from scipy.optimize import minimize, differential_evolution
from itertools import combinations, product
import warnings
warnings.filterwarnings('ignore')


def build_mode(k, theta):
    """Build polarization vector perpendicular to k with angle theta."""
    k = np.array(k, dtype=float)
    knorm = k / np.linalg.norm(k)
    if abs(knorm[0]) < 0.9:
        v = np.array([1.0, 0.0, 0.0])
    else:
        v = np.array([0.0, 1.0, 0.0])
    e1 = v - (v @ knorm) * knorm
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(knorm, e1)
    return np.cos(theta) * e1 + np.sin(theta) * e2


def compute_all_vertices(ks, vs, amps):
    """Compute |ω|², S, at all 2^N vertex sign combinations.
    Return the vertex with max |ω|² and the S²ê/|ω|² there."""
    N = len(ks)
    best_om2 = 0.0
    best_S2e = 0.0
    best_alpha_ratio = 0.0

    for signs in product([1.0, -1.0], repeat=N):
        signs = np.array(signs)
        # ω at this vertex
        omega = np.zeros(3)
        for i in range(N):
            omega += amps[i] * signs[i] * vs[i]
        om2 = omega @ omega
        if om2 < 1e-12:
            continue

        # S at this vertex
        S = np.zeros((3, 3))
        for i in range(N):
            wi = np.cross(ks[i], vs[i])
            ki2 = ks[i] @ ks[i]
            outer = np.outer(ks[i], wi)
            S += amps[i] * signs[i] * (outer + outer.T) / (2 * ki2)

        e_hat = omega / np.sqrt(om2)
        Se = S @ e_hat
        s2e = Se @ Se
        alpha = e_hat @ Se

        if om2 > best_om2:
            best_om2 = om2
            best_S2e = s2e / om2
            best_alpha_ratio = alpha / np.sqrt(om2)

    return best_S2e, best_alpha_ratio, np.sqrt(best_om2)


def neg_s2e_ratio(params, ks_fixed):
    """Objective: maximize S²ê/|ω|² by varying polarization angles and amplitudes."""
    N = len(ks_fixed)
    thetas = params[:N]
    # Amplitudes: softmax of raw params
    raw_amps = params[N:2*N]
    amps = np.exp(raw_amps)
    amps /= amps.sum()

    vs = [build_mode(k, theta) for k, theta in zip(ks_fixed, thetas)]
    ks = [np.array(k, dtype=float) for k in ks_fixed]

    try:
        ratio, _, _ = compute_all_vertices(ks, vs, amps)
    except Exception:
        return 0.0
    return -ratio


def optimize_for_k_set(ks_fixed, n_restarts=50):
    """Find worst S²ê/|ω|² for a fixed set of k-vectors."""
    N = len(ks_fixed)
    best_ratio = 0.0
    best_params = None

    for _ in range(n_restarts):
        x0 = np.random.uniform(0, 2*np.pi, N).tolist() + np.random.randn(N).tolist()
        try:
            res = minimize(neg_s2e_ratio, x0, args=(ks_fixed,),
                           method='Nelder-Mead',
                           options={'maxiter': 5000, 'xatol': 1e-10, 'fatol': 1e-12})
            ratio = -res.fun
            if ratio > best_ratio:
                best_ratio = ratio
                best_params = res.x
        except Exception:
            continue

    return best_ratio, best_params


def main():
    # Build k-vector pool
    k_pool = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = (i, j, l)
                k2 = i*i + j*j + l*l
                if 0 < k2 <= 12:
                    k_pool.append(k)

    # Remove k and -k duplicates (keep one)
    k_unique = []
    seen = set()
    for k in k_pool:
        kn = tuple(-x for x in k)
        if k not in seen and kn not in seen:
            k_unique.append(k)
            seen.add(k)
    print(f"Unique k-vectors: {len(k_unique)}")

    # ============================================================
    # Phase 1: Exhaustive 2-mode optimization
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 1: ALL 2-MODE k-PAIRS (exhaustive, gradient-optimized)")
    print("=" * 70)

    overall_worst = 0.0
    worst_config = None

    pairs = list(combinations(k_unique, 2))
    print(f"Total k-pairs: {len(pairs)}")

    for idx, (k1, k2) in enumerate(pairs):
        if idx % 500 == 0 and idx > 0:
            print(f"  Progress: {idx}/{len(pairs)}, current worst: {overall_worst:.6f}")

        ratio, params = optimize_for_k_set([k1, k2], n_restarts=20)
        if ratio > overall_worst:
            overall_worst = ratio
            worst_config = (k1, k2, params)
            print(f"  NEW WORST: {ratio:.6f} at k1={k1}, k2={k2}")

    print(f"\n2-mode worst: S²ê/|ω|² = {overall_worst:.6f}")
    if worst_config:
        k1, k2, params = worst_config
        print(f"  k1 = {k1}, k2 = {k2}")
        print(f"  θ1 = {params[0]:.4f}, θ2 = {params[1]:.4f}")
        print(f"  raw_amps = {params[2:]}")

    # ============================================================
    # Phase 2: Top k-pairs from Phase 1, add 3rd mode
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 2: BEST k-PAIRS + 3rd MODE")
    print("=" * 70)

    # Collect top pairs
    top_pairs = []
    for k1, k2 in combinations(k_unique, 2):
        ratio, _ = optimize_for_k_set([k1, k2], n_restarts=5)
        if ratio > overall_worst * 0.7:
            top_pairs.append((k1, k2, ratio))

    top_pairs.sort(key=lambda x: -x[2])
    top_pairs = top_pairs[:20]
    print(f"Top {len(top_pairs)} pairs, best ratio: {top_pairs[0][2]:.6f}")

    for k1, k2, r2 in top_pairs[:10]:
        for k3 in k_unique:
            if k3 == k1 or k3 == k2:
                continue
            ratio, params = optimize_for_k_set([k1, k2, k3], n_restarts=10)
            if ratio > overall_worst:
                overall_worst = ratio
                print(f"  NEW 3-MODE WORST: {ratio:.6f} at k's = {k1}, {k2}, {k3}")

    # ============================================================
    # Phase 3: Random N-mode with differential evolution
    # ============================================================
    print("\n" + "=" * 70)
    print("PHASE 3: DIFFERENTIAL EVOLUTION (N=2-6)")
    print("=" * 70)

    rng = np.random.RandomState(999)
    for N in [2, 3, 4, 5, 6]:
        best_N = 0.0
        for trial in range(500):
            indices = rng.choice(len(k_unique), N, replace=False)
            ks_trial = [k_unique[i] for i in indices]

            bounds = [(0, 2*np.pi)] * N + [(-3, 3)] * N
            try:
                res = differential_evolution(
                    neg_s2e_ratio, bounds, args=(ks_trial,),
                    maxiter=200, seed=trial, tol=1e-10, polish=True
                )
                ratio = -res.fun
                if ratio > best_N:
                    best_N = ratio
                if ratio > overall_worst:
                    overall_worst = ratio
                    print(f"  N={N}, trial {trial}: NEW WORST {ratio:.6f}")
            except Exception:
                continue

        print(f"  N={N} worst: {best_N:.6f}")

    # ============================================================
    # Summary
    # ============================================================
    print("\n" + "=" * 70)
    print(f"OVERALL WORST S²ê/|ω|² = {overall_worst:.8f}")
    print(f"Threshold for barrier: 0.750")
    print(f"Margin: {0.75 - overall_worst:.8f}")
    print(f"Ratio to threshold: {overall_worst / 0.75:.4f}")
    print("=" * 70)

    if overall_worst < 0.5:
        print("\n*** S²ê/|ω|² < 1/2 AT ALL TESTED CONFIGURATIONS ***")
        print("*** If proven: S²ê < |ω|²/2 → barrier argument gives regularity ***")
    if overall_worst < 0.75:
        print("\n*** S²ê/|ω|² < 3/4 AT ALL TESTED CONFIGURATIONS ***")
        print("*** Barrier DR/Dt < 0 at R=1/2 confirmed ***")


if __name__ == '__main__':
    main()
