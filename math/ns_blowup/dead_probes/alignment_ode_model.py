"""
Restricted Euler / Vieillefosse Model with Pressure Hessian

Track the alignment cos²(ω, e₁) of a vortex tube with the
strain eigenvectors, including:
1. Self-stretching by the strain
2. Pressure Hessian (isotropic + deviatoric)
3. Perturbations from nearby tubes (transient forcing)

The velocity gradient tensor A = S + W (strain + rotation) evolves:
  dA/dt + A² + H = ν∆A  (simplified, ignoring advection)

We parameterize by:
- α = stretching rate (eigenvalue of S along ω)
- ξ = vorticity direction in strain eigenbasis
- |ω| = vorticity magnitude

Key question: does the pressure Hessian push cos²(ω,e₁) below 1/3
at high |ω|?

Output: time series of (|ω|, cos²(ω,e₁), stretching_sign) for PySR.
"""
import numpy as np
from scipy.integrate import solve_ivp
import json

def run_alignment_model(n_realizations=500, T=5.0, dt_max=0.01,
                        nu=1e-4, perturbation_strength=0.1):
    """
    Evolve the velocity gradient tensor dA/dt = -A² - H + ν∆A + perturbation.

    A is a 3x3 traceless matrix (9 components, trace=0 gives 8 DoF).
    We decompose A = S + W where S = sym(A), W = antisym(A).

    The vorticity vector ω is extracted from W: ω_i = -ε_ijk W_jk.
    The strain eigenvalues and eigenvectors come from S.

    Pressure Hessian models:
    1. Isotropic (Vieillefosse): H = -(1/3)tr(A²) I
    2. Tetrad model: H_dev proportional to ω⊗ω
    3. Our model: isotropic part scales as |ω|²/6, deviatoric bounded by f(α)
    """

    results = []

    for realization in range(n_realizations):
        np.random.seed(realization)

        # Random initial velocity gradient (traceless)
        A0 = np.random.randn(3,3)
        A0 -= np.eye(3) * np.trace(A0) / 3  # make traceless

        # Scale to desired initial |ω|
        omega_init = 1.0 + 5.0 * np.random.rand()  # |ω| between 1 and 6
        W0 = 0.5 * (A0 - A0.T)
        omega0 = np.array([W0[2,1]-W0[1,2], W0[0,2]-W0[2,0], W0[1,0]-W0[0,1]]) / 2
        if np.linalg.norm(omega0) > 1e-10:
            A0 *= omega_init / np.linalg.norm(omega0)

        # Random perturbation direction (from "nearby tubes")
        perturb_dir = np.random.randn(3,3)
        perturb_dir -= np.eye(3) * np.trace(perturb_dir) / 3
        perturb_dir /= np.linalg.norm(perturb_dir) + 1e-10

        # Random perturbation frequency (eddy turnover-like)
        perturb_freq = 1.0 + 3.0 * np.random.rand()

        def rhs(t, A_flat):
            A = A_flat.reshape(3,3)

            # Strain and rotation
            S = 0.5 * (A + A.T)
            W = 0.5 * (A - A.T)

            # Vorticity from W
            omega = np.array([W[2,1]-W[1,2], W[0,2]-W[2,0], W[1,0]-W[0,1]]) / 2
            omega_mag = np.linalg.norm(omega)

            # A² term
            A2 = A @ A

            # Pressure Hessian — OUR MODEL
            # Isotropic part: H_iso = (|ω|²/2 - |S|²) / 3 × I
            # For the restricted Euler, |S|² = tr(S²) = 0.5*tr(A²+A^T A)
            S_sq = np.trace(S @ S)
            omega_sq = omega_mag**2
            delta_p = 0.5 * omega_sq - S_sq  # Δp = |ω|²/2 - |S|²
            H_iso = (delta_p / 3.0) * np.eye(3)

            # Deviatoric part: bounded by our f(α) result
            # Use the "tetrad" model: H_dev ~ -c × (ω⊗ω - |ω|²I/3) / |ω|²
            # This models the non-local pressure from the vorticity
            if omega_mag > 1e-10:
                omega_hat = omega / omega_mag
                H_dev = -0.2 * omega_sq * (np.outer(omega_hat, omega_hat) - np.eye(3)/3)
            else:
                H_dev = np.zeros((3,3))

            H = H_iso + H_dev

            # Viscous term (simplified)
            visc = -nu * np.linalg.norm(A)**2 * A  # rough model of ν∆A

            # Perturbation from nearby tubes (transient forcing)
            perturb = perturbation_strength * np.sin(perturb_freq * t) * perturb_dir

            # dA/dt = -A² - H + viscous + perturbation
            dA = -A2 - H + visc + perturb

            # Project to traceless
            dA -= np.eye(3) * np.trace(dA) / 3

            return dA.flatten()

        # Solve
        sol = solve_ivp(rhs, [0, T], A0.flatten(), max_step=dt_max,
                       method='RK45', rtol=1e-8, atol=1e-10)

        # Extract time series
        for i in range(0, len(sol.t), max(1, len(sol.t)//50)):
            A = sol.y[:, i].reshape(3,3)
            S = 0.5 * (A + A.T)
            W = 0.5 * (A - A.T)

            omega = np.array([W[2,1]-W[1,2], W[0,2]-W[2,0], W[1,0]-W[0,1]]) / 2
            omega_mag = np.linalg.norm(omega)

            if omega_mag < 1e-10:
                continue

            # Strain eigenvalues and eigenvectors
            evals, evecs = np.linalg.eigh(S)
            # Sort: λ₁ ≥ λ₂ ≥ λ₃
            idx = np.argsort(evals)[::-1]
            evals = evals[idx]
            evecs = evecs[:, idx]

            e1 = evecs[:, 0]  # most stretching
            e3 = evecs[:, 2]  # most compressive

            omega_hat = omega / omega_mag
            cos2_e1 = np.dot(omega_hat, e1)**2
            cos2_e3 = np.dot(omega_hat, e3)**2

            # Stretching rate
            alpha = np.dot(omega_hat, S @ omega_hat)

            # Pressure Hessian contribution
            S_sq = np.trace(S @ S)
            delta_p = 0.5 * omega_mag**2 - S_sq

            results.append({
                'omega_mag': float(omega_mag),
                'cos2_e1': float(cos2_e1),
                'cos2_e3': float(cos2_e3),
                'alpha': float(alpha),  # stretching rate
                'lambda1': float(evals[0]),
                'lambda3': float(evals[2]),
                'delta_p': float(delta_p),  # Δp (isotropic pressure source)
                'realization': realization,
                't': float(sol.t[i]),
            })

    return results


def analyze_results(results):
    """Analyze alignment vs intensity and prepare for PySR."""

    omegas = np.array([r['omega_mag'] for r in results])
    cos2s = np.array([r['cos2_e1'] for r in results])
    alphas = np.array([r['alpha'] for r in results])
    delta_ps = np.array([r['delta_p'] for r in results])

    print(f"ALIGNMENT ODE MODEL — {len(results)} data points")
    print("="*60)

    # Bin by |ω| and compute mean cos²(ω, e₁)
    bins = [0, 1, 2, 5, 10, 20, 50, 100, 500, np.inf]
    print(f"\n{'|ω| range':>15} {'n':>6} {'cos²(ω,e₁)':>12} {'α (stretch)':>12} {'Δp':>12}")

    for i in range(len(bins)-1):
        mask = (omegas >= bins[i]) & (omegas < bins[i+1])
        n = mask.sum()
        if n < 5:
            continue
        c2 = np.mean(cos2s[mask])
        al = np.mean(alphas[mask])
        dp = np.mean(delta_ps[mask])
        label = f"[{bins[i]:.0f}, {bins[i+1]:.0f})" if bins[i+1] < np.inf else f"[{bins[i]:.0f}, ∞)"
        verdict = "< 1/3 ✓" if c2 < 1/3 else "> 1/3 ✗"
        print(f"{label:>15} {n:>6} {c2:>12.4f} {al:>+12.4f} {dp:>+12.2f}  {verdict}")

    # The KEY question: at high |ω|, is cos² < 1/3?
    high_mask = omegas > 20
    low_mask = (omegas > 1) & (omegas < 5)

    if high_mask.sum() > 10 and low_mask.sum() > 10:
        print(f"\n{'='*60}")
        print(f"HIGH vs LOW INTENSITY:")
        print(f"  Low  (|ω| ∈ [1,5)):  cos²(ω,e₁) = {np.mean(cos2s[low_mask]):.4f}")
        print(f"  High (|ω| > 20):     cos²(ω,e₁) = {np.mean(cos2s[high_mask]):.4f}")
        print(f"  Random:              cos²(ω,e₁) = 0.3333")

        if np.mean(cos2s[high_mask]) < 1/3:
            print(f"\n  *** HIGH INTENSITY → cos² < 1/3 → COMPRESSION ✓ ***")
        else:
            print(f"\n  *** HIGH INTENSITY → cos² > 1/3 → still stretching ✗ ***")

    # Prepare PySR data
    # Features: |ω|, λ₁, λ₃, Δp, λ₁/|λ₃|
    X = np.column_stack([
        omegas,
        np.array([r['lambda1'] for r in results]),
        np.array([r['lambda3'] for r in results]),
        delta_ps,
        np.array([r['lambda1'] for r in results]) / (np.abs(np.array([r['lambda3'] for r in results])) + 1e-10),
    ])
    y = cos2s

    # Save for PySR
    np.save('ns_blowup/results/alignment_X.npy', X)
    np.save('ns_blowup/results/alignment_y.npy', y)
    print(f"\nSaved PySR data: X shape {X.shape}, y shape {y.shape}")
    print(f"Features: [|ω|, λ₁, λ₃, Δp, λ₁/|λ₃|]")

    # Also check: does stretching α correlate with cos²?
    print(f"\n{'='*60}")
    print("STRETCHING vs ALIGNMENT:")
    stretch_mask = alphas > 0
    compress_mask = alphas < 0
    if stretch_mask.sum() > 10 and compress_mask.sum() > 10:
        print(f"  Stretching (α>0): cos²(ω,e₁) = {np.mean(cos2s[stretch_mask]):.4f}, mean α = {np.mean(alphas[stretch_mask]):+.4f}")
        print(f"  Compression (α<0): cos²(ω,e₁) = {np.mean(cos2s[compress_mask]):.4f}, mean α = {np.mean(alphas[compress_mask]):+.4f}")
        print(f"  Fraction compressive: {compress_mask.sum()/len(alphas)*100:.1f}%")


if __name__ == '__main__':
    print("Running alignment ODE model...")
    results = run_alignment_model(n_realizations=500, T=5.0, perturbation_strength=0.3)
    analyze_results(results)
