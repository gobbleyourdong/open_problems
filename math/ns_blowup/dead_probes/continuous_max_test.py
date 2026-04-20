"""
Test whether the global max of |ω|² on T³ is at a lattice point {0,π}³.
If not: compute |S|²/|ω|² at the true max.

Key insight: at lattice points, sin(k·x) = 0 for integer k, so S = 0.
If max is always at lattice → Key Lemma holds trivially.
"""
import numpy as np
from scipy.optimize import differential_evolution
from itertools import product as iproduct
import sys

def get_K_shell(K2):
    """Get all k-vectors on shell |k|²=K2 with integer components."""
    R = int(np.sqrt(K2)) + 1
    vecs = []
    for kx in range(-R, R+1):
        for ky in range(-R, R+1):
            for kz in range(-R, R+1):
                if kx*kx + ky*ky + kz*kz == K2:
                    vecs.append((kx, ky, kz))
    # Take only half (k and -k give same cos contribution)
    half = []
    seen = set()
    for v in vecs:
        neg = tuple(-x for x in v)
        if v not in seen and neg not in seen:
            half.append(np.array(v, dtype=float))
            seen.add(v)
    return half

def random_config(k_vecs, N):
    """Generate N random modes on given k-vectors with div-free polarizations."""
    idx = np.random.choice(len(k_vecs), N, replace=False)
    ks = [k_vecs[i] for i in idx]
    vs = []
    for k in ks:
        # Random v perpendicular to k (div-free: k·v = 0)
        v = np.random.randn(3)
        v -= (v @ k) / (k @ k) * k
        v /= np.linalg.norm(v)
        v *= np.random.uniform(0.5, 2.0)  # random amplitude
        vs.append(v)
    return ks, vs

def omega_squared(x, ks, vs):
    """Compute |ω(x)|² at point x."""
    omega = np.zeros(3)
    for k, v in zip(ks, vs):
        omega += v * np.cos(k @ x)
    return np.sum(omega**2)

def neg_omega_squared(x, ks, vs):
    return -omega_squared(x, ks, vs)

def strain_at(x, ks, vs):
    """Compute strain tensor S(x) = sym(∇u) where u = Biot-Savart(ω)."""
    S = np.zeros((3,3))
    for k, v in zip(ks, vs):
        u_hat = np.cross(k, v) / (k @ k)  # Biot-Savart mode
        # ∇u contribution: -(u_hat ⊗ k) sin(k·x)
        s = np.sin(k @ x)
        S -= 0.5 * (np.outer(u_hat, k) + np.outer(k, u_hat)) * s
    return S

def gradu_at(x, ks, vs):
    """Compute ∇u(x)."""
    G = np.zeros((3,3))
    for k, v in zip(ks, vs):
        u_hat = np.cross(k, v) / (k @ k)
        s = np.sin(k @ x)
        G -= np.outer(u_hat, k) * s
    return G

def compute_S2e(S, omega_vec):
    """Compute S²ê = ê·S²·ê where ê = ω/|ω|."""
    w = np.linalg.norm(omega_vec)
    if w < 1e-12:
        return 0.0
    e = omega_vec / w
    Se = S @ e
    return np.dot(Se, Se)

def lattice_max(ks, vs, L=4):
    """Find max |ω|² over lattice points {m*π/L}³.
    For K=√2 shell (freq ≤ 2): L=4 gives π/4 spacing, 8³=512 points.
    Also separately track points where ALL sin(k·x) = 0."""
    best = 0.0
    best_x = np.zeros(3)
    best_sinzero = 0.0
    best_sinzero_x = np.zeros(3)
    steps = [m * np.pi / L for m in range(2*L)]
    for x1, x2, x3 in iproduct(steps, repeat=3):
        x = np.array([x1, x2, x3])
        val = omega_squared(x, ks, vs)
        if val > best:
            best = val
            best_x = x.copy()
        # Check if all sines vanish
        all_sin_zero = all(abs(np.sin(k @ x)) < 1e-10 for k in ks)
        if all_sin_zero and val > best_sinzero:
            best_sinzero = val
            best_sinzero_x = x.copy()
    return best, best_x, best_sinzero, best_sinzero_x

