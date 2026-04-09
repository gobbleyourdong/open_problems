"""
Γ asymptotic analysis — does Γ→0 linearly, or is there deceleration?

If Γ drops linearly → crosses zero → viscosity wins → regularity
If Γ decelerates (power law, exponential approach) → asymptotes to floor → blowup

This is the single most important question right now.
Uses the 20K extended data from Nr=256.
"""
import json
import numpy as np

with open("ns_blowup/results/h200_sync/gamma_nr256_extended.json") as f:
    data = [d for d in json.load(f) if d["step"] >= 8000]  # new territory only

steps = np.array([d["step"] for d in data])
gamma = np.array([d["gamma"] for d in data])
t_arr = np.array([d["t"] for d in data])

print(f"=== Γ ASYMPTOTIC ANALYSIS (Nr=256, step 8K-20K) ===\n")
print(f"Points: {len(data)}")
print(f"Γ range: [{gamma.min():.4f}, {gamma.max():.4f}]")
print(f"Step range: [{steps.min()}, {steps.max()}]")

# Model 1: Linear (Γ = a*step + b) → crosses zero
c_lin = np.polyfit(steps, gamma, 1)
gamma_zero_lin = -c_lin[1] / c_lin[0]
pred_lin = np.polyval(c_lin, steps)
r2_lin = 1 - np.sum((gamma - pred_lin)**2) / np.sum((gamma - gamma.mean())**2)

print(f"\n--- Model 1: LINEAR ---")
print(f"Γ = {c_lin[0]:.8f}·step + {c_lin[1]:.4f}")
print(f"R² = {r2_lin:.6f}")
print(f"Γ=0 at step {gamma_zero_lin:.0f}")

# Model 2: Exponential decay (Γ = a·exp(-b·step)) → asymptotes to 0 but never crosses
log_gamma = np.log(gamma)
c_exp = np.polyfit(steps, log_gamma, 1)
pred_exp = np.exp(np.polyval(c_exp, steps))
r2_exp = 1 - np.sum((gamma - pred_exp)**2) / np.sum((gamma - gamma.mean())**2)
halflife = np.log(2) / (-c_exp[0]) if c_exp[0] < 0 else float('inf')

print(f"\n--- Model 2: EXPONENTIAL DECAY ---")
print(f"Γ = {np.exp(c_exp[1]):.4f}·exp({c_exp[0]:.8f}·step)")
print(f"R² = {r2_exp:.6f}")
print(f"Half-life: {halflife:.0f} steps")
print(f"Γ at step 40K: {np.exp(c_exp[0]*40000 + c_exp[1]):.6f}")

# Model 3: Power law (Γ = a·(step_max - step)^p) → reaches zero at step_max
# Try Γ = a·(S - step)^p, find S by optimization
from scipy.optimize import minimize_scalar

def power_law_residual(S_guess):
    if S_guess <= steps.max():
        return 1e10
    tau = S_guess - steps
    log_tau = np.log(tau)
    log_g = np.log(gamma)
    c = np.polyfit(log_tau, log_g, 1)
    pred = np.exp(np.polyval(c, log_tau))
    return np.sum((gamma - pred)**2)

result = minimize_scalar(power_law_residual, bounds=(steps.max()+100, steps.max()+50000), method='bounded')
S_opt = result.x
tau_opt = S_opt - steps
c_pow = np.polyfit(np.log(tau_opt), np.log(gamma), 1)
pred_pow = np.exp(np.polyval(c_pow, np.log(tau_opt)))
r2_pow = 1 - np.sum((gamma - pred_pow)**2) / np.sum((gamma - gamma.mean())**2)

print(f"\n--- Model 3: POWER LAW ---")
print(f"Γ = {np.exp(c_pow[1]):.6f}·(S - step)^{c_pow[0]:.4f}")
print(f"S (Γ=0 step) = {S_opt:.0f}")
print(f"R² = {r2_pow:.6f}")
print(f"Exponent p = {c_pow[0]:.4f}")

# Model 4: Γ = floor + decay (Γ = Γ_∞ + a·exp(-b·step)) → asymptotes to Γ_∞ > 0
# This is the blowup scenario: Γ never reaches zero
from scipy.optimize import curve_fit

def floor_exp(step, gamma_inf, a, b):
    return gamma_inf + a * np.exp(-b * step)

try:
    popt, pcov = curve_fit(floor_exp, steps, gamma, p0=[0.05, 0.5, 1e-4], maxfev=10000)
    pred_floor = floor_exp(steps, *popt)
    r2_floor = 1 - np.sum((gamma - pred_floor)**2) / np.sum((gamma - gamma.mean())**2)
    print(f"\n--- Model 4: FLOOR + EXPONENTIAL DECAY ---")
    print(f"Γ = {popt[0]:.6f} + {popt[1]:.4f}·exp({-popt[2]:.8f}·step)")
    print(f"Γ_∞ (floor) = {popt[0]:.6f}")
    print(f"R² = {r2_floor:.6f}")
    print(f"Γ at step 40K: {floor_exp(40000, *popt):.6f}")
    has_floor = True
except:
    print(f"\n--- Model 4: FLOOR FIT FAILED ---")
    has_floor = False
    r2_floor = 0

# Summary
print(f"\n{'='*60}")
print(f"{'Model':<25} {'R²':>10} {'Γ=0 step':>12} {'Γ@40K':>10}")
print(f"{'-'*60}")
print(f"{'Linear':.<25} {r2_lin:>10.6f} {gamma_zero_lin:>12.0f} {np.polyval(c_lin, 40000):>10.6f}")
print(f"{'Exponential decay':.<25} {r2_exp:>10.6f} {'never':>12} {np.exp(c_exp[0]*40000+c_exp[1]):>10.6f}")
print(f"{'Power law':.<25} {r2_pow:>10.6f} {S_opt:>12.0f} {'<0':>10}")
if has_floor:
    print(f"{'Floor + exp':.<25} {r2_floor:>10.6f} {'never':>12} {floor_exp(40000, *popt):>10.6f}")

print(f"\n=== VERDICT ===")
best_r2 = max(r2_lin, r2_exp, r2_pow, r2_floor if has_floor else 0)
if best_r2 == r2_lin:
    print(f"LINEAR fits best → Γ crosses zero at step {gamma_zero_lin:.0f}")
    print(f"→ Viscosity WINS. No rebound. Regularity at this ν.")
elif best_r2 == r2_exp:
    print(f"EXPONENTIAL DECAY fits best → Γ→0 asymptotically, never crosses")
    print(f"→ Ambiguous. Stretching always barely leads but gap closes forever.")
elif best_r2 == r2_pow:
    print(f"POWER LAW fits best → Γ=0 at step {S_opt:.0f}, exponent {c_pow[0]:.2f}")
    print(f"→ Depends on exponent. If p>0: reaches zero. If p<0: never reaches.")
elif has_floor and best_r2 == r2_floor:
    print(f"FLOOR + EXP fits best → Γ→{popt[0]:.4f}")
    print(f"→ Γ floors above zero! Stretching ALWAYS wins. BLOWUP.")

# Save
results = {
    "r2_linear": float(r2_lin), "gamma_zero_linear": float(gamma_zero_lin),
    "r2_exponential": float(r2_exp),
    "r2_power_law": float(r2_pow), "gamma_zero_power": float(S_opt), "power_exponent": float(c_pow[0]),
    "r2_floor": float(r2_floor) if has_floor else None,
    "gamma_floor": float(popt[0]) if has_floor else None,
}
with open("ns_blowup/results/gamma_asymptotic_nr256.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to ns_blowup/results/gamma_asymptotic_nr256.json")
