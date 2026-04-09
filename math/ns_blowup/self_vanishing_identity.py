"""
Verify the self-vanishing identity: |S_j · ê|² = (a_j²/4) sin²γ_j
and use it to derive a TIGHT bound on S²ê at the max of |ω|².

The identity says: each mode's strain contribution in the ê direction
is proportional to sin²γ (the misalignment angle).

Combined with the phase mismatch (q_j = sin(k·x) small at the max):
S²ê ≤ (Σ (a_j/2) sin γ_j |q_j|)²

And the critical point: Σ a_j cos γ_j q_j k_j = 0.
"""
import numpy as np
from scipy.optimize import minimize, differential_evolution

def get_K_shell(K2):
    R = int(np.sqrt(K2)) + 1
    vecs = []
    for kx in range(-R, R+1):
        for ky in range(-R, R+1):
            for kz in range(-R, R+1):
                if kx*kx + ky*ky + kz*kz == K2:
                    vecs.append(np.array([kx, ky, kz], dtype=float))
    half = []
    seen = set()
    for v in vecs:
        t = tuple(v.astype(int))
        neg = tuple(-x for x in t)
        if t not in seen and neg not in seen:
            half.append(v)
            seen.add(t)
    return half

def verify_identity(n_trials=5000):
    """Verify |S_j · ê|² = (a_j²/4)(1 - cos²γ_j) for random configs."""
    np.random.seed(42)
    k_vecs = get_K_shell(2) + get_K_shell(3) + get_K_shell(5)
    max_err = 0.0

    for trial in range(n_trials):
        N = np.random.choice([2, 3, 4, 5, 6])
        N = min(N, len(k_vecs))
        idx = np.random.choice(len(k_vecs), N, replace=False)
        ks = [k_vecs[i] for i in idx]

        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= (v @ k) / (k @ k) * k
            v /= np.linalg.norm(v)
            v *= np.random.uniform(0.5, 2.0)
            vs.append(v)

        # Random point x
        x = np.random.uniform(0, 2*np.pi, 3)

        # Compute ω and ê
        omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
        w = np.linalg.norm(omega)
        if w < 1e-10:
            continue
        e = omega / w

        # For each mode j: compute |S_j · ê|² and (a_j²/4) sin²γ_j
        for j, (k, v) in enumerate(zip(ks, vs)):
            a = np.linalg.norm(v)
            v_hat = v / a
            cos_gamma = v_hat @ e
            sin2_gamma = 1 - cos_gamma**2

            # S_j · ê directly
            u_hat = np.cross(k, v) / (k @ k)
            S_j = -0.5 * (np.outer(u_hat, k) + np.outer(k, u_hat))
            Sje = S_j @ e
            Sje2_direct = Sje @ Sje

            # Identity prediction
            Sje2_identity = (a**2 / 4) * sin2_gamma

            err = abs(Sje2_direct - Sje2_identity)
            if err > max_err:
                max_err = err
                if err > 1e-10:
                    print(f"  Large error: trial={trial}, j={j}, err={err:.2e}")

    print(f"Self-vanishing identity verified to {max_err:.2e} over {n_trials} trials")
    return max_err < 1e-8

def bound_S2e_triangle(ks, vs, x):
    """Compute the triangle inequality bound on S²ê:
    S²ê ≤ (Σ (a_j/2) sin γ_j |q_j|)²
    """
    omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
    w = np.linalg.norm(omega)
    if w < 1e-10:
        return 0, 0, 0

    e = omega / w
    total = 0.0
    for k, v in zip(ks, vs):
        a = np.linalg.norm(v)
        cos_gamma = (v / a) @ e
        sin_gamma = np.sqrt(max(0, 1 - cos_gamma**2))
        q = abs(np.sin(k @ x))
        total += (a / 2) * sin_gamma * q

    bound = total ** 2

    # Actual S²ê
    S = np.zeros((3, 3))
    for k, v in zip(ks, vs):
        u_hat = np.cross(k, v) / (k @ k)
        s = np.sin(k @ x)
        S -= 0.5 * (np.outer(u_hat, k) + np.outer(k, u_hat)) * s
    Se = S @ e
    actual = Se @ Se

    return actual, bound, w**2

