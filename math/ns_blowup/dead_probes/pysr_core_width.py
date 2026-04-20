"""
PySR on Nr=64 core width data — find α/||ω|| vs R_rms relationship.
Runs on CPU (no GPU needed).
Gemini's prediction: α/||ω|| = C₁ + C₂·ln(L/R_min) (elliptic integral asymptotics)
"""
import json
import numpy as np

# Load the Nr=64 diagnostic data
with open("ns_blowup/results/core_width_nr64.json") as f:
    data = json.load(f)

# Filter to the trough region (Γ < 0.5, skip t=0)
trough = [d for d in data if 0 < d["t"] and d["gamma"] < 0.5 and d["om1"] > 100]

print(f"Total points: {len(data)}, Trough points: {len(trough)}")
print(f"Γ range in trough: [{min(d['gamma'] for d in trough):.4f}, {max(d['gamma'] for d in trough):.4f}]")
print(f"R_rms range: [{min(d['R_rms'] for d in trough):.4f}, {max(d['R_rms'] for d in trough):.4f}]")
print(f"|ω| range: [{min(d['om1'] for d in trough):.2e}, {max(d['om1'] for d in trough):.2e}]")
print(f"α range: [{min(d['alpha_max'] for d in trough):.2e}, {max(d['alpha_max'] for d in trough):.2e}]")

# Compute α/||ω|| — the dimensionless strain amplification
t_arr = np.array([d["t"] for d in trough])
gamma_arr = np.array([d["gamma"] for d in trough])
R_arr = np.array([d["R_rms"] for d in trough])
alpha_arr = np.array([d["alpha_max"] for d in trough])
omega_arr = np.array([d["om1"] for d in trough])
S_arr = np.array([d["S"] for d in trough])
nuP_arr = np.array([d["nuP"] for d in trough])

# Dimensionless ratio
ratio = alpha_arr / omega_arr

print(f"\nα/||ω|| range: [{ratio.min():.6f}, {ratio.max():.6f}]")
print(f"α/||ω|| at Γ_min: {ratio[np.argmin(gamma_arr)]:.6f}")

# Quick correlation check before PySR
from numpy.polynomial import polynomial as P

# Fit ratio vs R_rms
coeffs = np.polyfit(R_arr, ratio, 2)
pred = np.polyval(coeffs, R_arr)
ss_res = np.sum((ratio - pred)**2)
ss_tot = np.sum((ratio - ratio.mean())**2)
r2_poly = 1 - ss_res/ss_tot
print(f"\nQuadratic fit α/||ω|| vs R_rms: R²={r2_poly:.4f}")
print(f"  Coefficients: {coeffs}")

# Fit ratio vs log(1/R_rms)
log_R = np.log(1.0 / R_arr)
coeffs_log = np.polyfit(log_R, ratio, 1)
pred_log = np.polyval(coeffs_log, log_R)
ss_res_log = np.sum((ratio - pred_log)**2)
r2_log = 1 - ss_res_log/ss_tot
print(f"\nLinear fit α/||ω|| vs ln(1/R): R²={r2_log:.4f}")
print(f"  α/||ω|| = {coeffs_log[0]:.6f}·ln(1/R) + {coeffs_log[1]:.6f}")

# Fit ratio vs 1/R
inv_R = 1.0 / R_arr
coeffs_inv = np.polyfit(inv_R, ratio, 1)
pred_inv = np.polyval(coeffs_inv, inv_R)
ss_res_inv = np.sum((ratio - pred_inv)**2)
r2_inv = 1 - ss_res_inv/ss_tot
print(f"\nLinear fit α/||ω|| vs 1/R: R²={r2_inv:.4f}")
print(f"  α/||ω|| = {coeffs_inv[0]:.6f}/R + {coeffs_inv[1]:.6f}")

# Also check S/nuP vs R (the ratio that IS Γ-related)
S_over_nuP = S_arr / (nuP_arr + 1e-30)
print(f"\nS/νP range: [{S_over_nuP.min():.4f}, {S_over_nuP.max():.4f}]")
print(f"S/νP at Γ_min: {S_over_nuP[np.argmin(gamma_arr)]:.4f}")

# Save quick analysis results
results = {
    "n_trough_points": len(trough),
    "gamma_min": float(gamma_arr.min()),
    "R_at_gamma_min": float(R_arr[np.argmin(gamma_arr)]),
    "alpha_at_gamma_min": float(alpha_arr[np.argmin(gamma_arr)]),
    "ratio_at_gamma_min": float(ratio[np.argmin(gamma_arr)]),
    "r2_quadratic": float(r2_poly),
    "r2_log": float(r2_log),
    "r2_inv_R": float(r2_inv),
    "log_fit_slope": float(coeffs_log[0]),
    "log_fit_intercept": float(coeffs_log[1]),
}

with open("ns_blowup/results/pysr_quick_analysis.json", "w") as f:
    json.dump(results, f, indent=2)

print(f"\nSaved to ns_blowup/results/pysr_quick_analysis.json")

# Now try PySR if available
try:
    from pysr import PySRRegressor

    print("\n=== PySR Symbolic Regression ===")
    print("Target: α/||ω|| as function of R_rms")

    X = np.column_stack([R_arr, omega_arr, t_arr])
    y = ratio

    model = PySRRegressor(
        niterations=100,
        binary_operators=["+", "-", "*", "/"],
        unary_operators=["log", "sqrt", "inv(x) = 1/x"],
        populations=20,
        population_size=50,
        maxsize=15,
        parsimony=0.01,
        deterministic=True,
        parallelism="serial",
        progress=True,
        variable_names=["R", "omega", "t"],
    )

    model.fit(X, y)

    print("\n=== Best equations ===")
    print(model)

    # Save PySR results
    model.equations_.to_csv("ns_blowup/results/pysr_core_width_equations.csv")
    print("Saved equations to ns_blowup/results/pysr_core_width_equations.csv")

except ImportError:
    print("\nPySR not available in this environment. Quick analysis above is sufficient.")
    print("Install with: pip install pysr")
except Exception as e:
    print(f"\nPySR failed: {e}")
    print("Quick analysis above is still valid.")

print("\n=== SUMMARY ===")
print(f"Best simple fit: α/||ω|| = {coeffs_log[0]:.4f}·ln(1/R) + {coeffs_log[1]:.4f} (R²={r2_log:.4f})")
print(f"Gemini predicted logarithmic dependence — {'CONFIRMED' if r2_log > 0.8 else 'INCONCLUSIVE'}")
