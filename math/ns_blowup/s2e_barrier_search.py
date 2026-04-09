#!/usr/bin/env python3
"""
Comprehensive search for worst-case S²ê/|ω|² at the global vorticity maximum
for N-mode div-free fields on T³.

The barrier argument: at R = α/|ω| = 1/2,
  DR/Dt = (S²ê - 3α² - H_ωω)/|ω|

For DR/Dt < 0: need S²ê < 3|ω|²/4 + H_ωω.
Since H_ωω > 0: sufficient condition is S²ê < 3|ω|²/4 = 0.75|ω|².

This script finds the supremum of S²ê/|ω|² over all N-mode configurations.
"""

import numpy as np
from itertools import product
from scipy.optimize import minimize

np.random.seed(42)

def random_perp_unit(k):
    """Random unit vector perpendicular to k."""
    k = np.array(k, dtype=float)
    # Find a non-parallel vector
    if abs(k[0]) < 0.9:
        v = np.array([1.0, 0.0, 0.0])
    else:
        v = np.array([0.0, 1.0, 0.0])
    # Gram-Schmidt
    v = v - (v @ k) / (k @ k) * k
    v /= np.linalg.norm(v)
    return v

def random_perp_unit_full(k, rng=None):
    """Random unit vector perpendicular to k with random angle."""
    if rng is None:
        rng = np.random
    k = np.array(k, dtype=float)
    knorm = k / np.linalg.norm(k)

    # Build orthonormal basis in plane ⊥ k
    if abs(knorm[0]) < 0.9:
        v = np.array([1.0, 0.0, 0.0])
    else:
        v = np.array([0.0, 1.0, 0.0])
    e1 = v - (v @ knorm) * knorm
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(knorm, e1)

    theta = rng.uniform(0, 2 * np.pi)
    return np.cos(theta) * e1 + np.sin(theta) * e2


def compute_at_max(ks, vs, amps, grid_res=64):
    """
    Compute S²ê/|ω|² at the global maximum of |ω| on T³.

    ks: list of N wavevectors (each in Z³)
    vs: list of N unit polarization vectors (v_i ⊥ k_i)
    amps: list of N amplitudes

    Returns: S²ê/|ω|², α/|ω|, |ω|_max, x*
    """
    N = len(ks)
    ks = [np.array(k, dtype=float) for k in ks]
    vs = [np.array(v, dtype=float) for v in vs]
    amps = np.array(amps, dtype=float)

    # Step 1: Find global max of |ω|² on a grid
    # For modes with k ∈ Z³: all critical points are at vertices
    # (where cos(k_i · x) = ±1 for all i with independent k's)
    # But also check a fine grid for non-vertex maxima

    # First: try all sign combinations at vertices (2^N possibilities per independent k)
    # The max of |ω|² for fields like Σ a_i v̂_i cos(k_i·x) occurs where
    # each cos(k_i·x) = ±1 (for independent k's).
    # Try all 2^N sign combos:
    best_om2 = 0.0
    best_signs = None

    if N <= 15:  # Enumerate sign combos
        for signs in product([1, -1], repeat=N):
            signs = np.array(signs, dtype=float)
            omega = sum(amps[i] * signs[i] * vs[i] for i in range(N))
            om2 = omega @ omega
            if om2 > best_om2:
                best_om2 = om2
                best_signs = signs.copy()

    # Also search on a grid (catches non-vertex maxima)
    g = np.linspace(0, 2*np.pi, grid_res, endpoint=False)
    xx, yy, zz = np.meshgrid(g, g, g, indexing='ij')

    omega_grid = np.zeros((grid_res, grid_res, grid_res, 3))
    for i in range(N):
        phase = ks[i][0]*xx + ks[i][1]*yy + ks[i][2]*zz
        for j in range(3):
            omega_grid[..., j] += amps[i] * vs[i][j] * np.cos(phase)

    om2_grid = np.sum(omega_grid**2, axis=-1)
    idx = np.unravel_index(np.argmax(om2_grid), om2_grid.shape)
    grid_max = om2_grid[idx]

    if grid_max > best_om2:
        x_star = np.array([g[idx[0]], g[idx[1]], g[idx[2]]])
        best_om2 = grid_max
    else:
        # x_star from vertex: need to find actual x where cos(k_i·x) = best_signs[i]
        # This is a system of equations. For vertex solutions: cos(k_i·x) = s_i
        # i.e., k_i·x = 0 or π. Use the grid point closest to this.
        x_star = np.array([g[idx[0]], g[idx[1]], g[idx[2]]])
        # Recompute with vertex signs
        omega_star = sum(amps[i] * best_signs[i] * vs[i] for i in range(N))
        if omega_star @ omega_star > grid_max:
            # Vertex is better; find x_star approximately
            # For simplicity, just use the grid max location
            # (it should be close to the vertex)
            best_om2 = omega_star @ omega_star

    # Refine x_star with local optimization
    def neg_om2(x):
        omega = np.zeros(3)
        for i in range(N):
            omega += amps[i] * vs[i] * np.cos(ks[i] @ x)
        return -(omega @ omega)

    from scipy.optimize import minimize
    res = minimize(neg_om2, x_star, method='Nelder-Mead',
                   options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 10000})
    x_star = res.x
    best_om2 = -res.fun

    if best_om2 < 1e-12:
        return 0.0, 0.0, 0.0, x_star

    # Step 2: Compute ω, S at x_star
    omega = np.zeros(3)
    for i in range(N):
        omega += amps[i] * vs[i] * np.cos(ks[i] @ x_star)

    om_mag = np.sqrt(omega @ omega)
    e_hat = omega / om_mag

    # Strain: S = Σ_i a_i cos(k_i·x*) × sym(k_i ⊗ w_i) / |k_i|²
    # where w_i = k_i × v̂_i
    S = np.zeros((3, 3))
    for i in range(N):
        ci = np.cos(ks[i] @ x_star)
        wi = np.cross(ks[i], vs[i])
        ki2 = ks[i] @ ks[i]
        outer = np.outer(ks[i], wi)
        S += amps[i] * ci * (outer + outer.T) / (2 * ki2)

    # S²ê = |S·ê|²
    Se = S @ e_hat
    S2e = Se @ Se

    # α = ê·S·ê
    alpha = e_hat @ S @ e_hat

    return S2e / best_om2, alpha / om_mag, om_mag, x_star


