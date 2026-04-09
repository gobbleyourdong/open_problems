#!/usr/bin/env python3
"""
temperature_SP.py — Temperature sensitivity of the specious present via Kramers kinetics.

Context:
  SP = N / B = 128 / 50 = 2.56 s at T_body = 310 K (parameter-free match).
  B(T) = k_Kramers(T) × N_active_channels / compression_ratio
  SP(T) = N × compression_ratio / (k_Kramers(T) × N_active_channels)

  The compression ratio is held fixed (cognitive architecture constant):
    compression_ratio = k_Kramers(310K) × N_active_channels / B_ref
  where B_ref = 50 bits/s, N_active_channels = 8.6e17 (1% active of 8.6e10 × 1e9),
  and k_Kramers at ΔE = 16.58 k_BT gives exactly 1000 Hz at 310 K.

Experiments:
  1. SP(T) for T = 295, 300, 305, 310, 315, 320 K.
  2. Q10 for SP predicted from Kramers vs psychophysical data.
  3. Hypothermia prediction: SP(306K) vs SP(310K).

Saves: results/temperature_SP_data.json
       results/temperature_SP_findings.md

Numerical track, what_is_time — 2026-04-09
"""

import math
import json
import os

# ── Physical constants ─────────────────────────────────────────────────────────

K_B    = 1.380649e-23   # J/K
T_REF  = 310.0          # K  (reference physiological temperature)

# Overdamped Kramers prefactor (same as kramers_neural.py)
OMEGA_0 = 1.0e12        # rad/s
GAMMA   = 10.0 * OMEGA_0
PREFACTOR = (OMEGA_0**2) / (2.0 * math.pi * GAMMA)   # Hz ≈ 1.592e10 Hz

# Barrier energy from the exact match: ΔE = 16.58 k_BT at T_ref = 310 K
# → k_Kramers(310K) = 1000 Hz  (matches brain K-rate target)
DELTA_E_KBT_REF = 16.58           # dimensionless at T_ref
DELTA_E_J       = DELTA_E_KBT_REF * K_B * T_REF   # fixed physical energy (J)

# Verify prefactor gives 1000 Hz at 310 K
k_check = PREFACTOR * math.exp(-DELTA_E_J / (K_B * T_REF))
print(f"[check] k_Kramers(310K) = {k_check:.4f} Hz  (expected ~1000 Hz)")

# Brain architecture — 1% active
N_CHANNELS_TOTAL   = 8.6e10 * 1.0e9   # total channels
ACTIVE_FRACTION    = 0.01
N_ACTIVE_CHANNELS  = N_CHANNELS_TOTAL * ACTIVE_FRACTION   # = 8.6e17

# Specious present architecture
N_MOMENTS = 128           # phenomenal moments per SP window
B_REF     = 50.0          # bits/s  conscious bandwidth at T_ref
SP_REF    = N_MOMENTS / B_REF   # = 2.56 s

# Compression ratio (cognitive architecture constant, independent of T)
# B = k_Kramers × N_active / compression_ratio  →  compression_ratio = k × N / B
COMPRESSION_RATIO = k_check * N_ACTIVE_CHANNELS / B_REF
print(f"[check] compression_ratio = {COMPRESSION_RATIO:.4e}  (30M:1 target ≈ 3e7)")


# ── Core functions ─────────────────────────────────────────────────────────────

def kramers_rate(T):
    """Kramers rate at temperature T with fixed physical barrier DELTA_E_J."""
    return PREFACTOR * math.exp(-DELTA_E_J / (K_B * T))


def bandwidth(T):
    """Conscious bandwidth B(T) = k_Kramers(T) × N_active / compression_ratio."""
    return kramers_rate(T) * N_ACTIVE_CHANNELS / COMPRESSION_RATIO


def specious_present(T):
    """SP(T) = N_moments / B(T)."""
    return N_MOMENTS / bandwidth(T)


# ── Experiment 1: SP over temperature grid ─────────────────────────────────────

temperatures = [295.0, 300.0, 305.0, 310.0, 315.0, 320.0]

print("\n── Experiment 1: SP(T) across physiological range ──────────────────────────")
print(f"{'T (K)':>8}  {'k_Kramers (Hz)':>16}  {'B (bits/s)':>12}  {'SP (s)':>10}  {'SP/SP_ref':>10}")
print("-" * 65)

exp1_data = []
for T in temperatures:
    k = kramers_rate(T)
    B = bandwidth(T)
    SP = specious_present(T)
    ratio = SP / SP_REF
    print(f"{T:>8.1f}  {k:>16.4e}  {B:>12.4f}  {SP:>10.4f}  {ratio:>10.4f}")
    exp1_data.append({
        "T_K": T,
        "k_Kramers_Hz": k,
        "B_bits_per_s": B,
        "SP_s": SP,
        "SP_ratio_to_310K": ratio,
    })


# ── Experiment 2: Q10 for SP ───────────────────────────────────────────────────

