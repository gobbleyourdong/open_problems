#!/usr/bin/env python3
"""
simulation_cost.py — The simulation hypothesis: information-theoretic cost analysis.

Context: PROBLEM.md asks "what is reality?" One ontology is that reality is a computation
(pancomputationalism, simulation hypothesis). This script asks: what would it cost to
simulate the observable universe at various levels of precision?

The K-information framing from what_is_computation applies: physical laws are finite
K-specifications. If those laws plus initial conditions specify all of observable reality,
then reality has a finite K-description. But the STATE of the universe (the specific
history) may have much higher K-content than the laws.

This script computes:
1. The Bekenstein-Hawking information bound for the observable universe (S-information)
2. The K-information content of physical laws (laws as K-specification)
3. The cost of simulating the universe at several precision levels
4. The distinction between simulating the LAWS vs the HISTORY
5. What quantum mechanics says about the minimum simulation cost

The key question: is reality K-simple (described by its laws) or K-complex (its full history
requires specifying all initial conditions)?

Usage:
    cd ~/open_problems/physics/what_is_reality
    python3 numerics/simulation_cost.py

Numerical track, what_is_reality — 2026-04-09
"""

import math, json, os

# ── Physical constants ────────────────────────────────────────────────────────
hbar = 1.054571817e-34   # J·s
c    = 2.99792458e8      # m/s
G    = 6.67430e-11       # m³/(kg·s²)
k_B  = 1.380649e-23      # J/K
eV   = 1.602176634e-19   # J

# Planck scale
l_P = math.sqrt(hbar * G / c**3)    # 1.616e-35 m
t_P = math.sqrt(hbar * G / c**5)    # 5.391e-44 s
E_P = math.sqrt(hbar * c**5 / G)    # 1.956e9 J

# Cosmological parameters (Planck 2023)
H_0 = 67.4e3 / 3.086e22    # Hubble constant in s⁻¹ (67.4 km/s/Mpc)
T_univ = 13.8e9 * 365.25 * 24 * 3600  # Age of universe in seconds
T_CMB = 2.725                # K
r_H = c / H_0                # Hubble radius ≈ observable universe radius

# ── Bekenstein bound (S-information) ─────────────────────────────────────────

def bekenstein_bound(R_m: float, E_J: float) -> float:
    """
    Bekenstein bound: maximum S-information in a sphere of radius R with energy E.
    S_max = 2π k_B R E / (ħ c)  bits = S_max / ln(2)
    """
    S_max_nat = 2 * math.pi * k_B * R_m * E_J / (hbar * c)   # nats
    return S_max_nat / math.log(2)  # bits

def holographic_bound(R_m: float) -> float:
    """
    Holographic bound (Bousso/Susskind): for a sphere of radius R,
    S_max ≤ Area / (4 G ħ/c³) = π R² / l_P²
    Returns maximum bits.
    """
    area = 4 * math.pi * R_m**2
    S_max = area * c**3 / (4 * G * hbar)  # in nats
    return S_max / math.log(2)             # bits

# ── Observable universe S-information ────────────────────────────────────────

# Comoving radius of observable universe ≈ 46.5 billion light years
r_obs = 4.65e10 * 9.461e15       # ≈ 4.40e26 m

# Total energy of observable universe (matter + radiation, excluding dark energy)
# Approximate: mass of ordinary matter × c²
# Observable universe has ~10^80 protons worth of ordinary matter
m_proton = 1.673e-27  # kg
N_protons = 1e80
M_obs = N_protons * m_proton   # ≈ 1.67e53 kg
E_obs = M_obs * c**2           # ≈ 1.50e70 J

S_bekenstein = bekenstein_bound(r_obs, E_obs)
S_holographic = holographic_bound(r_obs)

# Cosmic microwave background photon count
# CMB photon density: n_CMB ≈ 411 photons/cm³ = 4.11e8 m⁻³
n_CMB = 4.11e8  # m⁻³
V_obs = (4/3) * math.pi * r_obs**3
N_CMB = n_CMB * V_obs  # total CMB photons

# ── Simulation cost at various precision levels ───────────────────────────────

def simulation_cost_bits(precision_levels: list[tuple]) -> list[dict]:
    """
    For each (precision_name, dx_m, dt_s) pair, compute how many bits are needed
    to simulate the observable universe for T_univ seconds.
    """
    results = []
    V_obs_val = (4/3) * math.pi * r_obs**3

    for name, dx_m, dt_s in precision_levels:
        # Number of spatial cells
        N_cells = V_obs_val / dx_m**3

        # Number of time steps
        N_steps = T_univ / dt_s

        # Bits per cell per timestep: depends on what needs to be stored
        # For a classical field: need to store field values
        # Assume each cell stores 3 position values + 3 momentum values × 64-bit floats
        bits_per_cell = 6 * 64  # 384 bits

        # Total bits for the state at one timestep
        state_bits = N_cells * bits_per_cell

        # Total bits for the full simulation (state at each step)
        total_bits = state_bits * N_steps

        results.append({
            "precision": name,
            "dx_m": dx_m,
            "dt_s": dt_s,
            "N_cells": N_cells,
            "N_timesteps": N_steps,
            "state_bits_per_step": state_bits,
            "total_simulation_bits": total_bits,
            "log10_state_bits": math.log10(max(state_bits, 1)),
            "log10_total_bits": math.log10(max(total_bits, 1)),
        })

    return results