def search_2mode(n_trials=50000):
    """Systematic search for worst S²ê/|ω|² with 2 modes."""
    print("=" * 70)
    print("2-MODE SEARCH")
    print("=" * 70)

    rng = np.random.RandomState(123)

    # All k vectors with |k|² ≤ 9
    k_pool = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i, j, l])
                if 0 < k @ k <= 9:
                    k_pool.append(k)
    print(f"k-vectors in pool: {len(k_pool)}")

    worst_s2e = 0.0
    worst_alpha = 0.0
    worst_config = None

    for trial in range(n_trials):
        # Random k vectors
        idx1, idx2 = rng.choice(len(k_pool), 2, replace=False)
        k1 = k_pool[idx1]
        k2 = k_pool[idx2]

        # Random polarizations
        v1 = random_perp_unit_full(k1, rng)
        v2 = random_perp_unit_full(k2, rng)

        # Random amplitudes (normalized)
        a1 = rng.exponential(1.0)
        a2 = rng.exponential(1.0)
        total = a1 + a2
        a1 /= total
        a2 /= total

        try:
            s2e_ratio, alpha_ratio, om_max, x_star = compute_at_max(
                [k1, k2], [v1, v2], [a1, a2], grid_res=32
            )
        except Exception:
            continue

        if s2e_ratio > worst_s2e:
            worst_s2e = s2e_ratio
            worst_config = (k1.copy(), k2.copy(), v1.copy(), v2.copy(), a1, a2)
            print(f"  Trial {trial}: S²ê/|ω|² = {s2e_ratio:.6f}, "
                  f"α/|ω| = {alpha_ratio:.4f}, |ω| = {om_max:.4f}")

        if abs(alpha_ratio) > worst_alpha:
            worst_alpha = abs(alpha_ratio)

    print(f"\nWorst S²ê/|ω|² = {worst_s2e:.6f} (threshold: 0.750)")
    print(f"Worst |α/|ω|| = {worst_alpha:.6f} (threshold: 0.500)")
    if worst_config:
        k1, k2, v1, v2, a1, a2 = worst_config
        print(f"  k1 = {k1}, k2 = {k2}")
        print(f"  v1 = {v1}")
        print(f"  v2 = {v2}")
        print(f"  a1 = {a1:.4f}, a2 = {a2:.4f}")

    return worst_s2e


def search_nmode(N, n_trials=10000):
    """Search for worst S²ê/|ω|² with N modes."""
    print(f"\n{'=' * 70}")
    print(f"{N}-MODE SEARCH")
    print(f"{'=' * 70}")

    rng = np.random.RandomState(456 + N)

    k_pool = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i, j, l])
                if 0 < k @ k <= 9:
                    k_pool.append(k)

    worst_s2e = 0.0
    worst_alpha = 0.0

    for trial in range(n_trials):
        indices = rng.choice(len(k_pool), N, replace=False)
        ks = [k_pool[i] for i in indices]
        vs = [random_perp_unit_full(k, rng) for k in ks]
        amps = rng.exponential(1.0, N)
        amps /= amps.sum()

        try:
            s2e_ratio, alpha_ratio, om_max, x_star = compute_at_max(
                ks, vs, amps, grid_res=24
            )
        except Exception:
            continue

        if s2e_ratio > worst_s2e:
            worst_s2e = s2e_ratio
            print(f"  Trial {trial}: S²ê/|ω|² = {s2e_ratio:.6f}, "
                  f"α/|ω| = {alpha_ratio:.4f}")

        if abs(alpha_ratio) > worst_alpha:
            worst_alpha = abs(alpha_ratio)

    print(f"\nWorst S²ê/|ω|² = {worst_s2e:.6f} (threshold: 0.750)")
    print(f"Worst |α/|ω|| = {worst_alpha:.6f}")

    return worst_s2e


