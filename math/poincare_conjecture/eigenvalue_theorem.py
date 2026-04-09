"""
numerical track Cycle 3 — Single-Mode Eigenvalue Theorem

THEOREM: For a divergence-free Fourier mode (k, v) with |v|=1, v⊥k,
the strain matrix S_k = -(k⊗w + w⊗k)/(2|k|²) where w = k×v has:

  eigenvalues:  {0, +1/2, -1/2}
  eigenvectors: {v, (k̂+ŵ)/√2, (k̂-ŵ)/√2}  where k̂=k/|k|, ŵ=w/|w|

PROOF:
  1. S_k v = 0: (v·w)k + (v·k)w = 0 since v⊥k and v·(k×v)=0. [Cycle 1b]
  2. tr(S_k) = 0: S is traceless since (k⊗w + w⊗k) has tr = 2(k·w) = 0. [k⊥w]
  3. ||S_k||²_F = |ω|²/2 = 1/2: Single-mode theorem. [Proven in Lean]
  4. Eigenvalues {0, λ, -λ} with λ² + λ² = 1/2 → λ = 1/2.
  5. Eigenvectors of (k⊗w + w⊗k) in the k-w plane: k̂±ŵ.

COROLLARIES (all Lean-provable):
  C1. ||S_k||_op = 1/2  (operator norm)
  C2. |S_j v_k| ≤ 1/2 for any unit v_k  (per-term bound)
  C3. S_j v_j = 0  (self-interaction vanishes)
  C4. v_j · S_j v_k = 0 for all k  (orthogonality to own polarization)
  C5. F_j = Σ_k c_k S_j v_k ⊥ v_j  (per-mode strain ⊥ own vorticity)

SIGNIFICANCE: The complete eigenstructure of S_k is determined by ONE number
(the 1/2 from the single-mode theorem). Everything follows algebraically.
"""
import numpy as np

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref); e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1); return e1, e2

def verify_eigenstructure(n_tests=10000):
    """Verify the eigenvalue theorem for random modes."""
    print("VERIFYING EIGENVALUE THEOREM")
    print("=" * 60)

    max_ev_error = 0
    max_evec_error = 0

    for _ in range(n_tests):
        # Random mode
        k = np.random.randint(-3, 4, 3).astype(float)
        if k @ k < 0.5:
            continue
        e1, e2 = build_perp_basis(k)
        theta = np.random.uniform(0, 2*np.pi)
        v = np.cos(theta)*e1 + np.sin(theta)*e2

        w = np.cross(k, v)
        k2 = k @ k
        S = -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

        # Eigendecomposition
        evals, evecs = np.linalg.eigh(S)
        evals_sorted = np.sort(evals)

        # Check eigenvalues = {-1/2, 0, +1/2}
        expected = np.array([-0.5, 0.0, 0.5])
        ev_error = np.max(np.abs(evals_sorted - expected))
        max_ev_error = max(max_ev_error, ev_error)

        # Check that v is the zero-eigenvector
        Sv = S @ v
        evec_error = np.linalg.norm(Sv)
        max_evec_error = max(max_evec_error, evec_error)

        # Check predicted eigenvectors for ±1/2
        k_hat = k / np.linalg.norm(k)
        w_hat = w / np.linalg.norm(w)
        e_plus = (k_hat + w_hat) / np.sqrt(2)
        e_minus = (k_hat - w_hat) / np.sqrt(2)

        # S e_plus should = -1/2 e_plus (or +1/2, depending on sign convention)
        Se_plus = S @ e_plus
        Se_minus = S @ e_minus

        # Check: Se = λe means Se × e = 0 (parallel)
        cross_plus = np.linalg.norm(np.cross(Se_plus, e_plus))
        cross_minus = np.linalg.norm(np.cross(Se_minus, e_minus))
        max_evec_error = max(max_evec_error, cross_plus, cross_minus)

    print(f"  Tests: {n_tests}")
    print(f"  Max eigenvalue error: {max_ev_error:.2e} (should be ~0)")
    print(f"  Max eigenvector error: {max_evec_error:.2e} (should be ~0)")
    print(f"  Eigenvalues = {{-1/2, 0, +1/2}}: {'CONFIRMED' if max_ev_error < 1e-10 else 'FAILED'}")
    print(f"  v is zero-eigenvector: {'CONFIRMED' if max_evec_error < 1e-10 else 'FAILED'}")
    print()

    # Check which eigenvalue goes with which eigenvector
    k = np.array([1., 0., 0.])
    v = np.array([0., 1., 0.])
    w = np.cross(k, v)  # = (0, 0, 1)
    S = -(np.outer(w, k) + np.outer(k, w)) / 2

    print("  Example: k=(1,0,0), v=(0,1,0), w=(0,0,1)")
    print(f"  S = \n{S}")
    evals, evecs = np.linalg.eigh(S)
    print(f"  Eigenvalues: {evals}")
    print(f"  Eigenvectors (columns):\n{evecs}")
    print()

    k_hat = k / np.linalg.norm(k)
    w_hat = w / np.linalg.norm(w)
    e_p = (k_hat + w_hat) / np.sqrt(2)
    e_m = (k_hat - w_hat) / np.sqrt(2)
    print(f"  Predicted eigenvectors:")
    print(f"    λ=0:    v = {v}")
    print(f"    λ=+1/2: (k̂-ŵ)/√2 = {e_m} → S·e = {S @ e_m}")
    print(f"    λ=-1/2: (k̂+ŵ)/√2 = {e_p} → S·e = {S @ e_p}")

