"""
numerical track Cycle 1 — Vorticity-Strain Alignment Anatomy

At the vorticity maximum x*, the strain S has eigenvalues λ₁ ≥ λ₂ ≥ λ₃
with eigenvectors e₁, e₂, e₃. The vorticity direction ê = ω/|ω|
decomposes as ê = a₁e₁ + a₂e₂ + a₃e₃.

S²ê = |Sê|² = λ₁²a₁² + λ₂²a₂² + λ₃²a₃²

Key question: does ê align preferentially with e₃ (smallest eigenvalue)?
If a₃² → 1 as N → ∞, then S²ê → λ₃², and since tr(S)=0:
  λ₃ = -(λ₁+λ₂), typically |λ₃| < max(|λ₁|,|λ₂|)
  → S²ê/|ω|² is bounded away from ||S||²_F/|ω|²

This is the DEPLETION OF NONLINEARITY — turbulence's self-organizing tendency
to align vorticity with the least-stretching eigenvector. If we can prove it
holds at the maximum, the Key Lemma follows with HUGE margin.
"""
import numpy as np
from scipy.optimize import minimize

def build_perp_basis(k):
    kn = k / np.linalg.norm(k)
    ref = np.array([1.,0.,0.]) if abs(kn[0]) < 0.9 else np.array([0.,1.,0.])
    e1 = np.cross(kn, ref)
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(kn, e1)
    return e1, e2

def strain_matrix(k, v):
    w = np.cross(k, v)
    k2 = k @ k
    return -(np.outer(w, k) + np.outer(k, w)) / (2 * k2)

def get_ks(max_k2=3):
    ks = []
    r = int(np.sqrt(max_k2)) + 1
    for i in range(-r, r+1):
        for j in range(-r, r+1):
            for l in range(-r, r+1):
                mag2 = i*i + j*j + l*l
                if 0 < mag2 <= max_k2:
                    ks.append(np.array([i, j, l], float))
    return ks

def analyze_alignment(N_modes, n_trials=300, K2_max=3):
    """Measure vorticity alignment with strain eigenvectors at x*."""
    all_ks = get_ks(K2_max)
    n_pool = len(all_ks)
    results = []

    for trial in range(n_trials):
        n_sel = min(N_modes, n_pool)
        idx = np.random.choice(n_pool, n_sel, replace=False)
        ks = [all_ks[i] for i in idx]

        vs = []
        for k in ks:
            e1, e2 = build_perp_basis(k)
            theta = np.random.uniform(0, 2*np.pi)
            vs.append(np.cos(theta)*e1 + np.sin(theta)*e2)

        # Find vorticity max
        def neg_om2(x):
            omega = sum(v * np.cos(k @ x) for k, v in zip(ks, vs))
            return -np.dot(omega, omega)

        best_om2 = 0
        best_x = None
        for _ in range(20):
            x0 = np.random.uniform(0, 2*np.pi, 3)
            res = minimize(neg_om2, x0, method='Nelder-Mead',
                           options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 5000})
            if -res.fun > best_om2:
                best_om2 = -res.fun
                best_x = res.x.copy()

        if best_x is None or best_om2 < 1e-15:
            continue

        # Compute fields at x*
        cos_kx = [np.cos(k @ best_x) for k in ks]
        omega = sum(v * c for v, c in zip(vs, cos_kx))
        S = sum(strain_matrix(k, v) * c for k, v, c in zip(ks, vs, cos_kx))

        om2 = omega @ omega
        if om2 < 1e-15:
            continue
        e_hat = omega / np.sqrt(om2)

        # Strain eigendecomposition
        eigenvalues, eigenvectors = np.linalg.eigh(S)
        # eigh returns ascending order: λ₁ ≤ λ₂ ≤ λ₃ → reverse for λ₁ ≥ λ₂ ≥ λ₃
        idx_sort = np.argsort(-eigenvalues)
        lam = eigenvalues[idx_sort]  # λ₁ ≥ λ₂ ≥ λ₃
        evecs = eigenvectors[:, idx_sort]  # columns are eigenvectors

        # Alignment coefficients
        a = np.array([abs(e_hat @ evecs[:, i]) for i in range(3)])
        a2 = a**2  # a₁², a₂², a₃² (should sum to 1)

        # S²ê components
        S2e_components = lam**2 * a2
        S2e = np.sum(S2e_components)
        S2_F = np.sum(lam**2)  # = λ₁² + λ₂² + λ₃²

        # Stretching rate
        alpha = e_hat @ S @ e_hat  # = λ₁a₁² + λ₂a₂² + λ₃a₃²

        results.append({
            'N': N_modes,
            'lam': lam.copy(),
            'a2': a2.copy(),
            'S2e': S2e,
            'S2_F': S2_F,
            'om2': om2,
            'S2e_over_om2': S2e / om2,
            'SF_over_om2': S2_F / om2,
            'alpha_over_om': alpha / np.sqrt(om2),
            'a3_sq': a2[2],  # alignment with SMALLEST eigenvalue
            'a1_sq': a2[0],  # alignment with LARGEST eigenvalue
            'lam_ratio': lam[2]**2 / lam[0]**2 if abs(lam[0]) > 1e-15 else 0,
        })

    return results

