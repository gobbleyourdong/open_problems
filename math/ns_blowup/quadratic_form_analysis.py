"""
QUADRATIC FORM ANALYSIS

The target: 4C + |ω|² > 0 at x* = argmax|ω|.

Expanding at x* = 0 (WLOG, translate max to origin):
  w_k = v_k  (effective amplitudes, cos(k·0) = 1 for all k)

  |ω|² = |Σ w_k|²
  C = Σ_{j<k} (w_j·n̂_{jk})(w_k·n̂_{jk}) sin²θ_{jk}

4C + |ω|² = 4Σ_{j<k} (w_j·n̂)(w_k·n̂)sin²θ + |Σw_k|²

This is a QUADRATIC FORM in the w_k. If positive semi-definite: done.

Key constraint: at the max, all modes point in the same half-space
(sign-flip: w_k·ê ≥ 0 for all k, where ê = ω/|ω|).

Q: Is 4C + |ω|² > 0 for all div-free {w_k} with the sign-flip constraint?
Or is it > 0 WITHOUT the constraint?
"""
import numpy as np
from itertools import combinations

def compute_quadratic_form(ks, ws):
    """Compute Q = 4C + |ω|² for given k-vectors and amplitudes."""
    N = len(ks)

    omega = sum(ws)
    om2 = omega @ omega

    C = 0.0
    for j in range(N):
        for l in range(j+1, N):
            n = np.cross(ks[j], ks[l])
            n_norm = np.linalg.norm(n)
            if n_norm < 1e-12:
                continue
            n_hat = n / n_norm
            cos_theta = (ks[j] @ ks[l]) / (np.linalg.norm(ks[j]) * np.linalg.norm(ks[l]))
            sin2_theta = 1 - cos_theta**2
            C += (ws[j] @ n_hat) * (ws[l] @ n_hat) * sin2_theta

    Q = 4*C + om2
    return Q, C, om2

def test_positivity_without_constraint(ks, n_trials=10000):
    """Test if Q = 4C + |ω|² > 0 for ARBITRARY div-free w_k (no sign-flip)."""
    N = len(ks)
    min_Q = float('inf')
    min_ratio = float('inf')  # C/|ω|²

    for _ in range(n_trials):
        ws = []
        for k in ks:
            v = np.random.randn(3)
            v -= k * (v @ k) / (k @ k)
            # Random magnitude
            v *= np.random.exponential(1)
            ws.append(v)

        Q, C, om2 = compute_quadratic_form(ks, ws)
        if om2 > 1e-10:
            min_Q = min(min_Q, Q)
            min_ratio = min(min_ratio, C/om2)

    return min_Q, min_ratio

