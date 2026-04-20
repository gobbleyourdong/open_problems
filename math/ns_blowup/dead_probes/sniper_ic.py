"""
Sniper IC — vorticity centered at r=0.10 (peak Biot-Savart sensitivity).

In Hou-Li variables: u₁ = uθ/r, ω₁ = ωθ/r
The 1/r is already factored out, so u₁ and ω₁ are regular at r=0.

IC design:
- u₁ peaked at r≈0.10, smooth, satisfies BCs
- ω₁ = 0 initially (let the dynamics generate it)
- Odd in z (sin profile), even/zero at z=Lz
- Smooth cutoff at r=1 (wall BC: u₁=0)

The key: place the vorticity-generating swirl at r=0.10 where
∂α/∂R = +6.4e4 (broadening INCREASES strain).

Test at Nr=64 on Spark CPU first — just check the IC is valid
and the solver runs without crashing. Then take to GPU.
"""
import sys, os, math, time, json
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))

# Can't use torch GPU on Spark (CUDA mismatch), so test IC construction only
# and run a few CPU steps to verify stability

print("=== SNIPER IC DESIGN ===\n")

# Parameters
Nr = 64
Nz = 128
L = 1.0 / 6.0
Lz = L / 4.0
r_target = 0.10  # Peak sensitivity location
sigma_r = 0.05   # Radial width
amplitude = 100.0  # Same order as Luo-Hou

# Chebyshev points
j = np.arange(Nr + 1, dtype=np.float64)
r = np.cos(j * np.pi / Nr)  # [-1, 1], index 0=r=1(wall), Nr=r=-1

# z grid
z = np.linspace(0, Lz, Nz + 1)
R, Z = np.meshgrid(r, z, indexing='ij')

# IC for u₁: peaked at r=r_target
# u₁ must be 0 at r=1 (wall BC) and regular at r=0
# Use: u₁ = A * exp(-(r - r_target)²/σ²) * (1 - r²) * sin(2πz/L)
# The (1-r²) ensures u₁=0 at r=±1
# sin(2πz/L) gives odd symmetry at z=0 and z=Lz

u1 = amplitude * np.exp(-((R - r_target)**2) / sigma_r**2) * \
     (1 - R**2) * np.sin(2 * math.pi * Z / L)

# ω₁ = 0 initially
omega1 = np.zeros_like(u1)

# Enforce BCs
u1[0, :] = 0  # r=1 wall

print(f"Domain: r∈[-1,1] (Chebyshev), z∈[0,{Lz:.6f}]")
print(f"Target: r₀={r_target}, σᵣ={sigma_r}")
print(f"Amplitude: {amplitude}")
print(f"\nu₁ stats:")
print(f"  max = {u1.max():.4f}")
print(f"  min = {u1.min():.4f}")
print(f"  |u₁|_max = {np.abs(u1).max():.4f}")

# Where is u₁ peaked?
peak_idx = np.unravel_index(np.abs(u1).argmax(), u1.shape)
print(f"  Peak at r={r[peak_idx[0]]:.4f}, z={z[peak_idx[1]]:.6f}")
print(f"  Peak value = {u1[peak_idx[0], peak_idx[1]]:.4f}")

# Check u₁ at r=0 (should be small)
axis_idx = Nr  # r=-1 is index Nr... wait, Chebyshev maps to [-1,1]
# Actually for the NS solver, r∈[0,1] is mapped from Chebyshev [-1,1]
# Need to check how the solver handles this

print(f"\n  u₁ at r=1.0 (wall, idx 0) = {u1[0, Nz//4]:.6f}")
print(f"  u₁ at r=0.0 (near axis) ≈ {u1[Nr//2, Nz//4]:.6f}")
print(f"  u₁ at r=-1.0 (idx Nr) = {u1[Nr, Nz//4]:.6f}")

# Radial profile at z = Lz/4 (quarter period, where sin is max)
z_quarter = Nz // 4
print(f"\n=== RADIAL PROFILE at z={z[z_quarter]:.6f} ===")
print(f"{'r':>8} {'u₁':>12}")
for i in range(0, Nr+1, max(1, Nr//20)):
    print(f"{r[i]:8.4f} {u1[i, z_quarter]:12.4f}")

# Also try a version with different r_target values for comparison
print(f"\n=== SENSITIVITY COMPARISON: peak u₁ at different r₀ ===")
for rt in [0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 0.80, 0.95]:
    u_test = amplitude * np.exp(-((R - rt)**2) / sigma_r**2) * \
             (1 - R**2) * np.sin(2 * math.pi * Z / L)
    print(f"  r₀={rt:.2f}: |u₁|_max={np.abs(u_test).max():.2f}, "
          f"peak_r={r[np.unravel_index(np.abs(u_test).argmax(), u_test.shape)[0]]:.3f}")

# Save IC for inspection
ic_data = {
    "r_target": r_target,
    "sigma_r": sigma_r,
    "amplitude": amplitude,
    "Nr": Nr, "Nz": Nz,
    "L": L,
    "u1_max": float(np.abs(u1).max()),
    "u1_peak_r": float(r[peak_idx[0]]),
    "u1_peak_z": float(z[peak_idx[1]]),
    "formula": "u1 = A * exp(-(r-r0)^2/sigma^2) * (1-r^2) * sin(2*pi*z/L)",
}
with open("ns_blowup/results/sniper_ic_design.json", "w") as f:
    json.dump(ic_data, f, indent=2)
print(f"\nSaved to ns_blowup/results/sniper_ic_design.json")

print(f"\n=== NEXT STEP ===")
print(f"Add this IC to sweep.py as init_sniper()")
print(f"Run at Nr=64 on GPU to verify Γ trajectory")
print(f"If Γ stays high → run at Nr=256")
