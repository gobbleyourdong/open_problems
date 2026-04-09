#!/usr/bin/env python3
"""
zeno_maxwell.py — Quantum Zeno Effect and Maxwell's Demon as K-information arguments.

Context: quantum_K_change.py established that unitary evolution K=0 and
measurement K = -log2(P). Two famous phenomena are essentially K-information
arguments in disguise:

1. QUANTUM ZENO EFFECT
   Frequent measurement "freezes" a quantum system. K-view: frequent measurements
   force K-change ≈ 0 (outcomes near-certain) → total K-accumulation → 0 as N → ∞.

2. MAXWELL'S DEMON
   A demon sorts gas molecules by speed, seemingly violating the 2nd law.
   Resolution (Szilard 1929, Landauer 1961): the demon must erase its memory,
   costing k_B T ln(2) per bit. K-view: the demon's acquisition of K-information
   and its mandatory erasure are the same act seen from two sides. K-acquisition
   by demon = entropy decrease in gas = Landauer erasure cost. Net ΔS ≥ 0.

3. GAP.MD R1 — CAUSATION
   The demon demonstrates K-change IS physical intervention. Landauer-Szilard is
   the interventionist causal theory made quantitative: an intervention acquires
   K about the system and uses it to modify the system's state.

Usage:
    cd ~/open_problems/physics/what_is_change
    python3 numerics/zeno_maxwell.py

Numerical track, what_is_change — 2026-04-09
"""

import math
import json
import os

# ── Physical constants ────────────────────────────────────────────────────────

k_B = 1.380649e-23   # J/K  Boltzmann constant
ln2 = math.log(2)

T_room = 300.0        # K   representative room temperature


# ── Utility ───────────────────────────────────────────────────────────────────

def safe_log2(p: float) -> float:
    """log2(p) returning +inf for p == 0 (K-change of impossible event)."""
    if p <= 0.0:
        return math.inf
    return -math.log2(p)


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1 — QUANTUM ZENO EFFECT
# ═══════════════════════════════════════════════════════════════════════════════
#
# Model: qubit precessing under H = ω σ_x / 2.
#   Initial state: |0⟩.
#   After time t (no measurement): P(|1⟩) = sin²(ωt/2).
#
# Full period T = π/ω  (where P(|1⟩) = sin²(π/2) = 1 without interruption).
#
# With N measurements evenly spaced in [0, T]:
#   Each measurement is at time t_k = k·T/N.
#   After each small step Δt = T/N, starting from |0⟩, the probability of
#   finding |1⟩ is:
#       P_step = sin²(ω·Δt/2) = sin²(π/(2N))
#
#   After each measurement the state collapses:
#     - if measured |0⟩ (prob 1 - P_step): reset to |0⟩, continue precessing.
#     - if measured |1⟩ (prob P_step): chain broken, we record this.
#
#   The probability that the qubit survives to the END in |0⟩ (never been
#   caught in |1⟩) is:
#       P_survive = (1 - P_step)^N
#
#   So the probability of being in |1⟩ at the end of the full period:
#       P_final_1 = 1 - (1 - sin²(π/(2N)))^N
#
# For each step measurement (if we are still in |0⟩), the step probability
# of |0⟩ is (1 - P_step), so:
#   K per step  = -log2(1 - P_step)  [only counting the |0⟩ outcome that keeps us going]
#
# Total K accumulated (conditional on surviving all N steps in |0⟩):
#   K_total = N × (-log2(1 - P_step))
#
# As N → ∞:  P_step → (π/(2N))²  (small-angle)
#   K_total ≈ N × P_step / ln2 = N × (π/(2N))² / ln2 = π²/(4N·ln2) → 0.
#
# This is the Zeno effect in K-information language: infinite measurement
# frequency drives total K-accumulation to zero.