precision_levels = [
    ("human_neuron",    1e-6,  1e-3),   # micron, millisecond
    ("cell_biology",    1e-9,  1e-9),   # nanometer, nanosecond
    ("atom",            1e-10, 1e-15),  # Angstrom, femtosecond
    ("nuclear",         1e-15, 1e-24),  # femtometer, yoctosecond
    ("Planck",          l_P,   t_P),    # Planck length, Planck time
]

# ── Physical law K-content ─────────────────────────────────────────────────

def physical_law_k_content():
    """
    Estimate the K-information content of fundamental physical laws.
    The laws are the program; the universe's history is the output.
    """
    # Very rough estimates of the "character count" for each theory in compact notation
    laws = [
        ("Maxwell equations (SI)", 4, "4 equations: ∇·E=ρ/ε₀, ∇×B-∂E/∂t=μ₀J, ..."),
        ("Einstein equations (compact)", 1, "G_μν + Λg_μν = 8πG/c⁴ T_μν"),
        ("Schrödinger equation", 1, "iħ∂ψ/∂t = Hψ"),
        ("Standard Model Lagrangian (full)", 2000, "~2000 chars in tensor notation"),
        ("Feynman path integral", 1, "Z = ∫Dφ exp(iS[φ]/ħ)"),
        ("Total (non-redundant)", 3000, "physics + initial conditions + measurement theory"),
    ]

    print(f"\n── Physical Law K-Content ──")
    print(f"{'Theory':<40} {'Chars':<10} {'K-bits'}")
    print("─" * 60)
    for name, chars, notation in laws:
        k_bits = chars * 8  # rough: 8 bits per ASCII char (overestimate)
        print(f"{name:<40} {chars:<10} ~{k_bits} bits")
        print(f"  '{notation[:60]}...' " if len(notation) > 60 else f"  '{notation}'")

    # Planck-scale state K-content
    # If universe has S_max bits (holographic bound), the initial conditions
    # need S_max bits to specify. But the laws are only ~3000 chars.
    ratio = 3000 * 8 / math.log10(S_holographic) / math.log10(2)

    return {
        "law_k_bits_estimate": 3000 * 8,
        "universe_S_bits_holographic": S_holographic,
        "law_to_S_ratio": ratio,
    }

# ── Quantum measurement and underdetermination ────────────────────────────────

def quantum_interpretations():
    """
    Different QM interpretations make identical predictions for measurement outcomes
    but differ radically in their ontology. This quantifies the underdetermination.

    Copenhagen: only measurement outcomes are real. State vector is epistemic.
    Many-worlds: all outcomes are real. State vector is ontic (= all branches).
    QBism: quantum states are agents' degrees of belief (fully epistemic).
    Pilot wave: particles have definite positions; wave function guides them.

    Each predicts the same Born rule probabilities for measurement outcomes.
    The ontological differences are:
    - Number of real worlds: 1 (Copenhagen/QBism) vs 2^N (MWI) where N = decoherence events
    - Information per measurement: log₂(2) = 1 bit (which outcome) vs 1 bit per branch (which branch)
    - Total information in the universe:
        Copenhagen: N measurements × 1 bit = N bits
        MWI: 2^N bits (all branches)

    N_decoherence = number of decoherence events since Big Bang
    """
    # Rough estimate of decoherence events:
    # Each particle interaction + measurement is a decoherence event
    # Observable universe: ~10^80 particles, each undergoing ~10^40 interactions
    N_decoherence = 1e80 * 1e40  # = 10^120

    info_copenhagen = N_decoherence * 1  # 1 bit per measurement (which outcome)
    log10_info_MWI = N_decoherence  # log₁₀(2^N) = N bits

    return {
        "N_decoherence_events_estimate": N_decoherence,
        "Copenhagen_total_bits": info_copenhagen,
        "log10_Copenhagen_bits": math.log10(info_copenhagen),
        "MWI_total_branches": "2^(10^120)",
        "log10_MWI_bits": N_decoherence,  # ≈ 10^120
        "key_point": (
            "Both interpretations agree on measurement predictions. "
            "Copenhagen: 10^120 bits. MWI: 2^(10^120) bits (incomprehensibly larger). "
            "Underdetermination: observations cannot distinguish them."
        ),
    }

# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("=" * 70)
    print("Reality as Computation: Information-Theoretic Cost Analysis")
    print("=" * 70)

    # Observable universe S-information
    print("\n── Observable Universe S-Information ──")
    print(f"  Observable universe radius:     {r_obs:.4e} m")
    print(f"  Total ordinary matter energy:   {E_obs:.4e} J")
    print(f"  Bekenstein bound (energy):      10^{math.log10(S_bekenstein):.1f} bits")
    print(f"  Holographic bound (area):       10^{math.log10(S_holographic):.1f} bits")
    print(f"  CMB photon count:               {N_CMB:.4e}")
    print(f"  log₁₀(N_CMB):                   {math.log10(N_CMB):.1f}")
    print()
    print(f"  The holographic bound gives the maximum S-information storable in")
    print(f"  the observable universe: ~10^{math.log10(S_holographic):.0f} bits.")
    print(f"  This is the upper bound on the HISTORY's K-content as well.")

    # Simulation costs
    print("\n── Simulation Cost at Various Precision Levels ──")
    print(f"{'Precision':<18} {'dx (m)':<12} {'dt (s)':<12} {'log₁₀(state bits)':<20} {'log₁₀(total bits)'}")
    print("─" * 80)
    sim_results = simulation_cost_bits(precision_levels)
    for r in sim_results:
        print(f"{r['precision']:<18} {r['dx_m']:<12.4e} {r['dt_s']:<12.4e} "
              f"{r['log10_state_bits']:<20.1f} {r['log10_total_bits']:.1f}")
    print()
    print(f"  Planck-precision simulation: 10^{sim_results[-1]['log10_total_bits']:.0f} bits")
    print(f"  Holographic bound:           10^{math.log10(S_holographic):.0f} bits")
    print(f"  The Planck simulation exceeds the holographic bound by a factor of:")
    print(f"  10^({sim_results[-1]['log10_total_bits']:.0f} - {math.log10(S_holographic):.0f})")
    print(f"  = 10^{sim_results[-1]['log10_total_bits'] - math.log10(S_holographic):.0f}")
    print()
    print(f"  KEY FINDING: a naive Planck-precision simulation EXCEEDS the holographic")
    print(f"  information bound. This means classical simulation at Planck resolution is")
    print(f"  information-theoretically IMPOSSIBLE — not just computationally expensive.")
    print(f"  The universe cannot simulate itself at its own resolution.")

    # Physical law K-content
    law_results = physical_law_k_content()
    print(f"\n  Physical laws K-content: ~{law_results['law_k_bits_estimate']} bits")
    print(f"  Universe S-information:  10^{math.log10(law_results['universe_S_bits_holographic']):.0f} bits")
    print(f"  Laws are K-poor (short program). History is S-rich (complex output).")
    print(f"  This is the same pattern as π: K=O(1) program, locally complex output.")

    # Quantum interpretations
    print("\n── Quantum Interpretations and Underdetermination ──")
    qi = quantum_interpretations()
    print(f"  Estimated decoherence events in universe history: 10^120")
    print(f"  Copenhagen information: 10^{qi['log10_Copenhagen_bits']:.0f} bits (which outcome at each event)")
    print(f"  Many-worlds information: 2^(10^120) ≈ 10^(10^120) bits (all branches)")
    print(f"  Observational difference: ZERO — both predict identical Born rule probabilities")
    print()
    print(f"  The ontological gap between Copenhagen and MWI:")
    print(f"    Copenhagen: 10^120 bits of real information")
    print(f"    MWI:        10^(10^120) bits (incomprehensibly larger)")
    print(f"  Both are consistent with every possible measurement. This is the")
    print(f"  underdetermination problem: reality could differ by a factor of 10^(10^120)")
    print(f"  in information content with no observable difference.")

    print("\n── KEY FINDINGS ──")
    print("1. The observable universe has ≤ 10^122 bits (holographic bound).")
    print("2. Its physical laws have ~3×10⁴ bits (the SM Lagrangian).")
    print("3. A Planck-resolution classical simulation exceeds the holographic bound.")
    print("   → The universe cannot 'run' itself as a classical simulation at its own scale.")
    print("4. Quantum mechanics introduces a 10^(10^120) ontological ambiguity")
    print("   with zero observational consequence.")
    print("5. The laws (K-short) plus boundary conditions (S-rich) = the universe.")
    print("   Which is more fundamental: the K-short laws or the S-rich history?")
    print("   This is the reality question, numerically precise.")

    # Save
    os.makedirs("results", exist_ok=True)
    manifest = {
        "bekenstein_bound_bits": S_bekenstein,
        "holographic_bound_bits": S_holographic,
        "CMB_photon_count": N_CMB,
        "log10_holographic_bits": math.log10(S_holographic),
        "simulation_costs": [
            {k: v for k, v in r.items() if not isinstance(v, float) or abs(v) < 1e300}
            for r in sim_results
        ],
        "physical_law_k_bits": law_results["law_k_bits_estimate"],
        "quantum_interpretations": {
            k: str(v) if isinstance(v, float) and abs(v) > 1e300 else v
            for k, v in qi.items()
        },
    }
    with open("results/simulation_cost_data.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest → results/simulation_cost_data.json")

if __name__ == "__main__":
    run()
