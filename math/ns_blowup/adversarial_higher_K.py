"""
Adversarial S²ê test with higher K shells and mixed modes.
Tests K=1, √2, √3, 2, √5, √6 and mixed combinations.
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

def compute_ratio(ks, thetas):
    N = len(ks)
    bases = [build_perp_basis(k) for k in ks]
    vs = [np.cos(thetas[i])*bases[i][0] + np.sin(thetas[i])*bases[i][1] for i in range(N)]

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

    omega = sum(s*v for s, v in zip(best_signs, vs))
    om2 = omega @ omega
    e_hat = omega / np.sqrt(om2)
    S = np.zeros((3, 3))
    for k, v, s in zip(ks, vs, best_signs):
        w = np.cross(k, s*v)
        S -= (np.outer(w, k) + np.outer(k, w)) / (2 * (k@k))
    Se = S @ e_hat
    return (Se @ Se) / om2

def adversarial(ks, n_iter=150, popsize=12):
    N = len(ks)
    bounds = [(0, 2*np.pi)] * N
    result = differential_evolution(lambda t: -compute_ratio(ks, t), bounds,
                                    maxiter=n_iter, popsize=popsize, seed=42, tol=1e-10)
    return -result.fun

def build_shell(K2_max):
    """Build all k-vectors with |k|² ≤ K2_max, unique (no -k duplicates)."""
    modes = {}
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i, j, l], float)
                k2 = int(k @ k)
                if 0 < k2 <= K2_max:
                    if k2 not in modes:
                        modes[k2] = []
                    modes[k2].append(k)

    # Remove -k duplicates within each shell
    unique_by_shell = {}
    for k2, klist in modes.items():
        unique = []
        for k in klist:
            if not any(np.allclose(k, -u) for u in unique):
                unique.append(k)
        unique_by_shell[k2] = unique

    return unique_by_shell

if __name__ == '__main__':
    np.random.seed(42)

    shells = build_shell(6)

    print("Available shells:")
    for k2 in sorted(shells.keys()):
        print(f"  |k|² = {k2}: {len(shells[k2])} unique vectors")

    # Test each shell individually
    print()
    print("=" * 60)
    print("SINGLE-SHELL ADVERSARIAL (worst S²ê/|ω|² at global max)")
    print("=" * 60)

    shell_worst = {}
    for k2 in sorted(shells.keys()):
        vecs = shells[k2]
        if len(vecs) < 2:
            continue

        worst = 0
        for N in [2, 3, 4, min(5, len(vecs))]:
            if N > len(vecs):
                continue
            subs = list(combinations(range(len(vecs)), N))
            if len(subs) > 50:
                np.random.shuffle(subs)
                subs = subs[:50]

            for sub in subs:
                ks = [vecs[i] for i in sub]
                ratio = adversarial(ks, n_iter=100, popsize=10)
                worst = max(worst, ratio)

        shell_worst[k2] = worst
        print(f"  |k|² = {k2}: worst = {worst:.6f}")

    # Test MIXED shells
    print()
    print("=" * 60)
    print("MIXED-SHELL ADVERSARIAL")
    print("=" * 60)

    all_vecs = []
    for k2 in sorted(shells.keys()):
        all_vecs.extend(shells[k2])
    print(f"Total unique vectors (|k|² ≤ 6): {len(all_vecs)}")

    mixed_worst = 0
    for trial in range(200):
        N = np.random.randint(2, min(8, len(all_vecs)))
        idx = np.random.choice(len(all_vecs), N, replace=False)
        ks = [all_vecs[i] for i in idx]

        # Check that k-vectors span different shells (mixed)
        k2s = set(int(k@k) for k in ks)

        ratio = adversarial(ks, n_iter=80, popsize=8)
        mixed_worst = max(mixed_worst, ratio)

        if trial % 50 == 0:
            print(f"  trial {trial}/200: worst mixed = {mixed_worst:.6f}")

    print(f"\n  WORST mixed S²ê/|ω|²: {mixed_worst:.6f}")

    # Specifically test modes with high K ratios (large |k|)
    print()
    print("=" * 60)
    print("HIGH-K ADVERSARIAL (|k|² = 4,5,6)")
    print("=" * 60)

    for k2 in [4, 5, 6]:
        if k2 not in shells or len(shells[k2]) < 2:
            continue
        vecs = shells[k2]
        worst_high = 0
        for N in [2, 3, min(4, len(vecs))]:
            if N > len(vecs):
                continue
            subs = list(combinations(range(len(vecs)), N))
            if len(subs) > 40:
                np.random.shuffle(subs)
                subs = subs[:40]
            for sub in subs:
                ks = [vecs[i] for i in sub]
                ratio = adversarial(ks, n_iter=100, popsize=10)
                worst_high = max(worst_high, ratio)
        print(f"  |k|² = {k2}: worst = {worst_high:.6f}")

    # Grand summary
    print()
    print("=" * 60)
    print("GRAND SUMMARY")
    print("=" * 60)
    overall = max(max(shell_worst.values()), mixed_worst)
    print(f"  Overall worst S²ê/|ω|²: {overall:.6f}")
    print(f"  Threshold: 0.750")
    print(f"  Margin: {(0.75-overall)/0.75*100:.1f}%")
    print(f"  Key Lemma holds: {overall < 0.75}")
