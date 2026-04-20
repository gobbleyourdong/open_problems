"""
Attempt 856 — Scan T^3 for vorticity critical points at attempt_852 configuration
(k4 = (1,1,0)), find all critical points (not just local maxima), classify, and
report P(c) at each.

This tests the tight set with the polynomial angle-link (which IS automatic on
T^3) and the three first-order equations (which are the gradient of |omega|^2).

At attempt_852 config, k4 is integer-lattice so omega IS 2pi-periodic on T^3.

Mapping to 8-variable tight set: for any x in T^3,
  c_j = cos(k_j . x), s_j = sin(k_j . x) satisfies sphere_j + AL_c + AL_s
  automatically. First-order (grad|omega|^2 = 0) gives FO_1, FO_2, FO_3.
  NONDEG |omega|^2 > 0 is a non-degeneracy check.

For each critical point x* (grad = 0) the 8-tuple (c, s) is in the tight set.
So P(c) at x* is a value of P on the tight set.
"""
import numpy as np
from scipy.optimize import minimize
from scipy.ndimage import maximum_filter, minimum_filter
import time

SQRT2 = np.sqrt(2.0)

# Config from attempt_852
K = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
], dtype=float)
V = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
    [1.0/SQRT2, -1.0/SQRT2, 0],
])

# Strain trace matrix T_{jk} = Tr(S_j S_k), from attempt_852 §2:
# Diag 1/2, off-diagonals: (1,4)=(-sqrt2/4), (3,4)=(-sqrt2/4), others 0.
Tmat = np.zeros((4,4))
for j in range(4):
    Tmat[j,j] = 0.5
Tmat[0,3] = -SQRT2/4; Tmat[3,0] = -SQRT2/4
Tmat[2,3] = -SQRT2/4; Tmat[3,2] = -SQRT2/4

# Polarization Gram matrix Mv = V V^T (4x4)
Mv = V @ V.T

def cossin(x):
    kx = K @ x  # length 4
    return np.cos(kx), np.sin(kx)

def omega2(x):
    c, _ = cossin(x)
    return float(c @ Mv @ c)

def omega_vec(x):
    c, _ = cossin(x)
    return c @ V  # sum_j c_j v_j, shape (3,)

def grad_omega2(x):
    c, s = cossin(x)
    # omega = V^T c (as 3-vec), so |omega|^2 = c^T Mv c
    # d/dx_n |omega|^2 = 2 c^T Mv dc/dx_n, dc_j/dx_n = -s_j k_{j,n}
    # => -2 sum_j s_j K[j,n] (Mv c)_j
    Mvc = Mv @ c
    return -2.0 * (s * Mvc) @ K  # shape (3,)

def hess_omega2(x):
    c, s = cossin(x)
    Mvc = Mv @ c
    # H_{nm} = d/dx_m (-2 sum_j s_j K[j,n] (Mv c)_j)
    # = -2 sum_j [ c_j K[j,m] K[j,n] (Mv c)_j + s_j K[j,n] (Mv dc/dx_m)_j ]
    # = -2 sum_j c_j K[j,n] K[j,m] (Mv c)_j
    #   + 2 sum_j sum_l s_j K[j,n] Mv[j,l] s_l K[l,m]
    H = np.zeros((3,3))
    for j in range(4):
        H -= 2.0 * c[j] * Mvc[j] * np.outer(K[j], K[j])
    # second term
    ds = s[:,None] * K  # shape (4,3), ds/dx_m = -s_j K[j,m] but sign below
    # actually: dc_j/dx_m = -s_j K[j,m]; so in "sum_j s_j K[j,n] (Mv dc/dx_m)_j":
    # = sum_j s_j K[j,n] sum_l Mv[j,l] * (-s_l K[l,m]) = -sum_jl s_j Mv[j,l] s_l K[j,n] K[l,m]
    # Multiply by -2 (outer prefactor): +2 sum_jl s_j Mv[j,l] s_l K[j,n] K[l,m]
    H += 2.0 * (K.T @ np.diag(s) @ Mv @ np.diag(s) @ K)
    return H

def SF2(x):
    c, _ = cossin(x)
    return float(c @ Tmat @ c)

def P_at_x(x):
    c, _ = cossin(x)
    c1, c2, c3, c4 = c
    return (5.0/8.0)*(c1**2+c2**2+c3**2+c4**2) + (SQRT2/8.0)*c4*(13*c3 - 5*c1)

def neg_omega2(x):
    return -omega2(x)
def neg_grad(x):
    return -grad_omega2(x)

# For finding saddles / minima too, we use grad norm minimization
def grad_norm_sq(x):
    g = grad_omega2(x)
    return float(g @ g)
def grad_norm_sq_grad(x):
    # d/dx_n (grad^T grad) = 2 grad^T d(grad)/dx_n = 2 (H grad)_n
    g = grad_omega2(x)
    H = hess_omega2(x)
    return 2.0 * H @ g

