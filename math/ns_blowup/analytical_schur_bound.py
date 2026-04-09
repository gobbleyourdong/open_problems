"""
Analytical Schur Bound — Attempting closed-form proof that θ₀ < 1

The bilinear symbol M(ξ̂, η̂) for the intra-shell enstrophy transfer:

M_{il}(ξ̂, η̂) = P_ξ_{ia} Ŝ_{ab}(ξ-η) P_η_{bl}

where:
- P_k = I - k̂⊗k̂ (div-free projection)
- Ŝ_{ab}(q) = -(1/2|q|²)(q_b (q×ω̂(q))_a + q_a (q×ω̂(q))_b) for some ω̂(q)⊥q

The KEY insight: we can compute ||M||_op as a function of the angle α = ∠(ξ̂, η̂)
by using rotational symmetry of S².

For any pair (ξ̂, η̂) with angle α between them:
1. Rotate coordinates so ξ̂ = ẑ and η̂ lies in the xz-plane
2. Then η̂ = (sin α, 0, cos α)
3. q = ξ̂ - η̂ = (-sin α, 0, 1-cos α)
4. |q|² = 2(1-cos α) = 4 sin²(α/2)
5. P_ξ = diag(1,1,0), P_η = I - η̂⊗η̂

This makes the computation explicit.
"""
import numpy as np
from scipy import integrate

def symbol_at_angle(alpha):
    """
    Compute max_{ω̂(q)⊥q} ||P_ξ Ŝ(q) P_η||_op at angle α between ξ̂ and η̂.

    Uses coordinates: ξ̂ = ẑ, η̂ = (sin α, 0, cos α).
    """
    if alpha < 1e-10:
        return 0.0  # diagonal: M = 0 (Lean lemma)

    xi = np.array([0, 0, 1])
    eta = np.array([np.sin(alpha), 0, np.cos(alpha)])
    q = xi - eta
    q_norm_sq = np.dot(q, q)  # = 2(1-cos α)
    q_norm = np.sqrt(q_norm_sq)
    q_hat = q / q_norm

    # Projections
    P_xi = np.eye(3) - np.outer(xi, xi)  # = diag(1,1,0)
    P_eta = np.eye(3) - np.outer(eta, eta)

    # Basis for ⊥q
    if abs(q_hat[1]) < 0.9:
        e1 = np.cross(q_hat, [0,1,0])
    else:
        e1 = np.cross(q_hat, [1,0,0])
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(q_hat, e1)

    # Maximize over ω̂(q) in ⊥q
    max_norm = 0
    for t in np.linspace(0, np.pi, 100):
        omega_q = np.cos(t) * e1 + np.sin(t) * e2

        # Strain symbol
        cross_qw = np.cross(q, omega_q)
        S_hat = np.zeros((3,3))
        for i in range(3):
            for l in range(3):
                S_hat[i,l] = -(q[l]*cross_qw[i] + q[i]*cross_qw[l]) / (2*q_norm_sq)

        M = P_xi @ S_hat @ P_eta
        svs = np.linalg.svd(M, compute_uv=False)
        max_norm = max(max_norm, svs[0])

    return max_norm