def zeno_analysis(N_values: list[int]) -> list[dict]:
    """
    Compute the Zeno effect numerically for each measurement count N.

    Returns a list of dicts, one per N value.
    """
    results = []
    for N in N_values:
        # Small-step probability of finding |1⟩ in one interval
        angle_step = math.pi / (2 * N)   # ω·Δt/2 = (π/ω) / (2N) × ω/2 = π/(2N)
        P_step = math.sin(angle_step) ** 2

        # Probability that ALL N steps end in |0⟩ (survive = never transition)
        P_survive_0 = (1.0 - P_step) ** N

        # Final probability of |1⟩ (at least one step found |1⟩)
        P_final_1 = 1.0 - P_survive_0

        # K per step — the surprise of the |0⟩ outcome (near-certain as N grows)
        K_per_step = safe_log2(1.0 - P_step)  # = -log2(P(|0⟩ per step))

        # Total K accumulated across all N steps (summing the per-step K)
        # This is the K the environment collects by watching N near-certain outcomes.
        K_total = N * K_per_step if not math.isinf(K_per_step) else math.inf

        # Comparison: no measurements — free precession K-change at end of T
        # Unitary evolution is K=0 by quantum_K_change.py; K-change only at collapse.
        # Without any intermediate measurement, P(|1⟩ at T) = sin²(π/2) = 1.0
        # (complete flip).  If we measured ONCE at the end:
        P_free_1 = 1.0      # sin²(π/2)
        K_free_single = safe_log2(P_free_1)   # = 0 bits (certain outcome)

        results.append({
            "N": N,
            "angle_step_rad": angle_step,
            "P_step_1": P_step,
            "P_survive_0": P_survive_0,
            "P_final_1": P_final_1,
            "K_per_step_bits": K_per_step,
            "K_total_bits": K_total,
            "note": (
                f"N={N}: P_step={P_step:.6f}, survive={P_survive_0:.6f}, "
                f"P(|1⟩)={P_final_1:.6f}, K/step={K_per_step:.6f}, "
                f"K_total={K_total:.6f} bits"
            ),
        })
    return results


def zeno_small_angle_approximation(N_values: list[int]) -> list[dict]:
    """
    Small-angle approximation for large N:
    P_step ≈ (π/(2N))²
    K_total ≈ π²/(4N·ln2)

    Shows analytically that K_total → 0 as 1/N.
    """
    results = []
    for N in N_values:
        P_step_approx = (math.pi / (2 * N)) ** 2
        K_total_approx = math.pi ** 2 / (4 * N * ln2)
        results.append({
            "N": N,
            "P_step_approx": P_step_approx,
            "K_total_approx_bits": K_total_approx,
        })
    return results


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2 — MAXWELL'S DEMON
# ═══════════════════════════════════════════════════════════════════════════════
#
# Toy model: 2 particles in a box, each independently equally likely to be
# "fast" or "slow" (binary speed classification).
#
# BEFORE DEMON:
#   Each particle: 2 equally probable states → entropy H = 1 bit per particle.
#   2-particle gas entropy: H_gas = 2 bits.
#
# DEMON MEASURES particle 1 speed (acquires 1 bit of K):
#   Demon memory transitions from "blank" (maximal entropy) to "fast" or "slow".
#   K_demon = 1 bit.
#   After measurement: particle 1's state is now known → conditional entropy = 0.
#   Gas entropy (particle 1 only): ΔH_gas_1 = -1 bit.
#
# DEMON SORTS: uses its 1-bit K to open/close the partition.
#   Fast particles go right, slow particles go left.
#   After sorting 1 particle: H_gas decreases by 1 bit.
#   ΔH_gas = -1 bit.
#
# DEMON ERASES its memory (Landauer):
#   Erasure of 1 bit at temperature T costs k_B T ln(2) joules.
#   This heat goes into the environment → ΔS_environment = +k_B ln(2) = +1 bit × k_B.
#
# NET ENTROPY BALANCE:
#   ΔS_gas       = -1 bit × k_B ln(2)   (sorted = less entropy)
#   ΔS_demon     =  0                    (memory returned to blank after erasure)
#   ΔS_environment = +1 bit × k_B ln(2)  (Landauer erasure heat)
#   ΔS_total     =  0                    (conservation, 2nd law saturated)
#
# The exact cancellation: K-acquisition = entropy decrease = Landauer erasure.

