"""
t3_realizability_v2.py — augmented check.

Goal: rigorously identify TRUE local maxima of |omega|^2 on T^3 (not saddles),
then evaluate the Frobenius ratio at each. Uses analytic gradient and
numerical Hessian to classify each critical point.

Also: expands the seed pool to the full set of grid-detected local maxima
plus a random sample (in case the grid missed any).
"""

import numpy as np
from scipy.ndimage import maximum_filter
from scipy.optimize import minimize

# -----------------------------------------------------------------------------
# Field constants
# -----------------------------------------------------------------------------
SQ2 = np.sqrt(2.0)
SQ3 = np.sqrt(3.0)

k1 = np.array([1.0, 0.0, 0.0], dtype=np.float64)
k2 = np.array([0.0, 1.0, 0.0], dtype=np.float64)
k3 = np.array([0.0, 0.0, 1.0], dtype=np.float64)
k4 = np.array([1.0, 1.0, 1.0], dtype=np.float64) / SQ3

v1 = np.array([0.0, 1.0, 0.0], dtype=np.float64)
v2 = np.array([0.0, 0.0, 1.0], dtype=np.float64)
v3 = np.array([1.0, 0.0, 0.0], dtype=np.float64)
v4 = np.array([1.0, -1.0, 0.0], dtype=np.float64) / SQ2

K = np.stack([k1, k2, k3, k4], axis=0)
V = np.stack([v1, v2, v3, v4], axis=0)

W = np.cross(K, V)
S_stack = np.empty((4, 3, 3), dtype=np.float64)
for j in range(4):
    S_stack[j] = -0.5 * (np.outer(K[j], W[j]) + np.outer(W[j], K[j]))

T_gram = np.einsum('jab,kab->jk', S_stack, S_stack)


def omega_vec(x):
    phi = K @ x
    c = np.cos(phi)
    return c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4


def omega_sq(x):
    v = omega_vec(x)
    return float(np.dot(v, v))


def neg_omega_sq(x):
    return -omega_sq(x)


def grad_omega_sq(x):
    """Analytic gradient of |omega|^2 w.r.t. x in R^3.

    |omega|^2 = sum_m [sum_j c_j v_j^m]^2
    d/dx^n |omega|^2 = sum_m 2 [sum_j c_j v_j^m] * [sum_j -s_j k_j^n v_j^m]
    """
    phi = K @ x        # (4,)
    c = np.cos(phi)
    s = np.sin(phi)
    # omega vector:
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    # d omega / d x^n = sum_j -s_j k_j^n v_j
    # So d|omega|^2/d x^n = 2 * om . sum_j (-s_j k_j^n) v_j
    # = -2 * sum_j s_j k_j^n (om . v_j)
    om_dot_v = np.array([np.dot(om, V[j]) for j in range(4)])  # (4,)
    g = np.zeros(3)
    for n in range(3):
        g[n] = -2.0 * np.sum(s * K[:, n] * om_dot_v)
    return g


def neg_grad_omega_sq(x):
    return -grad_omega_sq(x)


