"""
Lasserre moment relaxation of the TIGHT N=4 first-order vorticity-max system
(attempt_851 configuration) with (E) enforced as three polynomial EQUALITIES
plus the four sphere equalities c_j^2 + s_j^2 = 1.

Variables (8): c1, c2, c3, c4, s1, s2, s3, s4  (indexed 0..7).

Target polynomial to test nonnegativity of:
  P(c) := (9/8) |omega|^2  -  ||S||_F^2
        = (5/8) (c1^2+c2^2+c3^2+c4^2)                   (the "||c||^2" contribution)
          + (9/8) * off_omega                           (from |omega|^2)
          - off_F                                       (from ||S||_F^2)
  with
    off_omega = sqrt(2) * c4 * (c3 - c1)
    off_F     = (c4 / (3 sqrt(2))) * (-c1 + 2 c2 - c3)   = (sqrt(2)/6) c4 (-c1 + 2c2 - c3)

Constraints (all polynomial):
  EQ sphere_j: c_j^2 + s_j^2 - 1 = 0,   j = 1..4          (4 equalities, deg 2)
  EQ E1:  s1 * a1  +  (1/sqrt(3)) * s4 * a4  = 0           (deg 2)
  EQ E2:  s2 * a2  +  (1/sqrt(3)) * s4 * a4  = 0           (deg 2)
  EQ E3:  s3 * a3  +  (1/sqrt(3)) * s4 * a4  = 0           (deg 2)
  with a1 = c1 - c4/sqrt2,  a2 = c2,  a3 = c3 + c4/sqrt2,
       a4 = c4 + (c3 - c1)/sqrt2.

  INEQ boxc_j:   1 - c_j^2  >= 0   (redundant w/ sphere but kept for Putinar archimedean)
  INEQ boxs_j:   1 - s_j^2  >= 0   (likewise)
  INEQ NONDEG:   |omega|^2 - eps >= 0   with eps = 1e-3.
     |omega|^2 = sum c_j^2 + off_omega = c1^2+c2^2+c3^2+c4^2 + sqrt2 * c4*(c3 - c1)

Lasserre relaxation order d:
  - Moment matrix M_d(y) indexed by monomials of total deg <= d, sized C(n+d, d).
  - For each eq constraint g (deg dg): impose M_{d - ceil(dg/2)}(g*y) = 0
    (equivalently the localizing matrix is identically zero, which is equivalent
    to every monomial of (g*y) up to degree 2d vanishing — we just impose
    y[beta + alpha] * coef to sum to zero at each alpha of degree <= 2d - dg).
  - For each ineq constraint g: impose M_{d - ceil(dg/2)}(g*y) >= 0.
  - Impose M_d(y) >= 0.
  - Normalize y[0] = 1.
  - Objective: minimize <P, y>. Lower bound on min_S P. If < 0, (P>=0) fails.

If d=3 is infeasible/slow/OOM we fall back to d=2. Both degrees: n_vars=8.
  n=8, d=2: half-monomials = C(10,2)=45, full=C(12,4)=495
  n=8, d=3: half-monomials = C(11,3)=165, full=C(14,6)=3003
d=3 is probably too big. We try d=2 first.
"""
import itertools
import time
import sys
import numpy as np
import cvxpy as cp

SQRT2 = np.sqrt(2.0)
SQRT3 = np.sqrt(3.0)
EPS_ND = 1e-3

n_vars = 8  # (c1, c2, c3, c4, s1, s2, s3, s4) at indices 0,1,2,3,4,5,6,7

def monomials(max_deg, n=n_vars):
    out = set()
    for total in range(max_deg+1):
        for combo in itertools.combinations_with_replacement(range(n), total):
            alpha = [0]*n
            for i in combo:
                alpha[i] += 1
            out.add(tuple(alpha))
    return sorted(out, key=lambda a: (sum(a), a))