def continuous_max(ks, vs, n_restarts=20):
    """Find max |ω|² using differential evolution + multi-start."""
    bounds = [(0, 2*np.pi), (0, 2*np.pi), (0, 2*np.pi)]

    result = differential_evolution(
        lambda x: neg_omega_squared(x, ks, vs),
        bounds, seed=42, maxiter=500, tol=1e-12, polish=True
    )
    best_val = -result.fun
    best_x = result.x.copy()

    # Multi-start refinement
    for _ in range(n_restarts):
        x0 = np.random.uniform(0, 2*np.pi, 3)
        from scipy.optimize import minimize
        res = minimize(lambda x: neg_omega_squared(x, ks, vs), x0,
                      method='Nelder-Mead', options={'xatol': 1e-14, 'fatol': 1e-14, 'maxiter': 5000})
        if -res.fun > best_val + 1e-12:
            best_val = -res.fun
            best_x = res.x.copy()

    return best_val, best_x

def is_lattice_point(x, tol=1e-6):
    """Check if x is close to a lattice point {0,π}³ mod 2π."""
    for xi in x:
        xi_mod = xi % (2*np.pi)
        if xi_mod > np.pi:
            xi_mod -= 2*np.pi
        if abs(xi_mod) > tol and abs(abs(xi_mod) - np.pi) > tol:
            return False
    return True

