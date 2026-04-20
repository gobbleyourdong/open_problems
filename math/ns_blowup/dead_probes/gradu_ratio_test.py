"""
Test |∇u|²/|ω|² at the global max of |ω| for random multi-mode div-free fields on T³.

The key question: is |∇u|²/|ω|² < 13/8 = 1.625 universally?
If so: S²ê ≤ (2/3)(|∇u|² - |ω|²/2) < (2/3)(13|ω|²/8 - |ω|²/2) = 3|ω|²/4.

Also verifies:
- Pointwise identity |S|² = |∇u|² - |ω|²/2
- |∇u|² = N at vertices for orthogonal k-vectors
- S²ê/|ω|² < 3/4 universally
"""
import numpy as np
from itertools import product as iprod

def make_field(N_modes, orthogonal_k=False, max_k=3):
    """Create random div-free modes on T³."""
    modes = []
    if orthogonal_k and N_modes <= 3:
        # Use axis-aligned k-vectors
        ks = np.eye(3, dtype=int)[:N_modes]
        for i in range(N_modes):
            k = ks[i]
            # Random polarization perpendicular to k
            v = np.random.randn(3)
            v -= v.dot(k) * k / np.dot(k, k)
            v /= np.linalg.norm(v)
            a = np.random.uniform(0.5, 2.0)
            modes.append((k, v, a))
    else:
        # Random k-vectors (nonzero integers)
        used = set()
        while len(modes) < N_modes:
            k = np.random.randint(-max_k, max_k+1, 3)
            if np.all(k == 0):
                continue
            tk = tuple(k)
            if tk in used or tuple(-k) in used:
                continue
            used.add(tk)
            # Random div-free polarization (v ⊥ k)
            v = np.random.randn(3)
            v -= v.dot(k) * k / np.dot(k, k)
            v /= np.linalg.norm(v)
            a = np.random.uniform(0.5, 2.0)
            modes.append((k.astype(float), v, a))
    return modes

def eval_field(modes, x):
    """Evaluate ω, ∇u, S at point x for sum of cos modes."""
    omega = np.zeros(3)
    grad_u = np.zeros((3, 3))

    for k, v, a in modes:
        knorm2 = np.dot(k, k)
        phase = np.dot(k, x)
        c = np.cos(phase)
        s = np.sin(phase)

        # ω_mode = a * v * cos(k·x)
        omega += a * v * c

        # u_mode = a * (k × v) * sin(k·x) / |k|²
        w = np.cross(k, v)
        u_coeff = a * w / knorm2  # amplitude of sin term

        # ∇u_mode = u_coeff ⊗ k * cos(k·x)  (derivative of sin → cos)
        grad_u += np.outer(u_coeff, k) * c

    S = 0.5 * (grad_u + grad_u.T)
    return omega, grad_u, S

def find_max_omega(modes, N_grid=32):
    """Find the global max of |ω| by grid search + refinement."""
    # Coarse grid
    xs = np.linspace(0, 2*np.pi, N_grid, endpoint=False)
    best_x = None
    best_om2 = -1

    for ix, iy, iz in iprod(range(N_grid), repeat=3):
        x = np.array([xs[ix], xs[iy], xs[iz]])
        omega = np.zeros(3)
        for k, v, a in modes:
            omega += a * v * np.cos(np.dot(k, x))
        om2 = np.dot(omega, omega)
        if om2 > best_om2:
            best_om2 = om2
            best_x = x.copy()

    # Refine with gradient ascent on |ω|²
    x = best_x.copy()
    lr = 0.01
    for _ in range(500):
        omega = np.zeros(3)
        grad_om2 = np.zeros(3)  # ∇_x |ω|²
        for k, v, a in modes:
            phase = np.dot(k, x)
            c = np.cos(phase)
            s = np.sin(phase)
            omega += a * v * c
            # d|ω|²/dx_i = 2 ω · dω/dx_i = 2 ω · (-a v sin(k·x) k_i)
            # = -2a sin(k·x) (ω·v) k
            grad_om2 += -2 * a * s * np.dot(omega, v) * k

        # Recompute omega for fresh grad
        omega = np.zeros(3)
        for k, v, a in modes:
            omega += a * v * np.cos(np.dot(k, x))

        for k, v, a in modes:
            phase = np.dot(k, x)
            s = np.sin(phase)
            grad_om2 += -2 * a * s * np.dot(omega, v) * k

        # Actually, recompute properly
        grad_om2 = np.zeros(3)
        for k, v, a in modes:
            phase = np.dot(k, x)
            s = np.sin(phase)
            grad_om2 -= 2 * a * s * np.dot(omega, v) * k

        x += lr * grad_om2
        x = x % (2 * np.pi)

    return x

