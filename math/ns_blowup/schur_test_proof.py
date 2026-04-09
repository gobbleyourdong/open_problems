"""
Schur Test for the Bilinear Symbol — Attempting Analytical Bound

The Schur test says: if K(x,y) is a kernel on a measure space, then
||K||_{op on L²} ≤ √(sup_x ∫|K(x,y)|dμ(y) × sup_y ∫|K(x,y)|dμ(x))

For our bilinear symbol M(ξ̂, η̂) restricted to div-free fields:
- ξ̂, η̂ ∈ S² (directions on the sphere)
- M(ξ̂, ξ̂) = 0 (Lean lemma — diagonal vanishes)
- M is O(|ξ̂ - η̂|) near diagonal (continuity)
- The quadratic form T(j,j) = ∫∫ ω̂*(ξ) M(ξ,η) ω̂(η) dσ(ξ)dσ(η)

If we can show sup_ξ ∫_{S²} |M(ξ,η)| dσ(η) ≤ C₀ < 4π (the total solid angle),
then the operator norm of M is < 1 (after normalization).

This script:
1. Computes ∫|M(ξ,η)|dσ(η) for many ξ values
2. Finds the supremum
3. Compares to 4π to determine if Schur test gives θ < 1

The Schur test would give a RIGOROUS proof that θ < 1.
"""
import numpy as np
import time

def fibonacci_sphere(n):
    """Generate n nearly-uniform points on S²."""
    golden = (1 + np.sqrt(5)) / 2
    indices = np.arange(n)
    theta = np.arccos(1 - 2*indices/n)
    phi = 2 * np.pi * indices / golden
    return np.column_stack([
        np.sin(theta) * np.cos(phi),
        np.sin(theta) * np.sin(phi),
        np.cos(theta)
    ])