def main():
    np.random.seed(42)
    K2 = 2  # K=√2 shell
    k_vecs = get_K_shell(K2)
    print(f"K² = {K2}, {len(k_vecs)} half-shell vectors")

    n_configs = 500
    n_off_lattice = 0
    worst_S2_ratio = 0.0
    worst_S2e_ratio = 0.0
    worst_gradu_ratio = 0.0
    off_lattice_ratios = []

    n_sin_nonzero_max = 0  # max is at a point where some sin ≠ 0

    for trial in range(n_configs):
        N = min(np.random.choice([3, 4, 5, 6]), len(k_vecs))
        ks, vs = random_config(k_vecs, N)

        grid_val, grid_x, sinzero_val, sinzero_x = lattice_max(ks, vs)
        cont_val, cont_x = continuous_max(ks, vs)

        # The TRUE max (best of grid and continuous)
        if cont_val > grid_val + 1e-12:
            true_val, true_x = cont_val, cont_x
        else:
            true_val, true_x = grid_val, grid_x

        # Gap between true max and sin-zero max
        sinzero_gap = (true_val - sinzero_val) / max(sinzero_val, 1e-15)

        # Check if any sin is non-zero at the true max
        max_sin = max(abs(np.sin(k @ true_x)) for k in ks)

        if max_sin > 1e-6:
            n_sin_nonzero_max += 1
            # Compute ratios at the TRUE max (where S ≠ 0)
            omega_vec = sum(v * np.cos(k @ true_x) for k, v in zip(ks, vs))
            w2 = np.sum(omega_vec**2)
            S = strain_at(true_x, ks, vs)
            S2 = np.sum(S**2)
            S2e = compute_S2e(S, omega_vec)
            G = gradu_at(true_x, ks, vs)
            gradu2 = np.sum(G**2)

            r_S2 = S2 / w2 if w2 > 1e-15 else 0
            r_S2e = S2e / w2 if w2 > 1e-15 else 0
            r_gradu = gradu2 / w2 if w2 > 1e-15 else 0

            off_lattice_ratios.append((N, sinzero_gap, r_S2, r_S2e, r_gradu, max_sin))
            worst_S2_ratio = max(worst_S2_ratio, r_S2)
            worst_S2e_ratio = max(worst_S2e_ratio, r_S2e)
            worst_gradu_ratio = max(worst_gradu_ratio, r_gradu)

            if trial < 30 or r_S2e > 0.3:
                print(f"  Trial {trial}: N={N}, sin_gap={sinzero_gap:.6f}, max_sin={max_sin:.4f}, "
                      f"|S|²/|ω|²={r_S2:.4f}, S²ê/|ω|²={r_S2e:.4f}, |∇u|²/|ω|²={r_gradu:.4f}")

        if (trial+1) % 100 == 0:
            print(f"Progress: {trial+1}/{n_configs}, sin≠0 at max: {n_sin_nonzero_max}")

    n_off_lattice = n_sin_nonzero_max

    print(f"\n{'='*60}")
    print(f"RESULTS: {n_configs} configs, K²={K2}")
    print(f"Off-lattice maxima: {n_off_lattice}/{n_configs} ({100*n_off_lattice/n_configs:.1f}%)")

    if n_off_lattice > 0:
        print(f"\nAt maxima where sin ≠ 0 (S possibly nonzero):")
        print(f"  Worst |S|²/|ω|²  = {worst_S2_ratio:.6f}  (threshold: 9/8 = 1.125)")
        print(f"  Worst S²ê/|ω|²   = {worst_S2e_ratio:.6f}  (threshold: 3/4 = 0.750)")
        print(f"  Worst |∇u|²/|ω|² = {worst_gradu_ratio:.6f} (threshold: 13/8 = 1.625)")

        print(f"\n  Distribution of off-lattice gaps:")
        gaps = [r[1] for r in off_lattice_ratios]
        print(f"    Mean gap:   {np.mean(gaps):.6f}")
        print(f"    Max gap:    {np.max(gaps):.6f}")
        print(f"    Median gap: {np.median(gaps):.6f}")

        max_sins = [r[5] for r in off_lattice_ratios]
        print(f"  Max |sin| at max:")
        print(f"    Mean:   {np.mean(max_sins):.6f}")
        print(f"    Max:    {np.max(max_sins):.6f}")

        violations_S2e = sum(1 for r in off_lattice_ratios if r[3] >= 0.750)
        violations_gradu = sum(1 for r in off_lattice_ratios if r[4] >= 1.625)
        print(f"\n  Key Lemma violations (S²ê/|ω|² ≥ 0.75): {violations_S2e}")
        print(f"  Gradient violations (|∇u|²/|ω|² ≥ 1.625): {violations_gradu}")
    else:
        print("\nALL maxima at sin=0 points! S = 0 at every max.")
        print("KEY LEMMA HOLDS TRIVIALLY for all tested configurations.")

    # Also test K²=3 shell
    print(f"\n{'='*60}")
    print("Testing K²=3 shell...")
    k_vecs_3 = get_K_shell(3)
    print(f"K²=3: {len(k_vecs_3)} half-shell vectors")

    n_off_3 = 0
    worst_3 = 0.0
    for trial in range(200):
        N = min(np.random.choice([3, 4, 5, 6]), len(k_vecs_3))
        ks, vs = random_config(k_vecs_3, N)
        cont_val, cont_x = continuous_max(ks, vs)
        max_sin = max(abs(np.sin(k @ cont_x)) for k in ks)
        if max_sin > 1e-6:
            n_off_3 += 1
            omega_vec = sum(v * np.cos(k @ cont_x) for k, v in zip(ks, vs))
            w2 = np.sum(omega_vec**2)
            S2e = compute_S2e(strain_at(cont_x, ks, vs), omega_vec)
            r = S2e / w2 if w2 > 1e-15 else 0
            worst_3 = max(worst_3, r)

    print(f"K²=3: sin≠0 at max: {n_off_3}/200, worst S²ê/|ω|² = {worst_3:.6f}")

if __name__ == '__main__':
    main()
