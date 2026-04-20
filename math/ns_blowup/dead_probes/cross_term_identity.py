"""
CROSS-TERM IDENTITY VERIFICATION

Claim: For two Fourier modes with k_j, k_k and div-free amplitudes v_j ⊥ k_j, v_k ⊥ k_k:

  2 Tr(Ŝ_j Ŝ_kᵀ) - (v_j · v_k) = -2(v_j · n̂)(v_k · n̂) sin²θ

where θ = angle between k_j and k_k, and n̂ = (k_j × k_k)/|k_j × k_k|.

Consequence: At x* = argmax|ω|:
  |S(x*)|²_F = |ω(x*)|²/2 - 2 Σ_{j<k} (v_j·n̂_{jk})(v_k·n̂_{jk}) sin²θ_{jk} cos(q_{jk}·x*)

If the correction is ≥ 0 at x*: |S|²_F ≤ |ω|²/2 → S²ê ≤ |S|²_F ≤ |ω|²/2 < 3|ω|²/4.
KEY LEMMA FOLLOWS.
"""
import numpy as np

def compute_S_mode(k, v):
    """Compute Ŝ = -(w⊗k + k⊗w)/(2|k|²) where w = k × v"""
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

def verify_identity(k_j, k_k, v_j, v_k, verbose=True):
    """Verify the cross-term identity for one pair."""
    # Compute strain modes
    S_j = compute_S_mode(k_j, v_j)
    S_k = compute_S_mode(k_k, v_k)

    # LHS: 2 Tr(Ŝ_j Ŝ_kᵀ) - v_j·v_k
    cross_S = np.sum(S_j * S_k)  # Tr(Ŝ_j Ŝ_kᵀ) = Frobenius inner product
    cross_omega = v_j @ v_k
    LHS = 2 * cross_S - cross_omega

    # RHS: -2(v_j·n̂)(v_k·n̂) sin²θ
    n = np.cross(k_j, k_k)
    n_norm = np.linalg.norm(n)

    if n_norm < 1e-12:
        # Parallel k-vectors: sin²θ = 0, RHS = 0
        RHS = 0.0
    else:
        n_hat = n / n_norm
        cos_theta = (k_j @ k_k) / (np.linalg.norm(k_j) * np.linalg.norm(k_k))
        sin2_theta = 1 - cos_theta**2
        RHS = -2 * (v_j @ n_hat) * (v_k @ n_hat) * sin2_theta

    if verbose:
        print(f"  k_j={k_j.astype(int)}, k_k={k_k.astype(int)}")
        print(f"  LHS = {LHS:.10f}")
        print(f"  RHS = {RHS:.10f}")
        print(f"  Match: {abs(LHS-RHS) < 1e-10}")

    return abs(LHS - RHS) < 1e-8

def verify_frobenius_identity(ks, vs, x):
    """Verify |S|²_F = |ω|²/2 - 2Σ correction at point x."""
    N = len(ks)

    # Compute ω and S at x
    omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
    om2 = omega @ omega

    S = sum(compute_S_mode(k, v) * np.cos(k @ x) for k, v in zip(ks, vs))
    S2_F = np.sum(S**2)

    # Compute correction
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
            q = ks[j] - ks[l]
            phase = np.cos(q @ x)
            correction += (vs[j] @ n_hat) * (vs[l] @ n_hat) * sin2_theta * phase

    # Check identity
    predicted = om2/2 - 2*correction
    error = abs(S2_F - predicted)

    return S2_F, om2, predicted, correction, error

