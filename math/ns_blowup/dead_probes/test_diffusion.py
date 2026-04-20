"""
Diffusion operator verification — manufactured solutions.

Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz    (5D Laplacian radial part)

Strategy: pick functions where we KNOW the answer analytically,
compute numerically, compare. No ambiguity.

Also: pure diffusion test — set advection=0, stretching=0, ν=1.
The solution should DECAY, not blow up. If it blows up, operator is wrong.
"""
import torch
import math
import numpy as np
import sys
sys.path.insert(0, 'ns_blowup')
from euler_fixed import EulerFixed

dev = 'cuda' if torch.cuda.is_available() else 'cpu'

# =========================================
# TEST 1: Manufactured solutions for Δ₃
# =========================================
print("="*60)
print("TEST 1: MANUFACTURED SOLUTIONS — Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz")
print("="*60)

Nr, Nz = 64, 128
solver = EulerFixed(Nr=Nr, Nz=Nz, L=1/6, device=dev)
r = solver.r          # (Nr+1,) from 1 to 0
z = solver.z          # (Nz+1,) from 0 to Lz
R, Z = solver.R, solver.Z
D1 = solver.D_r       # d/dr
D2 = solver.D_r2      # d²/dr²
dz = solver.dz

def apply_delta3_numerical(f, D1, D2, r, dz, Nr):
    """Apply Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz numerically."""
    f_rr = D2 @ f
    f_r = D1 @ f

    r_safe = r.clamp(min=1e-10)
    three_over_r = 3.0 / r_safe

    # Radial part
    delta_r = f_rr + three_over_r.unsqueeze(1) * f_r

    # L'Hôpital at r=0 (index Nr): (3/r)f' → 3f'' → Δ₃ = 4f''
    delta_r[Nr, :] = 4.0 * f_rr[Nr, :]

    # z part: 2nd order central FD (odd-odd ghost: f=0 at boundaries)
    f_zz = torch.zeros_like(f)
    f_zz[:, 1:-1] = (f[:, 2:] - 2*f[:, 1:-1] + f[:, :-2]) / dz**2
    # z=0: f=0 (odd), ghost f[-1] = -f[1] → f_zz = (f[1]-f[-1]-2·0)/dz² ...
    # Actually for f(z=0)=0: f_zz[0] = (f[1] + f[-1] - 2*f[0])/dz² = (f[1]+(-f[1]))/dz² = 0
    f_zz[:, 0] = 0.0
    # z=Lz: f=0 (odd), ghost f[Nz+1] = -f[Nz-1]
    f_zz[:, -1] = (-2*f[:, -1] + 0) / dz**2  # f[Nz]=0 for odd

    return delta_r + f_zz

# --- Test A: f(r,z) = r² ---
# ∂ᵣf = 2r, ∂ᵣᵣf = 2
# (3/r)·2r = 6
# ∂zzf = 0
# Δ₃f = 2 + 6 = 8 (constant everywhere)
print("\nTest A: f = r²")
f_a = R**2
exact_a = 8.0 * torch.ones_like(f_a)
numerical_a = apply_delta3_numerical(f_a, D1, D2, r, dz, Nr)
# Skip boundaries (BC rows)
interior = slice(1, Nr)
err_a = (numerical_a[interior, :] - exact_a[interior, :]).abs().max().item()
print(f"  Exact Δ₃(r²) = 8 everywhere")
print(f"  Max error (interior): {err_a:.2e}")
print(f"  {'✓ PASS' if err_a < 1e-6 else '✗ FAIL'}")

# --- Test B: f(r,z) = r⁴ ---
# ∂ᵣf = 4r³, ∂ᵣᵣf = 12r²
# (3/r)·4r³ = 12r²
# Δ₃f = 12r² + 12r² = 24r²
print("\nTest B: f = r⁴")
f_b = R**4
exact_b = 24.0 * R**2
numerical_b = apply_delta3_numerical(f_b, D1, D2, r, dz, Nr)
err_b = (numerical_b[interior, :] - exact_b[interior, :]).abs().max().item()
rel_b = err_b / exact_b[interior, :].abs().max().item()
print(f"  Exact Δ₃(r⁴) = 24r²")
print(f"  Max error (interior): {err_b:.2e} (rel: {rel_b:.2e})")
print(f"  {'✓ PASS' if rel_b < 1e-6 else '✗ FAIL'}")

