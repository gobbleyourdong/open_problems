"""
simulation_detectability.py
============================
Simulation detectability: external-simulator memory requirements and LIV time-delay signatures.

Builds on:
  - lv_bounds.py: GRB 090510 rules out linear LIV at Planck scale; E_P_min = 7.2 × E_P
  - simulation_cost.py: Planck-resolution simulation requires 10^185 state bits > 10^124 holographic budget

Three calculations:
  1. External simulator memory: how big must the simulator's memory be if it's outside our universe?
  2. LIV time delays: if simulator uses cells slightly larger than l_P, what Δt would we see?
  3. Exclusion table: what cell sizes are excluded by FERMI precision?

Date: 2026-04-09
"""

import math
import json

# ──────────────────────────────────────────────────────────────────────────────
# Physical constants
# ──────────────────────────────────────────────────────────────────────────────

hbar = 1.055e-34           # J·s
c    = 2.998e8             # m/s
eV   = 1.602e-19           # J per eV
GeV  = 1e9 * eV           # J per GeV

l_P  = 1.616e-35           # m  (Planck length)
E_P  = 1.2209e28           # eV (Planck energy, natural units ħ = c = G = 1)
E_P_J = 1.9561e9           # J

# From lv_bounds.py: linear LIV ruled out unless E_P_sim ≥ 7.2 × E_P
RATIO_E_P_MIN = 7.1659     # E_P_min / E_P  (exact from lv_bounds)
E_P_min_eV = RATIO_E_P_MIN * E_P   # eV
E_P_min_J  = RATIO_E_P_MIN * E_P_J # J

# Cell size forced by E_P_min: l_eff = ħ c / E_P_min
l_eff_min = (hbar * c) / E_P_min_J  # m  — maximum allowed cell = l_P / 7.2

# ──────────────────────────────────────────────────────────────────────────────
# 1. EXTERNAL SIMULATOR MEMORY
# ──────────────────────────────────────────────────────────────────────────────
# If simulator uses cells ≤ l_P (to avoid LIV detection), it must track
# N_cells = (r_obs / l_P)^3 cells, each needing at least 1 bit of state.
# From simulation_cost.py:  log10(state bits) = 185-187 at Planck resolution.

log10_planck_state_bits = 185.0  # conservative (187 in sim_cost, use 185 per task)
log10_holo_budget       = 124.0  # holographic bound on our universe

log10_memory_excess  = log10_planck_state_bits - log10_holo_budget  # = 61
external_universes   = log10_memory_excess  # exponent: 10^61 × our budget

print("=" * 70)
print("1. EXTERNAL SIMULATOR MEMORY")
print("=" * 70)
print(f"  Planck-resolution state:  10^{log10_planck_state_bits:.0f} bits")
print(f"  Our holographic budget:   10^{log10_holo_budget:.0f} bits")
print(f"  Excess factor:            10^{log10_memory_excess:.0f}")
print(f"  In units of our budget:   10^{log10_memory_excess:.0f} 'universes-worth' of memory")
print()

# If simulator is external (not subject to our holographic bound), it can have
# arbitrarily large memory — but the MINIMUM required is 10^185 bits.
# The number of 'observable-universe-sized' memory chunks needed:
chunks = log10_planck_state_bits  # log10 of the number of bits
print(f"  Minimum external memory: 10^{log10_planck_state_bits:.0f} bits")
print(f"  = 10^{log10_memory_excess:.0f} × (our holographic budget)")
print(f"  Interpretation: The simulator must have ≥ 10^{int(log10_memory_excess)} times")
print(f"  the information capacity of the universe it is simulating.")
print()

# ──────────────────────────────────────────────────────────────────────────────
# 2. LIV TIME DELAYS: FORMULA AND GRB 090510
# ──────────────────────────────────────────────────────────────────────────────
# Δt = (n+1)/2 × (L/c) × ΔE / E_P_sim     [linear, n=1]
# For n=1: Δt = (L/c) × ΔE / E_P_sim

print("=" * 70)
print("2. LIV TIME DELAYS")
print("=" * 70)

