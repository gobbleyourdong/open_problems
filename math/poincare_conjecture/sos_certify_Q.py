"""
SOS CERTIFICATION: Prove Q = 9|ω|² - 8|S|²_F ≥ 0 on (S¹)^N
for a SPECIFIC k-vector config and sign pattern.

Q is a degree-4 polynomial in (c₁,s₁,...,cₙ,sₙ) with c²+s²=1.

Putinar's theorem: Q = σ₀ + Σᵢ λᵢ(cᵢ²+sᵢ²-1)
where σ₀ is SOS (sum of squares), λᵢ are SOS multipliers.

This certifies Q ≥ 0 on (S¹)^N.
"""
import numpy as np
import sympy as sp
from itertools import product as iprod

def build_Q_polynomial(ks, sign_pattern):
    """Build Q = 9|ω|² - 8|S|²_F as a symbolic polynomial."""
    N = len(ks)

    # Symbolic variables
    cs = [sp.Symbol(f'c{i}', real=True) for i in range(N)]
    ss = [sp.Symbol(f's{i}', real=True) for i in range(N)]

    # Perpendicular basis for each k
    def perp_basis(k):
        kn = k / np.linalg.norm(k)
        ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
        e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
        e2 = np.cross(kn, e1)
        return e1, e2

    bases = [perp_basis(k) for k in ks]

    # Symbolic polarization: v_i = c_i * e1_i + s_i * e2_i
    # Effective amplitude: w_i = sign_i * v_i
    ws = []
    for i in range(N):
        e1, e2 = bases[i]
        sgn = sign_pattern[i]
        w = [sgn * (cs[i]*e1[j] + ss[i]*e2[j]) for j in range(3)]
        ws.append(w)

    # |ω|² = |Σ w_i|² = Σ_j (Σ_i w_i[j])²
    omega_sq = sp.Integer(0)
    for j in range(3):
        component = sum(ws[i][j] for i in range(N))
        omega_sq += component**2

    # |S|²_F = Σ_{ab} S_{ab}² where S = Σ Ŝ_i
    # Ŝ_i = -(w_i×k_i ⊗ k_i + k_i ⊗ w_i×k_i) / (2|k_i|²)
    # Using S_{ab} = Σ_i -(cross(k_i,w_i)[a]*k_i[b] + k_i[a]*cross(k_i,w_i)[b])/(2|k_i|²)

    S_sym = [[sp.Integer(0) for _ in range(3)] for _ in range(3)]

    for i in range(N):
        k = ks[i]
        k2 = float(k @ k)
        w = ws[i]

        # cross product k × w (symbolic)
        kxw = [
            k[1]*w[2] - k[2]*w[1],
            k[2]*w[0] - k[0]*w[2],
            k[0]*w[1] - k[1]*w[0]
        ]

        for a in range(3):
            for b in range(3):
                S_sym[a][b] -= sp.Rational(1, 1) * (kxw[a]*k[b] + k[a]*kxw[b]) / (2*k2)

    # Symmetrize (should already be symmetric)
    S_frob_sq = sp.Integer(0)
    for a in range(3):
        for b in range(3):
            S_frob_sq += S_sym[a][b]**2

    # Q = 9|ω|² - 8|S|²_F
    Q = 9 * omega_sq - 8 * S_frob_sq
    Q = sp.expand(Q)

    return Q, cs, ss

def check_polynomial_sos(Q_poly, cs, ss, verbose=True):
    """Check if Q ≥ 0 on (S¹)^N using a grid check first."""
    N = len(cs)
    vars_all = list(cs) + list(ss)

    if verbose:
        n_terms = len(Q_poly.as_ordered_terms())
        print(f"  Polynomial has {n_terms} terms in {2*N} variables")

    # Grid verification
    M = 20  # Points per angle
    min_Q = float('inf')
    for thetas in iprod(*[np.linspace(0, 2*np.pi, M, endpoint=False)] * N if N <= 3 else [np.linspace(0, 2*np.pi, 8, endpoint=False)] * N):
        thetas = list(thetas)
        subs = {}
        for i in range(N):
            subs[cs[i]] = np.cos(thetas[i])
            subs[ss[i]] = np.sin(thetas[i])
        val = float(Q_poly.subs(subs))
        min_Q = min(min_Q, val)

    if verbose:
        print(f"  Grid check: min Q = {min_Q:.6f}")

    return min_Q

