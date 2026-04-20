"""
Numerical sampling on the TIGHT N=4 set.

Tight set in (c1,c2,c3,c4):
  Q1 := (1-c1^2)(c1 - c4/sqrt2)^2
  Q2 := (1-c2^2) c2^2
  Q3 := (1-c3^2)(c3 + c4/sqrt2)^2
  Q4 := (1/3)(1-c4^2)(c4 + (c3-c1)/sqrt2)^2
must satisfy Q1 = Q2 = Q3 = Q4 (three equalities).

Vorticity nondegeneracy:
  |omega|^2 = c1^2 + c2^2 + c3^2 + c4^2 + sqrt2 c4 (c3 - c1)  >  eps_nondeg

Target nonnegativity to test:
  P(c) = (9/8) |omega|^2 - ||S||_F^2,  with ||S||_F^2 = 0.5||c||^2 + (c4/(3 sqrt2))(-c1+2c2-c3)

We sample by:
  Strategy A: fix a grid (c2, c4), set lambda^2 = (1-c2^2) c2^2; solve j=1 and j=3 quartics
              in c1, c3 via numpy roots; then check j=4 arm Q4 = lambda^2 and NONDEG.
  Strategy B: fix (c1, c2, c3, c4) randomly; use scipy root (hybrid/lm) to project.

We use both. A gives structured coverage; B gives random coverage. Vectorize A.
"""
import numpy as np
import time
import sys

SQRT2 = np.sqrt(2.0)
SQRT3 = np.sqrt(3.0)
TOL   = 1e-10
EPS_ND = 1e-3

def P_target(c1, c2, c3, c4):
    cnorm2 = c1*c1 + c2*c2 + c3*c3 + c4*c4
    off_omega = SQRT2 * c4 * (c3 - c1)
    omega2 = cnorm2 + off_omega
    off_F = (c4 / (3*SQRT2)) * (-c1 + 2*c2 - c3)
    SF2 = 0.5 * cnorm2 + off_F
    return (9.0/8.0)*omega2 - SF2, omega2

def Q_values(c1, c2, c3, c4):
    a1 = c1 - c4/SQRT2
    a2 = c2
    a3 = c3 + c4/SQRT2
    a4 = c4 + (c3 - c1)/SQRT2
    Q1 = (1 - c1*c1) * a1*a1
    Q2 = (1 - c2*c2) * a2*a2
    Q3 = (1 - c3*c3) * a3*a3
    Q4 = (1/3.0) * (1 - c4*c4) * a4*a4
    return Q1, Q2, Q3, Q4

def solve_quartic_for_c(lam2, offset):
    """
    Solve (1 - c^2)*(c - offset)^2 = lam2 for real c in [-1,1].
    Expand: (1-c^2)(c-offset)^2 = lam2.
      Let u = c - offset, so c = u + offset, 1 - c^2 = 1 - (u+offset)^2.
      = (1 - (u+offset)^2) * u^2 = lam2.
    Or directly:
      (c^2 - 1)(c - offset)^2 + lam2 = 0
    Degree 4 polynomial in c: expand (c^2-1)(c-offset)^2 = (c^2-1)(c^2 - 2*offset c + offset^2)
      = c^4 - 2 offset c^3 + offset^2 c^2 - c^2 + 2 offset c - offset^2
      = c^4 - 2 offset c^3 + (offset^2 - 1) c^2 + 2 offset c - offset^2
    So (c^2-1)(c-offset)^2 + lam2 = c^4 - 2 offset c^3 + (offset^2-1) c^2 + 2 offset c - offset^2 + lam2
    We want the negated polynomial = 0:
      (1-c^2)(c-offset)^2 - lam2 = -c^4 + 2 offset c^3 - (offset^2-1) c^2 - 2 offset c + offset^2 - lam2
    Equivalently multiply by -1:
      c^4 - 2 offset c^3 + (offset^2 - 1) c^2 + 2 offset c - offset^2 + lam2 = 0.
    Return real roots in [-1, 1].
    """
    coefs = np.array([1.0, -2*offset, offset*offset - 1, 2*offset, -offset*offset + lam2])
    roots = np.roots(coefs)
    real_roots = [r.real for r in roots if abs(r.imag) < 1e-9]
    # in-box
    in_box = [r for r in real_roots if -1.0 - 1e-9 <= r <= 1.0 + 1e-9]
    in_box = [np.clip(r, -1.0, 1.0) for r in in_box]
    return in_box

