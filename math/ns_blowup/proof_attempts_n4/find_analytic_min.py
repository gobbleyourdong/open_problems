"""
Find the analytic minimizer of P on the TIGHT N=4 set.
Use scipy.optimize to minimize P subject to E-equalities and sphere equalities as constraints.
"""
import numpy as np
from scipy.optimize import minimize

SQRT2 = np.sqrt(2.0)
SQRT3 = np.sqrt(3.0)

def unpack(x):
    return x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]

def P(x):
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(x)
    cnorm2 = c1*c1 + c2*c2 + c3*c3 + c4*c4
    off_om = SQRT2 * c4 * (c3 - c1)
    omega2 = cnorm2 + off_om
    off_F = (c4/(3*SQRT2))*(-c1+2*c2-c3)
    SF2 = 0.5*cnorm2 + off_F
    return (9/8)*omega2 - SF2

def eqs(x):
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(x)
    a1 = c1 - c4/SQRT2
    a2 = c2
    a3 = c3 + c4/SQRT2
    a4 = c4 + (c3 - c1)/SQRT2
    sph = [c1*c1+s1*s1-1, c2*c2+s2*s2-1, c3*c3+s3*s3-1, c4*c4+s4*s4-1]
    E = [s1*a1 + s4*a4/SQRT3,
         s2*a2 + s4*a4/SQRT3,
         s3*a3 + s4*a4/SQRT3]
    return np.array(sph + E)

def omega2_fn(x):
    c1, c2, c3, c4, _, _, _, _ = unpack(x)
    cnorm2 = c1*c1 + c2*c2 + c3*c3 + c4*c4
    off_om = SQRT2 * c4 * (c3 - c1)
    return cnorm2 + off_om

# Start from the sampler min, then refine with SLSQP
x0s = [
    np.array([-0.998275, -0.017182, 0.998275, -0.997902, 0.0, 1.0, 0.0, 0.0]),  # sampler
    np.array([-1, 0, 1, -1, 0, 1, 0, 0]),  # limit
    np.array([1, 0, -1, 1, 0, 1, 0, 0]),
    np.array([0.9, 0.2, -0.9, 0.9, 0.436, 0.980, -0.436, 0.436]),
]

best = None
for x0 in x0s:
    # normalize sphere
    # (enforce via constraints)
    constraints = [
        {'type': 'eq', 'fun': eqs},
        {'type': 'ineq', 'fun': lambda x: omega2_fn(x) - 1e-3}
    ]
    bounds = [(-1,1)]*4 + [(-1.1, 1.1)]*4
    res = minimize(P, x0, method='SLSQP', constraints=constraints, bounds=bounds,
                   options={'ftol': 1e-14, 'maxiter': 1000})
    r = eqs(res.x)
    if np.max(np.abs(r)) < 1e-7 and omega2_fn(res.x) > 1e-3:
        print(f"P_min = {res.fun:+.10f} at x={res.x}, residual max = {np.max(np.abs(r)):.2e}, |om|^2={omega2_fn(res.x):.5f}")
        if best is None or res.fun < best[0]:
            best = (res.fun, res.x)

if best is not None:
    print(f"\nBest P_min = {best[0]:+.10f}")
    print(f"at x = {best[1]}")
    c1, c2, c3, c4, s1, s2, s3, s4 = unpack(best[1])
    print(f"  (c1,c2,c3,c4) = ({c1:+.8f}, {c2:+.8f}, {c3:+.8f}, {c4:+.8f})")
    print(f"  (s1,s2,s3,s4) = ({s1:+.8f}, {s2:+.8f}, {s3:+.8f}, {s4:+.8f})")
    print(f"  |omega|^2 = {omega2_fn(best[1]):+.8f}")
    r = eqs(best[1])
    print(f"  residuals:")
    print(f"    sphere = {r[0]}, {r[1]}, {r[2]}, {r[3]}")
    print(f"    E = {r[4]}, {r[5]}, {r[6]}")
    # Try rational guesses
    # c1 ≈ -0.9983 ≈ ?,  c2 ≈ -0.0172, c3 ≈ 0.9983, c4 ≈ -0.9979
    # These look like (-1, 0, 1, -1) + small perturbations. Hmm.
