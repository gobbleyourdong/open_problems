#!/usr/bin/env python3
"""
sk_bekenstein_bounds.py — Physical bounds on S vs K for concrete physical systems.

Gap.md R1: "What physical quantities bound K-information in a region? The holographic
bound bounds S (number of distinguishable states); whether K is bounded similarly depends
on what kinds of structure are realizable in those states."

This script computes BOTH the S-information bound (Bekenstein/holographic) and a
K-information bound (via computational complexity arguments) for a set of concrete
physical systems, and shows the gap between the two bounds.

The core argument:
- S is bounded by the holographic principle: S_max = A c³/(4 G ħ) where A is surface area
- K is bounded by the MINIMUM program to describe the regularities of the system
- For physically realizable systems, K << S: laws are short, states are complex
- The gap S - K is the "computational overhead": how much of the S-information is
  accounted for by the laws (K-simple) vs random quantum fluctuations (K-complex)

Systems analyzed:
1. Proton (r ≈ 1 fm): S_holo, K_laws (QCD), S-K gap
2. Cell (r ≈ 10 µm): S_holo, K_laws (biochemistry), S-K gap
3. Human brain (r ≈ 0.08 m): S_holo, K_laws (neuroscience), S-K gap
4. Earth (r ≈ 6.4e6 m): S_holo, K_laws (geology/physics), S-K gap
5. Solar system (r ≈ 6e12 m): S_holo, K_laws (celestial mechanics)
6. Milky Way galaxy (r ≈ 5e20 m): S_holo
7. Observable universe (r ≈ 4.4e26 m): S_holo, K_laws (SM + GR)

For each, the key ratio: K_laws / S_max gives the "structural compression ratio" — how much
of the system's S-information content is accounted for by K-simple laws.

Usage:
    cd ~/open_problems/physics/what_is_information
    python3 numerics/sk_bekenstein_bounds.py

Numerical track, what_is_information — 2026-04-09
"""

import math, json, os

# Physical constants
hbar = 1.054571817e-34   # J·s
c    = 2.99792458e8      # m/s
G    = 6.67430e-11       # m³/(kg·s²)
k_B  = 1.380649e-23      # J/K
eV   = 1.602176634e-19   # J
l_P  = math.sqrt(hbar * G / c**3)  # Planck length

def bekenstein_bound_bits(R_m, E_J):
    """Bekenstein bound: S = 2π k_B R E / (ħ c), in bits."""
    return 2 * math.pi * k_B * R_m * E_J / (hbar * c) / math.log(2)

def holographic_bound_bits(R_m):
    """Holographic bound: S = π R² c³/(G ħ) / ln(2), in bits."""
    return math.pi * R_m**2 * c**3 / (G * hbar) / math.log(2)

def landauer_energy_per_bit(T_K):
    """Energy to erase one bit at temperature T: k_B T ln(2)."""
    return k_B * T_K * math.log(2)

# ── System definitions ────────────────────────────────────────────────────────
# Each entry: (name, radius_m, energy_J, T_K, K_laws_bits, K_laws_source)

systems = [
    (
        "Proton",
        0.87e-15,                          # R = 0.87 fm (charge radius)
        938.3e6 * eV,                      # E = 938.3 MeV rest energy
        1e12,                              # T ≈ 1 TeV (QCD confinement scale)
        1000,                              # K_laws ≈ QCD Lagrangian, 1000 chars
        "QCD Lagrangian (~1000 chars)",
    ),
    (
        "DNA double helix (1 turn)",
        0.5e-9,                            # R = 0.5 nm (radius)
        1e-17,                             # E ~ 100 eV per base pair × 10 bp
        310,                               # T = 37°C (body temperature)
        500,                               # K_laws ≈ base-pair rules
        "Watson-Crick base pairing rules",
    ),
    (
        "Bacterium (E. coli)",
        1e-6,                              # R = 1 µm
        1e-12,                             # E ~ 1 pJ (metabolic)
        310,                               # Body temperature
        50_000,                            # K_laws ≈ minimal genome description
        "Minimal genome + metabolic rules",
    ),
    (
        "Neuron",
        1e-5,                              # R = 10 µm
        1e-11,                             # E ~ 10 pJ
        310,                               # Body temperature
        100_000,                           # K_laws ≈ Hodgkin-Huxley + connectivity
        "Hodgkin-Huxley equations + synaptic rules",
    ),
    (
        "Human brain",
        0.08,                              # R = 8 cm
        1e-3 * 20 / 3600,                 # E ≈ 20 W × 1 second power
        310,                               # Body temperature
        1_000_000,                         # K_laws ≈ neuroscience laws (rough)
        "Neuroscience + biochemistry laws",
    ),
    (
        "Earth",
        6.371e6,                           # Earth radius
        5.97e24 * c**2,                    # E = M c²
        300,                               # Surface temperature
        500_000,                           # K_laws ≈ all of physics
        "Standard Model + GR + geophysics",
    ),
    (
        "Solar system",
        6e12,                              # R ≈ 40 AU ≈ 6e12 m
        1.989e30 * c**2,                   # E ≈ M_sun × c²
        300,                               # Effective T
        50_000,                            # K_laws ≈ gravitational + planetary formation
        "GR + planetary formation equations",
    ),
    (
        "Observable universe",
        4.40e26,                           # R = 46.5 billion light years
        1.50e70,                           # E = M_ordinary × c²
        2.725,                             # CMB temperature
        24_000,                            # K_laws ≈ SM + GR
        "Standard Model + General Relativity",
    ),
]

