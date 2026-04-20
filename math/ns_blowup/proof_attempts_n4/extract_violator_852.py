"""
Attempt 856 — Extract a concrete violator on the tight system with polynomial
angle-link at attempt_852 configuration, via SLSQP with equality constraints.

Constraints (see sos_polylink_d3.py):
 EQ: 4 spheres, 2 angle-link (AL_c, AL_s), 3 first-order (FO_1, FO_2, FO_3)
 INEQ: |omega|^2 >= 1e-3
Objective: minimize P(c) = (5/8) Sum c_j^2 + (sqrt2/8) c_4 (13 c_3 - 5 c_1).
"""
import numpy as np
from scipy.optimize import minimize, NonlinearConstraint
import time

SQRT2 = np.sqrt(2.0)
EPS_ND = 1e-3

def unpack(z):
    return z[0], z[1], z[2], z[3], z[4], z[5], z[6], z[7]

def a_of(c1, c2, c3, c4):
    a1 = c1 - c4/SQRT2
    a2 = c2
    a3 = c3 + c4/SQRT2
    a4 = c4 + (c3 - c1)/SQRT2
    return a1, a2, a3, a4

def P_val(z):
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(z)
    return (5.0/8.0)*(c1**2+c2**2+c3**2+c4**2) + (SQRT2/8.0)*c4*(13*c3 - 5*c1)

def omega2_val(z):
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(z)
    return c1**2 + c2**2 + c3**2 + c4**2 + SQRT2*c4*(c3 - c1)

def SF2_val(z):
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(z)
    return 0.5*(c1**2+c2**2+c3**2+c4**2) - (SQRT2/2.0)*(c1+c3)*c4

def eq_vec(z):
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(z)
    a1, a2, a3, a4 = a_of(c1, c2, c3, c4)
    return np.array([
        c1*c1 + s1*s1 - 1,   # sphere1
        c2*c2 + s2*s2 - 1,   # sphere2
        c3*c3 + s3*s3 - 1,   # sphere3
        c4*c4 + s4*s4 - 1,   # sphere4  (implied but included)
        c4 - (c1*c2 - s1*s2),   # AL_c
        s4 - (s1*c2 + c1*s2),   # AL_s
        s3*a3,                  # FO1
        s1*a1 - s2*a2,          # FO2
        s1*a1 + s4*a4,          # FO3
    ])

def ineq_vec(z):
    # Must be >= 0
    return np.array([omega2_val(z) - EPS_ND])

def run_slsqp_from(z0):
    from scipy.optimize import minimize
    con_eq = {'type':'eq', 'fun': eq_vec}
    con_ineq = {'type':'ineq', 'fun': ineq_vec}
    res = minimize(P_val, z0, method='SLSQP',
                   constraints=[con_eq, con_ineq],
                   options={'ftol':1e-14, 'maxiter':2000})
    return res

def make_seed_from_xtriple(x1, x2, x3):
    """Seed built from x1, x2, x3 angles and x4 = x1 + x2 (the T3 realization at
    attempt_852 config). This always satisfies all equalities."""
    c1, s1 = np.cos(x1), np.sin(x1)
    c2, s2 = np.cos(x2), np.sin(x2)
    c3, s3 = np.cos(x3), np.sin(x3)
    c4, s4 = np.cos(x1+x2), np.sin(x1+x2)
    return np.array([c1, c2, c3, c4, s1, s2, s3, s4])

def project_to_tight_manifold(z):
    """Project z to nearest point on tight manifold via SLSQP minimization of
    ||z - z0||^2 under the equality + inequality constraints."""
    z0 = z.copy()
    def obj(w):
        return np.sum((w - z0)**2)
    con_eq = {'type':'eq', 'fun': eq_vec}
    con_ineq = {'type':'ineq', 'fun': ineq_vec}
    res = minimize(obj, z0, method='SLSQP',
                   constraints=[con_eq, con_ineq],
                   options={'ftol':1e-14, 'maxiter':2000})
    return res.x, res.success

