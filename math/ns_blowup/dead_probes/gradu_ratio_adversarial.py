"""
Adversarial search for worst |∇u|²/|ω|² at the global max of |ω|.

Two approaches:
1. VERTEX: evaluate all 2^N sign combos (exact for commensurate modes)
2. CONTINUOUS: Nelder-Mead multi-start over all x

Compare results. The vertex approach may find DIFFERENT (possibly worse)
configurations than the continuous search.

Target: is worst |∇u|²/|ω|² < 13/8 = 1.625?
"""
import numpy as np
from scipy.optimize import minimize
from itertools import product as iprod

def build_mode(k, theta):
    k = np.array(k, float)
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta)*e1 + np.sin(theta)*e2

def eval_at_point(ks, vs, amps, x):
    """Compute ω, ∇u, S at point x."""
    omega = np.zeros(3)
    gradu = np.zeros((3,3))
    for k, v, a in zip(ks, vs, amps):
        c = np.cos(k @ x)
        omega += a * v * c
        w = np.cross(k, v)
        gradu += a * np.outer(w, k) * c / (k@k)
    S = 0.5*(gradu + gradu.T)
    return omega, gradu, S

def vertex_max(ks, vs, amps):
    """Find max |ω|² over all 2^N sign combinations."""
    N = len(ks)
    best_om2 = 0
    best_data = None
    for signs in iprod([1.0, -1.0], repeat=N):
        signs = list(signs)
        omega = sum(a*s*v for a,s,v in zip(amps, signs, vs))
        om2 = omega @ omega
        if om2 > best_om2:
            gradu = sum(a*s*np.outer(np.cross(k,v), k)/(k@k)
                       for k,v,a,s in zip(ks,vs,amps,signs))
            S = 0.5*(gradu + gradu.T)
            best_om2 = om2
            best_data = (omega.copy(), gradu.copy(), S.copy())
    return best_om2, best_data

def continuous_max(ks, vs, amps, n_starts=20):
    """Find max |ω|² over continuous x via multi-start Nelder-Mead."""
    best_om2 = 0
    best_x = None
    for _ in range(n_starts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def f(xyz):
            om = sum(a*v*np.cos(k@xyz) for k,v,a in zip(ks,vs,amps))
            return -(om@om)
        res = minimize(f, x0, method='Nelder-Mead',
                      options={'xatol':1e-11,'fatol':1e-13,'maxiter':10000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()
    if best_x is None:
        return 0, None
    omega, gradu, S = eval_at_point(ks, vs, amps, best_x)
    return omega@omega, (omega, gradu, S)

def compute_ratios(omega, gradu, S):
    om2 = omega @ omega
    if om2 < 1e-10:
        return None
    e = omega / np.sqrt(om2)
    Se = S @ e
    S2e = Se @ Se
    gradu2 = np.sum(gradu**2)
    S2 = np.sum(S**2)
    return {
        'gradu_ratio': gradu2 / om2,
        'S2e_ratio': S2e / om2,
        'S_ratio': S2 / om2,
        'excess': (gradu2 - om2) / om2,
    }

def optimize_gradu_ratio(ks_fixed, n_restarts=40, method='vertex'):
    """Maximize |∇u|²/|ω|² for fixed k-vectors, varying polarizations + amps."""
    N = len(ks_fixed)
    ks = [np.array(k, float) for k in ks_fixed]

    best_ratio = 0
    for _ in range(n_restarts):
        thetas = np.random.uniform(0, 2*np.pi, N)
        raw_amps = np.random.randn(N) * 0.3
        vs = [build_mode(k, t) for k, t in zip(ks, thetas)]
        amps = np.exp(raw_amps)

        if method == 'vertex':
            om2, data = vertex_max(ks, vs, amps)
        else:
            om2, data = continuous_max(ks, vs, amps, n_starts=12)

        if data is None or om2 < 0.01:
            continue
        r = compute_ratios(*data)
        if r and r['gradu_ratio'] > best_ratio:
            best_ratio = r['gradu_ratio']

    return best_ratio

np.random.seed(42)

# Build k-pool
k_pool = []
for i in range(-2, 3):
    for j in range(-2, 3):
        for l in range(-2, 3):
            m2 = i*i+j*j+l*l
            if 0 < m2 <= 8:
                k_pool.append([i,j,l])

print("ADVERSARIAL |∇u|²/|ω|² SEARCH")
print("Threshold: 13/8 = 1.625")
print("=" * 70)

for N in [2, 3, 4, 5]:
    n_k_trials = 300 if N <= 3 else 150
    worst_vertex = 0
    worst_continuous = 0

    for trial in range(n_k_trials):
        idx = np.random.choice(len(k_pool), N, replace=False)
        ks = [k_pool[i] for i in idx]

        # Vertex search
        rv = optimize_gradu_ratio(ks, n_restarts=30, method='vertex')
        worst_vertex = max(worst_vertex, rv)

        # Continuous search
        rc = optimize_gradu_ratio(ks, n_restarts=30, method='continuous')
        worst_continuous = max(worst_continuous, rc)

        if trial % 100 == 0 and trial > 0:
            print(f"  N={N} [{trial}] vtx={worst_vertex:.4f} cont={worst_continuous:.4f}")

    print(f"N={N}: vertex={worst_vertex:.6f} continuous={worst_continuous:.6f} "
          f"threshold=1.625 margin_v={1.625-worst_vertex:.3f} margin_c={1.625-worst_continuous:.3f}")

# DEEP SEARCH for N=3 (the apparent worst case)
print("\n" + "=" * 70)
print("DEEP SEARCH N=3: 1000 k-triples × 50 restarts")
print("=" * 70)

worst_v = 0
worst_c = 0
worst_config = None

for trial in range(1000):
    idx = np.random.choice(len(k_pool), 3, replace=False)
    ks = [k_pool[i] for i in idx]

    rv = optimize_gradu_ratio(ks, n_restarts=50, method='vertex')
    rc = optimize_gradu_ratio(ks, n_restarts=50, method='continuous')

    if rv > worst_v:
        worst_v = rv
        worst_config = ('vertex', ks)
    if rc > worst_c:
        worst_c = rc

    if trial % 200 == 0 and trial > 0:
        print(f"  [{trial}] vtx={worst_v:.6f} cont={worst_c:.6f}")

print(f"\nN=3 DEEP: vertex={worst_v:.6f} continuous={worst_c:.6f}")
print(f"vs 13/8 = 1.625: margin_v={1.625-worst_v:.4f} margin_c={1.625-worst_c:.4f}")
if worst_config:
    print(f"Worst config k's: {worst_config[1]}")
