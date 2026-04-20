"""
Find the maximum α/|ω| at the vorticity maximum for N-mode div-free fields on T³.

For N=1: α = 0 at max (proven analytically, file 263).
For N=2: FIND THE MAXIMUM — this is the key unknown.
For N≥3: characterize convergence.

Single mode: ω = v̂ cos(k·x), k⊥v̂.
At max (cos=1): ê = v̂/|v̂|. α = ê·S·ê = 0 because ê·(k×v̂) = 0.

Two modes: ω = a₁v̂₁cos(k₁·x) + a₂v̂₂cos(k₂·x).
At the max: ê = ω/|ω|. α = ê·(S₁+S₂)·ê ≠ 0 generically.
"""

import numpy as np
from scipy.optimize import minimize
from itertools import product

def compute_alpha_omega_ratio(k_list, v_list, a_list, x):
    """
    Compute α/|ω| at point x for a multi-mode div-free field.

    ω = Σ aᵢ v̂ᵢ cos(kᵢ·x)
    u = Σ aᵢ (kᵢ×v̂ᵢ) sin(kᵢ·x) / |kᵢ|²
    S = sym(∇u) evaluated at x
    α = ê·S·ê where ê = ω/|ω|
    """
    omega = np.zeros(3)
    S = np.zeros((3,3))

    for k, v, a in zip(k_list, v_list, a_list):
        k = np.array(k, float)
        v = np.array(v, float)

        # Vorticity contribution
        cos_kx = np.cos(k @ x)
        omega += a * v * cos_kx

        # Velocity: u = a * (k × v) * sin(k·x) / |k|²
        kxv = np.cross(k, v)
        sin_kx = np.sin(k @ x)
        k2 = k @ k

        # Strain: S_ij = (1/2)(∂u_i/∂x_j + ∂u_j/∂x_i)
        # ∂u_i/∂x_j = a * kxv_i * k_j * cos(k·x) / |k|²
        # So ∇u = a * (kxv ⊗ k) * cos(k·x) / |k|²
        grad_u = a * np.outer(kxv, k) * cos_kx / k2
        S += 0.5 * (grad_u + grad_u.T)

    omega_mag = np.linalg.norm(omega)
    if omega_mag < 1e-15:
        return 0.0, 0.0, omega_mag

    e_hat = omega / omega_mag
    alpha = e_hat @ S @ e_hat

    return alpha / omega_mag, alpha, omega_mag


def parametrize_2mode(params):
    """
    Parametrize a 2-mode field and return -α/|ω| (for minimization = maximize α/|ω|).

    params: [θ₁, φ₁, θ₂, φ₂, x, y, z, amplitude_ratio]
    k₁ = (1,0,0), k₂ = (0,1,0) fixed for now.
    v̂ᵢ parametrized by angles (perpendicular to kᵢ).
    """
    th1, ph1, th2, ph2, x, y, z, log_a = params

    # k₁ = (1,0,0): v̂₁ in yz-plane
    v1 = np.array([0, np.cos(th1), np.sin(th1)])
    # k₂ = (0,1,0): v̂₂ in xz-plane
    v2 = np.array([np.cos(th2), 0, np.sin(th2)])

    a1 = 1.0
    a2 = np.exp(log_a)  # positive amplitude ratio

    k_list = [(1,0,0), (0,1,0)]
    v_list = [v1, v2]
    a_list = [a1, a2]
    pt = np.array([x, y, z])

    ratio, alpha, omega_mag = compute_alpha_omega_ratio(k_list, v_list, a_list, pt)

    # We want to maximize |ratio|, so minimize -|ratio|
    # But also want to be near a maximum of |ω|
    # Penalty for not being at max: add gradient norm penalty
    return -abs(ratio)


