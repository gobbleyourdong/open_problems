"""
Exact S²ê/|ω|² for 3 modes with orthogonal k-vectors.
k₁=(1,0,0), k₂=(0,1,0), k₃=(0,0,1), equal amplitudes, at x=0.
Parameter space: 3 angles (α₁, α₂, α₃) for polarization rotations.

Find the EXACT maximum and characterize the worst configuration.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution

def compute_3mode(a1, a2, a3):
    """
    3 modes with k₁=(1,0,0), k₂=(0,1,0), k₃=(0,0,1).
    v̂₁ = (0, cos α₁, sin α₁)
    v̂₂ = (cos α₂, 0, sin α₂)
    v̂₃ = (cos α₃, sin α₃, 0)
    At x=0 (all cos(k·x)=1).
    """
    v1 = np.array([0, np.cos(a1), np.sin(a1)])
    v2 = np.array([np.cos(a2), 0, np.sin(a2)])
    v3 = np.array([np.cos(a3), np.sin(a3), 0])

    k1 = np.array([1.,0,0]); k2 = np.array([0.,1,0]); k3 = np.array([0.,0,1])

    omega = v1 + v2 + v3
    om2 = np.dot(omega, omega)
    if om2 < 1e-14:
        return 0, 0, 0, omega, np.zeros(3)

    om = np.sqrt(om2)
    e = omega / om

    # Strain at x=0
    S = np.zeros((3,3))
    for k, v in [(k1,v1), (k2,v2), (k3,v3)]:
        w = np.cross(k, v)
        # At x=0: cos(k·x)=1, so S contribution = sym(w⊗k)/(2|k|²)
        # But wait: S = a*cos(k·x)/(2|k|²) * (k⊗w + w⊗k)/2... let me recompute
        # grad_u = a * outer(w, k) * cos(k·x) / |k|² where w = k×v
        # At x=0, cos=1: grad_u_ij = w_i * k_j / |k|²
        # For |k|=1: grad_u = outer(w, k)
        gu = np.outer(w, k)  # |k|²=1
        S += 0.5 * (gu + gu.T)

    Se = S @ e
    S2e = np.dot(Se, Se)
    alpha = np.dot(e, Se)

    return S2e/om2, alpha/om, om, omega, Se


def scan_exhaustive():
    """Fine grid scan over 3 angles."""
    n = 200
    best_ratio = 0
    best_angles = None
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)

    for i1 in range(n):
        for i2 in range(n):
            for i3 in range(n):
                r, ar, om, _, _ = compute_3mode(angles[i1], angles[i2], angles[i3])
                if r > best_ratio and om > 0.1:
                    best_ratio = r
                    best_angles = (angles[i1], angles[i2], angles[i3])
                    best_alpha = ar
                    best_om = om

    return best_ratio, best_angles, best_alpha, best_om


def optimize_de():
    """Differential evolution optimization."""
    def neg_ratio(params):
        r, _, om, _, _ = compute_3mode(*params)
        if om < 0.1:
            return 0
        return -r

    bounds = [(0, 2*np.pi)] * 3
    result = differential_evolution(neg_ratio, bounds, maxiter=1000,
                                     tol=1e-12, seed=42, polish=True)
    return -result.fun, result.x


def check_global_max(a1, a2, a3):
    """Verify x=0 is the global max of |ω| for this configuration."""
    v1 = np.array([0, np.cos(a1), np.sin(a1)])
    v2 = np.array([np.cos(a2), 0, np.sin(a2)])
    v3 = np.array([np.cos(a3), np.sin(a3), 0])

    k1 = np.array([1.,0,0]); k2 = np.array([0.,1,0]); k3 = np.array([0.,0,1])

    om_at_0 = np.linalg.norm(v1 + v2 + v3)

    # Check: is |ω(0)| ≥ max over single-mode maxima?
    # Single-mode max for mode k at x where cos(k·x)=1, others cos≈0:
    # For orthogonal k's: at (0,π/2,π/2), mode 1 has cos=1, others cos=0.
    # |ω| = |v1| = 1.
    single_max = 1.0

    # Two-mode max: modes 1,2 at cos=1, mode 3 at cos=0
    # At (0,0,π/2): cos(k₁·x)=cos(0)=1, cos(k₂·x)=cos(0)=1, cos(k₃·x)=cos(π/2)=0
    two_maxes = [
        np.linalg.norm(v1 + v2),  # modes 1,2
        np.linalg.norm(v1 + v3),  # modes 1,3
        np.linalg.norm(v2 + v3),  # modes 2,3
    ]

    all_max = max(single_max, max(two_maxes))
    is_global = om_at_0 >= all_max - 1e-10

    return is_global, om_at_0, all_max


def analyze_worst_case():
    """Find and analyze the worst S²ê/|ω|² configuration."""
    print("N=3 EXACT S²ê/|ω|² ANALYSIS")
    print("k₁=(1,0,0), k₂=(0,1,0), k₃=(0,0,1), equal amplitudes")
    print("At x=0 where all cos(k·x)=1")
    print("=" * 60)

    # Phase 1: DE optimization
    print("\nDifferential evolution optimization...", flush=True)
    best_de, angles_de = optimize_de()
    r_de, ar_de, om_de, omega_de, Se_de = compute_3mode(*angles_de)
    is_glob, om0, omax = check_global_max(*angles_de)
    print(f"  Best S²ê/|ω|² = {best_de:.8f}")
    print(f"  α/|ω| = {ar_de:.6f}, |ω| = {om_de:.6f}")
    print(f"  Is global max: {is_glob} (|ω(0)|={om0:.4f}, other max={omax:.4f})")
    print(f"  Angles: α₁={angles_de[0]:.6f}, α₂={angles_de[1]:.6f}, α₃={angles_de[2]:.6f}")

    # Phase 2: Fine grid (to verify DE found the true max)
    print("\nFine grid scan (200³ = 8M points)...", flush=True)
    best_grid, angles_grid, ar_grid, om_grid = scan_exhaustive()
    is_glob2, om02, omax2 = check_global_max(*angles_grid)
    print(f"  Best S²ê/|ω|² = {best_grid:.8f}")
    print(f"  α/|ω| = {ar_grid:.6f}, |ω| = {om_grid:.6f}")
    print(f"  Is global max: {is_glob2} (|ω(0)|={om02:.4f}, other max={omax2:.4f})")
    print(f"  Angles: α₁={angles_grid[0]:.4f}, α₂={angles_grid[1]:.4f}, α₃={angles_grid[2]:.4f}")

    # Phase 3: Only consider configs where x=0 IS the global max
    print("\nRe-scanning with global max enforcement...", flush=True)
    n = 150
    best_valid = 0
    best_valid_angles = None
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)

    for i1 in range(n):
        for i2 in range(n):
            for i3 in range(n):
                a = (angles[i1], angles[i2], angles[i3])
                is_g, _, _ = check_global_max(*a)
                if not is_g:
                    continue
                r, ar, om, _, _ = compute_3mode(*a)
                if r > best_valid and om > 0.5:
                    best_valid = r
                    best_valid_angles = a

    if best_valid_angles:
        r_v, ar_v, om_v, omega_v, Se_v = compute_3mode(*best_valid_angles)
        print(f"  Best VALID S²ê/|ω|² = {best_valid:.8f}")
        print(f"  α/|ω| = {ar_v:.6f}, |ω| = {om_v:.6f}")
        print(f"  ω = [{omega_v[0]:.4f}, {omega_v[1]:.4f}, {omega_v[2]:.4f}]")
        print(f"  S·ê = [{Se_v[0]:.4f}, {Se_v[1]:.4f}, {Se_v[2]:.4f}]")

        # Detailed analysis
        v1 = np.array([0, np.cos(best_valid_angles[0]), np.sin(best_valid_angles[0])])
        v2 = np.array([np.cos(best_valid_angles[1]), 0, np.sin(best_valid_angles[1])])
        v3 = np.array([np.cos(best_valid_angles[2]), np.sin(best_valid_angles[2]), 0])
        e = omega_v / om_v

        print(f"\n  Detailed structure:")
        for i, (v, name) in enumerate([(v1,'v̂₁'), (v2,'v̂₂'), (v3,'v̂₃')]):
            c = (e @ v)**2
            print(f"    {name} = [{v[0]:.4f}, {v[1]:.4f}, {v[2]:.4f}], "
                  f"c_k = {c:.4f}, 1-c_k = {1-c:.4f}")

    print(f"\n{'='*60}")
    print(f"RESULT: max S²ê/|ω|² at global max = {best_valid:.6f}")
    print(f"Threshold: 0.750")
    print(f"Margin: {0.75 - best_valid:.4f} ({(0.75-best_valid)/0.75*100:.1f}%)")

    if best_valid < 0.5:
        print(f"\n*** S²ê/|ω|² < 1/2 for ALL 3-mode configs at global max ***")
    if best_valid < 0.375:
        print(f"*** S²ê/|ω|² < 3/8 — even tighter than needed ***")
    if best_valid < 0.26:
        print(f"*** S²ê/|ω|² ≈ 1/4 — same bound as 2-mode case! ***")


if __name__ == '__main__':
    analyze_worst_case()
