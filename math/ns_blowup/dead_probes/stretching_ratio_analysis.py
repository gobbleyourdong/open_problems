"""
S/νP ratio analysis — is stretching STRUCTURALLY bounded above dissipation?

Key question: does S/νP have a lower bound > 1 that persists across the
entire trajectory? If S > νP ALWAYS (even at Γ_min), then Γ > 0 always,
and enstrophy grows monotonically → BKM integral diverges → blowup.

This is the simplest possible proof path:
  If S(t) > νP(t) for all t → dE/dt > 0 → E → ∞ → blowup.

Uses Nr=64 core width data (has S and νP at every timestep).
"""
import json
import numpy as np

with open("ns_blowup/results/core_width_nr64.json") as f:
    data = json.load(f)

# Filter valid data
data = [d for d in data if d["t"] > 0 and d["om1"] > 10]

t = np.array([d["t"] for d in data])
gamma = np.array([d["gamma"] for d in data])
S = np.array([d["S"] for d in data])
nuP = np.array([d["nuP"] for d in data])
omega = np.array([d["om1"] for d in data])
R_rms = np.array([d["R_rms"] for d in data])
alpha = np.array([d["alpha_max"] for d in data])

# S/νP ratio
ratio = S / (nuP + 1e-30)

print("=== S/νP RATIO ANALYSIS (Nr=64, ν=1e-4) ===\n")
print(f"Total timesteps: {len(data)}")
print(f"S/νP range: [{ratio.min():.4f}, {ratio.max():.4f}]")
print(f"S/νP at Γ_min: {ratio[np.argmin(gamma)]:.4f}")
print(f"S > νP at ALL timesteps: {np.all(ratio > 1)}")
print(f"Min S/νP: {ratio.min():.4f} at t={t[np.argmin(ratio)]:.6f}")

# The minimum S/νP should correspond to Γ_min
# Γ = (S - νP)/(S + νP), so S/νP = (1+Γ)/(1-Γ)
gamma_min = gamma.min()
predicted_ratio = (1 + gamma_min) / (1 - gamma_min)
actual_ratio = ratio[np.argmin(gamma)]
print(f"\nΓ_min = {gamma_min:.4f}")
print(f"Predicted S/νP from Γ_min: (1+Γ)/(1-Γ) = {predicted_ratio:.4f}")
print(f"Actual S/νP at Γ_min: {actual_ratio:.4f}")
print(f"Match: {'YES' if abs(predicted_ratio - actual_ratio) < 0.01 else 'NO'}")

# Rate of enstrophy growth: dE/dt = S - νP
dE = S - nuP
print(f"\n=== ENSTROPHY GROWTH ===")
print(f"dE/dt = S - νP range: [{dE.min():.4e}, {dE.max():.4e}]")
print(f"dE/dt > 0 at ALL timesteps: {np.all(dE > 0)}")
print(f"dE/dt at Γ_min: {dE[np.argmin(gamma)]:.4e}")

# If dE/dt > 0 always, enstrophy is monotonically increasing
# Cumulative enstrophy growth
dt_arr = np.diff(t)
E_growth = np.cumsum(dE[:-1] * dt_arr)
print(f"\nCumulative enstrophy growth: {E_growth[-1]:.4e}")

# Check if S/νP shows any trend toward 1 (would mean approaching balance)
# Split into phases
n = len(ratio)
phase1 = ratio[:n//3]      # early
phase2 = ratio[n//3:2*n//3]  # trough
phase3 = ratio[2*n//3:]     # rebound

print(f"\n=== S/νP BY PHASE ===")
print(f"Early (pre-trough):  mean={phase1.mean():.4f}, min={phase1.min():.4f}")
print(f"Trough:              mean={phase2.mean():.4f}, min={phase2.min():.4f}")
print(f"Rebound:             mean={phase3.mean():.4f}, min={phase3.min():.4f}")

# The key structural question: does the ratio approach 1 or have a hard floor?
# Fit ratio vs time in the trough
trough_mask = gamma < 0.3
if trough_mask.sum() > 5:
    trough_t = t[trough_mask]
    trough_ratio = ratio[trough_mask]

    # Is the ratio still declining at Γ_min, or has it floored?
    # Check derivative of ratio near minimum
    min_idx = np.argmin(gamma)
    if min_idx > 2 and min_idx < len(ratio) - 2:
        d_ratio = np.gradient(ratio, t)
        print(f"\n=== RATIO DERIVATIVE NEAR Γ_MIN ===")
        for i in range(max(0, min_idx-3), min(len(ratio), min_idx+4)):
            print(f"  t={t[i]:.6f} Γ={gamma[i]:.4f} S/νP={ratio[i]:.4f} d(S/νP)/dt={d_ratio[i]:.2e}")

# Theoretical minimum: for Γ > 0, S/νP > 1 always
# At Γ=0.12, S/νP = (1.12)/(0.88) = 1.273
# At Γ=0.05, S/νP = (1.05)/(0.95) = 1.105
# At Γ=0, S/νP = 1 (exact balance)
print(f"\n=== CRITICAL QUESTION ===")
print(f"Does S/νP → 1 (balance) or floor above 1?")
print(f"Current trajectory: S/νP minimum = {ratio.min():.4f}")
print(f"  If Nr=256 shows S/νP → 1 (Γ→0): viscosity catches stretching, no rebound, no blowup")
print(f"  If Nr=256 shows S/νP floors > 1: stretching ALWAYS wins, blowup inevitable")
print(f"  Nr=64 showed floor at S/νP = {ratio.min():.4f} (Γ={gamma_min:.4f})")
print(f"  Nr=256 currently at Γ=0.111 → S/νP = {(1+0.111)/(1-0.111):.4f}")

# Save
results = {
    "min_S_over_nuP": float(ratio.min()),
    "S_over_nuP_at_gamma_min": float(ratio[np.argmin(gamma)]),
    "gamma_min": float(gamma_min),
    "dE_always_positive": bool(np.all(dE > 0)),
    "dE_at_gamma_min": float(dE[np.argmin(gamma)]),
    "predicted_ratio_from_gamma": float(predicted_ratio),
}

with open("ns_blowup/results/stretching_ratio_analysis.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to ns_blowup/results/stretching_ratio_analysis.json")