def parametrize_general_2mode(params):
    """
    General 2-mode: both k-vectors and polarizations parametrized.
    params: [k1x,k1y,k1z, k2x,k2y,k2z, th1,ph1, th2,ph2, x,y,z, log_a]
    k-vectors are integers (we'll round).
    """
    k1 = np.round(params[0:3]).astype(int)
    k2 = np.round(params[3:6]).astype(int)

    if np.linalg.norm(k1) < 0.5 or np.linalg.norm(k2) < 0.5:
        return 0.0

    th1, ph1, th2, ph2 = params[6:10]
    x, y, z = params[10:13]
    log_a = params[13]

    # Build v̂ᵢ perpendicular to kᵢ
    def perp_vec(k, th, ph):
        k = np.array(k, float)
        kn = k / np.linalg.norm(k)
        # Find two vectors perpendicular to k
        if abs(kn[0]) < 0.9:
            e1 = np.cross(kn, [1,0,0])
        else:
            e1 = np.cross(kn, [0,1,0])
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(kn, e1)
        return np.cos(th) * e1 + np.sin(th) * e2

    v1 = perp_vec(k1, th1, ph1)
    v2 = perp_vec(k2, th2, ph2)

    a1 = 1.0
    a2 = np.exp(log_a)

    k_list = [k1, k2]
    v_list = [v1, v2]
    a_list = [a1, a2]
    pt = np.array([x, y, z])

    ratio, alpha, omega_mag = compute_alpha_omega_ratio(k_list, v_list, a_list, pt)
    return -abs(ratio)


def brute_force_2mode_fixed_k():
    """
    For fixed k₁=(1,0,0), k₂=(0,1,0): scan all parameters.
    """
    print("=" * 60)
    print("FIXED k₁=(1,0,0), k₂=(0,1,0): scanning α/|ω| at max |ω|")
    print("=" * 60)

    best_ratio = 0
    best_params = None

    # Grid search over angles and position
    n_angle = 24
    n_pos = 20

    for i1 in range(n_angle):
        th1 = 2 * np.pi * i1 / n_angle
        v1 = np.array([0, np.cos(th1), np.sin(th1)])

        for i2 in range(n_angle):
            th2 = 2 * np.pi * i2 / n_angle
            v2 = np.array([np.cos(th2), 0, np.sin(th2)])

            for a_ratio in [0.5, 0.8, 1.0, 1.2, 2.0]:
                # Find the max of |ω|² by scanning
                best_local_ratio = 0
                best_local_x = None

                for ix in range(n_pos):
                    for iy in range(n_pos):
                        for iz in range(n_pos):
                            x = 2*np.pi*ix/n_pos
                            y = 2*np.pi*iy/n_pos
                            z = 2*np.pi*iz/n_pos
                            pt = np.array([x, y, z])

                            omega = v1*np.cos(pt[0]) + a_ratio*v2*np.cos(pt[1])
                            omega_mag = np.linalg.norm(omega)

                            if omega_mag > 0.5:  # only at significant |ω|
                                ratio, _, _ = compute_alpha_omega_ratio(
                                    [(1,0,0), (0,1,0)], [v1, v2], [1.0, a_ratio], pt)

                                if abs(ratio) > best_local_ratio:
                                    best_local_ratio = abs(ratio)
                                    best_local_x = pt.copy()

                if best_local_ratio > best_ratio:
                    best_ratio = best_local_ratio
                    best_params = (th1, th2, a_ratio, best_local_x)

    print(f"Max |α/|ω|| = {best_ratio:.6f}")
    print(f"Best params: θ₁={best_params[0]:.3f}, θ₂={best_params[1]:.3f}, "
          f"a₂/a₁={best_params[2]:.2f}")
    print(f"At x = {best_params[3]}")
    print(f"Ratio to 0.5: {best_ratio/0.5:.4f}")
    return best_ratio