def mono_str(alpha, names=('c1','c2','c3','c4','s1','s2','s3','s4')):
    parts = []
    for i, e in enumerate(alpha):
        if e == 1: parts.append(names[i])
        elif e > 1: parts.append(f"{names[i]}^{e}")
    return '*'.join(parts) if parts else '1'

# Polynomial arithmetic on dict[tuple -> float]
def poly_add(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0.0) + v
    return {k: v for k, v in r.items() if abs(v) > 1e-15}

def poly_scale(p, c):
    return {k: c*v for k, v in p.items() if abs(c*v) > 1e-15}

def poly_mul(p, q):
    r = {}
    for ka, va in p.items():
        for kb, vb in q.items():
            kc = tuple(ka[i]+kb[i] for i in range(n_vars))
            r[kc] = r.get(kc, 0.0) + va*vb
    return {k: v for k, v in r.items() if abs(v) > 1e-15}

def poly_degree(p):
    return max((sum(k) for k in p), default=0)

def mono(*powers):
    return {tuple(powers): 1.0}

# Create atomic polynomials for each variable
c1 = mono(1,0,0,0,0,0,0,0)
c2 = mono(0,1,0,0,0,0,0,0)
c3 = mono(0,0,1,0,0,0,0,0)
c4 = mono(0,0,0,1,0,0,0,0)
s1 = mono(0,0,0,0,1,0,0,0)
s2 = mono(0,0,0,0,0,1,0,0)
s3 = mono(0,0,0,0,0,0,1,0)
s4 = mono(0,0,0,0,0,0,0,1)
one = {(0,)*n_vars: 1.0}

# Build off_omega, off_F
# off_omega = sqrt(2) * c4 * (c3 - c1)
off_omega = poly_scale(poly_mul(c4, poly_add(c3, poly_scale(c1, -1.0))), SQRT2)
# off_F = (1/(3 sqrt2)) * c4 * (-c1 + 2 c2 - c3)
lin_F = poly_add(poly_add(poly_scale(c1, -1.0), poly_scale(c2, 2.0)), poly_scale(c3, -1.0))
off_F = poly_scale(poly_mul(c4, lin_F), 1.0/(3.0*SQRT2))

# ||c||^2 = c1^2 + c2^2 + c3^2 + c4^2
cnorm2 = poly_add(poly_add(poly_add(poly_mul(c1,c1), poly_mul(c2,c2)),
                           poly_mul(c3,c3)), poly_mul(c4,c4))

# |omega|^2 = ||c||^2 + off_omega
omega2 = poly_add(cnorm2, off_omega)

# ||S||_F^2 = (1/2) ||c||^2 + off_F
SF2 = poly_add(poly_scale(cnorm2, 0.5), off_F)

# P = (9/8) |omega|^2 - ||S||_F^2
P = poly_add(poly_scale(omega2, 9.0/8.0), poly_scale(SF2, -1.0))

# Equality constraints
# sphere_j : c_j^2 + s_j^2 - 1 = 0
sphere_1 = poly_add(poly_add(poly_mul(c1,c1), poly_mul(s1,s1)), poly_scale(one, -1.0))
sphere_2 = poly_add(poly_add(poly_mul(c2,c2), poly_mul(s2,s2)), poly_scale(one, -1.0))
sphere_3 = poly_add(poly_add(poly_mul(c3,c3), poly_mul(s3,s3)), poly_scale(one, -1.0))
sphere_4 = poly_add(poly_add(poly_mul(c4,c4), poly_mul(s4,s4)), poly_scale(one, -1.0))

# a's
a1 = poly_add(c1, poly_scale(c4, -1.0/SQRT2))
a2 = c2
a3 = poly_add(c3, poly_scale(c4, 1.0/SQRT2))
# a4 = c4 + (c3 - c1)/sqrt2
a4 = poly_add(c4, poly_scale(poly_add(c3, poly_scale(c1, -1.0)), 1.0/SQRT2))