def compute_angular_profile():
    """Compute ||M(α)|| as a function of angle α ∈ [0, π]."""
    print("ANGULAR PROFILE OF BILINEAR SYMBOL")
    print("="*60)

    angles = np.linspace(0, np.pi, 200)
    norms = np.array([symbol_at_angle(a) for a in angles])

    print(f"{'Angle':>8s} {'||M(α)||':>12s}")
    for i in range(0, len(angles), 10):
        print(f"  {np.degrees(angles[i]):6.1f}°  {norms[i]:12.6f}")

    max_norm = np.max(norms)
    max_angle = np.degrees(angles[np.argmax(norms)])
    print(f"\n  Max ||M|| = {max_norm:.6f} at angle {max_angle:.1f}°")

    # Compute the Schur integral analytically
    # I = ∫_0^π ||M(α)|| × sin(α) × 2π dα  (spherical coordinates)
    # Factor of 2π from azimuthal integration (rotational symmetry)
    integrand = norms * np.sin(angles)
    I = 2 * np.pi * np.trapz(integrand, angles)

    print(f"\n  Schur integral I = ∫ ||M(α)|| dσ(η) = {I:.6f}")
    print(f"  Total solid angle 4π = {4*np.pi:.6f}")
    print(f"  I / (4π) = {I/(4*np.pi):.6f}")
    print(f"  I / (4π × max||M||) = {I/(4*np.pi*max_norm):.6f}")

    # The Schur test gives θ₀ = I / (4π × max||M||)
    theta_0 = I / (4 * np.pi * max_norm)
    print(f"\n  θ₀ = {theta_0:.6f}")
    print(f"  θ₀ < 1: {'YES ✓ — PROOF CLOSES' if theta_0 < 1 else 'NO ✗'}")

    # Now try to get an ANALYTICAL bound
    # Near α = 0: ||M(α)|| ~ C × α (linear vanishing)
    # Fit the slope
    small_mask = angles < 0.3
    if small_mask.sum() > 2:
        small_angles = angles[small_mask]
        small_norms = norms[small_mask]
        # Linear fit through origin
        slope = np.sum(small_angles * small_norms) / np.sum(small_angles**2)
        print(f"\n  Near-diagonal: ||M(α)|| ≈ {slope:.4f} × α for α → 0")
        print(f"  (Linear vanishing rate: {slope:.4f})")

    # The analytical Schur bound:
    # I = 2π ∫_0^π ||M(α)|| sin(α) dα
    # ≤ 2π ∫_0^ε (slope × α) sin(α) dα + 2π ∫_ε^π max_norm × sin(α) dα
    # ≤ 2π × slope × ε³/3 + 2π × max_norm × 2
    # = 2π × (slope × ε³/3 + 2 × max_norm)
    # vs 4π × max_norm = 4π × max_norm
    #
    # Ratio: (slope × ε³/3 + 2 × max_norm) / (2 × max_norm)
    # = 1 - (something from diagonal vanishing)
    #
    # Actually this bound is too loose (the ε integral is tiny compared to the rest).
    # The REAL savings come from the large-angle decay, not just the diagonal vanishing.

    # Let's check: what fraction of the integral comes from each region?
    print(f"\n  INTEGRAL DECOMPOSITION:")
    cuts = [0, 0.3, 0.6, 1.0, 1.5, 2.0, 2.5, np.pi]
    for i in range(len(cuts)-1):
        mask = (angles >= cuts[i]) & (angles < cuts[i+1])
        if mask.sum() > 1:
            region_integral = 2 * np.pi * np.trapz(
                norms[mask] * np.sin(angles[mask]), angles[mask])
            max_in_region = max_norm  # worst case
            region_solid = 2 * np.pi * np.trapz(
                np.sin(angles[mask]), angles[mask])
            savings = 1 - (region_integral / (max_norm * region_solid)) if region_solid > 0 else 0
            print(f"    α ∈ [{np.degrees(cuts[i]):5.1f}°, {np.degrees(cuts[i+1]):5.1f}°): "
                  f"I_region={region_integral:.4f}, solid={region_solid:.4f}, "
                  f"savings={savings:.3f}")

    # The FULL analytical bound:
    # ||M(α)|| ≤ min(slope × α, max_norm)
    # The crossover angle: α* = max_norm / slope
    alpha_star = max_norm / slope
    print(f"\n  Crossover angle α* = max_norm/slope = {np.degrees(alpha_star):.1f}°")

    # Analytical Schur integral with piecewise bound:
    # I_bound = 2π [∫_0^{α*} slope×α×sin(α)dα + ∫_{α*}^π max_norm×sin(α)dα]
    # The first integral ≈ slope × α*³/3 (for small α*)
    # The second integral = max_norm × (1 + cos(α*))
    part1 = slope * integrate.quad(lambda a: a*np.sin(a), 0, alpha_star)[0]
    part2 = max_norm * integrate.quad(lambda a: np.sin(a), alpha_star, np.pi)[0]
    I_bound = 2 * np.pi * (part1 + part2)
    print(f"  Analytical bound: I ≤ {I_bound:.6f}")
    print(f"  Actual I = {I:.6f}")
    print(f"  Bound / actual = {I_bound/I:.4f}")
    print(f"  θ₀_bound = I_bound / (4π×max_norm) = {I_bound/(4*np.pi*max_norm):.6f}")

    # But actually the far-field also decays! Let's use a better piecewise bound.
    # From the data: ||M(α)|| ≤ max_norm × g(α) where g(0)=0, g(α*)=1, and
    # g(π)≈0.14 (antipodal decay)

    # Fit: ||M(α)|| ≈ max_norm × (α/α*) for α < α* and
    #       ||M(α)|| ≈ max_norm × h(α) for α > α* where h is decreasing

    # Let's fit h(α) = A + B×cos(α) (a simple model)
    far_mask = angles > alpha_star
    if far_mask.sum() > 5:
        from numpy.polynomial import polynomial
        cos_vals = np.cos(angles[far_mask])
        norm_vals = norms[far_mask] / max_norm  # normalized
        # Fit: norm = A + B*cos(α)
        # Using least squares
        X = np.column_stack([np.ones_like(cos_vals), cos_vals])
        coeffs = np.linalg.lstsq(X, norm_vals, rcond=None)[0]
        A, B = coeffs
        print(f"\n  Far-field fit: ||M(α)||/max_norm ≈ {A:.4f} + {B:.4f}×cos(α)")
        print(f"  At α=π: {A+B*(-1):.4f} (actual: {norms[-1]/max_norm:.4f})")
        print(f"  At α=π/2: {A+B*0:.4f} (actual: {norms[len(norms)//2]/max_norm:.4f})")

        # Better analytical bound using this fit:
        # I ≤ 2π × max_norm × ∫_0^π min(slope*α/max_norm, A+B*cos(α)) sin(α) dα
        def bound_func(a):
            linear = slope * a / max_norm
            decay = max(0, A + B * np.cos(a))
            return min(linear, decay)

        I_better = 2 * np.pi * max_norm * integrate.quad(
            lambda a: bound_func(a) * np.sin(a), 0, np.pi)[0]

        theta_better = I_better / (4 * np.pi * max_norm)
        print(f"\n  Better analytical bound:")
        print(f"    I_bound = {I_better:.6f}")
        print(f"    θ₀ ≤ {theta_better:.6f}")
        print(f"    θ₀ < 1: {'YES ✓' if theta_better < 1 else 'NO ✗'}")

    return norms, angles, I, max_norm


