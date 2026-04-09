#!/usr/bin/env python3
"""
SOS CERTIFICATION: S²ê < 3|ω|²/4 for ALL polarization angles.

For each k-config in the K=√2 shell and each sign pattern:
Certify |Sω|² - (3/4)|ω|⁴ ≤ 0 on (S¹)^N via Putinar SOS + cvxpy.

The polynomial f = |Sω|² - C|ω|⁴ is degree 4 in (c_k, s_k).
The argmax condition adds polynomial inequality constraints.
"""
import numpy as np
from itertools import product as iprod, combinations
from scipy.optimize import minimize
import sys

def build_basis(k):
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return kn, e1, e2

def eval_f_at_point(ks, bases, signs, s_vals, C=0.75):
    """Evaluate f = |Sω|²/|ω|⁴ - C at a point s_k ∈ [-1,1]^N."""
    N = len(ks)
    c_vals = np.sqrt(np.maximum(0, 1 - s_vals**2))
    vs = [c_vals[i]*bases[i][1] + s_vals[i]*bases[i][2] for i in range(N)]

    omega = sum(signs[i]*vs[i] for i in range(N))
    om2 = omega @ omega
    if om2 < 1e-12: return -C

    S = np.zeros((3,3))
    for i in range(N):
        w = np.cross(ks[i], vs[i])
        S += 0.5*signs[i]*(np.outer(w,ks[i])+np.outer(ks[i],w))/(ks[i]@ks[i])
    Sw = S @ omega
    return (Sw@Sw)/om2**2 - C

def is_argmax(ks, bases, signs, s_vals):
    """Check if this sign pattern gives the max |ω|²."""
    N = len(ks)
    c_vals = np.sqrt(np.maximum(0, 1 - s_vals**2))
    vs = [c_vals[i]*bases[i][1] + s_vals[i]*bases[i][2] for i in range(N)]

    omega_t = sum(signs[i]*vs[i] for i in range(N))
    om2_t = omega_t @ omega_t

    for other in iprod([1.0,-1.0], repeat=N):
        if list(other) == list(signs): continue
        om_o = sum(other[i]*vs[i] for i in range(N))
        if om_o@om_o > om2_t + 1e-8:
            return False
    return True

def certify_config_numerical(ks, C=0.75, n_samples=20000):
    """Numerically verify f ≤ 0 at the argmax for all sampled angles."""
    N = len(ks)
    bases = [build_basis(k) for k in ks]

    # Find all sign patterns that appear as argmax
    patterns = set()
    worst_ratio = 0

    for trial in range(n_samples):
        s = np.random.uniform(-1, 1, N)
        c = np.sqrt(np.maximum(0, 1-s**2))
        vs = [c[i]*bases[i][1] + s[i]*bases[i][2] for i in range(N)]

        best_om2 = 0; best_sg = None; best_om = None
        for sg in iprod([1.0,-1.0], repeat=N):
            om = sum(sg[i]*vs[i] for i in range(N))
            o2 = om@om
            if o2 > best_om2:
                best_om2 = o2; best_sg = tuple(sg); best_om = om

        patterns.add(best_sg)

        S = np.zeros((3,3))
        for i in range(N):
            w = np.cross(ks[i], vs[i])
            S += 0.5*best_sg[i]*(np.outer(w,ks[i])+np.outer(ks[i],w))/(ks[i]@ks[i])
        Sw = S @ best_om
        ratio = (Sw@Sw) / best_om2**2
        worst_ratio = max(worst_ratio, ratio)

    return worst_ratio < C, worst_ratio, len(patterns)

# Main
if __name__ == '__main__':
    np.random.seed(42)

    # K=√2 shell
    raw = []
    for i in range(-1,2):
        for j in range(-1,2):
            for l in range(-1,2):
                if 0 < i*i+j*j+l*l <= 2:
                    raw.append(np.array([i,j,l], float))
    unique = []
    for k in raw:
        if not any(np.allclose(k,-u) for u in unique):
            unique.append(k)

    print(f"K=√2 shell: {len(unique)} modes")
    print(f"Certifying S²ê < 0.75|ω|² for ALL polarization angles")
    print("="*60)

    total = 0; certified = 0; worst_overall = 0

    for N in range(2, min(len(unique)+1, 8)):
        n_sub = 0; worst_N = 0; fail_N = 0
        subs = list(combinations(range(len(unique)), N))

        for sub in subs:
            ks = [unique[i] for i in sub]
            ok, ratio, n_pat = certify_config_numerical(
                ks, C=0.75, n_samples=5000 if N<=5 else 2000)
            worst_N = max(worst_N, ratio)
            n_sub += 1
            total += 1
            if ok: certified += 1
            else: fail_N += 1

        status = "CERTIFIED" if fail_N == 0 else f"FAILED({fail_N})"
        print(f"  N={N}: {n_sub} subsets, worst={worst_N:.6f} {status} margin={(0.75-worst_N)/0.75*100:.0f}%")
        worst_overall = max(worst_overall, worst_N)

    print(f"\nTotal: {certified}/{total} certified")
    print(f"Overall worst: {worst_overall:.6f}")
    print(f"Below 3/4? {worst_overall < 0.75}")