def maxwell_demon_2particle(T: float = T_room) -> dict:
    """
    Maxwell's demon with 2 particles.

    Each particle independently has probability 0.5 of being "fast" or "slow".
    The demon measures one particle, sorts it, then erases its memory.

    Returns a full accounting of entropy flows in bits and joules.
    """
    # ── Initial gas state ─────────────────────────────────────────────────────
    n_particles = 2
    n_speed_states = 2   # fast or slow
    H_per_particle = math.log2(n_speed_states)   # 1 bit each (uniform distribution)
    H_gas_initial = n_particles * H_per_particle  # 2 bits total

    # ── Demon's initial memory (blank register) ───────────────────────────────
    # A blank register is a pure state: 0 bits of entropy.
    H_demon_initial = 0.0    # bits — memory in a definite "blank" state

    # ── Step 1: Demon measures particle 1 speed ───────────────────────────────
    # Demon observes: "fast" with prob 0.5, "slow" with prob 0.5.
    P_fast = 0.5
    P_slow = 0.5

    # K-information acquired by demon = Shannon info of measurement outcome
    K_acquired_fast = -math.log2(P_fast)   # 1 bit
    K_acquired_slow = -math.log2(P_slow)   # 1 bit
    K_demon_acquired = P_fast * K_acquired_fast + P_slow * K_acquired_slow  # expected K = 1 bit

    # Demon memory after measurement: 1 bit of definite K (knows "fast" or "slow")
    H_demon_after_measure = 1.0   # bits — memory now encodes the measurement

    # Gas entropy after measurement:
    # Particle 1 is now known → its conditional entropy = 0.
    # Particle 2 is still unknown → H = 1 bit.
    H_gas_after_measure = (n_particles - 1) * H_per_particle   # 1 bit

    delta_H_gas_from_measurement = H_gas_after_measure - H_gas_initial  # -1 bit

    # ── Step 2: Demon sorts using its K ───────────────────────────────────────
    # The demon opens/closes a partition based on its 1-bit memory.
    # This correlates the particle's position with its speed classification.
    # The gas positional entropy does not further change (particle 1 is already
    # in the right side after sorting; the action itself is macroscopic and
    # the information cost was already accounted in Step 1).
    # Net: demon's K is "used up" in directing particle 1 — but the memory
    # still holds the record.
    delta_H_gas_from_sorting = 0.0   # already counted in measurement step
    # (In the Szilard engine, the work extracted from the expansion of the
    # 1-particle box is exactly k_B T ln(2) per bit — see below.)

    # Szilard work extracted from 1-bit K:
    W_extracted_J = k_B * T * ln2   # joules — isothermal expansion of 1-molecule box
    W_extracted_bits = 1.0           # 1 bit worth of work

    # ── Step 3: Demon erases its 1-bit memory (Landauer) ─────────────────────
    # Erasure of 1 bit costs k_B T ln(2) joules dissipated to environment.
    bits_erased = K_demon_acquired   # 1 bit
    E_erasure_J = k_B * T * ln2 * bits_erased
    E_erasure_bits = bits_erased     # in information units

    # ΔS of environment from erasure heat
    delta_S_env_J_per_K = E_erasure_J / T     # = k_B ln(2) J/K
    delta_S_env_bits = E_erasure_J / (k_B * T * ln2)   # = 1 bit (in bit units)

    # ── Step 4: Demon memory after erasure ────────────────────────────────────
    H_demon_after_erasure = 0.0   # blank again — same as initial

    # ── Entropy balance ───────────────────────────────────────────────────────
    delta_S_gas_bits = H_gas_after_measure - H_gas_initial   # -1 bit
    delta_S_demon_bits = H_demon_after_erasure - H_demon_initial  # 0 bits
    delta_S_env_bits_final = delta_S_env_bits   # +1 bit
    delta_S_total_bits = delta_S_gas_bits + delta_S_demon_bits + delta_S_env_bits_final

    # ── Szilard engine work-heat balance ──────────────────────────────────────
    # Work extracted from gas expansion: +k_B T ln(2) joules.
    # Heat deposited by erasure to environment: +k_B T ln(2) joules.
    # Net work output of full cycle: W_extracted - E_erasure = 0. (No free energy.)
    net_work_J = W_extracted_J - E_erasure_J

    return {
        "T_K": T,
        "n_particles": n_particles,
        "n_speed_states": n_speed_states,
        "H_per_particle_bits": H_per_particle,
        "H_gas_initial_bits": H_gas_initial,
        "H_demon_initial_bits": H_demon_initial,
        # Measurement step
        "K_acquired_per_outcome_bits": K_acquired_fast,
        "K_demon_acquired_expected_bits": K_demon_acquired,
        "H_gas_after_measure_bits": H_gas_after_measure,
        "delta_H_gas_from_measurement_bits": delta_H_gas_from_measurement,
        # Sorting step
        "W_szilard_extracted_J": W_extracted_J,
        "W_szilard_extracted_bits": W_extracted_bits,
        # Erasure step
        "bits_erased": bits_erased,
        "E_landauer_erasure_J": E_erasure_J,
        "delta_S_env_from_erasure_bits": delta_S_env_bits,
        "delta_S_env_from_erasure_J_per_K": delta_S_env_J_per_K,
        # After erasure
        "H_demon_after_erasure_bits": H_demon_after_erasure,
        # Entropy balance
        "delta_S_gas_bits": delta_S_gas_bits,
        "delta_S_demon_bits": delta_S_demon_bits,
        "delta_S_env_bits": delta_S_env_bits_final,
        "delta_S_total_bits": delta_S_total_bits,
        # Work balance
        "net_work_output_J": net_work_J,
        # K-information identity
        "K_acquisition_equals_entropy_reduction": abs(K_demon_acquired + delta_S_gas_bits) < 1e-12,
        "K_acquisition_equals_landauer_erasure": abs(K_demon_acquired - bits_erased) < 1e-12,
        "landauer_erasure_equals_env_entropy_increase": abs(bits_erased - delta_S_env_bits_final) < 1e-12,
        "second_law_satisfied": delta_S_total_bits >= -1e-12,
    }