def test_positivity_adversarial(ks, n_trials=5000):
    """Adversarial search for minimum Q using optimization."""
    from scipy.optimize import minimize
    N = len(ks)

    # Parameterize w_k by angles in the plane ⊥ k_j and magnitude
    def perp_basis(k):
        kn = k / np.linalg.norm(k)
        ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
        e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
        e2 = np.cross(kn, e1)
        return e1, e2

    bases = [perp_basis(k) for k in ks]

    min_Q = float('inf')

    for _ in range(n_trials):
        # Random initialization: angle + magnitude for each mode
        x0 = np.random.randn(2*N)  # theta, log_mag for each

        def neg_Q(params):
            ws = []
            for i in range(N):
                theta = params[2*i]
                mag = np.exp(np.clip(params[2*i+1], -3, 3))
                e1, e2 = bases[i]
                w = mag * (np.cos(theta)*e1 + np.sin(theta)*e2)
                ws.append(w)
            Q, _, om2 = compute_quadratic_form(ks, ws)
            if om2 < 1e-15:
                return 0.0
            return Q / om2  # Minimize Q/|ω|² (scale-invariant)

        res = minimize(neg_Q, x0, method='Nelder-Mead',
                      options={'maxiter': 500, 'fatol': 1e-12})
        min_Q = min(min_Q, res.fun)

    return min_Q

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("QUADRATIC FORM POSITIVITY TEST")
    print("Q = 4C + |ω|² ≥ 0?  (Equivalently: C/|ω|² ≥ -1/4)")
    print("=" * 70)

    # Build k-vectors for different shells
    all_modes = {}
    for i in range(-3, 4):
        for j in range(-3, 4):
            for l in range(-3, 4):
                k = np.array([i, j, l], float)
                k2 = int(k @ k)
                if 0 < k2 <= 9:
                    if k2 not in all_modes:
                        all_modes[k2] = []
                    # Only keep unique (no -k)
                    if not any(np.allclose(k, -u) for u in all_modes[k2]):
                        all_modes[k2].append(k)

    # Test 1: WITHOUT sign-flip constraint (worst case)
    print("\nTest 1: Q positivity WITHOUT sign-flip (arbitrary w_k)")
    print("(If Q > 0 always: proof complete, no constraint needed!)")

    for k2 in [1, 2, 3]:
        vecs = all_modes[k2]
        for N in [2, 3, min(4, len(vecs))]:
            if N > len(vecs):
                continue
            for sub in list(combinations(range(len(vecs)), N))[:10]:
                ks = [vecs[i] for i in sub]
                min_Q, min_ratio = test_positivity_without_constraint(ks, 5000)
                if min_Q < 0.01:
                    print(f"  |k|²={k2}, N={N}: min Q/|ω|² = {min_ratio+0.25:.6f}+1/4"
                          f"  (C/|ω|² = {min_ratio:.6f})")

    # Test 2: Adversarial minimization of Q/|ω|²
    print("\nTest 2: Adversarial minimization of Q/|ω|²")

    overall_min = float('inf')
    for k2 in [1, 2, 3, 4, 5]:
        if k2 not in all_modes:
            continue
        vecs = all_modes[k2]
        shell_min = float('inf')

        for N in [2, 3, min(4, len(vecs))]:
            if N > len(vecs):
                continue
            subs = list(combinations(range(len(vecs)), N))
            if len(subs) > 20:
                np.random.shuffle(subs)
                subs = subs[:20]

            for sub in subs:
                ks = [vecs[i] for i in sub]
                min_q = test_positivity_adversarial(ks, 200)
                shell_min = min(shell_min, min_q)

        overall_min = min(overall_min, shell_min)
        print(f"  |k|²={k2}: min Q/|ω|² = {shell_min:.6f} (≥ 0? {shell_min >= -1e-6})")

    # Mixed shells
    print("\n  Mixed shells:")
    all_vecs_flat = []
    for k2 in sorted(all_modes.keys()):
        all_vecs_flat.extend(all_modes[k2])

    for trial in range(50):
        N = np.random.randint(2, 6)
        if N > len(all_vecs_flat):
            continue
        idx = np.random.choice(len(all_vecs_flat), N, replace=False)
        ks = [all_vecs_flat[i] for i in idx]
        min_q = test_positivity_adversarial(ks, 100)
        overall_min = min(overall_min, min_q)

    print(f"  Overall min Q/|ω|²: {overall_min:.6f}")

    print()
    print(f"=" * 70)
    print(f"RESULT: min Q/|ω|² = {overall_min:.6f}")
    if overall_min >= -1e-6:
        print(f"Q ≥ 0 ALWAYS (no sign-flip needed!)")
        print(f"→ C ≥ -|ω|²/4 for ALL div-free fields")
        print(f"→ |S|²_F ≤ |ω|² for ALL div-free fields")
        print(f"→ S²ê ≤ (2/3)|ω|² < 3|ω|²/4")
        print(f"→ KEY LEMMA HOLDS")
    else:
        print(f"Q can be negative without sign-flip constraint.")
        print(f"Sign-flip at the max is NEEDED for the bound.")