def sample_tight_structured(nc2=400, nc4=400):
    """Grid sweep over (c2, c4)."""
    c2s = np.linspace(-1+1e-4, 1-1e-4, nc2)
    c4s = np.linspace(-1+1e-4, 1-1e-4, nc4)
    points = []
    for c2 in c2s:
        lam2 = (1 - c2*c2) * c2*c2
        # lam2 ∈ [0, 1/4]
        for c4 in c4s:
            # Solve j=1: (1-c1^2)(c1 - c4/sqrt2)^2 = lam2
            c1s = solve_quartic_for_c(lam2, c4/SQRT2)
            # Solve j=3: (1-c3^2)(c3 + c4/sqrt2)^2 = lam2
            c3s = solve_quartic_for_c(lam2, -c4/SQRT2)
            for c1 in c1s:
                for c3 in c3s:
                    # Check Q4 = lam2, i.e., (1/3)(1-c4^2)(c4 + (c3-c1)/sqrt2)^2 == lam2
                    a4 = c4 + (c3 - c1)/SQRT2
                    Q4 = (1/3.0)*(1 - c4*c4)*a4*a4
                    resid = Q4 - lam2
                    # We accept only if resid ~ 0 (else this lam2 is inconsistent with j=4 arm).
                    # Since lam2 is a continuous parameter and the constraint is 1D in lam2,
                    # the set Q4 = lam2 is a codim-1 subset. We track residual for later filtering.
                    points.append((c1, c2, c3, c4, resid))
    pts = np.array(points)
    return pts

def sample_tight_random(n_seeds, rng):
    """
    Start from random (c1,c2,c3,c4) and drive to the tight set via 1D parametrization.
    We choose to let c2 and c4 be free, compute lam2 = Q2 = (1-c2^2)c2^2,
    then pick c1 and c3 from the set of quartic roots matching lam2 (with j=1, j=3 offsets),
    then check residual r = Q4 - lam2 (acceptance).
    """
    c2s = rng.uniform(-1+1e-4, 1-1e-4, n_seeds)
    c4s = rng.uniform(-1+1e-4, 1-1e-4, n_seeds)
    points = []
    for c2, c4 in zip(c2s, c4s):
        lam2 = (1 - c2*c2) * c2*c2
        c1s = solve_quartic_for_c(lam2, c4/SQRT2)
        c3s = solve_quartic_for_c(lam2, -c4/SQRT2)
        for c1 in c1s:
            for c3 in c3s:
                a4 = c4 + (c3 - c1)/SQRT2
                Q4 = (1/3.0)*(1 - c4*c4)*a4*a4
                resid = Q4 - lam2
                points.append((c1, c2, c3, c4, resid))
    return np.array(points) if points else np.zeros((0,5))

def refine_on_tight_subset(seeds, rng, n_iter=200, step=0.01):
    """Given seed points nearly on the tight set (small Q4-lam2 residual),
    locally search the c4 direction to reduce the residual to ~0.
    We adjust c4 via Newton: fix (c2, lam2, c1, c3), vary c4; residual(c4) = Q4 - lam2.
    """
    refined = []
    for seed in seeds:
        c1, c2, c3, c4, _ = seed
        lam2 = (1 - c2*c2) * c2*c2
        for _ in range(n_iter):
            a4 = c4 + (c3 - c1)/SQRT2
            Q4 = (1/3.0)*(1 - c4*c4)*a4*a4
            r = Q4 - lam2
            if abs(r) < 1e-10:
                break
            dQ4_dc4 = (1/3.0) * ((-2*c4)*a4*a4 + (1 - c4*c4)*2*a4)
            if abs(dQ4_dc4) < 1e-14:
                break
            dc4 = r / dQ4_dc4
            c4_new = c4 - dc4
            if abs(c4_new) > 1.0:
                break
            # Recompute c1, c3 since they depend on c4; re-project via quartic:
            c4 = c4_new
            # update c1, c3 by picking the closest root
            c1s = solve_quartic_for_c(lam2, c4/SQRT2)
            c3s = solve_quartic_for_c(lam2, -c4/SQRT2)
            if not c1s or not c3s:
                break
            c1 = min(c1s, key=lambda x: abs(x - c1))
            c3 = min(c3s, key=lambda x: abs(x - c3))
        # final residual
        a4 = c4 + (c3 - c1)/SQRT2
        Q4 = (1/3.0)*(1 - c4*c4)*a4*a4
        r = Q4 - lam2
        if abs(r) < 1e-8:
            refined.append((c1, c2, c3, c4))
    return np.array(refined) if refined else np.zeros((0,4))

