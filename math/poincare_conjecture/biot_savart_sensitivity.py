"""
Biot-Savart Sensitivity Map — where does broadening → strongest strain?

For each (r₀, z₀), place a Gaussian vorticity blob, solve Poisson,
measure strain. Then broaden the blob and measure again. The ratio
∂α/∂R tells us where the Poisson coupling is most sensitive to
viscous broadening.

This maps the OPERATOR, not the solution. It's a property of the
geometry and the Poisson equation. Compute once, use forever.

Runs on CPU. Uses the existing Poisson solver from euler_fixed.py.
"""
import sys, os, time, json
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# We need the Poisson solver but can't use GPU on Spark (CUDA mismatch)
# Build a simple CPU Poisson solver for this analysis

def build_chebyshev_diff(Nr):
    """Chebyshev differentiation matrix on [0,1] mapped from [-1,1]."""
    j = np.arange(Nr + 1, dtype=np.float64)
    x = np.cos(j * np.pi / Nr)  # Chebyshev points in [-1,1]

    # Differentiation matrix
    c = np.ones(Nr + 1)
    c[0] = 2.0
    c[Nr] = 2.0
    c *= (-1.0) ** j

    X = np.tile(x, (Nr + 1, 1))
    dX = X - X.T
    D = (c[:, None] / c[None, :]) / (dX + np.eye(Nr + 1))
    D -= np.diag(D.sum(axis=1))

    return x, D  # x = Chebyshev points (r), D = first derivative matrix


def solve_poisson_cpu(omega1, D_r, D_r2, r, Nz, Lz):
    """
    Solve -Δ₃ψ₁ = ω₁ on CPU using FFT in z, direct solve in r.
    Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz
    """
    Nr = len(r) - 1
    dz = Lz / Nz
    r_safe = np.where(np.abs(r) < 1e-10, 1e-10, r)
    three_over_r = 3.0 / r_safe

    # L3_r = D²ᵣ + (3/r)Dᵣ
    L3_r = D_r2 + np.diag(three_over_r) @ D_r
    # L'Hôpital at r=0 (index Nr): 4∂ᵣᵣ
    L3_r[Nr, :] = 4.0 * D_r2[Nr, :]

    # Extend omega1 to full period using odd extension for FFT
    n_pad = Nz
    omega_ext = np.zeros((Nr + 1, 2 * Nz))
    omega_ext[:, :Nz + 1] = omega1
    omega_ext[:, Nz + 1:] = -omega1[:, Nz - 1:0:-1]

    # FFT in z
    omega_hat = np.fft.rfft(omega_ext, axis=1)

    psi1 = np.zeros_like(omega1)

    # Solve per Fourier mode
    Nz_ext = 2 * Nz
    k_z = np.fft.rfftfreq(Nz_ext, d=1.0 / Nz_ext)

    for m in range(omega_hat.shape[1]):
        kz = 2.0 * np.pi * k_z[m] / (Lz * 2)  # physical wavenumber
        A = -(L3_r + np.eye(Nr + 1) * (-kz**2))

        # BCs
        A[0, :] = 0; A[0, 0] = 1  # ψ₁=0 at r=1
        A[Nr, :] = D_r[Nr, :]       # ∂ᵣψ₁=0 at r=0

        rhs = omega_hat[:, m].copy()
        rhs[0] = 0
        rhs[Nr] = 0

        try:
            psi_hat = np.linalg.solve(A, rhs)
        except np.linalg.LinAlgError:
            psi_hat = np.zeros(Nr + 1, dtype=complex)

        # Accumulate using inverse FFT contribution
        # For odd extension, only sine modes contribute
        if m > 0 and m < Nz:
            for j in range(Nz + 1):
                psi1[:, j] += (psi_hat * np.exp(1j * kz * j * dz)).real * (2.0 / Nz_ext)

    return psi1


def compute_strain(psi1, dz):
    """Compute ψ₁,z = ∂ψ₁/∂z (drives stretching term 2u₁ψ₁,z)."""
    dpsi_dz = np.zeros_like(psi1)
    dpsi_dz[:, 1:-1] = (psi1[:, 2:] - psi1[:, :-2]) / (2 * dz)
    dpsi_dz[:, 0] = (-3*psi1[:, 0] + 4*psi1[:, 1] - psi1[:, 2]) / (2*dz)
    dpsi_dz[:, -1] = (3*psi1[:, -1] - 4*psi1[:, -2] + psi1[:, -3]) / (2*dz)
    return dpsi_dz


# Parameters
Nr = 64  # Chebyshev points in r
Nz = 128  # Grid points in z
L = 1.0 / 6.0  # Domain period
Lz = L / 4.0   # Quarter period (Luo-Hou domain)