# E_j = s_j * a_j + (1/sqrt3) * s4 * a4  = 0
s4a4_scaled = poly_scale(poly_mul(s4, a4), 1.0/SQRT3)
E1 = poly_add(poly_mul(s1, a1), s4a4_scaled)
E2 = poly_add(poly_mul(s2, a2), s4a4_scaled)
E3 = poly_add(poly_mul(s3, a3), s4a4_scaled)

eq_list = [
    ("sphere1", sphere_1), ("sphere2", sphere_2),
    ("sphere3", sphere_3), ("sphere4", sphere_4),
    ("E1", E1), ("E2", E2), ("E3", E3),
]

# Inequality constraints
# box_c_j : 1 - c_j^2 >= 0
box_c1 = poly_add(one, poly_scale(poly_mul(c1,c1), -1.0))
box_c2 = poly_add(one, poly_scale(poly_mul(c2,c2), -1.0))
box_c3 = poly_add(one, poly_scale(poly_mul(c3,c3), -1.0))
box_c4 = poly_add(one, poly_scale(poly_mul(c4,c4), -1.0))
# box_s_j : 1 - s_j^2 >= 0
box_s1 = poly_add(one, poly_scale(poly_mul(s1,s1), -1.0))
box_s2 = poly_add(one, poly_scale(poly_mul(s2,s2), -1.0))
box_s3 = poly_add(one, poly_scale(poly_mul(s3,s3), -1.0))
box_s4 = poly_add(one, poly_scale(poly_mul(s4,s4), -1.0))
# NONDEG: omega2 - eps >= 0
nondeg = poly_add(omega2, poly_scale(one, -EPS_ND))

ineq_list = [
    ("box_c1", box_c1), ("box_c2", box_c2), ("box_c3", box_c3), ("box_c4", box_c4),
    ("box_s1", box_s1), ("box_s2", box_s2), ("box_s3", box_s3), ("box_s4", box_s4),
    ("NONDEG", nondeg),
]

