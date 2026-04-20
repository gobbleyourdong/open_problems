"""
Refine the sampled violator via local minimization (SLSQP). The Lasserre relaxation
says min_S P = -1.395869, and the moment matrix has rank 2 (two atoms +/-x). We seek
the explicit (a,b,c2,c4) achieving this minimum.
"""
import numpy as np
from scipy.optimize import minimize

SQRT2 = np.sqrt(2.0)

def P(x):
    a,b,c2,c4 = x
    return (5.0/8.0)*(a*a+b*b+c2*c2) - (SQRT2/3.0)*c4*(a+c2-2*b) - c4*c4

def gradP(x):
    a,b,c2,c4 = x
    return np.array([
        (5/4)*a - (SQRT2/3)*c4,
        (5/4)*b + (SQRT2*2/3)*c4,
        (5/4)*c2 - (SQRT2/3)*c4,
        -2*c4 - (SQRT2/3)*(a+c2-2*b)
    ])

# Constraints as g(x) >= 0
def c_box1(x):
    a,b,c2,c4 = x
    return 1.0 - (a + c4/SQRT2)**2
def c_box2(x):
    a,b,c2,c4 = x
    return 1.0 - (b - c4/SQRT2)**2
def c_box3(x):
    a,b,c2,c4 = x
    return 1.0 - c2**2
def c_box4(x):
    a,b,c2,c4 = x
    return 1.0 - c4**2
def c_F1(x):
    a,b,c2,c4 = x
    c1 = a + c4/SQRT2
    return 0.25 - (1 - c1*c1) * a*a
def c_F3(x):
    a,b,c2,c4 = x
    c3 = b - c4/SQRT2
    return 0.25 - (1 - c3*c3) * b*b
def c_F(x):
    a,b,c2,c4 = x
    return 1.5 - (1 - c4*c4)*(b - a)**2
def c_ND(x):
    a,b,c2,c4 = x
    return a*a + b*b + c2*c2 + 2*c4*c4 + SQRT2*c4*(a-b) - 1e-6

constraints = [
    {'type':'ineq','fun':c_box1},
    {'type':'ineq','fun':c_box2},
    {'type':'ineq','fun':c_box3},
    {'type':'ineq','fun':c_box4},
    {'type':'ineq','fun':c_F1},
    {'type':'ineq','fun':c_F3},
    {'type':'ineq','fun':c_F},
    {'type':'ineq','fun':c_ND},
]

best = None
best_val = np.inf
rng = np.random.default_rng(20260419)
for trial in range(200):
    x0 = rng.uniform(-0.8, 0.8, 4)
    # fine-tune c4 corner (violators tend to be c4 near +/-1)
    x0[3] = np.sign(rng.uniform(-1,1)) * rng.uniform(0.85, 0.995)
    try:
        res = minimize(P, x0, jac=gradP, method='SLSQP',
                       constraints=constraints,
                       options={'maxiter':500, 'ftol':1e-12})
        if res.success and res.fun < best_val:
            # Double-check feasibility
            feas = all(c['fun'](res.x) >= -1e-8 for c in constraints)
            if feas:
                best = res.x.copy()
                best_val = res.fun
    except Exception:
        pass

print(f"Best (a,b,c2,c4) found: {best}")
print(f"P at best = {best_val:.8f}")
print(f"(Lasserre d=2 lower bound was -1.395866; d=3 was -1.395869)")

if best is not None:
    a_s, b_s, c2_s, c4_s = best
    c1_s = a_s + c4_s/SQRT2
    c3_s = b_s - c4_s/SQRT2
    print(f"\n(c1, c2, c3, c4) = ({c1_s:.6f}, {c2_s:.6f}, {c3_s:.6f}, {c4_s:.6f})")
    print(f"Constraint slack values (all should be >= 0):")
    names = ['box1','box2','box3','box4','F1p','F3p','Fp','ND']
    for n, c in zip(names, constraints):
        print(f"  {n}: {c['fun'](best):+.8f}")
    # Frobenius ratio at this c-vector
    # S = c1 S1 + c2 S2 + c3 S3 + c4 S4
    S1 = -0.5 * np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=float)
    S2 = -0.5 * np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=float)
    S3 = -0.5 * np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=float)
    M = np.array([[2,2,-1],[2,2,-1],[-1,-1,-4]], dtype=float)
    S4 = -(1.0/(2.0*np.sqrt(18.0))) * M
    v1 = np.array([0,1,0], dtype=float)
    v2 = np.array([0,0,1], dtype=float)
    v3 = np.array([1,0,0], dtype=float)
    v4 = np.array([1,-1,0], dtype=float) / SQRT2
    S = c1_s*S1 + c2_s*S2 + c3_s*S3 + c4_s*S4
    om = c1_s*v1 + c2_s*v2 + c3_s*v3 + c4_s*v4
    F2 = np.sum(S*S)
    OM2 = float(om @ om)
    print(f"\nDirect matrix computation:")
    print(f"  ||S||_F^2 = {F2:.6f}")
    print(f"  |omega|^2 = {OM2:.6f}")
    if OM2 > 0:
        print(f"  Frobenius ratio ||S||_F^2 / |omega|^2 = {F2/OM2:.6f}")
        print(f"  Target (9/8) = {9/8:.6f}")
        print(f"  Excess over target: {F2/OM2 - 9/8:.6f}")