def maxwell_demon_N_particles(n: int, T: float = T_room) -> dict:
    """
    Generalise to N particles: demon acquires log2(N) bits per full sort,
    each bit costs Landauer erasure, net ΔS = 0.

    For N particles with n_speed_states speed classes each, the demon sorts
    particles by speed. Here we use the binary (fast/slow) classification
    and model the demon measuring each particle independently.
    """
    n_speed_states = 2
    H_per_particle = math.log2(n_speed_states)   # 1 bit
    H_gas_initial = n * H_per_particle            # n bits

    # Demon measures all n particles: acquires n bits of K
    K_demon_total = n * H_per_particle   # n bits

    # After demon sorts: gas is perfectly sorted → entropy = 0
    H_gas_after_sort = 0.0
    delta_H_gas = H_gas_after_sort - H_gas_initial   # -n bits

    # Demon erases n-bit memory
    E_erasure_total_J = k_B * T * ln2 * K_demon_total
    delta_S_env_bits = K_demon_total   # +n bits to environment

    # Net entropy
    delta_S_gas = delta_H_gas        # -n bits
    delta_S_demon = 0.0              # 0 (erased)
    delta_S_total = delta_S_gas + delta_S_demon + delta_S_env_bits   # = 0

    return {
        "n_particles": n,
        "T_K": T,
        "H_gas_initial_bits": H_gas_initial,
        "K_demon_acquired_bits": K_demon_total,
        "H_gas_after_sort_bits": H_gas_after_sort,
        "delta_H_gas_bits": delta_H_gas,
        "E_landauer_erasure_total_J": E_erasure_total_J,
        "delta_S_env_bits": delta_S_env_bits,
        "delta_S_gas_bits": delta_S_gas,
        "delta_S_total_bits": delta_S_total,
        "second_law_satisfied": delta_S_total >= -1e-12,
    }


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3 — K-CHANGE IS PHYSICAL INTERVENTION (GAP.MD R1)
# ═══════════════════════════════════════════════════════════════════════════════

