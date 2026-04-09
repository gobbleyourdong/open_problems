"""
Test whether the Gram matrix eigenvalue bound closes N ≥ 5.

Key idea: S²ê = Σ|ŝ_j||ŝ_k|(d̂_j·d̂_k) ≤ λ_max(G) × Σ|ŝ_k|²
where G_{jk} = d̂_j·d̂_k is the Gram matrix of ŝ_k direction vectors.

The constraint: d̂_k ⊥ v̂_k (from Biot-Savart structure).

If λ_max(G) ≤ N/3: then S²ê ≤ (N/3)Σ|ŝ_k|².
Combined with Σ|ŝ_k|² ≤ (N-1)|ω|²/(4N) (diagonal from file 363):
S²ê ≤ (N/3)(N-1)|ω|²/(4N) = (N-1)|ω|²/12 < 3|ω|²/4 for all N.

Test: what is λ_max(G) for actual worst-case configurations?
"""
import numpy as np
from scipy.optimize import minimize

def compute_gram_at_max(ks, vs, amps=None):
    """Compute the Gram matrix of ŝ_k directions at the global max of |ω|."""
    N = len(ks)
    if amps is None:
        amps = np.ones(N)

    # Find global max
    best_om2 = 0
    best_x = None
    for _ in range(15):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def f(xyz):
            om = sum(a*v*np.cos(k@xyz) for k,v,a in zip(ks,vs,amps))
            return -(om@om)
        res = minimize(f, x0, method='Nelder-Mead',
                      options={'xatol':1e-10,'fatol':1e-12,'maxiter':5000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x
    if best_om2 < 0.01 or best_x is None:
        return None

    # Compute ω and ê
    omega = sum(a*v*np.cos(k@best_x) for k,v,a in zip(ks,vs,amps))
    om = np.sqrt(omega@omega)
    e_hat = omega / om

    # Compute ŝ_k = S_k · ê for each mode
    s_vecs = []
    s_mags = []
    for k, v, a in zip(ks, vs, amps):
        c = np.cos(k @ best_x)
        w = np.cross(k, v)
        gu = a * np.outer(w, k) * c / (k@k)
        Sk = 0.5 * (gu + gu.T)
        sk = Sk @ e_hat
        mag = np.linalg.norm(sk)
        s_vecs.append(sk)
        s_mags.append(mag)

    # Build Gram matrix of directions
    G = np.zeros((N, N))
    d_hats = []
    for i in range(N):
        if s_mags[i] > 1e-10:
            d_hats.append(s_vecs[i] / s_mags[i])
        else:
            d_hats.append(np.zeros(3))

    for i in range(N):
        for j in range(N):
            G[i,j] = d_hats[i] @ d_hats[j]

    evals = np.linalg.eigvalsh(G)
    lambda_max = evals[-1]

    # Also compute actual S²ê and the bounds
    S_total = sum(s_vecs)
    S2e_actual = S_total @ S_total
    diag_sum = sum(m**2 for m in s_mags)
    b = np.array(s_mags)
    S2e_gram = b @ G @ b  # should equal S2e_actual

    return {
        'lambda_max': lambda_max,
        'lambda_min': evals[0],
        'lambda_ratio': lambda_max / N if N > 0 else 0,
        'S2e_actual': S2e_actual,
        'S2e_diag': diag_sum,
        'S2e_gram_check': S2e_gram,
        'om2': om**2,
        'S2e_ratio': S2e_actual / om**2,
        'evals': evals,
    }

def rand_perp(k):
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    r = np.random.randn(3)
    r -= (r@kn)*kn
    return r / np.linalg.norm(r)

np.random.seed(42)

all_ks = []
for i in range(-2,3):
    for j in range(-2,3):
        for l in range(-2,3):
            if 0 < i*i+j*j+l*l <= 12:
                all_ks.append(np.array([i,j,l],float))

print("GRAM MATRIX EIGENVALUE ANALYSIS")
print("=" * 70)
print(f"{'N':>3} | {'λ_max':>8} | {'λ_max/N':>8} | {'λ_min':>8} | {'S²ê/ω²':>10} | {'diag/ω²':>10} | {'ratio':>8}")
print("-" * 70)

for N in [2, 3, 4, 5, 8, 12, 20]:
    worst_lmax = 0
    worst_lratio = 0
    worst_S2e = 0
    n_trials = 500 if N <= 8 else 200

    for trial in range(n_trials):
        idx = np.random.choice(len(all_ks), min(N, len(all_ks)), replace=False)
        ks = [all_ks[i] for i in idx]
        vs = [rand_perp(k) for k in ks]

        r = compute_gram_at_max(ks, vs)
        if r is None:
            continue

        worst_lmax = max(worst_lmax, r['lambda_max'])
        worst_lratio = max(worst_lratio, r['lambda_ratio'])
        worst_S2e = max(worst_S2e, r['S2e_ratio'])

    print(f"{N:3d} | {worst_lmax:8.4f} | {worst_lratio:8.4f} | {'':8s} | {worst_S2e:10.6f} | {'':10s} | {'':8s}")

# Detailed analysis for a specific worst case
print("\nDETAILED: N=5, worst-case search")
print("=" * 70)

worst_S2e = 0
worst_result = None
for trial in range(1000):
    idx = np.random.choice(len(all_ks), 5, replace=False)
    ks = [all_ks[i] for i in idx]
    vs = [rand_perp(k) for k in ks]
    r = compute_gram_at_max(ks, vs)
    if r and r['S2e_ratio'] > worst_S2e:
        worst_S2e = r['S2e_ratio']
        worst_result = r

if worst_result:
    r = worst_result
    print(f"Worst S²ê/|ω|² = {r['S2e_ratio']:.6f}")
    print(f"Gram eigenvalues: {r['evals'].round(4)}")
    print(f"λ_max = {r['lambda_max']:.4f}, λ_max/N = {r['lambda_max']/5:.4f}")
    print(f"S²ê_actual = {r['S2e_actual']:.4f}, diagonal = {r['S2e_diag']:.4f}")
    print(f"Cross-term fraction: {(r['S2e_actual']-r['S2e_diag'])/r['S2e_actual']:.2%}")

# Test the BOUND: S²ê ≤ λ_max × Σ|ŝ_k|²
print("\nBOUND CHECK: S²ê ≤ λ_max × Σ|ŝ_k|² → S²ê/|ω|² ≤ λ_max × diag/|ω|²")
print("=" * 70)
for N in [3, 5, 8, 12]:
    worst_bound_ratio = 0
    for trial in range(300):
        idx = np.random.choice(len(all_ks), min(N, len(all_ks)), replace=False)
        ks = [all_ks[i] for i in idx]
        vs = [rand_perp(k) for k in ks]
        r = compute_gram_at_max(ks, vs)
        if r is None: continue
        bound = r['lambda_max'] * r['S2e_diag'] / r['om2']
        worst_bound_ratio = max(worst_bound_ratio, bound)
    print(f"  N={N:2d}: worst λ_max×diag/|ω|² = {worst_bound_ratio:.6f} (threshold 0.75)")
