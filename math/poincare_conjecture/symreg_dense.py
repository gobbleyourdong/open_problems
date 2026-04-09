"""
PySR on dense Euler blowup data — 12,577 points.
Find the scaling structure in the blowup regime.

Target: discover the functional form of ‖ω‖(τ) where τ = T* - t.
"""
import numpy as np
import json
from pysr import PySRRegressor

# Load dense timeseries
with open('ns_blowup/results/euler_dense_nr64_timeseries.json') as f:
    ts = json.load(f)

t = np.array(ts['t'])
w1r = np.array(ts['w1r'])
u1z = np.array(ts['u1z'])
T_star = ts['T_star']

tau = T_star - t  # time to blowup

# Focus on blowup regime: w1r > 1000 and τ > 0
mask = (w1r > 1000) & (tau > 1e-7)
tau_bl = tau[mask]
w1r_bl = w1r[mask]
u1z_bl = u1z[mask]

print(f"Total points: {len(t)}")
print(f"Blowup regime: {len(tau_bl)} points")
print(f"τ range: [{tau_bl.min():.2e}, {tau_bl.max():.2e}]")
print(f"|w1r| range: [{w1r_bl.min():.2e}, {w1r_bl.max():.2e}]")

# Subsample for PySR speed (still dense — every 10th point)
stride = max(1, len(tau_bl) // 1000)
tau_sub = tau_bl[::stride]
w1r_sub = w1r_bl[::stride]
u1z_sub = u1z_bl[::stride]
print(f"PySR input: {len(tau_sub)} points (stride={stride})")

# --- FIT 1: |w1r| = f(τ) ---
print("\n" + "="*60)
print("FIT 1: |w1r| = f(τ)")
print("="*60)

model_w = PySRRegressor(
    niterations=200,
    binary_operators=["+", "-", "*", "/", "pow"],
    unary_operators=["log", "exp", "sqrt", "inv"],
    maxsize=20,
    populations=30,
    parallelism="serial",
    deterministic=True,
    random_state=42,
    temp_equation_file=True,
    loss="loss(prediction, target) = (log(abs(prediction)) - log(abs(target)))^2",  # log-space loss
)

model_w.fit(tau_sub.reshape(-1, 1), w1r_sub)
print("\nBest equations:")
print(model_w)

# --- FIT 2: |u1z| = f(τ) ---
print("\n" + "="*60)
print("FIT 2: |u1z| = f(τ)")
print("="*60)

model_u = PySRRegressor(
    niterations=200,
    binary_operators=["+", "-", "*", "/", "pow"],
    unary_operators=["log", "exp", "sqrt", "inv"],
    maxsize=20,
    populations=30,
    parallelism="serial",
    deterministic=True,
    random_state=42,
    temp_equation_file=True,
    loss="loss(prediction, target) = (log(abs(prediction)) - log(abs(target)))^2",
)

model_u.fit(tau_sub.reshape(-1, 1), u1z_sub)
print("\nBest equations:")
print(model_u)

# --- FIT 3: relationship between w1r and u1z ---
print("\n" + "="*60)
print("FIT 3: |w1r| = g(|u1z|)")
print("="*60)

model_rel = PySRRegressor(
    niterations=100,
    binary_operators=["+", "-", "*", "/", "pow"],
    unary_operators=["log", "sqrt", "inv"],
    maxsize=12,
    populations=20,
    parallelism="serial",
    deterministic=True,
    random_state=42,
    temp_equation_file=True,
)

model_rel.fit(u1z_sub.reshape(-1, 1), w1r_sub)
print("\nBest equations:")
print(model_rel)

# --- Manual analysis ---
print("\n" + "="*60)
print("MANUAL ANALYSIS")
print("="*60)

# Power law fit in blowup regime
log_tau = np.log(tau_sub)
log_w = np.log(w1r_sub)
log_u = np.log(u1z_sub)

# Piecewise γ — check if exponent changes through blowup
n = len(tau_sub)
chunks = 5
for i in range(chunks):
    sl = slice(i*n//chunks, (i+1)*n//chunks)
    lt, lw = log_tau[sl], log_w[sl]
    if len(lt) > 3:
        coeffs = np.polyfit(lt, lw, 1)
        gamma = -coeffs[0]
        r2 = 1 - np.sum((lw - np.polyval(coeffs, lt))**2) / np.sum((lw - lw.mean())**2)
        tau_range = f"[{tau_sub[sl].min():.2e}, {tau_sub[sl].max():.2e}]"
        print(f"  Chunk {i+1}: γ(w1r) = {gamma:.4f}  R²={r2:.4f}  τ∈{tau_range}")

# Overall
coeffs_all = np.polyfit(log_tau, log_w, 1)
gamma_all = -coeffs_all[0]
print(f"\n  Overall: γ(w1r) = {gamma_all:.4f}")
print(f"  Literature: γ=2.5 (Luo-Hou), γ=1.0 (Hou 2022)")

# w1r vs u1z scaling
coeffs_rel = np.polyfit(log_u, log_w, 1)
print(f"\n  |w1r| ~ |u1z|^{coeffs_rel[0]:.4f}")
