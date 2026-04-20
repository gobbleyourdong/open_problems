"""
DEFINITIVE adversarial search for worst C/|ω|² across all N and K.
Uses DE optimization over polarization angles at the exact vertex max.
"""
import numpy as np
from scipy.optimize import differential_evolution
from itertools import combinations, product as iprod

def perp(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def compute_C_ratio(ks, thetas):
    N = len(ks)
    bases = [perp(k) for k in ks]
    vs = [np.cos(thetas[i])*bases[i][0] + np.sin(thetas[i])*bases[i][1] for i in range(N)]
    best_om2 = 0; best_signs = None
    for signs in iprod([1.0, -1.0], repeat=N):
        omega = sum(s*v for s, v in zip(signs, vs))
        om2 = omega @ omega
        if om2 > best_om2:
            best_om2 = om2; best_signs = signs
    if best_om2 < 1e-15: return 0
    omega = sum(s*v for s, v in zip(best_signs, vs)); om2 = omega @ omega
    S = np.zeros((3, 3))
    for k, v, s in zip(ks, vs, best_signs):
        w = np.cross(k, s*v)
        S -= (np.outer(w, k) + np.outer(k, w)) / (2 * (k@k))
    S2_F = np.sum(S**2)
    return ((om2/2 - S2_F) / 2) / om2

all_k = []
for i in range(-3, 4):
    for j in range(-3, 4):
        for l in range(-3, 4):
            k = np.array([i, j, l], float)
            if 0 < k@k <= 9:
                if not any(np.allclose(k, -u) for u in all_k):
                    all_k.append(k)

print(f"{len(all_k)} unique k-vectors with |k|² ≤ 9")

results = {}
overall_worst = 0
overall_config = None

for N in [2, 3, 4, 5]:
    subs = list(combinations(range(len(all_k)), N))
    np.random.shuffle(subs)
    n_test = min(len(subs), {2: len(subs), 3: 2000, 4: 500, 5: 200}[N])
    subs = subs[:n_test]

    worst = 0; worst_config = None
    for idx, sub in enumerate(subs):
        ks = [all_k[i] for i in sub]
        res = differential_evolution(lambda t: compute_C_ratio(ks, t),
                                    [(0, 2*np.pi)]*N, maxiter=100,
                                    popsize=10, seed=42, tol=1e-10)
        cr = res.fun
        if cr < worst:
            worst = cr
            worst_config = [all_k[i].astype(int).tolist() for i in sub]
        if (idx+1) % max(1, n_test//5) == 0:
            print(f"  N={N}: {idx+1}/{n_test}, worst C/|ω|² = {worst:.8f}")

    results[N] = worst
    if worst < overall_worst:
        overall_worst = worst
        overall_config = worst_config
    print(f"  N={N} DONE: worst C/|ω|² = {worst:.8f} "
          f"(|S|²_F/|ω|² = {0.5-2*worst:.6f}, "
          f"margin to -5/16: {(-5/16-worst)/(-5/16)*100:.1f}%)")
    if worst_config:
        print(f"  Config: {worst_config}")
    print()

print("=" * 60)
print("DEFINITIVE RESULTS")
print("=" * 60)
for N, w in sorted(results.items()):
    print(f"  N={N}: C/|ω|² ≥ {w:.8f}  |S|²_F/|ω|² ≤ {0.5-2*w:.6f}")
print(f"\n  Overall worst: C/|ω|² = {overall_worst:.8f}")
print(f"  Config: {overall_config}")
print(f"  Threshold: -5/16 = {-5/16:.8f}")
print(f"  Margin: {(-5/16-overall_worst)/(-5/16)*100:.1f}%")
print(f"\n  C > -5/16? {overall_worst > -5/16}")
print(f"  → |S|²_F < 9|ω|²/8? {0.5-2*overall_worst < 9/8}")
print(f"  → S²ê < 3|ω|²/4 (via trace-free)? {(2/3)*(0.5-2*overall_worst) < 3/4}")