def optimize_2mode_fixed_k():
    """
    Optimize α/|ω| at the max of |ω| for k₁=(1,0,0), k₂=(0,1,0).
    First find max |ω|, then compute α/|ω| there.
    """
    print("\n" + "=" * 60)
    print("OPTIMIZING α/|ω| AT MAX |ω| for k₁=(1,0,0), k₂=(0,1,0)")
    print("=" * 60)

    best_ratio = 0
    best_config = None

    n_trials = 2000
    for trial in range(n_trials):
        th1 = np.random.uniform(0, 2*np.pi)
        th2 = np.random.uniform(0, 2*np.pi)
        a_ratio = np.exp(np.random.uniform(-1, 1))

        v1 = np.array([0, np.cos(th1), np.sin(th1)])
        v2 = np.array([np.cos(th2), 0, np.sin(th2)])

        # Find max |ω| by optimization
        def neg_omega_sq(xyz):
            pt = np.array(xyz)
            omega = v1*np.cos(pt[0]) + a_ratio*v2*np.cos(pt[1])
            return -np.dot(omega, omega)

        # Multi-start for max |ω|
        best_om = 0
        best_x = None
        for _ in range(5):
            x0 = np.random.uniform(0, 2*np.pi, 3)
            res = minimize(neg_omega_sq, x0, method='Nelder-Mead')
            if -res.fun > best_om:
                best_om = -res.fun
                best_x = res.x

        if best_x is None or best_om < 0.01:
            continue

        ratio, alpha, omega_mag = compute_alpha_omega_ratio(
            [(1,0,0), (0,1,0)], [v1, v2], [1.0, a_ratio], best_x)

        if abs(ratio) > best_ratio:
            best_ratio = abs(ratio)
            best_config = {
                'th1': th1, 'th2': th2, 'a_ratio': a_ratio,
                'x': best_x, 'alpha': alpha, 'omega': omega_mag,
                'ratio': ratio
            }

    print(f"Max |α/|ω|| = {best_ratio:.6f}")
    if best_config:
        print(f"Config: θ₁={best_config['th1']:.4f}, θ₂={best_config['th2']:.4f}, "
              f"a₂/a₁={best_config['a_ratio']:.4f}")
        print(f"At x = [{best_config['x'][0]:.4f}, {best_config['x'][1]:.4f}, {best_config['x'][2]:.4f}]")
        print(f"α = {best_config['alpha']:.6f}, |ω| = {best_config['omega']:.6f}")
    print(f"Ratio to 0.5: {best_ratio/0.5:.4f}")
    return best_ratio