def causal_intervention_analysis(demon_result: dict) -> dict:
    """
    Map the demon's K-acquisition and erasure onto the four theories of causation
    from gap.md R1, showing interventionism is the best fit.
    """
    K_acquired = demon_result["K_demon_acquired_expected_bits"]
    E_erasure  = demon_result["E_landauer_erasure_J"]
    delta_S_gas = demon_result["delta_S_gas_bits"]
    delta_S_total = demon_result["delta_S_total_bits"]

    return {
        "K_acquired_bits": K_acquired,
        "E_erasure_J": E_erasure,
        "delta_S_gas_bits": delta_S_gas,
        "delta_S_total_bits": delta_S_total,
        "causal_theories": {
            "regularity": {
                "verdict": "incomplete",
                "reason": (
                    "Regularity theory: causation = constant conjunction. "
                    "Sorting always follows measurement — that is a regularity. "
                    "But regularity cannot distinguish a demon that actually sorts "
                    "from a demon that measures and does nothing. The K-acquisition "
                    "step and the sorting step are both regularities yet they differ "
                    "in the entropy change they produce. Regularity cannot capture "
                    "the directionality embedded in K-acquisition → use → erasure."
                ),
            },
            "counterfactual": {
                "verdict": "partially correct",
                "reason": (
                    "Counterfactual theory: C causes E iff, absent C, E would not occur. "
                    "If the demon had not measured (no K acquired), it could not have "
                    "sorted — correct. But counterfactual theory does not explain WHY "
                    "the erasure step is necessary: the counterfactual 'if demon never "
                    "erased, 2nd law violated' is correct but the theory gives no "
                    "mechanism for why the counterfactual world is physically blocked. "
                    "The mechanism is Landauer's principle — a K-information constraint."
                ),
            },
            "interventionist": {
                "verdict": "best fit",
                "reason": (
                    "Interventionist theory (Woodward 2003): C causes E iff an "
                    "intervention on C changes E. The demon intervenes on the gas by "
                    "acquiring K about particle speeds and using that K to change the "
                    "partition position. The intervention IS the K-acquisition event. "
                    "The cost of the intervention (Landauer erasure) is the "
                    "information-theoretic price of causation. This makes interventionism "
                    "quantitative: the strength of the intervention (how much it costs) "
                    "is exactly K_demon × k_B T ln(2). No other causal theory makes "
                    "this quantitative connection."
                ),
                "quantitative_strength_J": E_erasure,
                "quantitative_strength_bits": K_acquired,
            },
            "structural": {
                "verdict": "complementary",
                "reason": (
                    "Structural causal models (Pearl): causation encoded in DAG structure. "
                    "The demon fits naturally: measure → demon-state → sort → erase → "
                    "environment. The DAG captures the flow. But structural models are "
                    "agnostic about what makes an edge in the DAG physical rather than "
                    "a mere labelling. K-information + Landauer gives edges a physical "
                    "weight: each edge that crosses an K-acquisition boundary costs "
                    "k_B T ln(2) per bit. Structural and interventionist are complementary."
                ),
            },
        },
        "conclusion": (
            "The Landauer-Szilard analysis makes interventionism quantitative: "
            f"an intervention acquires {K_acquired:.1f} bit(s) of K-information "
            f"and costs {E_erasure:.4e} J of Landauer erasure. "
            "This is the compression view of causation made thermodynamically concrete: "
            "to change a system's state, you must acquire K about it and then erase "
            "that K — paying the Landauer price. Change without K-acquisition is not "
            "an intervention; it is either unitary (K=0) or random noise."
        ),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def run():
    print("=" * 72)
    print("Zeno & Maxwell — K-information arguments in quantum physics")
    print("=" * 72)
    print()

    # ── SECTION 1: QUANTUM ZENO ───────────────────────────────────────────────

    print("── SECTION 1: Quantum Zeno Effect as K-information argument ──")
    print()
    print("System: qubit precessing under H = ω σ_x / 2, starting in |0⟩.")
    print("Full period T = π/ω (free precession flips qubit to |1⟩ with P=1).")
    print("With N evenly-spaced measurements: P(flip) → 0 as N → ∞ (Zeno effect).")
    print()

    N_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096, 16384, 65536]
    zeno_rows = zeno_analysis(N_values)
    approx_rows = zeno_small_angle_approximation(N_values)

    print(f"{'N':>7}  {'P_step':>10}  {'P_survive':>10}  {'P(|1⟩)final':>13}  "
          f"{'K/step(bits)':>14}  {'K_total(bits)':>14}")
    print("─" * 75)
    for row in zeno_rows:
        K_str = (f"{row['K_per_step_bits']:.8f}" if not math.isinf(row['K_per_step_bits'])
                 else "inf")
        Kt_str = (f"{row['K_total_bits']:.8f}" if not math.isinf(row['K_total_bits'])
                  else "inf")
        print(f"{row['N']:>7}  {row['P_step_1']:>10.6f}  {row['P_survive_0']:>10.6f}  "
              f"{row['P_final_1']:>13.6f}  {K_str:>14}  {Kt_str:>14}")
    print()

    print("Small-angle approximation (valid for large N): K_total ≈ π²/(4N·ln2)")
    print(f"{'N':>7}  {'K_total exact':>16}  {'K_total approx':>16}  {'ratio exact/approx':>20}")
    print("─" * 65)
    for exact, approx in zip(zeno_rows, approx_rows):
        N = exact["N"]
        K_exact = exact["K_total_bits"]
        K_approx = approx["K_total_approx_bits"]
        if not math.isinf(K_exact) and K_approx > 0:
            ratio = K_exact / K_approx
            print(f"{N:>7}  {K_exact:>16.8f}  {K_approx:>16.8f}  {ratio:>20.6f}")
    print()

    print("KEY: As N → ∞:")
    print("  P(|1⟩ at end of T) → 0            (Zeno effect: qubit frozen in |0⟩)")
    print("  K_total → 0 ∝ 1/N                 (K-information accumulation vanishes)")
    print("  K_per_step → 0                    (each outcome is near-certain)")
    print()
    print("Zeno reframed: frequent measurement prevents K-change.")
    print("The qubit is 'frozen' because each measurement is near-certain (K≈0).")
    print("The classical Zeno paradox (motion = impossible) maps to:")
    print("  'Infinite measurement rate → zero K-rate → no state change in K-sense.'")
    print()

    # Landmark values for clarity
    zeno_N1 = zeno_rows[0]   # N=1
    zeno_large = zeno_rows[-1]  # N=65536
    print(f"  N=1 (single mid-period check):  K_total = {zeno_N1['K_total_bits']:.6f} bits, "
          f"P(|1⟩) = {zeno_N1['P_final_1']:.6f}")
    print(f"  N={zeno_large['N']}: K_total = {zeno_large['K_total_bits']:.2e} bits, "
          f"P(|1⟩) = {zeno_large['P_final_1']:.2e}")
    print(f"  Ratio K_total(N=1) / K_total(N={zeno_large['N']}): "
          f"{zeno_N1['K_total_bits'] / zeno_large['K_total_bits']:.2e}")
    print()

    # ── SECTION 2: MAXWELL'S DEMON ────────────────────────────────────────────

    print("── SECTION 2: Maxwell's Demon — K-information accounting ──")
    print()
    print("Toy model: 2 particles, each uniformly fast or slow (1 bit each).")
    print(f"Temperature: T = {T_room} K")
    print()

    demon_2p = maxwell_demon_2particle(T=T_room)

    print("INITIAL STATE:")
    print(f"  Gas entropy:       {demon_2p['H_gas_initial_bits']:.4f} bits  "
          f"(2 particles × 1 bit each)")
    print(f"  Demon memory:      {demon_2p['H_demon_initial_bits']:.4f} bits  (blank register)")
    print()

    print("STEP 1 — Demon measures particle 1 speed:")
    print(f"  K acquired:        {demon_2p['K_demon_acquired_expected_bits']:.4f} bits  "
          f"(-log2(0.5) = 1 bit per outcome)")
    print(f"  Gas entropy after: {demon_2p['H_gas_after_measure_bits']:.4f} bits  "
          f"(particle 1 known, particle 2 still 1 bit)")
    print(f"  ΔH_gas:            {demon_2p['delta_H_gas_from_measurement_bits']:.4f} bits")
    print()

    print("STEP 2 — Demon sorts using its K (opens/closes partition):")
    print(f"  Szilard work extracted: {demon_2p['W_szilard_extracted_J']:.4e} J  "
          f"(= k_B T ln2, isothermal expansion)")
    print(f"  This is: {demon_2p['W_szilard_extracted_bits']:.4f} bit × k_B T ln2")
    print()

    print("STEP 3 — Demon erases 1-bit memory (Landauer):")
    print(f"  Bits erased:       {demon_2p['bits_erased']:.4f} bits")
    print(f"  Erasure cost:      {demon_2p['E_landauer_erasure_J']:.4e} J  (= k_B T ln2)")
    print(f"  ΔS_environment:    +{demon_2p['delta_S_env_from_erasure_bits']:.4f} bits  "
          f"(heat dumped into bath)")
    print()

    print("ENTROPY BALANCE:")
    print(f"  ΔS_gas:            {demon_2p['delta_S_gas_bits']:+.4f} bits")
    print(f"  ΔS_demon:          {demon_2p['delta_S_demon_bits']:+.4f} bits")
    print(f"  ΔS_environment:    {demon_2p['delta_S_env_bits']:+.4f} bits")
    print(f"  ─────────────────────────────────")
    print(f"  ΔS_total:          {demon_2p['delta_S_total_bits']:+.4f} bits  "
          f"{'✓ 2nd law preserved' if demon_2p['second_law_satisfied'] else '✗ VIOLATION'}")
    print()

    print("WORK BALANCE:")
    print(f"  Szilard work out:  {demon_2p['W_szilard_extracted_J']:.4e} J")
    print(f"  Landauer cost in:  {demon_2p['E_landauer_erasure_J']:.4e} J")
    print(f"  Net work output:   {demon_2p['net_work_output_J']:.4e} J  (= 0, no perpetual motion)")
    print()

    print("K-INFORMATION IDENTITIES (exact equality):")
    print(f"  K_acquired == |ΔH_gas|:   "
          f"{demon_2p['K_acquisition_equals_entropy_reduction']}")
    print(f"  K_acquired == bits_erased: "
          f"{demon_2p['K_acquisition_equals_landauer_erasure']}")
    print(f"  bits_erased == ΔS_env:     "
          f"{demon_2p['landauer_erasure_equals_env_entropy_increase']}")
    print()

    print("Generalisation to N particles:")
    N_particle_cases = [2, 4, 8, 16, 32, 64, 128]
    demon_Np_rows = [maxwell_demon_N_particles(n, T=T_room) for n in N_particle_cases]
    print(f"{'N':>6}  {'K_acquired(bits)':>18}  {'ΔH_gas(bits)':>14}  "
          f"{'E_erasure(J)':>14}  {'ΔS_total':>10}")
    print("─" * 70)
    for row in demon_Np_rows:
        print(f"{row['n_particles']:>6}  {row['K_demon_acquired_bits']:>18.4f}  "
              f"{row['delta_H_gas_bits']:>14.4f}  "
              f"{row['E_landauer_erasure_total_J']:>14.4e}  "
              f"{row['delta_S_total_bits']:>10.4f}")
    print()

    # ── SECTION 3: CAUSATION ─────────────────────────────────────────────────

    print("── SECTION 3: K-change as physical intervention (gap.md R1) ──")
    print()
    causal = causal_intervention_analysis(demon_2p)

    for theory, analysis in causal["causal_theories"].items():
        print(f"[{theory.upper()}] verdict: {analysis['verdict']}")
        print(f"  {analysis['reason']}")
        print()

    print("CONCLUSION:")
    print(f"  {causal['conclusion']}")
    print()

    # ── KEY FINDINGS ──────────────────────────────────────────────────────────

    print("=" * 72)
    print("KEY FINDINGS")
    print("=" * 72)
    print()

    zeno_N1_K = zeno_rows[0]["K_total_bits"]
    zeno_N65k = zeno_rows[-1]["K_total_bits"]
    zeno_N65k_P = zeno_rows[-1]["P_final_1"]

    print("F1. ZENO EFFECT = K-RATE SUPPRESSION")
    print(f"   N=1 measurement: K_total = {zeno_N1_K:.4f} bits, P(flip) = "
          f"{zeno_rows[0]['P_final_1']:.4f}")
    print(f"   N={zeno_large['N']}:     K_total = {zeno_N65k:.2e} bits, P(flip) = "
          f"{zeno_N65k_P:.2e}")
    print(f"   Suppression factor: {zeno_N1_K / zeno_N65k:.2e}×")
    print(f"   K_total decays as 1/N — infinite measurement rate drives K-rate to zero.")
    print(f"   Zeno 'freezing' is K-freezing: each outcome is near-certain (K≈0).")
    print(f"   The qubit cannot accumulate K-change under continuous observation.")
    print()

    print("F2. DEMON'S K-ACQUISITION = ENTROPY DECREASE = LANDAUER ERASURE COST")
    print(f"   K acquired by demon:  {demon_2p['K_demon_acquired_expected_bits']:.4f} bits")
    print(f"   Gas entropy decrease: {abs(demon_2p['delta_S_gas_bits']):.4f} bits")
    print(f"   Landauer erasure:     {demon_2p['bits_erased']:.4f} bits  "
          f"({demon_2p['E_landauer_erasure_J']:.4e} J at {T_room} K)")
    print(f"   All three are equal — this is not a coincidence but a logical identity.")
    print(f"   The demon cannot decrease gas entropy by more K than it acquires,")
    print(f"   and it cannot acquire K without later paying Landauer erasure.")
    print()

    print("F3. 2ND LAW FROM K-CONSERVATION")
    print(f"   ΔS_total = ΔS_gas + ΔS_demon + ΔS_env = "
          f"{demon_2p['delta_S_gas_bits']:.1f} + "
          f"{demon_2p['delta_S_demon_bits']:.1f} + "
          f"{demon_2p['delta_S_env_bits']:.1f} = "
          f"{demon_2p['delta_S_total_bits']:.1f} bits")
    print(f"   The 2nd law is preserved EXACTLY, not approximately.")
    print(f"   K-conservation (total bits in closed system ≥ initial) is equivalent")
    print(f"   to the 2nd law at the information-theoretic level.")
    print()

    print("F4. INTERVENTION IS K-ACQUISITION (gap.md R1 — interventionist causation)")
    print(f"   Interventionist theory wins: an intervention on system S IS:")
    print(f"     (a) acquiring K about S's state  [{demon_2p['K_demon_acquired_expected_bits']:.1f} bit]")
    print(f"     (b) using K to modify S          [ΔH_gas = {demon_2p['delta_S_gas_bits']:.1f} bits]")
    print(f"     (c) paying Landauer cost         [{demon_2p['E_landauer_erasure_J']:.4e} J]")
    print(f"   This quantifies the interventionist picture: the 'strength' of an")
    print(f"   intervention is measured in bits of K acquired and joules of Landauer cost.")
    print(f"   Regularity theory cannot capture this; counterfactuals get it partially;")
    print(f"   structural models are complementary but need K-weighting on edges.")
    print()

    print("F5. BOTH EFFECTS ARE K-CHANGE = 0 vs K-CHANGE > 0 BOUNDARY")
    print(f"   Zeno: continuous measurement → K_per_step → 0 → total K → 0.")
    print(f"         System at K=0 boundary: not changing in the K-sense.")
    print(f"   Demon: measurement IS a K>0 event for the demon (K=1 bit).")
    print(f"          Sorting uses K>0 to push gas toward K=0 (sorted = known state).")
    print(f"          Erasure returns demon to K=0 at Landauer cost.")
    print(f"   Both cases confirm: the K=0/K>0 boundary (from quantum_K_change.py)")
    print(f"   is the fundamental dividing line between 'no change' and 'change' in")
    print(f"   the K-information framework.")
    print()

    # ── SAVE DATA ─────────────────────────────────────────────────────────────

    os.makedirs("results", exist_ok=True)

    manifest = {
        "constants": {
            "k_B_J_per_K": k_B,
            "ln2": ln2,
            "T_room_K": T_room,
        },
        "section1_quantum_zeno": {
            "description": (
                "Qubit precessing under H = ω σ_x / 2, full period T = π/ω. "
                "N measurements evenly distributed across T. "
                "Shows K_total → 0 as N → ∞ (Zeno effect kills K-accumulation)."
            ),
            "N_values": N_values,
            "rows": zeno_rows,
            "small_angle_approximation": approx_rows,
            "landmark_N1": {
                "N": zeno_rows[0]["N"],
                "K_total_bits": zeno_rows[0]["K_total_bits"],
                "P_final_1": zeno_rows[0]["P_final_1"],
            },
            "landmark_N_large": {
                "N": zeno_rows[-1]["N"],
                "K_total_bits": zeno_rows[-1]["K_total_bits"],
                "P_final_1": zeno_rows[-1]["P_final_1"],
            },
            "suppression_factor": zeno_rows[0]["K_total_bits"] / zeno_rows[-1]["K_total_bits"],
        },
        "section2_maxwell_demon_2particle": demon_2p,
        "section2_maxwell_demon_N_particle": demon_Np_rows,
        "section3_causation": causal,
    }

    with open("results/zeno_maxwell_data.json", "w") as f:
        json.dump(manifest, f, indent=2)

    print("Data saved → results/zeno_maxwell_data.json")
    print()

    return manifest


if __name__ == "__main__":
    run()
