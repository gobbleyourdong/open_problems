"""
Attempt 857 — Lasserre moment relaxation of the TIGHT N=4 first-order vorticity-MAX
system at attempt_852's configuration, with the polynomial angle-link AND the
second-order Hessian-NSD condition encoded as a 3x3 MATRIX-PSD localizer.

This is attempt_856 plus Hessian-NSD. Expected: SOS closes to P_min >= 0.

Variables (8): c1..c4, s1..s4 at indices 0..7.
Configuration (attempt_852):
  k_1 = e1, k_2 = e2, k_3 = e3, k_4 = (1,1,0)
  v_1 = e2, v_2 = e3, v_3 = e1, v_4 = (1,-1,0)/sqrt2

Mv (polarization Gram) entries: diag 1; Mv[0,3] = -1/sqrt2, Mv[2,3] = +1/sqrt2,
others zero.

Hessian polynomial entries (derived symbolically and numerically verified in
the attempt report):

  H_{11} = -2 c1^2 + 2 sqrt2 c1 c4 - sqrt2 c3 c4 - 2 c4^2 + 2 s1^2 - 2 sqrt2 s1 s4 + 2 s4^2
  H_{22} = sqrt2 c1 c4 - 2 c2^2 - sqrt2 c3 c4 - 2 c4^2 + 2 s2^2 + 2 s4^2
  H_{33} = -2 c3^2 - sqrt2 c3 c4 + 2 s3^2
  H_{12} = sqrt2 c1 c4 - sqrt2 c3 c4 - 2 c4^2 - sqrt2 s1 s4 + 2 s4^2
  H_{13} = sqrt2 s3 s4
  H_{23} = sqrt2 s3 s4

All entries are degree 2 polynomials in (c, s).

The Hessian-NSD condition (needed for local MAX of |omega|^2) is:
   -H(c, s)  is PSD   (equivalently H is NSD).

In Lasserre moment relaxation at order d, this is a MATRIX-PSD localizer:
we build a block matrix B of size 3*M x 3*M with
  B[(i,a), (j,b)] = Sum_beta  (-H)_{ij}[beta] * y_{u_a + u_b + beta}
where {u_a} are half-monomials of degree <= d - 1 (since deg(H)=2). B >> 0.

For d = 2: M = C(8+1, 1) = 9, block size = 27. Tractable.
For d = 3: M = C(8+2, 2) = 45, block size = 135.
"""
import itertools
import time
import sys
import numpy as np
import cvxpy as cp

SQRT2 = np.sqrt(2.0)
EPS_ND = 1e-3

n_vars = 8  # (c1, c2, c3, c4, s1, s2, s3, s4)

def monomials(max_deg, n=n_vars):
    out = set()
    for total in range(max_deg + 1):
        for combo in itertools.combinations_with_replacement(range(n), total):
            alpha = [0] * n
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

# Atomic polynomials
c1 = mono(1,0,0,0,0,0,0,0)
c2 = mono(0,1,0,0,0,0,0,0)
c3 = mono(0,0,1,0,0,0,0,0)
c4 = mono(0,0,0,1,0,0,0,0)
s1 = mono(0,0,0,0,1,0,0,0)
s2 = mono(0,0,0,0,0,1,0,0)
s3 = mono(0,0,0,0,0,0,1,0)
s4 = mono(0,0,0,0,0,0,0,1)
one = {(0,)*n_vars: 1.0}

# ||c||^2 and omega^2
cnorm2 = poly_add(poly_add(poly_add(poly_mul(c1,c1), poly_mul(c2,c2)),
                           poly_mul(c3,c3)), poly_mul(c4,c4))
off_omega = poly_scale(poly_mul(c4, poly_add(c3, poly_scale(c1, -1.0))), SQRT2)
omega2 = poly_add(cnorm2, off_omega)

# P(c)
lin_P = poly_add(poly_scale(c3, 13.0), poly_scale(c1, -5.0))
P = poly_add(poly_scale(cnorm2, 5.0/8.0),
             poly_scale(poly_mul(c4, lin_P), SQRT2/8.0))

# Sphere equalities
sphere_1 = poly_add(poly_add(poly_mul(c1,c1), poly_mul(s1,s1)), poly_scale(one, -1.0))
sphere_2 = poly_add(poly_add(poly_mul(c2,c2), poly_mul(s2,s2)), poly_scale(one, -1.0))
sphere_3 = poly_add(poly_add(poly_mul(c3,c3), poly_mul(s3,s3)), poly_scale(one, -1.0))
sphere_4 = poly_add(poly_add(poly_mul(c4,c4), poly_mul(s4,s4)), poly_scale(one, -1.0))