def verify_corollaries(n_tests=10000):
    """Verify all corollaries."""
    print("\nVERIFYING COROLLARIES")
    print("=" * 60)

    max_C1 = 0  # ||S||_op
    max_C2 = 0  # |S_j v_k|
    max_C3 = 0  # |S_j v_j|
    max_C4 = 0  # |v_j · S_j v_k|

    for _ in range(n_tests):
        k = np.random.randint(-3, 4, 3).astype(float)
        if k @ k < 0.5: continue
        e1, e2 = build_perp_basis(k)
        t1 = np.random.uniform(0, 2*np.pi)
        vj = np.cos(t1)*e1 + np.sin(t1)*e2
        wj = np.cross(k, vj)
        k2 = k @ k
        S = -(np.outer(wj, k) + np.outer(k, wj)) / (2 * k2)

        # C1: operator norm
        op_norm = np.linalg.norm(S, ord=2)
        max_C1 = max(max_C1, abs(op_norm - 0.5))

        # C2, C3, C4: random v_k
        k2r = np.random.randint(-3, 4, 3).astype(float)
        if k2r @ k2r < 0.5: continue
        e12, e22 = build_perp_basis(k2r)
        t2 = np.random.uniform(0, 2*np.pi)
        vk = np.cos(t2)*e12 + np.sin(t2)*e22

        Svk = S @ vk
        max_C2 = max(max_C2, np.linalg.norm(Svk))
        Svj = S @ vj
        max_C3 = max(max_C3, np.linalg.norm(Svj))
        max_C4 = max(max_C4, abs(vj @ Svk))

    print(f"  C1: ||S_k||_op = 0.5 ± {max_C1:.2e}")
    print(f"  C2: max |S_j v_k| = {max_C2:.6f} ≤ 0.5 {'✓' if max_C2 <= 0.5 + 1e-10 else '✗'}")
    print(f"  C3: max |S_j v_j| = {max_C3:.2e} ≈ 0 {'✓' if max_C3 < 1e-10 else '✗'}")
    print(f"  C4: max |v_j · S_j v_k| = {max_C4:.2e} ≈ 0 {'✓' if max_C4 < 1e-10 else '✗'}")

def summarize():
    print("\n" + "=" * 60)
    print("COMPLETE EIGENSTRUCTURE OF SINGLE-MODE STRAIN")
    print("=" * 60)
    print("""
For div-free mode (k, v), |v|=1, v⊥k, the strain S_k is:

  S_k = -(k⊗w + w⊗k)/(2|k|²),   w = k×v

  Eigenvalues:  {-1/2, 0, +1/2}
  Eigenvectors: {(k̂+ŵ)/√2, v, (k̂-ŵ)/√2}

This matrix is completely determined: it stretches along (k̂-ŵ)/√2
at rate +1/2, compresses along (k̂+ŵ)/√2 at rate -1/2, and has
zero strain along v (the vorticity direction).

PROOF CHAIN FOR KEY LEMMA:
  S_k v_k = 0  →  Sω = Σ_{j≠k} c_j c_k S_j v_k  (cross-terms only)
  ||S_k||_op = 1/2  →  each |S_j v_k| ≤ 1/2
  S_k^T = S_k  →  v_j · S_j v_k = 0  (⊥ own polarization)

  Sω = Σ_j c_j F_j where F_j ⊥ v_j
  ω = Σ_j c_j v_j

  The strain contribution of mode j is PERPENDICULAR to mode j's
  vorticity. This is the depletion of nonlinearity: the mode that
  CREATES the strain cannot BENEFIT from it.

  DATA: |F_j| ~ √N (not N), S²ê/|ω|² ~ 0.05 (not growing).
  REMAINING GAP: prove the coherence bound analytically.
""")

if __name__ == '__main__':
    verify_eigenstructure()
    verify_corollaries()
    summarize()