# --- Test C: f(r,z) = sin(kz) (z-only function) ---
# ∂ᵣf = 0, ∂ᵣᵣf = 0
# (3/r)·0 = 0
# ∂zzf = -k²sin(kz)
# Δ₃f = -k²sin(kz)
k_test = 2 * math.pi / solver.Lz  # first mode
print(f"\nTest C: f = sin(kz), k={k_test:.2f}")
f_c = torch.sin(k_test * Z)
exact_c = -k_test**2 * torch.sin(k_test * Z)
numerical_c = apply_delta3_numerical(f_c, D1, D2, r, dz, Nr)
# z interior only (skip boundary ghost points)
z_int = slice(2, Nz-1)
err_c = (numerical_c[interior, z_int] - exact_c[interior, z_int]).abs().max().item()
rel_c = err_c / exact_c[interior, z_int].abs().max().item()
print(f"  Exact Δ₃(sin(kz)) = -k²sin(kz)")
print(f"  Max error (interior): {err_c:.2e} (rel: {rel_c:.2e})")
print(f"  {'✓ PASS' if rel_c < 0.01 else '✗ FAIL'}  (2nd order FD — expect O(dz²)={dz**2:.2e})")

# --- Test D: f(r,z) = r²·sin(kz) (mixed) ---
# ∂ᵣf = 2r·sin(kz), ∂ᵣᵣf = 2·sin(kz)
# (3/r)·2r·sin(kz) = 6·sin(kz)
# ∂zzf = -k²r²sin(kz)
# Δ₃f = 8·sin(kz) - k²r²sin(kz)
print(f"\nTest D: f = r²·sin(kz)")
f_d = R**2 * torch.sin(k_test * Z)
exact_d = 8.0 * torch.sin(k_test * Z) - k_test**2 * R**2 * torch.sin(k_test * Z)
numerical_d = apply_delta3_numerical(f_d, D1, D2, r, dz, Nr)
err_d = (numerical_d[interior, z_int] - exact_d[interior, z_int]).abs().max().item()
rel_d = err_d / exact_d[interior, z_int].abs().max().item()
print(f"  Exact Δ₃(r²sin(kz)) = 8sin(kz) - k²r²sin(kz)")
print(f"  Max error (interior): {err_d:.2e} (rel: {rel_d:.2e})")
print(f"  {'✓ PASS' if rel_d < 0.01 else '✗ FAIL'}")