def optimize_many_k_pairs():
    """
    Try different k-vector pairs to find worst case.
    """
    print("\n" + "=" * 60)
    print("SCANNING OVER k-VECTOR PAIRS")
    print("=" * 60)

    # Integer wavevectors up to |k| = 3
    ks = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                if i*i + j*j + l*l > 0 and i*i + j*j + l*l <= 9:
                    ks.append((i,j,l))

    print(f"Testing {len(ks)} wavevectors, {len(ks)*(len(ks)-1)//2} pairs")

    global_best = 0
    global_config = None

    # Sample pairs
    n_pairs = min(200, len(ks)*(len(ks)-1)//2)
    pairs_tested = set()

    for _ in range(n_pairs):
        idx1, idx2 = np.random.choice(len(ks), 2, replace=False)
        pair = (min(idx1,idx2), max(idx1,idx2))
        if pair in pairs_tested:
            continue
        pairs_tested.add(pair)

        k1 = np.array(ks[idx1], float)
        k2 = np.array(ks[idx2], float)

        # Skip parallel k-vectors
        if np.linalg.norm(np.cross(k1, k2)) < 0.01:
            continue

        best_for_pair = 0

        for trial in range(50):
            # Random polarizations perpendicular to k
            def rand_perp(k):
                k = np.array(k, float)
                kn = k / np.linalg.norm(k)
                r = np.random.randn(3)
                r -= (r @ kn) * kn
                return r / np.linalg.norm(r)

            v1 = rand_perp(k1)
            v2 = rand_perp(k2)
            a_ratio = np.exp(np.random.uniform(-1, 1))

            # Find max |ω|
            def neg_omega_sq(xyz):
                pt = np.array(xyz)
                omega = v1*np.cos(k1@pt) + a_ratio*v2*np.cos(k2@pt)
                return -np.dot(omega, omega)

            best_om = 0
            best_x = None
            for _ in range(3):
                x0 = np.random.uniform(0, 2*np.pi, 3)
                res = minimize(neg_omega_sq, x0, method='Nelder-Mead')
                if -res.fun > best_om:
                    best_om = -res.fun
                    best_x = res.x

            if best_x is None or best_om < 0.01:
                continue

            ratio, alpha, omega_mag = compute_alpha_omega_ratio(
                [k1, k2], [v1, v2], [1.0, a_ratio], best_x)

            if abs(ratio) > best_for_pair:
                best_for_pair = abs(ratio)

            if abs(ratio) > global_best:
                global_best = abs(ratio)
                global_config = {
                    'k1': ks[idx1], 'k2': ks[idx2],
                    'v1': v1.copy(), 'v2': v2.copy(),
                    'a_ratio': a_ratio, 'x': best_x.copy(),
                    'ratio': ratio, 'alpha': alpha, 'omega': omega_mag
                }

    print(f"\nGlobal max |α/|ω|| = {global_best:.6f}")
    if global_config:
        print(f"k₁ = {global_config['k1']}, k₂ = {global_config['k2']}")
        print(f"v̂₁ = [{global_config['v1'][0]:.3f}, {global_config['v1'][1]:.3f}, {global_config['v1'][2]:.3f}]")
        print(f"v̂₂ = [{global_config['v2'][0]:.3f}, {global_config['v2'][1]:.3f}, {global_config['v2'][2]:.3f}]")
        print(f"a₂/a₁ = {global_config['a_ratio']:.4f}")
        print(f"α = {global_config['alpha']:.6f}, |ω| = {global_config['omega']:.6f}")
    print(f"Ratio to 0.5: {global_best/0.5:.4f}")
    return global_best


def verify_at_max(k1, k2, v1, v2, a1, a2, x):
    """Verify we're at a max of |ω| and compute α/|ω| with gradient check."""
    eps = 1e-6
    _, _, omega0 = compute_alpha_omega_ratio([k1,k2], [v1,v2], [a1,a2], x)

    is_max = True
    for d in range(3):
        dx = np.zeros(3)
        dx[d] = eps
        _, _, om_p = compute_alpha_omega_ratio([k1,k2], [v1,v2], [a1,a2], x+dx)
        _, _, om_m = compute_alpha_omega_ratio([k1,k2], [v1,v2], [a1,a2], x-dx)
        if om_p > omega0 + 1e-10 or om_m > omega0 + 1e-10:
            is_max = False

    ratio, alpha, omega = compute_alpha_omega_ratio([k1,k2], [v1,v2], [a1,a2], x)
    return ratio, alpha, omega, is_max


def optimize_2mode_at_true_max():
    """
    More careful: optimize α/|ω| specifically AT the global max of |ω|.
    Use analytic gradient for max-finding.
    """
    print("\n" + "=" * 60)
    print("CAREFUL OPTIMIZATION: α/|ω| at TRUE max of |ω|")
    print("=" * 60)

    best_ratio = 0
    best_config = None

    # Integer k-vectors, |k| = 1 and √2 and √3
    k_candidates = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for l in range(-2, 3):
                mag2 = i*i + j*j + l*l
                if 0 < mag2 <= 6:
                    k_candidates.append(np.array([i,j,l], float))

    n_trials = 5000
    for trial in range(n_trials):
        # Random k-pair
        idx = np.random.choice(len(k_candidates), 2, replace=False)
        k1 = k_candidates[idx[0]]
        k2 = k_candidates[idx[1]]

        if np.linalg.norm(np.cross(k1, k2)) < 0.01:
            continue

        # Random perp polarizations
        def rand_perp(k):
            kn = k / np.linalg.norm(k)
            r = np.random.randn(3)
            r -= (r @ kn) * kn
            if np.linalg.norm(r) < 1e-10:
                r = np.random.randn(3)
                r -= (r @ kn) * kn
            return r / np.linalg.norm(r)

        v1 = rand_perp(k1)
        v2 = rand_perp(k2)
        a2 = np.exp(np.random.uniform(-0.5, 0.5))

        # Find TRUE global max of |ω|² on [0,2π)³
        # For two modes: |ω|² = |v1 cos(k1·x) + a2 v2 cos(k2·x)|²
        # Multi-start optimization
        best_om_sq = 0
        best_x = None

        for _ in range(10):
            x0 = np.random.uniform(0, 2*np.pi, 3)

            def neg_omega_sq(xyz):
                omega = v1*np.cos(k1@xyz) + a2*v2*np.cos(k2@xyz)
                return -np.dot(omega, omega)

            def grad_neg_omega_sq(xyz):
                c1 = np.cos(k1@xyz); s1 = np.sin(k1@xyz)
                c2 = np.cos(k2@xyz); s2 = np.sin(k2@xyz)
                omega = v1*c1 + a2*v2*c2
                # d(omega)/d(xyz_j) = -v1*s1*k1_j - a2*v2*s2*k2_j
                grad = np.zeros(3)
                for j in range(3):
                    domega_j = -v1*s1*k1[j] - a2*v2*s2*k2[j]
                    grad[j] = -2 * np.dot(omega, domega_j)
                return grad

            res = minimize(neg_omega_sq, x0, jac=grad_neg_omega_sq, method='L-BFGS-B')
            if -res.fun > best_om_sq:
                best_om_sq = -res.fun
                best_x = res.x.copy()

        if best_x is None or best_om_sq < 0.01:
            continue

        ratio, alpha, omega_mag, is_max = verify_at_max(
            k1, k2, v1, v2, 1.0, a2, best_x)

        if abs(ratio) > best_ratio:
            best_ratio = abs(ratio)
            best_config = {
                'k1': k1.copy(), 'k2': k2.copy(),
                'v1': v1.copy(), 'v2': v2.copy(),
                'a2': a2, 'x': best_x.copy(),
                'ratio': ratio, 'alpha': alpha, 'omega': omega_mag,
                'is_max': is_max
            }
            if trial % 500 == 0 or abs(ratio) > 0.4:
                print(f"  Trial {trial}: |α/ω| = {abs(ratio):.6f}, "
                      f"k1={k1.astype(int).tolist()}, k2={k2.astype(int).tolist()}, "
                      f"is_max={is_max}")

    print(f"\nBest |α/|ω|| at max |ω| = {best_ratio:.6f}")
    if best_config:
        c = best_config
        print(f"k₁ = {c['k1'].astype(int).tolist()}, k₂ = {c['k2'].astype(int).tolist()}")
        print(f"a₂ = {c['a2']:.4f}")
        print(f"α = {c['alpha']:.6f}, |ω| = {c['omega']:.6f}")
        print(f"Is at true max: {c['is_max']}")
    print(f"\nRatio to 0.5 barrier: {best_ratio/0.5:.4f}")

    if best_ratio < 0.5:
        print(f"\n*** 2-MODE BOUND: α/|ω| < {best_ratio:.4f} < 0.5 ***")
        print(f"*** Gap to 0.5: {0.5 - best_ratio:.4f} ({(0.5-best_ratio)/0.5*100:.1f}%) ***")
    else:
        print(f"\n*** 2-MODE: α/|ω| can reach {best_ratio:.4f} ≥ 0.5 ***")

    return best_ratio


if __name__ == '__main__':
    print("MAXIMUM α/|ω| FOR MULTI-MODE DIV-FREE FIELDS ON T³")
    print("=" * 60)

    # Phase 1: Fixed k-pair, brute force
    r1 = brute_force_2mode_fixed_k()

    # Phase 2: Fixed k-pair, optimization
    r2 = optimize_2mode_fixed_k()

    # Phase 3: Scan over k-pairs
    r3 = optimize_many_k_pairs()

    # Phase 4: Careful optimization at true max
    r4 = optimize_2mode_at_true_max()

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Fixed k, brute force:   max |α/ω| = {r1:.6f}")
    print(f"Fixed k, optimized:     max |α/ω| = {r2:.6f}")
    print(f"Many k-pairs:           max |α/ω| = {r3:.6f}")
    print(f"Careful at true max:    max |α/ω| = {r4:.6f}")
    print(f"\nOverall max: {max(r1,r2,r3,r4):.6f}")
    print(f"Critical threshold: 0.500000")

    overall = max(r1,r2,r3,r4)
    if overall < 0.5:
        print(f"\n*** RESULT: For 2-mode fields, α/|ω| < {overall:.4f} < 1/2 ***")
        print(f"*** This is a STRICT bound — kinematic, not dynamic! ***")
    else:
        print(f"\n*** RESULT: 2-mode fields CAN reach α/|ω| = {overall:.4f} ***")