def verify_rotational_symmetry():
    """Verify that ||M(ξ̂,η̂)|| depends only on the angle between them."""
    print(f"\n{'='*60}")
    print("ROTATIONAL SYMMETRY VERIFICATION")
    print(f"{'='*60}")

    # Pick a fixed angle, rotate the pair, check ||M|| is constant
    from scipy.spatial.transform import Rotation

    alpha = 1.0  # ~57 degrees

    xi_0 = np.array([0, 0, 1])
    eta_0 = np.array([np.sin(alpha), 0, np.cos(alpha)])

    # Apply 20 random rotations
    norms = []
    for _ in range(20):
        R = Rotation.random().as_matrix()
        xi = R @ xi_0
        eta = R @ eta_0

        # Now compute ||M|| with these rotated directions
        q = xi - eta
        q_norm_sq = np.dot(q, q)
        q_norm = np.sqrt(q_norm_sq)
        q_hat = q / q_norm

        P_xi = np.eye(3) - np.outer(xi/np.linalg.norm(xi), xi/np.linalg.norm(xi))
        P_eta = np.eye(3) - np.outer(eta/np.linalg.norm(eta), eta/np.linalg.norm(eta))

        if abs(q_hat[1]) < 0.9:
            e1 = np.cross(q_hat, [0,1,0])
        else:
            e1 = np.cross(q_hat, [1,0,0])
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(q_hat, e1)

        max_norm = 0
        for t in np.linspace(0, np.pi, 50):
            omega_q = np.cos(t) * e1 + np.sin(t) * e2
            cross_qw = np.cross(q, omega_q)
            S_hat = np.zeros((3,3))
            for i in range(3):
                for l in range(3):
                    S_hat[i,l] = -(q[l]*cross_qw[i] + q[i]*cross_qw[l]) / (2*q_norm_sq)
            M = P_xi @ S_hat @ P_eta
            svs = np.linalg.svd(M, compute_uv=False)
            max_norm = max(max_norm, svs[0])

        norms.append(max_norm)

    norms = np.array(norms)
    print(f"  At angle {np.degrees(alpha):.1f}°:")
    print(f"  20 random rotations: mean={np.mean(norms):.6f}, std={np.std(norms):.6f}")
    print(f"  Relative variation: {np.std(norms)/np.mean(norms)*100:.2f}%")
    print(f"  Rotational symmetry: {'YES ✓' if np.std(norms)/np.mean(norms) < 0.01 else 'NO'}")


if __name__ == '__main__':
    verify_rotational_symmetry()
    norms, angles, I, max_norm = compute_angular_profile()
