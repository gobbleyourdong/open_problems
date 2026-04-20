"""
CRITICAL CHECK: Does the vertex-based max agree with the continuous max?

For non-orthogonal k's, the global max of |ω| may NOT be at a lattice vertex.
If the vertex evaluator finds a secondary max, the ratio there could be HIGHER
than at the true global max — giving a spurious violation.
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

def vertex_analysis(ks, vs, amps):
    """All vertices sorted by |ω|²."""
    N = len(ks)
    results = []
    for signs in iprod([1.0, -1.0], repeat=N):
        signs = list(signs)
        omega = sum(a*s*v for a,s,v in zip(amps, signs, vs))
        om2 = omega @ omega
        if om2 < 1e-10:
            continue
        gradu = sum(a*s*np.outer(np.cross(k,v), k)/(k@k)
                   for k,v,a,s in zip(ks,vs,amps,signs))
        gradu2 = np.sum(gradu**2)
        results.append({'om2': om2, 'gradu2': gradu2, 'ratio': gradu2/om2,
                        'signs': list(signs)})
    results.sort(key=lambda r: r['om2'], reverse=True)
    return results

def continuous_analysis(ks, vs, amps, n_starts=30):
    """Find true global max via multi-start optimization."""
    best_om2 = 0
    best_x = None
    for _ in range(n_starts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def f(xyz):
            om = sum(a*v*np.cos(k@xyz) for k,v,a in zip(ks,vs,amps))
            return -(om@om)
        res = minimize(f, x0, method='Nelder-Mead',
                      options={'xatol':1e-12,'fatol':1e-14,'maxiter':10000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()
    if best_x is None:
        return None

    omega = np.zeros(3)
    gradu = np.zeros((3,3))
    for k,v,a in zip(ks,vs,amps):
        c = np.cos(k@best_x)
        omega += a*v*c
        gradu += a*np.outer(np.cross(k,v), k)*c/(k@k)
    om2 = omega@omega
    gradu2 = np.sum(gradu**2)
    return {'om2': om2, 'gradu2': gradu2, 'ratio': gradu2/om2, 'x': best_x}

np.random.seed(42)

print("VERTEX vs CONTINUOUS MAX — discrepancy check")
print("=" * 70)

k_pool = []
for i in range(-2, 3):
    for j in range(-2, 3):
        for l in range(-2, 3):
            if 0 < i*i+j*j+l*l <= 8:
                k_pool.append(np.array([i,j,l], float))

n_discrepant = 0
max_discrepancy = 0
worst_vertex_ratio = 0
worst_cont_ratio = 0

for trial in range(500):
    idx = np.random.choice(len(k_pool), 3, replace=False)
    ks = [k_pool[i] for i in idx]
    vs = [build_mode(k, np.random.uniform(0, 2*np.pi)) for k in ks]
    amps = np.exp(np.random.uniform(-0.3, 0.3, 3))

    verts = vertex_analysis(ks, vs, amps)
    cont = continuous_analysis(ks, vs, amps, n_starts=25)

    if not verts or cont is None:
        continue

    vtx_best = verts[0]  # highest |ω|² vertex
    cont_om2 = cont['om2']
    vtx_om2 = vtx_best['om2']

    # Check if continuous max exceeds vertex max
    if cont_om2 > vtx_om2 * 1.001:
        n_discrepant += 1
        discrepancy = cont_om2 / vtx_om2
        max_discrepancy = max(max_discrepancy, discrepancy)

        # Compare ratios at vertex-max vs true-max
        vtx_ratio = vtx_best['ratio']
        cont_ratio = cont['ratio']

        if trial < 10 or vtx_ratio > 1.3:
            print(f"  Trial {trial}: vtx |ω|²={vtx_om2:.4f} ratio={vtx_ratio:.4f} | "
                  f"cont |ω|²={cont_om2:.4f} ratio={cont_ratio:.4f} | "
                  f"Δ|ω|²={discrepancy:.4f}x")

    worst_vertex_ratio = max(worst_vertex_ratio, vtx_best['ratio'])
    worst_cont_ratio = max(worst_cont_ratio, cont['ratio'])

    # Also check: is |∇u|²/|ω|² at the SECONDARY vertex higher?
    if len(verts) > 1:
        second = verts[1]
        if second['ratio'] > vtx_best['ratio']:
            # Secondary vertex has HIGHER ratio than primary
            pass

print(f"\nDiscrepant (cont > vtx): {n_discrepant}/500")
print(f"Max discrepancy: {max_discrepancy:.4f}x")
print(f"Worst |∇u|²/|ω|² at VERTEX max: {worst_vertex_ratio:.6f}")
print(f"Worst |∇u|²/|ω|² at CONTINUOUS max: {worst_cont_ratio:.6f}")
print(f"\nThreshold: 13/8 = 1.625")
print(f"5/4 = 1.250")

# Specifically test configs where vertex gives ratio > 5/4
print("\n" + "=" * 70)
print("CONFIGS WHERE VERTEX RATIO > 5/4:")
for trial in range(2000):
    idx = np.random.choice(len(k_pool), 3, replace=False)
    ks = [k_pool[i] for i in idx]
    vs = [build_mode(k, np.random.uniform(0, 2*np.pi)) for k in ks]
    amps = np.exp(np.random.uniform(-0.3, 0.3, 3))

    verts = vertex_analysis(ks, vs, amps)
    if not verts:
        continue

    if verts[0]['ratio'] > 1.25:
        # This vertex claims ratio > 5/4. Check continuous max.
        cont = continuous_analysis(ks, vs, amps, n_starts=30)
        if cont:
            print(f"  vtx: |ω|²={verts[0]['om2']:.4f} ratio={verts[0]['ratio']:.4f} | "
                  f"cont: |ω|²={cont['om2']:.4f} ratio={cont['ratio']:.4f} | "
                  f"{'REAL' if cont['ratio'] > 1.25 else 'SPURIOUS'}")
