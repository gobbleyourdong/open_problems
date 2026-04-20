"""
t3_realizability_v5.py — FINAL clean version.

Approach: high-resolution grid enumeration of local maxima of |omega|^2 on T^3.
For each grid-level local maximum, locally refine via scipy BFGS with analytic
gradient, then classify by analytic Hessian to keep only true maxima.

The question: does any TRUE local maximum of |omega|^2 have
  ||S(x)||_F^2 / |omega(x)|^2 >= 9/8 = 1.125 ?
"""

import numpy as np
from scipy.ndimage import maximum_filter
from scipy.optimize import minimize

SQ2 = np.sqrt(2.0); SQ3 = np.sqrt(3.0)
k1 = np.array([1.0,0,0]); k2 = np.array([0,1.0,0]); k3 = np.array([0,0,1.0])
k4 = np.array([1.0,1.0,1.0]) / SQ3
v1 = np.array([0,1.0,0]); v2 = np.array([0,0,1.0]); v3 = np.array([1.0,0,0])
v4 = np.array([1.0,-1.0,0]) / SQ2
K = np.stack([k1,k2,k3,k4]); V = np.stack([v1,v2,v3,v4])
W = np.cross(K, V)
S_stack = np.empty((4,3,3))
for j in range(4):
    S_stack[j] = -0.5 * (np.outer(K[j], W[j]) + np.outer(W[j], K[j]))
T_gram = np.einsum('jab,kab->jk', S_stack, S_stack)
Mv = V @ V.T


def omega_sq(x):
    c = np.cos(K @ x)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    return float(om @ om)


def neg_omega_sq(x):
    return -omega_sq(x)