def frobenius_ratio(x):
    phi = K @ x
    c = np.cos(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_sq = float(np.dot(om, om))
    sf_sq = float(c @ T_gram @ c)
    return om_sq, sf_sq, (sf_sq / om_sq if om_sq > 1e-12 else float('nan'))


# -----------------------------------------------------------------------------
# Grid maxima detection
# -----------------------------------------------------------------------------
def grid_local_maxima(N, frac_threshold=0.3):
    L = 2.0 * np.pi
    xs = np.linspace(0.0, L, N, endpoint=False, dtype=np.float64)
    X1, X2, X3 = np.meshgrid(xs, xs, xs, indexing='ij')
    phi1 = X1
    phi2 = X2
    phi3 = X3
    phi4 = (X1 + X2 + X3) / SQ3
    c1 = np.cos(phi1); c2 = np.cos(phi2); c3 = np.cos(phi3); c4 = np.cos(phi4)
    omx = c3 + c4 / SQ2
    omy = c1 - c4 / SQ2
    omz = c2
    osq = omx*omx + omy*omy + omz*omz

    gmax = float(np.max(osq))
    nbhd_max = maximum_filter(osq, size=3, mode='wrap')
    mask = (osq == nbhd_max) & (osq >= frac_threshold * gmax)
    idx = np.argwhere(mask)
    seeds = [np.array([xs[i], xs[j], xs[k]], dtype=np.float64) for (i, j, k) in idx]
    return seeds, gmax


# -----------------------------------------------------------------------------
# Refine + classify
# -----------------------------------------------------------------------------
def refine_and_classify(seeds, dedup_tol=1e-4):
    results = []
    for x0 in seeds:
        res = minimize(neg_omega_sq, x0, jac=neg_grad_omega_sq, method='L-BFGS-B',
                       options={'gtol': 1e-14, 'ftol': 1e-16, 'maxiter': 2000})
        x = np.mod(res.x, 2.0 * np.pi)
        g = grad_omega_sq(x)
        gnorm = float(np.linalg.norm(g))
        om_sq, sf_sq, rat = frobenius_ratio(x)

        # Hessian via central-difference numerical differentiation of grad
        h = 1e-5
        H = np.zeros((3, 3))
        for n in range(3):
            ep = x.copy(); ep[n] += h
            em = x.copy(); em[n] -= h
            H[:, n] = (grad_omega_sq(ep) - grad_omega_sq(em)) / (2.0 * h)
        H = 0.5 * (H + H.T)  # symmetrize
        eigs = np.linalg.eigvalsh(H)
        # For a LOCAL MAX of |omega|^2, all eigenvalues of Hessian should be <= 0.
        is_max = bool(np.all(eigs <= 1e-6))
        results.append({
            'x': x, 'grad_norm': gnorm, 'om_sq': om_sq, 'sf_sq': sf_sq,
            'ratio': rat, 'hessian_eigs': eigs, 'is_max': is_max,
        })

    # Dedup: by periodic L2 distance
    uniq = []
    for r in sorted(results, key=lambda t: -t['om_sq']):
        new = True
        for u in uniq:
            d = np.mod(r['x'] - u['x'] + np.pi, 2.0 * np.pi) - np.pi
            if np.linalg.norm(d) < dedup_tol:
                new = False
                break
        if new:
            uniq.append(r)
    return uniq


def print_points(points, label):
    print(f"\n--- {label} ---", flush=True)
    print(f"  {'rank':>4}  {'x1':>8}  {'x2':>8}  {'x3':>8}  {'|omega|^2':>10}  {'||S||_F^2':>10}  {'ratio':>10}  {'gnorm':>9}  {'is_max':>6}  {'eig_max':>9}", flush=True)
    for r, p in enumerate(points):
        print(f"  {r:4d}  {p['x'][0]:8.5f}  {p['x'][1]:8.5f}  {p['x'][2]:8.5f}  "
              f"{p['om_sq']:10.6f}  {p['sf_sq']:10.6f}  {p['ratio']:10.6f}  "
              f"{p['grad_norm']:9.2e}  {str(p['is_max']):>6}  {np.max(p['hessian_eigs']):9.2e}", flush=True)


def main():
    print("=" * 70, flush=True)
    print(" t3_realizability_v2.py — augmented (with grad/Hessian classification)", flush=True)
    print("=" * 70, flush=True)

    # Seeds from N=128 grid
    print("\n[1] Grid-level seed detection (N=128^3)...", flush=True)
    seeds_128, gmax_128 = grid_local_maxima(128, frac_threshold=0.2)
    print(f"    global max |omega|^2 = {gmax_128:.8f}", flush=True)
    print(f"    # grid-level local maxima above 0.2*gmax: {len(seeds_128)}", flush=True)

    # Also throw in a bunch of random seeds
    rng = np.random.default_rng(0)
    random_seeds = [2.0 * np.pi * rng.random(3) for _ in range(60)]
    seeds_all = seeds_128 + random_seeds

    print(f"\n[2] Refining {len(seeds_all)} seeds with analytic gradient...", flush=True)
    uniq = refine_and_classify(seeds_all)
    print(f"    Unique refined critical points (by position): {len(uniq)}", flush=True)

    # Separate true maxima from saddles / minima
    max_points = [p for p in uniq if p['is_max']]
    non_max_points = [p for p in uniq if not p['is_max']]

    max_points_sorted = sorted(max_points, key=lambda p: -p['om_sq'])
    non_max_points_sorted = sorted(non_max_points, key=lambda p: -p['om_sq'])

    print_points(max_points_sorted[:40], "TRUE LOCAL MAXIMA of |omega|^2 (Hessian <= 0)")
    print_points(non_max_points_sorted[:20], "Saddles / non-maxima (Hessian has positive eig)")

    if max_points_sorted:
        max_rat_at_max = max(p['ratio'] for p in max_points_sorted)
        max_omega_global = max(p['om_sq'] for p in max_points_sorted)
        print(f"\n  >>> MAX |omega|^2 over TRUE maxima: {max_omega_global:.10f}", flush=True)
        print(f"  >>> MAX ratio over TRUE maxima: {max_rat_at_max:.10f}", flush=True)
    else:
        print("\n  !!! no true maxima found (something is wrong)", flush=True)
        max_rat_at_max = None

    print("\n" + "=" * 70, flush=True)
    print(f"  9/8 threshold = {9.0/8.0:.10f}", flush=True)
    if max_rat_at_max is None:
        print("  VERDICT: INCONCLUSIVE (no maxima classified)", flush=True)
    elif max_rat_at_max >= 9.0/8.0:
        print("  VERDICT: KILL — realizable T^3 max with ratio >= 9/8", flush=True)
    else:
        print(f"  VERDICT: CONFIRM — max ratio over TRUE T^3 maxima = {max_rat_at_max:.8f} < 9/8", flush=True)
        print(f"           Margin: {9.0/8.0 - max_rat_at_max:.8f}", flush=True)
    print("=" * 70, flush=True)


if __name__ == "__main__":
    main()
