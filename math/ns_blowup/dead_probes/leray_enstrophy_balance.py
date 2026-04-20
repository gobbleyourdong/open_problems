"""
Leray-rescaled enstrophy balance from Nr=256 extended data.

In Leray coordinates, both S and νP scale as (T*-t)^{-2}.
If we define:
  S̃ = (T*-t)²·S    (rescaled stretching)
  P̃ = (T*-t)²·νP   (rescaled dissipation)

Then Γ = (S̃ - P̃)/(S̃ + P̃) — same formula, but S̃ and P̃ should be O(1).

Question: do S̃ and P̃ approach each other (S̃/P̃ → 1) or does S̃/P̃ have a floor?

Uses the Nr=64 data (has S and νP). Nr=256 only has Γ.
"""
import json
import numpy as np

# Nr=64 has S and νP
with open("ns_blowup/results/core_width_nr64.json") as f:
    data64 = [d for d in json.load(f) if d["t"] > 0 and d["om1"] > 10]

t = np.array([d["t"] for d in data64])
gamma = np.array([d["gamma"] for d in data64])
S = np.array([d["S"] for d in data64])
nuP = np.array([d["nuP"] for d in data64])
omega = np.array([d["om1"] for d in data64])

# Estimate T* from Nr=64 data
inv_om = 1.0 / omega[-10:]
c = np.polyfit(t[-10:], inv_om, 1)
T_star = -c[1] / c[0]
if T_star <= t[-1]:
    T_star = t[-1] * 1.001
print(f"Estimated T* = {T_star:.6f}")

tau = T_star - t  # time to singularity

# Leray-rescaled quantities
S_tilde = tau**2 * S
P_tilde = tau**2 * nuP
omega_tilde = tau * omega  # should be O(1)

# Ratio in Leray frame
ratio_leray = S_tilde / (P_tilde + 1e-30)

print(f"\n=== LERAY-RESCALED ENSTROPHY BALANCE (Nr=64) ===")
print(f"\n{'Phase':<15} {'S̃ mean':>12} {'P̃ mean':>12} {'S̃/P̃':>8} {'Ω̃ mean':>8}")

# Split into phases by Γ
phases = [
    ("Early (Γ>0.8)", gamma > 0.8),
    ("Drop (0.3-0.8)", (gamma > 0.3) & (gamma <= 0.8)),
    ("Trough (<0.3)", (gamma <= 0.3) & (t < t[np.argmin(gamma)])),
    ("At minimum", abs(gamma - gamma.min()) < 0.01),
    ("Rebound", (gamma <= 0.5) & (t > t[np.argmin(gamma)])),
    ("Late (Γ>0.8)", (gamma > 0.8) & (t > t[np.argmin(gamma)])),
]

for name, mask in phases:
    if mask.sum() > 0:
        print(f"{name:<15} {S_tilde[mask].mean():>12.4e} {P_tilde[mask].mean():>12.4e} "
              f"{ratio_leray[mask].mean():>8.2f} {omega_tilde[mask].mean():>8.2f}")

# The key question: does S̃/P̃ have structure or is it noisy?
print(f"\n=== S̃/P̃ TRAJECTORY ===")
print(f"{'t':>8} {'Γ':>7} {'S̃':>12} {'P̃':>12} {'S̃/P̃':>8} {'Ω̃':>8}")
for i in range(0, len(data64), max(1, len(data64)//25)):
    print(f"{t[i]:8.6f} {gamma[i]:7.4f} {S_tilde[i]:12.4e} {P_tilde[i]:12.4e} "
          f"{ratio_leray[i]:8.2f} {omega_tilde[i]:8.2f}")

# Check: is S̃-P̃ approximately constant? (would mean dE/dt ~ const in Leray frame)
dE_tilde = S_tilde - P_tilde
print(f"\n=== RESCALED ENSTROPHY GROWTH S̃-P̃ ===")
print(f"Range: [{dE_tilde.min():.4e}, {dE_tilde.max():.4e}]")
print(f"At Γ_min: {dE_tilde[np.argmin(gamma)]:.4e}")
print(f"S̃-P̃ > 0 always: {np.all(dE_tilde > 0)}")

# Check if S̃ and P̃ individually stabilize
trough_mask = gamma < 0.3
if trough_mask.sum() > 3:
    print(f"\n=== TROUGH STABILITY ===")
    print(f"S̃ in trough: mean={S_tilde[trough_mask].mean():.4e}, std={S_tilde[trough_mask].std():.4e}, "
          f"cv={S_tilde[trough_mask].std()/S_tilde[trough_mask].mean():.2f}")
    print(f"P̃ in trough: mean={P_tilde[trough_mask].mean():.4e}, std={P_tilde[trough_mask].std():.4e}, "
          f"cv={P_tilde[trough_mask].std()/P_tilde[trough_mask].mean():.2f}")
    print(f"Ω̃ in trough: mean={omega_tilde[trough_mask].mean():.2f}, std={omega_tilde[trough_mask].std():.2f}")

# Save
results = {
    "T_star": float(T_star),
    "S_tilde_at_gamma_min": float(S_tilde[np.argmin(gamma)]),
    "P_tilde_at_gamma_min": float(P_tilde[np.argmin(gamma)]),
    "ratio_at_gamma_min": float(ratio_leray[np.argmin(gamma)]),
    "omega_tilde_at_gamma_min": float(omega_tilde[np.argmin(gamma)]),
    "dE_tilde_always_positive": bool(np.all(dE_tilde > 0)),
}
with open("ns_blowup/results/leray_enstrophy_balance.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to ns_blowup/results/leray_enstrophy_balance.json")
