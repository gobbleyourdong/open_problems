"""
Symbolic regression on Euler blowup data.
Find the scaling law: ‖ω‖_∞ ~ f(T* - t)

Known from literature:
  Luo-Hou 2014: γ = 5/2 (boundary blowup)
  Hou 2022: γ = 1 (interior blowup)
  Our Nr=64: γ ≈ 1.85 (wall BC simplified)

PySR should rediscover: ‖ω‖ ~ C / (T* - t)^γ
"""
import numpy as np
from pysr import PySRRegressor

# Euler Nr=64 data (from validated run)
T_star = 0.0036495383190477773

data = [
    # (t, |w1r|, |u1z|)
    (0.00000000, 0.0, 3.77e+03),
    (0.00099910, 4.00e+02, 5.34e+03),
    (0.00199910, 1.00e+03, 1.44e+04),
    (0.00299910, 6.90e+03, 6.93e+04),
    (0.00346711, 5.72e+04, 7.88e+05),
    (0.00357400, 1.57e+05, 2.44e+06),
    (0.00361755, 3.49e+05, 5.27e+06),
    (0.00363780, 7.29e+05, 9.99e+06),
    (0.00364752, 1.53e+06, 1.88e+07),
    (0.00365208, 3.34e+06, 3.78e+07),
    (0.00365411, 7.82e+06, 8.41e+07),
    (0.00365495, 1.98e+07, 2.08e+08),
    (0.00365527, 5.43e+07, 5.64e+08),
]

t_arr = np.array([d[0] for d in data])
w1r_arr = np.array([d[1] for d in data])
u1z_arr = np.array([d[2] for d in data])

# Use time-to-blowup as the independent variable
tau = T_star - t_arr  # τ = T* - t

# Filter: only use points where vorticity is significant (blowup regime)
mask = (w1r_arr > 100) & (tau > 1e-7)  # positive τ only
tau_fit = tau[mask]
w1r_fit = w1r_arr[mask]
u1z_fit = u1z_arr[mask]

print(f"Fitting {len(tau_fit)} points in blowup regime")
print(f"τ range: [{tau_fit.min():.2e}, {tau_fit.max():.2e}]")
print(f"|w1r| range: [{w1r_fit.min():.2e}, {w1r_fit.max():.2e}]")

# --- FIT 1: |w1r| as function of τ ---
print("\n=== FIT 1: |w1r| = f(τ) ===")
model_w = PySRRegressor(
    niterations=100,
    binary_operators=["+", "-", "*", "/", "^"],
    unary_operators=["log", "exp", "sqrt", "inv"],
    maxsize=15,
    populations=20,
    procs=4,
    temp_equation_file=True,
    parallelism="serial",
    deterministic=True,
    random_state=42,
)
model_w.fit(tau_fit.reshape(-1, 1), w1r_fit)
print("\nBest equations found:")
print(model_w)

# --- FIT 2: |u1z| as function of τ ---
print("\n=== FIT 2: |u1z| = f(τ) ===")
model_u = PySRRegressor(
    niterations=100,
    binary_operators=["+", "-", "*", "/", "^"],
    unary_operators=["log", "exp", "sqrt", "inv"],
    maxsize=15,
    populations=20,
    procs=4,
    temp_equation_file=True,
    parallelism="serial",
    deterministic=True,
    random_state=42,
)
model_u.fit(tau_fit.reshape(-1, 1), u1z_fit)
print("\nBest equations found:")
print(model_u)

# --- Manual check: power law fit ---
print("\n=== MANUAL POWER LAW CHECK ===")
log_tau = np.log(tau_fit)
log_w1r = np.log(w1r_fit)
log_u1z = np.log(u1z_fit)

# Linear regression on log-log: log(y) = -γ·log(τ) + log(C)
from numpy.polynomial import polynomial as P

# w1r
coeffs_w = np.polyfit(log_tau, log_w1r, 1)
gamma_w = -coeffs_w[0]
C_w = np.exp(coeffs_w[1])
print(f"|w1r| ~ {C_w:.4f} / τ^{gamma_w:.4f}")

# u1z
coeffs_u = np.polyfit(log_tau, log_u1z, 1)
gamma_u = -coeffs_u[0]
C_u = np.exp(coeffs_u[1])
print(f"|u1z| ~ {C_u:.4f} / τ^{gamma_u:.4f}")

# R² values
pred_w = C_w * tau_fit**(-gamma_w)
r2_w = 1 - np.sum((w1r_fit - pred_w)**2) / np.sum((w1r_fit - w1r_fit.mean())**2)
pred_u = C_u * tau_fit**(-gamma_u)
r2_u = 1 - np.sum((u1z_fit - pred_u)**2) / np.sum((u1z_fit - u1z_fit.mean())**2)
print(f"R² (w1r): {r2_w:.6f}")
print(f"R² (u1z): {r2_u:.6f}")

print(f"\nExpected γ from literature: 2.5 (Luo-Hou), 1.0 (Hou 2022)")
print(f"Our γ (w1r): {gamma_w:.4f}")
print(f"Our γ (u1z): {gamma_u:.4f}")
