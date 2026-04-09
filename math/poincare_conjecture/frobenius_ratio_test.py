"""
Test: is |S|²_F / |ω|² < 3/4 at vorticity maxima?

If yes: S²ê ≤ |S|²_F < 3|ω|²/4 → Key Lemma follows trivially.

Per-mode identity: |Ŝ_k|²_F = |ω̂_k|²/2  (exact, from Biot-Savart on T³)
L² identity: ||S||²_{L²} = ||ω||²_{L²}/2  (Parseval consequence)

The question: does the pointwise ratio |S(x*)|²_F / |ω(x*)|² stay below 3/4 at x* = argmax|ω|?

Cross-term formula:
  Tr(Ŝ_j Ŝ_kᵀ) = [(k_j·k_k)(w_j·w_k) + (k_j·w_k)(w_j·k_k)] / (2|k_j|²|k_k|²)
  where w_j = k_j × ω̂_j

If the strain cross-terms at x* are less than 3/4 of the vorticity cross-terms,
the Key Lemma follows.
"""

import numpy as np
from itertools import product as iprod

def build_field(N_modes, K_max=3):
    """Build a random div-free field on T³ with modes up to |k| ≤ K_max."""
    modes = []
    for i in range(-K_max, K_max+1):
        for j in range(-K_max, K_max+1):
            for l in range(-K_max, K_max+1):
                k = np.array([i,j,l], float)
                k2 = k@k
                if 0 < k2 <= K_max**2:
                    modes.append(k)

    # Select N_modes random modes (keep k and -k independent for real fields...
    # but we'll work with complex amplitudes for simplicity)
    if N_modes > len(modes):
        N_modes = len(modes)
    idx = np.random.choice(len(modes), N_modes, replace=False)
    ks = [modes[i] for i in idx]

    # Random div-free amplitudes: omega_hat_k ⊥ k
    omegas = []
    for k in ks:
        # Random vector, project out k component
        v = np.random.randn(3)
        v -= k * (v@k) / (k@k)
        if np.linalg.norm(v) < 1e-10:
            v = np.random.randn(3)
            v -= k * (v@k) / (k@k)
        omegas.append(v)

    return ks, omegas

def eval_omega(ks, omegas, x):
    """Evaluate ω(x) = Σ ω̂_k e^{ik·x}"""
    omega = np.zeros(3)
    for k, om in zip(ks, omegas):
        omega += om * np.cos(k@x)  # Real part only (symmetric modes)
    return omega

def eval_S(ks, omegas, x):
    """Evaluate S(x) = sym(∇u)(x) from Biot-Savart."""
    S = np.zeros((3,3))
    for k, om in zip(ks, omegas):
        w = np.cross(k, om)  # k × ω̂
        # (∇u)^k = -w⊗k / |k|²
        # S^k = -(w⊗k + k⊗w) / (2|k|²)
        k2 = k@k
        phase = np.cos(k@x)
        S -= phase * (np.outer(w, k) + np.outer(k, w)) / (2*k2)
    return S

def find_max_omega(ks, omegas, N_grid=40, N_refine=5):
    """Find x* = argmax |ω(x)| on [0,2π]³."""
    # Coarse grid search
    best_x = np.zeros(3)
    best_om2 = 0

    xs = np.linspace(0, 2*np.pi, N_grid, endpoint=False)
    for i in range(N_grid):
        for j in range(N_grid):
            for l in range(N_grid):
                x = np.array([xs[i], xs[j], xs[l]])
                om = eval_omega(ks, omegas, x)
                om2 = om@om
                if om2 > best_om2:
                    best_om2 = om2
                    best_x = x.copy()

    # Refine with gradient ascent
    for _ in range(N_refine):
        h = 1e-4
        grad = np.zeros(3)
        om0 = eval_omega(ks, omegas, best_x)
        f0 = om0@om0
        for d in range(3):
            xp = best_x.copy(); xp[d] += h
            omp = eval_omega(ks, omegas, xp)
            grad[d] = (omp@omp - f0) / h

        # Line search
        for step in [0.1, 0.01, 0.001]:
            xt = best_x + step * grad / (np.linalg.norm(grad) + 1e-10)
            omt = eval_omega(ks, omegas, xt)
            if omt@omt > best_om2:
                best_om2 = omt@omt
                best_x = xt

    return best_x

def compute_ratios(ks, omegas, x_star):
    """Compute |S|²_F/|ω|² and S²ê/|ω|² at x*."""
    omega = eval_omega(ks, omegas, x_star)
    om2 = omega@omega
    if om2 < 1e-15:
        return None, None

    S = eval_S(ks, omegas, x_star)

    # Frobenius norm squared
    S2_F = np.sum(S**2)

    # S²ê
    e_hat = omega / np.sqrt(om2)
    Se = S @ e_hat
    S2e = Se @ Se

    return S2_F / om2, S2e / om2