def run_relaxation(d):
    print(f"\n=== Lasserre moment relaxation at d={d} (moments up to 2d={2*d}) ===")
    t0 = time.time()
    half_mons = monomials(d)
    full_mons = monomials(2*d)
    mono_idx = {m: i for i, m in enumerate(full_mons)}
    print(f"  |half|={len(half_mons)} (moment matrix side), |full|={len(full_mons)} (scalar moment variables)")
    sys.stdout.flush()

    y = cp.Variable(len(full_mons), name='y')
    cs = [y[mono_idx[(0,)*n_vars]] == 1.0]

    # Moment matrix M_d(y) >= 0
    sz = len(half_mons)
    M = cp.Variable((sz, sz), symmetric=True)
    for i in range(sz):
        for j in range(sz):
            alpha = tuple(half_mons[i][k] + half_mons[j][k] for k in range(n_vars))
            cs.append(M[i,j] == y[mono_idx[alpha]])
    cs.append(M >> 0)
    print(f"  moment matrix M_d: {sz}x{sz}")
    sys.stdout.flush()

    # Localizing matrices for inequalities: M_{d - ceil(dg/2)}(g*y) >= 0
    loc_count = 0
    for name, g in ineq_list:
        dg = poly_degree(g)
        dloc = d - (dg + 1)//2
        if dloc < 0:
            print(f"  skip ineq {name}: dg={dg} too large for d={d}")
            continue
        loc_mons = monomials(dloc)
        sz_l = len(loc_mons)
        L = cp.Variable((sz_l, sz_l), symmetric=True)
        for i in range(sz_l):
            for j in range(sz_l):
                alpha_ij = tuple(loc_mons[i][k] + loc_mons[j][k] for k in range(n_vars))
                expr = 0.0
                for beta, coef in g.items():
                    gam = tuple(alpha_ij[k] + beta[k] for k in range(n_vars))
                    if gam in mono_idx:
                        expr = expr + coef * y[mono_idx[gam]]
                cs.append(L[i,j] == expr)
        cs.append(L >> 0)
        loc_count += 1
        print(f"  ineq localizer {name}: dg={dg}, dloc={dloc}, size={sz_l}")
        sys.stdout.flush()

    # Equality constraints: for every shifted monomial u of degree <= 2d - dg,
    # impose sum_beta g[beta] * y[u + beta] == 0.
    eq_count = 0
    for name, g in eq_list:
        dg = poly_degree(g)
        shift_deg = 2*d - dg
        if shift_deg < 0:
            print(f"  skip eq {name}: dg={dg} exceeds 2d={2*d}")
            continue
        shift_mons = monomials(shift_deg)
        for u in shift_mons:
            expr = 0.0
            active = False
            for beta, coef in g.items():
                gam = tuple(u[k] + beta[k] for k in range(n_vars))
                if gam in mono_idx:
                    expr = expr + coef * y[mono_idx[gam]]
                    active = True
            if active:
                cs.append(expr == 0)
        eq_count += 1
        print(f"  eq {name}: dg={dg}, shift_monos={len(shift_mons)}")
        sys.stdout.flush()

    # Objective: minimize <P, y>
    obj_expr = sum(coef * y[mono_idx[alpha]] for alpha, coef in P.items())
    problem = cp.Problem(cp.Minimize(obj_expr), cs)
    print(f"  total constraints: {len(cs)}")
    print(f"  building problem took {time.time()-t0:.1f}s")
    sys.stdout.flush()

    t1 = time.time()
    print("  solving with SCS...")
    sys.stdout.flush()
    try:
        problem.solve(solver='SCS', verbose=False, max_iters=200000, eps=1e-7)
    except Exception as e:
        print(f"  SOLVER ERROR: {e}")
        import traceback; traceback.print_exc()
        return None
    t2 = time.time()
    print(f"  solve took {t2-t1:.1f}s")
    print(f"  status: {problem.status}")
    print(f"  optimal value (lower bound on min P over tight set): {problem.value}")
    sys.stdout.flush()

    # Extract candidate atom from moments
    if problem.value is not None and M.value is not None:
        Mval = np.array(M.value)
        idx1 = mono_idx.get(tuple([0]*n_vars), None)
        print(f"  y[1]={y.value[idx1] if idx1 is not None else 'N/A':.6f}")
        # first-order moments
        labels = ['c1','c2','c3','c4','s1','s2','s3','s4']
        vals = []
        for k in range(n_vars):
            alpha = tuple(1 if i==k else 0 for i in range(n_vars))
            if alpha in mono_idx:
                vals.append(y.value[mono_idx[alpha]])
            else:
                vals.append(float('nan'))
        print("  first-order moments (candidate mean values of variables):")
        for lab, v in zip(labels, vals):
            print(f"    E[{lab}] = {v:+.6f}")
        evals = np.linalg.eigvalsh(Mval)
        top = evals[-6:] if len(evals) >= 6 else evals
        print(f"  moment matrix top eigenvalues: {top}")
        print(f"  moment matrix bottom eigenvalues: {evals[:6]}")
        # If moment matrix is rank-1 on the top, can read atom off directly
        c1v, c2v, c3v, c4v, s1v, s2v, s3v, s4v = vals
        # Check feasibility of the mean point on the tight system
        def feas_check(c1v, c2v, c3v, c4v, s1v, s2v, s3v, s4v):
            print("  feasibility check at moment-mean (may not be a true atom):")
            for j, (cv, sv) in enumerate(zip([c1v,c2v,c3v,c4v],[s1v,s2v,s3v,s4v]), start=1):
                print(f"    sphere_{j}: c^2+s^2-1 = {cv*cv+sv*sv-1:+.4e}")
            a1v = c1v - c4v/SQRT2
            a2v = c2v
            a3v = c3v + c4v/SQRT2
            a4v = c4v + (c3v - c1v)/SQRT2
            E1v = s1v*a1v + s4v*a4v/SQRT3
            E2v = s2v*a2v + s4v*a4v/SQRT3
            E3v = s3v*a3v + s4v*a4v/SQRT3
            print(f"    E1 = {E1v:+.4e},  E2 = {E2v:+.4e},  E3 = {E3v:+.4e}")
            omega2v = c1v**2+c2v**2+c3v**2+c4v**2 + SQRT2*c4v*(c3v - c1v)
            print(f"    |omega|^2 = {omega2v:+.4e}  (need >= {EPS_ND})")
            SF2v = 0.5*(c1v**2+c2v**2+c3v**2+c4v**2) + (c4v/(3*SQRT2))*(-c1v+2*c2v-c3v)
            Pv = 9.0/8.0 * omega2v - SF2v
            print(f"    P = (9/8)|omega|^2 - ||S||_F^2 = {Pv:+.6f}")
            return Pv
        feas_check(c1v, c2v, c3v, c4v, s1v, s2v, s3v, s4v)
    return problem.value

