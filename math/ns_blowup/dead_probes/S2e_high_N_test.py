"""
Test S²ê/|ω|² for HIGH N modes using the PROVEN reliable method
(Nelder-Mead multi-start, same as original S2e_bound_test.py).
Focus on N = 20, 30, 50 to see if the bound ever exceeds 0.75.
"""
import numpy as np
from scipy.optimize import minimize

def rand_perp(k):
    k = np.asarray(k, float)
    kn = k / np.linalg.norm(k)
    r = np.random.randn(3)
    r -= (r @ kn) * kn
    norm = np.linalg.norm(r)
    if norm < 1e-10:
        r = np.random.randn(3)
        r -= (r @ kn) * kn
        norm = np.linalg.norm(r)
    return r / norm

def compute_at_point(k_list, v_list, a_list, x):
    omega = np.zeros(3)
    S = np.zeros((3, 3))
    grad_u = np.zeros((3, 3))
    for k, v, a in zip(k_list, v_list, a_list):
        k = np.asarray(k, float)
        v = np.asarray(v, float)
        cos_kx = np.cos(k @ x)
        kxv = np.cross(k, v)
        k2 = k @ k
        omega += a * v * cos_kx
        gu = a * np.outer(kxv, k) * cos_kx / k2
        grad_u += gu
        S += 0.5 * (gu + gu.T)

    om_mag2 = omega @ omega
    if om_mag2 < 1e-14:
        return None
    om_mag = np.sqrt(om_mag2)
    e_hat = omega / om_mag
    Se = S @ e_hat
    alpha = e_hat @ Se
    S2e = Se @ Se
    S_mag2 = np.sum(S * S)
    gradu_mag2 = np.sum(grad_u * grad_u)
    return {
        'alpha_ratio': alpha / om_mag,
        'S2e_ratio': S2e / om_mag2,
        'S_ratio': S_mag2 / om_mag2,
        'gradu_ratio': gradu_mag2 / om_mag2,
        'om_mag': om_mag,
    }

def find_max_omega(k_list, v_list, a_list, n_starts=20):
    best_om2 = 0
    best_x = None
    for _ in range(n_starts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        def neg_om2(xyz):
            omega = np.zeros(3)
            for k, v, a in zip(k_list, v_list, a_list):
                omega += a * np.asarray(v) * np.cos(np.asarray(k, float) @ xyz)
            return -np.dot(omega, omega)
        res = minimize(neg_om2, x0, method='Nelder-Mead',
                       options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 10000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()
    return best_x

def get_ks(max_k=2):
    """All integer k with |k|² ≤ max_k² × 3 and |k| > 0."""
    ks = []
    for i in range(-max_k, max_k+1):
        for j in range(-max_k, max_k+1):
            for l in range(-max_k, max_k+1):
                mag2 = i*i + j*j + l*l
                if 0 < mag2 <= max_k*max_k*3:
                    ks.append(np.array([i, j, l], float))
    return ks

def scan(N_modes, n_trials, max_k=2, n_starts=20):
    all_ks = get_ks(max_k)
    worst_S2e = 0
    worst_gradu = 0
    worst_alpha = 0
    n_done = 0

    for trial in range(n_trials):
        idx = np.random.choice(len(all_ks), min(N_modes, len(all_ks)), replace=False)
        ks = [all_ks[i] for i in idx]
        vs = [rand_perp(k) for k in ks]
        amp = np.exp(np.random.uniform(-0.5, 0.5, len(ks))).tolist()

        x_max = find_max_omega(ks, vs, amp, n_starts=n_starts)
        if x_max is None:
            continue
        r = compute_at_point(ks, vs, amp, x_max)
        if r is None:
            continue

        n_done += 1
        worst_S2e = max(worst_S2e, abs(r['S2e_ratio']))
        worst_gradu = max(worst_gradu, r['gradu_ratio'])
        worst_alpha = max(worst_alpha, abs(r['alpha_ratio']))

        if trial % 100 == 0 and trial > 0:
            print(f"  [{trial}/{n_trials}] worst S²ê/ω²={worst_S2e:.4f}, ∇u²/ω²={worst_gradu:.4f}", flush=True)

    return worst_S2e, worst_gradu, worst_alpha, n_done


if __name__ == '__main__':
    np.random.seed(42)
    print("HIGH-N S²ê TEST (Nelder-Mead multi-start)")
    print("=" * 70)

    for N in [3, 5, 8, 12, 20, 30]:
        n_trials = 500 if N <= 12 else 200
        n_starts = 25 if N <= 12 else 30
        max_k = 2

        print(f"\nN={N} modes, {n_trials} trials, {n_starts} restarts, max_k={max_k}")
        ws, wg, wa, nd = scan(N, n_trials, max_k=max_k, n_starts=n_starts)
        barrier = "PASS" if ws < 0.75 else "**FAIL**"
        print(f"  Done: {nd} valid trials")
        print(f"  Worst S²ê/|ω|² = {ws:.6f}  ({barrier})")
        print(f"  Worst |∇u|²/|ω|² = {wg:.6f}  (threshold: 1.625)")
        print(f"  Worst |α|/|ω| = {wa:.6f}  (threshold: 0.500)")
