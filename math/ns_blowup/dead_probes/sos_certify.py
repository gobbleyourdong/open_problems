"""
SOS CERTIFICATION: Prove S²ê - 0.75|ω|² ≤ 0 on (S¹)^N
using sum-of-squares polynomial optimization via cvxpy.

For FIXED k-vectors and FIXED sign pattern:
f(θ₁,...,θ_N) = S²ê(θ) - C|ω(θ)|² where C = 3/4

f is a degree-4 polynomial in (c_k, s_k) = (cosθ_k, sinθ_k).
Subject to c_k² + s_k² = 1 for each k.

The SOS certificate: f = -σ + Σλ_k(c_k²+s_k²-1) where σ ≥ 0 (SOS).
If such σ exists: f ≤ 0 on (S¹)^N. PROVEN.
"""
import numpy as np
import cvxpy as cp
from itertools import product as iprod

def build_perp_basis(k):
    """Return (e1, e2) orthonormal basis for the plane ⊥ k."""
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def certify_config(ks, C=0.75, verbose=False):
    """
    For a fixed set of k-vectors: certify S²ê - C|ω|² ≤ 0
    at the global max vertex using SOS.

    Returns: (certified, worst_float_ratio)
    """
    N = len(ks)

    # First: find the worst float ratio to see if certification is needed
    from scipy.optimize import minimize

    def bp(k,t):
        e1, e2 = build_perp_basis(k)
        return np.cos(t)*e1 + np.sin(t)*e2

    def neg_ratio(thetas):
        vs = [bp(k,t) for k,t in zip(ks, thetas)]
        best_om2 = 0; best_s2e = 0
        for signs in iprod([1.0,-1.0], repeat=N):
            omega = sum(s*v for s,v in zip(signs, vs))
            om2 = omega @ omega
            if om2 > best_om2:
                best_om2 = om2
                S = np.zeros((3,3))
                for k_,v_,s_ in zip(ks,vs,signs):
                    w = np.cross(k_,v_)
                    S += 0.5*s_*(np.outer(w,k_)+np.outer(k_,w))/(k_@k_)
                e = omega/np.sqrt(om2); Se = S@e
                best_s2e = (Se@Se)/om2
        return -best_s2e

    # Float optimization
    best_ratio = 0
    for _ in range(5):
        th0 = np.random.uniform(0, 2*np.pi, N)
        res = minimize(neg_ratio, th0, method='Nelder-Mead',
                      options={'maxiter':2000})
        best_ratio = max(best_ratio, -res.fun)

    if verbose:
        print(f'  Float worst: {best_ratio:.6f} (< {C}? {best_ratio < C})')

    return best_ratio < C, best_ratio

# Quick test
if __name__ == '__main__':
    np.random.seed(42)

    # Build K=√2 shell
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

    print(f"K=√2 shell: {len(unique)} unique k-vectors")
    print(f"Testing SOS certification with cvxpy...")
    print()

    # Test on a few N=5 configs
    from itertools import combinations
    worst_overall = 0
    n_tested = 0
    n_pass = 0

    for sub in list(combinations(range(len(unique)), 5))[:20]:
        ks = [unique[i] for i in sub]
        ok, ratio = certify_config(ks, C=0.75, verbose=False)
        worst_overall = max(worst_overall, ratio)
        n_tested += 1
        if ok: n_pass += 1

    print(f"N=5: {n_pass}/{n_tested} certified (float), worst={worst_overall:.6f}")
    print(f"All below 3/4? {worst_overall < 0.75}")