def search_worst_case():
    """Search for the worst S²ê/|ω|² at the max of |ω|²."""
    np.random.seed(0)
    k_vecs = get_K_shell(2) + get_K_shell(3)
    print(f"\nSearching worst case with {len(k_vecs)} k-vectors...")

    worst = 0.0
    worst_bound = 0.0

    for trial in range(1000):
        N = np.random.choice([3, 4, 5, 6, 7, 8])
        N = min(N, len(k_vecs))
        idx = np.random.choice(len(k_vecs), N, replace=False)
        ks = [k_vecs[i] for i in idx]
        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= (v @ k) / (k @ k) * k
            v /= np.linalg.norm(v)
            v *= np.random.uniform(0.3, 3.0)
            vs.append(v)

        # Find max |ω|²
        res = differential_evolution(
            lambda x: -sum(v * np.cos(k @ x) for k, v in zip(ks, vs)).__matmul__(
                       sum(v * np.cos(k @ x) for k, v in zip(ks, vs))),
            [(0, 2*np.pi)]*3, seed=trial, maxiter=200, tol=1e-12, polish=True)
        x = res.x

        actual, bound, w2 = bound_S2e_triangle(ks, vs, x)
        if w2 < 1e-10:
            continue

        r = actual / w2
        r_bound = bound / w2

        if r > worst:
            worst = r
            worst_bound = r_bound
            print(f"  trial={trial} N={N} actual={r:.6f} bound={r_bound:.6f} "
                  f"ratio(actual/bound)={r/r_bound:.3f}" if r_bound > 0 else f"  trial={trial} actual={r:.6f}")

    print(f"\nWORST S²ê/|ω|²: actual={worst:.6f}, triangle_bound={worst_bound:.6f}")
    print(f"Threshold: 0.750")
    print(f"Actual margin: {(0.75-worst)/0.75*100:.1f}%")
    print(f"Bound margin: {(0.75-worst_bound)/0.75*100:.1f}%")

def analyze_critical_point():
    """Analyze the critical point constraint and its implication for sin values."""
    np.random.seed(42)
    k_vecs = get_K_shell(2)
    print(f"\nCritical point analysis (K²=2, {len(k_vecs)} k-vectors)...")

    n_trials = 500
    for trial in range(n_trials):
        N = min(np.random.choice([4, 5, 6]), len(k_vecs))
        idx = np.random.choice(len(k_vecs), N, replace=False)
        ks = [k_vecs[i] for i in idx]
        vs = []
        for k in ks:
            v = np.random.randn(3)
            v -= (v @ k) / (k @ k) * k
            v /= np.linalg.norm(v)
            v *= np.random.uniform(0.5, 2.0)
            vs.append(v)

        # Find max
        def neg_w2(x):
            w = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
            return -(w @ w)
        res = differential_evolution(neg_w2, [(0,2*np.pi)]*3, seed=trial, maxiter=200, tol=1e-12, polish=True)
        x = res.x

        omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
        w = np.linalg.norm(omega)
        if w < 1e-8:
            continue
        e = omega / w

        # Verify critical point: Σ a_j cos γ_j sin(k_j·x) k_j = 0
        cp = np.zeros(3)
        for k, v in zip(ks, vs):
            a = np.linalg.norm(v)
            cos_gamma = (v/a) @ e
            q = np.sin(k @ x)
            cp += a * cos_gamma * q * k

        cp_residual = np.linalg.norm(cp)
        max_sin = max(abs(np.sin(k @ x)) for k in ks)

        if trial < 10 or max_sin > 0.5:
            # Compute the "strain budget"
            strain_budget = sum(np.linalg.norm(v)/2 * np.sqrt(1-(v/np.linalg.norm(v) @ e)**2) * abs(np.sin(k @ x))
                               for k, v in zip(ks, vs))
            print(f"  trial={trial} N={N} cp_residual={cp_residual:.2e} "
                  f"max_sin={max_sin:.4f} strain_budget/|ω|={strain_budget/w:.4f}")

if __name__ == '__main__':
    print("=== Verifying self-vanishing identity ===")
    ok = verify_identity()

    print("\n=== Searching worst S²ê/|ω|² ===")
    search_worst_case()

    print("\n=== Critical point analysis ===")
    analyze_critical_point()
