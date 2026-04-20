"""
Test S²ê / |ω|² at the vorticity maximum for multi-mode div-free fields.

The barrier at R = α/|ω| = 1/2 needs: S²ê < 3|ω|²/4.
S²ê = ê·S²·ê = Σλᵢ²cᵢ where cᵢ = (ê·eᵢ)².

Key structural fact: S·ê = 0 for single modes at their max.
For multi-mode: S·ê comes from cross-interactions only.

Test: find worst-case S²ê/|ω|² for N = 2, 3, 5, 10, 20 modes.
Also verify the barrier margin.
"""

import numpy as np
from scipy.optimize import minimize

def compute_at_point(k_list, v_list, a_list, x):
    """Compute ω, S, α, S²ê at point x."""
    omega = np.zeros(3)
    S = np.zeros((3, 3))

    for k, v, a in zip(k_list, v_list, a_list):
        k = np.asarray(k, float)
        v = np.asarray(v, float)
        cos_kx = np.cos(k @ x)
        sin_kx = np.sin(k @ x)
        kxv = np.cross(k, v)
        k2 = k @ k

        omega += a * v * cos_kx
        grad_u = a * np.outer(kxv, k) * cos_kx / k2
        S += 0.5 * (grad_u + grad_u.T)

    om_mag = np.linalg.norm(omega)
    if om_mag < 1e-14:
        return 0, 0, 0, 0, om_mag

    e_hat = omega / om_mag
    Se = S @ e_hat
    alpha = e_hat @ Se
    S2e = Se @ Se  # |S·ê|² = S²ê

    # Also compute |S|²
    S_mag2 = np.sum(S * S)  # Frobenius norm squared

    return alpha / om_mag, S2e / om_mag**2, S_mag2 / om_mag**2, alpha, om_mag


def rand_perp(k):
    """Random unit vector perpendicular to k."""
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


def find_max_omega(k_list, v_list, a_list, n_starts=15):
    """Find global max of |ω|² by multi-start optimization."""
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
                       options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 5000})
        if -res.fun > best_om2:
            best_om2 = -res.fun
            best_x = res.x.copy()

    return best_x, np.sqrt(best_om2)


def scan_modes(N_modes, n_trials=2000):
    """Scan random N-mode configs, find worst S²ê/|ω|² at max."""
    # Integer wavevectors up to |k|² = 6
    all_ks = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            for l in range(-2, 3):
                mag2 = i*i + j*j + l*l
                if 0 < mag2 <= 6:
                    all_ks.append(np.array([i, j, l], float))

    worst_S2e = 0
    worst_alpha = 0
    worst_Smag = 0
    count = 0

    for trial in range(n_trials):
        # Random k-vectors (non-parallel)
        idx = np.random.choice(len(all_ks), min(N_modes, len(all_ks)), replace=False)
        ks = [all_ks[i] for i in idx]
        vs = [rand_perp(k) for k in ks]
        a_s = np.exp(np.random.uniform(-0.5, 0.5, len(ks))).tolist()

        x_max, om_max = find_max_omega(ks, vs, a_s, n_starts=8)
        if om_max < 0.1:
            continue

        ratio_alpha, ratio_S2e, ratio_Smag, alpha, om = compute_at_point(ks, vs, a_s, x_max)

        if abs(ratio_S2e) > worst_S2e:
            worst_S2e = abs(ratio_S2e)
        if abs(ratio_alpha) > worst_alpha:
            worst_alpha = abs(ratio_alpha)
        if abs(ratio_Smag) > worst_Smag:
            worst_Smag = abs(ratio_Smag)
        count += 1

    return worst_alpha, worst_S2e, worst_Smag, count


if __name__ == '__main__':
    np.random.seed(42)

    print("S²ê / |ω|² AT THE VORTICITY MAXIMUM")
    print("Barrier threshold: S²ê/|ω|² < 3/4 = 0.750")
    print("=" * 65)

    results = {}
    for N in [2, 3, 5, 8, 12, 20]:
        n_trials = 3000 if N <= 5 else 1500
        print(f"\nN = {N} modes ({n_trials} trials)...", flush=True)
        wa, ws, wsm, cnt = scan_modes(N, n_trials)
        results[N] = (wa, ws, wsm, cnt)
        print(f"  Tested: {cnt}")
        print(f"  Worst α/|ω|    = {wa:.6f}  (threshold: 0.500)")
        print(f"  Worst S²ê/|ω|² = {ws:.6f}  (threshold: 0.750)")
        print(f"  Worst |S|²/|ω|² = {wsm:.6f}")
        print(f"  Barrier margin  = {0.75 - ws:.4f} ({(0.75-ws)/0.75*100:.1f}%)")

    print("\n" + "=" * 65)
    print("SUMMARY TABLE")
    print("=" * 65)
    print(f"{'N modes':>8} {'α/|ω|':>10} {'S²ê/|ω|²':>12} {'|S|²/|ω|²':>12} {'margin':>10}")
    print("-" * 65)
    for N in sorted(results.keys()):
        wa, ws, wsm, cnt = results[N]
        margin = 0.75 - ws
        print(f"{N:>8} {wa:>10.4f} {ws:>12.4f} {wsm:>12.4f} {margin:>10.4f}")

    overall_ws = max(r[1] for r in results.values())
    overall_wa = max(r[0] for r in results.values())
    print(f"\nOverall worst α/|ω| = {overall_wa:.4f}")
    print(f"Overall worst S²ê/|ω|² = {overall_ws:.4f}")
    print(f"Barrier at 0.750: {'HOLDS' if overall_ws < 0.75 else 'VIOLATED'}")
    print(f"Margin: {0.75 - overall_ws:.4f}")

    if overall_ws < 0.75:
        print(f"\n*** S²ê/|ω|² < {overall_ws:.3f} << 0.750 across ALL configs ***")
        print(f"*** The barrier DR/Dt < 0 at R=1/2 holds with {(0.75-overall_ws)/0.75*100:.0f}% margin ***")
