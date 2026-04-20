"""
Lasserre moment-relaxation / SOS feasibility at degree 4 for (R*) from attempt_851.

Primal (SOS, Putinar): does there exist an SOS decomposition
    P(a,b,c2,c4) = sigma_0 + sigma_1 * g_1 + ... + sigma_m * g_m
where P = (5/8)(a^2+b^2+c2^2) - (sqrt2/3)c4(a+c2-2b) - c4^2, each sigma_i SOS,
and g_i are the POSITIVE constraint polynomials
  g_box1 = 1 - (a + c4/sqrt2)^2        (>= 0 in S)
  g_box2 = 1 - (b - c4/sqrt2)^2
  g_box3 = 1 - c2^2
  g_box4 = 1 - c4^2
  g_F1   = 1/4 - (1 - (a+c4/sqrt2)^2) * a^2
  g_F3   = 1/4 - (1 - (b-c4/sqrt2)^2) * b^2
  g_F    = 3/2 - (1 - c4^2) * (b - a)^2
  g_ND   = a^2 + b^2 + c2^2 + 2 c4^2 + sqrt2 * c4 * (a - b)   (>0 strictly; use as >=0)

Dual (moment): minimize <P, y> over pseudo-moment sequences y of degree <= 2d
subject to moment matrix M_d(y) >= 0 and localizing matrices M_{d-deg(g)/2}(g_i * y) >= 0.
Lower bound on min_{S} P. If minimum < 0, certificate = violator (via moment
extraction). If bound >= 0 at some degree d, P >= 0 on S.

We implement the moment relaxation at degree d=2 (so moments of degree up to 4)
using cvxpy + SCS/CLARABEL.
"""
import itertools
import numpy as np
import cvxpy as cp

SQRT2 = np.sqrt(2.0)

# Variables: x = (a, b, c2, c4)  (4 vars)
# Monomial basis up to total degree 2d, with d=2 => moments up to deg 4.
# For d=2, we generate monomials up to degree 4 in the moment sequence y.
# Moment matrix M_d(y) is indexed by monomials of degree <= d.

n_vars = 4

def monomials(max_deg, n=n_vars):
    """List all multi-indices of total degree <= max_deg, sorted grlex."""
    out = []
    for total in range(max_deg+1):
        for combo in itertools.combinations_with_replacement(range(n), total):
            alpha = [0]*n
            for i in combo: alpha[i] += 1
            out.append(tuple(alpha))
    # dedup and sort
    out = sorted(set(out), key=lambda a: (sum(a), a))
    return out

def mono_str(alpha, names=('a','b','c2','c4')):
    parts = []
    for i,e in enumerate(alpha):
        if e == 1: parts.append(names[i])
        elif e > 1: parts.append(f"{names[i]}^{e}")
    return '*'.join(parts) if parts else '1'

def poly_add(p, q):
    r = dict(p)
    for k,v in q.items():
        r[k] = r.get(k, 0.0) + v
    return {k:v for k,v in r.items() if abs(v) > 1e-15}

def poly_scale(p, c):
    return {k: c*v for k,v in p.items() if abs(c*v) > 1e-15}

def poly_mul(p, q):
    r = {}
    for ka, va in p.items():
        for kb, vb in q.items():
            kc = tuple(ka[i]+kb[i] for i in range(n_vars))
            r[kc] = r.get(kc, 0.0) + va*vb
    return {k:v for k,v in r.items() if abs(v) > 1e-15}

# Build constraint polynomials and objective
def mono(*powers):
    return {tuple(powers): 1.0}

a = mono(1,0,0,0); b = mono(0,1,0,0); c2 = mono(0,0,1,0); c4 = mono(0,0,0,1)
one = {(0,0,0,0): 1.0}

# P = (5/8)(a^2+b^2+c2^2) - (sqrt2/3) c4 (a+c2-2b) - c4^2
P = poly_add(poly_add(poly_add(
        poly_scale(poly_mul(a,a), 5/8),
        poly_scale(poly_mul(b,b), 5/8)),
        poly_scale(poly_mul(c2,c2), 5/8)),
        poly_add(
            poly_scale(poly_mul(c4, poly_add(poly_add(a,c2), poly_scale(b,-2))), -SQRT2/3),
            poly_scale(poly_mul(c4,c4), -1)
        ))

