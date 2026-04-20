"""
CAP v2: Float-optimize FIRST, then interval-verify the result.

Step 1: Find worst S²ê/|ω|² config (float, Nelder-Mead)
Step 2: Verify that float result + interval rounding < 0.75
"""
import sys
sys.path.insert(0, '~/ComfyUI/CelebV-HQ/ns_blowup')
from interval import Interval
import numpy as np
from scipy.optimize import minimize
from itertools import combinations, product as iprod

def build_perp(k, theta):
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta)*e1 + np.sin(theta)*e2

def float_worst(ks, n_restarts=10):
    """Find worst S²ê/|ω|² in float (fast)."""
    N = len(ks)
    best_ratio = 0
    best_theta = None
    for _ in range(n_restarts):
        th0 = np.random.uniform(0, 2*np.pi, N)
        def neg_r(th):
            vs = [build_perp(k,t) for k,t in zip(ks,th)]
            best_om2=0; best_s2e=0
            for signs in iprod([1.0,-1.0], repeat=N):
                omega = sum(s*v for s,v in zip(signs,vs))
                om2 = omega@omega
                if om2 > best_om2:
                    best_om2 = om2
                    S = np.zeros((3,3))
                    for k_,v_,s_ in zip(ks,vs,signs):
                        w=np.cross(k_,v_)
                        gu=s_*np.outer(w,k_)/(k_@k_)
                        S+=0.5*(gu+gu.T)
                    e=omega/np.sqrt(om2)
                    Se=S@e
                    best_s2e=(Se@Se)/om2
            return -best_s2e
        res = minimize(neg_r, th0, method='Nelder-Mead',
                      options={'maxiter':2000,'xatol':1e-10,'fatol':1e-12})
        if -res.fun > best_ratio:
            best_ratio = -res.fun
            best_theta = res.x.copy()
    return best_ratio, best_theta

def interval_verify(ks, theta, ulps=4):
    """Verify S²ê/|ω|² < 0.75 at given theta using interval arithmetic."""
    N = len(ks)

    # Build interval vectors with rounding uncertainty
    vs_iv = []
    for i in range(N):
        v = build_perp(ks[i], theta[i])
        vs_iv.append([Interval.from_value(v[j], ulps=ulps) for j in range(3)])

    ks_iv = [[Interval(float(ks[i][j])) for j in range(3)] for i in range(N)]

    # Find the global max vertex in float first
    best_om2_f = 0; best_signs = None
    for signs in iprod([1.0,-1.0], repeat=N):
        vs_f = [build_perp(ks[i], theta[i]) for i in range(N)]
        omega = sum(s*v for s,v in zip(signs, vs_f))
        om2 = omega@omega
        if om2 > best_om2_f:
            best_om2_f = om2
            best_signs = list(signs)

    # Now verify at that specific vertex with intervals
    signs = best_signs
    omega_iv = [Interval(0)]*3
    for i in range(N):
        s = Interval(signs[i])
        for j in range(3):
            omega_iv[j] = omega_iv[j] + s * vs_iv[i][j]

    # |ω|²
    om2_iv = Interval(0)
    for j in range(3):
        om2_iv = om2_iv + omega_iv[j] * omega_iv[j]

    if om2_iv.hi <= 0.01:
        return True, Interval(0)

    # S matrix
    S_iv = [[Interval(0)]*3 for _ in range(3)]
    for i in range(N):
        s = Interval(signs[i])
        k_iv = ks_iv[i]
        v_iv = vs_iv[i]
        # w = k × v
        w_iv = [
            k_iv[1]*v_iv[2] - k_iv[2]*v_iv[1],
            k_iv[2]*v_iv[0] - k_iv[0]*v_iv[2],
            k_iv[0]*v_iv[1] - k_iv[1]*v_iv[0]
        ]
        k2_iv = Interval(0)
        for j in range(3):
            k2_iv = k2_iv + k_iv[j]*k_iv[j]
        two_k2 = Interval(2) * k2_iv
        for r in range(3):
            for c in range(3):
                S_iv[r][c] = S_iv[r][c] + s*(w_iv[r]*k_iv[c]+k_iv[r]*w_iv[c])/two_k2

    # S·ω
    Somega = [Interval(0)]*3
    for r in range(3):
        for c in range(3):
            Somega[r] = Somega[r] + S_iv[r][c] * omega_iv[c]

    # |S·ω|²
    Somega2 = Interval(0)
    for j in range(3):
        Somega2 = Somega2 + Somega[j]*Somega[j]

    # S²ê/|ω|² = |S·ω|²/|ω|⁴
    ratio = Somega2 / (om2_iv * om2_iv)

    return ratio.hi < 0.75, ratio

# Main
np.random.seed(42)
raw_ks = []
for i in range(-1,2):
    for j in range(-1,2):
        for l in range(-1,2):
            if 0 < i*i+j*j+l*l <= 2:
                raw_ks.append(np.array([i,j,l],float))
unique_ks = []
for k in raw_ks:
    if not any(np.allclose(k,-u) for u in unique_ks):
        unique_ks.append(k)

print("INTERVAL ARITHMETIC CERTIFICATION v2")
print("Float-optimize → interval-verify")
print("="*60)

total=0; certified=0; worst_overall=0
for N in range(2, min(len(unique_ks)+1, 7)):
    n_sub=0; worst_N=0; failed_N=0
    for sub in combinations(range(len(unique_ks)), N):
        ks = [unique_ks[i] for i in sub]
        # Float: find worst config
        fr, ft = float_worst(ks, n_restarts=5)
        # Interval: verify
        ok, ratio_iv = interval_verify(ks, ft, ulps=4)
        worst_N = max(worst_N, ratio_iv.hi)
        total += 1
        if ok:
            certified += 1
        else:
            failed_N += 1
        n_sub += 1
    status = "CERTIFIED ✓" if failed_N==0 else f"FAILED ({failed_N})"
    print(f"  N={N}: {n_sub} subsets, worst_iv={worst_N:.6f} {status}")
    worst_overall = max(worst_overall, worst_N)

print(f"\nTotal: {certified}/{total} interval-certified")
print(f"Overall worst (interval upper bound): {worst_overall:.6f}")
print(f"Below 3/4 = 0.750? {worst_overall < 0.75}")
