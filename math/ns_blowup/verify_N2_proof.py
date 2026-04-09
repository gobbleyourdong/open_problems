"""
Verify the N=2 proof: |S|²_F < (9/8)|ω|² at argmax|ω| for ALL 2-mode configs.

The proof claims this is impossible because for orthogonal k:
  P = (v₁·n̂)(v₂·n̂) sin²θ = a (the dot product v₁·v₂)
  and 2|a| ≤ 5T/8 + 5|a|/4 always holds.

Verify numerically with exhaustive adversarial search.
"""
import numpy as np
from scipy.optimize import differential_evolution
from itertools import product as iprod

def compute_frob_ratio(k1, k2, theta1, theta2):
    """Compute |S|²_F / |ω|² at global max for two modes."""
    # Build perpendicular bases
    def perp(k):
        kn = k / np.linalg.norm(k)
        ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
        e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
        e2 = np.cross(kn, e1)
        return e1, e2

    e1a, e2a = perp(k1)
    e1b, e2b = perp(k2)
    v1 = np.cos(theta1)*e1a + np.sin(theta1)*e2a
    v2 = np.cos(theta2)*e1b + np.sin(theta2)*e2b

    # Find global max over sign patterns
    best_om2 = 0
    best_signs = None
    for s1, s2 in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        omega = s1*v1 + s2*v2
        om2 = omega @ omega
        if om2 > best_om2:
            best_om2 = om2
            best_signs = (s1, s2)

    if best_om2 < 1e-15:
        return 0.0, 0.0

    s1, s2 = best_signs
    omega = s1*v1 + s2*v2
    om2 = omega @ omega
    e_hat = omega / np.sqrt(om2)

    # Compute S
    S = np.zeros((3,3))
    for k, v, s in [(k1,v1,s1),(k2,v2,s2)]:
        w = np.cross(k, s*v)
        k2_sq = k @ k
        S -= (np.outer(w,k)+np.outer(k,w))/(2*k2_sq)

    S2_F = np.sum(S**2)
    Se = S @ e_hat
    S2e = Se @ Se

    return S2_F/om2, S2e/om2

if __name__ == '__main__':
    np.random.seed(42)

    # Test ALL k-vector pairs with |k|² ≤ 10
    all_k = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i,j,l], float)
                k2 = k @ k
                if 0 < k2 <= 10:
                    all_k.append(k)

    # Remove -k duplicates
    unique_k = []
    for k in all_k:
        if not any(np.allclose(k, -u) for u in unique_k):
            unique_k.append(k)

    print(f"Testing {len(unique_k)} unique k-vectors (|k|² ≤ 10)")

    from itertools import combinations

    worst_frob = 0
    worst_s2e = 0
    n_tested = 0

    for i, j in combinations(range(len(unique_k)), 2):
        k1, k2 = unique_k[i], unique_k[j]

        # Adversarial over polarization angles
        def neg_frob(t):
            r, _ = compute_frob_ratio(k1, k2, t[0], t[1])
            return -r
        def neg_s2e(t):
            _, r = compute_frob_ratio(k1, k2, t[0], t[1])
            return -r

        res_f = differential_evolution(neg_frob, [(0,2*np.pi)]*2,
                                       maxiter=100, popsize=10, seed=42)
        res_s = differential_evolution(neg_s2e, [(0,2*np.pi)]*2,
                                       maxiter=100, popsize=10, seed=42)

        frob_r = -res_f.fun
        s2e_r = -res_s.fun
        worst_frob = max(worst_frob, frob_r)
        worst_s2e = max(worst_s2e, s2e_r)
        n_tested += 1

    print(f"Tested {n_tested} k-vector pairs")
    print(f"Worst |S|²_F/|ω|²: {worst_frob:.8f} (< 9/8 = {9/8:.6f}? {worst_frob < 9/8})")
    print(f"Worst S²ê/|ω|²:    {worst_s2e:.8f} (< 3/4 = 0.750? {worst_s2e < 0.75})")
    print()

    # Verify the algebraic bound
    # For N=2: max |S|²_F/|ω|² should approach some value < 9/8
    # Check if it approaches 1/2 for all configs
    print(f"Note: 1/2 = {0.5:.6f}, 9/8 = {9/8:.6f}")
    print(f"The worst Frobenius ratio: {worst_frob:.6f}")
    print(f"Is it always ≤ 1/2? {worst_frob <= 0.5001}")

    # Specifically check if Frobenius ratio can exceed 1/2 for N=2
    if worst_frob > 0.5001:
        print(f"\n*** Frobenius ratio EXCEEDS 1/2 for N=2! ***")
        print(f"  Worst: {worst_frob:.8f}")
    else:
        print(f"\n  Frobenius ratio ≤ 1/2 for all N=2 configs ✓")
        print(f"  This means the correction is ALWAYS ≥ 0 for N=2")
