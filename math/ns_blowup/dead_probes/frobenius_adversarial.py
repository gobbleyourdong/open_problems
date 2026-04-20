"""
ADVERSARIAL search for worst |S|²_F / |ω|² at the vorticity maximum.

Uses differential evolution to maximize the Frobenius ratio over:
  - Polarization angles θ_k (orientation of ω̂_k in the plane ⊥ k)
  - Position x (we evaluate at the exact max)

If worst ratio < 3/4 = 0.75: Key Lemma follows from
  S²ê ≤ (2/3)|S|²_F < (2/3)(3/4)|ω|² = |ω|²/2 < 3|ω|²/4  ← WRONG

Actually: S²ê ≤ |S|²_F. So if |S|²_F < 3|ω|²/4: Key Lemma holds directly.
And S²ê ≤ (2/3)|S|²_F. So if |S|²_F < (3/2)(3/4)|ω|² = 9|ω|²/8: also works.
"""

import numpy as np
from scipy.optimize import differential_evolution
from itertools import combinations, product as iprod

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def compute_frobenius_ratio(ks, thetas):
    """For given k-vectors and polarization angles, find x* and compute |S|²_F/|ω|²."""
    N = len(ks)
    bases = [build_perp_basis(k) for k in ks]

    # Build polarization vectors
    vs = []
    for i, (e1, e2) in enumerate(bases):
        vs.append(np.cos(thetas[i]) * e1 + np.sin(thetas[i]) * e2)

    # Find the global max of |ω|² over all sign patterns and positions
    # For each sign pattern: ω(x) = Σ s_k v_k cos(k·x) (using real field)
    # At the max: gradient = 0 → k·x is determined

    best_ratio = 0

    for signs in iprod([1.0, -1.0], repeat=N):
        # Effective amplitudes
        eff_vs = [s * v for s, v in zip(signs, vs)]

        # ω(x) = Σ eff_v_k cos(k_k·x)
        # At the max of |ω|², all cos(k_k·x) should be +1 (phases aligned)
        # But with integer k-vectors on T³, not all can be +1 simultaneously
        # The actual max is found by evaluating on a grid

        # Grid search (coarse)
        best_om2 = 0
        best_x = np.zeros(3)
        M = 24  # Grid resolution
        xs = np.linspace(0, 2*np.pi, M, endpoint=False)

        for i in range(M):
            for j in range(M):
                for l in range(M):
                    x = np.array([xs[i], xs[j], xs[l]])
                    omega = sum(ev * np.cos(k @ x) for k, ev in zip(ks, eff_vs))
                    om2 = omega @ omega
                    if om2 > best_om2:
                        best_om2 = om2
                        best_x = x.copy()

        # Refine
        for _ in range(10):
            h = 1e-5
            grad = np.zeros(3)
            omega0 = sum(ev * np.cos(k @ best_x) for k, ev in zip(ks, eff_vs))
            f0 = omega0 @ omega0
            for d in range(3):
                xp = best_x.copy()
                xp[d] += h
                om_p = sum(ev * np.cos(k @ xp) for k, ev in zip(ks, eff_vs))
                grad[d] = (om_p @ om_p - f0) / h

            for step in [0.05, 0.01, 0.002]:
                xt = best_x + step * grad / (np.linalg.norm(grad) + 1e-12)
                om_t = sum(ev * np.cos(k @ xt) for k, ev in zip(ks, eff_vs))
                if om_t @ om_t > best_om2:
                    best_om2 = om_t @ om_t
                    best_x = xt

        # Compute S and Frobenius ratio at best_x
        omega = sum(ev * np.cos(k @ best_x) for k, ev in zip(ks, eff_vs))
        om2 = omega @ omega
        if om2 < 1e-15:
            continue

        S = np.zeros((3, 3))
        for k, ev in zip(ks, eff_vs):
            w = np.cross(k, ev)
            k2 = k @ k
            phase = np.cos(k @ best_x)
            S -= phase * (np.outer(w, k) + np.outer(k, w)) / (2 * k2)

        S_frob2 = np.sum(S**2)
        e_hat = omega / np.sqrt(om2)
        Se = S @ e_hat
        s2e = Se @ Se

        ratio_frob = S_frob2 / om2
        ratio_s2e = s2e / om2

        if ratio_frob > best_ratio:
            best_ratio = ratio_frob

    return best_ratio

