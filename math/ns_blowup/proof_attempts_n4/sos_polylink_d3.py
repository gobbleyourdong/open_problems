"""
Attempt 856 — Lasserre moment relaxation of the TIGHT N=4 first-order vorticity-max
system at the ATTEMPT_852 configuration (k4 = (1,1,0), integer lattice mode), with
the POLYNOMIAL angle-link imposed as two additional polynomial equalities.

Configuration (attempt_852):
  k_1 = e1, v_1 = e2, w_1 = e3
  k_2 = e2, v_2 = e3, w_2 = e1
  k_3 = e3, v_3 = e1, w_3 = e2
  k_4 = (1,1,0), |k_4|^2 = 2, v_4 = (1,-1,0)/sqrt2, w_4 = (0,0,-sqrt2)

Because k_4 = k_1 + k_2 (integer-lattice), cos(k_4 . x) = cos(x_1 + x_2) is
POLYNOMIAL in (c_1, s_1, c_2, s_2) via cos-sum / sin-sum identities:

  c_4 = c_1 * c_2 - s_1 * s_2         (angle-link, c_4)
  s_4 = s_1 * c_2 + c_1 * s_2         (angle-link, s_4)

Variables (8 reals, same indexing): c_1, c_2, c_3, c_4, s_1, s_2, s_3, s_4.

Target polynomial (from attempt_852 §3):
  P(c) = (5/8) * (c_1^2 + c_2^2 + c_3^2 + c_4^2)
         + (sqrt(2)/8) * c_4 * (13 c_3 - 5 c_1)
(equivalent to (9/8)|omega|^2 - ||S||_F^2 at this config). All degree 2.

Constraints (all polynomial):
  EQ sphere_j: c_j^2 + s_j^2 - 1 = 0,   j = 1..4          (4 equalities, deg 2)
  EQ AL_c: c_4 - (c_1 c_2 - s_1 s_2) = 0                   (deg 2)
  EQ AL_s: s_4 - (s_1 c_2 + c_1 s_2) = 0                   (deg 2)
  EQ FO_1 (C1):  s_3 * a_3 = 0,                            (deg 2)
    where a_3 = c_3 + c_4/sqrt2
  EQ FO_2 (C2):  s_1 * a_1 - s_2 * a_2 = 0,                (deg 2)
    where a_1 = c_1 - c_4/sqrt2,  a_2 = c_2
  EQ FO_3 (C3):  s_1 * a_1 + s_4 * a_4 = 0,                (deg 2)
    where a_4 = c_4 + (c_3 - c_1)/sqrt2
  INEQ NONDEG:  |omega|^2 - eps >= 0,  |omega|^2 = sum c_j^2 + sqrt2 * c_4 * (c_3 - c_1)
  (Also box inequalities 1 - c_j^2 >= 0, 1 - s_j^2 >= 0 for Putinar archimedeanness.)

Lasserre order d:
  d=2: moment-matrix side = C(10,2)=45, full moment vector = C(12,4)=495
  d=3: moment-matrix side = C(11,3)=165, full = C(14,6)=3003
"""
import itertools
import time
import sys
import numpy as np
import cvxpy as cp

SQRT2 = np.sqrt(2.0)
EPS_ND = 1e-3

n_vars = 8  # (c1, c2, c3, c4, s1, s2, s3, s4) at indices 0..7

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

# Atomic polynomials for each variable
c1 = mono(1,0,0,0,0,0,0,0)
c2 = mono(0,1,0,0,0,0,0,0)
c3 = mono(0,0,1,0,0,0,0,0)
c4 = mono(0,0,0,1,0,0,0,0)
s1 = mono(0,0,0,0,1,0,0,0)
s2 = mono(0,0,0,0,0,1,0,0)
s3 = mono(0,0,0,0,0,0,1,0)
s4 = mono(0,0,0,0,0,0,0,1)
one = {(0,)*n_vars: 1.0}

# ||c||^2
cnorm2 = poly_add(poly_add(poly_add(poly_mul(c1,c1), poly_mul(c2,c2)),
                           poly_mul(c3,c3)), poly_mul(c4,c4))

# off_omega = sqrt(2) * c_4 * (c_3 - c_1)
off_omega = poly_scale(poly_mul(c4, poly_add(c3, poly_scale(c1, -1.0))), SQRT2)

# |omega|^2 = ||c||^2 + sqrt(2) c_4 (c_3 - c_1)
omega2 = poly_add(cnorm2, off_omega)

