"""
Attempt 856 — Verify: the T^3 saddle point x* = (2.128, 1.484, 0) from
scan_852_critpoints.py satisfies the 8-var tight system (spheres + AL + FO +
NONDEG) and gives P = -1.1638654, matching the Lasserre SOS bound.

Also: sample ~10^6 T^3 points, compute P(c(x)) and check min.
"""
import numpy as np
import time

SQRT2 = np.sqrt(2.0)

K = np.array([
    [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 0],
], dtype=float)
V = np.array([
    [0, 1, 0], [0, 0, 1], [1, 0, 0], [1.0/SQRT2, -1.0/SQRT2, 0],
])
Mv = V @ V.T
Tmat = np.zeros((4,4))
for j in range(4):
    Tmat[j,j] = 0.5
Tmat[0,3] = -SQRT2/4; Tmat[3,0] = -SQRT2/4
Tmat[2,3] = -SQRT2/4; Tmat[3,2] = -SQRT2/4

def verify_single(xstar):
    c = np.cos(K @ xstar)
    s = np.sin(K @ xstar)
    print(f"x* = {xstar}")
    print(f"c = {c}")
    print(f"s = {s}")
    c1,c2,c3,c4 = c; s1,s2,s3,s4 = s
    # Sphere residuals
    for j in range(4):
        r = c[j]**2 + s[j]**2 - 1
        print(f"  sphere_{j+1}: c^2+s^2-1 = {r:+.2e}")
    # AL residuals
    AL_c = c4 - (c1*c2 - s1*s2)
    AL_s = s4 - (s1*c2 + c1*s2)
    print(f"  AL_c = {AL_c:+.2e},  AL_s = {AL_s:+.2e}")
    # FO residuals
    a1 = c1 - c4/SQRT2
    a2 = c2
    a3 = c3 + c4/SQRT2
    a4 = c4 + (c3 - c1)/SQRT2
    FO1 = s3*a3
    FO2 = s1*a1 - s2*a2
    FO3 = s1*a1 + s4*a4
    print(f"  FO_1 (C1): s_3*a_3       = {FO1:+.2e}")
    print(f"  FO_2 (C2): s_1 a_1 - s_2 a_2 = {FO2:+.2e}")
    print(f"  FO_3 (C3): s_1 a_1 + s_4 a_4 = {FO3:+.2e}")
    # Values
    om2 = c @ Mv @ c
    sf2 = c @ Tmat @ c
    Pv = (5.0/8.0)*(c1**2+c2**2+c3**2+c4**2) + (SQRT2/8.0)*c4*(13*c3 - 5*c1)
    print(f"  |omega|^2 = {om2:.6f}")
    print(f"  ||S||_F^2 = {sf2:.6f}")
    print(f"  ratio     = {sf2/om2:.6f}")
    print(f"  P(c)      = {Pv:+.8f}")
    return Pv

def main():
    t0 = time.time()
    # Exact saddle from scan (to full float64 refinement — use closed-form x)
    # From scan: x1 = 2.127990, x2 = 1.484300, x3 = 0
    xstar = np.array([2.127990, 1.484300, 0.000000])
    print("=== Verifying scan_852 worst-P saddle ===")
    Pv_saddle = verify_single(xstar)

    # Refine this saddle via minimization of ||grad||^2 for higher precision
    from scipy.optimize import minimize
    def omega2_of(x):
        c = np.cos(K @ x)
        return float(c @ Mv @ c)
    def grad_omega2_of(x):
        c = np.cos(K @ x); s = np.sin(K @ x)
        Mvc = Mv @ c
        return -2.0 * (s * Mvc) @ K
    def grn2(x):
        g = grad_omega2_of(x)
        return float(g @ g)
    res = minimize(grn2, xstar, method='L-BFGS-B',
                   options={'ftol':1e-20, 'gtol':1e-18, 'maxiter':10000})
    print(f"\nRefined: x* = {res.x}, ||grad||^2 = {res.fun:.2e}")
    print("=== Refined saddle details ===")
    Pv_refined = verify_single(res.x)

    # ---- Bulk sampling: 10^6 random T^3 points, compute P at each ----
    print("\n=== Bulk sampling 10^6 T^3 points ===")
    np.random.seed(123)
    B = 10**6
    X = np.random.uniform(0, 2*np.pi, size=(B, 3))
    c = np.cos(X @ K.T)
    # P
    c1_,c2_,c3_,c4_ = c[:,0], c[:,1], c[:,2], c[:,3]
    P_bulk = (5.0/8.0)*(c1_**2+c2_**2+c3_**2+c4_**2) + (SQRT2/8.0)*c4_*(13*c3_ - 5*c1_)
    print(f"  P sample min over T^3: {P_bulk.min():+.6f}")
    print(f"  P sample max over T^3: {P_bulk.max():+.6f}")
    print(f"  Quantiles of P (0,5,50,95,100): {np.quantile(P_bulk, [0,0.05,0.5,0.95,1.0])}")
    # The samples don't satisfy FO (generic T^3 points aren't vorticity critical)
    # but they give us the range of P on the (sphere+AL)-set alone.

    # Now sample only the tight set: seed BFGS-refined critical points from many starts.
    # (This is computationally heavy; instead we rely on the 60 critical points found.)
    # Confirmed by scan: min P over T^3 critical points = -1.163865.

    # Check: attempt_854 had min P = -1.3096 on the T^3-detached tight set.
    # With polynomial angle-link (attempt_852 config), min P = -1.163865.
    # So the polynomial angle-link DOES shrink the feasible set (the Lasserre
    # bound moves from -1.3096 to -1.1639) but P is still negative at a saddle.
    print(f"\n  For reference, attempt_854 (no AL): min P = -1.3096")
    print(f"  This attempt (polynomial AL) :    min P = {Pv_refined:+.6f}")
    print(f"  Improvement from AL: {(-1.3096) - Pv_refined:+.4f} (AL shrinks the bound)")

    print(f"\n=== Runtime: {time.time()-t0:.1f}s ===")

if __name__ == '__main__':
    main()