# c1 = a + c4/sqrt2, c3 = b - c4/sqrt2
c1 = poly_add(a, poly_scale(c4, 1.0/SQRT2))
c3 = poly_add(b, poly_scale(c4, -1.0/SQRT2))

# Constraint polynomials g_i >= 0
g_box1 = poly_add(one, poly_scale(poly_mul(c1,c1), -1))
g_box2 = poly_add(one, poly_scale(poly_mul(c3,c3), -1))
g_box3 = poly_add(one, poly_scale(poly_mul(c2,c2), -1))
g_box4 = poly_add(one, poly_scale(poly_mul(c4,c4), -1))
g_F1   = poly_add(poly_scale(one, 0.25), poly_scale(poly_mul(g_box1, poly_mul(a,a)), -1))
g_F3   = poly_add(poly_scale(one, 0.25), poly_scale(poly_mul(g_box2, poly_mul(b,b)), -1))
# (1 - c4^2) * (b-a)^2
bma = poly_add(b, poly_scale(a, -1))
g_F    = poly_add(poly_scale(one, 1.5), poly_scale(poly_mul(g_box4, poly_mul(bma,bma)), -1))
# NON-DEG: a^2+b^2+c2^2+2 c4^2 + sqrt2 c4 (a-b)
g_ND = poly_add(poly_add(poly_add(poly_add(
            poly_mul(a,a), poly_mul(b,b)), poly_mul(c2,c2)),
            poly_scale(poly_mul(c4,c4), 2)),
            poly_scale(poly_mul(c4, poly_add(a, poly_scale(b,-1))), SQRT2))

constraints_list = [
    ("box1", g_box1), ("box2", g_box2), ("box3", g_box3), ("box4", g_box4),
    ("F1p", g_F1), ("F3p", g_F3), ("Fp", g_F), ("ND", g_ND)
]

d = 2   # relaxation order: moments up to deg 2d = 4
half_mons = monomials(d)            # deg <= d
full_mons = monomials(2*d)          # deg <= 2d
mono_idx = {m:i for i,m in enumerate(full_mons)}

print(f"Relaxation order d = {d}")
print(f"  half-degree monomials: {len(half_mons)}  (size of M_d)")
print(f"  full-degree monomials: {len(full_mons)}  (moment variables)")

# Decision variable: y[alpha] for alpha in full_mons; y[0]=1
y = cp.Variable(len(full_mons), name='y')

# Normalize: y for alpha=(0,..,0) equal to 1
cs = [y[mono_idx[(0,)*n_vars]] == 1]

# Moment matrix M_d(y) >= 0, where M[i,j] = y[half_mons[i] + half_mons[j]]
sz = len(half_mons)
M = cp.Variable((sz, sz), symmetric=True)
M_entries = []
for i in range(sz):
    for j in range(sz):
        alpha = tuple(half_mons[i][k] + half_mons[j][k] for k in range(n_vars))
        cs.append(M[i,j] == y[mono_idx[alpha]])
cs.append(M >> 0)

# Localizing matrices M_{d - ceil(deg(g)/2)}(g * y) >= 0
# For each constraint g of degree deg_g, use localizing matrix indexed by monomials
# of degree <= d - ceil(deg_g / 2).
def poly_degree(p):
    return max((sum(k) for k in p), default=0)

