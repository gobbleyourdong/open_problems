"""
Lasserre moment relaxation at degree d=3 (moments up to deg 6).
Also attempts proper atom extraction from the moment matrix.
"""
import itertools
import numpy as np
import cvxpy as cp

SQRT2 = np.sqrt(2.0)
n_vars = 4

def monomials(max_deg, n=n_vars):
    out = set()
    for total in range(max_deg+1):
        for combo in itertools.combinations_with_replacement(range(n), total):
            alpha = [0]*n
            for i in combo: alpha[i] += 1
            out.add(tuple(alpha))
    return sorted(out, key=lambda a: (sum(a), a))

def mono(*powers): return {tuple(powers): 1.0}
def poly_add(p, q):
    r = dict(p)
    for k,v in q.items(): r[k] = r.get(k, 0.0) + v
    return {k:v for k,v in r.items() if abs(v) > 1e-15}
def poly_scale(p, c): return {k: c*v for k,v in p.items() if abs(c*v) > 1e-15}
def poly_mul(p, q):
    r = {}
    for ka, va in p.items():
        for kb, vb in q.items():
            kc = tuple(ka[i]+kb[i] for i in range(n_vars))
            r[kc] = r.get(kc, 0.0) + va*vb
    return {k:v for k,v in r.items() if abs(v) > 1e-15}
def poly_degree(p): return max((sum(k) for k in p), default=0)

a = mono(1,0,0,0); b = mono(0,1,0,0); c2 = mono(0,0,1,0); c4 = mono(0,0,0,1)
one = {(0,0,0,0): 1.0}
P = poly_add(poly_add(poly_add(
        poly_scale(poly_mul(a,a), 5/8),
        poly_scale(poly_mul(b,b), 5/8)),
        poly_scale(poly_mul(c2,c2), 5/8)),
        poly_add(
            poly_scale(poly_mul(c4, poly_add(poly_add(a,c2), poly_scale(b,-2))), -SQRT2/3),
            poly_scale(poly_mul(c4,c4), -1)
        ))

c1 = poly_add(a, poly_scale(c4, 1.0/SQRT2))
c3 = poly_add(b, poly_scale(c4, -1.0/SQRT2))
g_box1 = poly_add(one, poly_scale(poly_mul(c1,c1), -1))
g_box2 = poly_add(one, poly_scale(poly_mul(c3,c3), -1))
g_box3 = poly_add(one, poly_scale(poly_mul(c2,c2), -1))
g_box4 = poly_add(one, poly_scale(poly_mul(c4,c4), -1))
g_F1   = poly_add(poly_scale(one, 0.25), poly_scale(poly_mul(g_box1, poly_mul(a,a)), -1))
g_F3   = poly_add(poly_scale(one, 0.25), poly_scale(poly_mul(g_box2, poly_mul(b,b)), -1))
bma = poly_add(b, poly_scale(a, -1))
g_F    = poly_add(poly_scale(one, 1.5), poly_scale(poly_mul(g_box4, poly_mul(bma,bma)), -1))
g_ND = poly_add(poly_add(poly_add(poly_add(
            poly_mul(a,a), poly_mul(b,b)), poly_mul(c2,c2)),
            poly_scale(poly_mul(c4,c4), 2)),
            poly_scale(poly_mul(c4, poly_add(a, poly_scale(b,-1))), SQRT2))

constraints_list = [
    ("box1", g_box1), ("box2", g_box2), ("box3", g_box3), ("box4", g_box4),
    ("F1p", g_F1), ("F3p", g_F3), ("Fp", g_F), ("ND", g_ND)
]

