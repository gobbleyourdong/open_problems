"""
Leray transform on Nr=256 field checkpoint.
Examine the spatial profile of u₁ and ω₁ at step 5000 (Γ≈0.56, pre-trough).

Questions:
1. What does the vorticity profile look like in physical coordinates?
2. How many modes dominate the radial structure? (rank for CAP)
3. Where is the vorticity concentrated? (core width from actual field)
"""
import torch
import numpy as np
import json

# Load checkpoint
ckpt = torch.load("ns_blowup/results/h200_sync/checkpoint_nr256_step5000.pt",
                   map_location="cpu", weights_only=False)

u1 = ckpt["u1"].numpy()
omega1 = ckpt["omega1"].numpy()
t_val = ckpt["t"]
step = ckpt["step"]

Nr, Nz = u1.shape[0] - 1, u1.shape[1] - 1  # Chebyshev points

print(f"=== Nr=256 FIELD SNAPSHOT (step {step}, t={t_val:.6f}) ===")
print(f"u1 shape: {u1.shape} (Nr+1={Nr+1}, Nz+1={Nz+1})")
print(f"|u1|_max = {np.abs(u1).max():.4f}")
print(f"|ω1|_max = {np.abs(omega1).max():.4f}")

# Chebyshev points in r: r_j = cos(j*pi/Nr), j=0..Nr
# Index 0 = r=1 (wall), index Nr = r=0 (axis)
r = np.cos(np.arange(Nr+1) * np.pi / Nr)

# z grid: uniform, z_k = k*Lz/Nz, k=0..Nz
Lz = 1.0/(6.0*4.0)  # L/4 for Luo-Hou
z = np.linspace(0, Lz, Nz+1)

print(f"\nr range: [{r.min():.4f}, {r.max():.4f}] (index 0=wall, {Nr}=axis)")
print(f"z range: [{z.min():.6f}, {z.max():.6f}]")

# Where is vorticity concentrated?
omega_abs = np.abs(omega1)
peak_idx = np.unravel_index(omega_abs.argmax(), omega_abs.shape)
print(f"\n|ω1| peak at: r_idx={peak_idx[0]} (r={r[peak_idx[0]]:.4f}), z_idx={peak_idx[1]} (z={z[peak_idx[1]]:.6f})")
print(f"|ω1| peak value: {omega1[peak_idx[0], peak_idx[1]]:.4f}")

# Radial profile at z of peak
z_peak_idx = peak_idx[1]
omega_r_profile = omega1[:, z_peak_idx]
u1_r_profile = u1[:, z_peak_idx]

print(f"\n=== RADIAL PROFILE at z={z[z_peak_idx]:.6f} ===")
print(f"{'r':>8} {'ω1':>12} {'u1':>12}")
for i in range(0, Nr+1, max(1, Nr//20)):
    print(f"{r[i]:8.4f} {omega_r_profile[i]:12.4f} {u1_r_profile[i]:12.4f}")

# Spectral analysis: Chebyshev coefficients of ω1 radial profile
# The Chebyshev transform of f(r_j) gives coefficients a_k
# Using DCT-I (discrete cosine transform)
from numpy.fft import rfft

# For Chebyshev coefficients: use DCT
omega_cheb = np.zeros(Nr+1)
for k in range(Nr+1):
    omega_cheb[k] = np.sum(omega_r_profile * np.cos(k * np.arange(Nr+1) * np.pi / Nr))
    omega_cheb[k] *= 2.0 / Nr
    if k == 0 or k == Nr:
        omega_cheb[k] *= 0.5

# How many modes are significant?
omega_cheb_abs = np.abs(omega_cheb)
total_energy = np.sum(omega_cheb_abs**2)
cumulative = np.cumsum(omega_cheb_abs**2) / total_energy

print(f"\n=== CHEBYSHEV SPECTRAL ANALYSIS (radial) ===")
print(f"Total modes: {Nr+1}")

for threshold in [0.90, 0.95, 0.99, 0.999]:
    n_modes = np.searchsorted(cumulative, threshold) + 1
    print(f"  {threshold*100:.1f}% energy in {n_modes} modes")

# Energy in first 50 modes (Chen-Hou used rank<50)
e50 = cumulative[49] if Nr >= 49 else cumulative[-1]
print(f"  First 50 modes capture {e50*100:.2f}% of energy")

# Decay rate of coefficients
print(f"\n=== COEFFICIENT DECAY ===")
print(f"{'Mode':>6} {'|a_k|':>12} {'Cumulative%':>12}")
for k in [0, 1, 2, 5, 10, 20, 50, 100, 150, 200, 250]:
    if k <= Nr:
        print(f"{k:6d} {omega_cheb_abs[k]:12.4e} {cumulative[k]*100:12.4f}%")

# Z-direction: Fourier coefficients
omega_z_profile = omega1[peak_idx[0], :]
omega_fft = np.abs(np.fft.rfft(omega_z_profile))
print(f"\n=== FOURIER ANALYSIS (z-direction, at r={r[peak_idx[0]]:.4f}) ===")
print(f"Total z-modes: {len(omega_fft)}")
z_total = np.sum(omega_fft**2)
z_cum = np.cumsum(omega_fft**2) / z_total
for threshold in [0.90, 0.95, 0.99]:
    n = np.searchsorted(z_cum, threshold) + 1
    print(f"  {threshold*100:.1f}% energy in {n} z-modes")

# Save summary
results = {
    "step": int(step), "t": float(t_val),
    "Nr": Nr, "Nz": Nz,
    "omega_peak_r": float(r[peak_idx[0]]),
    "omega_peak_z": float(z[peak_idx[1]]),
    "omega_peak_value": float(omega1[peak_idx[0], peak_idx[1]]),
    "modes_90pct": int(np.searchsorted(cumulative, 0.90) + 1),
    "modes_95pct": int(np.searchsorted(cumulative, 0.95) + 1),
    "modes_99pct": int(np.searchsorted(cumulative, 0.99) + 1),
    "first_50_modes_pct": float(e50 * 100),
}
with open("ns_blowup/results/field_snapshot_step5000.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to ns_blowup/results/field_snapshot_step5000.json")
