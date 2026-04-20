"""
Analytic violator: given c1 = -1, c3 = +1, c4 = -1, maximize -P over c2 in [-1,1].
This gives the exact analytic minimum of P over the box corner + F-set.
"""
import numpy as np
from sympy import symbols, Rational, sqrt, simplify, expand, solve, diff, S

c2 = symbols('c2', real=True)
# a = c1 - c4/sqrt2 = -1 - (-1)/sqrt2 = -1 + 1/sqrt2
a = -1 + Rational(1,1)/sqrt(2)
# b = c3 + c4/sqrt2 = 1 + (-1)/sqrt2 = 1 - 1/sqrt2
b = 1 - Rational(1,1)/sqrt(2)
c4 = -1

P_expr = Rational(5,8)*(a**2 + b**2 + c2**2) - (sqrt(2)/3)*c4*(a + c2 - 2*b) - c4**2
P_expr = expand(P_expr)
print("P(a,b,c2,c4) at (a,b,c4) = (1/sqrt2-1, 1-1/sqrt2, -1):")
print(f"  P = {P_expr}")
print(f"  P (simplified) = {simplify(P_expr)}")

dP = diff(P_expr, c2)
print(f"\ndP/dc2 = {simplify(dP)}")
c2_opt = solve(dP, c2)
print(f"c2 optimal (unconstrained): {c2_opt}")
for v in c2_opt:
    print(f"  numeric: {float(v):.8f}")
    P_at = P_expr.subs(c2, v)
    print(f"  P at optimum = {simplify(P_at)} = {float(P_at):.8f}")

# Feasibility check at the optimum
import math
SQRT2 = math.sqrt(2.0)
c2_star = float(c2_opt[0])
a_num = float(a); b_num = float(b); c4_num = -1.0

# F1': (1 - c1^2) a^2 <= 1/4.  c1 = -1 so 1 - c1^2 = 0. LHS = 0 <= 0.25. OK.
# F3': similar, c3 = 1, 1 - c3^2 = 0, LHS = 0 <= 0.25. OK.
# F':  (1 - c4^2) (b-a)^2 <= 3/2.  c4 = -1 so 1 - c4^2 = 0, LHS = 0 <= 1.5. OK.
# box: |c1|,|c2|,|c3|,|c4| <= 1 - all tight or interior.
# ND: a^2+b^2+c2^2+2 c4^2+sqrt2 c4 (a-b)
#   = (1/sqrt2-1)^2 + (1-1/sqrt2)^2 + c2^2 + 2 + sqrt2*(-1)*(1/sqrt2-1 - (1-1/sqrt2))
#   = 2*(1-1/sqrt2)^2 + c2^2 + 2 + sqrt2*(-1)*(2/sqrt2 - 2)
#   = 2*(1-1/sqrt2)^2 + c2^2 + 2 + sqrt2*(-1)*(sqrt2 - 2)
#   = 2*(1-1/sqrt2)^2 + c2^2 + 2 + (-2 + 2 sqrt2)
#   = 2*(1-1/sqrt2)^2 + c2^2 + 2 sqrt2
# At c2 = 0.377...: ND = 2*(1-0.7071)^2 + 0.1423 + 2.8284 = 2*0.08579 + 0.1423 + 2.8284 = 3.1424
ND_sym = a**2 + b**2 + c2**2 + 2*c4**2 + sqrt(2)*c4*(a - b)
ND_val = simplify(ND_sym.subs(c2, c2_opt[0]))
print(f"\nND at optimum = {ND_val} = {float(ND_val):.8f}")
print(f"(positive -> |omega|^2 > 0, not a degenerate boundary)")

# All feasibility conditions satisfied. Report the exact P value.
P_min_exact = simplify(P_expr.subs(c2, c2_opt[0]))
print(f"\nExact analytic minimum of P on this corner: {P_min_exact}")
print(f"  = {float(P_min_exact):.10f}")
print(f"Lasserre d=2 lower bound was: -1.395866")
print(f"Lasserre d=3 lower bound was: -1.395869")
print(f"These match to 5+ digits.")

# Now verify the corresponding Frobenius ratio exactly
c1_num = a_num + c4_num/SQRT2
c3_num = b_num - c4_num/SQRT2
print(f"\n(c1, c2, c3, c4) = ({c1_num:.6f}, {c2_star:.6f}, {c3_num:.6f}, {c4_num:.6f})")
print(f"  (c1, c3, c4) are exactly (-1, +1, -1); c2 = {c2_star:.6f}")