# P(c) = (5/8) ||c||^2 + (sqrt2/8) c_4 (13 c_3 - 5 c_1)
# Equivalent form: (5/8)*Sum_c^2 + (sqrt2/8)*(13 c_3 - 5 c_1)*c_4
lin_P = poly_add(poly_scale(c3, 13.0), poly_scale(c1, -5.0))
P = poly_add(poly_scale(cnorm2, 5.0/8.0),
             poly_scale(poly_mul(c4, lin_P), SQRT2/8.0))

# Sanity: double-check P = (9/8)|omega|^2 - ||S||_F^2.
#   ||S||_F^2 = 0.5*||c||^2 - (sqrt2/2)*(c1+c3)*c4
SF2_check = poly_add(poly_scale(cnorm2, 0.5),
                     poly_scale(poly_mul(c4, poly_add(c1, c3)), -SQRT2/2.0))
P_check = poly_add(poly_scale(omega2, 9.0/8.0), poly_scale(SF2_check, -1.0))
# P_check should equal P.
diff = poly_add(P, poly_scale(P_check, -1.0))
print(f"Sanity: ||P - P_check|| = {sum(abs(v) for v in diff.values()):.2e}")

# Equality constraints
# 1) Sphere j: c_j^2 + s_j^2 - 1 = 0
sphere_1 = poly_add(poly_add(poly_mul(c1,c1), poly_mul(s1,s1)), poly_scale(one, -1.0))
sphere_2 = poly_add(poly_add(poly_mul(c2,c2), poly_mul(s2,s2)), poly_scale(one, -1.0))
sphere_3 = poly_add(poly_add(poly_mul(c3,c3), poly_mul(s3,s3)), poly_scale(one, -1.0))
sphere_4 = poly_add(poly_add(poly_mul(c4,c4), poly_mul(s4,s4)), poly_scale(one, -1.0))

# 2) Angle-link: c_4 - (c_1 c_2 - s_1 s_2) = 0,  s_4 - (s_1 c_2 + c_1 s_2) = 0
c1c2 = poly_mul(c1, c2)
s1s2 = poly_mul(s1, s2)
s1c2 = poly_mul(s1, c2)
c1s2 = poly_mul(c1, s2)
AL_c = poly_add(c4, poly_scale(poly_add(c1c2, poly_scale(s1s2, -1.0)), -1.0))
AL_s = poly_add(s4, poly_scale(poly_add(s1c2, c1s2), -1.0))

# 3) First-order (at attempt_852 config)
#    a_1 = c_1 - c_4/sqrt2
#    a_2 = c_2
#    a_3 = c_3 + c_4/sqrt2
#    a_4 = c_4 + (c_3 - c_1)/sqrt2
a1 = poly_add(c1, poly_scale(c4, -1.0/SQRT2))
a2 = c2
a3 = poly_add(c3, poly_scale(c4, 1.0/SQRT2))
a4 = poly_add(c4, poly_scale(poly_add(c3, poly_scale(c1, -1.0)), 1.0/SQRT2))

# (C1): s_3 * a_3 = 0
FO_1 = poly_mul(s3, a3)
# (C2): s_1 * a_1 - s_2 * a_2 = 0
FO_2 = poly_add(poly_mul(s1, a1), poly_scale(poly_mul(s2, a2), -1.0))
# (C3): s_1 * a_1 + s_4 * a_4 = 0
FO_3 = poly_add(poly_mul(s1, a1), poly_mul(s4, a4))

eq_list = [
    ("sphere1", sphere_1), ("sphere2", sphere_2),
    ("sphere3", sphere_3), ("sphere4", sphere_4),
    ("AL_c", AL_c), ("AL_s", AL_s),
    ("FO_1_C1", FO_1), ("FO_2_C2", FO_2), ("FO_3_C3", FO_3),
]

