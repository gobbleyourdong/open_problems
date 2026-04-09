#!/usr/bin/env python3
"""
Test: is |∇u|² ≤ C|ω|² at the global max of |ω|?
If C < 13/8 = 1.625: then S²ê < 3|ω|²/4 via trace-free bound.

Also compute the ACTUAL S²ê/|ω|² to compare.
"""

import numpy as np
from itertools import product, combinations

np.random.seed(42)

def compute_at_vertex(ks, vs, amps, signs):
    """Compute |ω|², |∇u|², |S|², S²ê at a specific vertex with given signs."""
    N = len(ks)
    omega = np.zeros(3)
    grad_u = np.zeros((3, 3))

    for i in range(N):
        k = np.array(ks[i], dtype=float)
        v = np.array(vs[i], dtype=float)
        a = amps[i]
        s = signs[i]

        omega += a * s * v
        w = np.cross(k, v)
        k2 = k @ k
        grad_u += a * s * np.outer(w, k) / k2  # Note: ∇u = w⊗k/|k|² for each mode

    om2 = omega @ omega
    if om2 < 1e-14:
        return None

    e_hat = omega / np.sqrt(om2)

    # |∇u|² (Frobenius norm)
    nabla_u_sq = np.sum(grad_u**2)

    # S = sym(∇u)
    S = (grad_u + grad_u.T) / 2
    S_sq = np.sum(S**2)  # |S|²

    # S·ê
    Se = S @ e_hat
    S2e = Se @ Se

    # α = ê·S·ê
    alpha = e_hat @ Se

    return {
        'om2': om2,
        'nabla_u_sq': nabla_u_sq,
        'S_sq': S_sq,
        'S2e': S2e,
        'alpha': alpha,
        'omega': omega.copy(),
        'e_hat': e_hat.copy()
    }


def search_worst_ratio(n_trials=50000):
    """Find worst |∇u|²/|ω|² and S²ê/|ω|² at global max."""

    k_pool = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i, j, l])
                if 0 < k @ k <= 12:
                    k_pool.append(k)

    rng = np.random.RandomState(123)

    worst_ratio = 0.0
    worst_s2e = 0.0
    worst_alpha = 0.0

    for trial in range(n_trials):
        N = rng.randint(2, 8)
        indices = rng.choice(len(k_pool), N, replace=False)
        ks = [k_pool[i] for i in indices]
        vs = []
        for k in ks:
            kn = k / np.linalg.norm(k)
            if abs(kn[0]) < 0.9:
                v = np.array([1., 0., 0.])
            else:
                v = np.array([0., 1., 0.])
            e1 = v - (v @ kn) * kn
            e1 /= np.linalg.norm(e1)
            e2 = np.cross(kn, e1)
            theta = rng.uniform(0, 2 * np.pi)
            vs.append(np.cos(theta) * e1 + np.sin(theta) * e2)

        amps = rng.exponential(1.0, N)
        amps /= amps.sum()

        # Find global max vertex
        best = None
        for signs in product([1, -1], repeat=N):
            signs = list(signs)
            result = compute_at_vertex(ks, vs, amps, signs)
            if result and (best is None or result['om2'] > best['om2']):
                best = result

        if best is None or best['om2'] < 1e-10:
            continue

        ratio = best['nabla_u_sq'] / best['om2']
        s2e_ratio = best['S2e'] / best['om2']
        alpha_ratio = best['alpha'] / np.sqrt(best['om2'])

        if ratio > worst_ratio:
            worst_ratio = ratio
            if trial < 1000 or ratio > 1.3:
                print(f"Trial {trial} (N={N}): |∇u|²/|ω|² = {ratio:.6f}, "
                      f"S²ê/|ω|² = {s2e_ratio:.6f}, α/|ω| = {alpha_ratio:.4f}")

        if s2e_ratio > worst_s2e:
            worst_s2e = s2e_ratio

        if abs(alpha_ratio) > worst_alpha:
            worst_alpha = abs(alpha_ratio)

    print(f"\n{'='*60}")
    print(f"Worst |∇u|²/|ω|²  = {worst_ratio:.6f}  (threshold 13/8 = {13/8:.4f})")
    print(f"Worst S²ê/|ω|²    = {worst_s2e:.6f}  (threshold 3/4 = 0.7500)")
    print(f"Worst |α/|ω||      = {worst_alpha:.6f}  (threshold 1/2 = 0.5000)")

    # Check trace-free bound: S²ê ≤ (2/3)(|∇u|² - |ω|²/2)
    tf_bound = (2/3) * (worst_ratio - 0.5)
    print(f"\nTrace-free bound: S²ê/|ω|² ≤ (2/3)({worst_ratio:.4f} - 0.5) = {tf_bound:.6f}")
    print(f"  → {'CLOSES' if tf_bound < 0.75 else 'FAILS'} the barrier (threshold 0.75)")

    return worst_ratio, worst_s2e


def identity_test():
    """Verify: |∇u|² = |S|² + |ω|²/2 at all test points."""
    print("\nIDENTITY TEST: |∇u|² = |S|² + |ω|²/2")
    rng = np.random.RandomState(456)
    max_error = 0.0

    for _ in range(1000):
        N = rng.randint(2, 6)
        k_pool = [np.array([rng.randint(-2,3), rng.randint(-2,3), rng.randint(-2,3)])
                   for _ in range(N)]
        k_pool = [k for k in k_pool if k@k > 0]
        if len(k_pool) < 2:
            continue

        ks = k_pool[:N]
        vs = []
        for k in ks:
            kn = k / np.linalg.norm(k)
            v = np.array([1., 0., 0.]) if abs(kn[0]) < 0.9 else np.array([0., 1., 0.])
            e1 = v - (v @ kn) * kn
            e1 /= np.linalg.norm(e1)
            e2 = np.cross(kn, e1)
            theta = rng.uniform(0, 2*np.pi)
            vs.append(np.cos(theta) * e1 + np.sin(theta) * e2)

        amps = rng.exponential(1., N)
        signs = [1] * N

        result = compute_at_vertex(ks, vs, amps, signs)
        if result is None:
            continue

        # Check identity
        lhs = result['nabla_u_sq']
        rhs = result['S_sq'] + result['om2'] / 2
        error = abs(lhs - rhs) / max(abs(lhs), 1e-10)
        max_error = max(max_error, error)

    print(f"Max relative error: {max_error:.2e} (should be ~machine epsilon)")


if __name__ == '__main__':
    identity_test()
    print()
    search_worst_ratio(n_trials=100000)
