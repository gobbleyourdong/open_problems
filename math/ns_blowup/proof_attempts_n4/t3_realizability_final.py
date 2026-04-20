"""
t3_realizability_final.py — FINAL version with corrected Hessian.

Strategy:
  1. Dense grid N=256 on T^3, compute |omega|^2 and ||S||_F^2 pointwise.
  2. Enumerate grid-level local maxima (nearest-neighbor, periodic).
  3. For EACH grid local max, seed BFGS refinement with analytic gradient.
  4. Classify each converged point by analytic Hessian (corrected sign).
  5. Report: for each TRUE local maximum of |omega|^2 on T^3, the Frobenius
     ratio ||S||_F^2 / |omega|^2.
  6. Also report max ratio over N=256 grid cells with |omega|^2 > 0.5*gmax
     as an independent cross-check.
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


def grad(x):
    phi = K @ x; c = np.cos(phi); s = np.sin(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    ov = V @ om
    return -2.0 * (K.T @ (s * ov))


def hessian(x):
    """Corrected Hessian of |omega|^2."""
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


def refine_bfgs(x0):
    res = minimize(lambda y: -omega_sq(y), x0, jac=lambda y: -grad(y),
                   method='L-BFGS-B',
                   options={'gtol': 1e-15, 'ftol': 1e-16, 'maxiter': 5000})
    return res.x


def run_analysis(N):
    print(f"\n>> Grid N = {N}^3", flush=True)
    L = 2.0 * np.pi
    xs = np.linspace(0, L, N, endpoint=False)
    dx = xs[1] - xs[0]
    X1, X2, X3 = np.meshgrid(xs, xs, xs, indexing='ij')
    phi4 = (X1 + X2 + X3) / SQ3
    c1 = np.cos(X1); c2 = np.cos(X2); c3 = np.cos(X3); c4 = np.cos(phi4)
    omx = c3 + c4/SQ2; omy = c1 - c4/SQ2; omz = c2
    osq = omx*omx + omy*omy + omz*omz
    c_arr = np.stack([c1,c2,c3,c4])
    sf = np.zeros_like(osq)
    for j in range(4):
        for k in range(4):
            sf += T_gram[j,k] * c_arr[j] * c_arr[k]
    ratio = np.where(osq > 1e-8, sf/osq, np.nan)

    gmax = float(np.max(osq))
    nbhd = maximum_filter(osq, size=3, mode='wrap')
    mask = (osq == nbhd)
    idx = np.argwhere(mask)
    lmax = [(i,j,k) for (i,j,k) in idx if osq[i,j,k] > 1e-3]
    print(f"   dx = {dx:.5e}", flush=True)
    print(f"   global max |omega|^2 = {gmax:.8f}", flush=True)
    print(f"   # non-trivial grid-level local maxima = {len(lmax)}", flush=True)

    mask_keep = osq > 0.5 * gmax
    print(f"   max ratio over grid cells with |om|^2 > 0.5*gmax: {np.nanmax(ratio[mask_keep]):.8f}", flush=True)

    return xs, osq, sf, ratio, lmax, gmax


def main():
    print("="*75, flush=True)
    print(" t3_realizability_final.py — attempt 855 (N=4 Frobenius T^3 test)", flush=True)
    print(" Test: does any T^3 local max of |omega|^2 have ||S||^2/|omega|^2 >= 9/8?", flush=True)
    print(f" 9/8 = {9.0/8.0:.10f}", flush=True)
    print("="*75, flush=True)

    # N=128 pass
    xs128, osq128, sf128, ratio128, lmax128, gmax128 = run_analysis(128)
    # N=256 pass
    xs256, osq256, sf256, ratio256, lmax256, gmax256 = run_analysis(256)

    # Seeds: all N=256 grid local maxima + neighbors + random
    seeds = []
    for (i,j,k) in lmax256:
        seeds.append(np.array([xs256[i], xs256[j], xs256[k]]))
        # perturb small
        for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            h = xs256[1] - xs256[0]
            seeds.append(np.array([xs256[i]+dx*h*0.3, xs256[j]+dy*h*0.3, xs256[k]+dz*h*0.3]))

    # Plus random seeds biased to high-|omega|^2 regions
    rng = np.random.default_rng(0)
    for _ in range(300):
        seeds.append(2.0 * np.pi * rng.random(3))

    print(f"\n[refine] {len(seeds)} seeds...", flush=True)
    refined = []
    for s in seeds:
        x = refine_bfgs(s)
        refined.append(x)

    # Classify each refined point
    records = []
    for x in refined:
        g = grad(x); gn = float(np.linalg.norm(g))
        om_sq, sf_sq, rat = ratio_at(x)
        H = hessian(x)
        eigs = np.linalg.eigvalsh(H)
        records.append({'x': np.mod(x, 2*np.pi), 'gn': gn,
                        'om_sq': om_sq, 'sf_sq': sf_sq,
                        'ratio': rat, 'eigs': eigs})

    # Dedup (periodic)
    uniq = []
    for r in sorted(records, key=lambda t: -t['om_sq']):
        new = True
        for u in uniq:
            d = np.mod(r['x'] - u['x'] + np.pi, 2*np.pi) - np.pi
            if np.linalg.norm(d) < 5e-3:
                new = False; break
        if new:
            uniq.append(r)

    # Converged (||grad|| small)
    conv = [r for r in uniq if r['gn'] < 1e-4]
    # True local max (Hessian NSD, positive |omega|^2)
    true_max = [r for r in conv if np.max(r['eigs']) <= 1e-5 and r['om_sq'] > 1e-4]
    true_max.sort(key=lambda r: -r['om_sq'])

    print(f"\n[Classification]", flush=True)
    print(f"   unique refined points: {len(uniq)}", flush=True)
    print(f"   converged (||grad|| < 1e-4): {len(conv)}", flush=True)
    print(f"   TRUE maxima (Hessian NSD): {len(true_max)}", flush=True)

    print(f"\n   {'rk':>3} {'x1':>9} {'x2':>9} {'x3':>9} {'|om|^2':>10} {'||S||^2':>10} {'ratio':>10} {'gnorm':>9} {'max_eig':>10}", flush=True)
    for i, r in enumerate(true_max):
        print(f"   {i:3d} {r['x'][0]:9.5f} {r['x'][1]:9.5f} {r['x'][2]:9.5f} "
              f"{r['om_sq']:10.6f} {r['sf_sq']:10.6f} {r['ratio']:10.6f} "
              f"{r['gn']:9.2e} {np.max(r['eigs']):10.2e}", flush=True)

    # Separate: all converged crit points (any type) for reference
    print(f"\n[All converged critical points, for reference]", flush=True)
    conv_sorted = sorted(conv, key=lambda r: -r['om_sq'])
    print(f"   {'rk':>3} {'x1':>9} {'x2':>9} {'x3':>9} {'|om|^2':>10} {'ratio':>10} {'max_eig':>10} {'type':>10}", flush=True)
    for i, r in enumerate(conv_sorted[:40]):
        eig_max = np.max(r['eigs'])
        eig_min = np.min(r['eigs'])
        if eig_max <= 1e-5:
            typ = "max"
        elif eig_min >= -1e-5:
            typ = "min"
        else:
            typ = "saddle"
        print(f"   {i:3d} {r['x'][0]:9.5f} {r['x'][1]:9.5f} {r['x'][2]:9.5f} "
              f"{r['om_sq']:10.6f} {r['ratio']:10.6f} {eig_max:10.2e} {typ:>10}", flush=True)

    print("\n" + "="*75, flush=True)
    if true_max:
        max_rat = max(r['ratio'] for r in true_max)
        max_om = max(r['om_sq'] for r in true_max)
        idx_best = int(np.argmax([r['ratio'] for r in true_max]))
        best = true_max[idx_best]
        print(f" MAX |omega|^2 over TRUE maxima: {max_om:.10f}", flush=True)
        print(f" MAX ratio over TRUE maxima:     {max_rat:.10f}", flush=True)
        print(f" Max-ratio point: x = {best['x']}", flush=True)
        print(f"                  |om|^2 = {best['om_sq']:.6f}, ratio = {best['ratio']:.8f}", flush=True)
        print(f" 9/8 =                           {9.0/8.0:.10f}", flush=True)
        if max_rat >= 9.0/8.0:
            print(" VERDICT: KILL — T^3 max with ratio >= 9/8", flush=True)
        else:
            print(f" VERDICT: CONFIRM — max ratio {max_rat:.6f} < 9/8 (margin {9.0/8.0-max_rat:.6f})", flush=True)
    else:
        print(" VERDICT: INCONCLUSIVE", flush=True)
    print("="*75, flush=True)


if __name__ == "__main__":
    main()