R_base = 0.05   # Baseline blob width
R_broad = 0.07  # Broadened width (40% wider, mimics viscous spreading)
delta_R = R_broad - R_base

# Build grid
r, D_r = build_chebyshev_diff(Nr)
D_r2 = D_r @ D_r
dz = Lz / Nz
z = np.linspace(0, Lz, Nz + 1)

R_grid, Z_grid = np.meshgrid(r, z, indexing='ij')  # (Nr+1, Nz+1)

print(f"=== BIOT-SAVART SENSITIVITY MAP ===")
print(f"Nr={Nr}, Nz={Nz}, L={L}, Lz={Lz}")
print(f"R_base={R_base}, R_broad={R_broad}")
print(f"r range: [{r.min():.4f}, {r.max():.4f}]")
print(f"z range: [{z.min():.6f}, {z.max():.6f}]")

# Sample grid of (r₀, z₀) positions for the blob center
# Skip too close to boundaries
r_samples = np.linspace(0.05, 0.95, 19)  # 19 radial positions
z_samples = np.linspace(Lz * 0.1, Lz * 0.9, 9)  # 9 axial positions

results = []
t0 = time.time()

for ir, r0 in enumerate(r_samples):
    for iz, z0 in enumerate(z_samples):
        # Place Gaussian blob
        omega_base = np.exp(-((R_grid - r0)**2 + (Z_grid - z0)**2) / R_base**2)
        omega_broad = np.exp(-((R_grid - r0)**2 + (Z_grid - z0)**2) / R_broad**2)

        # Solve Poisson for each
        psi_base = solve_poisson_cpu(omega_base, D_r, D_r2, r, Nz, Lz)
        psi_broad = solve_poisson_cpu(omega_broad, D_r, D_r2, r, Nz, Lz)

        # Compute strain at blob center
        dpsi_base = compute_strain(psi_base, dz)
        dpsi_broad = compute_strain(psi_broad, dz)

        # Find closest grid point to (r0, z0)
        ir0 = np.argmin(np.abs(r - r0))
        iz0 = np.argmin(np.abs(z - z0))

        alpha_base = np.abs(dpsi_base[ir0, iz0])
        alpha_broad = np.abs(dpsi_broad[ir0, iz0])

        # Also get max strain anywhere
        alpha_base_max = np.abs(dpsi_base).max()
        alpha_broad_max = np.abs(dpsi_broad).max()

        sensitivity = (alpha_broad - alpha_base) / delta_R
        sensitivity_max = (alpha_broad_max - alpha_base_max) / delta_R

        results.append({
            "r0": float(r0), "z0": float(z0),
            "alpha_base": float(alpha_base),
            "alpha_broad": float(alpha_broad),
            "sensitivity_local": float(sensitivity),
            "sensitivity_max": float(sensitivity_max),
        })

        if (ir * len(z_samples) + iz) % 20 == 0:
            elapsed = time.time() - t0
            print(f"  r0={r0:.2f} z0={z0:.5f} α_base={alpha_base:.4e} "
                  f"α_broad={alpha_broad:.4e} S={sensitivity:.4e} [{elapsed:.0f}s]")

elapsed = time.time() - t0
print(f"\nDone in {elapsed:.0f}s. {len(results)} points.")

# Find peak sensitivity
best = max(results, key=lambda x: x["sensitivity_local"])
print(f"\n=== PEAK SENSITIVITY ===")
print(f"Location: r₀={best['r0']:.3f}, z₀={best['z0']:.6f}")
print(f"α_base={best['alpha_base']:.4e}, α_broad={best['alpha_broad']:.4e}")
print(f"∂α/∂R = {best['sensitivity_local']:.4e}")

# Top 5
top5 = sorted(results, key=lambda x: x["sensitivity_local"], reverse=True)[:5]
print(f"\n=== TOP 5 LOCATIONS ===")
for i, t in enumerate(top5):
    print(f"  {i+1}. r₀={t['r0']:.3f} z₀={t['z0']:.6f} S={t['sensitivity_local']:.4e}")

# Bottom 5 (wall/boundary penalty)
bot5 = sorted(results, key=lambda x: x["sensitivity_local"])[:5]
print(f"\n=== BOTTOM 5 (weakest coupling) ===")
for i, b in enumerate(bot5):
    print(f"  {i+1}. r₀={b['r0']:.3f} z₀={b['z0']:.6f} S={b['sensitivity_local']:.4e}")

# Save
with open("ns_blowup/results/biot_savart_sensitivity.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to ns_blowup/results/biot_savart_sensitivity.json")
