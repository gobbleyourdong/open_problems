"""
CORRECTED: Check ALL 8 sign combinations for 3 orthogonal k-vectors.
The global max of |ω| is at one of x ∈ {0,π}³ (8 vertices).
At each vertex: ω = s₁v̂₁ + s₂v̂₂ + s₃v̂₃ with sᵢ ∈ {±1}.
"""
import numpy as np
from scipy.optimize import differential_evolution
from itertools import product

def compute_at_vertex(v1, v2, v3, signs):
    """Compute S²ê/|ω|² at the vertex with given signs."""
    k1 = np.array([1.,0,0]); k2 = np.array([0.,1,0]); k3 = np.array([0.,0,1])
    s1, s2, s3 = signs

    omega = s1*v1 + s2*v2 + s3*v3
    om2 = np.dot(omega, omega)
    if om2 < 1e-14:
        return 0, 0, 0

    om = np.sqrt(om2)
    e = omega / om

    # Strain: each mode k gets factor sₖ (from cos(k·x)=sₖ at vertex)
    S = np.zeros((3,3))
    for k, v, s in [(k1,v1,s1), (k2,v2,s2), (k3,v3,s3)]:
        w = np.cross(k, v)
        gu = s * np.outer(w, k)  # grad_u = s * outer(w,k) since cos(k·x)=s
        S += 0.5 * (gu + gu.T)

    Se = S @ e
    S2e = np.dot(Se, Se)
    alpha = np.dot(e, Se)

    return S2e / om2, alpha / om, om


def find_worst_at_global_max(a1, a2, a3):
    """For given polarization angles, find the GLOBAL max vertex and S²ê there."""
    v1 = np.array([0, np.cos(a1), np.sin(a1)])
    v2 = np.array([np.cos(a2), 0, np.sin(a2)])
    v3 = np.array([np.cos(a3), np.sin(a3), 0])

    # Check all 8 vertices
    best_om = 0
    best_vertex = None
    for signs in product([-1, 1], repeat=3):
        omega = signs[0]*v1 + signs[1]*v2 + signs[2]*v3
        om = np.linalg.norm(omega)
        if om > best_om:
            best_om = om
            best_vertex = signs

    if best_vertex is None or best_om < 0.01:
        return 0, 0, 0

    # Compute S²ê at the global max vertex
    return compute_at_vertex(v1, v2, v3, best_vertex)


