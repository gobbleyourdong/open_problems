"""
Spectral degradation trend analysis on 20K extended Nr=256 data.
Questions:
1. At what Γ does spectral ratio hit MARGINAL (0.01)?
2. Is spectral degradation exponential, polynomial, or something else?
3. Predict: will Nr=256 become under-resolved before the rebound (if any)?
"""
import json
import numpy as np

# Load the 20K extended data
with open("ns_blowup/results/h200_sync/gamma_nr256_extended.json") as f:
    data = json.load(f)

data = [d for d in data if d["step"] > 0]
steps = np.array([d["step"] for d in data])
t_arr = np.array([d["t"] for d in data])
gamma = np.array([d["gamma"] for d in data])
spectral = np.array([d["spectral"] for d in data])
omega = np.array([d["om1"] for d in data])

print(f"=== Nr=256 EXTENDED RUN — SPECTRAL ANALYSIS ===\n")
print(f"Steps: {steps[0]} to {steps[-1]} ({len(data)} entries)")
print(f"Γ range: [{gamma.min():.4f}, {gamma.max():.4f}]")
print(f"Spectral range: [{spectral.min():.6f}, {spectral.max():.6f}]")
print(f"|ω| range: [{omega.min():.2e}, {omega.max():.2e}]")

# Phase analysis
# Phase 1: Γ dropping (pre-trough)
# Phase 2: Γ in trough (< 0.3)
# Phase 3: new territory (past original 8K endpoint)

phase1_mask = gamma > 0.3
phase2_mask = (gamma <= 0.3) & (steps <= 8000)
phase3_mask = steps > 8000

print(f"\n--- Phase 1 (Γ > 0.3, pre-trough): {phase1_mask.sum()} points ---")
if phase1_mask.sum() > 0:
    print(f"  Spectral: [{spectral[phase1_mask].min():.6f}, {spectral[phase1_mask].max():.6f}]")
    print(f"  Mean: {spectral[phase1_mask].mean():.6f}")

print(f"\n--- Phase 2 (Γ ≤ 0.3, original trough): {phase2_mask.sum()} points ---")
if phase2_mask.sum() > 0:
    print(f"  Spectral: [{spectral[phase2_mask].min():.6f}, {spectral[phase2_mask].max():.6f}]")
    print(f"  Mean: {spectral[phase2_mask].mean():.6f}")

print(f"\n--- Phase 3 (new territory, step > 8K): {phase3_mask.sum()} points ---")
if phase3_mask.sum() > 0:
    print(f"  Spectral: [{spectral[phase3_mask].min():.6f}, {spectral[phase3_mask].max():.6f}]")
    print(f"  Γ range: [{gamma[phase3_mask].min():.4f}, {gamma[phase3_mask].max():.4f}]")

# Spectral trend in new territory
new_steps = steps[phase3_mask]
new_spec = spectral[phase3_mask]
new_gamma = gamma[phase3_mask]

if len(new_steps) > 5:
    # Fit log(spectral) vs step — exponential growth?
    log_spec = np.log(new_spec + 1e-30)
    coeffs_exp = np.polyfit(new_steps, log_spec, 1)
    doubling_steps = np.log(2) / coeffs_exp[0] if coeffs_exp[0] > 0 else float('inf')

    # Fit spectral vs Γ — what's the relationship?
    coeffs_sg = np.polyfit(new_gamma, new_spec, 2)

    # Predict when spectral hits 0.01 (MARGINAL)
    # From exponential fit
    if coeffs_exp[0] > 0:
        step_marginal = (np.log(0.01) - coeffs_exp[1]) / coeffs_exp[0]
        # What Γ at that step? Extrapolate Γ trend
        coeffs_gamma = np.polyfit(new_steps, new_gamma, 1)
        gamma_at_marginal = np.polyval(coeffs_gamma, step_marginal)
    else:
        step_marginal = float('inf')
        gamma_at_marginal = float('nan')

    print(f"\n=== SPECTRAL TREND (new territory) ===")
    print(f"Exponential fit: spec ~ exp({coeffs_exp[0]:.6f} * step)")
    print(f"Doubling every {doubling_steps:.0f} steps")
    print(f"Predicted MARGINAL (spec=0.01) at step ~{step_marginal:.0f}")
    print(f"Predicted Γ at MARGINAL: ~{gamma_at_marginal:.4f}")

    # Γ trend
    print(f"\nΓ linear trend: Γ = {coeffs_gamma[0]:.8f} * step + {coeffs_gamma[1]:.4f}")
    print(f"Γ drops by {-coeffs_gamma[0]*200:.4f} per log entry")
    gamma_zero_step = -coeffs_gamma[1] / coeffs_gamma[0] if coeffs_gamma[0] < 0 else float('inf')
    print(f"Predicted Γ=0 at step ~{gamma_zero_step:.0f}")

    # Will spectral degrade before Γ reaches zero?
    print(f"\n=== CRITICAL PREDICTION ===")
    if step_marginal < gamma_zero_step:
        print(f"Spectral hits MARGINAL (step {step_marginal:.0f}) BEFORE Γ=0 (step {gamma_zero_step:.0f})")
        print(f"→ Resolution will degrade before we can see if Γ reaches zero")
        print(f"→ Need Nr=512 to resolve the true floor")
    else:
        print(f"Γ reaches zero (step {gamma_zero_step:.0f}) BEFORE spectral degrades (step {step_marginal:.0f})")
        print(f"→ Nr=256 is sufficient to see the full picture")

# Print trajectory table for the last 20 entries
print(f"\n=== LAST 20 ENTRIES ===")
print(f"{'Step':>6} {'Γ':>8} {'Spec':>10} {'|ω|':>10}")
for d in data[-20:]:
    s = "OK" if d["spectral"] < 0.01 else "MARG" if d["spectral"] < 0.1 else "UNDER"
    print(f"{d['step']:6d} {d['gamma']:8.4f} {d['spectral']:10.6f} {d['om1']:10.2e} [{s}]")

# Save
results = {
    "final_gamma": float(gamma[-1]),
    "final_spectral": float(spectral[-1]),
    "spectral_doubling_steps": float(doubling_steps) if 'doubling_steps' in dir() else None,
    "predicted_marginal_step": float(step_marginal) if 'step_marginal' in dir() else None,
    "predicted_gamma_at_marginal": float(gamma_at_marginal) if 'gamma_at_marginal' in dir() else None,
    "predicted_gamma_zero_step": float(gamma_zero_step) if 'gamma_zero_step' in dir() else None,
}
with open("ns_blowup/results/spectral_trend_nr256.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to ns_blowup/results/spectral_trend_nr256.json")