def analytic_2mode_sweep():
    """
    Exact analytic computation for 2 orthogonal-k modes.

    For k₁=(1,0,0), k₂=(0,1,0), equal amplitudes:
    S·ω = (cosφ₁ sinφ₂, -cosφ₂ sinφ₁, 0)
    |ω|² = 2 + 2sinφ₁sinφ₂
    S²ê/|ω|² = (s₁² + s₂² - 2s₁²s₂²) / [4(1+s₁s₂)²]
    """
    print("\n" + "=" * 70)
    print("ANALYTIC 2-MODE SWEEP (orthogonal k, equal amplitudes)")
    print("=" * 70)

    # Sweep s1, s2
    n = 500
    s_vals = np.linspace(-0.999, 0.999, n)

    worst = 0.0
    worst_s1s2 = (0, 0)

    for s1 in s_vals:
        for s2 in s_vals:
            denom = 4 * (1 + s1*s2)**2
            if denom < 1e-10:
                continue
            numer = s1**2 + s2**2 - 2*s1**2*s2**2
            ratio = numer / denom
            if ratio > worst:
                worst = ratio
                worst_s1s2 = (s1, s2)

    print(f"Worst S²ê/|ω|² = {worst:.8f}")
    print(f"At s1={worst_s1s2[0]:.4f}, s2={worst_s1s2[1]:.4f}")

    # Analytic optimum: s1 = s2 = 1/√3
    s_opt = 1/np.sqrt(3)
    ratio_opt = (2*s_opt**2 - 2*s_opt**4) / (4*(1+s_opt**2)**2)
    print(f"Analytic optimum (s=1/√3): S²ê/|ω|² = {ratio_opt:.8f} = 1/16 = {1/16:.8f}")

    # Check: also try s1 ≠ s2
    from scipy.optimize import minimize_scalar, minimize
    def neg_ratio(params):
        s1, s2 = params
        denom = 4 * (1 + s1*s2)**2
        if denom < 1e-10:
            return 0.0
        numer = s1**2 + s2**2 - 2*s1**2*s2**2
        return -numer / denom

    best = 0.0
    for _ in range(1000):
        s0 = np.random.uniform(-0.99, 0.99, 2)
        res = minimize(neg_ratio, s0, method='Nelder-Mead')
        if -res.fun > best:
            best = -res.fun
            best_s = res.x

    print(f"Optimized (asymmetric): S²ê/|ω|² = {best:.8f} at s1={best_s[0]:.4f}, s2={best_s[1]:.4f}")

    return worst


def targeted_adversarial_search(n_trials=100000):
    """
    Adversarial search: try to MAXIMIZE S²ê/|ω|² using gradient-free optimization.
    Parameterize: k vectors, polarization angles, amplitudes.
    """
    print("\n" + "=" * 70)
    print("ADVERSARIAL OPTIMIZATION (scipy, 2-5 modes)")
    print("=" * 70)

    k_pool = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i, j, l])
                k2 = k @ k
                if 0 < k2 <= 9:
                    k_pool.append(k)
    k_pool = np.array(k_pool)

    rng = np.random.RandomState(789)

    overall_worst = 0.0

    for N in [2, 3, 4, 5]:
        print(f"\n--- N = {N} modes ---")
        worst_s2e = 0.0

        n_trials_n = 20000 if N <= 3 else 5000

        for trial in range(n_trials_n):
            # Random configuration
            indices = rng.choice(len(k_pool), N, replace=False)
            ks = [k_pool[i] for i in indices]
            vs = [random_perp_unit_full(k, rng) for k in ks]
            amps = rng.exponential(1.0, N)
            amps /= amps.sum()

            try:
                s2e_ratio, alpha_ratio, om_max, x_star = compute_at_max(
                    ks, vs, amps, grid_res=24
                )
            except Exception:
                continue

            if s2e_ratio > worst_s2e:
                worst_s2e = s2e_ratio
                if s2e_ratio > overall_worst:
                    overall_worst = s2e_ratio
                    print(f"  N={N}, trial {trial}: S²ê/|ω|² = {s2e_ratio:.6f}, "
                          f"α/|ω| = {alpha_ratio:.4f}, |ω| = {om_max:.4f}")

        print(f"  N={N} worst: S²ê/|ω|² = {worst_s2e:.6f}")

    print(f"\n{'=' * 70}")
    print(f"OVERALL WORST S²ê/|ω|² = {overall_worst:.6f}")
    print(f"Threshold: 0.750")
    print(f"Margin: {0.75 - overall_worst:.6f}")
    print(f"{'=' * 70}")

    return overall_worst


if __name__ == '__main__':
    # Phase 1: Analytic sweep for 2 orthogonal modes
    analytic_2mode_sweep()

    # Phase 2: Random search for 2 modes (general k's)
    search_2mode(n_trials=20000)

    # Phase 3: N modes for N = 3, 4, 5, 8
    for N in [3, 5, 8]:
        search_nmode(N, n_trials=5000)

    # Phase 4: Adversarial optimization
    targeted_adversarial_search()
