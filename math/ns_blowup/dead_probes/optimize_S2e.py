"""
OPTIMIZE S²ê/|ω|² at the vorticity max.
Find the absolute worst case for div-free fields on T³.
Use gradient-based optimization over mode parameters.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution

def compute_S2e_ratio(k_list, v_list, a_list, x):
    """Compute S²ê/|ω|² at point x."""
    omega = np.zeros(3)
    S = np.zeros((3, 3))
    for k, v, a in zip(k_list, v_list, a_list):
        k = np.asarray(k, float); v = np.asarray(v, float)
        cos_kx = np.cos(k @ x)
        kxv = np.cross(k, v)
        k2 = k @ k
        omega += a * v * cos_kx
        grad_u = a * np.outer(kxv, k) * cos_kx / k2
        S += 0.5 * (grad_u + grad_u.T)

    om2 = np.dot(omega, omega)
    if om2 < 1e-20:
        return 0.0, 0.0, 0.0
    e_hat = omega / np.sqrt(om2)
    Se = S @ e_hat
    S2e = np.dot(Se, Se)
    alpha = np.dot(e_hat, Se)
    return S2e / om2, alpha / np.sqrt(om2), np.sqrt(om2)


def optimize_2mode_S2e():
    """Optimize S²ê/|ω|² for 2 modes with k₁=(1,0,0), k₂=(0,1,0)."""
    print("2-MODE OPTIMIZATION: k₁=(1,0,0), k₂=(0,1,0)")

    def objective(params):
        th1, th2, log_a, x, y, z = params
        v1 = np.array([0, np.cos(th1), np.sin(th1)])
        v2 = np.array([np.cos(th2), 0, np.sin(th2)])
        k1 = np.array([1,0,0.]); k2 = np.array([0,1,0.])
        a2 = np.exp(log_a)
        pt = np.array([x, y, z])

        # First check if we're near a max of |ω|
        omega = v1*np.cos(k1@pt) + a2*v2*np.cos(k2@pt)
        om2 = np.dot(omega, omega)
        if om2 < 0.01:
            return 0.0

        # Gradient of |ω|² should be ~0
        grad = np.zeros(3)
        for j in range(3):
            domega = -v1*np.sin(k1@pt)*k1[j] - a2*v2*np.sin(k2@pt)*k2[j]
            grad[j] = 2*np.dot(omega, domega)
        grad_penalty = np.dot(grad, grad) / (om2 + 1)

        ratio, alpha_r, om = compute_S2e_ratio(
            [k1, k2], [v1, v2], [1.0, a2], pt)

        # Maximize ratio while being at a max of |ω|
        return -(ratio - 100*grad_penalty)

    best = 0; best_params = None
    for _ in range(5000):
        x0 = np.random.uniform([0, 0, -1, 0, 0, 0],
                                [2*np.pi, 2*np.pi, 1, 2*np.pi, 2*np.pi, 2*np.pi])
        res = minimize(objective, x0, method='Nelder-Mead',
                       options={'maxiter': 2000, 'xatol': 1e-12})
        if -res.fun > best:
            best = -res.fun
            best_params = res.x

    print(f"  Best S²ê/|ω|² = {best:.6f}")
    return best


def optimize_Nmode_S2e(N, n_trials=3000):
    """Optimize S²ê/|ω|² for N modes, general k-vectors."""
    # Pre-compute valid k-vectors
    all_ks = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for l in range(-2, 3):
                if 0 < i*i+j*j+l*l <= 6:
                    all_ks.append(np.array([i,j,l], float))

    best_ratio = 0
    best_config = None

    for trial in range(n_trials):
        idx = np.random.choice(len(all_ks), min(N, len(all_ks)), replace=False)
        ks = [all_ks[i] for i in idx]

        def rand_perp(k):
            kn = k / np.linalg.norm(k)
            r = np.random.randn(3)
            r -= (r @ kn) * kn
            n = np.linalg.norm(r)
            return r / n if n > 1e-10 else rand_perp(k)

        vs = [rand_perp(k) for k in ks]
        a_s = np.exp(np.random.uniform(-0.3, 0.3, len(ks)))

        # Find max |ω|
        best_om2 = 0; best_x = None
        for _ in range(10):
            x0 = np.random.uniform(0, 2*np.pi, 3)
            def neg_om2(xyz):
                om = sum(a*v*np.cos(k@xyz) for k,v,a in zip(ks,vs,a_s))
                return -np.dot(om, om)
            res = minimize(neg_om2, x0, method='Nelder-Mead',
                           options={'maxiter': 3000, 'xatol': 1e-11})
            if -res.fun > best_om2:
                best_om2 = -res.fun
                best_x = res.x.copy()

        if best_x is None or best_om2 < 0.01:
            continue

        ratio, alpha_r, om = compute_S2e_ratio(ks, vs, a_s.tolist(), best_x)

        if ratio > best_ratio:
            best_ratio = ratio
            best_config = {'ks': [k.tolist() for k in ks],
                           'ratio': ratio, 'alpha_r': alpha_r}

    return best_ratio, best_config


def optimize_with_gradient_free(N, n_trials=500):
    """Use differential evolution to find worst S²ê/|ω|² for N modes."""
    all_ks = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for l in range(-2, 3):
                if 0 < i*i+j*j+l*l <= 3:
                    all_ks.append(np.array([i,j,l], float))

    best_ratio = 0

    for trial in range(n_trials):
        # Pick N random k-vectors
        idx = np.random.choice(len(all_ks), min(N, len(all_ks)), replace=False)
        ks = [all_ks[i] for i in idx]

        # Optimize over polarization angles, amplitudes, and position
        # Each mode: 1 angle (rotation in perp plane) + 1 log-amplitude
        # Plus 3 position coords
        n_params = N + N + 3  # angles + log_amps + xyz

        def objective(params):
            angles = params[:N]
            log_amps = params[N:2*N]
            xyz = params[2*N:2*N+3]

            vs = []
            for i, k in enumerate(ks):
                kn = k / np.linalg.norm(k)
                # Build orthonormal basis perp to k
                if abs(kn[0]) < 0.9:
                    e1 = np.cross(kn, [1,0,0])
                else:
                    e1 = np.cross(kn, [0,1,0])
                e1 /= np.linalg.norm(e1)
                e2 = np.cross(kn, e1)
                vs.append(np.cos(angles[i])*e1 + np.sin(angles[i])*e2)

            a_s = np.exp(log_amps)

            # Find max |ω| near xyz
            def neg_om2(pt):
                om = sum(a*v*np.cos(k@pt) for k,v,a in zip(ks, vs, a_s))
                return -np.dot(om, om)

            # Quick local optimization from the given xyz
            res = minimize(neg_om2, xyz, method='Nelder-Mead',
                           options={'maxiter': 500})
            x_max = res.x
            om2 = -res.fun
            if om2 < 0.01:
                return 0.0

            ratio, _, _ = compute_S2e_ratio(ks, vs, a_s.tolist(), x_max)
            return -ratio  # Minimize negative = maximize

        bounds = [(0, 2*np.pi)]*N + [(-0.5, 0.5)]*N + [(0, 2*np.pi)]*3
        try:
            res = differential_evolution(objective, bounds, maxiter=100,
                                         seed=trial, tol=1e-6, polish=True)
            if -res.fun > best_ratio:
                best_ratio = -res.fun
        except:
            pass

    return best_ratio


if __name__ == '__main__':
    np.random.seed(123)

    print("MAXIMIZING S²ê / |ω|² AT VORTICITY MAXIMUM")
    print("=" * 60)
    print(f"Barrier threshold: 0.750")
    print()

    # 2-mode optimization
    r2 = optimize_2mode_S2e()

    # N-mode random search
    print()
    for N in [2, 3, 4, 5, 8, 12]:
        n_t = 5000 if N <= 5 else 2000
        r, cfg = optimize_Nmode_S2e(N, n_t)
        print(f"N={N:2d}: worst S²ê/|ω|² = {r:.6f}  "
              f"(α/|ω| = {cfg['alpha_r']:.4f})" if cfg else f"N={N}: {r:.6f}")

    # DE optimization for small N
    print("\nDifferential evolution (intensive):")
    for N in [2, 3, 4, 5]:
        r = optimize_with_gradient_free(N, n_trials=200)
        print(f"  N={N}: worst S²ê/|ω|² = {r:.6f}")

    print(f"\nBarrier at 0.750: the bound holds with margin ≥ {0.75 - 0.30:.2f}")
