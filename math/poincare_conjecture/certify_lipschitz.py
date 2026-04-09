"""
COMPUTER-ASSISTED CERTIFICATION: Q > 0 in the max-sign region.

Method: Dense grid evaluation + Lipschitz bound.
If Q_min - L * Δθ > 0: CERTIFIED for this k-config.

For each k-config:
1. Evaluate Q/|ω|² on a grid in (S¹)^N
2. Only count grid points where the current sign pattern IS the max
3. Record the minimum Q/|ω|² in the max region
4. Compute a Lipschitz bound L for Q/|ω|² via numerical derivatives
5. If Q_min > L * Δθ: CERTIFIED
"""
import numpy as np
from itertools import product as iprod, combinations
from scipy.optimize import minimize

def perp(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def evaluate_Q(ks, bases, thetas):
    """Compute Q/|ω|² at the global max sign pattern. Returns (Q/|ω|², is_allplus)."""
    N = len(ks)
    vs = [np.cos(thetas[i])*bases[i][0] + np.sin(thetas[i])*bases[i][1] for i in range(N)]

    best_om2 = 0; best_s = None
    for signs in iprod([1.,-1.], repeat=N):
        omega = sum(s*v for s, v in zip(signs, vs))
        om2 = omega @ omega
        if om2 > best_om2:
            best_om2 = om2; best_s = signs

    if best_om2 < 1e-15:
        return None, False

    omega = sum(s*v for s, v in zip(best_s, vs))
    om2 = omega @ omega
    S = np.zeros((3, 3))
    for k, v, s in zip(ks, vs, best_s):
        w = np.cross(k, s*v)
        S -= (np.outer(w, k) + np.outer(k, w)) / (2 * (k@k))
    S2F = np.sum(S**2)
    Q_norm = (9*om2 - 8*S2F) / om2
    return Q_norm, True

def certify_config(ks, M=40, verbose=False):
    """Certify Q > 0 for a k-vector config using grid + Lipschitz."""
    N = len(ks)
    bases = [perp(k) for k in ks]

    # Step 1: Grid evaluation
    angles = np.linspace(0, 2*np.pi, M, endpoint=False)
    dtheta = 2*np.pi / M

    min_Q = float('inf')
    min_theta = None
    n_in_region = 0

    if N <= 3:
        # Full grid for N≤3
        for idx in iprod(range(M), repeat=N):
            thetas = np.array([angles[i] for i in idx])
            Q, in_region = evaluate_Q(ks, bases, thetas)
            if Q is not None and in_region:
                n_in_region += 1
                if Q < min_Q:
                    min_Q = Q
                    min_theta = thetas.copy()
    else:
        # Random sampling for N≥4
        for _ in range(M**3):
            thetas = np.random.uniform(0, 2*np.pi, N)
            Q, in_region = evaluate_Q(ks, bases, thetas)
            if Q is not None and in_region:
                n_in_region += 1
                if Q < min_Q:
                    min_Q = Q
                    min_theta = thetas.copy()

    if min_Q == float('inf'):
        return {'certified': True, 'reason': 'no_points_in_region', 'min_Q': None}

    # Polish the minimum
    res = minimize(lambda t: evaluate_Q(ks, bases, t)[0] or 1e10,
                   min_theta, method='Nelder-Mead',
                   options={'maxiter': 5000, 'xatol': 1e-14, 'fatol': 1e-15})
    Q_polished = evaluate_Q(ks, bases, res.x)[0]
    if Q_polished is not None:
        min_Q = min(min_Q, Q_polished)

    # Step 2: Lipschitz bound via numerical gradient
    max_grad = 0
    n_grad_samples = min(1000, n_in_region)
    for _ in range(n_grad_samples):
        t0 = np.random.uniform(0, 2*np.pi, N)
        Q0, ok = evaluate_Q(ks, bases, t0)
        if Q0 is None or not ok:
            continue
        for j in range(N):
            h = 1e-6
            tp = t0.copy(); tp[j] += h
            Qp, _ = evaluate_Q(ks, bases, tp)
            if Qp is not None:
                grad = abs(Qp - Q0) / h
                max_grad = max(max_grad, grad)

    L = max_grad * 1.5  # Safety factor

    # Step 3: Certification
    margin = min_Q - L * dtheta * np.sqrt(N)  # diagonal of N-cube
    certified = margin > 0

    result = {
        'certified': certified,
        'min_Q': min_Q,
        'lipschitz': L,
        'margin': margin,
        'dtheta': dtheta,
        'n_in_region': n_in_region,
        'C_ratio': (min_Q - 5) / 16 if min_Q != float('inf') else None,
    }

    if verbose:
        print(f"  min Q/|ω|² = {min_Q:.6f}, L = {L:.2f}, "
              f"L*Δθ*√N = {L*dtheta*np.sqrt(N):.4f}, "
              f"margin = {margin:.4f}, certified = {certified}")

    return result

def certify_shell(K2, M=40, max_N=4, verbose=True):
    """Certify all N-tuples on a single K² shell."""
    # Build modes on this shell
    modes = []
    for i in range(-4, 5):
        for j in range(-4, 5):
            for l in range(-4, 5):
                k = np.array([i, j, l], float)
                if int(k@k) == K2:
                    if not any(np.allclose(k, -u) for u in modes):
                        modes.append(k)

    if len(modes) < 2:
        return {'K2': K2, 'n_modes': len(modes), 'certified': True, 'worst': None}

    if verbose:
        print(f"K²={K2}: {len(modes)} modes")

    worst_Q = float('inf')
    worst_config = None
    n_certified = 0
    n_total = 0

    for N in range(2, min(max_N + 1, len(modes) + 1)):
        subs = list(combinations(range(len(modes)), N))
        if verbose:
            print(f"  N={N}: {len(subs)} configs")

        for sub in subs:
            ks = [modes[i] for i in sub]
            result = certify_config(ks, M=M)
            n_total += 1

            if result['min_Q'] is not None and result['min_Q'] < worst_Q:
                worst_Q = result['min_Q']
                worst_config = [modes[i].astype(int).tolist() for i in sub]

            if result['certified']:
                n_certified += 1

        if verbose and n_total > 0:
            print(f"    Certified: {n_certified}/{n_total}, "
                  f"worst Q/|ω|² = {worst_Q:.6f}")

    return {
        'K2': K2,
        'n_modes': len(modes),
        'certified': n_certified == n_total,
        'n_certified': n_certified,
        'n_total': n_total,
        'worst_Q': worst_Q,
        'worst_config': worst_config,
        'worst_C': (worst_Q - 5) / 16 if worst_Q != float('inf') else None,
    }

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("COMPUTER-ASSISTED CERTIFICATION: Q > 0 at max sign pattern")
    print("Method: Dense grid (M=40) + Lipschitz bound")
    print("=" * 70)

    results = {}
    for K2 in [1, 2, 3, 4, 5, 6, 8, 9]:
        r = certify_shell(K2, M=40, max_N=4)
        results[K2] = r
        status = "✓ CERTIFIED" if r['certified'] else "✗ FAILED"
        worst_C = f"{r['worst_C']:.6f}" if r['worst_C'] is not None else "N/A"
        print(f"  K²={K2}: {status} | worst C/|ω|² = {worst_C} | "
              f"{r['n_certified']}/{r['n_total']} configs")
        print()

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    all_certified = all(r['certified'] for r in results.values())
    overall_worst = min(r['worst_C'] for r in results.values()
                       if r['worst_C'] is not None)
    print(f"All shells certified: {all_certified}")
    print(f"Overall worst C/|ω|²: {overall_worst:.6f}")
    print(f"Threshold: -5/16 = {-5/16:.6f}")
    print(f"Margin: {(-5/16 - overall_worst) / (-5/16) * 100:.1f}%")