def cross_term_analysis(ks, omegas, x_star):
    """Analyze Tr(Ŝ_j Ŝ_kᵀ) vs ω̂_j · ω̂_k cross terms at x*."""
    N = len(ks)

    # Per-mode quantities at x*
    ws = [np.cross(k, om) for k, om in zip(ks, omegas)]
    phases = [np.cos(k@x_star) for k in ks]

    # Vorticity cross-terms (with phases)
    omega_cross = 0.0
    strain_cross = 0.0

    for j in range(N):
        for l in range(j+1, N):
            # Vorticity cross: (ω̂_j · ω̂_l) × phase_j × phase_l
            C_omega = (omegas[j] @ omegas[l]) * phases[j] * phases[l]

            # Strain cross: Tr(Ŝ_j Ŝ_lᵀ) × phase_j × phase_l
            # = [(k_j·k_l)(w_j·w_l) + (k_j·w_l)(w_j·k_l)] / (2|k_j|²|k_l|²) × phases
            kj, kl = ks[j], ks[l]
            wj, wl = ws[j], ws[l]
            kj2, kl2 = kj@kj, kl@kl

            C_strain = ((kj@kl)*(wj@wl) + (kj@wl)*(wj@kl)) / (2*kj2*kl2)
            C_strain *= phases[j] * phases[l]

            omega_cross += C_omega
            strain_cross += C_strain

    return omega_cross, strain_cross

# === MAIN TEST ===
if __name__ == '__main__':
    np.random.seed(42)

    print("=" * 70)
    print("FROBENIUS RATIO TEST: |S|²_F / |ω|² at vorticity maxima")
    print("Key Lemma follows if ratio < 3/4 = 0.75")
    print("=" * 70)
    print()

    worst_frob = 0
    worst_s2e = 0
    n_trials = 0

    results_by_N = {}

    for N in [2, 3, 4, 5, 8, 12, 20, 30, 50]:
        K_max = 2 if N <= 12 else 3
        n_per = 50 if N <= 12 else 20

        frob_ratios = []
        s2e_ratios = []

        for trial in range(n_per):
            ks, omegas = build_field(N, K_max=K_max)
            x_star = find_max_omega(ks, omegas, N_grid=30)

            frob_r, s2e_r = compute_ratios(ks, omegas, x_star)
            if frob_r is None:
                continue

            frob_ratios.append(frob_r)
            s2e_ratios.append(s2e_r)

            worst_frob = max(worst_frob, frob_r)
            worst_s2e = max(worst_s2e, s2e_r)
            n_trials += 1

        if frob_ratios:
            results_by_N[N] = {
                'frob_max': max(frob_ratios),
                'frob_mean': np.mean(frob_ratios),
                's2e_max': max(s2e_ratios),
                's2e_mean': np.mean(s2e_ratios),
            }
            print(f"N={N:3d}: |S|²_F/|ω|² max={max(frob_ratios):.6f}  "
                  f"mean={np.mean(frob_ratios):.6f}  |  "
                  f"S²ê/|ω|² max={max(s2e_ratios):.6f}  "
                  f"mean={np.mean(s2e_ratios):.6f}")

    print()
    print(f"Overall worst |S|²_F/|ω|²: {worst_frob:.6f} (< 0.75? {worst_frob < 0.75})")
    print(f"Overall worst S²ê/|ω|²:    {worst_s2e:.6f} (< 0.75? {worst_s2e < 0.75})")
    print(f"Total trials: {n_trials}")

    # Cross-term analysis for a few configs
    print()
    print("=" * 70)
    print("CROSS-TERM ANALYSIS: C_S / C_ω at the max")
    print("If C_S/C_ω ≈ 1/2 (matching diagonal): Key Lemma follows")
    print("=" * 70)
    print()

    for N in [3, 5, 10, 20]:
        K_max = 2 if N <= 12 else 3
        ratios = []
        for trial in range(30):
            ks, omegas = build_field(N, K_max=K_max)
            x_star = find_max_omega(ks, omegas, N_grid=30)

            C_om, C_S = cross_term_analysis(ks, omegas, x_star)
            if abs(C_om) > 1e-10:
                ratios.append(C_S / C_om)

        if ratios:
            print(f"N={N:3d}: C_S/C_ω  max={max(ratios):.6f}  "
                  f"min={min(ratios):.6f}  mean={np.mean(ratios):.6f}  "
                  f"(need < 0.75)")