# Inequalities
box_c1 = poly_add(one, poly_scale(poly_mul(c1,c1), -1.0))
box_c2 = poly_add(one, poly_scale(poly_mul(c2,c2), -1.0))
box_c3 = poly_add(one, poly_scale(poly_mul(c3,c3), -1.0))
box_c4 = poly_add(one, poly_scale(poly_mul(c4,c4), -1.0))
box_s1 = poly_add(one, poly_scale(poly_mul(s1,s1), -1.0))
box_s2 = poly_add(one, poly_scale(poly_mul(s2,s2), -1.0))
box_s3 = poly_add(one, poly_scale(poly_mul(s3,s3), -1.0))
box_s4 = poly_add(one, poly_scale(poly_mul(s4,s4), -1.0))
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
    print(f"  |half|={len(half_mons)} (moment matrix side), |full|={len(full_mons)} (scalar moment vars)")
    sys.stdout.flush()

    y = cp.Variable(len(full_mons), name='y')
    cs = [y[mono_idx[(0,)*n_vars]] == 1.0]

    sz = len(half_mons)
    M = cp.Variable((sz, sz), symmetric=True)
    for i in range(sz):
        for j in range(sz):
            alpha = tuple(half_mons[i][k] + half_mons[j][k] for k in range(n_vars))
            cs.append(M[i,j] == y[mono_idx[alpha]])
    cs.append(M >> 0)
    print(f"  moment matrix M_d: {sz}x{sz}")
    sys.stdout.flush()

    # Localizers for inequalities
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
        print(f"  ineq localizer {name}: dg={dg}, dloc={dloc}, size={sz_l}")
        sys.stdout.flush()

    # Equality shifts
    for name, g in eq_list:
        dg = poly_degree(g)
        shift_deg = 2*d - dg
        if shift_deg < 0:
            print(f"  skip eq {name}: dg={dg} exceeds 2d={2*d}")
            continue
        shift_mons = monomials(shift_deg)
        cnt = 0
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
                cnt += 1
        print(f"  eq {name}: dg={dg}, shift_monos={len(shift_mons)}, active={cnt}")
        sys.stdout.flush()

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

    if problem.value is not None and M.value is not None:
        Mval = np.array(M.value)
        labels = ['c1','c2','c3','c4','s1','s2','s3','s4']
        vals = []
        for k in range(n_vars):
            alpha = tuple(1 if i==k else 0 for i in range(n_vars))
            if alpha in mono_idx:
                vals.append(y.value[mono_idx[alpha]])
            else:
                vals.append(float('nan'))
        print("  first-order moments (candidate mean):")
        for lab, v in zip(labels, vals):
            print(f"    E[{lab}] = {v:+.6f}")
        evals = np.linalg.eigvalsh(Mval)
        top = evals[-6:] if len(evals) >= 6 else evals
        print(f"  moment matrix top eigenvalues: {top}")
        print(f"  moment matrix bottom eigenvalues: {evals[:6]}")
        c1v, c2v, c3v, c4v, s1v, s2v, s3v, s4v = vals
        def feas(c1v, c2v, c3v, c4v, s1v, s2v, s3v, s4v):
            print("  feasibility at moment-mean (may not be an atom):")
            for j, (cv, sv) in enumerate(zip([c1v,c2v,c3v,c4v],[s1v,s2v,s3v,s4v]), start=1):
                print(f"    sphere_{j}: c^2+s^2-1 = {cv*cv+sv*sv-1:+.4e}")
            ALc_v = c4v - (c1v*c2v - s1v*s2v)
            ALs_v = s4v - (s1v*c2v + c1v*s2v)
            print(f"    AL_c = {ALc_v:+.4e},  AL_s = {ALs_v:+.4e}")
            a1v = c1v - c4v/SQRT2
            a2v = c2v
            a3v = c3v + c4v/SQRT2
            a4v = c4v + (c3v - c1v)/SQRT2
            FO1v = s3v*a3v
            FO2v = s1v*a1v - s2v*a2v
            FO3v = s1v*a1v + s4v*a4v
            print(f"    FO1 = {FO1v:+.4e}, FO2 = {FO2v:+.4e}, FO3 = {FO3v:+.4e}")
            omega2v = c1v**2+c2v**2+c3v**2+c4v**2 + SQRT2*c4v*(c3v - c1v)
            print(f"    |omega|^2 = {omega2v:+.4e} (need >= {EPS_ND})")
            Pv = (5.0/8.0)*(c1v**2+c2v**2+c3v**2+c4v**2) + (SQRT2/8.0)*c4v*(13*c3v - 5*c1v)
            print(f"    P at mean = {Pv:+.6f}")
            return Pv
        feas(c1v, c2v, c3v, c4v, s1v, s2v, s3v, s4v)
    return problem.value

def main():
    overall_t0 = time.time()
    print("Attempt 856: Tight SOS with POLYNOMIAL angle-link at attempt_852 config")
    print("  target: P(c) >= 0 on tight set (spheres + AL + FO + NONDEG)")
    print(f"  NONDEG epsilon = {EPS_ND}")
    print(f"  P monomials: {len(P)}")
    for alpha, coef in sorted(P.items(), key=lambda kv: (sum(kv[0]), kv[0])):
        print(f"    P[{mono_str(alpha):20s}] = {coef:+.6f}")

    degrees_to_try = [int(x) for x in (sys.argv[1].split(',') if len(sys.argv) > 1 else ['2'])]
    for d in degrees_to_try:
        try:
            v = run_relaxation(d)
            print(f"\n--> d={d}: min P lower bound = {v}")
        except Exception as e:
            print(f"d={d} crashed: {e}")
            import traceback; traceback.print_exc()
    print(f"\nTOTAL runtime: {time.time()-overall_t0:.1f}s")

if __name__ == '__main__':
    main()
