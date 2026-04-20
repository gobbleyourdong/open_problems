"""
Verify a candidate violator of (R*) against the full N=4 setup in attempt_851:
the 4-mode k-configuration, the CONSTRAINT Sum_j s_j (omega.v_j) k_j = 0, and
the Frobenius ratio ||S||_F^2 / |omega|^2.

The violator's c's should correspond to a FEASIBLE critical point (vorticity max)
up to the box/constraint relaxation. We verify three things:
  (a) The reduction (a,b,c2,c4) -> (c1,c2,c3,c4) is consistent.
  (b) The polynomial (R*) = (5/8)(a^2+b^2+c2^2) - (sqrt2/3)c4(a+c2-2b) - c4^2
      equals the original (TARGET) LHS - RHS up to sign conventions.
  (c) Independent computation of ||S||_F^2 and |omega|^2 at these c's using
      the explicit S_j and v_j matrices, and verification that the ratio
      exceeds 9/8 at the violator (since R* < 0 means ||S||_F^2 > (9/8)|omega|^2).
"""
import numpy as np

SQRT2 = np.sqrt(2.0)
SQRT3 = np.sqrt(3.0)
SQRT6 = np.sqrt(6.0)

# --- Exact S_j matrices from attempt_851 Sec (ii) ---
S1 = -0.5 * np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=float)
S2 = -0.5 * np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=float)
S3 = -0.5 * np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=float)
# S4 = -(1/(2 sqrt(18))) * M  where M =
M = np.array([[2,2,-1],[2,2,-1],[-1,-1,-4]], dtype=float)
S4 = -(1.0/(2.0*np.sqrt(18.0))) * M

# v_j
v1 = np.array([0,1,0], dtype=float)
v2 = np.array([0,0,1], dtype=float)
v3 = np.array([1,0,0], dtype=float)
v4 = np.array([1,-1,0], dtype=float) / SQRT2

# --- Sanity checks: Tr(S_j^2) = 1/2 each ---
for i, Sj in enumerate([S1,S2,S3,S4], 1):
    tr = np.trace(Sj @ Sj)
    print(f"Tr(S{i}^2) = {tr:.6f}  (expect 0.5)")

# --- Tabulate tau_jk, mu_jk ---
Ss = [S1,S2,S3,S4]
vs = [v1,v2,v3,v4]
print("\ntau[j,k] = Tr(S_j S_k):")
for j in range(4):
    for k in range(j+1,4):
        tau = np.trace(Ss[j] @ Ss[k])
        print(f"  tau[{j+1},{k+1}] = {tau:+.6f}  (1/(6 sqrt2) = {1.0/(6.0*SQRT2):+.6f}, 1/(3 sqrt2) = {1.0/(3.0*SQRT2):+.6f})")

print("\nmu[j,k] = v_j . v_k:")
for j in range(4):
    for k in range(j+1,4):
        mu = vs[j] @ vs[k]
        print(f"  mu[{j+1},{k+1}] = {mu:+.6f}  (+-1/sqrt2 = {1.0/SQRT2:.6f})")

def frobenius_and_omega(c):
    """Given c = (c1,c2,c3,c4), compute ||S||_F^2 and |omega|^2 at x* using
    the explicit S_j matrices. S = sum c_j S_j, omega = sum c_j v_j."""
    c1,c2,c3,c4 = c
    S = c1*S1 + c2*S2 + c3*S3 + c4*S4
    omega = c1*v1 + c2*v2 + c3*v3 + c4*v4
    return np.sum(S*S), float(omega @ omega)

def polynomial_R_star(a,b,c2,c4):
    """Return LHS - RHS of R*:  (5/8)(a^2+b^2+c2^2) - (sqrt2/3)c4(a+c2-2b) - c4^2."""
    return (5.0/8.0)*(a*a+b*b+c2*c2) - (SQRT2/3.0)*c4*(a+c2-2*b) - c4*c4

def feasibility(a,b,c2,c4):
    c1 = a + c4/SQRT2
    c3 = b - c4/SQRT2
    info = {}
    info['c1'] = c1; info['c3'] = c3
    info['box_c1'] = abs(c1) <= 1.0 + 1e-9
    info['box_c2'] = abs(c2) <= 1.0 + 1e-9
    info['box_c3'] = abs(c3) <= 1.0 + 1e-9
    info['box_c4'] = abs(c4) <= 1.0 + 1e-9
    info['F1p'] = (1.0 - c1*c1)*a*a
    info['F3p'] = (1.0 - c3*c3)*b*b
    info['Fp']  = (1.0 - c4*c4)*(b-a)**2
    info['F1p_ok'] = info['F1p'] <= 0.25 + 1e-9
    info['F3p_ok'] = info['F3p'] <= 0.25 + 1e-9
    info['Fp_ok']  = info['Fp']  <= 1.5  + 1e-9
    info['ND'] = a*a + b*b + c2*c2 + 2*c4*c4 + SQRT2*c4*(a-b)
    info['ND_ok'] = info['ND'] > 0
    return info