def scan_and_optimize():
    """Find worst S²ê/|ω|² at the TRUE global max."""
    print("N=3 EXACT S²ê/|ω|² — CORRECTED (all 8 vertices)")
    print("=" * 60)

    # Phase 1: DE optimization
    print("Differential evolution...", flush=True)
    def neg_ratio(params):
        r, _, _ = find_worst_at_global_max(*params)
        return -r

    bounds = [(0, 2*np.pi)] * 3
    result = differential_evolution(neg_ratio, bounds, maxiter=2000,
                                     tol=1e-14, seed=42, polish=True,
                                     popsize=50)
    best_de = -result.fun
    angles_de = result.x
    r_de, ar_de, om_de = find_worst_at_global_max(*angles_de)
    print(f"  DE: S²ê/|ω|² = {best_de:.10f}, α/|ω| = {ar_de:.6f}, |ω| = {om_de:.4f}")

    # Phase 2: Grid scan for verification
    print("Grid scan (100³)...", flush=True)
    n = 100
    best_grid = 0
    best_grid_angles = None
    for i1 in range(n):
        a1 = 2*np.pi*i1/n
        for i2 in range(n):
            a2 = 2*np.pi*i2/n
            for i3 in range(n):
                a3 = 2*np.pi*i3/n
                r, ar, om = find_worst_at_global_max(a1, a2, a3)
                if r > best_grid:
                    best_grid = r
                    best_grid_angles = (a1, a2, a3)

    r_g, ar_g, om_g = find_worst_at_global_max(*best_grid_angles)
    print(f"  Grid: S²ê/|ω|² = {best_grid:.10f}, α/|ω| = {ar_g:.6f}, |ω| = {om_g:.4f}")

    overall = max(best_de, best_grid)

    # Phase 3: Refine around the best
    print(f"\nRefining around best ({overall:.8f})...", flush=True)
    best_angles = angles_de if best_de >= best_grid else best_grid_angles
    for trial in range(10000):
        perturb = np.random.randn(3) * 0.1
        angles = np.array(best_angles) + perturb
        r, ar, om = find_worst_at_global_max(*angles)
        if r > overall:
            overall = r
            best_angles = tuple(angles)

    r_f, ar_f, om_f = find_worst_at_global_max(*best_angles)
    print(f"  Refined: S²ê/|ω|² = {overall:.10f}, α/|ω| = {ar_f:.6f}, |ω| = {om_f:.4f}")

    # Analyze the worst case
    print(f"\n{'='*60}")
    print(f"WORST S²ê/|ω|² at global max = {overall:.8f}")
    print(f"Barrier threshold: 0.750")

    if overall < 0.75:
        print(f"MARGIN: {0.75-overall:.4f} ({(0.75-overall)/0.75*100:.1f}%) — BARRIER HOLDS")
    else:
        print(f"VIOLATION: {overall-0.75:.4f} — BARRIER FAILS!")

    # Detailed analysis of worst config
    v1 = np.array([0, np.cos(best_angles[0]), np.sin(best_angles[0])])
    v2 = np.array([np.cos(best_angles[1]), 0, np.sin(best_angles[1])])
    v3 = np.array([np.cos(best_angles[2]), np.sin(best_angles[2]), 0])

    best_om_val = 0
    best_signs = None
    for signs in product([-1, 1], repeat=3):
        omega = signs[0]*v1 + signs[1]*v2 + signs[2]*v3
        om = np.linalg.norm(omega)
        if om > best_om_val:
            best_om_val = om
            best_signs = signs
            best_omega = omega.copy()

    e = best_omega / best_om_val
    print(f"\nWorst-case configuration:")
    print(f"  Signs: {best_signs}")
    print(f"  ω = [{best_omega[0]:.6f}, {best_omega[1]:.6f}, {best_omega[2]:.6f}]")
    print(f"  |ω| = {best_om_val:.6f}")
    for i, (v, name) in enumerate([(v1,'v̂₁'), (v2,'v̂₂'), (v3,'v̂₃')]):
        c = (e @ v)**2
        print(f"  {name} = [{v[0]:.4f}, {v[1]:.4f}, {v[2]:.4f}], c = {c:.4f}")

    # Also check: does the ratio CHANGE with unequal amplitudes?
    print("\nAmplitude scan (unequal modes)...", flush=True)
    best_uneq = 0
    for trial in range(5000):
        a1r, a2r, a3r = np.random.uniform(0, 2*np.pi, 3)
        amps = np.exp(np.random.uniform(-1, 1, 3))

        v1t = np.array([0, np.cos(a1r), np.sin(a1r)])
        v2t = np.array([np.cos(a2r), 0, np.sin(a2r)])
        v3t = np.array([np.cos(a3r), np.sin(a3r), 0])

        best_om_t = 0
        best_signs_t = None
        for signs in product([-1, 1], repeat=3):
            omega = signs[0]*amps[0]*v1t + signs[1]*amps[1]*v2t + signs[2]*amps[2]*v3t
            om = np.linalg.norm(omega)
            if om > best_om_t:
                best_om_t = om
                best_signs_t = signs

        if best_om_t < 0.1:
            continue

        s1, s2, s3 = best_signs_t
        omega = s1*amps[0]*v1t + s2*amps[1]*v2t + s3*amps[2]*v3t
        om = np.linalg.norm(omega)
        e_t = omega / om

        S = np.zeros((3,3))
        k1 = np.array([1.,0,0]); k2 = np.array([0.,1,0]); k3 = np.array([0.,0,1])
        for k, v, s, a in [(k1,v1t,s1,amps[0]), (k2,v2t,s2,amps[1]), (k3,v3t,s3,amps[2])]:
            w = np.cross(k, v)
            gu = a * s * np.outer(w, k)
            S += 0.5 * (gu + gu.T)

        Se = S @ e_t
        S2e = np.dot(Se, Se)
        ratio = S2e / om**2

        if ratio > best_uneq:
            best_uneq = ratio

    print(f"  Worst with unequal amps: {best_uneq:.8f}")

    print(f"\n{'='*60}")
    final = max(overall, best_uneq)
    print(f"FINAL WORST S²ê/|ω|² = {final:.8f}")
    if final < 0.75:
        print(f"*** BARRIER HOLDS: margin {0.75-final:.4f} ({(0.75-final)/0.75*100:.1f}%) ***")
    else:
        print(f"*** BARRIER FAILS: violation {final-0.75:.4f} ***")


if __name__ == '__main__':
    scan_and_optimize()
