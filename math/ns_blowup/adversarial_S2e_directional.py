"""
numerical track Cycle 1b — Adversarial S²ê/|ω|² Maximization

For each N-tuple of wavevectors, use differential evolution to find
the polarization angles that MAXIMIZE S²ê/|ω|² at the vorticity maximum.

This is the KEY computation: if the adversarial worst-case S²ê/|ω|²
stays well below 0.75, the Key Lemma has enormous margin and the
directional proof path is viable.

Method:
1. For each k-tuple: DE optimizes over θ₁,...,θ_N (polarization angles)
2. For each θ-config: find x* (vorticity max) via multi-start Nelder-Mead
3. At x*: compute S²ê/|ω|² where ê = ω/|ω|
4. Report the global worst case across all k-tuples and angles
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution
from itertools import combinations

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def get_ks(max_k2=3):
    ks = []
    r = int(np.sqrt(max_k2)) + 1
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            for l in range(-r, r+1):
                mag2 = i*i + j*j + l*l
                if 0 < mag2 <= max_k2:
                    ks.append(np.array([i, j, l], float))
    return ks

def compute_S2e_at_xstar(ks, thetas, n_xstarts=15):
    """
    For given wavevectors and polarization angles:
    1. Build polarization vectors
    2. Find x* that maximizes |ω(x)|²
    3. Compute S²ê/|ω|² at x*
    """
    N = len(ks)
    bases = [build_perp_basis(k) for k in ks]
    vs = [np.cos(thetas[i])*bases[i][0] + np.sin(thetas[i])*bases[i][1] for i in range(N)]

    # Find vorticity max
    def neg_om2(x):
        omega = np.zeros(3)
        for k, v in zip(ks, vs):
            omega += v * np.cos(k @ x)
        return -np.dot(omega, omega)

    best_om2 = 0
    best_x = None
    for _ in range(n_xstarts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        res = minimize(neg_om2, x0, method='Nelder-Mead',
                       options={'xatol': 1e-9, 'fatol': 1e-11, 'maxiter': 5000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()

    if best_x is None or best_om2 < 1e-14:
        return 0.0

    # Compute fields at x*
    omega = np.zeros(3)
    S = np.zeros((3, 3))
    for k, v in zip(ks, vs):
        c = np.cos(k @ best_x)
        omega += v * c
        w = np.cross(k, v)
        k2 = k @ k
        S -= c * (np.outer(w, k) + np.outer(k, w)) / (2 * k2)

    om2 = omega @ omega
    if om2 < 1e-14:
        return 0.0

    e_hat = omega / np.sqrt(om2)
    Se = S @ e_hat
    S2e = Se @ Se

    return S2e / om2

def adversarial_for_ks(ks, n_de_iter=150, popsize=12):
    """Use DE to MAXIMIZE S²ê/|ω|² over polarization angles for given k-set."""
    N = len(ks)
    bounds = [(0, 2*np.pi)] * N

    def neg_S2e(thetas):
        return -compute_S2e_at_xstar(ks, thetas, n_xstarts=8)

    result = differential_evolution(neg_S2e, bounds, maxiter=n_de_iter,
                                     popsize=popsize, seed=42, tol=1e-6)
    return -result.fun

def main():
    print("=" * 70)
    print("ADVERSARIAL S²ê/|ω|² MAXIMIZATION")
    print("Threshold: 0.75 (Key Lemma)")
    print("=" * 70)
    print()

    all_ks = get_ks(3)  # 26 vectors with K²≤3
    n_pool = len(all_ks)
    print(f"Pool: {n_pool} wavevectors with K²≤3")

    for N in [3, 4, 5, 6, 8]:
        print(f"\n--- N = {N} ---")
        # Sample k-tuples and find worst case
        combs = list(combinations(range(n_pool), N))
        np.random.shuffle(combs)

        if N <= 4:
            n_test = min(200, len(combs))
        elif N <= 6:
            n_test = min(80, len(combs))
        else:
            n_test = min(30, len(combs))

        worst = 0
        worst_ks = None

        for idx, combo in enumerate(combs[:n_test]):
            ks = [all_ks[i] for i in combo]
            ratio = adversarial_for_ks(ks, n_de_iter=80, popsize=8)

            if ratio > worst:
                worst = ratio
                worst_ks = ks

            if (idx + 1) % max(1, n_test // 5) == 0:
                print(f"  {idx+1}/{n_test}: worst so far = {worst:.4f} {'< 0.75 ✓' if worst < 0.75 else '≥ 0.75 ✗'}")

        print(f"  RESULT N={N}: worst S²ê/|ω|² = {worst:.4f} (margin: {(0.75 - worst)/0.75:.1%})")
        if worst >= 0.75:
            print(f"  *** VIOLATION at N={N}! ***")
            break

    print()
    print("=" * 70)
    print("SUMMARY")
    print("If all values < 0.75: Key Lemma holds for directional bound")
    print("Margin = how far below 0.75 the worst case is")
    print("=" * 70)

if __name__ == '__main__':
    main()