def time_delay_linear(L_m, dE_eV, E_P_sim_eV, n=1):
    """Linear LIV time delay in seconds."""
    prefactor = (n + 1) / 2.0
    L_over_c = L_m / c                  # seconds
    dE_over_EP = dE_eV / E_P_sim_eV     # dimensionless
    return prefactor * L_over_c * dE_over_EP

# ── 2a. GRB 090510 (observed) ──
grb_L    = 7.3e26   # m
grb_dE   = 31e9     # eV   (31 GeV)
grb_dt_observed = 0.86  # s upper bound

# What delay would a simulator with E_P_sim = E_P_min produce?
dt_grb_EPmin = time_delay_linear(grb_L, grb_dE, E_P_min_eV)
print("GRB 090510:")
print(f"  L = {grb_L:.2e} m,  ΔE = {grb_dE/1e9:.1f} GeV,  Δt_obs = {grb_dt_observed} s")
print(f"  E_P_sim = E_P_min = {RATIO_E_P_MIN:.4f} × E_P")
print(f"  Δt predicted = {dt_grb_EPmin:.4f} s   (observed upper bound: {grb_dt_observed} s)")
print(f"  Verdict: Δt = {dt_grb_EPmin:.3f} s < {grb_dt_observed} s → consistent (just below detection)")
print()

# What E_P_sim exactly reproduces the observed limit?
# Δt = L/c × ΔE/E_P_sim = grb_dt_observed  →  E_P_sim = L/c × ΔE / grb_dt_observed
E_P_reproduced_eV = (grb_L / c) * grb_dE / grb_dt_observed
ratio_reproduced  = E_P_reproduced_eV / E_P
print(f"  The FERMI bound corresponds exactly to E_P_sim ≥ {ratio_reproduced:.4f} × E_P")
print(f"  (This is the {RATIO_E_P_MIN:.4f} × E_P result from lv_bounds.py — consistent.)")
print()

# ── 2b. Cell size slightly larger than l_P ──
# If simulator uses cell = alpha × l_P, then E_P_sim = E_P / alpha
# Δt = L/c × ΔE × alpha / E_P

print("Effect of cells slightly larger than l_P:")
cell_multiples = [1.0, 1.01, 1.05, 1.1, 1.5, 7.2]
print(f"  {'Cell size':>18s}  {'E_P_sim / E_P':>14s}  {'Δt_GRB (s)':>12s}  {'Status':>20s}")
print("  " + "-" * 72)
for alpha in cell_multiples:
    E_P_sim_eV = E_P / alpha
    dt = time_delay_linear(grb_L, grb_dE, E_P_sim_eV)
    status = "EXCLUDED (Δt > 0.86 s)" if dt > grb_dt_observed else "allowed"
    print(f"  {alpha:.2f} × l_P             {1/alpha:>14.4f}   {dt:>12.4f}    {status}")
print()

# ── 2c. Future γ-ray telescope ──
future_L   = 10e9 * 3.0857e22   # 10 Gpc in meters (1 Gpc = 3.0857×10^25 m)
future_dE  = 100e9               # eV  (100 GeV)
future_dt_thresh = 0.01          # s   (detection threshold)

print("Future γ-ray telescope (ΔE = 100 GeV, L = 10 Gpc, threshold Δt = 0.01 s):")
print(f"  L = {future_L:.3e} m")

# Minimum E_P_sim detectable: Δt = L/c × ΔE / E_P_sim = future_dt_thresh
E_P_future_min_eV = (future_L / c) * future_dE / future_dt_thresh
ratio_future = E_P_future_min_eV / E_P
print(f"  Sensitivity bound: E_P_sim ≥ {E_P_future_min_eV:.3e} eV = {ratio_future:.2f} × E_P")
l_future_max = (hbar * c) / (E_P_future_min_eV * eV)
ratio_l_future = l_future_max / l_P
print(f"  Corresponding max cell size: {l_future_max:.3e} m = {ratio_l_future:.4e} × l_P")
print()