# Angle-link
c1c2 = poly_mul(c1, c2)
s1s2 = poly_mul(s1, s2)
s1c2 = poly_mul(s1, c2)
c1s2 = poly_mul(c1, s2)
AL_c = poly_add(c4, poly_scale(poly_add(c1c2, poly_scale(s1s2, -1.0)), -1.0))
AL_s = poly_add(s4, poly_scale(poly_add(s1c2, c1s2), -1.0))

# First-order
a1 = poly_add(c1, poly_scale(c4, -1.0/SQRT2))
a2 = c2
a3 = poly_add(c3, poly_scale(c4, 1.0/SQRT2))
a4 = poly_add(c4, poly_scale(poly_add(c3, poly_scale(c1, -1.0)), 1.0/SQRT2))
FO_1 = poly_mul(s3, a3)
FO_2 = poly_add(poly_mul(s1, a1), poly_scale(poly_mul(s2, a2), -1.0))
FO_3 = poly_add(poly_mul(s1, a1), poly_mul(s4, a4))

eq_list = [
    ("sphere1", sphere_1), ("sphere2", sphere_2),
    ("sphere3", sphere_3), ("sphere4", sphere_4),
    ("AL_c", AL_c), ("AL_s", AL_s),
    ("FO_1_C1", FO_1), ("FO_2_C2", FO_2), ("FO_3_C3", FO_3),
]

# Box + NONDEG
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

# ---- Hessian polynomial matrix entries (NEW for attempt 857) ----
# H_{11} = -2 c1^2 + 2 sqrt2 c1 c4 - sqrt2 c3 c4 - 2 c4^2 + 2 s1^2 - 2 sqrt2 s1 s4 + 2 s4^2
H11 = poly_add(poly_scale(poly_mul(c1,c1), -2.0),
       poly_add(poly_scale(poly_mul(c1,c4), 2*SQRT2),
        poly_add(poly_scale(poly_mul(c3,c4), -SQRT2),
         poly_add(poly_scale(poly_mul(c4,c4), -2.0),
          poly_add(poly_scale(poly_mul(s1,s1), 2.0),
           poly_add(poly_scale(poly_mul(s1,s4), -2*SQRT2),
                    poly_scale(poly_mul(s4,s4), 2.0)))))))

# H_{22} = sqrt2 c1 c4 - 2 c2^2 - sqrt2 c3 c4 - 2 c4^2 + 2 s2^2 + 2 s4^2
H22 = poly_add(poly_scale(poly_mul(c1,c4), SQRT2),
       poly_add(poly_scale(poly_mul(c2,c2), -2.0),
        poly_add(poly_scale(poly_mul(c3,c4), -SQRT2),
         poly_add(poly_scale(poly_mul(c4,c4), -2.0),
          poly_add(poly_scale(poly_mul(s2,s2), 2.0),
                   poly_scale(poly_mul(s4,s4), 2.0))))))

# H_{33} = -2 c3^2 - sqrt2 c3 c4 + 2 s3^2
H33 = poly_add(poly_scale(poly_mul(c3,c3), -2.0),
       poly_add(poly_scale(poly_mul(c3,c4), -SQRT2),
                poly_scale(poly_mul(s3,s3), 2.0)))

# H_{12} = sqrt2 c1 c4 - sqrt2 c3 c4 - 2 c4^2 - sqrt2 s1 s4 + 2 s4^2
H12 = poly_add(poly_scale(poly_mul(c1,c4), SQRT2),
       poly_add(poly_scale(poly_mul(c3,c4), -SQRT2),
        poly_add(poly_scale(poly_mul(c4,c4), -2.0),
         poly_add(poly_scale(poly_mul(s1,s4), -SQRT2),
                  poly_scale(poly_mul(s4,s4), 2.0)))))

# H_{13} = sqrt2 s3 s4
H13 = poly_scale(poly_mul(s3,s4), SQRT2)
# H_{23} = sqrt2 s3 s4
H23 = poly_scale(poly_mul(s3,s4), SQRT2)

# -H (what we want PSD)
def neg(p): return poly_scale(p, -1.0)