if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("CROSS-TERM IDENTITY VERIFICATION")
    print("2 Tr(Ŝ_j Ŝ_kᵀ) - (v_j·v_k) = -2(v_j·n̂)(v_k·n̂) sin²θ")
    print("=" * 70)
    print()

    # Test 1: Orthogonal k-vectors
    print("Test 1: Orthogonal k")
    verify_identity(np.array([1,0,0.]), np.array([0,1,0.]),
                   np.array([0,1,1.]), np.array([1,0,-1.]))

    # Test 2: Same k-vectors
    print("\nTest 2: Parallel k")
    verify_identity(np.array([1,0,0.]), np.array([2,0,0.]),
                   np.array([0,1,0.]), np.array([0,0,1.]))

    # Test 3: General angles
    print("\nTest 3: General angle (45°)")
    verify_identity(np.array([1,0,0.]), np.array([1,1,0.]),
                   np.array([0,1,0.]), np.array([-1,1,0.])/np.sqrt(2))
    # Oops, v_k must be ⊥ k_k. k=(1,1,0), v must have v·k=0.
    # (-1,1,0)·(1,1,0) = 0 ✓, |v|=√2, already divided

    # Test 4: Random pairs (exhaustive)
    print("\n" + "=" * 70)
    print("Random pair verification (1000 pairs)")
    print("=" * 70)
    n_pass = 0
    n_total = 1000
    for _ in range(n_total):
        k_j = np.random.randint(-3, 4, 3).astype(float)
        k_k = np.random.randint(-3, 4, 3).astype(float)
        if np.linalg.norm(k_j) < 0.5 or np.linalg.norm(k_k) < 0.5:
            continue

        # Random div-free amplitudes
        v_j = np.random.randn(3)
        v_j -= k_j * (v_j @ k_j) / (k_j @ k_j)
        v_k = np.random.randn(3)
        v_k -= k_k * (v_k @ k_k) / (k_k @ k_k)

        if verify_identity(k_j, k_k, v_j, v_k, verbose=False):
            n_pass += 1

    print(f"  Passed: {n_pass}/{n_total}")

    # Test 5: Full Frobenius identity at random points
    print("\n" + "=" * 70)
    print("Full Frobenius identity: |S|²_F = |ω|²/2 - 2Σ correction")
    print("=" * 70)
    print()

    max_error = 0
    for trial in range(100):
        N = np.random.randint(2, 8)
        ks = []
        vs = []
        for _ in range(N):
            k = np.random.randint(-2, 3, 3).astype(float)
            if np.linalg.norm(k) < 0.5:
                k = np.array([1, 0, 0.])
            v = np.random.randn(3)
            v -= k * (v @ k) / (k @ k)
            ks.append(k)
            vs.append(v)

        x = np.random.randn(3) * 2

        S2_F, om2, predicted, correction, error = verify_frobenius_identity(ks, vs, x)
        max_error = max(max_error, error)

    print(f"  Max error across 100 random tests: {max_error:.2e}")

    # Test 6: AT THE VORTICITY MAX — is correction ≥ 0?
    print("\n" + "=" * 70)
    print("CORRECTION SIGN AT VORTICITY MAX")
    print("If correction ≥ 0 at x*: |S|²_F ≤ |ω|²/2 → KEY LEMMA")
    print("=" * 70)
    print()

    n_positive = 0
    n_negative = 0
    worst_excess = 0  # max of (|S|²_F - |ω|²/2) / |ω|²

    for trial in range(500):
        N = np.random.choice([2, 3, 4, 5, 6, 8, 12])
        K_max = 2

        # Random modes from lattice
        all_modes = []
        for i in range(-K_max, K_max+1):
            for j in range(-K_max, K_max+1):
                for l in range(-K_max, K_max+1):
                    k = np.array([i, j, l], float)
                    if 0 < k @ k <= K_max**2:
                        all_modes.append(k)

        if N > len(all_modes):
            N = len(all_modes)
        idx = np.random.choice(len(all_modes), N, replace=False)
        ks = [all_modes[i] for i in idx]
        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= k * (v @ k) / (k @ k)
            vs.append(v)

        # Find max |ω|
        best_x = np.zeros(3)
        best_om2 = 0
        M = 24
        xs = np.linspace(0, 2*np.pi, M, endpoint=False)
        for i in range(M):
            for j in range(M):
                for l in range(M):
                    x = np.array([xs[i], xs[j], xs[l]])
                    om = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
                    om2 = om @ om
                    if om2 > best_om2:
                        best_om2 = om2
                        best_x = x.copy()

        # Compute at max
        S2_F, om2, predicted, correction, error = verify_frobenius_identity(ks, vs, best_x)

        if correction >= -1e-10:
            n_positive += 1
        else:
            n_negative += 1
            excess = (S2_F - om2/2) / om2 if om2 > 1e-10 else 0
            worst_excess = max(worst_excess, excess)

        if trial % 100 == 0:
            print(f"  {trial}/500: pos={n_positive} neg={n_negative} worst_excess={worst_excess:.6f}")

    print()
    print(f"  RESULT: correction ≥ 0 at max: {n_positive}/{n_positive+n_negative}")
    print(f"  correction < 0 at max: {n_negative}/{n_positive+n_negative}")
    print(f"  Worst |S|²_F/|ω|² excess above 1/2: {worst_excess:.6f}")
    print(f"  Worst |S|²_F/|ω|² ratio: {0.5 + worst_excess:.6f} (need < 0.75)")