def main():
    rng = np.random.default_rng(42)
    t0 = time.time()

    # ---- 1. Structured grid sweep (c2, c4), just collect with residual ----
    print("Structured grid sweep over (c2, c4) with nc2=nc4=300...")
    sys.stdout.flush()
    pts_struct = sample_tight_structured(nc2=300, nc4=300)
    print(f"  {len(pts_struct)} raw (c1,c2,c3,c4) points (from quartic roots)")
    # Filter by residual small enough
    mask = np.abs(pts_struct[:,4]) < 1e-4
    near_tight = pts_struct[mask, :4]
    print(f"  {len(near_tight)} points with |Q4-lam2| < 1e-4")

    # ---- 2. Refine (via Newton on c4) ----
    print("Refining near-tight points via Newton on c4...")
    sys.stdout.flush()
    # Refine a subset to avoid excessive runtime
    max_refine = min(len(near_tight), 50000)
    refined = []
    for seed in near_tight[:max_refine]:
        c1, c2, c3, c4 = seed
        lam2 = (1 - c2*c2) * c2*c2
        success = True
        for _ in range(50):
            a4 = c4 + (c3 - c1)/SQRT2
            Q4 = (1/3.0)*(1 - c4*c4)*a4*a4
            r = Q4 - lam2
            if abs(r) < 1e-10:
                break
            # Newton in c4
            dQ4_dc4 = (1/3.0) * ((-2*c4)*a4*a4 + (1 - c4*c4)*2*a4)
            if abs(dQ4_dc4) < 1e-14:
                success = False
                break
            c4_new = c4 - r / dQ4_dc4
            if abs(c4_new) > 1.0 - 1e-12:
                success = False
                break
            c4 = c4_new
            c1s_list = solve_quartic_for_c(lam2, c4/SQRT2)
            c3s_list = solve_quartic_for_c(lam2, -c4/SQRT2)
            if not c1s_list or not c3s_list:
                success = False; break
            c1 = min(c1s_list, key=lambda x: abs(x - c1))
            c3 = min(c3s_list, key=lambda x: abs(x - c3))
        a4 = c4 + (c3 - c1)/SQRT2
        Q4 = (1/3.0)*(1 - c4*c4)*a4*a4
        r = Q4 - lam2
        if abs(r) < 1e-7 and success:
            refined.append((c1, c2, c3, c4))
    refined = np.array(refined) if refined else np.zeros((0,4))
    print(f"  {len(refined)} refined tight-set points (|Q4-lam2| < 1e-7)")

    # ---- 3. Random-seed sampling ----
    print("Random-seed sampling (N=200000 c2,c4 seeds)...")
    sys.stdout.flush()
    pts_rnd = sample_tight_random(200000, rng)
    mask_r = np.abs(pts_rnd[:,4]) < 1e-4
    near_tight_r = pts_rnd[mask_r, :4]
    print(f"  {len(near_tight_r)} near-tight points from random seeds")

    # Combine all (near)-tight points (may have residual up to 1e-4 → drop later)
    all_pts = np.concatenate([refined, near_tight_r], axis=0) if len(refined) > 0 else near_tight_r

    # Compute P and filter NONDEG
    Pvals = []
    kept = []
    for c1, c2, c3, c4 in all_pts:
        Pv, om2 = P_target(c1, c2, c3, c4)
        if om2 >= EPS_ND:
            Pvals.append(Pv)
            kept.append((c1, c2, c3, c4, om2))
    Pvals = np.array(Pvals)
    kept = np.array(kept)
    t1 = time.time()
    print(f"\nTotal tight-set points kept (|omega|^2 >= {EPS_ND}): {len(Pvals)}")
    print(f"Runtime: {t1-t0:.1f}s")

    if len(Pvals) > 0:
        print(f"\nmin P observed: {Pvals.min():+.6f}")
        imin = np.argmin(Pvals)
        c1, c2, c3, c4, om2 = kept[imin]
        print(f"  at (c1,c2,c3,c4) = ({c1:+.6f}, {c2:+.6f}, {c3:+.6f}, {c4:+.6f})")
        print(f"  |omega|^2 = {om2:+.6f}")
        r = Q_values(c1, c2, c3, c4)
        print(f"  Q1..Q4 = {r}  (should be all equal on tight set)")
        q = np.quantile(Pvals, [0.0, 0.001, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 1.0])
        print(f"  P quantiles: {dict(zip(['0%','0.1%','1%','5%','25%','50%','75%','95%','99%','100%'], np.round(q, 5)))}")
        print(f"  fraction with P<0: {(Pvals<0).sum()}/{len(Pvals)} = {100*(Pvals<0).mean():.2f}%")
        print(f"  min Frobenius ratio: ||S||^2/|omega|^2 max?")
        # Compute ratio
        ratios = []
        for row in kept:
            c1, c2, c3, c4, om2 = row
            cnorm2 = c1**2+c2**2+c3**2+c4**2
            off_F = (c4/(3*SQRT2))*(-c1+2*c2-c3)
            SF2 = 0.5*cnorm2 + off_F
            ratios.append(SF2 / om2)
        ratios = np.array(ratios)
        print(f"  max ||S||^2/|omega|^2 over tight set: {ratios.max():.4f}  (target < 9/8 = 1.125)")
        print(f"  fraction with ratio >= 9/8: {(ratios >= 9/8).sum()}/{len(ratios)} = {100*(ratios>=9/8).mean():.2f}%")

        # Report top-10 worst P points
        idx_sorted = np.argsort(Pvals)
        print(f"\n  Worst-10 (smallest P) points on tight set:")
        for k in range(min(10, len(Pvals))):
            i = idx_sorted[k]
            c1, c2, c3, c4, om2 = kept[i]
            Pv = Pvals[i]
            print(f"    P={Pv:+.5f}, |om|^2={om2:+.4f}, c=({c1:+.4f}, {c2:+.4f}, {c3:+.4f}, {c4:+.4f})")

if __name__ == '__main__':
    main()