def main():
    print("=" * 70)
    print("VORTICITY-STRAIN ALIGNMENT at the Vorticity Maximum")
    print("=" * 70)
    print()
    print("a₃² = cos²(angle between ω and SMALLEST strain eigenvector)")
    print("If a₃² ≈ 1: perfect alignment with weakest stretching → depletion")
    print()

    header = (f"{'N':>3} | {'trials':>6} | {'⟨a₁²⟩':>6} {'⟨a₂²⟩':>6} {'⟨a₃²⟩':>6} | "
              f"{'⟨S²ê/ω²⟩':>9} {'max':>7} | {'⟨||S||²/ω²⟩':>11} {'max':>7} | "
              f"{'⟨α/|ω|⟩':>8} | {'⟨λ₃²/λ₁²⟩':>9}")
    print(header)
    print("-" * len(header))

    for N in [3, 4, 5, 6, 8, 10, 13, 16, 20, 26]:
        n_trials = max(50, min(400, 4000 // N))
        results = analyze_alignment(N, n_trials)

        if not results:
            continue

        a1 = np.mean([r['a2'][0] for r in results])
        a2 = np.mean([r['a2'][1] for r in results])
        a3 = np.mean([r['a2'][2] for r in results])

        s2e_mean = np.mean([r['S2e_over_om2'] for r in results])
        s2e_max = np.max([r['S2e_over_om2'] for r in results])
        sf_mean = np.mean([r['SF_over_om2'] for r in results])
        sf_max = np.max([r['SF_over_om2'] for r in results])
        alpha_mean = np.mean([r['alpha_over_om'] for r in results])
        lr_mean = np.mean([r['lam_ratio'] for r in results])

        print(f"{N:3d} | {len(results):6d} | {a1:.4f} {a2:.4f} {a3:.4f} | "
              f"{s2e_mean:9.4f} {s2e_max:7.4f} | {sf_mean:11.4f} {sf_max:7.4f} | "
              f"{alpha_mean:8.4f} | {lr_mean:9.4f}")

    print()
    print("=" * 70)
    print("INTERPRETATION:")
    print("  a₃² >> 1/3: ω preferentially aligns with SMALLEST strain eigenvector")
    print("  This makes S²ê ≈ λ₃²|ω|² << ||S||²_F |ω|²")
    print("  Depletion grows with N → Key Lemma margin increases")
    print()
    print("  If a₃² → 1 as N → ∞: proof reduces to bounding λ₃²/|ω|²")
    print("  Since tr(S)=0: λ₃ = -(λ₁+λ₂), typically |λ₃| ≤ max(|λ₁|,|λ₂|)")
    print("  Combined with Frobenius: λ₁²+λ₂²+λ₃² = ||S||²_F ≤ |ω|²/2")
    print("  → λ₃² ≤ |ω|²/2 → S²ê/|ω|² ≤ 1/2 (with perfect alignment)")
    print("=" * 70)

    # Adversarial: find configs where a₃² is SMALL (anti-aligned)
    print()
    print("ADVERSARIAL: configs where a₃² is smallest (worst alignment)")
    for N in [3, 5, 10, 20]:
        n_trials = max(100, 2000 // N)
        results = analyze_alignment(N, n_trials)
        if results:
            worst = min(results, key=lambda r: r['a3_sq'])
            print(f"  N={N:3d}: min a₃² = {worst['a3_sq']:.4f}, "
                  f"a₁² = {worst['a2'][0]:.4f}, "
                  f"S²ê/|ω|² = {worst['S2e_over_om2']:.4f}, "
                  f"λ = [{worst['lam'][0]:.3f}, {worst['lam'][1]:.3f}, {worst['lam'][2]:.3f}]")

if __name__ == '__main__':
    main()