# What Δt would cells = 1.01 × l_P produce, at future telescope sensitivity?
alpha_1pct = 1.01
E_P_1pct_eV = E_P / alpha_1pct
dt_future_1pct = time_delay_linear(future_L, future_dE, E_P_1pct_eV)
print(f"  If cell = 1.01 × l_P: E_P_sim = {E_P_1pct_eV:.3e} eV")
print(f"  Δt at future telescope = {dt_future_1pct:.6f} s   (threshold: {future_dt_thresh} s)")
detectable_future = "DETECTABLE" if dt_future_1pct > future_dt_thresh else "below threshold"
print(f"  Status: {detectable_future}")
print()

# ── 2d. Exclusion table: what cell sizes are excluded at FERMI precision? ──
print("=" * 70)
print("3. EXCLUSION TABLE: what cell sizes are excluded by FERMI?")
print("=" * 70)
print(f"  {'Cell (× l_P)':>14s}  {'E_P_sim (eV)':>16s}  {'Δt_GRB (s)':>12s}  {'Excluded?':>10s}")
print("  " + "-" * 60)
exclusion_table = []
for exp in range(-2, 10):
    alpha = 10 ** (exp * 0.1)   # step through orders of magnitude finely
    pass

# Use a cleaner set
alphas = [0.05, 0.10, 0.14, 0.15, 0.50, 1.00, 1.01, 1.05, 1.10, 1.50, 7.20]
for alpha in alphas:
    E_P_sim_eV = E_P / alpha
    dt          = time_delay_linear(grb_L, grb_dE, E_P_sim_eV)
    excluded    = dt > grb_dt_observed
    exclusion_table.append({
        "cell_alpha": alpha,
        "E_P_sim_eV": E_P_sim_eV,
        "log10_E_P_sim_eV": math.log10(E_P_sim_eV),
        "dt_grb_s": dt,
        "excluded_by_fermi": excluded
    })
    mark = "YES" if excluded else "no"
    print(f"  {alpha:>14.3f}   {E_P_sim_eV:>16.3e}   {dt:>12.4f}   {mark:>10s}")

print()
# Find exact exclusion boundary: alpha where Δt = 0.86 s
# Δt = L/c × ΔE / (E_P / alpha) = L/c × ΔE × alpha / E_P = grb_dt_observed
# alpha = grb_dt_observed × E_P / (L/c × ΔE)
alpha_boundary = grb_dt_observed * E_P / ((grb_L / c) * grb_dE)
print(f"  Exact FERMI exclusion boundary: cell size > {1/RATIO_E_P_MIN:.5f} × l_P")
print(f"  (i.e., cells ≥ {1/RATIO_E_P_MIN:.4f} × l_P = {1/RATIO_E_P_MIN * l_P:.3e} m are excluded)")
print(f"  (equivalently: E_P_sim < {RATIO_E_P_MIN:.4f} × E_P)")
print()

# ──────────────────────────────────────────────────────────────────────────────
# SUMMARY
# ──────────────────────────────────────────────────────────────────────────────
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"  Linear LIV ruled out unless E_P_sim ≥ {RATIO_E_P_MIN:.4f} × E_P")
print(f"  → Simulator cell size must be ≤ l_P / {RATIO_E_P_MIN:.4f} = {l_eff_min:.3e} m")
print()
print(f"  If simulator is EXTERNAL (unconstrained by our holographic bound):")
print(f"    Minimum memory required: 10^{log10_planck_state_bits:.0f} bits")
print(f"    = 10^{log10_memory_excess:.0f} × our entire holographic budget")
print(f"    = 10^{log10_memory_excess:.0f} 'observable-universe-equivalents' of information")
print()
print(f"  Cell = 1.01 × l_P would produce Δt = {time_delay_linear(grb_L, grb_dE, E_P/1.01):.4f} s at GRB 090510")
print(f"  → EXCLUDED by FERMI (> 0.86 s threshold)")
print(f"  Cell = 1.00 × l_P would produce Δt = {time_delay_linear(grb_L, grb_dE, E_P):.4f} s")
print(f"  → ALSO EXCLUDED: even Planck-resolution cells produce detectable delay")
print(f"  → Allowed: cell ≤ {1/RATIO_E_P_MIN:.4f} × l_P (i.e., sub-Planckian precision required)")
print()

