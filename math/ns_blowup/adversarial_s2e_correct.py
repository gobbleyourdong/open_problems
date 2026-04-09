"""
CORRECTED adversarial S²ê search.
Only compute S²ê at the GLOBAL max of |ω|² (exact vertex enumeration).
"""
import numpy as np
from scipy.optimize import differential_evolution
from itertools import combinations, product as iprod

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def compute_ratio_at_global_max(ks, thetas):
    """Compute S²ê/|ω|² at the GLOBAL max of |ω|² over all sign patterns."""
    N = len(ks)
    bases = [build_perp_basis(k) for k in ks]
    vs = [np.cos(thetas[i])*bases[i][0] + np.sin(thetas[i])*bases[i][1] for i in range(N)]

    # Find the sign pattern that gives the GLOBAL max of |ω|²
    best_om2 = 0
    best_signs = None

    for signs in iprod([1.0, -1.0], repeat=N):
        omega = sum(s*v for s, v in zip(signs, vs))
        om2 = omega @ omega
        if om2 > best_om2:
            best_om2 = om2
            best_signs = signs

    if best_om2 < 1e-15:
        return 0.0

    # Compute S²ê at the global max
    omega = sum(s*v for s, v in zip(best_signs, vs))
    om2 = omega @ omega
    e_hat = omega / np.sqrt(om2)

    S = np.zeros((3, 3))
    for k, v, s in zip(ks, vs, best_signs):
        w = np.cross(k, s*v)
        k2 = k @ k
        S -= (np.outer(w, k) + np.outer(k, w)) / (2 * k2)

    Se = S @ e_hat
    s2e = Se @ Se

    return s2e / om2

def adversarial_search(ks, n_iter=200, popsize=15):
    """Use DE to MAXIMIZE S²ê/|ω|² over polarization angles, at the global max."""
    N = len(ks)
    bounds = [(0, 2*np.pi)] * N

    def neg_ratio(thetas):
        return -compute_ratio_at_global_max(ks, thetas)

    result = differential_evolution(neg_ratio, bounds, maxiter=n_iter,
                                    popsize=popsize, seed=42, tol=1e-10)
    return -result.fun

if __name__ == '__main__':
    np.random.seed(42)

    # Build K=√2 shell
    raw = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            for l in range(-1, 2):
                k2 = i*i + j*j + l*l
                if 0 < k2 <= 2:
                    raw.append(np.array([i, j, l], float))
    unique = []
    for k in raw:
        if not any(np.allclose(k, -u) for u in unique):
            unique.append(k)

    print(f"K=√2 shell: {len(unique)} unique k-vectors")
    print()

    # Also include K=1 modes
    k1_modes = [np.array([1,0,0.]), np.array([0,1,0.]), np.array([0,0,1.])]

    overall_worst = 0

    for N in [2, 3, 4]:
        subs = list(combinations(range(len(unique)), N))
        print(f"N={N}: {len(subs)} K=√2 subsets")

        worst = 0
        worst_config = None
        for idx, sub in enumerate(subs):
            ks = [unique[i] for i in sub]
            ratio = adversarial_search(ks, n_iter=150, popsize=12)
            if ratio > worst:
                worst = ratio
                worst_config = [unique[i].astype(int).tolist() for i in sub]
            if (idx+1) % 30 == 0:
                print(f"  {idx+1}/{len(subs)}: worst so far = {worst:.6f}")

        print(f"  WORST S²ê/|ω|²: {worst:.6f} (< 0.75? {worst < 0.75})")
        print(f"  Config: {worst_config}")
        overall_worst = max(overall_worst, worst)
        print()

    # N=5,6 (sample)
    for N in [5, 6]:
        subs = list(combinations(range(len(unique)), N))
        np.random.shuffle(subs)
        subs = subs[:40]
        print(f"N={N}: {len(subs)} sampled K=√2 subsets")

        worst = 0
        for sub in subs:
            ks = [unique[i] for i in sub]
            ratio = adversarial_search(ks, n_iter=100, popsize=10)
            worst = max(worst, ratio)

        print(f"  WORST S²ê/|ω|²: {worst:.6f}")
        overall_worst = max(overall_worst, worst)
        print()

    # K=1 modes
    print("K=1 shell:")
    for N in [2, 3]:
        for sub in combinations(range(3), N):
            ks = [k1_modes[i] for i in sub]
            ratio = adversarial_search(ks, n_iter=200, popsize=15)
            print(f"  N={N}, k={[k.astype(int).tolist() for k in ks]}: S²ê/|ω|² = {ratio:.6f}")
            overall_worst = max(overall_worst, ratio)

    # Mixed K shells
    print("\nMixed K modes:")
    for trial in range(20):
        all_k = k1_modes + unique
        N = np.random.randint(3, 8)
        idx = np.random.choice(len(all_k), min(N, len(all_k)), replace=False)
        ks = [all_k[i] for i in idx]
        ratio = adversarial_search(ks, n_iter=100, popsize=10)
        overall_worst = max(overall_worst, ratio)

    print(f"  Worst from mixed: {overall_worst:.6f}")

    print()
    print(f"=" * 50)
    print(f"OVERALL WORST S²ê/|ω|² at global max: {overall_worst:.6f}")
    print(f"Key Lemma: {overall_worst < 0.75} (need < 0.750)")
    print(f"Margin: {(0.75 - overall_worst)/0.75 * 100:.1f}%")
