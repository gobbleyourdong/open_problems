"""
Test the identity |∇u|² and |S|² for non-orthogonal k-vectors.

For orthogonal k's: |∇u|² = N at vertices. |S|² = N - |ω|²/2.
For non-orthogonal: |∇u|² = N + 2Σ_{j<k} A_j:A_k at vertices.

Question: what is A_j:A_k for non-orthogonal k's?
Does |∇u|²/|ω|² stay bounded at the global max?
"""
import numpy as np
from scipy.optimize import minimize

def compute_all(ks, vs, x):
    """Compute ω, ∇u, S, and all relevant quantities at point x."""
    omega = np.zeros(3)
    gradu = np.zeros((3,3))

    for k, v in zip(ks, vs):
        k = np.asarray(k, float)
        v = np.asarray(v, float)
        c = np.cos(k @ x)
        w = np.cross(k, v)
        omega += v * c
        gradu += np.outer(w, k) * c / (k @ k)

    S = 0.5 * (gradu + gradu.T)
    om2 = omega @ omega
    gradu2 = np.sum(gradu**2)
    S2 = np.sum(S**2)

    if om2 < 1e-10:
        return None

    e = omega / np.sqrt(om2)
    Se = S @ e
    S2e = Se @ Se

    return {
        'om2': om2, 'gradu2': gradu2, 'S2': S2, 'S2e': S2e,
        'gradu_ratio': gradu2/om2, 'S_ratio': S2/om2, 'S2e_ratio': S2e/om2,
        'identity_check': abs(S2 - (gradu2 - om2/2)) / max(gradu2, 1e-10),
        'S2_predicted': gradu2 - om2/2,
    }

def find_global_max(ks, vs):
    best = 0
    best_x = None
    for _ in range(20):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def f(xyz):
            om = sum(np.asarray(v,float)*np.cos(np.asarray(k,float)@xyz) for k,v in zip(ks,vs))
            return -(om@om)
        res = minimize(f, x0, method='Nelder-Mead',
                      options={'xatol':1e-11,'fatol':1e-13,'maxiter':10000})
        if -res.fun > best:
            best = -res.fun
            best_x = res.x
    return best_x

def cross_term_analysis(k1, v1, k2, v2):
    """Compute the cross-term A₁:A₂ for non-orthogonal k's."""
    k1, k2 = np.asarray(k1,float), np.asarray(k2,float)
    v1, v2 = np.asarray(v1,float), np.asarray(v2,float)
    w1, w2 = np.cross(k1, v1), np.cross(k2, v2)

    # A₁ = (w₁⊗k₁)/|k₁|², A₂ = (w₂⊗k₂)/|k₂|²
    # A₁:A₂ = (w₁·w₂)(k₁·k₂) / (|k₁|²|k₂|²)
    A_cross = (w1@w2) * (k1@k2) / ((k1@k1)*(k2@k2))

    # S₁:S₂ for comparison
    A1 = np.outer(w1, k1) / (k1@k1)
    A2 = np.outer(w2, k2) / (k2@k2)
    S1 = 0.5*(A1+A1.T)
    S2 = 0.5*(A2+A2.T)
    S_cross = np.sum(S1*S2)

    # v̂₁·v̂₂
    d = v1@v2

    return A_cross, S_cross, d

np.random.seed(42)

print("CROSS-TERM ANALYSIS FOR NON-ORTHOGONAL k's")
print("=" * 60)

# Test pairs
pairs = [
    ("orthogonal", [1,0,0], [0,1,0], [0,1,0], [0,0,1]),
    ("sharing x", [1,0,0], [1,1,0], [0,1,0], [0,0,1]),
    ("sharing all", [1,1,0], [1,0,1], [0,1,0], [1,0,0]),
    ("parallel k", [1,0,0], [2,0,0], [0,1,0], [0,0,1]),
    ("anti-parallel", [1,1,0], [1,-1,0], [0,0,1], [0,0,1]),
]