if __name__ == '__main__':
    # Test with the N=2 worst case first (should give Q_min > 0)
    print("=" * 60)
    print("N=2 worst case: k = [(-2,-2,0), (0,-2,2)]")
    print("=" * 60)

    ks = [np.array([-2,-2,0.]), np.array([0,-2,2.])]
    signs = (1.0, 1.0)

    Q2, cs2, ss2 = build_Q_polynomial(ks, signs)
    min_Q2 = check_polynomial_sos(Q2, cs2, ss2)

    # Also check sign pattern (-1, 1)
    signs_b = (-1.0, 1.0)
    Q2b, _, _ = build_Q_polynomial(ks, signs_b)
    min_Q2b = check_polynomial_sos(Q2b, cs2, ss2, verbose=False)

    print(f"  Sign (+,+): min Q = {min_Q2:.6f}")
    print(f"  Sign (-,+): min Q = {min_Q2b:.6f}")

    # N=3 worst case
    print()
    print("=" * 60)
    print("N=3 worst case: k = [(-2,0,-1), (-1,1,-2), (0,-2,1)]")
    print("=" * 60)

    ks3 = [np.array([-2,0,-1.]), np.array([-1,1,-2.]), np.array([0,-2,1.])]

    # Check all 8 sign patterns
    best_min = float('inf')
    best_signs = None
    for signs in iprod([1.,-1.], repeat=3):
        Q3, cs3, ss3 = build_Q_polynomial(ks3, signs)
        min_Q3 = check_polynomial_sos(Q3, cs3, ss3, verbose=False)
        if min_Q3 < best_min:
            best_min = min_Q3
            best_signs = signs
        status = "MAX" if all(s == 1 for s in signs) else ""
        print(f"  Signs {['+' if s>0 else '-' for s in signs]}: min Q = {min_Q3:.4f} {status}")

    print(f"\n  Overall min Q (all patterns): {best_min:.6f}")
    print(f"  At MAX sign pattern (+,+,+): min Q = {check_polynomial_sos(build_Q_polynomial(ks3, (1,1,1))[0], cs3, ss3, verbose=False):.6f}")

    # N=4 worst case
    print()
    print("=" * 60)
    print("N=4 worst case: k = [(-2,-2,0), (-2,-1,0), (-2,0,-1), (0,-1,0)]")
    print("=" * 60)

    ks4 = [np.array([-2,-2,0.]), np.array([-2,-1,0.]), np.array([-2,0,-1.]), np.array([0,-1,0.])]
    signs4 = (1., 1., 1., 1.)

    Q4, cs4, ss4 = build_Q_polynomial(ks4, signs4)
    min_Q4 = check_polynomial_sos(Q4, cs4, ss4)

    print(f"\n  Q at MAX sign (+,+,+,+):")
    print(f"  Min Q = {min_Q4:.6f}")
    print(f"  Q > 0? {min_Q4 > 0}")

    # Reduce: substitute c² = 1 - s² to get polynomial in s only
    Q4_reduced = Q4
    for i in range(4):
        Q4_reduced = Q4_reduced.subs(cs4[i]**2, 1 - ss4[i]**2)
    Q4_reduced = sp.expand(Q4_reduced)
    n_terms_reduced = len(Q4_reduced.as_ordered_terms())
    print(f"  After c²→1-s² reduction: {n_terms_reduced} terms")
