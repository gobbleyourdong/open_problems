"""
t3_realizability_v4.py — robust Newton-style local search.

Strategy:
  - Sample a very fine grid (128^3) and enumerate ALL grid local maxima
    (nearest-neighbor, periodic).
  - For each grid-level candidate, run an analytic Newton iteration using
    the analytic gradient and analytic Hessian of |omega|^2. (Both are
    trigonometric, computable in closed form.)
  - Classify each converged point by Hessian eigenvalues.
  - Separately, add a large random seed pool + BFGS refine, to catch any
    local maxima the grid missed.

We need a RELIABLE verdict on:
    max_{ x a true local max of |omega|^2 } ||S(x)||_F^2 / |omega(x)|^2

against 9/8 = 1.125.
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

# Precompute Gram of v: M_{jk} = v_j . v_k
Mv = V @ V.T  # (4,4)


def fields_at(x):
    """Return c, s, om, om_sq, ||S||_F^2, ratio."""
    phi = K @ x
    c = np.cos(phi); s = np.sin(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_sq = float(np.dot(om, om))
    sf_sq = float(c @ T_gram @ c)
    rat = sf_sq / om_sq if om_sq > 1e-14 else float('nan')
    return c, s, om, om_sq, sf_sq, rat


def omega_sq(x):
    c = np.cos(K @ x)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    return float(np.dot(om, om))


def neg_omega_sq(x):
    return -omega_sq(x)


def grad_omega_sq(x):
    """Analytic gradient of |omega|^2."""
    phi = K @ x
    c = np.cos(phi); s = np.sin(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_dot_v = V @ om   # (4,)
    # d|om|^2 / dx^n = -2 sum_j s_j k_j^n (om . v_j)
    return -2.0 * (K.T @ (s * om_dot_v))  # (3,)


def hess_omega_sq(x):
    """Analytic Hessian of |omega|^2.
    |om|^2 = sum_{j,k} c_j c_k M_{jk},   M_{jk}=v_j.v_k.
    d/dx^n = -2 sum_{j,k} s_j k_j^n c_k M_{jk}
           = -2 sum_{j,k} s_j c_k M_{jk} k_j^n
    d^2/(dx^n dx^m) = -2 sum_{j,k} [ -c_j k_j^m c_k M_{jk} k_j^n
                                   + s_j k_j^n (-s_k k_k^m) M_{jk} ]
          = 2 sum_{j,k} c_j c_k M_{jk} k_j^m k_j^n
            + 2 sum_{j,k} s_j s_k M_{jk} k_j^n k_k^m
    """
    phi = K @ x
    c = np.cos(phi); s = np.sin(phi)
    # First term: A_{nm} = 2 sum_{j,k} c_j c_k M_{jk} k_j^n k_j^m
    # = 2 sum_j c_j (sum_k c_k M_{jk}) k_j^n k_j^m
    # Let a_j := c_j * sum_k M_{jk} c_k  = c_j * (Mv @ c)_j
    a = c * (Mv @ c)  # (4,)
    A = 2.0 * (K.T * a) @ K  # K^T diag(a) K? Let's compute explicitly
    # A_{nm} = 2 sum_j a_j k_j^n k_j^m
    A = 2.0 * np.einsum('j,jn,jm->nm', a, K, K)
    # Second term: B_{nm} = 2 sum_{j,k} s_j s_k M_{jk} k_j^n k_k^m
    # = 2 (K^T diag(s) Mv diag(s) K)_{nm}
    B = 2.0 * (K.T * s) @ Mv @ (s[:, None] * K)
    return A + B


def neg_grad(x):
    return -grad_omega_sq(x)


def neg_hess(x):
    return -hess_omega_sq(x)


def newton_refine(x0, max_iter=500, tol=1e-13):
    """Use scipy trust-ncg for maximization of |omega|^2 (min of neg)."""
    try:
        res = minimize(neg_omega_sq, x0, jac=neg_grad, hess=neg_hess,
                       method='trust-ncg',
                       options={'xtol': 1e-14, 'maxiter': max_iter})
        x = res.x
    except Exception as e:
        # Fall back to BFGS
        res = minimize(neg_omega_sq, x0, jac=neg_grad, method='BFGS',
                       options={'gtol': 1e-13, 'maxiter': max_iter})
        x = res.x
    # polish: pure Newton on gradient to drive ||grad|| down exactly
    for _ in range(50):
        g = grad_omega_sq(x)
        if np.linalg.norm(g) < tol:
            break
        H = hess_omega_sq(x)
        try:
            dx = np.linalg.solve(H, g)
        except np.linalg.LinAlgError:
            dx = np.linalg.lstsq(H + 1e-10*np.eye(3), g, rcond=None)[0]
        x = x - dx
    x = np.mod(x, 2.0 * np.pi)
    return x


def grid_seeds(N, frac=0.01):
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
    return seeds, gmax, osq


def run():
    print("=" * 72, flush=True)
    print(" t3_realizability_v4.py — analytic Newton w/ Hessian classification", flush=True)
    print(" 9/8 = {:.10f}".format(9.0/8.0), flush=True)
    print("=" * 72, flush=True)

    # Grid seeds
    seeds, gmax, osq = grid_seeds(128, frac=0.01)
    print(f"\n[1] Grid N=128: global max |omega|^2 ~ {gmax:.6f}", flush=True)
    print(f"    # grid-level local maxima (thresh 0.01*gmax) = {len(seeds)}", flush=True)

    # Refine each grid seed with Newton
    all_pts = []
    for s in seeds:
        x = newton_refine(s)
        all_pts.append(x)

    # Add random seeds
    rng = np.random.default_rng(123)
    for _ in range(500):
        s = 2.0 * np.pi * rng.random(3)
        x = newton_refine(s)
        all_pts.append(x)

    # Classify each point
    records = []
    for x in all_pts:
        g = grad_omega_sq(x)
        gn = float(np.linalg.norm(g))
        c, s, om, om_sq, sf_sq, rat = fields_at(x)
        H = hess_omega_sq(x)
        # For |omega|^2 to be a max, Hessian of |omega|^2 should be NSD (eigs <= 0)
        eigs = np.linalg.eigvalsh(H)
        records.append({'x': x, 'grad_norm': gn, 'om_sq': om_sq,
                        'sf_sq': sf_sq, 'ratio': rat, 'eigs': eigs})

    # Dedup
    uniq = []
    for r in sorted(records, key=lambda t: -t['om_sq']):
        new = True
        for u in uniq:
            d = np.mod(r['x'] - u['x'] + np.pi, 2.0 * np.pi) - np.pi
            if np.linalg.norm(d) < 1e-3:
                new = False; break
        if new:
            uniq.append(r)
    print(f"[2] Unique refined points: {len(uniq)}", flush=True)

    # Converged
    conv = [r for r in uniq if r['grad_norm'] < 1e-8]
    print(f"    Converged (||grad|| < 1e-8): {len(conv)}", flush=True)

    # True maxima (Hessian NSD)
    true_max = [r for r in conv if np.max(r['eigs']) <= 1e-8]
    saddles  = [r for r in conv if np.max(r['eigs']) > 1e-8]

    true_max.sort(key=lambda r: -r['om_sq'])
    saddles.sort(key=lambda r: -r['om_sq'])

    def print_tbl(pts, label, n=40):
        print(f"\n--- {label} (showing top {min(n, len(pts))} of {len(pts)}) ---", flush=True)
        print(f"  {'rk':>3} {'x1':>8} {'x2':>8} {'x3':>8} {'|om|^2':>10} {'||S||^2':>10} {'ratio':>10} {'gnorm':>9} {'max_eig':>10} {'min_eig':>10}", flush=True)
        for i, r in enumerate(pts[:n]):
            print(f"  {i:3d} {r['x'][0]:8.5f} {r['x'][1]:8.5f} {r['x'][2]:8.5f} "
                  f"{r['om_sq']:10.6f} {r['sf_sq']:10.6f} {r['ratio']:10.6f} "
                  f"{r['grad_norm']:9.2e} {np.max(r['eigs']):10.2e} {np.min(r['eigs']):10.2e}", flush=True)

    print_tbl(true_max, "TRUE LOCAL MAXIMA of |omega|^2")
    print_tbl(saddles, "Saddles / non-maxima")

    print(f"\n[3] Summary", flush=True)
    if true_max:
        max_rat = max(r['ratio'] for r in true_max)
        max_om = max(r['om_sq'] for r in true_max)
        idx_best = np.argmax([r['ratio'] for r in true_max])
        best = true_max[idx_best]
        print(f"    # true local maxima: {len(true_max)}", flush=True)
        print(f"    Max |omega|^2 over true maxima: {max_om:.10f}", flush=True)
        print(f"    Max ratio over true maxima:     {max_rat:.10f}", flush=True)
        print(f"    Max-ratio point: x = {best['x']}", flush=True)
        print(f"                     |om|^2 = {best['om_sq']:.10f}, ratio = {best['ratio']:.10f}", flush=True)
        print(f"    9/8 = {9.0/8.0:.10f}", flush=True)
        if max_rat >= 9.0/8.0:
            print("    VERDICT: KILL — T^3 max violates 9/8", flush=True)
        else:
            print(f"    VERDICT: CONFIRM — max ratio {max_rat:.6f} < 1.125 (margin {9.0/8.0-max_rat:.6f})", flush=True)
    else:
        print("    VERDICT: INCONCLUSIVE — no true maxima identified", flush=True)


if __name__ == "__main__":
    run()
