#!/usr/bin/env python3
"""
zeno_and_change.py — Zeno's paradox: mathematical resolution and philosophical residue.

Context: PROBLEM.md asks "what is change?" The competing ontologies range from
"change is illusion" (Parmenides) to "change is fundamental" (Heraclitus). Zeno's paradoxes
were meant to show that motion (change) is impossible or incoherent.

The standard mathematical resolution: the infinite sum 1/2 + 1/4 + 1/8 + ... = 1 (Achilles
DOES reach the tortoise). But this doesn't answer the philosophical question: WHAT MAKES the
state at t=1 a continuation of the state at t=0, rather than two separate static facts?

This script:
1. Computes the Zeno series convergence numerically at multiple precisions
2. Computes the minimum change (quantum of action) vs classical continuous motion
3. Demonstrates the K-information framing: change = K-content update between states
4. Shows the "stopped clock" anti-problem: is a stopped system changing?

Usage:
    cd ~/open_problems/physics/what_is_change
    python3 numerics/zeno_and_change.py

Numerical track, what_is_change — 2026-04-09
"""

import math, json, os

hbar = 1.054571817e-34  # J·s
c    = 2.99792458e8     # m/s
eV   = 1.602176634e-19  # J

# ── Zeno's Dichotomy: numerical convergence ───────────────────────────────────

def zeno_partial_sums(n_terms: int) -> list[dict]:
    """
    Compute partial sums S_n = Σ_{k=1}^{n} (1/2)^k.
    Mathematical fact: S_∞ = 1. Numerically: S_n → 1 exponentially fast.
    """
    results = []
    total = 0.0
    for k in range(1, n_terms + 1):
        term = 0.5**k
        total += term
        error = 1.0 - total
        results.append({
            "k": k,
            "term": term,
            "partial_sum": total,
            "error": error,
            "log10_error": math.log10(error) if error > 0 else float("-inf"),
        })
    return results

def achilles_convergence(v_achilles=2.0, v_tortoise=1.0, d_initial=1.0,
                          n_steps=15) -> list[dict]:
    """
    Zeno's race: Achilles (speed v_A) chases tortoise (speed v_T < v_A),
    starting d_initial meters behind.

    Exact solution: they meet at t* = d_initial / (v_A - v_T).

    Zeno's steps: at each step, Achilles reaches where tortoise was.
    Step 0: gap = d_initial
    Step 1: gap = d_initial × (v_T/v_A)
    Step k: gap = d_initial × (v_T/v_A)^k

    Compute the sequence of times to close each sub-gap.
    Show: times form a geometric series summing to t*.
    """
    r = v_tortoise / v_achilles  # 0 < r < 1

    steps = []
    current_time = 0.0
    current_gap = d_initial
    x_achilles = 0.0
    x_tortoise = d_initial

    t_exact = d_initial / (v_achilles - v_tortoise)

    for k in range(n_steps):
        # Time to close current gap
        dt = current_gap / (v_achilles - v_tortoise)
        current_time += dt
        x_achilles = v_achilles * current_time
        x_tortoise = d_initial + v_tortoise * current_time
        current_gap *= r

        steps.append({
            "step": k + 1,
            "time_elapsed": current_time,
            "x_achilles": x_achilles,
            "x_tortoise": x_tortoise,
            "gap": current_gap,
            "time_remaining": t_exact - current_time,
        })

    return steps, t_exact

# ── Quantum of action: minimum change ────────────────────────────────────────