def main():
    overall_t0 = time.time()
    print("Tight N=4 Lasserre SOS check")
    print("  target: P(c) = (9/8)|omega|^2 - ||S||_F^2  >= 0  on TIGHT set (E) as equalities")
    print(f"  NONDEG epsilon = {EPS_ND}")
    print(f"  polynomial monomials in P: {len(P)}")
    for alpha, coef in sorted(P.items(), key=lambda kv: (sum(kv[0]), kv[0])):
        print(f"    P[{mono_str(alpha):20s}] = {coef:+.6f}")

    # Cross-check: Agent B's violator (-1, -4sqrt2/15, +1, -1) on the TIGHT system
    print("\n--- Cross-check: Agent B's violator on the TIGHT system ---")
    c1v, c2v, c3v, c4v = -1.0, -4.0*SQRT2/15.0, 1.0, -1.0
    # At c1=-1 => s1=0, c3=1 => s3=0, c4=-1 => s4=0
    # The sphere forces s1, s3, s4 = 0 (unique up to sign, and the tight value 0).
    s1v, s3v, s4v = 0.0, 0.0, 0.0
    # s2 satisfies s2^2 = 1 - c2^2 = 1 - 32/225 = 193/225
    s2_pos = np.sqrt(1.0 - c2v*c2v)
    for s2v in [s2_pos, -s2_pos]:
        a1v = c1v - c4v/SQRT2
        a2v = c2v
        a3v = c3v + c4v/SQRT2
        a4v = c4v + (c3v - c1v)/SQRT2
        E1v = s1v*a1v + s4v*a4v/SQRT3
        E2v = s2v*a2v + s4v*a4v/SQRT3
        E3v = s3v*a3v + s4v*a4v/SQRT3
        print(f"  s2={s2v:+.6f}:  E1={E1v:+.4e}, E2={E2v:+.4e}, E3={E3v:+.4e}")
        print(f"    E2 = s2 * c2 = {s2v*c2v:+.6f}  (must be 0 for tight E2; NOT zero)")
    # sphere constraints OK? (s1, s3, s4) = 0 is the unique fix.
    print("  --> violator FAILS E2 as equality (unless s2 = 0, but sphere_2 forces s2^2 > 0). Good.")

    # Run relaxation.
    result = None
    degrees_to_try = [int(x) for x in (sys.argv[1].split(',') if len(sys.argv) > 1 else ['2'])]
    for d in degrees_to_try:
        try:
            v = run_relaxation(d)
            result = (d, v)
        except Exception as e:
            print(f"d={d} crashed: {e}")
            import traceback; traceback.print_exc()
    print(f"\nTOTAL runtime: {time.time()-overall_t0:.1f}s")
    if result is not None:
        print(f"Final: d={result[0]},  min_S P lower bound = {result[1]}")

if __name__ == '__main__':
    main()
