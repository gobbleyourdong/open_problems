"""
DIRECT per-mode analysis of S²ê at the vorticity max.

Key structural facts:
1. For aligned modes (v_k ∥ ê): contribution to α = ê·S·ê is ZERO
2. For aligned modes: contribution to S·ê is in the k×ê direction only
3. At x*: perpendicular components cancel (Σ b_k cos_k = 0)
4. The div-free condition couples a_k and b_k for modes with k·ê ≠ 0

Goal: decompose S²ê into per-mode contributions and bound the sum.
"""
import numpy as np

def analyze_Se_decomposition(ks, vs, x_star, verbose=False):
    """Decompose S·ê into per-mode contributions at x*."""
    N = len(ks)

    # Compute ω and ê at x*
    omega = sum(v * np.cos(k @ x_star) for k, v in zip(ks, vs))
    om2 = omega @ omega
    if om2 < 1e-10:
        return None

    e_hat = omega / np.sqrt(om2)

    # Compute S·ê directly
    S = np.zeros((3, 3))
    for k, v in zip(ks, vs):
        w = np.cross(k, v)
        k2 = k @ k
        phase = np.cos(k @ x_star)
        S -= phase * (np.outer(w, k) + np.outer(k, w)) / (2 * k2)
    Se = S @ e_hat
    S2e = Se @ Se

    # Per-mode decomposition of S·ê
    Se_modes = []
    alpha_modes = []  # ê-component (stretching)
    sigma_modes = []  # perpendicular component

    for k, v in zip(ks, vs):
        w = np.cross(k, v)
        k2 = k @ k
        phase = np.cos(k @ x_star)

        # Ŝ_k·ê = -(w·ê k + (k·ê) w) / (2|k|²) × phase
        w_dot_e = w @ e_hat
        k_dot_e = k @ e_hat
        Se_k = -(w_dot_e * k + k_dot_e * w) / (2 * k2) * phase

        # Decompose: α_k = (Se_k · ê), σ_k = Se_k - α_k ê
        alpha_k = Se_k @ e_hat
        sigma_k = Se_k - alpha_k * e_hat

        # Also decompose v_k: a_k = v_k·ê, b_k = v_k - a_k ê
        a_k = (v @ e_hat) * phase
        b_k_vec = v * phase - a_k * e_hat

        Se_modes.append(Se_k)
        alpha_modes.append(alpha_k)
        sigma_modes.append(sigma_k)

    # Total stretching
    alpha_total = sum(alpha_modes)
    sigma_total = sum(sigma_modes)

    # Check: S²ê = α² + |σ|²
    S2e_check = alpha_total**2 + np.linalg.norm(sigma_total)**2

    if verbose:
        print(f"  |ω|² = {om2:.6f}")
        print(f"  S²ê = {S2e:.6f}")
        print(f"  S²ê/|ω|² = {S2e/om2:.6f}")
        print(f"  α = {alpha_total:.6f}")
        print(f"  |σ| = {np.linalg.norm(sigma_total):.6f}")
        print(f"  α²/|ω|² = {alpha_total**2/om2:.6f}")
        print(f"  |σ|²/|ω|² = {np.linalg.norm(sigma_total)**2/om2:.6f}")

    return {
        'om2': om2,
        'S2e': S2e,
        'ratio': S2e / om2,
        'alpha': alpha_total,
        'sigma_norm': np.linalg.norm(sigma_total),
        'alpha2_ratio': alpha_total**2 / om2,
        'sigma2_ratio': np.linalg.norm(sigma_total)**2 / om2,
        'alpha_modes': alpha_modes,
        'sigma_modes': [np.linalg.norm(s) for s in sigma_modes],
        'N': N
    }

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("S²ê DECOMPOSITION: α² + |σ|² at the vorticity max")
    print("α = stretching (ê·S·ê), σ = perpendicular strain (S·ê)_⊥")
    print("=" * 70)

    results_by_N = {}

    for N in [2, 3, 4, 5, 8, 12, 20]:
        K_max = 2 if N <= 12 else 3
        n_per = 200

        ratios, alpha2_ratios, sigma2_ratios = [], [], []

        for trial in range(n_per):
            all_modes = []
            for i in range(-K_max, K_max+1):
                for j in range(-K_max, K_max+1):
                    for l in range(-K_max, K_max+1):
                        k = np.array([i, j, l], float)
                        if 0 < k @ k <= K_max**2:
                            all_modes.append(k)

            if N > len(all_modes):
                continue
            idx = np.random.choice(len(all_modes), N, replace=False)
            ks = [all_modes[i] for i in idx]
            vs = []
            for k in ks:
                v = np.random.randn(3)
                v -= k * (v @ k) / (k @ k)
                vs.append(v)

            # Find max |ω|
            best_x = np.zeros(3)
            best_om2 = 0
            M = 20
            xs_grid = np.linspace(0, 2*np.pi, M, endpoint=False)
            for i in range(M):
                for j in range(M):
                    for l in range(M):
                        x = np.array([xs_grid[i], xs_grid[j], xs_grid[l]])
                        om = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
                        om2 = om @ om
                        if om2 > best_om2:
                            best_om2 = om2
                            best_x = x.copy()

            # Refine
            for _ in range(5):
                h = 1e-4
                grad = np.zeros(3)
                omega0 = sum(v * np.cos(k @ best_x) for k, v in zip(ks, vs))
                f0 = omega0 @ omega0
                for d in range(3):
                    xp = best_x.copy(); xp[d] += h
                    om_p = sum(v * np.cos(k @ xp) for k, v in zip(ks, vs))
                    grad[d] = (om_p @ om_p - f0) / h
                for step in [0.1, 0.01, 0.001]:
                    xt = best_x + step * grad / (np.linalg.norm(grad) + 1e-12)
                    om_t = sum(v * np.cos(k @ xt) for k, v in zip(ks, vs))
                    if om_t @ om_t > best_om2:
                        best_om2 = om_t @ om_t
                        best_x = xt

            result = analyze_Se_decomposition(ks, vs, best_x)
            if result is None:
                continue

            ratios.append(result['ratio'])
            alpha2_ratios.append(result['alpha2_ratio'])
            sigma2_ratios.append(result['sigma2_ratio'])

        if ratios:
            print(f"N={N:2d}: S²ê/|ω|² max={max(ratios):.6f} mean={np.mean(ratios):.6f}  |  "
                  f"α²/|ω|² max={max(alpha2_ratios):.6f}  |  "
                  f"|σ|²/|ω|² max={max(sigma2_ratios):.6f}")
            results_by_N[N] = {
                'S2e_max': max(ratios),
                'alpha2_max': max(alpha2_ratios),
                'sigma2_max': max(sigma2_ratios)
            }

    print()
    print("KEY BOUNDS:")
    print(f"  Need S²ê < 3|ω|²/4 = 0.750")
    print(f"  S²ê = α² + |σ|²")
    print(f"  α² is bounded by what?")
    print(f"  |σ|² is bounded by what?")

    # The stretching α comes from perpendicular ω through BS
    # The sigma comes from both aligned and perpendicular ω
    # Can we bound them separately?

    print()
    print("=" * 70)
    print("ADVERSARIAL S²ê SEARCH (DE optimization)")
    print("=" * 70)

    from scipy.optimize import differential_evolution

    def build_perp_basis(k):
        kn = k / np.linalg.norm(k)
        ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
        e1 = np.cross(kn, ref)
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(kn, e1)
        return e1, e2

    # Build K=√2 shell
    raw = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for l in range(-1, 2):
                k = np.array([i, j, l], float)
                if 0 < k@k <= 2:
                    raw.append(k)
    unique = []
    for k in raw:
        if not any(np.allclose(k, -u) for u in unique):
            unique.append(k)

    def neg_S2e(thetas, ks):
        N = len(ks)
        bases = [build_perp_basis(k) for k in ks]
        vs = [np.cos(thetas[i])*bases[i][0] + np.sin(thetas[i])*bases[i][1] for i in range(N)]

        best_ratio = 0
        for signs in [(1.,)*N]:  # Just try all +1 first (speeds up, max is often here)
            omega = sum(s*v for s, v in zip(signs, vs))
            om2 = omega @ omega
            if om2 < 1e-15:
                continue
            e_hat = omega / np.sqrt(om2)
            S = np.zeros((3,3))
            for k, v, s in zip(ks, vs, signs):
                w = np.cross(k, s*v)
                S += 0.5*s*(np.outer(w, k) + np.outer(k, w))/(k@k)
            # Wait, sign is wrong. Let me use the correct formula.
            S = np.zeros((3,3))
            for k, v, s in zip(ks, vs, signs):
                sv = s * v
                w = np.cross(k, sv)
                S -= (np.outer(w, k) + np.outer(k, w)) / (2*(k@k))
            Se = S @ e_hat
            ratio = (Se @ Se) / om2
            best_ratio = max(best_ratio, ratio)

        # Also check all 2^N sign patterns for the max
        from itertools import product as iprod
        best_om2 = 0
        best_data = None
        for signs in iprod([1.0, -1.0], repeat=N):
            omega = sum(s*v for s, v in zip(signs, vs))
            om2 = omega @ omega
            if om2 > best_om2:
                best_om2 = om2
                best_data = (signs, omega, om2)

        if best_data:
            signs, omega, om2 = best_data
            e_hat = omega / np.sqrt(om2)
            S = np.zeros((3,3))
            for k, v, s in zip(ks, vs, signs):
                sv = s * v
                w = np.cross(k, sv)
                S -= (np.outer(w, k) + np.outer(k, w)) / (2*(k@k))
            Se = S @ e_hat
            ratio = (Se @ Se) / om2
            best_ratio = max(best_ratio, ratio)

        return -best_ratio

    from itertools import combinations

    # Test N=2,3,4 exhaustively on K=√2 shell
    overall_worst = 0
    for N in [2, 3, 4, 5]:
        subs = list(combinations(range(len(unique)), N))
        if N >= 5:
            np.random.shuffle(subs)
            subs = subs[:30]

        worst = 0
        worst_config = None
        for sub in subs:
            ks = [unique[i] for i in sub]
            bounds = [(0, 2*np.pi)] * N
            result = differential_evolution(lambda t: neg_S2e(t, ks), bounds,
                                          maxiter=100, popsize=10, seed=42, tol=1e-8)
            ratio = -result.fun
            if ratio > worst:
                worst = ratio
                worst_config = sub

        print(f"N={N}: {len(subs)} configs, worst S²ê/|ω|² = {worst:.6f}")
        overall_worst = max(overall_worst, worst)

    print(f"\nOverall worst S²ê/|ω|²: {overall_worst:.6f} (< 0.75? {overall_worst < 0.75})")