def quantum_action_analysis():
    """
    The minimum quantum of action is ħ. Any physical change involves exchanging
    at least one quantum of action. This is the physical basis for asking:
    can change be truly continuous, or is it discrete at small scales?

    Planck time: t_P = sqrt(ħG/c⁵) — the minimum meaningful time interval
    (below which spacetime structure may be discrete).

    We compare:
    1. Classical continuous motion: position changes by dx at every dt
    2. Quantum discrete transitions: position changes by Δx = ħ/(p × dt) at each step
    3. Planck-scale discreteness: at t_P scale, the notion of 'change' may not apply
    """
    G = 6.674e-11
    t_P = math.sqrt(hbar * G / c**5)
    l_P = math.sqrt(hbar * G / c**3)
    E_P = hbar / t_P

    # Compton wavelength of electron: minimum classical localization scale
    m_e = 9.109e-31  # kg
    lambda_C = hbar / (m_e * c)  # Compton wavelength

    # de Broglie wavelength of a tennis ball (57g, 30 m/s)
    m_ball = 0.057
    v_ball = 30.0
    lambda_dB_ball = hbar / (m_ball * v_ball)

    # de Broglie wavelength of a proton at LHC energy (6.5 TeV)
    E_LHC = 6.5e12 * eV  # J
    p_LHC = E_LHC / c
    lambda_dB_LHC = hbar / p_LHC

    return {
        "Planck_time_s": t_P,
        "Planck_length_m": l_P,
        "Planck_energy_eV": E_P / eV,
        "electron_Compton_wavelength_m": lambda_C,
        "tennis_ball_deBroglie_m": lambda_dB_ball,
        "proton_LHC_deBroglie_m": lambda_dB_LHC,
        "Planck_time_as_fraction_of_s": t_P,
        "discreteness_scale_m": l_P,
    }

# ── K-information framing of change ──────────────────────────────────────────

def k_change_analysis():
    """
    Change as K-information update between states.

    If change is real, then for a system transitioning from state S1 to state S2:
    - K(S1) is the K-complexity of S1
    - K(S2) is the K-complexity of S2
    - K(S2 | S1) is the conditional K-complexity: how much new K-information is needed
      to describe S2 given S1

    For TRIVIAL change (stopped clock between t1 and t2):
      K(S2 | S1) ≈ 0 (they're identical)

    For MAXIMAL change (quantum measurement outcome):
      K(S2 | S1) ≈ K(S2) (S1 gives no compression of S2)

    For SMOOTH change (classical motion):
      K(S(t+dt) | S(t)) ≈ some small value proportional to dt
      The "velocity" in K-space is dK/dt = K(S(t+dt)|S(t)) / dt

    We compute K-change proxies for several state transition types.
    """
    import gzip

    def state_to_bytes(state_desc: str) -> bytes:
        return state_desc.encode("utf-8")

    def k_proxy(data: bytes) -> float:
        return len(gzip.compress(data, compresslevel=9)) / max(len(data), 1)

    def k_conditional_proxy(s1: bytes, s2: bytes) -> float:
        """Proxy for K(S2|S1): compress S2 given S1 as context."""
        joint = s1 + b"|" + s2
        k_joint = len(gzip.compress(joint, compresslevel=9))
        k_s1 = len(gzip.compress(s1, compresslevel=9))
        k_conditional = k_joint - k_s1  # bits for S2 given S1 as prefix
        return max(0, k_conditional) / max(len(s2), 1)

    transitions = []

    # Stopped clock: identical states
    s1 = b"clock position: 12:00:00.000, hands static, no motion" * 20
    s2 = b"clock position: 12:00:00.000, hands static, no motion" * 20
    transitions.append(("stopped_clock", s1, s2))

    # Slow change: position increments by 1 unit
    s1 = ("particle at x=100.000, moving at v=1.0 unit/s" * 20).encode()
    s2 = ("particle at x=100.001, moving at v=1.0 unit/s" * 20).encode()
    transitions.append(("slow_motion_dx=0.001", s1, s2))

    # Fast change: position increments by large amount
    s1 = ("particle at x=000.000, moving at v=100.0 unit/s" * 20).encode()
    s2 = ("particle at x=100.000, moving at v=100.0 unit/s" * 20).encode()
    transitions.append(("fast_motion_dx=100", s1, s2))

    # Phase transition: water to ice (qualitative change)
    s1 = b"state: liquid water, T=273.2K, disordered H2O molecules, flowing" * 20
    s2 = b"state: solid ice,  T=273.0K, ordered crystal lattice, rigid" * 20
    transitions.append(("phase_transition_water_ice", s1, s2))

    # Random state change: no structure
    import os
    s1 = os.urandom(1000)
    s2 = os.urandom(1000)
    transitions.append(("random_states", s1, s2))

    results = []
    for name, state1, state2 in transitions:
        k1 = k_proxy(state1)
        k2 = k_proxy(state2)
        k_cond = k_conditional_proxy(state1, state2)
        results.append({
            "transition": name,
            "K_S1": round(k1, 4),
            "K_S2": round(k2, 4),
            "K_S2_given_S1": round(k_cond, 4),
            "delta_K": round(k2 - k1, 4),
        })
    return results

