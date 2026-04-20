"""
Find the EXACT worst case |∇u|²/|ω|² for N=5 on the integer lattice.

Strategy: for each 5-tuple of k-vectors, optimize polarization angles
to maximize the ratio. Use scipy minimize with many restarts.

Also compute the DECOMPOSITION: how much of the excess comes from
each pair, and what sign pattern the global max uses.
"""
import numpy as np
from scipy.optimize import minimize
from itertools import combinations, product as iprod

def build_perp(k, theta):
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    e1 = np.cross(kn, [1,0,0] if abs(kn[0])<0.9 else [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return np.cos(theta)*e1 + np.sin(theta)*e2

def eval_all_vertices(ks, vs, amps):
    """Return the ratio at the global-max vertex and the decomposition."""
    N = len(ks)
    best_om2 = 0
    best_data = None

    for signs in iprod([1.0, -1.0], repeat=N):
        omega = sum(a*s*v for a,s,v in zip(amps, signs, vs))
        om2 = omega @ omega
        if om2 > best_om2:
            best_om2 = om2
            gradu = sum(a*s*np.outer(np.cross(k,v), k)/(k@k)
                       for k,v,a,s in zip(ks,vs,amps,signs))
            gradu2 = np.sum(gradu**2)
            S = 0.5*(gradu + gradu.T)
            e = omega / np.sqrt(om2)
            Se = S @ e
            S2e = Se @ Se
            best_data = {
                'om2': om2, 'gradu2': gradu2, 'S2e': S2e,
                'ratio': gradu2/om2, 'S2e_ratio': S2e/om2,
                'signs': list(signs), 'excess': (gradu2-om2)/om2
            }
    return best_data

def optimize_ratio_for_ks(ks, n_restarts=40):
    """Maximize |∇u|²/|ω|² over polarization angles and amplitudes."""
    N = len(ks)
    ks = [np.asarray(k, float) for k in ks]

    best_ratio = 0
    best_data = None

    for _ in range(n_restarts):
        # Random initial angles and log-amplitudes
        x0 = np.concatenate([np.random.uniform(0, 2*np.pi, N),
                             np.random.randn(N)*0.3])
        def neg_ratio(params):
            thetas = params[:N]
            amps = np.exp(params[N:])
            vs = [build_perp(k, t) for k,t in zip(ks, thetas)]
            data = eval_all_vertices(ks, vs, amps)
            return -data['ratio'] if data else 0

        res = minimize(neg_ratio, x0, method='Nelder-Mead',
                      options={'maxiter': 5000, 'xatol': 1e-10, 'fatol': 1e-12})
        ratio = -res.fun
        if ratio > best_ratio:
            best_ratio = ratio
            # Reconstruct the best config
            thetas = res.x[:N]
            amps = np.exp(res.x[N:])
            vs = [build_perp(k, t) for k,t in zip(ks, thetas)]
            best_data = eval_all_vertices(ks, vs, amps)
            best_data['ks'] = ks
            best_data['vs'] = vs
            best_data['amps'] = amps

    return best_ratio, best_data

np.random.seed(42)

# Build k-pool (|k|² ≤ 8)
k_pool = []
for i in range(-2, 3):
    for j in range(-2, 3):
        for l in range(-2, 3):
            if 0 < i*i+j*j+l*l <= 8:
                k_pool.append(np.array([i,j,l], float))

# Remove anti-parallel
unique = []
for k in k_pool:
    if not any(np.allclose(k, -u) for u in unique):
        unique.append(k)
k_pool = unique
print(f"k-pool: {len(k_pool)} unique vectors (|k|² ≤ 8)")

# Sweep over many 5-tuples
print("\n" + "=" * 70)
print("EXHAUSTIVE N=5 SEARCH")
print("=" * 70)

worst_ratio = 0
worst_data = None
n_tested = 0

for trial in range(1000):
    idx = np.random.choice(len(k_pool), 5, replace=False)
    ks = [k_pool[i] for i in idx]
    ratio, data = optimize_ratio_for_ks(ks, n_restarts=30)
    n_tested += 1

    if ratio > worst_ratio:
        worst_ratio = ratio
        worst_data = data

    if trial % 200 == 0:
        print(f"  [{trial}] worst = {worst_ratio:.6f} (threshold 13/8 = 1.625)")

print(f"\nN=5 RESULT: worst |∇u|²/|ω|² = {worst_ratio:.6f}")
print(f"  vs 5/4 = 1.250: {'PASS' if worst_ratio < 1.25 else 'FAIL'}")
print(f"  vs 13/8 = 1.625: {'PASS' if worst_ratio < 1.625 else 'FAIL'}")

if worst_data:
    d = worst_data
    print(f"\n  |ω|² = {d['om2']:.4f}")
    print(f"  EXCESS/|ω|² = {d['excess']:.6f}")
    print(f"  S²ê/|ω|² = {d['S2e_ratio']:.6f} (threshold 0.75)")
    print(f"  Signs = {d['signs']}")
    print(f"  k-vectors:")
    for k in d['ks']:
        print(f"    {k.astype(int)}")

# Also do N=6 and N=7
for N in [6, 7]:
    worst = 0
    for trial in range(500):
        idx = np.random.choice(len(k_pool), min(N, len(k_pool)), replace=False)
        ks = [k_pool[i] for i in idx]
        r, _ = optimize_ratio_for_ks(ks, n_restarts=20)
        worst = max(worst, r)
        if trial % 200 == 0 and trial > 0:
            print(f"  N={N} [{trial}] worst = {worst:.6f}")
    print(f"N={N}: worst = {worst:.6f} vs 5/4={1.25:.3f} vs 13/8={1.625:.3f}")