def adversarial_search(ks, n_iter=200, popsize=15):
    """Use DE to maximize |S|²_F / |ω|² over polarization angles."""
    N = len(ks)
    bounds = [(0, 2*np.pi)] * N

    def neg_ratio(thetas):
        return -compute_frobenius_ratio(ks, thetas)

    result = differential_evolution(neg_ratio, bounds, maxiter=n_iter,
                                    popsize=popsize, seed=42, tol=1e-8)
    return -result.fun

if __name__ == '__main__':
    np.random.seed(42)

    # Build K=√2 shell
    raw = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for l in range(-1, 2):
                k2 = i*i + j*j + l*l
                if 0 < k2 <= 2:
                    raw.append(np.array([i, j, l], float))

    # Keep unique (remove -k duplicates)
    unique = []
    for k in raw:
        if not any(np.allclose(k, -u) for u in unique):
            unique.append(k)

    print(f"K=√2 shell: {len(unique)} unique k-vectors")
    print()

    # Test all N=2,3,4 subsets (adversarial)
    for N in [2, 3, 4]:
        subs = list(combinations(range(len(unique)), N))
        print(f"N={N}: {len(subs)} subsets")

        worst = 0
        worst_sub = None
        for sub in subs:
            ks = [unique[i] for i in sub]
            ratio = adversarial_search(ks, n_iter=100, popsize=10)
            if ratio > worst:
                worst = ratio
                worst_sub = sub
            # Progress
            if subs.index(sub) % 20 == 0:
                print(f"  {subs.index(sub)+1}/{len(subs)} done, current worst: {worst:.6f}")

        print(f"  WORST |S|²_F/|ω|²: {worst:.6f} (< 0.75? {worst < 0.75})")
        print(f"  Worst subset: {[unique[i].astype(int).tolist() for i in worst_sub]}")
        print()

    # Also test N=5 (sample 50 subsets)
    N = 5
    subs5 = list(combinations(range(len(unique)), N))
    np.random.shuffle(subs5)
    subs5 = subs5[:50]
    print(f"N={N}: testing {len(subs5)} random subsets")

    worst5 = 0
    for idx, sub in enumerate(subs5):
        ks = [unique[i] for i in sub]
        ratio = adversarial_search(ks, n_iter=80, popsize=10)
        worst5 = max(worst5, ratio)
        if idx % 10 == 0:
            print(f"  {idx+1}/{len(subs5)} done, current worst: {worst5:.6f}")

    print(f"  WORST |S|²_F/|ω|²: {worst5:.6f} (< 0.75? {worst5 < 0.75})")

    # Test with K=1 shell (simpler modes)
    print()
    print("=== K=1 shell (|k|²=1) ===")
    k1_modes = [np.array([1,0,0.]), np.array([0,1,0.]), np.array([0,0,1.])]
    for N in [2, 3]:
        for sub in combinations(range(3), N):
            ks = [k1_modes[i] for i in sub]
            ratio = adversarial_search(ks, n_iter=200, popsize=15)
            print(f"  N={N}, k={[k.astype(int).tolist() for k in ks]}: "
                  f"|S|²_F/|ω|² = {ratio:.6f}")

    # Test with mixed K shells
    print()
    print("=== Mixed K shells ===")
    mixed = [np.array([1,0,0.]), np.array([0,1,0.]),
             np.array([1,1,0.]), np.array([1,0,1.])]
    ratio = adversarial_search(mixed, n_iter=200, popsize=15)
    print(f"  Mixed 4 modes: |S|²_F/|ω|² = {ratio:.6f}")

    mixed5 = mixed + [np.array([0,1,1.])]
    ratio5 = adversarial_search(mixed5, n_iter=200, popsize=15)
    print(f"  Mixed 5 modes: |S|²_F/|ω|² = {ratio5:.6f}")

    # Try some higher K modes
    print()
    print("=== Higher K modes ===")
    high_k = [np.array([2,0,0.]), np.array([0,2,0.]), np.array([0,0,2.])]
    for N in [2, 3]:
        for sub in combinations(range(3), N):
            ks = [high_k[i] for i in sub]
            ratio = adversarial_search(ks, n_iter=200, popsize=15)
            print(f"  N={N}, k={[k.astype(int).tolist() for k in ks]}: "
                  f"|S|²_F/|ω|² = {ratio:.6f}")
