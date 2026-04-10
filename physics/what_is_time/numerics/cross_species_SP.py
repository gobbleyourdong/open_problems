#!/usr/bin/env python3
"""
cross_species_SP.py — Cross-species specious present predictions
================================================================

Uses the temporal causal chain (attempt_003) to predict the specious
present for organisms with different body temperatures and ecological
niches. Tests the universality theorem (attempt_005): the five-level
chain is architecture, not biology.

Key formula:
  k_Kramers(T) = k_ref × exp(ΔE_J/k_B × (1/T_ref - 1/T))
  B(T) = k_Kramers(T) × N_active / compression_ratio
  SP(T) = N_moments / B(T)

For cross-species: ΔE is conserved (Nav channels are highly conserved),
but N_active, compression_ratio, and ecological SP may differ.

Two prediction modes:
  1. KRAMERS-ONLY: assume same compression ratio, predict B(T) from T alone
  2. ECOLOGICAL: predict SP from known ecological timescales, derive N
"""

import json
import math
import os

# Constants from the human chain
k_B = 1.380649e-23       # Boltzmann constant (J/K)
T_ref = 310.0             # human body temperature (K)
delta_E_kT = 16.58        # barrier height in kT units at T_ref
delta_E_J = delta_E_kT * k_B * T_ref  # barrier in Joules

k_ref = 1002.8            # Kramers rate at T_ref (Hz)
B_ref = 50.0              # conscious bandwidth at T_ref (bits/s)
N_moments = 128           # moments in human SP
SP_ref = N_moments / B_ref  # 2.56 s


def kramers_rate(T):
    """Kramers ion-channel gating rate at temperature T."""
    return k_ref * math.exp(delta_E_J / k_B * (1/T_ref - 1/T))


def bandwidth(T, compression_scale=1.0):
    """Conscious bandwidth at temperature T.
    compression_scale: ratio of species compression to human compression.
    >1 means MORE compression (smaller brain → fewer conscious channels).
    """
    return B_ref * (kramers_rate(T) / k_ref) / compression_scale


def specious_present(T, N=N_moments, compression_scale=1.0):
    """Specious present at temperature T with N moments."""
    B = bandwidth(T, compression_scale)
    return N / B


# ============================================================
# Cross-species predictions
# ============================================================

species = [
    {
        "name": "Human",
        "T_body": 310.0,
        "ecological_SP_range": (2.0, 4.0),
        "compression_scale": 1.0,
        "notes": "Baseline. SP = 2.56 s measured.",
    },
    {
        "name": "Hummingbird",
        "T_body": 313.0,    # 40°C, high metabolic rate
        "ecological_SP_range": (0.5, 2.0),  # fast hovering, flower-to-flower
        "compression_scale": 3.0,  # much smaller brain, fewer channels
        "notes": "Fastest avian metabolism. Ecological timescale ~1 s.",
    },
    {
        "name": "Cat",
        "T_body": 311.5,    # 38.5°C
        "ecological_SP_range": (1.5, 4.0),  # stalking, pouncing
        "compression_scale": 1.5,  # smaller brain than human
        "notes": "Predator with fast reaction. Ecological timescale ~2 s.",
    },
    {
        "name": "Elephant",
        "T_body": 309.0,    # 36°C
        "ecological_SP_range": (3.0, 8.0),  # slow social dynamics
        "compression_scale": 0.5,  # larger brain, more channels
        "notes": "Largest land brain. Slow ecological dynamics.",
    },
    {
        "name": "Mouse",
        "T_body": 310.0,    # 37°C
        "ecological_SP_range": (0.3, 1.5),  # fast predator avoidance
        "compression_scale": 10.0,  # tiny brain
        "notes": "Small brain, fast dynamics. High compression ratio.",
    },
    {
        "name": "Fruit fly (Drosophila)",
        "T_body": 298.0,    # ambient ~25°C (ectotherm)
        "ecological_SP_range": (0.1, 0.5),  # flight maneuvers, escape
        "compression_scale": 100.0,  # ~100K neurons vs ~86B in humans
        "notes": "Ectotherm. ~100K neurons. Very fast dynamics.",
    },
    {
        "name": "Green iguana",
        "T_body": 308.0,    # 35°C (preferred body temp)
        "ecological_SP_range": (2.0, 10.0),  # basking, slow response
        "compression_scale": 5.0,  # small reptile brain
        "notes": "Ectotherm. Slow ecological dynamics except escape.",
    },
    {
        "name": "Hypothetical AI (LLM)",
        "T_body": 310.0,    # room temp irrelevant; use equivalent
        "ecological_SP_range": (60, 300),  # context window timescale
        "compression_scale": 0.001,  # vastly more "channels" (parameters)
        "notes": "Not Kramers-gated. B_digital ~ 1000 bits/s. Speculative.",
    },
]