# --- Check the deepest violator ---
print("\n" + "="*70)
print("VERIFYING DEEPEST SAMPLED VIOLATOR")
print("="*70)
violator = (-0.187653, 0.291851, -0.392914, -0.996193)
a,b,c2,c4 = violator
info = feasibility(a,b,c2,c4)
print(f"(a,b,c2,c4) = {violator}")
print(f"  c1 = {info['c1']:.6f}, c3 = {info['c3']:.6f}")
print(f"  box:  c1 in [-1,1]? {info['box_c1']}, c2? {info['box_c2']}, c3? {info['box_c3']}, c4? {info['box_c4']}")
print(f"  (F1'): (1-c1^2)*a^2 = {info['F1p']:.6f} <= 1/4? {info['F1p_ok']}")
print(f"  (F3'): (1-c3^2)*b^2 = {info['F3p']:.6f} <= 1/4? {info['F3p_ok']}")
print(f"  (F'):  (1-c4^2)*(b-a)^2 = {info['Fp']:.6f} <= 3/2? {info['Fp_ok']}")
print(f"  (NON-DEG): a^2+b^2+c2^2+2c4^2+sqrt2*c4*(a-b) = {info['ND']:.6f} > 0? {info['ND_ok']}")
P = polynomial_R_star(a,b,c2,c4)
print(f"  P(a,b,c2,c4) = {P:.6f}   (R* claims P >= 0; violator has P < 0)")

c1 = a + c4/SQRT2
c3 = b - c4/SQRT2
F2_F, OM2 = frobenius_and_omega((c1,c2,c3,c4))
print(f"\n  Direct matrix check:")
print(f"    ||S||_F^2 = {F2_F:.6f}")
print(f"    |omega|^2 = {OM2:.6f}")
if OM2 > 0:
    print(f"    ratio    = {F2_F/OM2:.6f}    (target: < 9/8 = {9.0/8.0:.6f})")
    print(f"    violation margin: ratio - 9/8 = {F2_F/OM2 - 9.0/8.0:.6f}")

# Also cross-check via the algebraic forms (TARGET)
# TARGET: off_F - (9/8) off_omega < (5/8) sum c_j^2
# With off_F = (c4/(3 sqrt2)) * (-c1 + 2 c2 - c3)
# And off_omega = sqrt2 * c4 * (c3 - c1)
sum_c2 = c1*c1 + c2*c2 + c3*c3 + c4*c4
off_F = (c4/(3.0*SQRT2)) * (-c1 + 2*c2 - c3)
off_omega = SQRT2 * c4 * (c3 - c1)
LHS_target = off_F - (9.0/8.0)*off_omega
RHS_target = (5.0/8.0)*sum_c2
print(f"\n  Via algebraic forms:")
print(f"    off_F      = {off_F:.6f}")
print(f"    off_omega  = {off_omega:.6f}")
print(f"    sum c_j^2  = {sum_c2:.6f}")
print(f"    LHS of TARGET = off_F - (9/8) off_omega = {LHS_target:.6f}")
print(f"    RHS of TARGET = (5/8) sum c_j^2          = {RHS_target:.6f}")
print(f"    TARGET says LHS < RHS; here LHS - RHS = {LHS_target - RHS_target:.6f}")
print(f"    (note: R* = RHS - LHS = {RHS_target - LHS_target:.6f} = P above)")

# --- Verify the vorticity-max CONSTRAINT: check if this c-vector corresponds
# to a real x* on T^3 that satisfies sum_j s_j (omega.v_j) k_j = 0.
#
# The sampling uses the relaxation (F1'), (F3'), (F') which EXPANDS the
# feasible set beyond the actual critical manifold. So the violator may not
# live on the real manifold. We check:
print("\n  CRITICAL POINT (first-order) check:")
# omega.v_j
omv1 = c1 - c4/SQRT2  # = a
omv2 = c2
omv3 = c3 + c4/SQRT2  # = b
omv4 = c4 + (c3 - c1)/SQRT2  # = c4 - (a-b+sqrt2*c4)/sqrt2 ... let's just compute
omv4_direct = c4 + (c3 - c1)/SQRT2
print(f"    omega.v1 = c1 - c4/sqrt2 = {omv1:.6f} (should = a = {a:.6f})")
print(f"    omega.v2 = c2            = {omv2:.6f}")
print(f"    omega.v3 = c3 + c4/sqrt2 = {omv3:.6f} (should = b = {b:.6f})")
print(f"    omega.v4 = c4+(c3-c1)/sqrt2 = {omv4_direct:.6f}")
# For vorticity max, need s1*a = s2*c2 = s3*b = lambda AND s4*omv4 = -sqrt3*lambda
# with s_j^2 = 1 - c_j^2. Equivalently (E):
# (1-c1^2)*a^2 = (1-c2^2)*c2^2 = (1-c3^2)*b^2 = (1/3)(1-c4^2)(omv4)^2 (all equal to lambda^2)
lam2_1 = (1 - c1*c1) * a*a
lam2_2 = (1 - c2*c2) * c2*c2
lam2_3 = (1 - c3*c3) * b*b
lam2_4 = (1.0/3.0) * (1 - c4*c4) * omv4_direct**2
print(f"    lambda^2 via j=1: (1-c1^2)*a^2          = {lam2_1:.6f}")
print(f"    lambda^2 via j=2: (1-c2^2)*c2^2         = {lam2_2:.6f}")
print(f"    lambda^2 via j=3: (1-c3^2)*b^2          = {lam2_3:.6f}")
print(f"    lambda^2 via j=4: (1/3)(1-c4^2)*omv4^2  = {lam2_4:.6f}")
print(f"    (at a real critical point these should all be equal)")

print(f"\n  NOTE: the sampling used the *relaxation* (F_j') <= 1/4 and (F') <= 3/2,")
print(f"  which corresponds to the INEQUALITY version of (E) (i.e., we bounded each")
print(f"  (1-c_j^2)(omv_j)^2 <= 1/4 via the j=2 arm). The violator above is feasible")
print(f"  for this relaxation but need not be on the critical manifold {{all four equal}}.")
print(f"  The original attempt_851 reduction (R*) is stated over THIS RELAXATION.")
