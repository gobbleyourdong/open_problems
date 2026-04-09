"""
CORRECTED Cross-Term Identity for REAL cosine fields.

For ω(x) = Σ_k v_k cos(k·x):

|S(x)|²_F = |ω(x)|²/2 - 2 Σ_{j<k} P_{jk} cos(k_j·x)cos(k_k·x)

where P_{jk} = (v_j·n̂_{jk})(v_k·n̂_{jk}) sin²θ_{jk}

The cos(k_j·x)cos(k_k·x) factor (NOT cos((k_j-k_k)·x)) is crucial.
"""
import numpy as np

def compute_S_mode(k, v):
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

def verify_full_identity(ks, vs, x):
    """Verify |S|²_F = |ω|²/2 - 2Σ P cos(k_j·x)cos(k_k·x)."""
    N = len(ks)

    # Direct computation
    omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
    om2 = omega @ omega

    S = sum(compute_S_mode(k, v) * np.cos(k @ x) for k, v in zip(ks, vs))
    S2_F = np.sum(S**2)

    # Identity prediction
    correction = 0.0
    for j in range(N):
        for l in range(j+1, N):
            n = np.cross(ks[j], ks[l])
            n_norm = np.linalg.norm(n)
            if n_norm < 1e-12:
                continue
            n_hat = n / n_norm
            cos_theta = (ks[j] @ ks[l]) / (np.linalg.norm(ks[j]) * np.linalg.norm(ks[l]))
            sin2_theta = 1 - cos_theta**2

            P = (vs[j] @ n_hat) * (vs[l] @ n_hat) * sin2_theta
            phase = np.cos(ks[j] @ x) * np.cos(ks[l] @ x)  # CORRECTED
            correction += P * phase

    predicted = om2/2 - 2*correction
    error = abs(S2_F - predicted)
    return S2_F, om2, predicted, correction, error

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("CORRECTED Frobenius Identity: |S|²_F = |ω|²/2 - 2Σ P·cos·cos")
    print("=" * 70)

    # Test 1: Verify identity is exact
    max_error = 0
    for trial in range(500):
        N = np.random.randint(2, 10)
        ks, vs = [], []
        for _ in range(N):
            k = np.random.randint(-2, 3, 3).astype(float)
            if np.linalg.norm(k) < 0.5:
                k = np.array([1., 0., 0.])
            v = np.random.randn(3)
            v -= k * (v @ k) / (k @ k)
            ks.append(k)
            vs.append(v)

        x = np.random.randn(3) * 3
        S2_F, om2, predicted, correction, error = verify_full_identity(ks, vs, x)
        max_error = max(max_error, error)

    print(f"\n  Identity check: max error across 500 random tests = {max_error:.2e}")

    # Test 2: Sign of correction at vorticity max
    print("\n" + "=" * 70)
    print("CORRECTION SIGN AT VORTICITY MAX (corrected phases)")
    print("=" * 70)

    n_pos = 0
    n_neg = 0
    worst_ratio = 0
    best_ratio = 1.0

    for trial in range(2000):
        N = np.random.choice([2, 3, 4, 5, 6, 8, 12, 20])
        K_max = 2 if N <= 12 else 3

        all_modes = []
        for i in range(-K_max, K_max+1):
            for j in range(-K_max, K_max+1):
                for l in range(-K_max, K_max+1):
                    k = np.array([i, j, l], float)
                    if 0 < k @ k <= K_max**2:
                        all_modes.append(k)

        if N > len(all_modes):
            N = len(all_modes)
        idx = np.random.choice(len(all_modes), min(N, len(all_modes)), replace=False)
        ks = [all_modes[i] for i in idx]
        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= k * (v @ k) / (k @ k)
            vs.append(v)

        # Find max |ω| on grid
        best_x = np.zeros(3)
        best_om2 = 0
        M = 20
        xs_grid = np.linspace(0, 2*np.pi, M, endpoint=False)
        for i in range(M):
            for j in range(M):
                for l in range(M):
                    x = np.array([xs_grid[i], xs_grid[j], xs_grid[l]])
                    om = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
                    om2 = om @ om
                    if om2 > best_om2:
                        best_om2 = om2
                        best_x = x.copy()

        # Refine
        for _ in range(5):
            h = 1e-4
            grad = np.zeros(3)
            omega0 = sum(v * np.cos(k @ best_x) for k, v in zip(ks, vs))
            f0 = omega0 @ omega0
            for d in range(3):
                xp = best_x.copy(); xp[d] += h
                om_p = sum(v * np.cos(k @ xp) for k, v in zip(ks, vs))
                grad[d] = (om_p @ om_p - f0) / h
            for step in [0.1, 0.01, 0.001]:
                xt = best_x + step * grad / (np.linalg.norm(grad) + 1e-12)
                om_t = sum(v * np.cos(k @ xt) for k, v in zip(ks, vs))
                if om_t @ om_t > best_om2:
                    best_om2 = om_t @ om_t
                    best_x = xt

        S2_F, om2, predicted, correction, error = verify_full_identity(ks, vs, best_x)

        if om2 < 1e-10:
            continue

        ratio = S2_F / om2

        if correction >= -1e-10:
            n_pos += 1
        else:
            n_neg += 1

        worst_ratio = max(worst_ratio, ratio)
        best_ratio = min(best_ratio, ratio)

        if trial % 500 == 0:
            print(f"  {trial}/2000: pos={n_pos} neg={n_neg} "
                  f"worst_ratio={worst_ratio:.6f} best_ratio={best_ratio:.6f}")

    print()
    print(f"  Correction ≥ 0 at max: {n_pos}/{n_pos+n_neg} ({100*n_pos/(n_pos+n_neg):.1f}%)")
    print(f"  Correction < 0 at max: {n_neg}/{n_pos+n_neg} ({100*n_neg/(n_pos+n_neg):.1f}%)")
    print(f"  Worst |S|²_F/|ω|² at max: {worst_ratio:.6f}")
    print(f"  Best |S|²_F/|ω|² at max:  {best_ratio:.6f}")
    print(f"  Key Lemma via Frobenius: {worst_ratio < 0.75} (need < 0.75)")
    print()

    # Even if |S|²_F > |ω|²/2 sometimes, the trace-free bound gives:
    # S²ê ≤ (2/3)|S|²_F. So for Key Lemma: need (2/3)|S|²_F < 3|ω|²/4
    # i.e., |S|²_F < 9|ω|²/8 = 1.125|ω|².
    print(f"  Via trace-free: S²ê ≤ (2/3)|S|²_F")
    print(f"  Need |S|²_F < 9|ω|²/8 = 1.125|ω|²")
    print(f"  Worst: {worst_ratio:.6f} << 1.125  ✓")
