"""
JOINT optimization: maximize S²ê/|ω|² over c_k AND d̂_k simultaneously.

At the Lagrange-saturated global max:
  S²ê/|ω|² = |Σ √(c_k(1-c_k)) d̂_k|²
  subject to: Σc_k = 1, c_k ∈ [0,1], d̂_k ⊥ v̂_k, |d̂_k|=1

This is the EXACT worst case (after applying sign-flip + saturation).
No factored bound — direct joint optimization.
"""
import numpy as np
from scipy.optimize import minimize

def S2e_ratio(params, N, v_hats):
    """Negative S²ê/|ω|² for minimization."""
    # params: [c_1...c_{N-1}, θ_1...θ_N] (c_N = 1 - Σc_k, θ = direction angle)
    c = np.zeros(N)
    c[:N-1] = params[:N-1]
    c[N-1] = 1.0 - np.sum(c[:N-1])

    # Check constraints
    if np.any(c < 0) or np.any(c > 1):
        return 0

    thetas = params[N-1:]

    # Build d̂_k directions
    vec = np.zeros(3)
    for k in range(N):
        vh = v_hats[k]
        e1 = np.cross(vh, [1,0,0] if abs(vh[0])<0.9 else [0,1,0])
        e1 /= np.linalg.norm(e1)
        e2 = np.cross(vh, e1)
        dk = np.cos(thetas[k])*e1 + np.sin(thetas[k])*e2

        w = np.sqrt(max(c[k]*(1-c[k]), 0))
        vec += w * dk

    return -np.dot(vec, vec)

def optimize_S2e(v_hats, n_restarts=100):
    """Find the maximum S²ê/|ω|² for given v̂ configuration."""
    N = len(v_hats)
    best = 0

    for _ in range(n_restarts):
        # Random initial c and theta
        c0 = np.random.dirichlet(np.ones(N))[:N-1]
        theta0 = np.random.uniform(0, 2*np.pi, N)
        x0 = np.concatenate([c0, theta0])

        res = minimize(S2e_ratio, x0, args=(N, v_hats),
                      method='Nelder-Mead',
                      options={'maxiter': 5000, 'xatol': 1e-12, 'fatol': 1e-14})
        val = -res.fun
        best = max(best, val)

    return best

np.random.seed(42)

print("JOINT OPTIMIZATION: max S²ê/|ω|² (saturated sign-flip config)")
print("=" * 60)
print("Threshold: 3/4 = 0.750")
print()

for N in [2, 3, 4, 5, 6, 8, 10]:
    worst = 0
    n_trials = 300 if N <= 6 else 100

    for trial in range(n_trials):
        # Random v̂ configuration
        v_hats = [np.random.randn(3) for _ in range(N)]
        v_hats = [v/np.linalg.norm(v) for v in v_hats]

        val = optimize_S2e(v_hats, n_restarts=30 if N <= 6 else 15)
        worst = max(worst, val)

    status = "PASS ✓" if worst < 0.75 else "FAIL ✗"
    print(f"  N={N:2d}: worst S²ê/|ω|² = {worst:.6f}  (threshold 0.75) {status}")

# Deep search for N=5 (the critical case from file 377)
print("\n" + "=" * 60)
print("DEEP SEARCH N=5 (1000 trials × 50 restarts)")
print("=" * 60)

worst = 0
worst_vh = None
for trial in range(1000):
    v_hats = [np.random.randn(3) for _ in range(5)]
    v_hats = [v/np.linalg.norm(v) for v in v_hats]

    val = optimize_S2e(v_hats, n_restarts=50)
    if val > worst:
        worst = val
        worst_vh = [v.copy() for v in v_hats]

    if trial % 200 == 0 and trial > 0:
        print(f"  [{trial}] worst = {worst:.6f}")

print(f"\nN=5 DEEP: worst S²ê/|ω|² = {worst:.6f}")
print(f"  vs 3/4 = 0.750: {'PASS ✓' if worst < 0.75 else 'FAIL ✗'}")

if worst_vh:
    # Verify by computing the optimal c and theta
    val = optimize_S2e(worst_vh, n_restarts=100)
    print(f"  Refined: {val:.6f}")