def main():
    t0 = time.time()
    # ---- Step 1: find all critical points on T^3 ----
    # Grid sample |omega|^2 + its critical points by minimizing ||grad||^2.
    np.random.seed(42)
    N = 64
    grid = np.linspace(0, 2*np.pi, N, endpoint=False)
    X1, X2, X3 = np.meshgrid(grid, grid, grid, indexing='ij')
    pts = np.stack([X1.ravel(), X2.ravel(), X3.ravel()], axis=1)
    print(f"Grid: {len(pts)} points")

    # compute omega^2 and grad_norm_sq at all points (vectorized)
    c = np.cos(pts @ K.T)   # (N^3, 4)
    s = np.sin(pts @ K.T)
    om2 = np.einsum('ij,jk,ik->i', c, Mv, c)
    Mvc = c @ Mv.T   # (N^3, 4); Mv is symmetric so same as c @ Mv
    # grad_n = -2 sum_j s_{ij} K[j,n] Mvc_{ij}
    gr = -2.0 * np.einsum('ij,ij,jn->in', s, Mvc, K)
    grn2 = np.einsum('in,in->i', gr, gr)
    print(f"Grid omega^2 range: [{om2.min():.4f}, {om2.max():.4f}]")
    print(f"Grid ||grad||^2 range: [{grn2.min():.4f}, {grn2.max():.4f}]")

    # ---- Step 2: refine seeds via grad=0 ----
    # Seed candidates: small ||grad|| grid points + random seeds
    thr_idx = np.argsort(grn2)[:3000]
    seeds = pts[thr_idx]
    # Plus 500 random extra
    extras = np.random.uniform(0, 2*np.pi, size=(500,3))
    seeds = np.vstack([seeds, extras])
    print(f"Seed candidates: {len(seeds)}")

    # Refine each seed by minimizing grad_norm_sq to find critical points
    critpts = []
    for i, s0 in enumerate(seeds):
        res = minimize(grad_norm_sq, s0, jac=grad_norm_sq_grad,
                       method='L-BFGS-B',
                       options={'ftol':1e-18, 'gtol':1e-14, 'maxiter':500})
        x = res.x % (2*np.pi)
        gn = np.sqrt(grad_norm_sq(x))
        if gn > 1e-6:
            continue
        critpts.append(x)

    critpts = np.array(critpts)
    print(f"Refined critical points: {len(critpts)}")

    # Deduplicate
    unique = []
    for x in critpts:
        isdup = False
        for y in unique:
            d = np.linalg.norm(((x - y + np.pi) % (2*np.pi)) - np.pi)
            if d < 1e-4:
                isdup = True; break
        if not isdup:
            unique.append(x)
    unique = np.array(unique)
    print(f"Unique critical points: {len(unique)}")

    # ---- Step 3: classify and report ----
    records = []
    for x in unique:
        H = hess_omega2(x)
        evals = np.linalg.eigvalsh(H)
        o2 = omega2(x)
        sf2 = SF2(x)
        ratio = sf2/o2 if o2 > 1e-12 else float('inf')
        Pv = P_at_x(x)
        maxeig = evals.max()
        mineig = evals.min()
        classification = 'max' if maxeig <= 1e-6 else ('min' if mineig >= -1e-6 else 'saddle')
        records.append((x, o2, sf2, ratio, Pv, evals, classification))

    # Sort by P ascending (most-violating first)
    records.sort(key=lambda r: r[4])
    print(f"\n== All critical points sorted by P (ascending) ==")
    print(f"{'x1':>8} {'x2':>8} {'x3':>8} {'|om|^2':>10} {'||S||_F^2':>10} {'ratio':>10} {'P':>10}  Hess_eigvals          class")
    for x, o2, sf2, ratio, Pv, evals, cls in records:
        print(f"{x[0]:8.4f} {x[1]:8.4f} {x[2]:8.4f} {o2:10.5f} {sf2:10.5f} {ratio:10.5f} {Pv:+10.5f}  [{evals[0]:+.3f} {evals[1]:+.3f} {evals[2]:+.3f}]  {cls}")

    # Subset: true local maxima (all H eigenvalues <= 0, strictly less for max of |omega|^2)
    max_records = [r for r in records if r[6] == 'max' and r[1] > 1e-6]
    print(f"\n== True local maxima of |omega|^2 (ratio ranked) ==")
    print(f"count = {len(max_records)}")
    if max_records:
        maxratio = max(r[3] for r in max_records)
        maxP_min = min(r[4] for r in max_records)
        maxP_max = max(r[4] for r in max_records)
        print(f"Max ratio over true maxima: {maxratio:.6f}")
        print(f"Min P over true maxima:    {maxP_min:+.6f}")
        print(f"Max P over true maxima:    {maxP_max:+.6f}")

    # Minimum P over ALL critical points (not just maxima)
    minP_all = min(r[4] for r in records)
    maxR_all = max(r[3] for r in records)
    print(f"\n== Minimum P over ALL critical points (incl. saddles) ==")
    print(f"Min P = {minP_all:+.6f}   (Lasserre bound: -1.16386)")
    print(f"Max Frobenius ratio over all crit points = {maxR_all:.4f}  (target: < 9/8 = 1.125)")

    # Worst critical point
    worst = records[0]
    x, o2, sf2, ratio, Pv, evals, cls = worst
    print(f"\nWorst-P critical point:")
    print(f"  x = ({x[0]:.6f}, {x[1]:.6f}, {x[2]:.6f})")
    print(f"  |omega|^2 = {o2:.6f}")
    print(f"  ||S||_F^2 = {sf2:.6f}")
    print(f"  ratio = {ratio:.6f}")
    print(f"  P = {Pv:+.6f}")
    print(f"  H eigenvalues = {evals}")
    print(f"  class = {cls}")
    c, s = cossin(x)
    print(f"  c = ({c[0]:+.6f}, {c[1]:+.6f}, {c[2]:+.6f}, {c[3]:+.6f})")
    print(f"  s = ({s[0]:+.6f}, {s[1]:+.6f}, {s[2]:+.6f}, {s[3]:+.6f})")

    print(f"\nRuntime: {time.time()-t0:.1f}s")

    # Save data
    np.savez('scan_852_critpoints.npz',
             critpts=np.array([r[0] for r in records]),
             om2=np.array([r[1] for r in records]),
             sf2=np.array([r[2] for r in records]),
             ratios=np.array([r[3] for r in records]),
             P=np.array([r[4] for r in records]))

if __name__ == '__main__':
    main()