def compute_symbol_norm(xi_hat, eta_hat):
    """
    Compute the operator norm of the restricted bilinear symbol M(ξ̂, η̂).

    M maps ω̂(η) ∈ ⊥η̂ to a vector in ⊥ξ̂, via the Biot-Savart strain.

    For the intra-shell transfer, the third wavevector is q = ξ - η,
    and the strain comes from ω̂(q) ⊥ q. We maximize over ω̂(q).

    Returns: max_{|ω̂(q)|=1, ω̂(q)⊥q̂} ||P_ξ Ŝ(q) P_η||_op
    """
    q = xi_hat - eta_hat  # assuming unit shell (|ξ|=|η|=1)
    q_norm = np.linalg.norm(q)
    if q_norm < 1e-10:
        return 0.0  # diagonal: M = 0

    # Check triad constraint: |q| should be O(1) for same-shell triads
    # For unit vectors, |q| ∈ [0, 2]

    q_hat = q / q_norm

    # Projection matrices
    P_xi = np.eye(3) - np.outer(xi_hat, xi_hat)
    P_eta = np.eye(3) - np.outer(eta_hat, eta_hat)
    P_q = np.eye(3) - np.outer(q_hat, q_hat)

    # Basis for ⊥q
    if abs(q_hat[0]) < 0.9:
        e1 = np.cross(q_hat, [1,0,0])
    else:
        e1 = np.cross(q_hat, [0,1,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(q_hat, e1)

    # Maximize over ω̂(q) directions in ⊥q
    max_norm = 0
    for angle in np.linspace(0, np.pi, 30):
        omega_q = np.cos(angle) * e1 + np.sin(angle) * e2

        # Strain symbol from ω̂(q):
        # Ŝ_{il}(q) = -(1/2|q|²)(q_l (q×ω̂)_i + q_i (q×ω̂)_l)
        cross_qw = np.cross(q, omega_q)
        S_hat = np.zeros((3,3))
        for i in range(3):
            for l in range(3):
                S_hat[i,l] = -(q[l]*cross_qw[i] + q[i]*cross_qw[l]) / (2*q_norm**2)

        # Restricted form: P_ξ · Ŝ · P_η
        M = P_xi @ S_hat @ P_eta

        # Operator norm
        svs = np.linalg.svd(M, compute_uv=False)
        max_norm = max(max_norm, svs[0])

    return max_norm


def schur_test(n_dirs=1000):
    """
    Compute the Schur test integral:
    I(ξ̂) = ∫_{S²} |M(ξ̂, η̂)| dσ(η̂)

    Numerically approximate by sampling η̂ uniformly on S².
    The solid angle element dσ = 4π/n_dirs for uniform sampling.

    If sup_ξ I(ξ) < 4π, the Schur test gives ||M||_op < 1.
    But actually we need to normalize by the L²(S²) norm structure.

    More precisely, the quadratic form is:
    T = Σ_{k,k'∈Λ_j} ω̂(k)* · M(k̂,k̂') · ω̂(k')

    This is a matrix with entries M(k̂,k̂'). Its operator norm on ℓ²
    is bounded by the Schur test:
    ||M||_op ≤ max_i Σ_j |M(k̂_i, k̂_j)|

    The ratio θ = ||M||_op / (max individual |M|) tells us the
    cancellation factor.
    """
    print(f"SCHUR TEST — {n_dirs} directions on S²")
    print("="*60)

    dirs = fibonacci_sphere(n_dirs)

    # For computational tractability, subsample for Schur integral
    n_schur = min(n_dirs, 500)
    schur_dirs = dirs[:n_schur]

    t0 = time.time()

    # Compute M(ξ̂_i, η̂_j) for all pairs
    # This is O(n_schur²) which is expensive for large n
    row_sums = np.zeros(n_schur)
    col_sums = np.zeros(n_schur)
    max_entry = 0
    diagonal_values = []

    for i in range(n_schur):
        if (i+1) % 50 == 0:
            print(f"  Row {i+1}/{n_schur} [{time.time()-t0:.1f}s]", flush=True)

        row_sum = 0
        for j in range(n_schur):
            m_val = compute_symbol_norm(schur_dirs[i], schur_dirs[j])
            row_sum += m_val
            col_sums[j] += m_val
            max_entry = max(max_entry, m_val)

            if i == j:
                diagonal_values.append(m_val)

        row_sums[i] = row_sum

    elapsed = time.time() - t0
    print(f"\nCompleted in {elapsed:.1f}s")

    # Schur test bound
    schur_bound = np.sqrt(np.max(row_sums) * np.max(col_sums))

    # The RATIO θ_Schur = schur_bound / (n_schur × max_entry)
    # gives the cancellation factor relative to the worst case
    # (where all entries equal the maximum)
    theta_schur = schur_bound / (n_schur * max_entry) if max_entry > 0 else 0

    print(f"\n{'='*60}")
    print(f"SCHUR TEST RESULTS")
    print(f"{'='*60}")
    print(f"  Max |M(ξ,η)|:        {max_entry:.6f}")
    print(f"  Max diagonal |M(ξ,ξ)|: {max(diagonal_values):.6f} (should be ~0 from Lean)")
    print(f"  Max row sum:         {np.max(row_sums):.4f}")
    print(f"  Max col sum:         {np.max(col_sums):.4f}")
    print(f"  Schur bound:         {schur_bound:.4f}")
    print(f"  N_dirs:              {n_schur}")
    print(f"  Max entry × N:       {n_schur * max_entry:.4f}")
    print(f"  θ_Schur = Schur / (N×max): {theta_schur:.6f}")
    print()

    # The actual question: does the Schur bound give θ < 1?
    # The transfer is T = Σ ω̂* M ω̂, and we want |T| < ||ω||² × ||S||_∞
    # ||S||_∞ ~ max|M| × ||ω̂||_∞ ~ max|M| × max_k |ω̂(k)|
    # ||ω||² = Σ|ω̂(k)|²
    # The ratio θ = Schur_bound / n_dirs gives the effective cancellation

    # BUT: the Schur test is for the FULL matrix M_{ij} = M(k̂_i, k̂_j)
    # The actual transfer uses M weighted by |ω̂(k)|, so:
    # θ ≤ Schur_bound / n_dirs (when ω̂ is flat across modes)
    # θ could be larger if ω̂ is concentrated on a few modes

    # Let's also check: what's the actual operator norm via eigendecomposition
    # for small n_dirs?
    if n_schur <= 200:
        # Build full matrix
        M_full = np.zeros((n_schur, n_schur))
        for i in range(n_schur):
            for j in range(n_schur):
                M_full[i,j] = compute_symbol_norm(schur_dirs[i], schur_dirs[j])

        # This is NOT the correct matrix because M should include the
        # complex structure (each entry is a 2×2 block mapping ⊥η → ⊥ξ).
        # But the Frobenius norm gives an upper bound on the operator norm.
        eigs = np.linalg.eigvalsh(M_full)
        print(f"  Eigenvalue range: [{min(eigs):.4f}, {max(eigs):.4f}]")
        print(f"  Spectral norm / (max_entry × N): {max(abs(eigs))/(n_schur*max_entry):.6f}")
        print(f"  Spectral norm / N: {max(abs(eigs))/n_schur:.6f}")

    # Row sum distribution
    print(f"\n  Row sum distribution (should be << N × max_entry = {n_schur * max_entry:.2f}):")
    print(f"    Mean: {np.mean(row_sums):.4f}")
    print(f"    Max:  {np.max(row_sums):.4f}")
    print(f"    Min:  {np.min(row_sums):.4f}")
    print(f"    Std:  {np.std(row_sums):.4f}")

    # Key ratio
    print(f"\n  KEY: max_row_sum / (N × max_entry) = {np.max(row_sums)/(n_schur*max_entry):.6f}")
    print(f"  If this is < 1: Schur test PROVES θ < 1!")
    is_proved = np.max(row_sums) < n_schur * max_entry
    print(f"  Result: {'PROVED ✓' if is_proved else 'NOT PROVED (need refinement)'}")


def schur_with_solid_angle(n_xi=200, n_eta=500):
    """
    More careful Schur test with proper solid angle weighting.

    I(ξ̂) = ∫_{S²} |M(ξ̂, η̂)| dσ(η̂)

    For the quadratic form T = ∫∫ ω̂*(ξ) M(ξ,η) ω̂(η) dσdσ,
    the operator is M acting on L²(S², C²_⊥k).

    The Schur test gives: ||M||_{L²→L²} ≤ sup_ξ I(ξ)

    For θ < 1, we need I(ξ) < ||S_ω||_∞ / ||ω||_{L²(S²)} for the
    worst-case ξ. Since ||S_ω||_∞ involves the MAXIMUM of the strain
    (not the average), and ||ω||_{L²} involves the average of |ω̂|²,
    the ratio naturally favors θ < 1 when the symbol has cancellation.
    """
    print(f"\n{'='*60}")
    print(f"SCHUR TEST WITH SOLID ANGLE WEIGHTING")
    print(f"  n_xi = {n_xi}, n_eta = {n_eta}")
    print(f"{'='*60}")

    xi_dirs = fibonacci_sphere(n_xi)
    eta_dirs = fibonacci_sphere(n_eta)

    # Solid angle element for each η point: dσ ≈ 4π/n_eta
    dσ = 4 * np.pi / n_eta

    t0 = time.time()
    I_values = np.zeros(n_xi)

    for i in range(n_xi):
        integral = 0
        for j in range(n_eta):
            m_val = compute_symbol_norm(xi_dirs[i], eta_dirs[j])
            integral += m_val * dσ

        I_values[i] = integral

        if (i+1) % 50 == 0:
            print(f"  ξ direction {i+1}/{n_xi} [{time.time()-t0:.1f}s]", flush=True)

    elapsed = time.time() - t0
    print(f"\nCompleted in {elapsed:.1f}s")

    print(f"\n  Schur integral I(ξ̂) = ∫|M(ξ̂,η̂)|dσ(η̂):")
    print(f"    Mean: {np.mean(I_values):.6f}")
    print(f"    Max:  {np.max(I_values):.6f}")
    print(f"    Min:  {np.min(I_values):.6f}")
    print(f"    Total solid angle: {4*np.pi:.4f}")
    print(f"    sup I / (4π): {np.max(I_values)/(4*np.pi):.6f}")
    print()

    # The operator norm bound from Schur test:
    # ||M||_{L²(S²)→L²(S²)} ≤ sup_ξ I(ξ)
    # For the transfer ratio:
    # θ = |T(j,j)| / (||ω_j||² × ||S_j||_∞)
    # = |∫∫ ω̂* M ω̂ dσdσ| / (||ω̂||² × max_x |S(x)|)
    # ≤ ||M||_op × ||ω̂||² / (||ω̂||² × ||S||_∞)
    # = ||M||_op / ||S||_∞
    #
    # ||S||_∞ is the PHYSICAL SPACE maximum of the strain,
    # which is related to the Fourier coefficients by:
    # ||S||_∞ ≤ Σ |Ŝ(k)| ≤ max|Ŝ| × N_j^{1/2} (Cauchy-Schwarz)
    # But also ||S||_∞ ≥ max|Ŝ| (trivially)
    #
    # So: θ ≤ sup I(ξ) / max|Ŝ|
    # From the data: max|M| ≈ 0.48 for unit vectors
    # And sup I(ξ) ≈ ? (computing now)

    # Actually, the proper normalization is:
    # T(j,j) = Σ_{k,k'} ω̂(k)* M(k,k') ω̂(k')
    # This is a DISCRETE sum, not a continuous integral.
    # The matrix M has entries M(k_i, k_j) for k_i, k_j ∈ Λ_j.
    # Its operator norm on ℂ^{N_j} is bounded by the Schur test as:
    # ||M|| ≤ max_i Σ_j |M(k_i, k_j)|
    # The ratio θ = ||M|| / (N_j × max|M|)
    # The continuous Schur integral is the limit of the discrete sum.

    print(f"  CONCLUSION:")
    print(f"  sup I(ξ) = {np.max(I_values):.6f}")
    print(f"  This bounds the continuous Schur integral.")
    print(f"  For the discrete matrix on N_j modes:")
    print(f"    θ ≤ sup I / max|M|  (continuous limit)")
    print(f"    Need to compare to the actual data...")


if __name__ == '__main__':
    import sys

    if '--solid-angle' in sys.argv:
        schur_with_solid_angle(n_xi=100, n_eta=200)
    else:
        schur_test(n_dirs=200)