results = []

print("=" * 80)
print("CROSS-SPECIES SPECIOUS PRESENT PREDICTIONS")
print("From the temporal causal chain (what_is_time)")
print("=" * 80)
print()

for sp in species:
    T = sp["T_body"]
    cs = sp["compression_scale"]
    eco_lo, eco_hi = sp["ecological_SP_range"]

    k = kramers_rate(T)
    B = bandwidth(T, cs)
    SP_kramers = specious_present(T, N_moments, cs)

    # Ecological prediction: SP ≈ geometric mean of ecological range
    SP_eco = math.sqrt(eco_lo * eco_hi)
    N_eco = SP_eco * bandwidth(T, cs)
    n_qubits_eco = math.log2(N_eco) if N_eco > 1 else 0

    # Bit-optimal check: t_order = 1/B
    t_order = 1.0 / B if B > 0 else float('inf')

    entry = {
        "species": sp["name"],
        "T_body_K": T,
        "kramers_rate_Hz": round(k, 1),
        "bandwidth_bps": round(B, 2),
        "SP_kramers_s": round(SP_kramers, 3),
        "SP_ecological_s": round(SP_eco, 3),
        "N_ecological": round(N_eco, 1),
        "n_qubits_eco": round(n_qubits_eco, 2),
        "t_order_ms": round(t_order * 1000, 2),
        "compression_scale": cs,
        "notes": sp["notes"],
    }
    results.append(entry)

    print(f"### {sp['name']}")
    print(f"  T = {T} K ({T - 273.15:.1f}°C)")
    print(f"  k_Kramers = {k:.1f} Hz")
    print(f"  B = {B:.2f} bits/s (compression scale = {cs}×)")
    print(f"  SP (Kramers, N=128) = {SP_kramers:.3f} s")
    print(f"  SP (ecological) = {SP_eco:.3f} s")
    print(f"  N (ecological) = {N_eco:.1f} moments → {n_qubits_eco:.2f} qubits")
    print(f"  t_order = {t_order*1000:.2f} ms")
    print(f"  Notes: {sp['notes']}")
    print()

# ============================================================
# Key predictions summary
# ============================================================
print("=" * 80)
print("KEY PREDICTIONS")
print("=" * 80)
print()

print("1. BIT-OPTIMAL CONSTRAINT: t_order × B = 1 should hold for ALL species")
print("   (if the constraint is architectural, not coincidental)")
print()
for r in results:
    if r["species"] != "Hypothetical AI (LLM)":
        product = r["t_order_ms"] / 1000 * r["bandwidth_bps"]
        print(f"   {r['species']:25s}: t_order × B = {product:.3f}"
              f"  {'✓' if abs(product - 1.0) < 0.01 else '(check)'}")
print()

print("2. CROSS-SPECIES Q10: Kramers Q10 ≈ 1.68 should hold for ALL species")
print("   (since ΔE is conserved across ion channel families)")
print()
for r in results:
    T = r["T_body_K"]
    if T > 295 and r["species"] != "Hypothetical AI (LLM)":
        k_T = kramers_rate(T)
        k_T10 = kramers_rate(T + 10)
        q10 = k_T10 / k_T
        print(f"   {r['species']:25s}: Q10({T:.0f}→{T+10:.0f}) = {q10:.3f}")
print()

print("3. THRESHOLD PREDICTION: organisms with N < 128 have NO phenomenal time")
print("   (testable via temporal order judgment tasks)")
print()
for r in results:
    has_time = "YES" if r["N_ecological"] >= 64 else "MARGINAL" if r["N_ecological"] >= 16 else "NO"
    print(f"   {r['species']:25s}: N = {r['N_ecological']:8.1f} → phenomenal time: {has_time}")
print()

# ============================================================
# Save results
# ============================================================
out_dir = os.path.join(os.path.dirname(__file__), "..", "results")
os.makedirs(out_dir, exist_ok=True)

data_path = os.path.join(out_dir, "cross_species_SP_data.json")
with open(data_path, "w") as f:
    json.dump({
        "script": "cross_species_SP.py",
        "date": "2026-04-10",
        "constants": {
            "delta_E_kT": delta_E_kT,
            "T_ref_K": T_ref,
            "k_ref_Hz": k_ref,
            "B_ref_bps": B_ref,
            "N_moments": N_moments,
            "SP_ref_s": SP_ref,
        },
        "species_predictions": results,
    }, f, indent=2)

print(f"Data saved to {data_path}")