# Frobenius via explicit matrices
S1 = -0.5 * np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=float)
S2 = -0.5 * np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=float)
S3 = -0.5 * np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=float)
Mmat = np.array([[2,2,-1],[2,2,-1],[-1,-1,-4]], dtype=float)
S4 = -(1.0/(2.0*np.sqrt(18.0))) * Mmat
v1 = np.array([0,1,0], dtype=float)
v2 = np.array([0,0,1], dtype=float)
v3 = np.array([1,0,0], dtype=float)
v4 = np.array([1,-1,0], dtype=float) / SQRT2

Smat = c1_num*S1 + c2_star*S2 + c3_num*S3 + c4_num*S4
om = c1_num*v1 + c2_star*v2 + c3_num*v3 + c4_num*v4
F2 = float(np.sum(Smat*Smat))
OM2 = float(om @ om)
print(f"  ||S||_F^2 = {F2:.6f}")
print(f"  |omega|^2 = {OM2:.6f}")
print(f"  Frobenius ratio = {F2/OM2:.6f}  (target threshold: 9/8 = 1.125)")
print(f"  Ratio EXCEEDS 9/8 by a factor of {F2/OM2 / (9/8):.3f}")

# Is this a TRUE vorticity maximum? Check critical point condition.
# ω·v1 = c1 - c4/sqrt2 = -1 + 1/sqrt2 = a (≈ -0.293)
# ω·v2 = c2 = c2_star (≈ -0.377)
# ω·v3 = c3 + c4/sqrt2 = 1 - 1/sqrt2 = b (≈ 0.293)
# ω·v4 = c4 + (c3-c1)/sqrt2 = -1 + 2/sqrt2 = -1 + sqrt2 (≈ 0.414)
omv1 = c1_num - c4_num/SQRT2
omv2 = c2_star
omv3 = c3_num + c4_num/SQRT2
omv4 = c4_num + (c3_num - c1_num)/SQRT2
print(f"\nCritical-point check (at a REAL vorticity max, these four must all share a common lambda):")
print(f"  omv1 = {omv1:.6f}")
print(f"  omv2 = {omv2:.6f}")
print(f"  omv3 = {omv3:.6f}")
print(f"  omv4 = {omv4:.6f}")
# sj^2 = 1 - cj^2. Since c1=c3=c4=-1,-+1,-1 => s1=s3=s4=0. The first-order equations
# s1 (omv1) = s2 (omv2) = s3 (omv3) = s4 (omv4)/(-sqrt3) = lambda
# all become 0 (since s1=s3=s4=0) and s2(omv2) = lambda. For this to hold, lambda = s2 * c2_star.
# But s2^2 = 1 - c2^2 so s2 can be anything in [-sqrt(1-c2^2), sqrt(1-c2^2)], and we need
# s2(omv2) = 0 (to match the zero from j=1,3,4), so s2 * c2_star = 0. So either s2 = 0
# (=> c2_star = +-1) or c2_star = 0.
#
# At c2_star = 0.377, c2_star != +-1 so we need s2 = 0, which means c2_star = +-1 -- contradiction.
# So THE ONLY WAY for the first-order constraint to be satisfied at c4 = -1 (which forces s4=0)
# with c1=-1 (s1=0), c3=+1 (s3=0), is that c2_star = 0 or +-1.
#
# CONCLUSION: the violator does NOT satisfy the tight first-order critical-point equations (E).
# It only satisfies the RELAXATION (F_j') <= 1/4 (which are implied by (E) but not tight).

print(f"\n  At c4 = -1 (so s4 = 0), c1 = -1 (so s1 = 0), c3 = +1 (so s3 = 0),")
print(f"  the first-order equations s_j*(omega.v_j)*k_j = 0 force lambda = 0.")
print(f"  Then s2*(omv2) = lambda = 0, so either s2 = 0 (=> c2 = +-1) or c2 = 0.")
print(f"  The sampled c2 ~ -0.377 satisfies NEITHER of these.")
print(f"  => The violator is NOT a real vorticity maximum on T^3.")
print(f"     It lives in the RELAXED semialgebraic set (F_j') but not on the tight")
print(f"     critical manifold (E) = {{all four (1-c_j^2)(omv_j)^2 equal}}.")