for name, k1, k2, v1, v2 in pairs:
    k1,k2,v1,v2 = [np.array(x,float) for x in [k1,k2,v1,v2]]
    # Ensure div-free
    v1 -= (v1@k1)*k1/(k1@k1); v1 /= np.linalg.norm(v1)
    v2 -= (v2@k2)*k2/(k2@k2); v2 /= np.linalg.norm(v2)

    Ac, Sc, d = cross_term_analysis(k1,v1,k2,v2)
    kk = k1@k2
    print(f"  {name:15s}: k·k={kk:.0f}, A_cross={Ac:+.4f}, S_cross={Sc:+.4f}, v·v={d:+.4f}")

# For ORTHOGONAL k's: A_cross = 0, S_cross = -d/2 (verified in file 367)
# For NON-orthogonal: A_cross = (w₁·w₂)(k₁·k₂)/(|k₁|²|k₂|²) ≠ 0

print("\nGLOBAL MAX ANALYSIS: |∇u|²/|ω|² and S²ê/|ω|² for 3-mode configs")
print("=" * 60)

configs = [
    ("orth symmetric", [[1,0,0],[0,1,0],[0,0,1]], [[0,1,0],[0,0,1],[1,0,0]]),
    ("orth random", [[1,0,0],[0,1,0],[0,0,1]], None),
    ("non-orth (1,1,1)", [[1,1,0],[1,0,1],[0,1,1]], None),
    ("non-orth (1,0,0)", [[1,0,0],[1,1,0],[0,1,0]], None),
    ("high |k|", [[2,0,0],[0,2,0],[0,0,2]], None),
]

for name, ks_raw, vs_raw in configs:
    ks = [np.array(k,float) for k in ks_raw]
    worst_ratio = 0
    worst_gradu = 0

    for trial in range(200):
        if vs_raw and trial == 0:
            vs = [np.array(v,float) for v in vs_raw]
        else:
            vs = []
            for k in ks:
                v = np.random.randn(3)
                v -= (v@k)*k/(k@k)
                v /= np.linalg.norm(v)
                vs.append(v)

        x_max = find_global_max(ks, vs)
        if x_max is None: continue
        r = compute_all(ks, vs, x_max)
        if r is None: continue

        worst_ratio = max(worst_ratio, r['S2e_ratio'])
        worst_gradu = max(worst_gradu, r['gradu_ratio'])

    print(f"  {name:20s}: worst S²ê/ω²={worst_ratio:.4f}, |∇u|²/ω²={worst_gradu:.4f}")

# KEY TEST: how does |∇u|² relate to N + cross at the global max?
print("\nIDENTITY TEST: |∇u|² vs N + 2Σ cross at global max vertex")
print("=" * 60)

def rand_perp(k):
    k = np.asarray(k,float)
    kn = k/np.linalg.norm(k)
    r = np.random.randn(3)
    r -= (r@kn)*kn
    return r/np.linalg.norm(r)

for trial in range(20):
    # Random 3-mode config
    all_ks = [[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,0,1],[0,1,1]]
    idx = np.random.choice(6, 3, replace=False)
    ks = [np.array(all_ks[i],float) for i in idx]
    vs = [rand_perp(k) for k in ks]

    x_max = find_global_max(ks, vs)
    if x_max is None: continue
    r = compute_all(ks, vs, x_max)
    if r is None: continue

    # Compute cross-terms
    total_cross_A = 0
    total_cross_S = 0
    for i in range(3):
        for j in range(i+1, 3):
            Ac, Sc, d = cross_term_analysis(ks[i], vs[i], ks[j], vs[j])
            ci = np.cos(ks[i] @ x_max)
            cj = np.cos(ks[j] @ x_max)
            total_cross_A += Ac * ci * cj
            total_cross_S += Sc * ci * cj

    pred_gradu2 = 3 + 2*total_cross_A  # N + 2Σ cross
    pred_S2 = 1.5 + 2*total_cross_S  # N/2 + 2Σ S-cross

    if trial < 5:
        print(f"  |∇u|²={r['gradu2']:.4f} pred={pred_gradu2:.4f} | "
              f"|S|²={r['S2']:.4f} pred={pred_S2:.4f} | "
              f"|ω|²={r['om2']:.4f} S²ê/ω²={r['S2e_ratio']:.4f}")