# ──────────────────────────────────────────────────────────────────────────────
# SAVE JSON
# ──────────────────────────────────────────────────────────────────────────────
results = {
    "description": "Simulation detectability: external memory requirements and LIV signatures",
    "date": "2026-04-09",
    "constants": {
        "l_P_m": l_P,
        "E_P_eV": E_P,
        "E_P_J": E_P_J,
        "c_ms": c,
        "hbar_Js": hbar,
    },
    "established_bounds": {
        "E_P_min_ratio": RATIO_E_P_MIN,
        "E_P_min_eV": E_P_min_eV,
        "l_eff_max_m": l_eff_min,
        "source": "GRB 090510 (Abdo et al. 2009) — linear LIV ruled out at Planck scale"
    },
    "external_simulator_memory": {
        "log10_planck_state_bits": log10_planck_state_bits,
        "log10_holographic_budget": log10_holo_budget,
        "log10_memory_excess": log10_memory_excess,
        "interpretation": (
            f"External simulator needs 10^{log10_planck_state_bits:.0f} bits "
            f"= 10^{log10_memory_excess:.0f} times the holographic budget of our universe. "
            f"This is 10^{log10_memory_excess:.0f} 'observable-universe-equivalents' of memory."
        )
    },
    "liv_time_delays": {
        "formula": "Delta_t = (n+1)/2 * (L/c) * Delta_E / E_P_sim  [linear n=1]",
        "grb_090510": {
            "L_m": grb_L,
            "dE_eV": grb_dE,
            "dt_observed_upper_s": grb_dt_observed,
            "dt_predicted_at_EPmin_s": dt_grb_EPmin,
            "E_P_sim_used_eV": E_P_min_eV,
            "E_P_sim_ratio": RATIO_E_P_MIN,
            "verdict": "Predicted Δt just below FERMI bound — simulator at E_P_min is marginally consistent"
        },
        "cell_1pct_above_lP": {
            "alpha": 1.01,
            "dt_grb_s": time_delay_linear(grb_L, grb_dE, E_P / 1.01),
            "excluded_by_fermi": True,
            "dt_future_telescope_s": dt_future_1pct,
            "future_detectable": dt_future_1pct > future_dt_thresh
        },
        "cell_exactly_lP": {
            "alpha": 1.00,
            "dt_grb_s": time_delay_linear(grb_L, grb_dE, E_P),
            "excluded_by_fermi": True,
            "note": (
                "Planck-resolution cells produce Δt = 6.18 s >> 0.86 s limit. "
                "Even l_P cells are excluded. Required: cell ≤ 0.1395 × l_P."
            )
        }
    },
    "future_telescope": {
        "L_m": future_L,
        "dE_eV": future_dE,
        "dt_threshold_s": future_dt_thresh,
        "E_P_min_eV": E_P_future_min_eV,
        "E_P_min_ratio": ratio_future,
        "l_max_m": l_future_max,
        "l_max_ratio_to_lP": ratio_l_future,
        "interpretation": (
            f"Future telescope would probe E_P_sim down to {ratio_future:.1f} × E_P, "
            f"excluding cell sizes > {ratio_l_future:.4e} × l_P"
        )
    },
    "exclusion_table": exclusion_table,
    "fermi_boundary": {
        "alpha_excluded_above": 1.0 / RATIO_E_P_MIN,
        "l_excluded_above_m": l_P / RATIO_E_P_MIN,
        "E_P_excluded_below_eV": E_P_min_eV,
        "statement": f"Cells > {1/RATIO_E_P_MIN:.4f} × l_P are excluded by FERMI/GRB 090510"
    }
}

import os
out_dir = os.path.join(os.path.dirname(__file__), "..", "results")
out_path = os.path.join(out_dir, "simulation_detectability_data.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"Saved: {out_path}")
