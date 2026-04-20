"""
Leray coordinate transform on Nr=64 trough data.
Question: does the Γ trajectory look simpler in Leray coordinates?

Leray scaling:
  ξ = r / √(T*-t)        (rescaled radius)
  τ = -ln(T*-t)           (log-time)
  Rescaled vorticity: Ω = (T*-t) · ω

We don't have the spatial fields from Nr=64, but we have the scalar
trajectory data. We can transform the time axis to τ and see if the
Γ oscillation looks periodic in log-time.

Also compute: does S and νP have cleaner scaling in Leray coordinates?
"""
import json
import numpy as np

# Load Nr=64 core width diagnostic data (has S, nuP, gamma, etc.)
with open("ns_blowup/results/core_width_nr64.json") as f:
    data = json.load(f)

# Filter out t=0
data = [d for d in data if d["t"] > 0 and d["om1"] > 10]

t_arr = np.array([d["t"] for d in data])
gamma_arr = np.array([d["gamma"] for d in data])
omega_arr = np.array([d["om1"] for d in data])
S_arr = np.array([d["S"] for d in data])
nuP_arr = np.array([d["nuP"] for d in data])
R_arr = np.array([d["R_rms"] for d in data])
alpha_arr = np.array([d["alpha_max"] for d in data])

# We need T* — the blowup time for Nr=64 with ν=1e-4
# From memory: T*(ν=1e-4) = 0.00675 on A100, but Nr=64 Spark will be different
# Let's estimate from the data — find where |ω| diverges
# Use last 10 points to extrapolate
late = data[-10:]
t_late = np.array([d["t"] for d in late])
om_late = np.array([d["om1"] for d in late])

# Fit 1/|ω| vs t to find T* (zero crossing)
inv_om = 1.0 / om_late
coeffs_tstar = np.polyfit(t_late, inv_om, 1)
T_star = -coeffs_tstar[1] / coeffs_tstar[0]
print(f"Estimated T* from 1/|ω| extrapolation: {T_star:.6f}")
print(f"Last data point: t={t_arr[-1]:.6f}, |ω|={omega_arr[-1]:.2e}")
print(f"Time remaining: T*-t = {T_star - t_arr[-1]:.6f}")

if T_star <= t_arr[-1]:
    print("WARNING: T* estimate is before last data point. Using T*=t_last*1.001")
    T_star = t_arr[-1] * 1.001

# Leray transform
tau_arr = -np.log(T_star - t_arr)  # log-time
tau_remaining = T_star - t_arr     # T* - t

print(f"\nτ range: [{tau_arr.min():.2f}, {tau_arr.max():.2f}]")
print(f"(T*-t) range: [{tau_remaining.min():.6f}, {tau_remaining.max():.6f}]")

# Rescaled quantities in Leray frame
omega_rescaled = tau_remaining * omega_arr  # Ω = (T*-t)·ω — should be O(1) if self-similar
S_rescaled = tau_remaining**2 * S_arr       # S scales as (T*-t)^{-2} in Leray
nuP_rescaled = tau_remaining**2 * nuP_arr   # νP scales as (T*-t)^{-2} in Leray

print(f"\n=== Leray-rescaled quantities ===")
print(f"Ω = (T*-t)·|ω| range: [{omega_rescaled.min():.4f}, {omega_rescaled.max():.4f}]")
print(f"  Is Ω approximately constant? std/mean = {omega_rescaled.std()/omega_rescaled.mean():.4f}")

print(f"\n(T*-t)²·S range: [{S_rescaled.min():.4e}, {S_rescaled.max():.4e}]")
print(f"(T*-t)²·νP range: [{nuP_rescaled.min():.4e}, {nuP_rescaled.max():.4e}]")

# Check if Γ looks periodic in τ
# Find the trough region
trough_mask = gamma_arr < 0.5
trough_tau = tau_arr[trough_mask]
trough_gamma = gamma_arr[trough_mask]

print(f"\n=== Γ in Leray coordinates ===")
print(f"Trough (Γ<0.5) spans τ ∈ [{trough_tau.min():.2f}, {trough_tau.max():.2f}]")
print(f"Trough width in τ: {trough_tau.max() - trough_tau.min():.2f}")