for d in [3]:
    print(f"\n=== Lasserre relaxation order d={d} (moments up to {2*d}) ===")
    half_mons = monomials(d)
    full_mons = monomials(2*d)
    mono_idx = {m:i for i,m in enumerate(full_mons)}
    print(f"  |half|={len(half_mons)}, |full|={len(full_mons)}")

    y = cp.Variable(len(full_mons), name='y')
    cs = [y[mono_idx[(0,)*n_vars]] == 1]

    sz = len(half_mons)
    M = cp.Variable((sz, sz), symmetric=True)
    for i in range(sz):
        for j in range(sz):
            alpha = tuple(half_mons[i][k] + half_mons[j][k] for k in range(n_vars))
            cs.append(M[i,j] == y[mono_idx[alpha]])
    cs.append(M >> 0)

    L_vars = {}
    for name, g in constraints_list:
        dg = poly_degree(g)
        dloc = d - (dg + 1) // 2
        if dloc < 0:
            print(f"  skipping {name} (deg(g)={dg})")
            continue
        loc_mons = monomials(dloc)
        sz_l = len(loc_mons)
        L = cp.Variable((sz_l, sz_l), symmetric=True)
        L_vars[name] = (L, loc_mons)
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
        print(f"  localizer {name}: deg(g)={dg}, dloc={dloc}, size={sz_l}")

    obj_expr = sum(coef * y[mono_idx[alpha]] for alpha, coef in P.items())
    problem = cp.Problem(cp.Minimize(obj_expr), cs)
    print(f"  Solving...")
    problem.solve(solver='SCS', verbose=False, max_iters=500000, eps=1e-7)
    print(f"  Status: {problem.status}")
    print(f"  Lower bound on min_S P = {problem.value:.6f}")

    # Extract atom: rank-1 decomposition of M_d
    Mval = np.array(M.value)
    evals, evecs = np.linalg.eigh(Mval)
    print(f"  M_d eigenvalues (top 6): {evals[-6:]}")
    print(f"  (smaller eigenvalues near 0 indicate moment matrix rank = # atoms)")

    # Degree-1 moments give the expected values of a,b,c2,c4 (as a mixture)
    idx_a = half_mons.index((1,0,0,0))
    idx_b = half_mons.index((0,1,0,0))
    idx_c2 = half_mons.index((0,0,1,0))
    idx_c4 = half_mons.index((0,0,0,1))
    print(f"  E[a]={Mval[0,idx_a]:.5f}, E[b]={Mval[0,idx_b]:.5f}, E[c2]={Mval[0,idx_c2]:.5f}, E[c4]={Mval[0,idx_c4]:.5f}")

    # If the optimum is an atomic measure at a single atom, eigen-extract:
    # Largest eigenvector gives (up to sign/normalization) a character of the atom.
    # Normalize by value at monomial '1': vec / vec[idx_one]
    idx_one = 0
    v = evecs[:, -1]
    if abs(v[idx_one]) > 1e-6:
        v = v / v[idx_one]
        print(f"  Top eigenvector normalized at 1: (a,b,c2,c4) ~ ({v[idx_a]:.5f}, {v[idx_b]:.5f}, {v[idx_c2]:.5f}, {v[idx_c4]:.5f})")
        a_s, b_s, c2_s, c4_s = v[idx_a], v[idx_b], v[idx_c2], v[idx_c4]
        Pval = (5.0/8.0)*(a_s**2+b_s**2+c2_s**2) - (SQRT2/3.0)*c4_s*(a_s+c2_s-2*b_s) - c4_s**2
        print(f"  P at top-eigenvector candidate: {Pval:.6f}")
        # Feasibility
        c1_s = a_s + c4_s/SQRT2; c3_s = b_s - c4_s/SQRT2
        print(f"    c1={c1_s:.5f}, c3={c3_s:.5f}, c2={c2_s:.5f}, c4={c4_s:.5f}")
        print(f"    |c1|<=1? {abs(c1_s)<=1+1e-4}, |c3|<=1? {abs(c3_s)<=1+1e-4}, |c2|<=1? {abs(c2_s)<=1+1e-4}, |c4|<=1? {abs(c4_s)<=1+1e-4}")
        F1v = (1-c1_s**2)*a_s**2; F3v = (1-c3_s**2)*b_s**2; Fv = (1-c4_s**2)*(b_s-a_s)**2
        NDv = a_s**2+b_s**2+c2_s**2+2*c4_s**2+SQRT2*c4_s*(a_s-b_s)
        print(f"    F1'={F1v:.4f} (<=0.25)? {F1v<=0.25+1e-4}")
        print(f"    F3'={F3v:.4f} (<=0.25)? {F3v<=0.25+1e-4}")
        print(f"    F'={Fv:.4f} (<=1.5)? {Fv<=1.5+1e-4}")
        print(f"    ND={NDv:.4f} (>0)? {NDv>0}")