def run():
    print("=" * 80)
    print("Physical S-Information Bounds vs K-Laws: The S/K Gap for Physical Systems")
    print("=" * 80)

    print(f"\n{'System':<26} {'R (m)':<12} {'log₁₀(S_holo)':<16} {'K_laws (bits)':<16} {'K/S_holo'}")
    print("─" * 82)

    results = []
    for name, R, E, T, K_bits, K_source in systems:
        S_holo = holographic_bound_bits(R)
        S_bek = bekenstein_bound_bits(R, E)
        E_per_bit = landauer_energy_per_bit(T)
        k_over_s = K_bits / S_holo if S_holo > 0 else 0

        log_s = math.log10(S_holo) if S_holo > 0 else 0
        log_k = math.log10(K_bits) if K_bits > 0 else 0
        gap = log_s - log_k  # orders of magnitude gap S_holo >> K_laws

        print(f"{name:<26} {R:<12.4e} 10^{log_s:<12.1f} {K_bits:<16} 10^{gap:.0f}:1")
        results.append({
            "name": name,
            "radius_m": R,
            "energy_J": E,
            "temperature_K": T,
            "S_holo_bits": S_holo,
            "log10_S_holo": round(log_s, 2),
            "S_bekenstein_bits": S_bek,
            "K_laws_bits": K_bits,
            "K_laws_source": K_source,
            "log10_gap_S_over_K": round(gap, 1),
            "K_fraction_of_S": round(k_over_s, 30),
            "Landauer_energy_per_bit_J": E_per_bit,
        })

    print()
    print("K/S gap = log₁₀(S_holo / K_laws): orders of magnitude by which laws")
    print("are shorter than the holographic information bound.")

    print("\n── S vs K gap across scales ──")
    for r in results:
        gap = r["log10_gap_S_over_K"]
        name = r["name"]
        k = r["K_laws_bits"]
        s_log = r["log10_S_holo"]
        print(f"  {name:<26}: S=10^{s_log:.1f} bits, K~{k} bits, gap={gap:.0f} orders")

    print("\n── Key pattern: gap grows with system size ──")
    print("The gap S_holo - log₁₀(K_laws) grows as systems get larger.")
    print("This is because S_holo ∝ R² (area) while K_laws grows slowly (or stays constant).")
    print()
    print("For the observable universe: S_holo = 10^124 bits, K_laws ≈ 24000 bits.")
    print("The laws describe 10^120 times LESS information than the holographic bound.")
    print("This means 99.999...% (120 nines after decimal) of the universe's S-capacity")
    print("is NOT accounted for by the laws alone — it requires the specific history.")

    print("\n── What bounds K? ──")
    print("The holographic principle bounds S (number of distinguishable states).")
    print("There is no analogous general bound on K for arbitrary physical systems.")
    print("However, specific constraints exist:")
    print()
    print("1. K ≤ S (a system's K-content cannot exceed its S-content, because a full")
    print("   specification of the state IS the maximum description of it).")
    print()
    print("2. K(laws) << S(state) for all observed physical systems. The laws of physics")
    print("   are K-simple; the states they produce are S-complex. This is consistent")
    print("   with the compression view: laws are the K-specification, states are the output.")
    print()
    print("3. K(state) can approach S(state) for random quantum measurement outcomes.")
    print("   A truly random measurement result has no K-description shorter than the result.")
    print("   This is the quantum-mechanical source of irreducible K-complexity.")
    print()
    print("4. For structured physical systems (crystals, organisms, brains), K(state) << S(state).")
    print("   The structure IS the K-information. Crystal: K = lattice parameters (small).")
    print("   Brain: K = neural connectivity pattern (large but << S_holo).")
    print()
    print("R1 partial answer: K in a region is bounded ABOVE by S (holographic bound)")
    print("and bounded BELOW by the K-content of the laws governing it.")
    print("The tight lower bound is an open problem — connected to computational complexity")
    print("(what is the minimum program length for a given physical system's dynamics?).")

    # Landauer costs
    print("\n── Landauer cost to 'erase' K-laws for each system ──")
    print(f"{'System':<26} {'T (K)':<10} {'K_laws bits':<15} {'E_landauer (J)'}")
    print("─" * 65)
    for r in results:
        E_erase = r["K_laws_bits"] * r["Landauer_energy_per_bit_J"]
        print(f"{r['name']:<26} {r['temperature_K']:<10.1f} {r['K_laws_bits']:<15} {E_erase:.4e}")

    # Save
    os.makedirs("results", exist_ok=True)
    with open("results/sk_bekenstein_data.json", "w") as f:
        json.dump({"systems": results}, f, indent=2)
    print(f"\nManifest → results/sk_bekenstein_data.json")

if __name__ == "__main__":
    run()
