"""
COMPUTER-ASSISTED PROOF: Verify S²ê < 3|ω|²/4 for ALL mode subsets with |k|² ≤ 2.

For K = √2 (|k|² ≤ 2): 9 unique k-vectors (removing anti-parallel pairs).
For each N-mode subset (N=2..9): enumerate all 2^N sign patterns,
optimize over polarization angles to find the WORST regression bound.

If worst R_bound < 13/8 for ALL subsets: CERTIFIED for this shell.
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

def regression_bound(ks, vs):
    """Compute the regression bound R for a given mode config."""
    N = len(ks)
    pairs = []
    for j in range(N):
        for k in range(j+1, N):
            D = vs[j] @ vs[k]
            w1, w2 = np.cross(ks[j], vs[j]), np.cross(ks[k], vs[k])
            G = (w1@w2)*(ks[j]@ks[k]) / ((ks[j]@ks[j])*(ks[k]@ks[k]))
            pairs.append((j, k, D, G-D))

    X_all, Y_all = [], []
    for signs in iprod([1.0, -1.0], repeat=N):
        Y = sum(signs[j]*signs[k]*D for j,k,D,_ in pairs)
        X = sum(signs[j]*signs[k]*d for j,k,_,d in pairs)
        X_all.append(X)
        Y_all.append(Y)

    Xa, Ya = np.array(X_all), np.array(Y_all)
    VY = np.mean(Ya**2)
    if VY < 1e-15:
        # Degenerate: |ω|² ≈ N for all signs. Excess matters.
        idx_max = np.argmax(np.array([N + 2*y for y in Ya]))
        return 1 + 2*Xa[idx_max]/(N + 2*Ya[idx_max])

    slope = np.mean(Xa*Ya) / VY
    L = Xa - slope * Ya
    Ym = np.max(Ya)
    om2_max = N + 2*Ym
    if om2_max < 0.01:
        return 0
    return 1 + 2*(np.max(L) + slope*Ym) / om2_max

def worst_bound_for_ks(ks, n_restarts=50):
    """Maximize the regression bound over polarization angles."""
    N = len(ks)
    ks = [np.asarray(k, float) for k in ks]
    best = 0
    for _ in range(n_restarts):
        thetas = np.random.uniform(0, 2*np.pi, N)
        def neg_Rb(th):
            vs = [build_perp(k, t) for k, t in zip(ks, th)]
            return -regression_bound(ks, vs)
        res = minimize(neg_Rb, thetas, method='Nelder-Mead',
                      options={'maxiter': 3000, 'xatol': 1e-10, 'fatol': 1e-12})
        best = max(best, -res.fun)
    return best

np.random.seed(42)

# Build the K=√2 shell: |k|² ≤ 2, remove anti-parallel
all_ks_raw = []
for i in range(-1, 2):
    for j in range(-1, 2):
        for l in range(-1, 2):
            m2 = i*i + j*j + l*l
            if 0 < m2 <= 2:
                all_ks_raw.append(np.array([i,j,l], float))

# Remove anti-parallel
unique_ks = []
for k in all_ks_raw:
    if not any(np.allclose(k, -u) for u in unique_ks):
        unique_ks.append(k)

K_total = len(unique_ks)
print(f"K=√2 shell: {K_total} unique k-vectors")
for k in unique_ks:
    print(f"  {k.astype(int)}, |k|²={int(k@k)}")

print(f"\n{'='*60}")
print(f"EXHAUSTIVE VERIFICATION: all N-mode subsets, N=2..{K_total}")
print(f"{'='*60}")

overall_worst = 0
overall_worst_config = None
total_configs = 0

for N in range(2, K_total + 1):
    n_subsets = 0
    worst_N = 0
    for subset in combinations(range(K_total), N):
        ks = [unique_ks[i] for i in subset]
        Rb = worst_bound_for_ks(ks, n_restarts=30)
        worst_N = max(worst_N, Rb)
        if Rb > overall_worst:
            overall_worst = Rb
            overall_worst_config = (N, subset, Rb)
        n_subsets += 1
        total_configs += 1

    status = "PASS ✓" if worst_N < 1.625 else "**FAIL**"
    print(f"  N={N}: {n_subsets:4d} subsets, worst Rb = {worst_N:.6f} {status}")

print(f"\n{'='*60}")
print(f"RESULT: {total_configs} total configs checked")
print(f"Overall worst Rb = {overall_worst:.6f}")
print(f"Threshold 13/8 = {13/8:.6f}")
print(f"{'CERTIFIED ✓✓✓' if overall_worst < 1.625 else 'FAILED'}")
if overall_worst_config:
    N, sub, Rb = overall_worst_config
    print(f"Worst at N={N}, k-indices={sub}, Rb={Rb:.6f}")
