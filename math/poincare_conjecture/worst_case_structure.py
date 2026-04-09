"""
Find the EXACT worst-case configuration for |S|²_F/|ω|² at the vorticity max.
Understand its structure to guide the proof.

Key question: What makes C/|ω|² most negative?
From the identity: |S|²_F = |ω|²/2 - 2C.
Worst |S|²_F/|ω|² ⟺ most negative C/|ω|².
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution
from itertools import product as iprod

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def compute_ratios_at_max(ks, thetas):
    """Compute |S|²_F/|ω|² and S²ê/|ω|² at the global max."""
    N = len(ks)
    bases = [build_perp_basis(k) for k in ks]
    vs = [np.cos(thetas[i])*bases[i][0] + np.sin(thetas[i])*bases[i][1] for i in range(N)]

    # Find global max over sign patterns
    best_om2 = 0
    best_signs = None
    for signs in iprod([1.0, -1.0], repeat=N):
        omega = sum(s*v for s, v in zip(signs, vs))
        om2 = omega @ omega
        if om2 > best_om2:
            best_om2 = om2
            best_signs = signs

    if best_om2 < 1e-15:
        return None

    signs = best_signs
    omega = sum(s*v for s, v in zip(signs, vs))
    om2 = omega @ omega
    e_hat = omega / np.sqrt(om2)

    # Compute S (both involve cos, evaluated at x*=0 where cos=1)
    S = np.zeros((3, 3))
    for k, v, s in zip(ks, vs, signs):
        w = np.cross(k, s*v)
        k2 = k @ k
        S -= (np.outer(w, k) + np.outer(k, w)) / (2 * k2)

    S2_F = np.sum(S**2)
    Se = S @ e_hat
    S2e = Se @ Se
    alpha = e_hat @ S @ e_hat

    # Correction C
    C = (om2/2 - S2_F) / 2

    # Self-vanishing angles
    gammas = []
    for v, s in zip(vs, signs):
        sv = s * v
        a = np.linalg.norm(sv)
        if a > 1e-12:
            cos_g = abs(sv @ e_hat) / a
            gammas.append(np.degrees(np.arccos(min(cos_g, 1.0))))
        else:
            gammas.append(90.0)

    return {
        'om2': om2, 'S2_F': S2_F, 'S2e': S2e,
        'frob_ratio': S2_F/om2, 's2e_ratio': S2e/om2,
        'C': C, 'C_ratio': C/om2,
        'alpha': alpha, 'alpha_ratio': alpha/np.sqrt(om2),
        'signs': signs, 'gammas': gammas,
    }

def find_worst_frob(ks, n_restarts=20):
    """Find thetas that maximize |S|²_F/|ω|² at global max."""
    N = len(ks)
    best_ratio = 0
    best_thetas = None
    best_result = None

    for _ in range(n_restarts):
        x0 = np.random.uniform(0, 2*np.pi, N)
        def neg_frob(t):
            r = compute_ratios_at_max(ks, t)
            return -(r['frob_ratio'] if r else 0)
        res = minimize(neg_frob, x0, method='Nelder-Mead',
                      options={'maxiter': 2000, 'fatol': 1e-12})
        r = compute_ratios_at_max(ks, res.x)
        if r and r['frob_ratio'] > best_ratio:
            best_ratio = r['frob_ratio']
            best_thetas = res.x.copy()
            best_result = r

    return best_thetas, best_result

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("WORST-CASE STRUCTURE ANALYSIS")
    print("Finding configs that maximize |S|²_F/|ω|² at the max")
    print("=" * 70)

    # Test on several k-vector sets
    configs = [
        ("K=1 orthogonal", [np.array([1,0,0.]), np.array([0,1,0.])]),
        ("K=1 full", [np.array([1,0,0.]), np.array([0,1,0.]), np.array([0,0,1.])]),
        ("K=√2 pair", [np.array([1,1,0.]), np.array([1,0,1.])]),
        ("K=1+√2", [np.array([1,0,0.]), np.array([1,1,0.])]),
        ("K=1+√2 mix", [np.array([1,0,0.]), np.array([0,1,0.]), np.array([1,1,0.])]),
        ("K=1+2", [np.array([1,0,0.]), np.array([2,0,0.])]),
        ("K=1+2 orth", [np.array([1,0,0.]), np.array([0,2,0.])]),
        ("K=1,2 mix", [np.array([1,0,0.]), np.array([0,1,0.]), np.array([0,0,2.])]),
    ]

    for name, ks in configs:
        thetas, result = find_worst_frob(ks, n_restarts=30)
        if result is None:
            continue
        print(f"\n{name} (N={len(ks)}):")
        print(f"  |S|²_F/|ω|² = {result['frob_ratio']:.6f}")
        print(f"  S²ê/|ω|² = {result['s2e_ratio']:.6f}")
        print(f"  C/|ω|² = {result['C_ratio']:.6f}")
        print(f"  α/|ω| = {result['alpha_ratio']:.6f}")
        print(f"  γ angles: {[f'{g:.1f}°' for g in result['gammas']]}")
        print(f"  signs: {result['signs']}")

    # Now: exhaustive search over many k-pairs to find the absolute worst
    print("\n" + "=" * 70)
    print("EXHAUSTIVE SEARCH: worst |S|²_F/|ω|² for N=2")
    print("=" * 70)

    worst = 0
    worst_ks = None
    worst_result = None

    from itertools import combinations
    all_k = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i,j,l], float)
                if 0 < k@k <= 9:
                    if not any(np.allclose(k, -u) for u in all_k):
                        all_k.append(k)

    for i, j_idx in combinations(range(len(all_k)), 2):
        ks = [all_k[i], all_k[j_idx]]
        thetas, result = find_worst_frob(ks, n_restarts=10)
        if result and result['frob_ratio'] > worst:
            worst = result['frob_ratio']
            worst_ks = ks
            worst_result = result

    print(f"\n  Worst N=2: |S|²_F/|ω|² = {worst:.8f}")
    print(f"  k-vectors: {[k.astype(int).tolist() for k in worst_ks]}")
    print(f"  C/|ω|² = {worst_result['C_ratio']:.8f}")
    print(f"  S²ê/|ω|² = {worst_result['s2e_ratio']:.8f}")
    print(f"  α/|ω| = {worst_result['alpha_ratio']:.8f}")
    print(f"  γ angles: {[f'{g:.1f}°' for g in worst_result['gammas']]}")

    # Analyze: what's the relationship between the two k-vectors?
    k1, k2 = worst_ks
    cos_angle = (k1@k2)/(np.linalg.norm(k1)*np.linalg.norm(k2))
    print(f"  angle(k1,k2) = {np.degrees(np.arccos(np.clip(cos_angle,-1,1))):.1f}°")
    print(f"  |k1|² = {k1@k1:.0f}, |k2|² = {k2@k2:.0f}")
