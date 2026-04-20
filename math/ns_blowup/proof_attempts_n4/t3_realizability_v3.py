"""
t3_realizability_v3.py — strict version.

Only accept critical points where grad_norm < tol AND Hessian <= 0.
Also use trust-ncg / BFGS with many restarts and a very fine grid seed pool.
"""

import numpy as np
from scipy.ndimage import maximum_filter
from scipy.optimize import minimize

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


def omega_sq(x):
    phi = K @ x
    c = np.cos(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    return float(np.dot(om, om))


def neg_omega_sq(x):
    return -omega_sq(x)


def grad_omega_sq(x):
    phi = K @ x
    c = np.cos(phi)
    s = np.sin(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_dot_v = np.array([np.dot(om, V[j]) for j in range(4)])
    g = np.zeros(3)
    for n in range(3):
        g[n] = -2.0 * np.sum(s * K[:, n] * om_dot_v)
    return g


def neg_grad_omega_sq(x):
    return -grad_omega_sq(x)


def hessian(x, h=1e-5):
    H = np.zeros((3, 3))
    for n in range(3):
        ep = x.copy(); ep[n] += h
        em = x.copy(); em[n] -= h
        H[:, n] = (grad_omega_sq(ep) - grad_omega_sq(em)) / (2.0 * h)
    return 0.5 * (H + H.T)


def frobenius_ratio(x):
    phi = K @ x
    c = np.cos(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_sq = float(np.dot(om, om))
    sf_sq = float(c @ T_gram @ c)
    return om_sq, sf_sq, (sf_sq / om_sq if om_sq > 1e-12 else float('nan'))


def refine_one(x0):
    # BFGS with analytic gradient; fall back to Newton-CG for polish
    res = minimize(neg_omega_sq, x0, jac=neg_grad_omega_sq, method='BFGS',
                   options={'gtol': 1e-13, 'maxiter': 2000})
    x = res.x
    # polish with Newton-CG using analytic Hessian
    try:
        res2 = minimize(neg_omega_sq, x, jac=neg_grad_omega_sq,
                        hess=lambda y: -hessian(y),
                        method='Newton-CG',
                        options={'xtol': 1e-14, 'maxiter': 500})
        x = res2.x
    except Exception:
        pass
    x = np.mod(x, 2.0 * np.pi)
    return x


def grid_seeds(N, frac=0.02):
    L = 2.0 * np.pi
    xs = np.linspace(0.0, L, N, endpoint=False, dtype=np.float64)
    X1, X2, X3 = np.meshgrid(xs, xs, xs, indexing='ij')
    phi1 = X1; phi2 = X2; phi3 = X3; phi4 = (X1 + X2 + X3) / SQ3
    c1 = np.cos(phi1); c2 = np.cos(phi2); c3 = np.cos(phi3); c4 = np.cos(phi4)
    omx = c3 + c4 / SQ2
    omy = c1 - c4 / SQ2
    omz = c2
    osq = omx*omx + omy*omy + omz*omz
    gmax = float(np.max(osq))
    nbhd_max = maximum_filter(osq, size=3, mode='wrap')
    mask = (osq == nbhd_max) & (osq >= frac * gmax)
    idx = np.argwhere(mask)
    seeds = [np.array([xs[i], xs[j], xs[k]], dtype=np.float64) for (i, j, k) in idx]
    return seeds, gmax, osq, xs


def main():
    print("=" * 72, flush=True)
    print(" t3_realizability_v3.py — strict critical point classification", flush=True)
    print("=" * 72, flush=True)

    # Detect seeds from a fine grid
    seeds, gmax, osq_grid, xs = grid_seeds(128, frac=0.01)
    print(f"\n[1] N=128^3 grid: global max |omega|^2 = {gmax:.8f}", flush=True)
    print(f"    # grid local maxima (threshold 0.01 gmax) = {len(seeds)}", flush=True)

    # Add random seeds to cover the torus
    rng = np.random.default_rng(42)
    rand_seeds = [2.0 * np.pi * rng.random(3) for _ in range(200)]
    all_seeds = seeds + rand_seeds
    print(f"[2] Adding {len(rand_seeds)} random seeds → total {len(all_seeds)}", flush=True)

    # Refine each seed
    records = []
    for i, s in enumerate(all_seeds):
        x = refine_one(s)
        g = grad_omega_sq(x)
        gn = float(np.linalg.norm(g))
        H = hessian(x)
        eigs = np.linalg.eigvalsh(H)
        om_sq, sf_sq, rat = frobenius_ratio(x)
        records.append({
            'x': x, 'grad_norm': gn, 'om_sq': om_sq, 'sf_sq': sf_sq,
            'ratio': rat, 'eigs': eigs,
        })

    # Dedup by periodic L2 distance
    uniq = []
    for r in sorted(records, key=lambda t: -t['om_sq']):
        new = True
        for u in uniq:
            d = np.mod(r['x'] - u['x'] + np.pi, 2.0 * np.pi) - np.pi
            if np.linalg.norm(d) < 1e-3:
                new = False
                break
        if new:
            uniq.append(r)
    print(f"[3] Unique refined critical points: {len(uniq)}", flush=True)

    # Filter to CONVERGED critical points (gnorm tiny)
    converged = [r for r in uniq if r['grad_norm'] < 1e-5]
    print(f"    Converged critical points (||grad|| < 1e-5): {len(converged)}", flush=True)

    # Classify by Hessian
    true_max = [r for r in converged if np.all(r['eigs'] <= 1e-8)]
    saddles  = [r for r in converged if not np.all(r['eigs'] <= 1e-8)]

    true_max.sort(key=lambda r: -r['om_sq'])
    saddles.sort(key=lambda r: -r['om_sq'])

    print("\n--- TRUE LOCAL MAXIMA of |omega|^2 (converged + all Hessian eigs <= 0) ---", flush=True)
    print(f"  {'rank':>4} {'x1':>9} {'x2':>9} {'x3':>9} {'|om|^2':>10} {'||S||^2':>10} {'ratio':>10} {'gnorm':>9} {'eig_max':>9}", flush=True)
    for i, r in enumerate(true_max):
        print(f"  {i:4d} {r['x'][0]:9.5f} {r['x'][1]:9.5f} {r['x'][2]:9.5f} "
              f"{r['om_sq']:10.6f} {r['sf_sq']:10.6f} {r['ratio']:10.6f} "
              f"{r['grad_norm']:9.2e} {np.max(r['eigs']):9.2e}", flush=True)

    print("\n--- Saddles / other critical points (converged, but Hessian has positive eig) ---", flush=True)
    for i, r in enumerate(saddles[:30]):
        print(f"  {i:4d} {r['x'][0]:9.5f} {r['x'][1]:9.5f} {r['x'][2]:9.5f} "
              f"{r['om_sq']:10.6f} {r['sf_sq']:10.6f} {r['ratio']:10.6f} "
              f"{r['grad_norm']:9.2e} {np.max(r['eigs']):9.2e}", flush=True)

    if true_max:
        max_rat = max(r['ratio'] for r in true_max)
        max_om = max(r['om_sq'] for r in true_max)
        print(f"\n>>> MAX |omega|^2 over true maxima: {max_om:.10f}", flush=True)
        print(f">>> MAX ratio over true maxima:     {max_rat:.10f}", flush=True)
        print(f">>> 9/8 threshold:                  {9.0/8.0:.10f}", flush=True)
        if max_rat >= 9.0/8.0:
            print(">>> VERDICT: KILL — realizable T^3 max with ratio >= 9/8", flush=True)
        else:
            print(f">>> VERDICT: CONFIRM — max ratio {max_rat:.8f} < 9/8, margin {9.0/8.0-max_rat:.8f}", flush=True)
    else:
        print("\nNO TRUE MAXIMA FOUND — INCONCLUSIVE", flush=True)

    # Save top critical points for later inspection
    np.savez('~/open_problems/math/ns_blowup/proof_attempts_n4/t3_crit_points.npz',
             true_max_x=np.array([r['x'] for r in true_max]) if true_max else np.zeros((0,3)),
             true_max_ratio=np.array([r['ratio'] for r in true_max]) if true_max else np.zeros(0),
             true_max_om_sq=np.array([r['om_sq'] for r in true_max]) if true_max else np.zeros(0))


if __name__ == "__main__":
    main()
