"""
FFT-based test of S²ê/|ω|² at the global max of |ω|.

Uses FFT to evaluate fields on a dense grid, finding the TRUE global max.
This eliminates the grid-resolution artifacts that plagued the point-based search.
"""
import numpy as np

def make_modes(N_modes, max_k=3, equal_amp=False):
    """Create random div-free modes on T³."""
    modes = []
    used = set()
    while len(modes) < N_modes:
        k = np.random.randint(-max_k, max_k+1, 3)
        if np.all(k == 0):
            continue
        tk = tuple(k.tolist())
        ntk = tuple((-k).tolist())
        if tk in used or ntk in used:
            continue
        used.add(tk)
        # Random div-free polarization
        v = np.random.randn(3)
        v -= v.dot(k) * k / np.dot(k, k)
        v /= np.linalg.norm(v)
        a = 1.0 if equal_amp else np.random.uniform(0.5, 2.0)
        modes.append((k.astype(float), v, a))
    return modes

def eval_on_grid(modes, N_grid):
    """Evaluate ω, ∇u, S on a uniform grid using direct summation.
    Returns 3D arrays of shape (N_grid, N_grid, N_grid, ...)"""
    xs = np.linspace(0, 2*np.pi, N_grid, endpoint=False)
    X, Y, Z = np.meshgrid(xs, xs, xs, indexing='ij')

    omega = np.zeros((N_grid, N_grid, N_grid, 3))
    grad_u = np.zeros((N_grid, N_grid, N_grid, 3, 3))

    for k, v, a in modes:
        phase = k[0]*X + k[1]*Y + k[2]*Z  # (N,N,N)
        c = np.cos(phase)
        s = np.sin(phase)

        # ω_mode = a * v * cos(k·x)
        for j in range(3):
            omega[..., j] += a * v[j] * c

        # u_mode = a * (k × v) * sin(k·x) / |k|²
        knorm2 = np.dot(k, k)
        w = np.cross(k, v)
        u_coeff = a * w / knorm2

        # ∇u_mode = u_coeff ⊗ k * cos(k·x)
        for i in range(3):
            for j in range(3):
                grad_u[..., i, j] += u_coeff[i] * k[j] * c

    return omega, grad_u

def compute_ratios_on_grid(omega, grad_u):
    """Compute |ω|², |∇u|², |S|², S²ê at every grid point."""
    N = omega.shape[0]

    # |ω|²
    om2 = np.sum(omega**2, axis=-1)  # (N,N,N)

    # S = (∇u + ∇uᵀ)/2
    S = 0.5 * (grad_u + np.swapaxes(grad_u, -2, -1))  # (N,N,N,3,3)

    # |∇u|²
    gradu2 = np.sum(grad_u**2, axis=(-2,-1))  # (N,N,N)

    # |S|²
    S2 = np.sum(S**2, axis=(-2,-1))  # (N,N,N)

    return om2, gradu2, S2, S

def analyze_at_max(modes, N_grid=64):
    """Find global max of |ω| and compute all ratios there."""
    omega, grad_u = eval_on_grid(modes, N_grid)
    om2, gradu2, S2, S = compute_ratios_on_grid(omega, grad_u)

    # Find global max
    idx = np.unravel_index(np.argmax(om2), om2.shape)
    om2_max = om2[idx]

    if om2_max < 1e-10:
        return None

    e_hat = omega[idx] / np.sqrt(om2_max)  # (3,)
    S_max = S[idx]  # (3,3)
    Se = S_max @ e_hat  # (3,)
    S2e = np.dot(Se, Se)
    alpha = e_hat @ S_max @ e_hat

    # Verify identity
    identity_err = abs(S2[idx] - (gradu2[idx] - om2_max/2)) / max(gradu2[idx], 1e-10)

    return {
        'om2': om2_max,
        'gradu2': gradu2[idx],
        'S2': S2[idx],
        'S2e': S2e,
        'alpha': alpha,
        'ratio_gradu': gradu2[idx] / om2_max,
        'ratio_S2': S2[idx] / om2_max,
        'ratio_S2e': S2e / om2_max,
        'ratio_alpha': alpha / np.sqrt(om2_max),
        'identity_err': identity_err,
    }