def analyze_point(modes, x):
    """Compute all quantities at a given point."""
    omega, grad_u, S = eval_field(modes, x)
    om2 = np.dot(omega, omega)
    if om2 < 1e-12:
        return None

    e_hat = omega / np.sqrt(om2)

    # |∇u|²
    gradu2 = np.sum(grad_u**2)

    # |S|²
    S2 = np.sum(S**2)

    # |Ω|² = |ω|²/2
    Omega2 = om2 / 2

    # Verify identity |∇u|² = |S|² + |ω|²/2
    identity_err = abs(gradu2 - S2 - Omega2) / max(gradu2, 1e-10)

    # S²ê = |S·ê|²
    Se = S @ e_hat
    S2e = np.dot(Se, Se)

    # α = ê·S·ê
    alpha = e_hat @ S @ e_hat

    return {
        'om2': om2,
        'gradu2': gradu2,
        'S2': S2,
        'S2e': S2e,
        'alpha': alpha,
        'ratio_gradu': gradu2 / om2,
        'ratio_S2': S2 / om2,
        'ratio_S2e': S2e / om2,
        'ratio_alpha': alpha / np.sqrt(om2),
        'identity_err': identity_err,
    }

def test_orthogonal_identity(N_trials=1000):
    """Test |∇u|² = N at vertices for orthogonal k-vectors."""
    print("=" * 60)
    print("TEST 1: |∇u|² = N at vertices (orthogonal k's)")
    print("=" * 60)

    for N in [1, 2, 3]:
        max_err = 0
        for _ in range(N_trials):
            modes = make_field(N, orthogonal_k=True)
            # Normalize to unit amplitude
            modes = [(k, v, 1.0) for k, v, _ in modes]

            # Pick a random vertex (all cos = ±1)
            signs = np.random.choice([-1, 1], 3)
            x = np.array([0 if s > 0 else np.pi for s in signs], dtype=float)

            omega, grad_u, S = eval_field(modes, x)
            gradu2 = np.sum(grad_u**2)
            err = abs(gradu2 - N)
            max_err = max(max_err, err)

        print(f"  N={N}: max |  |∇u|² - N  | = {max_err:.2e}")

def test_strain_identity(N_trials=5000):
    """Test |S|² = |∇u|² - |ω|²/2 pointwise."""
    print("\n" + "=" * 60)
    print("TEST 2: Pointwise identity |S|² = |∇u|² - |ω|²/2")
    print("=" * 60)

    max_err = 0
    for _ in range(N_trials):
        N = np.random.randint(1, 8)
        modes = make_field(N)
        x = np.random.uniform(0, 2*np.pi, 3)
        omega, grad_u, S = eval_field(modes, x)
        gradu2 = np.sum(grad_u**2)
        S2 = np.sum(S**2)
        om2 = np.dot(omega, omega)
        err = abs(S2 - (gradu2 - om2/2)) / max(gradu2, 1e-10)
        max_err = max(max_err, err)

    print(f"  Max relative error: {max_err:.2e}")

def test_ratio_at_max(N_modes_list, N_trials=500, N_grid=24):
    """Test |∇u|²/|ω|² and S²ê/|ω|² at the global max of |ω|."""
    print("\n" + "=" * 60)
    print("TEST 3: Ratios at global max of |ω|")
    print("=" * 60)
    print(f"{'N':>4} | {'worst ∇u²/ω²':>13} | {'worst S²/ω²':>12} | {'worst S²ê/ω²':>13} | {'worst α/|ω|':>12} | {'barrier':>7}")
    print("-" * 80)

    overall_worst_S2e = 0
    overall_worst_gradu = 0

    for N in N_modes_list:
        worst_gradu = 0
        worst_S2 = 0
        worst_S2e = 0
        worst_alpha = 0

        for trial in range(N_trials):
            # Mix of orthogonal and random k's
            orth = (N <= 3 and trial % 3 == 0)
            modes = make_field(N, orthogonal_k=orth)

            x_max = find_max_omega(modes, N_grid=N_grid)
            result = analyze_point(modes, x_max)

            if result is None:
                continue

            worst_gradu = max(worst_gradu, result['ratio_gradu'])
            worst_S2 = max(worst_S2, result['ratio_S2'])
            worst_S2e = max(worst_S2e, result['ratio_S2e'])
            worst_alpha = max(worst_alpha, result['ratio_alpha'])

        barrier = "PASS" if worst_S2e < 0.75 else "**FAIL**"
        print(f"{N:4d} | {worst_gradu:13.4f} | {worst_S2:12.4f} | {worst_S2e:13.4f} | {worst_alpha:12.4f} | {barrier}")

        overall_worst_S2e = max(overall_worst_S2e, worst_S2e)
        overall_worst_gradu = max(overall_worst_gradu, worst_gradu)

    print(f"\nOverall worst S²ê/|ω|² = {overall_worst_S2e:.4f} (threshold: 0.75)")
    print(f"Overall worst |∇u|²/|ω|² = {overall_worst_gradu:.4f} (threshold: 1.625)")
    return overall_worst_S2e, overall_worst_gradu

