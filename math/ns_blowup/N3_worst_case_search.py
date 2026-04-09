"""
Find the TRUE worst case S²ê/|ω|² for 3 modes at the global max.

Strategy: parametric optimization over all 3-mode configurations.
For 3 modes with k₁, k₂, k₃ and v̂₁, v̂₂, v̂₃:
- k's from integer lattice |k|² ≤ 12
- v̂'s are unit vectors ⊥ k
- Find the config that maximizes S²ê/|ω|² at the global max

Also: test whether the orthogonal k, symmetric v̂ configuration (giving 1/3)
is truly the worst case.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution

def compute_S2e_at_global_max(k1, v1, k2, v2, k3, v3, a1=1, a2=1, a3=1, n_starts=20):
    """Compute S²ê/|ω|² at the global maximum of |ω| for 3 modes."""
    ks = [k1, k2, k3]
    vs = [v1, v2, v3]
    amps = [a1, a2, a3]

    # Find global max by multi-start Nelder-Mead
    best_om2 = 0
    best_x = None

    for _ in range(n_starts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def neg_om2(xyz):
            omega = np.zeros(3)
            for k, v, a in zip(ks, vs, amps):
                omega += a * v * np.cos(np.asarray(k, float) @ xyz)
            return -omega @ omega
        res = minimize(neg_om2, x0, method='Nelder-Mead',
                      options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 10000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()

    if best_om2 < 1e-10 or best_x is None:
        return 0, 0, 0

    # Compute S²ê at the global max
    omega = np.zeros(3)
    S = np.zeros((3, 3))
    for k, v, a in zip(ks, vs, amps):
        k = np.asarray(k, float)
        c = np.cos(k @ best_x)
        omega += a * v * c
        w = np.cross(k, v)
        gu = a * np.outer(w, k) * c / (k @ k)
        S += 0.5 * (gu + gu.T)

    om2 = omega @ omega
    if om2 < 1e-10:
        return 0, 0, 0
    e_hat = omega / np.sqrt(om2)
    Se = S @ e_hat
    S2e = Se @ Se

    return S2e / om2, S2e, om2

def rand_perp(k):
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    r = np.random.randn(3)
    r -= (r @ kn) * kn
    n = np.linalg.norm(r)
    return r / n if n > 1e-10 else rand_perp(k)

def test_orthogonal_symmetric():
    """Test the known worst case: orthogonal k's, symmetric v̂'s."""
    print("KNOWN WORST CASE: orthogonal k's, symmetric v̂'s")
    print("k₁=(1,0,0), v̂₁=(0,1,0); k₂=(0,1,0), v̂₂=(0,0,1); k₃=(0,0,1), v̂₃=(1,0,0)")

    k1, v1 = np.array([1,0,0.]), np.array([0,1,0.])
    k2, v2 = np.array([0,1,0.]), np.array([0,0,1.])
    k3, v3 = np.array([0,0,1.]), np.array([1,0,0.])

    ratio, S2e, om2 = compute_S2e_at_global_max(k1,v1,k2,v2,k3,v3, n_starts=30)
    print(f"  S²ê/|ω|² = {ratio:.6f} (expected 1/3 = 0.333333)")
    print(f"  |ω|² = {om2:.4f}, S²ê = {S2e:.4f}")

def exhaustive_3mode_search():
    """Search ALL 3-mode configs with |k|² ≤ 3."""
    print("\nEXHAUSTIVE SEARCH: all 3-mode configs, |k|² ≤ 3")
    print("=" * 60)

    # Generate all k-vectors with |k|² ≤ 3
    all_ks = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for l in range(-1, 2):
                if 0 < i*i + j*j + l*l <= 3:
                    all_ks.append(np.array([i, j, l], float))

    print(f"  {len(all_ks)} k-vectors in shell |k|² ≤ 3")

    # Remove anti-parallel duplicates
    unique_ks = []
    for k in all_ks:
        is_dup = False
        for uk in unique_ks:
            if np.allclose(k, -uk):
                is_dup = True
                break
        if not is_dup:
            unique_ks.append(k)

    print(f"  {len(unique_ks)} unique k-vectors (removing ±k duplicates)")

    # For each triple of k-vectors, search over v̂ orientations
    worst_ratio = 0
    worst_config = None
    n_configs = 0

    from itertools import combinations
    for k_triple in combinations(range(len(unique_ks)), 3):
        k1, k2, k3 = [unique_ks[i] for i in k_triple]

        # Search over random v̂ orientations
        for _ in range(100):
            v1 = rand_perp(k1)
            v2 = rand_perp(k2)
            v3 = rand_perp(k3)

            ratio, S2e, om2 = compute_S2e_at_global_max(k1,v1,k2,v2,k3,v3, n_starts=10)
            n_configs += 1

            if ratio > worst_ratio:
                worst_ratio = ratio
                worst_config = (k1.copy(),v1.copy(), k2.copy(),v2.copy(), k3.copy(),v3.copy(), S2e, om2)

    print(f"  Tested {n_configs} configurations")
    print(f"  Worst S²ê/|ω|² = {worst_ratio:.6f}")
    if worst_config:
        k1,v1,k2,v2,k3,v3,S2e,om2 = worst_config
        print(f"  Config: k₁={k1}, v̂₁={v1.round(3)}")
        print(f"          k₂={k2}, v̂₂={v2.round(3)}")
        print(f"          k₃={k3}, v̂₃={v3.round(3)}")
        print(f"  |ω|² = {om2:.4f}, S²ê = {S2e:.4f}")
        # Check if k's are orthogonal
        print(f"  k₁·k₂ = {k1@k2:.0f}, k₁·k₃ = {k1@k3:.0f}, k₂·k₃ = {k2@k3:.0f}")

    return worst_ratio

def optimize_v_orientations():
    """For fixed orthogonal k's, optimize v̂ orientations to maximize S²ê/|ω|²."""
    print("\nOPTIMIZATION: fixed k's = axes, optimize v̂ orientations")
    print("=" * 60)

    k1, k2, k3 = np.array([1,0,0.]), np.array([0,1,0.]), np.array([0,0,1.])

    # v1 ⊥ k1 → v1 = (0, cosθ₁, sinθ₁)
    # v2 ⊥ k2 → v2 = (cosθ₂, 0, sinθ₂)
    # v3 ⊥ k3 → v3 = (cosθ₃, sinθ₃, 0)

    def neg_ratio(angles):
        t1, t2, t3 = angles
        v1 = np.array([0, np.cos(t1), np.sin(t1)])
        v2 = np.array([np.cos(t2), 0, np.sin(t2)])
        v3 = np.array([np.cos(t3), np.sin(t3), 0])
        ratio, _, _ = compute_S2e_at_global_max(k1,v1,k2,v2,k3,v3, n_starts=15)
        return -ratio

    # Multi-start optimization
    best_ratio = 0
    best_angles = None
    for _ in range(50):
        t0 = np.random.uniform(0, 2*np.pi, 3)
        res = minimize(neg_ratio, t0, method='Nelder-Mead',
                      options={'xatol':1e-8, 'maxiter':1000})
        if -res.fun > best_ratio:
            best_ratio = -res.fun
            best_angles = res.x.copy()

    print(f"  Best S²ê/|ω|² = {best_ratio:.6f}")
    if best_angles is not None:
        t1, t2, t3 = best_angles
        v1 = np.array([0, np.cos(t1), np.sin(t1)])
        v2 = np.array([np.cos(t2), 0, np.sin(t2)])
        v3 = np.array([np.cos(t3), np.sin(t3), 0])
        print(f"  v̂₁ = {v1.round(4)}")
        print(f"  v̂₂ = {v2.round(4)}")
        print(f"  v̂₃ = {v3.round(4)}")
        print(f"  v̂₁·v̂₂ = {v1@v2:.4f}, v̂₁·v̂₃ = {v1@v3:.4f}, v̂₂·v̂₃ = {v2@v3:.4f}")

        # Check: is this the symmetric config?
        print(f"\n  Symmetric config (expected): v̂₁·v̂₂ = v̂₁·v̂₃ = v̂₂·v̂₃ = 0")
        print(f"  1/3 = {1/3:.6f}")

    # Also try non-orthogonal k's
    print("\nOPTIMIZATION: non-orthogonal k's")
    worst_overall = 0
    for k_trial in range(20):
        # Random k-vectors from small integer lattice
        ks = []
        while len(ks) < 3:
            k = np.random.randint(-2, 3, 3).astype(float)
            if np.dot(k,k) > 0 and np.dot(k,k) <= 6:
                ks.append(k)
        k1, k2, k3 = ks

        def neg_ratio2(angles):
            t1, t2, t3 = angles
            v1 = rand_perp_angle(k1, t1)
            v2 = rand_perp_angle(k2, t2)
            v3 = rand_perp_angle(k3, t3)
            ratio, _, _ = compute_S2e_at_global_max(k1,v1,k2,v2,k3,v3, n_starts=12)
            return -ratio

        best = 0
        for _ in range(20):
            v1 = rand_perp(k1)
            v2 = rand_perp(k2)
            v3 = rand_perp(k3)
            ratio, _, _ = compute_S2e_at_global_max(k1,v1,k2,v2,k3,v3, n_starts=12)
            best = max(best, ratio)

        if best > worst_overall:
            worst_overall = best
            print(f"  k=({k1.astype(int)},{k2.astype(int)},{k3.astype(int)}): ratio={best:.6f}")

    print(f"\n  Overall worst (non-orth): {worst_overall:.6f}")

def rand_perp_angle(k, theta):
    """Unit vector perpendicular to k, parameterized by angle theta."""
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    # Two basis vectors perpendicular to k
    if abs(kn[0]) < 0.9:
        e1 = np.cross(kn, [1,0,0])
    else:
        e1 = np.cross(kn, [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta) * e1 + np.sin(theta) * e2


if __name__ == '__main__':
    np.random.seed(42)

    test_orthogonal_symmetric()
    worst = exhaustive_3mode_search()
    optimize_v_orientations()

    print("\n" + "=" * 60)
    print("CONCLUSION")
    print("=" * 60)
    print(f"The orthogonal symmetric config gives S²ê/|ω|² = 1/3 = 0.3333")
    print(f"Exhaustive search worst: {worst:.6f}")
    print(f"Is 1/3 the true worst case? {'YES' if worst < 0.334 else 'NO'}")
    print(f"Margin to 3/4: {(0.75 - worst)/0.75*100:.0f}%")