# Check if the Γ minimum and rebound have a characteristic τ-scale
gamma_min_idx = np.argmin(gamma_arr)
print(f"\nΓ minimum at τ = {tau_arr[gamma_min_idx]:.2f}")
print(f"Γ minimum value: {gamma_arr[gamma_min_idx]:.4f}")

# Look for periodicity: compute dΓ/dτ
dgamma_dtau = np.gradient(gamma_arr, tau_arr)
print(f"\ndΓ/dτ at minimum: {dgamma_dtau[gamma_min_idx]:.4f} (should be ~0)")
print(f"dΓ/dτ range: [{dgamma_dtau.min():.4f}, {dgamma_dtau.max():.4f}]")

# Check ω scaling: does |ω| ~ C/(T*-t)^γ ?
# In log: ln|ω| = -γ·ln(T*-t) + const = γ·τ + const
# So slope of ln|ω| vs τ gives γ
log_omega = np.log(omega_arr)
# Fit in the trough region where blowup is developing
late_mask = tau_arr > tau_arr.mean()
coeffs_gamma = np.polyfit(tau_arr[late_mask], log_omega[late_mask], 1)
gamma_exponent = coeffs_gamma[0]
print(f"\n=== Blowup exponent from Leray coordinates ===")
print(f"|ω| ~ exp(γ·τ) → γ = {gamma_exponent:.4f}")
print(f"Equivalently: |ω| ~ (T*-t)^(-{gamma_exponent:.4f})")
print(f"(Hou 2022 expects γ≈1 with log correction)")

# Check if log correction improves fit
# |ω| ~ τ/(T*-t) = τ·exp(τ) in Leray coords
# ln|ω| = ln(τ) + τ
log_omega_corrected = log_omega - np.log(tau_arr)  # remove log correction
coeffs_corrected = np.polyfit(tau_arr[late_mask], log_omega_corrected[late_mask], 1)
gamma_corrected = coeffs_corrected[0]

r2_plain = 1 - np.sum((log_omega[late_mask] - np.polyval(coeffs_gamma, tau_arr[late_mask]))**2) / \
           np.sum((log_omega[late_mask] - log_omega[late_mask].mean())**2)
r2_corrected = 1 - np.sum((log_omega_corrected[late_mask] - np.polyval(coeffs_corrected, tau_arr[late_mask]))**2) / \
               np.sum((log_omega_corrected[late_mask] - log_omega_corrected[late_mask].mean())**2)

print(f"\nPlain power law: γ={gamma_exponent:.4f}, R²={r2_plain:.6f}")
print(f"Log-corrected:   γ={gamma_corrected:.4f}, R²={r2_corrected:.6f}")
print(f"Log correction {'IMPROVES' if r2_corrected > r2_plain else 'does NOT improve'} the fit")

# Save results
results = {
    "T_star_estimate": float(T_star),
    "tau_range": [float(tau_arr.min()), float(tau_arr.max())],
    "trough_tau_width": float(trough_tau.max() - trough_tau.min()),
    "gamma_min_tau": float(tau_arr[gamma_min_idx]),
    "gamma_min_value": float(gamma_arr[gamma_min_idx]),
    "blowup_exponent_plain": float(gamma_exponent),
    "blowup_exponent_log_corrected": float(gamma_corrected),
    "r2_plain": float(r2_plain),
    "r2_log_corrected": float(r2_corrected),
    "omega_rescaled_variation": float(omega_rescaled.std()/omega_rescaled.mean()),
}

with open("ns_blowup/results/leray_transform_nr64.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved to ns_blowup/results/leray_transform_nr64.json")

# Print the full trajectory in Leray coordinates for reference
print(f"\n=== Full trajectory (Leray coords) ===")
print(f"{'τ':>8} {'Γ':>8} {'Ω=(T*-t)ω':>12} {'(T*-t)²S':>12} {'(T*-t)²νP':>12}")
for i in range(0, len(data), max(1, len(data)//20)):
    print(f"{tau_arr[i]:8.2f} {gamma_arr[i]:8.4f} {omega_rescaled[i]:12.4f} "
          f"{S_rescaled[i]:12.4e} {nuP_rescaled[i]:12.4e}")