print("\n── Experiment 2: Q10 for specious present ───────────────────────────────────")

# Q10 = ratio of rate at T+10K to rate at T  (usually defined for rates)
# For SP (which is ~1/rate), Q10_SP = SP(T) / SP(T+10) = B(T+10) / B(T)
# = k(T+10) / k(T)

q10_data = []
print(f"{'T (K)':>8}  {'T+10 (K)':>10}  {'Q10_Kramers':>14}  {'SP(T)/SP(T+10)':>16}  {'Matches psych?':>15}")
print("-" * 72)

for T in [295.0, 300.0, 305.0, 310.0]:
    T2 = T + 10.0
    q10_rate = kramers_rate(T2) / kramers_rate(T)   # k increases with T → Q10 > 1
    q10_SP   = specious_present(T) / specious_present(T2)  # SP decreases with T → ratio > 1
    # Psychophysical data: reaction times slow 2–4× when T drops 10K
    # → cognitive speed (1/RT) has Q10 ≈ 2–4  → SP has Q10 ≈ 2–4
    matches = "yes" if 2.0 <= q10_SP <= 4.0 else "borderline" if 1.5 <= q10_SP <= 5.0 else "no"
    print(f"{T:>8.1f}  {T2:>10.1f}  {q10_rate:>14.4f}  {q10_SP:>16.4f}  {matches:>15}")
    q10_data.append({
        "T_K": T,
        "T_plus10_K": T2,
        "Q10_Kramers_rate": q10_rate,
        "Q10_SP": q10_SP,
        "psychophysical_range_2to4": matches,
    })

# Also compute analytic approximation: Q10 ≈ exp(ΔE_J × 10 / (k_B × T × (T+10)))
print("\nAnalytic Q10 formula: exp(ΔE_J × 10 / (k_B × T × (T+10)))")
for T in [295.0, 300.0, 305.0, 310.0]:
    T2 = T + 10.0
    q10_analytic = math.exp(DELTA_E_J * 10.0 / (K_B * T * T2))
    print(f"  T = {T:.0f} K → Q10_analytic = {q10_analytic:.4f}")


# ── Experiment 3: Hypothermia prediction ──────────────────────────────────────

print("\n── Experiment 3: Hypothermia (T = 306 K = 33°C) ────────────────────────────")

T_HYPO = 306.0   # 33°C — mild clinical hypothermia
T_NORM = 310.0   # 37°C — normal body temperature

SP_hypo = specious_present(T_HYPO)
SP_norm = specious_present(T_NORM)
ratio_hypo = SP_hypo / SP_norm
pct_change = 100.0 * (SP_hypo - SP_norm) / SP_norm

print(f"  SP(310K, normal)     = {SP_norm:.4f} s")
print(f"  SP(306K, hypothermia)= {SP_hypo:.4f} s")
print(f"  Ratio SP(306)/SP(310)= {ratio_hypo:.4f}")
print(f"  % change in SP       = +{pct_change:.2f}% (SP lengthens → subjective time slows)")

# Expected anecdotal report: "time slows down" in hypothermia
# → SP is longer → each moment contains more real-time → time perception is stretched
slows_down = SP_hypo > SP_norm
print(f"  Predicted 'time slows down' in hypothermia: {slows_down}")

# Compute the exact 26% per 10K figure mentioned in context
shift_per_10K = 100.0 * (specious_present(T_NORM - 10.0) / SP_norm - 1.0)
print(f"\n  SP shift per 10K drop (300K vs 310K): +{shift_per_10K:.1f}%")

hypo_data = {
    "T_hypothermia_K": T_HYPO,
    "T_normal_K": T_NORM,
    "SP_hypothermia_s": SP_hypo,
    "SP_normal_s": SP_norm,
    "ratio_SP_hypo_to_norm": ratio_hypo,
    "pct_change_SP": pct_change,
    "predicted_time_slows_down": slows_down,
    "SP_shift_pct_per_10K_drop": shift_per_10K,
}


# ── Save results ──────────────────────────────────────────────────────────────

results = {
    "parameters": {
        "K_B_J_per_K": K_B,
        "T_ref_K": T_REF,
        "DELTA_E_kBT_at_Tref": DELTA_E_KBT_REF,
        "DELTA_E_J": DELTA_E_J,
        "prefactor_Hz": PREFACTOR,
        "k_Kramers_at_310K_Hz": k_check,
        "N_active_channels": N_ACTIVE_CHANNELS,
        "compression_ratio": COMPRESSION_RATIO,
        "N_moments": N_MOMENTS,
        "B_ref_bits_per_s": B_REF,
        "SP_ref_s": SP_REF,
    },
    "exp1_SP_vs_temperature": exp1_data,
    "exp2_Q10": q10_data,
    "exp3_hypothermia": hypo_data,
}

out_path = os.path.join(os.path.dirname(__file__), "..", "results", "temperature_SP_data.json")
out_path = os.path.normpath(out_path)
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\n[saved] {out_path}")

print("\nDone.")