# ── Anti-problem: the stopped clock ──────────────────────────────────────────

def stopped_clock_analysis():
    """
    PROBLEM.md's Tier 3 question: 'Is a stopped clock in some sense still changing?'

    From different ontological perspectives:
    - Block universe: the stopped clock at t=1 and t=2 are two different slices of the
      4D block. They ARE different entities even if their 3D cross-sections are identical.
      In this sense: yes, the clock 'changes' in the 4D sense even while 'stopped' in 3D.
    - Presentism: if only the present exists, the stopped clock at different moments are
      the same thing (same 3D state). It is NOT changing.
    - Process (Whitehead): change is not about state transitions but about occasions of
      experience. A stopped clock still participates in occasions at each moment, even if
      its macroscopic state is identical.
    - K-information: if K(S(t1) | S(t2)) ≈ 0 for a stopped clock, there is zero K-change.
      Change in the K sense requires K(S(t2) | S(t1)) > 0.

    We compute the information-theoretic answer: what distinguishes t=1 and t=2 for a
    stopped clock, informationally?
    """
    # The only distinguishing feature of the stopped clock at t1 vs t2 is the timestamp.
    # Everything else is identical.
    # K-content of the timestamp: log2(T/t_P) ≈ log2(1/5.4e-44) ≈ 140 bits
    t_P = 5.391e-44  # Planck time
    T_1s = 1.0       # 1 second
    k_timestamp = math.log2(T_1s / t_P)

    return {
        "K_bits_per_timestamp": round(k_timestamp, 2),
        "note": (
            "A stopped clock at t1 and t2 differ ONLY by their timestamps. "
            "The K-content of one second is ~log2(1/t_P) ≈ 140 bits. "
            "So from a K-information perspective, the stopped clock IS 'changing' "
            "by 140 bits/second — but only in its time-coordinate, not in its "
            "physical state. Whether this counts as 'real change' is the philosophical question."
        ),
    }

# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("=" * 65)
    print("Zeno's Paradox and the Nature of Change — Numerical Survey")
    print("=" * 65)

    # Zeno partial sums
    print("\n── Zeno's Dichotomy: convergence of 1/2 + 1/4 + 1/8 + ... ──")
    print(f"{'k':<6} {'term':<16} {'partial sum':<16} {'error':<16} {'log₁₀(error)'}")
    print("─" * 65)
    partial_sums = zeno_partial_sums(20)
    for rec in partial_sums:
        if rec["k"] <= 10 or rec["k"] % 5 == 0:
            print(f"{rec['k']:<6} {rec['term']:<16.2e} {rec['partial_sum']:<16.15f} "
                  f"{rec['error']:<16.2e} {rec['log10_error']:.1f}")
    print(f"  Limit: 1.000000000000000 exactly. Convergence is exponential.")
    print(f"  Mathematical resolution: the sum of infinitely many steps IS finite.")
    print()
    print(f"  PHILOSOPHICAL RESIDUE: calculus shows THAT the steps sum to 1,")
    print(f"  but not HOW Achilles 'passes through' infinitely many positions.")
    print(f"  The question 'what is change?' is upstream of the mathematics.")

    # Achilles race
    print("\n── Achilles and Tortoise (v_A=2, v_T=1, head start=1 unit) ──")
    print(f"{'Step':<6} {'t elapsed':<14} {'x_Achilles':<14} {'x_Tortoise':<14} {'gap':<14} {'t remaining'}")
    print("─" * 75)
    steps, t_exact = achilles_convergence()
    for s in steps[:10]:
        print(f"{s['step']:<6} {s['time_elapsed']:<14.6f} {s['x_achilles']:<14.6f} "
              f"{s['x_tortoise']:<14.6f} {s['gap']:<14.2e} {s['time_remaining']:.2e}")
    print(f"  Exact meeting time: t* = {t_exact:.6f}. Gap → 0 exponentially.")
    print(f"  Achilles meets the tortoise in finite time despite infinite sub-steps.")

    # Quantum action
    print("\n── Quantum of Action: is change truly continuous? ──")
    qa = quantum_action_analysis()
    print(f"  Planck time:          t_P = {qa['Planck_time_s']:.4e} s")
    print(f"  Planck length:        l_P = {qa['Planck_length_m']:.4e} m")
    print(f"  Planck energy:        E_P = {qa['Planck_energy_eV']:.4e} eV")
    print(f"  Electron Compton wavelength: {qa['electron_Compton_wavelength_m']:.4e} m")
    print(f"  Tennis ball de Broglie:      {qa['tennis_ball_deBroglie_m']:.4e} m")
    print(f"  Proton at LHC:               {qa['proton_LHC_deBroglie_m']:.4e} m")
    print()
    print(f"  Below the Planck scale, the standard picture of spacetime breaks down.")
    print(f"  If spacetime is discrete at l_P, then 'continuous change' (Heraclitean)")
    print(f"  is only an approximation. The de Broglie wavelength of a tennis ball")
    print(f"  is {qa['tennis_ball_deBroglie_m']:.2e} m — far below any measurement precision.")
    print(f"  Effectively continuous for macroscopic objects.")

    # K-information change
    print("\n── K-Information Framing: change as K-content update ──")
    print(f"{'Transition':<35} {'K(S1)':<9} {'K(S2)':<9} {'K(S2|S1)':<12} {'ΔK'}")
    print("─" * 75)
    k_results = k_change_analysis()
    for r in k_results:
        print(f"{r['transition']:<35} {r['K_S1']:<9.4f} {r['K_S2']:<9.4f} {r['K_S2_given_S1']:<12.4f} {r['delta_K']:+.4f}")
    print()
    print(f"  Stopped clock: K(S2|S1)≈0 — states are K-identical, zero K-change.")
    print(f"  Slow motion: K(S2|S1)>0 — small position change requires small K-update.")
    print(f"  Phase transition: K(S2|S1)>0 even though K(S2)≈K(S1) — description changes.")
    print(f"  Random states: K(S2|S1)≈K(S2) — S1 gives no compression of S2, maximal change.")

    # Stopped clock
    print("\n── Anti-Problem: the stopped clock ──")
    sc = stopped_clock_analysis()
    print(f"  K-bits per timestamp: {sc['K_bits_per_timestamp']:.1f} bits (log₂(1s/t_Planck))")
    print(f"  {sc['note']}")

    # Summary
    print("\n── SUMMARY ──")
    print("Zeno's mathematical resolution (sum converges) is necessary but not sufficient.")
    print("The philosophical residue:")
    print("  1. Calculus shows the TOTAL distance is finite. It doesn't explain what makes")
    print("     the particle at x=1 'the same object' as the particle at x=0.")
    print("  2. The block universe dissolves the problem: there is no 'movement' in 4D.")
    print("     There are just particle worldlines. 'Change' is a way of talking about")
    print("     the geometry of worldlines, not a feature of reality.")
    print("  3. Under K-information: change = K(S(t+dt)|S(t)) > 0. This is measurable,")
    print("     but it presupposes that states can be compared — which requires time.")
    print("  4. The stopped clock at t1 and t2 differs by 140 bits (the timestamp).")
    print("     Whether that K-difference constitutes 'real change' depends on whether")
    print("     you count time-coordinate as part of the state.")
    print()
    print("The gap: the block universe dissolves Zeno but replaces it with the question")
    print("of what makes a static 4D geometry 'run' for an embedded observer.")
    print("That question connects to what_is_time (the arrow) and what_is_mind")
    print("(the phenomenology of temporal experience).")

    # Save
    os.makedirs("results", exist_ok=True)
    manifest = {
        "zeno_partial_sums": partial_sums[:15],
        "achilles_steps": steps,
        "achilles_meeting_time": t_exact,
        "quantum_action": qa,
        "k_change_analysis": k_results,
        "stopped_clock": sc,
    }
    with open("results/zeno_data.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest → results/zeno_data.json")

if __name__ == "__main__":
    run()
