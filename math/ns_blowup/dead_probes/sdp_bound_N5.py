"""
SDP-style bound for N=5: find the maximum of |Σ r_k d̂_k|² / Σr_k²
subject to d̂_k ⊥ v̂_k (Biot-Savart constraint).

If this ratio (the frame bound constant) is < 3: then
S²ê ≤ 3 × Σ|ŝ_k|² ≤ 3(N-1)|ω|²/(4N) = 3×4/(4×5)|ω|² = 3/5|ω|² < 3/4|ω|².

For N=5: need frame constant C₅ < 3.75 (so 3.75 × 4/(4×5) = 3/4).
Actually: need C × (N-1)/(4N) < 3/4 → C < 3N/(N-1).
For N=5: C < 15/4 = 3.75.

The frame constant C = max eigenvalue of the Gram matrix D^TD
where D has rows d̂_k ∈ R³ with d̂_k ⊥ v̂_k.

Since D is N×3 with rank ≤ 3: eigenvalues λ₁ ≥ λ₂ ≥ λ₃ ≥ 0, λ₁+λ₂+λ₃ = N.

The constraint d̂_k ⊥ v̂_k limits which directions are available.

Maximize λ₁ subject to: v̂_k · d̂_k = 0 for all k.
"""
import numpy as np
from scipy.optimize import minimize

def compute_frame_constant(v_hats, d_hats):
    """Compute the max eigenvalue of the Gram matrix D^T D."""
    D = np.array(d_hats)  # N × 3
    G = D @ D.T  # N × N Gram matrix
    evals = np.linalg.eigvalsh(G)
    return evals[-1]  # λ_max

def optimize_frame_constant(v_hats, n_restarts=50):
    """For fixed v̂_k: find d̂_k ⊥ v̂_k that MAXIMIZES the frame constant λ₁."""
    N = len(v_hats)

    best_lmax = 0
    for _ in range(n_restarts):
        # Random initial angles
        angles = np.random.uniform(0, 2*np.pi, N)

        def neg_lmax(angles):
            d_hats = []
            for i, (vh, theta) in enumerate(zip(v_hats, angles)):
                # d̂ perpendicular to v̂, in the 2D plane ⊥ v̂
                e1 = np.cross(vh, [1,0,0] if abs(vh[0])<0.9 else [0,1,0])
                e1 /= np.linalg.norm(e1)
                e2 = np.cross(vh, e1)
                d_hats.append(np.cos(theta)*e1 + np.sin(theta)*e2)
            D = np.array(d_hats)
            evals = np.linalg.eigvalsh(D @ D.T)
            return -evals[-1]

        res = minimize(neg_lmax, angles, method='Nelder-Mead',
                      options={'maxiter': 3000, 'xatol': 1e-10})
        lmax = -res.fun
        best_lmax = max(best_lmax, lmax)

    return best_lmax

np.random.seed(42)

print("=" * 60)
print("FRAME CONSTANT (λ_max of Gram matrix) WITH ⊥ CONSTRAINT")
print("=" * 60)

# Test 1: worst-case v̂ configurations for N=5
print("\nN=5: Sweeping over random v̂ configurations")
print("Need: λ_max < 3.75 (for S²ê ≤ 3/4 × |ω|²)")

worst_lmax = 0
for trial in range(500):
    # Random v̂ vectors (unit, any direction)
    v_hats = [np.random.randn(3) for _ in range(5)]
    v_hats = [v/np.linalg.norm(v) for v in v_hats]

    lmax = optimize_frame_constant(v_hats, n_restarts=20)
    worst_lmax = max(worst_lmax, lmax)

    if trial % 100 == 0:
        print(f"  [{trial}] worst λ_max = {worst_lmax:.4f} (threshold 3.75)")

print(f"\nN=5 worst λ_max = {worst_lmax:.4f}")
print(f"  < 3.75? {'YES ✓' if worst_lmax < 3.75 else 'NO ✗'}")
print(f"  Implied S²ê/|ω|² ≤ {worst_lmax * 4/(4*5):.4f} (threshold 0.75)")

# Test 2: specific v̂ configs
print("\n" + "=" * 60)
print("SPECIFIC CONFIGURATIONS")
print("=" * 60)

configs = {
    "all_parallel": [np.array([0,0,1.])]*5,
    "planar_uniform": [np.array([np.cos(2*np.pi*i/5), np.sin(2*np.pi*i/5), 0]) for i in range(5)],
    "hemisphere_caps": [np.array([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)])
                        for t,p in [(0.5,0),(0.5,1.2),(0.5,2.4),(0.5,3.6),(0.5,4.8)]],
    "one_along_e": [np.array([0,0,1.]), np.array([1,0,0.]), np.array([0,1,0.]),
                    np.array([1,1,0.])/np.sqrt(2), np.array([1,0,1.])/np.sqrt(2)],
}

for name, vs in configs.items():
    lmax = optimize_frame_constant(vs, n_restarts=30)
    bound = lmax * 4/(4*5)
    print(f"  {name:20s}: λ_max = {lmax:.4f}, S²ê bound = {bound:.4f} {'✓' if bound < 0.75 else '✗'}")

# Test for N=5 through N=20: does λ_max stay below threshold?
print("\n" + "=" * 60)
print("SCALING: worst λ_max vs threshold 3N/(N-1)")
print("=" * 60)

for N in [5, 6, 8, 10, 15, 20]:
    threshold = 3*N/(N-1)
    worst = 0
    for trial in range(200):
        vs = [np.random.randn(3) for _ in range(N)]
        vs = [v/np.linalg.norm(v) for v in vs]
        lmax = optimize_frame_constant(vs, n_restarts=10)
        worst = max(worst, lmax)
    bound = worst*(N-1)/(4*N)
    print(f"  N={N:2d}: worst λ_max = {worst:.4f}, threshold = {threshold:.4f}, "
          f"{'PASS ✓' if worst < threshold else 'FAIL ✗'}, S²ê bound = {bound:.4f}")