for name, g in constraints_list:
    dg = poly_degree(g)
    dloc = d - (dg + 1) // 2
    if dloc < 0:
        print(f"  Skipping localizer for {name}: deg(g)={dg} too high for d={d}")
        continue
    loc_mons = monomials(dloc)
    sz_l = len(loc_mons)
    L = cp.Variable((sz_l, sz_l), symmetric=True)
    for i in range(sz_l):
        for j in range(sz_l):
            # Entry = sum_beta g[beta] * y[ loc_mons[i] + loc_mons[j] + beta ]
            alpha_ij = tuple(loc_mons[i][k] + loc_mons[j][k] for k in range(n_vars))
            expr = 0.0
            for beta, coef in g.items():
                gam = tuple(alpha_ij[k] + beta[k] for k in range(n_vars))
                if gam in mono_idx:
                    expr = expr + coef * y[mono_idx[gam]]
                else:
                    # Moment out of range -> constraint not representable at this order
                    # If the coefficient is tiny, we can drop; otherwise the relaxation is
                    # too weak for this constraint - skip and warn.
                    pass
            cs.append(L[i,j] == expr)
    cs.append(L >> 0)
    print(f"  Localizer for {name}: deg(g)={dg}, dloc={dloc}, size={sz_l}")

# Objective: minimize <P, y>
obj_expr = sum(coef * y[mono_idx[alpha]] for alpha, coef in P.items())
print(f"\nObjective P has {len(P)} monomials")
for alpha, coef in sorted(P.items()):
    print(f"    P[{mono_str(alpha)}] = {coef:+.6f}")

problem = cp.Problem(cp.Minimize(obj_expr), cs)
print(f"\nSolving moment relaxation (Lasserre dual) at degree d={d}...")
try:
    problem.solve(solver='SCS', verbose=False, max_iters=200000)
    print(f"Status: {problem.status}")
    print(f"Optimal value (lower bound on min P over S): {problem.value:.6f}")
    if problem.value is not None and problem.value < -1e-4:
        print("\n!! NEGATIVE LOWER BOUND: (R*) is NOT valid on the relaxed semialgebraic set S.")
        print("   This means (R*) is INFEASIBLE in the Putinar/SOS sense at degree", d, ".")
        print("   Try extracting a violator from the moment matrix.")

        # Extract a candidate atomic solution from the first-order moments
        Mval = M.value
        # Degree-1 moments are at indices 1..n_vars in half_mons (since half_mons[0] = 0)
        idx_a = half_mons.index((1,0,0,0))
        idx_b = half_mons.index((0,1,0,0))
        idx_c2 = half_mons.index((0,0,1,0))
        idx_c4 = half_mons.index((0,0,0,1))
        a_star = Mval[0, idx_a]
        b_star = Mval[0, idx_b]
        c2_star = Mval[0, idx_c2]
        c4_star = Mval[0, idx_c4]
        print(f"   Moment-extracted (a,b,c2,c4) = ({a_star:.6f}, {b_star:.6f}, {c2_star:.6f}, {c4_star:.6f})")
        P_at = (5.0/8.0)*(a_star**2+b_star**2+c2_star**2) - (SQRT2/3.0)*c4_star*(a_star+c2_star-2*b_star) - c4_star**2
        print(f"   P at this point = {P_at:.6f}")
        # verify feasibility
        c1_star = a_star + c4_star/SQRT2
        c3_star = b_star - c4_star/SQRT2
        print(f"   Derived c1 = {c1_star:.6f}, c3 = {c3_star:.6f}")
        print(f"   |c1|<=1? {abs(c1_star)<=1+1e-6}, |c3|<=1? {abs(c3_star)<=1+1e-6}, |c2|<=1? {abs(c2_star)<=1+1e-6}, |c4|<=1? {abs(c4_star)<=1+1e-6}")
        F1v = (1-c1_star**2)*a_star**2; F3v = (1-c3_star**2)*b_star**2; Fv = (1-c4_star**2)*(b_star-a_star)**2
        NDv = a_star**2+b_star**2+c2_star**2+2*c4_star**2+SQRT2*c4_star*(a_star-b_star)
        print(f"   F1'={F1v:.4f}<=0.25? {F1v<=0.25+1e-6}, F3'={F3v:.4f}<=0.25? {F3v<=0.25+1e-6}, F'={Fv:.4f}<=1.5? {Fv<=1.5+1e-6}, ND={NDv:.4f}>0? {NDv>0}")
except Exception as e:
    print(f"Solver error: {e}")
    import traceback; traceback.print_exc()