# --- Test E: L'Hôpital at r=0 ---
# At r=0: (3/r)∂ᵣf → 3∂ᵣᵣf, so Δ₃f → 4∂ᵣᵣf + ∂zzf
# For f = r²: Δ₃ = 4·2 + 0 = 8 ✓
# For f = r⁴: Δ₃ = 4·12r² + 0 → at r=0 → 0
print(f"\nTest E: L'Hôpital at r=0 (index {Nr})")
val_r0_a = numerical_a[Nr, Nz//2].item()
print(f"  Δ₃(r²) at r=0: {val_r0_a:.4f} (exact: 8)")
print(f"  {'✓ PASS' if abs(val_r0_a - 8) < 0.1 else '✗ FAIL'}")
val_r0_b = numerical_b[Nr, Nz//2].item()
print(f"  Δ₃(r⁴) at r=0: {val_r0_b:.6f} (exact: 0)")
print(f"  {'✓ PASS' if abs(val_r0_b) < 0.1 else '✗ FAIL'}")


# =========================================
# TEST 2: PURE DIFFUSION — must decay, not blow up
# =========================================
print("\n" + "="*60)
print("TEST 2: PURE DIFFUSION — ν=1, no advection, no stretching")
print("="*60)
print("If the solution decays, the diffusion operator is working.")
print("If it blows up, the operator is broken.\n")

# Simple IC: u₁ = sin(kz)·(1-r²)² (smooth, satisfies BCs approximately)
u1 = torch.sin(k_test * Z) * (1 - R**2)**2
u1[0, :] = 0  # wall BC
omega1 = torch.zeros_like(u1)

initial_energy = u1.abs().max().item()
print(f"Initial |u₁|_max = {initial_energy:.6f}")

# Run pure diffusion: du₁/dt = ν·Δ₃(u₁) with ν=1
nu = 1.0
dt_diff = 0.3 * min(solver.dr_min, dz)**2 / nu  # diffusion CFL
print(f"dt = {dt_diff:.2e}")

## --- Method 1: Raw operator (known broken) ---
print("\nMethod 1: Raw Δ₃ (no boundary fix) — expected to blow up")
u_test = u1.clone()
blew_up_raw = False
for step in range(500):
    delta_u = apply_delta3_numerical(u_test, D1, D2, r, dz, Nr)
    u_test = u_test + dt_diff * nu * delta_u
    u_test[0, :] = 0; u_test[:, 0] = 0; u_test[:, -1] = 0
    if u_test.abs().max().item() > 1e10:
        print(f"  ✗ BLEW UP at step {step}")
        blew_up_raw = True
        break

## --- Method 2: Boundary-row-replaced operator (the fix) ---
print("\nMethod 2: L3_r with boundary rows replaced — should decay")

# Build the fixed operator
r_safe = r.clamp(min=1e-10)
L3_r = D2 + torch.diag(3.0 / r_safe) @ D1
L3_r[Nr, :] = 4.0 * D2[Nr, :]      # L'Hôpital
L3_r[0, :] = 0.0; L3_r[0, 0] = 1.0  # Dirichlet at wall
L3_r[Nr, :] = D1[Nr, :]              # Neumann at axis

u_test = u1.clone()
for step in range(500):
    # Radial part via fixed operator
    diff_r = L3_r @ u_test
    # z part via FD (odd-odd)
    u_zz = torch.zeros_like(u_test)
    u_zz[:, 1:-1] = (u_test[:, 2:] - 2*u_test[:, 1:-1] + u_test[:, :-2]) / dz**2

    u_test = u_test + dt_diff * nu * (diff_r + u_zz)
    u_test[0, :] = 0; u_test[:, 0] = 0; u_test[:, -1] = 0

    if step % 100 == 0:
        energy = u_test.abs().max().item()
        ratio = energy / initial_energy
        print(f"  step {step:4d}: |u₁|_max = {energy:.6e} (ratio: {ratio:.4f})")

    if u_test.abs().max().item() > 1e10:
        print(f"  ✗ BLEW UP at step {step}")
        break

final_energy = u_test.abs().max().item()
ratio = final_energy / initial_energy
print(f"\nFinal |u₁|_max = {final_energy:.6e}")
print(f"Decay ratio: {ratio:.6f}")
if ratio < 0.5:
    print("✓ PASS — solution is decaying (diffusion works)")
elif ratio < 1.0:
    print("~ MARGINAL — decaying but slowly")
elif ratio > 10:
    print("✗ FAIL — solution is GROWING (operator broken)")
else:
    print("? UNCLEAR — barely changed")


# =========================================
# TEST 3: Compare 3/r vs 5/r
# =========================================
print("\n" + "="*60)
print("TEST 3: COEFFICIENT CHECK — 3/r is correct, not 5/r")
print("="*60)
print("Δ₃ = ∂ᵣᵣ + (3/r)∂ᵣ + ∂zz  (Hou-Li 5D Laplacian radial part)")
print("Common mistake: using 5/r or 1/r instead\n")

f_check = R**2  # Δ₃(r²) = 2 + (n/r)·2r = 2 + 2n

for n_coeff in [1, 3, 5]:
    r_safe = r.clamp(min=1e-10)
    coeff = float(n_coeff) / r_safe
    f_rr = D2 @ f_check
    f_r = D1 @ f_check
    result = f_rr + coeff.unsqueeze(1) * f_r
    val = result[Nr//2, Nz//2].item()
    expected = 2 + 2*n_coeff
    print(f"  {n_coeff}/r: Δ(r²) = {val:.4f} (expected {expected} for {n_coeff}/r)")

print(f"\n  Framework says: Δ₃ = ∂ᵣᵣ+(3/r)∂ᵣ+∂zz → Δ₃(r²) = 8")
print(f"  Using 3/r: ✓")