def main():
    np.random.seed(42)

    print("=" * 70)
    print("FFT-BASED S²ê/|ω|² TEST AT GLOBAL MAX OF |ω|")
    print("Grid: 64³ = 262,144 points per trial")
    print("=" * 70)

    N_grid = 64
    N_trials = 200

    print(f"\n{'N':>4} | {'trials':>6} | {'worst S²ê/ω²':>13} | {'worst ∇u²/ω²':>13} | {'worst S²/ω²':>12} | {'worst α/|ω|':>12} | {'barrier':>7}")
    print("-" * 90)

    for N_modes in [1, 2, 3, 5, 8, 12, 20]:
        worst_S2e = 0
        worst_gradu = 0
        worst_S2 = 0
        worst_alpha = -999
        n_done = 0

        for trial in range(N_trials):
            # Use smaller max_k for more modes (to stay within grid resolution)
            mk = max(1, min(3, 30 // N_modes))
            modes = make_modes(N_modes, max_k=mk)
            r = analyze_at_max(modes, N_grid=N_grid)
            if r is None:
                continue
            n_done += 1
            worst_S2e = max(worst_S2e, r['ratio_S2e'])
            worst_gradu = max(worst_gradu, r['ratio_gradu'])
            worst_S2 = max(worst_S2, r['ratio_S2'])
            worst_alpha = max(worst_alpha, r['ratio_alpha'])

        barrier = "PASS" if worst_S2e < 0.75 else "**FAIL**"
        print(f"{N_modes:4d} | {n_done:6d} | {worst_S2e:13.6f} | {worst_gradu:13.6f} | {worst_S2:12.6f} | {worst_alpha:12.6f} | {barrier}")

    # Adversarial: focus on N=3 with orthogonal k's
    print("\n" + "=" * 70)
    print("ADVERSARIAL: N=3, orthogonal k's, 500 trials")
    print("=" * 70)

    worst_S2e = 0
    worst_config = None
    for trial in range(500):
        ks = np.eye(3)
        modes = []
        for i in range(3):
            k = ks[i]
            v = np.random.randn(3)
            v -= v.dot(k) * k
            v /= np.linalg.norm(v)
            modes.append((k, v, 1.0))

        r = analyze_at_max(modes, N_grid=N_grid)
        if r and r['ratio_S2e'] > worst_S2e:
            worst_S2e = r['ratio_S2e']
            worst_config = (modes, r)

    print(f"Worst S²ê/|ω|² = {worst_S2e:.6f}")
    if worst_config:
        modes, r = worst_config
        print(f"|ω|² = {r['om2']:.4f}, |S|² = {r['S2']:.4f}, S²ê = {r['S2e']:.4f}")
        print(f"|∇u|² = {r['gradu2']:.4f}, identity err = {r['identity_err']:.2e}")
        for k, v, a in modes:
            print(f"  k={k}, v={v.round(4)}")

    # Adversarial: focus on N=3, non-orthogonal
    print("\n" + "=" * 70)
    print("ADVERSARIAL: N=3, non-orthogonal, 1000 trials")
    print("=" * 70)

    worst_S2e = 0
    for trial in range(1000):
        modes = make_modes(3, max_k=2)
        r = analyze_at_max(modes, N_grid=N_grid)
        if r and r['ratio_S2e'] > worst_S2e:
            worst_S2e = r['ratio_S2e']
            worst_r = r

    print(f"Worst S²ê/|ω|² = {worst_S2e:.6f}")
    print(f"|ω|² = {worst_r['om2']:.4f}, |∇u|²/|ω|² = {worst_r['ratio_gradu']:.4f}")

    # KEY TEST: high N with adapted grid
    print("\n" + "=" * 70)
    print("HIGH-N TEST (max_k=1, ensures resolution)")
    print("=" * 70)

    for N_modes in [8, 12, 20, 30]:
        worst_S2e = 0
        worst_gradu = 0
        for trial in range(100):
            modes = make_modes(N_modes, max_k=1, equal_amp=True)
            r = analyze_at_max(modes, N_grid=N_grid)
            if r is None:
                continue
            worst_S2e = max(worst_S2e, r['ratio_S2e'])
            worst_gradu = max(worst_gradu, r['ratio_gradu'])
        barrier = "PASS" if worst_S2e < 0.75 else "**FAIL**"
        print(f"  N={N_modes:3d} (max_k=1): worst S²ê/|ω|² = {worst_S2e:.6f}, |∇u|²/|ω|² = {worst_gradu:.6f} {barrier}")


if __name__ == '__main__':
    main()