def main():
    np.random.seed(7)
    best = None
    t0 = time.time()

    # Strategy 1: seeds from random T3 points (guaranteed feasible).
    print("--- Strategy 1: random T^3 seeds (automatically feasible) ---")
    for trial in range(200):
        x1 = np.random.uniform(0, 2*np.pi)
        x2 = np.random.uniform(0, 2*np.pi)
        x3 = np.random.uniform(0, 2*np.pi)
        z0 = make_seed_from_xtriple(x1, x2, x3)
        res = run_slsqp_from(z0)
        if not res.success:
            continue
        z = res.x
        # Check constraint residuals
        eq_resid = np.max(np.abs(eq_vec(z)))
        ineq_ok = ineq_vec(z)[0] >= -1e-8
        if eq_resid > 1e-8 or not ineq_ok:
            continue
        Pv = P_val(z)
        if best is None or Pv < best[0]:
            best = (Pv, z.copy(), eq_resid, x1, x2, x3)
            print(f"  trial {trial}: new best P = {Pv:.6f}, eq_resid = {eq_resid:.2e}, |w|^2={omega2_val(z):.4f}")

    # Strategy 2: seed from d=2 SOS atom suggestion (corner with s2~1, c1,c3,c4 ~ pm 1).
    # From attempt_854's structure, try (c1,c2,c3,c4) near (-1, 0, 1, -1) with various signs.
    print("\n--- Strategy 2: corner-style seeds (attempt_854 pattern) ---")
    corner_seeds = [
        (-0.999, -0.01, +0.999, -0.999, +0.045, +0.9999, -0.045, +0.045),
        (+0.999, +0.01, -0.999, +0.999, -0.045, +0.9999, +0.045, -0.045),
        (-0.99, +0.1, +0.99, -0.99, +0.14, +0.99, -0.14, +0.14),
        (-0.99, -0.1, +0.99, -0.99, +0.14, -0.99, -0.14, +0.14),
        (+0.99, +0.01, +0.99, +1.0, +0.14, +0.99, +0.14, 0.0),
        (-1.0, +0.01, -1.0, +1.0, 0.0, +0.999, 0.0, 0.0),
        (+1.0, 0.0, +1.0, +1.0, 0.0, +1.0, 0.0, 0.0),
        (-0.7, 0.0, +0.7, -0.98, +0.71, +1.0, -0.71, +0.2),
    ]
    for i, seed in enumerate(corner_seeds):
        z0 = np.array(seed)
        # project to tight manifold first
        zp, ok = project_to_tight_manifold(z0)
        if not ok:
            continue
        res = run_slsqp_from(zp)
        if not res.success:
            continue
        z = res.x
        eq_resid = np.max(np.abs(eq_vec(z)))
        ineq_ok = ineq_vec(z)[0] >= -1e-8
        if eq_resid > 1e-8 or not ineq_ok:
            continue
        Pv = P_val(z)
        if best is None or Pv < best[0]:
            best = (Pv, z.copy(), eq_resid, None, None, None)
            print(f"  corner seed {i}: new best P = {Pv:.6f}, eq_resid = {eq_resid:.2e}, |w|^2={omega2_val(z):.4f}")

    # Strategy 3: structured x-grid with x1,x2 on fine grid, x3 from subset.
    print("\n--- Strategy 3: x-grid seeds ---")
    grid = np.linspace(0, 2*np.pi, 32, endpoint=False)
    count = 0
    for x1 in grid[::4]:
        for x2 in grid[::4]:
            for x3 in grid[::4]:
                z0 = make_seed_from_xtriple(x1, x2, x3)
                if omega2_val(z0) < EPS_ND:
                    continue
                res = run_slsqp_from(z0)
                if not res.success:
                    continue
                z = res.x
                eq_resid = np.max(np.abs(eq_vec(z)))
                ineq_ok = ineq_vec(z)[0] >= -1e-8
                if eq_resid > 1e-8 or not ineq_ok:
                    continue
                Pv = P_val(z)
                if best is None or Pv < best[0] - 1e-9:
                    best = (Pv, z.copy(), eq_resid, x1, x2, x3)
                    print(f"  grid ({x1:.3f},{x2:.3f},{x3:.3f}): new best P = {Pv:.6f}, |w|^2={omega2_val(z):.4f}")
                count += 1
    print(f"  grid seeds examined: {count}")

    print(f"\nRuntime: {time.time()-t0:.1f}s")
    if best is None:
        print("No feasible minimizer found.")
        return
    Pbest, zbest, eq_resid, x1, x2, x3 = best
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(zbest)
    print(f"\nBEST VIOLATOR on tight set (spheres + AL + FO + NONDEG):")
    print(f"  P = {Pbest:.8f}")
    print(f"  eq residual max = {eq_resid:.2e}")
    print(f"  |omega|^2 = {omega2_val(zbest):.6f}")
    print(f"  ||S||_F^2 = {SF2_val(zbest):.6f}")
    print(f"  Frobenius ratio ||S||_F^2/|omega|^2 = {SF2_val(zbest)/omega2_val(zbest):.6f}")
    print(f"  9/8 threshold = {9.0/8.0}")
    print(f"  c = ({c1:+.8f}, {c2:+.8f}, {c3:+.8f}, {c4:+.8f})")
    print(f"  s = ({s1:+.8f}, {s2:+.8f}, {s3:+.8f}, {s4:+.8f})")
    if x1 is not None:
        print(f"  seed x-triple = ({x1:.4f}, {x2:.4f}, {x3:.4f})")
    # Save
    np.savez('extract_violator_852_out.npz', z=zbest, P=Pbest, omega2=omega2_val(zbest),
             SF2=SF2_val(zbest))
    print("  saved to extract_violator_852_out.npz")

if __name__ == '__main__':
    main()
