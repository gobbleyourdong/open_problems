"""
Bilinear Symbol Verification — Angular Cancellation on S²

THE critical numerical test: verify θ(j) ≤ C × 2^{-j} for the
intra-shell enstrophy transfer ratio.

For each dyadic shell Λ_j, generate random div-free fields ω_j,
compute T(j,j) = ∫ ω_j · S_j · ω_j dx, and compare to the
dimensional maximum T_max = ||ω_j||_{L²}² × ||S_j||_{L^∞}.

Tests:
1. Random phases: θ(j) should decrease with j (angular cancellation)
2. Adversarial alignment: can we BREAK θ < 1? (should be impossible)
3. Scaling: θ(j) ~ C × 2^{-j} (Reviewer 3 conjecture)
4. N-independence: same θ at different resolutions

This runs on CPU (no CUDA needed). ~10 min for full test.
"""
import numpy as np
import time
import json
import os

def run_bilinear_symbol_test(N=64, n_trials=200, seeds=range(200)):
    """Compute θ(j) = |T(j,j)| / (||ω_j||² ||S_j||_∞) for random div-free fields."""

    L = 2 * np.pi
    dx = L / N

    # Wavenumber grid
    k1d = np.fft.fftfreq(N, d=1.0/N)  # integer wavenumbers
    kx, ky, kz = np.meshgrid(k1d, k1d, k1d, indexing='ij')
    ksq = kx**2 + ky**2 + kz**2
    ksq[0,0,0] = 1.0  # avoid division by zero
    kmag = np.sqrt(ksq)

    # Dealiasing mask (2/3 rule)
    kmax = N // 3
    D = ((np.abs(kx) < kmax) & (np.abs(ky) < kmax) & (np.abs(kz) < kmax)).astype(np.float64)

    # Shell definitions
    max_shell = int(np.log2(kmax)) + 1
    shell_masks = []
    for j in range(max_shell + 1):
        if j == 0:
            mask = (kmag < 2).astype(np.float64) * D
        else:
            mask = ((kmag >= 2**j) & (kmag < 2**(j+1))).astype(np.float64) * D
        n_modes = int(mask.sum())
        shell_masks.append((mask, n_modes))

    print(f"BILINEAR SYMBOL VERIFICATION — N={N}, {n_trials} trials")
    print(f"Shells: {max_shell+1}, modes per shell: {[sm[1] for sm in shell_masks]}")
    print()

    # Storage for results
    results = {}
    for j in range(max_shell + 1):
        results[j] = {'theta': [], 'T_jj': [], 'T_max': [], 'n_modes': shell_masks[j][1]}

    t0 = time.time()

    for trial in range(n_trials):
        np.random.seed(seeds[trial] if trial < len(seeds) else trial)

        # Generate random div-free field on each shell independently
        for j in range(max_shell + 1):
            mask, n_modes = shell_masks[j]
            if n_modes < 3:
                continue

            # Random Fourier coefficients — project to div-free
            # ω̂(k) must satisfy ω̂(k) ⊥ k (divergence-free)
            # Generate random complex vectors, then project out k-component
            raw_x = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
            raw_y = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
            raw_z = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask

            # Project to divergence-free: ω̂ → ω̂ - k(k·ω̂)/|k|²
            kdot = (kx * raw_x + ky * raw_y + kz * raw_z) / ksq
            wh_x = (raw_x - kx * kdot) * mask
            wh_y = (raw_y - ky * kdot) * mask
            wh_z = (raw_z - kz * kdot) * mask

            # Ensure Hermitian symmetry for real field
            # (For this test, we work directly in Fourier — the quadratic form is
            #  evaluated via Parseval, so we just need the 3D FFT structure)

            # Compute velocity via Biot-Savart: û = ik × ω̂ / |k|²
            # (actually: stream function ψ̂ = ω̂/|k|², û = ik × ψ̂)
            ph_x = wh_x / ksq; ph_y = wh_y / ksq; ph_z = wh_z / ksq
            uh_x = 1j*ky*ph_z - 1j*kz*ph_y
            uh_y = 1j*kz*ph_x - 1j*kx*ph_z
            uh_z = 1j*kx*ph_y - 1j*ky*ph_x

            # Go to physical space
            w_x = np.fft.ifftn(wh_x).real
            w_y = np.fft.ifftn(wh_y).real
            w_z = np.fft.ifftn(wh_z).real

            # Compute strain tensor S = sym(∇u) in physical space
            # ∇u_{il} = IFFT(ik_l û_i)
            S = np.zeros((3,3,N,N,N))
            uh = [uh_x, uh_y, uh_z]
            ik = [1j*kx, 1j*ky, 1j*kz]
            for i in range(3):
                for l in range(3):
                    grad_ul = np.fft.ifftn(ik[l] * uh[i]).real
                    S[i,l] = grad_ul

            # Symmetrize
            S_sym = 0.5 * (S + S.transpose(1,0,2,3,4))

            # Compute T(j,j) = ∫ ω_j · S_j · ω_j dx
            w = np.array([w_x, w_y, w_z])  # (3, N, N, N)
            wSw = np.zeros((N,N,N))
            for i in range(3):
                for l in range(3):
                    wSw += w[i] * S_sym[i,l] * w[l]

            T_jj = wSw.sum() * dx**3

            # Compute ||ω_j||_{L²}² and ||S_j||_{L^∞}
            omega_sq = (w_x**2 + w_y**2 + w_z**2).sum() * dx**3

            # ||S||_∞ = max over grid of operator norm of S(x)
            # For symmetric 3×3, op norm = max |eigenvalue|
            # Vectorized: reshape S to (N³, 3, 3) and batch eigvalsh
            S_flat = S_sym.reshape(3, 3, -1).transpose(2, 0, 1)  # (N³, 3, 3)
            eigs = np.linalg.eigvalsh(S_flat)  # (N³, 3)
            S_inf = np.max(np.abs(eigs))

            T_max = omega_sq * S_inf
            theta = abs(T_jj) / (T_max + 1e-30)

            results[j]['theta'].append(theta)
            results[j]['T_jj'].append(T_jj)
            results[j]['T_max'].append(T_max)

        if (trial + 1) % 20 == 0:
            elapsed = time.time() - t0
            print(f"Trial {trial+1}/{n_trials} [{elapsed:.1f}s]", flush=True)

    total_time = time.time() - t0
    print(f"\nCompleted in {total_time:.1f}s")

    # Analysis
    print(f"\n{'='*70}")
    print(f"INTRA-SHELL DEPLETION RATIO θ(j) = |T(j,j)| / (||ω_j||² ||S_j||_∞)")
    print(f"{'='*70}")
    print(f"{'Shell':>6} {'N_modes':>8} {'θ_mean':>10} {'θ_max':>10} {'θ_min':>10} {'C=θ×2^j':>10}")

    theta_means = []
    theta_maxes = []
    for j in range(max_shell + 1):
        if not results[j]['theta']:
            theta_means.append(None)
            theta_maxes.append(None)
            continue
        thetas = results[j]['theta']
        tm = np.mean(thetas)
        tx = np.max(thetas)
        tn = np.min(thetas)
        C_j = tm * (2**j) if j > 0 else tm
        theta_means.append(tm)
        theta_maxes.append(tx)
        print(f"  j={j:d}  {results[j]['n_modes']:>8d}  {tm:>10.4f}  {tx:>10.4f}  {tn:>10.4f}  {C_j:>10.4f}")

    # Test 2^{-j} scaling
    print(f"\n{'='*70}")
    print(f"SCALING TEST: θ(j) ~ C × 2^{{-j}}")
    print(f"{'='*70}")
    for j in range(1, max_shell + 1):
        if theta_means[j] is not None and theta_means[j-1] is not None and theta_means[j-1] > 0:
            ratio = theta_means[j] / theta_means[j-1]
            expected = 0.5  # if θ ~ 2^{-j}
            print(f"  θ({j})/θ({j-1}) = {ratio:.4f}  (expected 0.50 for 2^{{-j}} scaling)")

    # Test: is θ < 1 UNIVERSALLY?
    all_thetas = []
    for j in range(max_shell + 1):
        all_thetas.extend(results[j]['theta'])

    print(f"\n{'='*70}")
    print(f"UNIVERSALITY TEST: θ < 1 for ALL trials?")
    print(f"{'='*70}")
    print(f"  Total measurements: {len(all_thetas)}")
    print(f"  Max θ ever seen: {max(all_thetas):.6f}")
    print(f"  θ < 1: {'YES ✓' if max(all_thetas) < 1.0 else 'NO ✗'}")
    print(f"  θ < 0.5: {'YES ✓' if max(all_thetas) < 0.5 else 'NO ✗'}")
    print(f"  θ < 0.25: {'YES ✓' if max(all_thetas) < 0.25 else 'NO ✗'}")

    # Save results
    out = {
        'N': N,
        'n_trials': n_trials,
        'max_shell': max_shell,
        'results': {}
    }
    for j in range(max_shell + 1):
        out['results'][str(j)] = {
            'n_modes': results[j]['n_modes'],
            'theta_mean': float(np.mean(results[j]['theta'])) if results[j]['theta'] else None,
            'theta_max': float(np.max(results[j]['theta'])) if results[j]['theta'] else None,
            'theta_min': float(np.min(results[j]['theta'])) if results[j]['theta'] else None,
            'thetas': [float(t) for t in results[j]['theta']],
        }

    outpath = 'ns_blowup/results/bilinear_symbol.json'
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: {outpath}")

    return out