def grad(x):
    phi = K @ x; c = np.cos(phi); s = np.sin(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    ov = V @ om
    return -2.0 * (K.T @ (s * ov))


def neg_grad(x):
    return -grad(x)


def hessian_omega(x):
    """Analytic Hessian of |omega|^2.
    H_{nm} = -2 sum_j c_j (Mv c)_j k_j^n k_j^m  +  2 sum_{j,k} M_{jk} s_j s_k k_j^n k_k^m.
    """
    phi = K @ x; c = np.cos(phi); s = np.sin(phi)
    a = c * (Mv @ c)
    A = -2.0 * np.einsum('j,jn,jm->nm', a, K, K)
    B = 2.0 * (K.T * s) @ Mv @ (s[:, None] * K)
    return A + B


def ratio_at(x):
    c = np.cos(K @ x)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_sq = float(om @ om)
    sf_sq = float(c @ T_gram @ c)
    return om_sq, sf_sq, (sf_sq / om_sq if om_sq > 1e-14 else float('nan'))


def refine(x0):
    res = minimize(neg_omega_sq, x0, jac=neg_grad, method='BFGS',
                   options={'gtol': 1e-13, 'maxiter': 2000})
    x = np.mod(res.x, 2.0*np.pi)
    return x


def run_analysis(N):
    print(f"\n--- N = {N}^3 grid enumeration ---", flush=True)
    L = 2.0 * np.pi
    xs = np.linspace(0, L, N, endpoint=False)
    dx = xs[1] - xs[0]
    X1, X2, X3 = np.meshgrid(xs, xs, xs, indexing='ij')
    phi4 = (X1 + X2 + X3) / SQ3
    c1 = np.cos(X1); c2 = np.cos(X2); c3 = np.cos(X3); c4 = np.cos(phi4)
    omx = c3 + c4/SQ2; omy = c1 - c4/SQ2; omz = c2
    osq = omx*omx + omy*omy + omz*omz

    # pointwise ||S||_F^2 and ratio on the grid
    sf_grid = np.zeros_like(osq)
    c_arr = np.stack([c1, c2, c3, c4])
    for j in range(4):
        for k in range(4):
            sf_grid += T_gram[j,k] * c_arr[j] * c_arr[k]
    ratio_grid = np.where(osq > 1e-10, sf_grid / osq, np.nan)

    gmax_osq = float(np.max(osq))
    # Grid-level local maxima (periodic)
    nbhd = maximum_filter(osq, size=3, mode='wrap')
    lmask = (osq == nbhd)
    lidx = np.argwhere(lmask)
    print(f"  dx = {dx:.4e}, gmax |omega|^2 = {gmax_osq:.6f}, #grid local maxima = {len(lidx)}", flush=True)

    # Filter: require |omega|^2 > some small threshold (not a vorticity zero)
    nontrivial = []
    for (i,j,k) in lidx:
        if osq[i,j,k] > 1e-6:
            nontrivial.append((i,j,k))
    print(f"  #non-trivial grid maxima (|omega|^2 > 1e-6): {len(nontrivial)}", flush=True)

    return xs, osq, sf_grid, ratio_grid, nontrivial


def main():
    print("="*74, flush=True)
    print(" t3_realizability_v5.py — T^3 local maxima of |omega|^2 (attempt 855)", flush=True)
    print(f" threshold 9/8 = {9.0/8.0:.10f}", flush=True)
    print("="*74, flush=True)

    # Run at N=128
    xs128, osq128, sf128, ratio128, grid_max128 = run_analysis(128)
    # Run at N=256
    xs256, osq256, sf256, ratio256, grid_max256 = run_analysis(256)

    # Seed refinement from N=256 grid maxima
    seeds = []
    for (i,j,k) in grid_max256:
        seeds.append(np.array([xs256[i], xs256[j], xs256[k]]))

    # Plus random seeds
    rng = np.random.default_rng(7)
    rand_seeds = [2.0 * np.pi * rng.random(3) for _ in range(200)]

    # Refine all
    all_pts = []
    for s in seeds + rand_seeds:
        x = refine(s)
        all_pts.append(x)

    # Classify
    records = []
    for x in all_pts:
        g = grad(x)
        gn = float(np.linalg.norm(g))
        om_sq, sf_sq, rat = ratio_at(x)
        H = hessian_omega(x)
        eigs = np.linalg.eigvalsh(H)
        records.append({'x': x, 'gn': gn, 'om_sq': om_sq, 'sf_sq': sf_sq,
                        'ratio': rat, 'eigs': eigs})

    # Dedup
    uniq = []
    for r in sorted(records, key=lambda t: -t['om_sq']):
        new = True
        for u in uniq:
            d = np.mod(r['x'] - u['x'] + np.pi, 2.0*np.pi) - np.pi
            if np.linalg.norm(d) < 2e-3:
                new = False; break
        if new:
            uniq.append(r)

    conv = [r for r in uniq if r['gn'] < 1e-4]
    true_max = [r for r in conv if np.max(r['eigs']) <= 1e-4 and r['om_sq'] > 1e-4]
    true_max.sort(key=lambda r: -r['om_sq'])

    print(f"\n[Classification]", flush=True)
    print(f"  Unique refined points: {len(uniq)}", flush=True)
    print(f"  Converged (||grad|| < 1e-4): {len(conv)}", flush=True)
    print(f"  TRUE LOCAL MAXIMA (Hessian NSD, |om|^2 > 1e-4): {len(true_max)}", flush=True)

    print(f"\n  {'rk':>3} {'x1':>8} {'x2':>8} {'x3':>8} {'|om|^2':>10} {'||S||^2':>10} {'ratio':>10} {'gnorm':>9} {'max_eig':>10}", flush=True)
    for i, r in enumerate(true_max):
        print(f"  {i:3d} {r['x'][0]:8.5f} {r['x'][1]:8.5f} {r['x'][2]:8.5f} "
              f"{r['om_sq']:10.6f} {r['sf_sq']:10.6f} {r['ratio']:10.6f} "
              f"{r['gn']:9.2e} {np.max(r['eigs']):10.2e}", flush=True)

    # Also report the cross-check: max ratio over grid cells (N=256) restricted
    # to |omega|^2 > 0.5 * global max.
    mask_keep = osq256 > 0.5 * np.max(osq256)
    print(f"\n[Grid cross-check, N=256, |omega|^2 > 0.5 * global max]", flush=True)
    print(f"  Max ratio in this region: {np.max(ratio256[mask_keep]):.8f}", flush=True)
    print(f"  Min ratio in this region: {np.min(ratio256[mask_keep]):.8f}", flush=True)

    # Also check: for each grid-level local max (unrefined) of |omega|^2, the ratio
    print(f"\n[Grid cross-check: ratio at each grid-level local max (N=256)]", flush=True)
    grid_ratios_at_max = [ratio256[i,j,k] for (i,j,k) in grid_max256 if osq256[i,j,k] > 0.5*np.max(osq256)]
    if grid_ratios_at_max:
        print(f"  Top-half grid-level local maxima: {len(grid_ratios_at_max)}", flush=True)
        print(f"  Max ratio among these: {max(grid_ratios_at_max):.8f}", flush=True)

    # Final verdict
    print("\n" + "="*74, flush=True)
    if true_max:
        max_rat = max(r['ratio'] for r in true_max)
        max_om = max(r['om_sq'] for r in true_max)
        print(f" MAX |omega|^2 over TRUE maxima: {max_om:.10f}", flush=True)
        print(f" MAX ratio over TRUE maxima:     {max_rat:.10f}", flush=True)
        print(f" 9/8 threshold:                  {9.0/8.0:.10f}", flush=True)
        if max_rat >= 9.0/8.0:
            print(" VERDICT: KILL — T^3 max with ratio >= 9/8", flush=True)
        else:
            print(f" VERDICT: CONFIRM — max ratio {max_rat:.6f} < 9/8 (margin {9.0/8.0-max_rat:.6f})", flush=True)
    else:
        print(" VERDICT: INCONCLUSIVE (no true maxima identified)", flush=True)
    print("="*74, flush=True)


if __name__ == "__main__":
    main()