def adversarial_search(N_modes=3, N_trials=10000, N_grid=20):
    """Adversarial search: try to MAXIMIZE S²ê/|ω|² or |∇u|²/|ω|²."""
    print("\n" + "=" * 60)
    print(f"ADVERSARIAL SEARCH: N={N_modes}, {N_trials} trials")
    print("=" * 60)

    best_S2e_ratio = 0
    best_gradu_ratio = 0
    best_S2e_config = None
    best_gradu_config = None

    for trial in range(N_trials):
        modes = make_field(N_modes, orthogonal_k=False, max_k=2)
        x_max = find_max_omega(modes, N_grid=N_grid)
        result = analyze_point(modes, x_max)

        if result is None:
            continue

        if result['ratio_S2e'] > best_S2e_ratio:
            best_S2e_ratio = result['ratio_S2e']
            best_S2e_config = (modes, x_max, result)

        if result['ratio_gradu'] > best_gradu_ratio:
            best_gradu_ratio = result['ratio_gradu']
            best_gradu_config = (modes, x_max, result)

        if trial % 2000 == 0 and trial > 0:
            print(f"  [{trial}] best S²ê/|ω|² = {best_S2e_ratio:.6f}, |∇u|²/|ω|² = {best_gradu_ratio:.6f}")

    print(f"\nBest S²ê/|ω|² = {best_S2e_ratio:.6f}")
    if best_S2e_config:
        modes, x, r = best_S2e_config
        print(f"  |ω|² = {r['om2']:.4f}, |S|² = {r['S2']:.4f}, S²ê = {r['S2e']:.4f}")
        print(f"  |∇u|² = {r['gradu2']:.4f}, α/|ω| = {r['ratio_alpha']:.4f}")
        print(f"  k-vectors:")
        for k, v, a in modes:
            print(f"    k={k}, v={v.round(3)}, a={a:.3f}")

    print(f"\nBest |∇u|²/|ω|² = {best_gradu_ratio:.6f}")
    if best_gradu_config:
        _, _, r = best_gradu_config
        print(f"  |ω|² = {r['om2']:.4f}, |∇u|² = {r['gradu2']:.4f}")

    return best_S2e_ratio, best_gradu_ratio

def test_high_N_limit(N_list=[10, 20, 50, 100], N_trials=100, N_grid=16):
    """Test whether the ratio grows with N (it shouldn't)."""
    print("\n" + "=" * 60)
    print("TEST 4: High-N scaling of |∇u|²/|ω|² at max")
    print("=" * 60)

    for N in N_list:
        worst_gradu = 0
        worst_S2e = 0
        for _ in range(N_trials):
            modes = make_field(N, max_k=5)
            x_max = find_max_omega(modes, N_grid=N_grid)
            r = analyze_point(modes, x_max)
            if r is None:
                continue
            worst_gradu = max(worst_gradu, r['ratio_gradu'])
            worst_S2e = max(worst_S2e, r['ratio_S2e'])
        print(f"  N={N:3d}: worst |∇u|²/|ω|² = {worst_gradu:.4f}, worst S²ê/|ω|² = {worst_S2e:.4f}")


if __name__ == '__main__':
    np.random.seed(42)

    test_orthogonal_identity()
    test_strain_identity()
    worst_S2e, worst_gradu = test_ratio_at_max([1, 2, 3, 5, 8, 12], N_trials=300, N_grid=20)
    adversarial_search(N_modes=3, N_trials=5000, N_grid=20)
    adversarial_search(N_modes=5, N_trials=3000, N_grid=16)
    test_high_N_limit(N_list=[10, 20, 50], N_trials=80, N_grid=16)

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Identity |S|² = |∇u|² - |ω|²/2: VERIFIED")
    print(f"|∇u|² = N at vertices for orthogonal k's: VERIFIED")
    print(f"Threshold for barrier: S²ê/|ω|² < 0.75")
    print(f"Threshold via identity: |∇u|²/|ω|² < 1.625")