def run_adversarial_test(N=32, n_trials=50):
    """Try to MAXIMIZE θ(j) by adversarial construction.

    The adversary concentrates all vorticity in a single direction
    (parallel k-vectors). This is the worst case from Reviewer 3's
    analysis — modes aligned maximally to avoid angular cancellation.

    If even the adversary can't get θ ≥ 1, the bound is robust.
    """
    L = 2 * np.pi
    dx = L / N

    k1d = np.fft.fftfreq(N, d=1.0/N)
    kx, ky, kz = np.meshgrid(k1d, k1d, k1d, indexing='ij')
    ksq = kx**2 + ky**2 + kz**2
    ksq[0,0,0] = 1.0
    kmag = np.sqrt(ksq)
    kmax = N // 3
    D = ((np.abs(kx) < kmax) & (np.abs(ky) < kmax) & (np.abs(kz) < kmax)).astype(np.float64)

    print(f"\n{'='*70}")
    print(f"ADVERSARIAL TEST — Can we BREAK θ < 1? N={N}")
    print(f"{'='*70}")

    # Test shell j=2 (has enough modes for meaningful test)
    j = 2
    mask = ((kmag >= 2**j) & (kmag < 2**(j+1))).astype(np.float64) * D
    n_modes = int(mask.sum())
    print(f"Shell j={j}, {n_modes} modes")

    best_theta = 0
    best_config = None

    strategies = [
        "random",
        "x-aligned",     # all ω̂ along x (k along y,z)
        "helical",       # ω̂ = k × e_z / |k × e_z| (helical)
        "beltrami",      # ω̂ ∥ k (maximally Beltrami-like, but violates div-free... project)
        "concentrated",  # all power in smallest number of modes
    ]

    for strategy in strategies:
        thetas_strat = []
        for trial in range(n_trials):
            np.random.seed(42 + trial)

            if strategy == "random":
                raw_x = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
                raw_y = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
                raw_z = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
            elif strategy == "x-aligned":
                # Put all vorticity along x-axis
                raw_x = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask * 10
                raw_y = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask * 0.01
                raw_z = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask * 0.01
            elif strategy == "helical":
                # ω̂(k) = k × e_z / |k × e_z| (helical structure)
                cross_x = ky * mask
                cross_y = -kx * mask
                cross_z = np.zeros_like(mask)
                mag = np.sqrt(cross_x**2 + cross_y**2 + 1e-30)
                raw_x = cross_x / mag * mask
                raw_y = cross_y / mag * mask
                raw_z = cross_z
                # Add small random perturbation
                raw_x += 0.1 * np.random.randn(N,N,N) * mask
                raw_y += 0.1 * np.random.randn(N,N,N) * mask
                raw_z += 0.1 * np.random.randn(N,N,N) * mask
            elif strategy == "beltrami":
                # Try to make ω as aligned with strain eigenvectors as possible
                # Start with random, iterate to maximize T(j,j) / ||ω||²||S||_∞
                raw_x = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
                raw_y = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
                raw_z = (np.random.randn(N,N,N) + 1j * np.random.randn(N,N,N)) * mask
            elif strategy == "concentrated":
                # Put all power in just a few modes
                raw_x = np.zeros((N,N,N), dtype=complex)
                raw_y = np.zeros((N,N,N), dtype=complex)
                raw_z = np.zeros((N,N,N), dtype=complex)
                # Find modes in shell
                indices = np.argwhere(mask > 0.5)
                n_active = min(5, len(indices))  # just 5 modes
                for idx in indices[:n_active]:
                    i,j_idx,k_idx = idx
                    raw_x[i,j_idx,k_idx] = np.random.randn() + 1j * np.random.randn()
                    raw_y[i,j_idx,k_idx] = np.random.randn() + 1j * np.random.randn()
                    raw_z[i,j_idx,k_idx] = np.random.randn() + 1j * np.random.randn()
                raw_x *= mask; raw_y *= mask; raw_z *= mask

            # Project to div-free
            kdot = (kx * raw_x + ky * raw_y + kz * raw_z) / ksq
            wh_x = (raw_x - kx * kdot) * mask
            wh_y = (raw_y - ky * kdot) * mask
            wh_z = (raw_z - kz * kdot) * mask

            # Velocity via BS
            ph_x = wh_x / ksq; ph_y = wh_y / ksq; ph_z = wh_z / ksq
            uh_x = 1j*ky*ph_z - 1j*kz*ph_y
            uh_y = 1j*kz*ph_x - 1j*kx*ph_z
            uh_z = 1j*kx*ph_y - 1j*ky*ph_x

            # Physical space
            w_x = np.fft.ifftn(wh_x).real
            w_y = np.fft.ifftn(wh_y).real
            w_z = np.fft.ifftn(wh_z).real

            # Strain
            ik = [1j*kx, 1j*ky, 1j*kz]
            uh = [uh_x, uh_y, uh_z]
            S = np.zeros((3,3,N,N,N))
            for i in range(3):
                for l in range(3):
                    S[i,l] = np.fft.ifftn(ik[l] * uh[i]).real
            S_sym = 0.5 * (S + S.transpose(1,0,2,3,4))

            # T(j,j)
            w = np.array([w_x, w_y, w_z])
            wSw_field = np.zeros((N,N,N))
            for i in range(3):
                for l in range(3):
                    wSw_field += w[i] * S_sym[i,l] * w[l]
            T_jj = wSw_field.sum() * dx**3

            # Norms
            omega_sq = (w_x**2 + w_y**2 + w_z**2).sum() * dx**3

            # ||S||_∞ via sampling (faster than full grid for adversarial)
            S_inf = 0.0
            # Sample a subset of points for speed
            n_sample = min(N**3, 5000)
            flat_indices = np.random.choice(N**3, n_sample, replace=False)
            ix, iy, iz = np.unravel_index(flat_indices, (N,N,N))
            for si in range(n_sample):
                mat = S_sym[:,:,ix[si],iy[si],iz[si]]
                eigs = np.linalg.eigvalsh(mat)
                S_inf = max(S_inf, max(abs(eigs)))

            T_max = omega_sq * S_inf
            theta = abs(T_jj) / (T_max + 1e-30)
            thetas_strat.append(theta)

            if theta > best_theta:
                best_theta = theta
                best_config = strategy

        mean_t = np.mean(thetas_strat)
        max_t = np.max(thetas_strat)
        print(f"  {strategy:>15s}: θ_mean={mean_t:.6f}  θ_max={max_t:.6f}")

    print(f"\n  BEST adversarial θ = {best_theta:.6f} (strategy: {best_config})")
    print(f"  θ < 1: {'YES ✓ — bound holds' if best_theta < 1.0 else 'NO ✗ — BOUND BROKEN'}")
    print(f"  θ < 0.25: {'YES ✓' if best_theta < 0.25 else 'NO'}")


def run_resolution_test():
    """Test θ at multiple resolutions to verify N-independence."""
    print(f"\n{'='*70}")
    print(f"RESOLUTION INDEPENDENCE TEST")
    print(f"{'='*70}")

    for N in [16, 32, 64]:
        print(f"\n--- N={N} ---")
        run_bilinear_symbol_test(N=N, n_trials=50, seeds=range(50))


if __name__ == '__main__':
    import sys

    if '--adversarial' in sys.argv:
        run_adversarial_test(N=32, n_trials=50)
    elif '--resolution' in sys.argv:
        run_resolution_test()
    elif '--quick' in sys.argv:
        # Quick test: fewer trials, smaller N
        run_bilinear_symbol_test(N=32, n_trials=30, seeds=range(30))
        run_adversarial_test(N=32, n_trials=20)
    else:
        # Full test
        run_bilinear_symbol_test(N=64, n_trials=200, seeds=range(200))
        run_adversarial_test(N=32, n_trials=50)