negH = [
    [neg(H11), neg(H12), neg(H13)],
    [neg(H12), neg(H22), neg(H23)],
    [neg(H13), neg(H23), neg(H33)],
]

# Sanity: verify Hessian at numeric point matches attempt_856 saddle H eigenvalues
def _sanity_hessian():
    # At saddle: c = (-0.52880671, 0.08638858, 1.0, -0.89125214)
    #            s = ( 0.84874228, 0.99626152, 0.0,  -0.45350813)
    vals = {'c1':-0.52880671,'c2':0.08638858,'c3':1.0,'c4':-0.89125214,
            's1':0.84874228,'s2':0.99626152,'s3':0.0,'s4':-0.45350813}
    def evalp(p):
        tot = 0.0
        names=('c1','c2','c3','c4','s1','s2','s3','s4')
        for alpha, coef in p.items():
            v = coef
            for i, e in enumerate(alpha):
                if e>0:
                    v *= vals[names[i]]**e
            tot += v
        return tot
    Hmat = np.array([[evalp(H11), evalp(H12), evalp(H13)],
                     [evalp(H12), evalp(H22), evalp(H23)],
                     [evalp(H13), evalp(H23), evalp(H33)]])
    evals = np.linalg.eigvalsh(Hmat)
    print(f"Sanity (saddle x*): H eigenvalues = {evals}")
    print(f"  Expected from attempt_856:  (-0.7396, +1.7168, +4.3892)")
_sanity_hessian()

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

    # Localizers for inequalities (scalar PSD)
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

    # --- NEW: matrix-PSD localizer for -H(c,s) (the Hessian NSD condition) ---
    # deg(H)=2, so dloc_H = d - 1 (half-monomials of degree <= d-1)
    dloc_H = d - 1
    if dloc_H < 0:
        print(f"  cannot add Hessian-NSD localizer at d={d} (need d>=1)")
    else:
        H_half = monomials(dloc_H)
        Mh = len(H_half)
        Bsz = 3 * Mh
        print(f"  Hessian-NSD matrix-PSD localizer: half-deg={dloc_H}, |halfH|={Mh}, block size={Bsz}x{Bsz}")
        sys.stdout.flush()
        B = cp.Variable((Bsz, Bsz), symmetric=True)
        # Build B[(i, a), (j, b)] = sum_beta (-H)_{ij}[beta] * y_{u_a + u_b + beta}
        t_build = time.time()
        for i in range(3):
            for j in range(3):
                g = negH[i][j]
                for a in range(Mh):
                    for b in range(Mh):
                        alpha_ab = tuple(H_half[a][k] + H_half[b][k] for k in range(n_vars))
                        expr = 0.0
                        for beta, coef in g.items():
                            gam = tuple(alpha_ab[k] + beta[k] for k in range(n_vars))
                            if gam in mono_idx:
                                expr = expr + coef * y[mono_idx[gam]]
                        cs.append(B[3*a + i, 3*b + j] == expr)
        cs.append(B >> 0)
        print(f"    matrix-PSD block constraints added in {time.time()-t_build:.1f}s")
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
    print(f"  optimal value (lower bound on min P over tight-MAX set): {problem.value}")
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
    return problem.value

def main():
    overall_t0 = time.time()
    print("Attempt 857: Tight SOS with polynomial angle-link AND Hessian-NSD matrix-PSD localizer")
    print("             at attempt_852 config (k_4 = (1,1,0) integer lattice)")
    print(f"  NONDEG epsilon = {EPS_ND}")
    print(f"  P monomials: {len(P)}")
    for alpha, coef in sorted(P.items(), key=lambda kv: (sum(kv[0]), kv[0])):
        print(f"    P[{mono_str(alpha):20s}] = {coef:+.6f}")

    degrees_to_try = [int(x) for x in (sys.argv[1].split(',') if len(sys.argv) > 1 else ['2'])]
    results = {}
    for d in degrees_to_try:
        try:
            v = run_relaxation(d)
            results[d] = v
            print(f"\n--> d={d}: min P lower bound = {v}")
        except Exception as e:
            print(f"d={d} crashed: {e}")
            import traceback; traceback.print_exc()
    print(f"\nTOTAL runtime: {time.time()-overall_t0:.1f}s")
    print(f"Summary: {results}")
    print(f"attempt_856 baseline (no Hessian-NSD): min P = -1.16386")

if __name__ == '__main__':
    main()
