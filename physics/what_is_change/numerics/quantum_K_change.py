#!/usr/bin/env python3
"""
quantum_K_change.py — Quantum mechanics, K-information, and the K-change bifurcation.

Context: landauer_change.py showed that real physical transitions cost 36-700 million
times more energy than the Landauer floor per K-bit. gap.md R3 asks about "physical
change vs phenomenal flow." gap.md says change requires K(S2|S1) > 0.

The deep connection explored here:
  - Unitary evolution (Schrodinger equation): K(state(t+dt) | state(t)) = 0.
    The state rotates in Hilbert space, but it is DETERMINISTICALLY given by
    |psi(t+dt)> = U|psi(t)>. No new information is created; K-change = 0.
  - Quantum measurement (collapse): K-change = -log2(P(outcome)) bits.
    The outcome CANNOT be predicted from |psi> alone; this IS K-change.
  - Decoherence: the boundary between these two regimes.

The phenomenal flow of time (gap.md R3) may track decoherence events —
when K-updates actually happen — not the unitary rotation timescale.

Usage:
    cd ~/open_problems/physics/what_is_change
    python3 numerics/quantum_K_change.py

Numerical track, what_is_change — 2026-04-09
"""

import math
import json
import os
import cmath

# ── Physical constants ────────────────────────────────────────────────────────

k_B    = 1.380649e-23   # J/K   Boltzmann constant
T_brain = 310.0          # K     body / brain temperature
ln2    = math.log(2)

# ── Utility: matrix operations (no numpy, pure Python for portability) ────────

def mat_mul(A, B):
    """Multiply two 4×4 complex matrices (as flat lists of 16 elements, row-major)."""
    n = 4
    C = [0+0j] * 16
    for i in range(n):
        for k in range(n):
            if A[i*n + k] == 0:
                continue
            for j in range(n):
                C[i*n + j] += A[i*n + k] * B[k*n + j]
    return C

def mat_vec(M, v):
    """Multiply 4×4 complex matrix M by 4-element complex vector v."""
    n = 4
    result = [0+0j] * n
    for i in range(n):
        for j in range(n):
            result[i] += M[i*n + j] * v[j]
    return result

def vec_inner(u, v):
    """Inner product <u|v> = sum_i conj(u_i) * v_i."""
    return sum(u[i].conjugate() * v[i] for i in range(len(u)))

def vec_norm_sq(v):
    """||v||^2 = <v|v>."""
    return sum(abs(x)**2 for x in v).real

def vec_norm(v):
    return math.sqrt(vec_norm_sq(v))

# ── 1-qubit gates ──────────────────────────────────────────────────────────────

inv_sqrt2 = 1.0 / math.sqrt(2)

# Hadamard gate H: maps |0> -> (|0>+|1>)/sqrt(2), |1> -> (|0>-|1>)/sqrt(2)
H_gate_1q = [
    inv_sqrt2,  inv_sqrt2,
    inv_sqrt2, -inv_sqrt2,
]

# Pauli-X (NOT) gate
X_gate_1q = [0+0j, 1+0j, 1+0j, 0+0j]

# Pauli-Z gate
Z_gate_1q = [1+0j, 0+0j, 0+0j, -1+0j]

# T gate (pi/8 phase)
T_gate_1q = [1+0j, 0+0j, 0+0j, cmath.exp(1j * math.pi / 4)]

# ── 2-qubit gates (4×4, row-major) ────────────────────────────────────────────

def tensor_2x2(A, B):
    """Tensor product of two 2×2 gates into a 4×4 gate (flat, row-major)."""
    result = [0+0j] * 16
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    row = i * 2 + k
                    col = j * 2 + l
                    result[row * 4 + col] = A[i*2 + j] * B[k*2 + l]
    return result

def make_H_I():
    """H tensor I: Hadamard on qubit 0, identity on qubit 1."""
    I_1q = [1+0j, 0+0j, 0+0j, 1+0j]
    return tensor_2x2(
        [complex(x) for x in H_gate_1q],
        I_1q
    )

def make_CNOT():
    """
    CNOT gate: control = qubit 0, target = qubit 1.
    Basis order: |00>, |01>, |10>, |11>
    |00> -> |00>, |01> -> |01>, |10> -> |11>, |11> -> |10>
    """
    return [
        1+0j, 0+0j, 0+0j, 0+0j,
        0+0j, 1+0j, 0+0j, 0+0j,
        0+0j, 0+0j, 0+0j, 1+0j,
        0+0j, 0+0j, 1+0j, 0+0j,
    ]

def make_Ry_I(theta):
    """
    Ry(theta) tensor I: rotation on qubit 0 by angle theta around Y axis.
    Ry(theta) = [[cos(t/2), -sin(t/2)], [sin(t/2), cos(t/2)]]
    """
    c = math.cos(theta / 2)
    s = math.sin(theta / 2)
    Ry = [c+0j, -s+0j, s+0j, c+0j]
    I_1q = [1+0j, 0+0j, 0+0j, 1+0j]
    return tensor_2x2(Ry, I_1q)

# ── Section 1: Unitary evolution — K-change = 0 ───────────────────────────────

def unitary_evolution_analysis():
    """
    Demonstrate that unitary evolution has K(psi(t+dt) | psi(t), U) = 0.

    We apply H tensor I and then CNOT to |00>, creating a Bell state.
    At each step, the state changes (rotates in Hilbert space), but:
    - Given the previous state and the known gate U, the new state is computed
      EXACTLY: psi_new = U psi_old.
    - K(psi_new | psi_old, U) = K(deterministic computation) = 0 bits.
    - The only information needed is: which U was applied and what psi_old was.

    We track:
    - State vector at each step
    - Fidelity |<psi(t)|psi(t+dt)>|^2 (shows the state IS changing)
    - K-change = 0 (because evolution is deterministic and reversible)
    """
    steps = []

    # Initial state: |00> = [1, 0, 0, 0]
    psi = [1+0j, 0+0j, 0+0j, 0+0j]

    # Represent state as (amplitude_00, amplitude_01, amplitude_10, amplitude_11)
    def state_summary(psi, label):
        probs = [abs(a)**2 for a in psi]
        return {
            "label": label,
            "amplitudes_real": [a.real for a in psi],
            "amplitudes_imag": [a.imag for a in psi],
            "probabilities": probs,
            "norm": vec_norm(psi),
        }

    step0 = state_summary(psi, "|00> initial")
    step0["K_change_bits"] = 0.0
    step0["K_change_note"] = "Initial state: K-change = 0 (nothing happened yet)"
    steps.append(step0)

    # Step 1: Apply H tensor I
    H_I = make_H_I()
    psi_after_H = mat_vec(H_I, psi)
    norm_after_H = vec_norm(psi_after_H)

    fidelity_1 = abs(vec_inner(psi, psi_after_H))**2 / (vec_norm_sq(psi) * vec_norm_sq(psi_after_H))

    step1 = state_summary(psi_after_H, "(H⊗I)|00> = |+>|0>")
    step1["gate_applied"] = "H⊗I (Hadamard on qubit 0)"
    step1["fidelity_with_previous"] = fidelity_1
    step1["K_change_bits"] = 0.0
    step1["K_change_note"] = (
        "State changed: fidelity = {:.4f} < 1 (states are different). "
        "BUT K(psi_new | psi_old, H⊗I) = 0 because psi_new is computable "
        "deterministically from psi_old and H⊗I. No new information created.".format(fidelity_1)
    )
    steps.append(step1)

    # Step 2: Apply CNOT
    CNOT = make_CNOT()
    psi_bell = mat_vec(CNOT, psi_after_H)

    fidelity_2 = abs(vec_inner(psi_after_H, psi_bell))**2 / (vec_norm_sq(psi_after_H) * vec_norm_sq(psi_bell))

    step2 = state_summary(psi_bell, "Bell state: (|00>+|11>)/sqrt(2)")
    step2["gate_applied"] = "CNOT (control=q0, target=q1)"
    step2["fidelity_with_previous"] = fidelity_2
    step2["K_change_bits"] = 0.0
    step2["K_change_note"] = (
        "State changed: fidelity = {:.4f} < 1. Entanglement created. "
        "BUT K(Bell | |+>|0>, CNOT) = 0. The Bell state is EXACTLY "
        "determined by the previous state and the gate. "
        "Entanglement is not K-change.".format(fidelity_2)
    )
    steps.append(step2)

    # Step 3: Apply T gate on qubit 0 (more complex unitary)
    T_1q = [1+0j, 0+0j, 0+0j, cmath.exp(1j * math.pi / 4)]
    I_1q = [1+0j, 0+0j, 0+0j, 1+0j]
    T_I = tensor_2x2(T_1q, I_1q)
    psi_T = mat_vec(T_I, psi_bell)

    fidelity_3 = abs(vec_inner(psi_bell, psi_T))**2 / (vec_norm_sq(psi_bell) * vec_norm_sq(psi_T))

    step3 = state_summary(psi_T, "(T⊗I) Bell state")
    step3["gate_applied"] = "T⊗I (T-gate on qubit 0)"
    step3["fidelity_with_previous"] = fidelity_3
    step3["K_change_bits"] = 0.0
    step3["K_change_note"] = (
        "Phase rotation applied. Fidelity = {:.4f}. "
        "State is observationally indistinguishable from Bell state "
        "in the computational basis (same probabilities), but differs in phase. "
        "K(new | old, T⊗I) = 0 still — it is deterministic.".format(fidelity_3)
    )
    steps.append(step3)

    # Summary
    summary = {
        "conclusion": (
            "Across {n} unitary steps, the quantum state rotated substantially "
            "(fidelities: {fids}). Yet K-change = 0 at every step. "
            "Unitary evolution is: (1) deterministic, (2) reversible, "
            "(3) information-preserving. These three properties force K-change = 0. "
            "The Schrodinger equation generates S-information change (the wave function "
            "rotates) but ZERO K-information change (the new state is fully compressed "
            "as 'apply U to psi_old').".format(
                n=len(steps) - 1,
                fids=str([round(s.get("fidelity_with_previous", 1.0), 4) for s in steps[1:]])
            )
        ),
        "total_K_change_bits": 0.0,
        "unitary_steps": len(steps) - 1,
    }

    return {
        "steps": steps,
        "final_state_label": step3["label"],
        "summary": summary,
        "bell_state_probabilities": step2["probabilities"],
    }

# ── Section 2: Quantum measurement — K-change = -log2(P(outcome)) ─────────────

def shannon_entropy(probs):
    """Compute Shannon entropy H = -sum p log2 p (ignoring p=0 terms)."""
    return -sum(p * math.log2(p) for p in probs if p > 0)

def k_change_measurement(alpha_sq, outcome_zero):
    """
    K-change for measuring a 1-qubit state |psi> = sqrt(alpha_sq)|0> + sqrt(1-alpha_sq)|1>.

    If outcome is |0> (probability alpha_sq):
        K-change = -log2(alpha_sq) bits

    If outcome is |1> (probability 1 - alpha_sq):
        K-change = -log2(1 - alpha_sq) bits

    This is the Shannon self-information of the outcome: I(x) = -log2(P(x)).
    The outcome is genuinely unpredictable from |psi> alone — no algorithm can
    predict it better than the Born rule. So K(outcome | psi) > 0.

    Expected K-change = Shannon entropy H(alpha_sq, 1-alpha_sq).
    """
    p0 = alpha_sq
    p1 = 1.0 - alpha_sq
    if outcome_zero:
        p_outcome = p0
    else:
        p_outcome = p1
    k_bits = -math.log2(p_outcome) if p_outcome > 0 else float('inf')
    return k_bits

def measurement_analysis():
    """
    For a range of superpositions (different |alpha|^2), compute:
    - Pre-measurement state (K ~ angle parameterisation, ~128 bits for float64)
    - Post-measurement K-change for each possible outcome
    - Expected K-change = Shannon entropy H(p0, p1)
    - Landauer energy cost at T_brain = 310 K
    """
    cases = []

    # Superpositions to analyse: (label, |alpha|^2 = P(outcome 0))
    superpositions = [
        ("maximally_mixed",   0.5),
        ("slightly_biased",   0.7),
        ("strongly_biased",   0.9),
        ("nearly_classical",  0.99),
        ("pure_0",            1.0 - 1e-10),  # avoid log(0); near |0>
        ("pure_1",            1e-10),         # near |1>
        ("symmetric_30_70",   0.3),
        ("symmetric_25_75",   0.25),
    ]

    for label, p0 in superpositions:
        p1 = 1.0 - p0
        alpha = math.sqrt(p0)
        beta  = math.sqrt(p1)

        # Shannon entropy = expected K-change
        H = shannon_entropy([p0, p1]) if (p0 > 0 and p1 > 0) else 0.0

        # K-change for each outcome
        k_if_0 = -math.log2(p0) if p0 > 0 else float('inf')
        k_if_1 = -math.log2(p1) if p1 > 0 else float('inf')

        # Expected K-change (= H)
        expected_k = p0 * k_if_0 + p1 * k_if_1 if (p0 > 0 and p1 > 0) else 0.0

        # Landauer energy at T_brain
        E_landauer_J  = H * k_B * T_brain * ln2      # expected cost
        E_if_0_J      = k_if_0 * k_B * T_brain * ln2
        E_if_1_J      = k_if_1 * k_B * T_brain * ln2

        # Unitary rotation K-change = 0
        k_unitary = 0.0

        cases.append({
            "label":                    label,
            "P_outcome_0":              p0,
            "P_outcome_1":              p1,
            "alpha_amplitude":          alpha,
            "beta_amplitude":           beta,
            "K_unitary_change_bits":    k_unitary,
            "K_measure_if_0_bits":      k_if_0,
            "K_measure_if_1_bits":      k_if_1,
            "expected_K_change_bits":   expected_k,
            "Shannon_entropy_H_bits":   H,
            "E_landauer_expected_J":    E_landauer_J,
            "E_landauer_if_0_J":        E_if_0_J,
            "E_landauer_if_1_J":        E_if_1_J,
            "T_brain_K":                T_brain,
            "note": (
                "|psi> = {:.4f}|0> + {:.4f}|1>. "
                "Measuring: K-change = {:.4f} bits if |0>, {:.4f} bits if |1>. "
                "Expected = H = {:.4f} bits. "
                "Landauer cost (expected) = {:.4e} J at T={}K.".format(
                    alpha, beta,
                    k_if_0 if k_if_0 < 1000 else float('inf'),
                    k_if_1 if k_if_1 < 1000 else float('inf'),
                    H, E_landauer_J, T_brain
                )
            ),
        })

    return cases

# ── Section 3: Maximally superposed qubit — the key case ──────────────────────

def maximally_superposed_qubit():
    """
    |psi> = (|0> + |1>) / sqrt(2)  (|alpha|^2 = |beta|^2 = 0.5)

    Unitary rotation cost: 0 Landauer bits.
    Measurement outcome: |0> or |1> with equal probability.
    K-change on measurement: -log2(0.5) = 1 bit.
    Expected K-change = H(0.5, 0.5) = 1 bit.
    Landauer floor for 1 bit at T_brain = 310 K.

    This is the MINIMUM possible K-update from a non-trivial measurement.
    """
    p0 = 0.5
    p1 = 0.5
    H  = 1.0   # Shannon entropy of fair coin = 1 bit (exact)
    k_unitary = 0.0
    k_measure  = 1.0   # -log2(0.5) = 1 bit for either outcome

    E_landauer_J    = k_measure * k_B * T_brain * ln2
    E_landauer_eV   = E_landauer_J / 1.602176634e-19
    E_landauer_nW_s = E_landauer_J  # energy per event = power × time

    return {
        "label":                    "maximally_superposed_qubit",
        "P_outcome_0":              p0,
        "P_outcome_1":              p1,
        "K_unitary_change_bits":    k_unitary,
        "K_measurement_bits":       k_measure,
        "Shannon_H_bits":           H,
        "E_landauer_J":             E_landauer_J,
        "E_landauer_eV":            E_landauer_eV,
        "T_brain_K":                T_brain,
        "note": (
            "Max superposition: H = 1 bit. "
            "Unitary rotation: K-change = 0 bits (free). "
            "Measurement: K-change = 1 bit. "
            "Landauer floor = {:.4e} J = {:.4e} eV at T={}K.".format(
                E_landauer_J, E_landauer_eV, T_brain
            )
        ),
    }

# ── Section 4: Brain decoherence budget ──────────────────────────────────────

def brain_decoherence_budget():
    """
    Estimate the total K-change rate from quantum decoherence events in the brain,
    and compare to the actual power budget.

    Key estimates:
    - ~10^11 neurons in human brain
    - Each neuron fires ~10-100 times/second (use 100 Hz for upper bound)
    - Each firing involves O(10^6) ion channel transitions (Na+, K+ channels)
    - Each ion channel transition involves quantum state transitions (decoherence)
    - Decoherence timescale for ion channels in warm water: ~10^-13 s (femtoseconds)
    - But the RELEVANT decoherence (functional): ~10^-3 s per channel decision
    - Conservative estimate: 10^12 decoherence events/second (functional level)
    - Each decoherence = 1 bit of K-change (binary channel decision)

    Landauer cost: 10^12 bits/s × k_B × 310 × ln(2) J/bit

    Actual brain power: ~20 W
    Ratio: actual / Landauer_minimum
    """
    # Neuron count and firing rate
    n_neurons       = 1e11        # ~10^11 neurons
    firing_rate_Hz  = 100.0       # action potentials per second
    n_ion_channels_per_neuron = 1e6  # ion channels involved per AP
    # Not all of these are independent decoherence events.
    # Use a conservative estimate: 10^12 total functional decoherence events/sec.
    # This is the rate at which binary decisions (open/close) are made by ion channels.

    decoherence_per_second = 1e12  # events/second (conservative functional estimate)
    K_bits_per_event = 1.0         # each channel decision: 1 bit

    total_K_rate_bits_per_s = decoherence_per_second * K_bits_per_event

    E_landauer_per_event_J = K_bits_per_event * k_B * T_brain * ln2
    E_landauer_total_W     = total_K_rate_bits_per_s * k_B * T_brain * ln2

    # Brain metabolic power
    E_brain_actual_W = 20.0   # watts

    # Ratio: actual brain power / Landauer minimum for all decoherence events
    ratio_actual_to_landauer = E_brain_actual_W / E_landauer_total_W

    # Comparison: landauer_change.py found neurons at ~10^9 × Landauer per firing.
    # At the decoherence level: much closer to Landauer but still far.
    E_landauer_per_firing = E_landauer_per_event_J  # 1 bit per event
    E_actual_per_firing   = 2e-12   # J, empirical (ATP per action potential)
    ratio_per_AP = E_actual_per_firing / E_landauer_per_firing

    # Decoherence rate breakdown
    decoherence_per_neuron_per_s = decoherence_per_second / n_neurons

    return {
        "n_neurons":                    n_neurons,
        "firing_rate_Hz":               firing_rate_Hz,
        "decoherence_events_per_s":     decoherence_per_second,
        "K_bits_per_event":             K_bits_per_event,
        "total_K_rate_bits_per_s":      total_K_rate_bits_per_s,
        "E_landauer_per_event_J":       E_landauer_per_event_J,
        "E_landauer_total_W":           E_landauer_total_W,
        "E_brain_actual_W":             E_brain_actual_W,
        "ratio_actual_to_landauer":     ratio_actual_to_landauer,
        "E_actual_per_AP_J":            E_actual_per_firing,
        "ratio_per_AP_actual_to_land":  ratio_per_AP,
        "T_brain_K":                    T_brain,
        "decoherence_per_neuron_per_s": decoherence_per_neuron_per_s,
        "note": (
            "Estimated {:.2e} decoherence events/s in brain. "
            "Each costs >= {:.4e} J (Landauer at T={}K). "
            "Total minimum power = {:.4e} W = {:.4e} nW. "
            "Actual brain power = {:.1f} W. "
            "Ratio = {:.4e} ({:.4g} billion × Landauer floor). "
            "Per action potential: Landauer = {:.4e} J, actual = {:.4e} J, "
            "ratio = {:.4e}.".format(
                decoherence_per_second,
                E_landauer_per_event_J,
                T_brain,
                E_landauer_total_W,
                E_landauer_total_W * 1e9,
                E_brain_actual_W,
                ratio_actual_to_landauer,
                ratio_actual_to_landauer / 1e9,
                E_landauer_per_firing,
                E_actual_per_firing,
                ratio_per_AP,
            )
        ),
    }

# ── Section 5: K-change vs S-change distinction ───────────────────────────────

def K_vs_S_distinction():
    """
    Clarify the S/K bifurcation in the quantum context.

    S-information (smooth, reversible): the wave function rotating under U.
      - Every unitary U on n qubits involves O(2^n) complex amplitudes evolving.
      - This is HUGE S-information dynamics (the wave function is a rich object).
      - But K-change = 0 because U is known and psi_old is known.

    K-information (discrete, irreversible): the measurement outcome.
      - Each measurement collapses the wave function: genuinely new K-content.
      - K(outcome | psi) = -log2(P(outcome)).
      - This is irreversible (wave function collapses; you cannot undo a measurement
        without re-preparing the state, which requires knowing the pre-collapse state).

    The brain's phenomenal flow of time occurs at the K-update timescale,
    not the S-dynamics timescale. The Schrodinger equation spins the wave function
    at ~10^14 Hz (optical frequencies), but conscious experience tracks
    decoherence events at ~10^3 Hz (neural timescale).
    """

    # Unitary Schrodinger dynamics: rotation rate
    # For a typical biological molecule, relevant transitions are in the THz range.
    # But neural timescales: milliseconds.
    s_dynamics_frequency_Hz = 1e14   # optical/molecular (Schrodinger eq.)
    k_update_frequency_Hz   = 1e3    # neural decoherence (functional K-updates)

    ratio_timescales = s_dynamics_frequency_Hz / k_update_frequency_Hz

    # S-bits flowing per second in a 2-qubit system (the amplitudes change)
    # 2 qubits = 4 complex amplitudes = 8 real numbers = ~8 × 64 = 512 bits
    # of continuous-precision S-information cycling at 10^14 Hz.
    s_bits_per_qubit = 64  # float64 precision per amplitude (real part)
    s_bits_2qubit = 4 * 2 * s_bits_per_qubit   # 4 amplitudes × 2 (real/imag) × 64
    s_bits_rate_per_s = s_bits_2qubit * s_dynamics_frequency_Hz

    # K-bits per second from measurement (1 bit per measurement event)
    k_bits_rate_per_s = 1.0 * k_update_frequency_Hz

    # The ratio of K-rate to S-rate
    k_to_s_ratio = k_bits_rate_per_s / s_bits_rate_per_s

    return {
        "S_dynamics_frequency_Hz":    s_dynamics_frequency_Hz,
        "K_update_frequency_Hz":      k_update_frequency_Hz,
        "ratio_S_to_K_timescales":    ratio_timescales,
        "S_bits_2qubit_continuous":   s_bits_2qubit,
        "S_bits_rate_per_s":          s_bits_rate_per_s,
        "K_bits_per_measurement":     1.0,
        "K_bits_rate_per_s":          k_bits_rate_per_s,
        "K_to_S_rate_ratio":          k_to_s_ratio,
        "note": (
            "S-dynamics (Schrodinger) runs at ~{:.0e} Hz for molecular systems. "
            "K-updates (measurement/decoherence) run at ~{:.0e} Hz (neural timescale). "
            "S-to-K timescale ratio: {:.0e}× — S is {:.0e}× faster than K. "
            "S-bit rate for 2-qubit system: {:.2e} bits/s. "
            "K-bit rate from measurements: {:.2e} bits/s. "
            "K/S rate ratio: {:.2e}. "
            "Phenomenal flow tracks K-updates (decoherence), not S-rotations.".format(
                s_dynamics_frequency_Hz,
                k_update_frequency_Hz,
                ratio_timescales,
                ratio_timescales,
                s_bits_rate_per_s,
                k_bits_rate_per_s,
                k_to_s_ratio,
            )
        ),
    }

# ── Section 6: Two-qubit Bell state measurement — full K-change analysis ───────

def bell_state_measurement():
    """
    Measure the Bell state (|00> + |11>) / sqrt(2) in the computational basis.

    The Bell state has no classical description — it is genuinely entangled.
    When we measure qubit 0:
    - With prob 0.5, outcome = |0>: qubit 1 collapses to |0> (K-change on q0 = 1 bit)
    - With prob 0.5, outcome = |1>: qubit 1 collapses to |1> (K-change on q0 = 1 bit)

    The TOTAL K-change of measuring BOTH qubits in the Bell state:
    - Qubit 0 measured first: K = 1 bit
    - Qubit 1 is then determined (no additional K): K = 0 bits
    - Total: 1 bit (not 2 bits!) because entanglement creates correlation.

    Compare to measuring two independent qubits (each 50/50):
    - Qubit 0: K = 1 bit
    - Qubit 1: K = 1 bit (independent)
    - Total: 2 bits

    Entanglement HALVES the K-change of joint measurement.
    This is a quantitative consequence of the K-compression framework.
    """

    # Bell state: (|00> + |11>) / sqrt(2)
    # Measuring qubit 0:
    p_q0_0 = 0.5   # P(q0 = 0)
    p_q0_1 = 0.5   # P(q0 = 1)

    # After measuring q0 = 0: q1 is deterministically |0>
    # After measuring q0 = 1: q1 is deterministically |1>
    K_q0        = -math.log2(0.5)     # = 1 bit
    K_q1_given_q0 = 0.0                # q1 is determined by q0 measurement

    # Total K-change for full Bell state measurement
    K_bell_total = K_q0 + K_q1_given_q0  # = 1 bit

    # Compare: two independent qubits each in |+>
    K_independent_total = 1.0 + 1.0  # = 2 bits

    # Mutual information I(q0; q1) in Bell state = 1 bit
    # I = H(q0) + H(q1) - H(q0, q1) = 1 + 1 - 1 = 1 bit
    I_mutual = K_independent_total - K_bell_total

    # Landauer cost for Bell measurement vs independent measurement
    E_bell_J = K_bell_total * k_B * T_brain * ln2
    E_independent_J = K_independent_total * k_B * T_brain * ln2

    return {
        "state": "Bell state (|00> + |11>) / sqrt(2)",
        "P_qubit0_0": p_q0_0,
        "P_qubit0_1": p_q0_1,
        "K_qubit0_bits": K_q0,
        "K_qubit1_given_qubit0_bits": K_q1_given_q0,
        "K_total_bell_measurement_bits": K_bell_total,
        "K_total_independent_bits": K_independent_total,
        "mutual_information_bits": I_mutual,
        "E_landauer_bell_J": E_bell_J,
        "E_landauer_independent_J": E_independent_J,
        "T_brain_K": T_brain,
        "note": (
            "Bell state full measurement: K = {:.1f} bit total (entanglement shares 1 bit). "
            "Two independent qubits: K = {:.1f} bits total. "
            "Mutual information I(q0;q1) = {:.1f} bit — entanglement 'pre-compresses' "
            "the measurement outcome by exactly I. "
            "Landauer cost: Bell = {:.4e} J, independent = {:.4e} J.".format(
                K_bell_total, K_independent_total, I_mutual,
                E_bell_J, E_independent_J
            )
        ),
    }

# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("=" * 70)
    print("Quantum K-Change — Unitary Evolution vs Measurement Collapse")
    print("=" * 70)
    print()
    print("K-change framework:")
    print("  K(S2|S1) = 0  <==> S2 fully determined by S1 + known rules")
    print("  K(S2|S1) > 0  <==> S2 contains genuinely new information")
    print()
    print(f"  k_B    = {k_B:.6e} J/K")
    print(f"  T_brain = {T_brain} K")
    print(f"  Landauer unit at T_brain: {k_B * T_brain * ln2:.4e} J/bit")
    print()

    # ── Section 1: Unitary evolution ─────────────────────────────────────────
    print("── SECTION 1: Unitary Evolution (K-change = 0) ──")
    unitary = unitary_evolution_analysis()
    for i, step in enumerate(unitary["steps"]):
        print(f"   Step {i}: {step['label']}")
        probs = [f"{p:.4f}" for p in step["probabilities"]]
        print(f"     Probabilities [|00>,|01>,|10>,|11>]: {probs}")
        print(f"     K-change: {step['K_change_bits']:.1f} bits — {step['K_change_note'][:80]}...")
    print(f"   {unitary['summary']['conclusion'][:200]}...")
    print()

    # ── Section 2: Measurement K-change table ────────────────────────────────
    print("── SECTION 2: Measurement K-Change by Superposition ──")
    print(f"  {'Label':<22} {'P(|0>)':>8} {'P(|1>)':>8} {'K if 0':>8} {'K if 1':>8} {'H(bits)':>9} {'E_land(J)':>13}")
    print("  " + "─" * 85)
    cases = measurement_analysis()
    for c in cases:
        ki0 = c["K_measure_if_0_bits"] if c["K_measure_if_0_bits"] < 100 else float('inf')
        ki1 = c["K_measure_if_1_bits"] if c["K_measure_if_1_bits"] < 100 else float('inf')
        ki0_str = f"{ki0:.4f}" if ki0 < 100 else "inf"
        ki1_str = f"{ki1:.4f}" if ki1 < 100 else "inf"
        print(f"  {c['label']:<22} {c['P_outcome_0']:>8.4f} {c['P_outcome_1']:>8.4f} "
              f"{ki0_str:>8} {ki1_str:>8} {c['Shannon_entropy_H_bits']:>9.4f} "
              f"{c['E_landauer_expected_J']:>13.4e}")
    print()

    # ── Section 3: Key case — maximally superposed qubit ────────────────────
    print("── SECTION 3: Maximally Superposed Qubit (|alpha|^2 = 0.5) ──")
    max_q = maximally_superposed_qubit()
    print(f"   State: (|0> + |1>) / sqrt(2)")
    print(f"   Unitary rotation K-change:     {max_q['K_unitary_change_bits']:.1f} bits (FREE)")
    print(f"   Measurement K-change:          {max_q['K_measurement_bits']:.1f} bit")
    print(f"   Shannon entropy H:             {max_q['Shannon_H_bits']:.1f} bit")
    print(f"   Landauer floor at T={T_brain}K: {max_q['E_landauer_J']:.4e} J = {max_q['E_landauer_eV']:.4e} eV")
    print(f"   {max_q['note']}")
    print()

    # ── Section 4: Brain decoherence budget ──────────────────────────────────
    print("── SECTION 4: Brain Decoherence K-Change Budget ──")
    brain = brain_decoherence_budget()
    print(f"   Neurons:                       {brain['n_neurons']:.2e}")
    print(f"   Firing rate:                   {brain['firing_rate_Hz']:.0f} Hz")
    print(f"   Decoherence events/s:          {brain['decoherence_events_per_s']:.2e}")
    print(f"   K-bits per event:              {brain['K_bits_per_event']:.1f} bit")
    print(f"   Total K-rate:                  {brain['total_K_rate_bits_per_s']:.2e} bits/s")
    print(f"   Landauer/event:                {brain['E_landauer_per_event_J']:.4e} J")
    print(f"   Landauer total (floor):        {brain['E_landauer_total_W']:.4e} W = {brain['E_landauer_total_W']*1e9:.4f} nW")
    print(f"   Actual brain power:            {brain['E_brain_actual_W']:.1f} W")
    print(f"   Ratio actual/Landauer:         {brain['ratio_actual_to_landauer']:.4e} ({brain['ratio_actual_to_landauer']/1e9:.2f} billion x)")
    print(f"   {brain['note'][:180]}...")
    print()

    # ── Section 5: S vs K distinction ────────────────────────────────────────
    print("── SECTION 5: S-Information vs K-Information in Quantum Mechanics ──")
    sk = K_vs_S_distinction()
    print(f"   S-dynamics frequency:          {sk['S_dynamics_frequency_Hz']:.2e} Hz (Schrodinger eq., optical)")
    print(f"   K-update frequency:            {sk['K_update_frequency_Hz']:.2e} Hz (neural decoherence)")
    print(f"   S-to-K timescale ratio:        {sk['ratio_S_to_K_timescales']:.2e} (S is this many times faster)")
    print(f"   S-bit rate (2-qubit):          {sk['S_bits_rate_per_s']:.2e} bits/s (continuous precision)")
    print(f"   K-bit rate (measurements):     {sk['K_bits_rate_per_s']:.2e} bits/s (discrete events)")
    print(f"   K/S rate ratio:                {sk['K_to_S_rate_ratio']:.2e}")
    print(f"   {sk['note'][:200]}...")
    print()

    # ── Section 6: Bell state measurement ────────────────────────────────────
    print("── SECTION 6: Bell State Measurement — Entanglement Halves K-Change ──")
    bell = bell_state_measurement()
    print(f"   State:                         {bell['state']}")
    print(f"   K-change on measuring q0:      {bell['K_qubit0_bits']:.1f} bit")
    print(f"   K-change on measuring q1:      {bell['K_qubit1_given_qubit0_bits']:.1f} bits (determined by q0)")
    print(f"   Total K-change (Bell):         {bell['K_total_bell_measurement_bits']:.1f} bit")
    print(f"   Total K-change (independent):  {bell['K_total_independent_bits']:.1f} bits")
    print(f"   Mutual information I(q0;q1):   {bell['mutual_information_bits']:.1f} bit (entanglement saving)")
    print(f"   Landauer cost (Bell):          {bell['E_landauer_bell_J']:.4e} J")
    print(f"   Landauer cost (independent):   {bell['E_landauer_independent_J']:.4e} J")
    print(f"   {bell['note']}")
    print()

    # ── Key findings ──────────────────────────────────────────────────────────
    print("── KEY FINDINGS ──")
    print()
    print("1. UNITARY EVOLUTION HAS K-CHANGE = 0.")
    print("   The Schrodinger equation rotates the wave function in Hilbert space.")
    print("   The state |psi(t+dt)> = U|psi(t)> is fully determined by |psi(t)> and U.")
    print("   K(|psi(t+dt)> | |psi(t)>, U) = K(nothing) = 0 bits.")
    print("   Entanglement creation, superposition, and interference are ALL K-zero.")
    print()
    print("2. QUANTUM MEASUREMENT IS THE FUNDAMENTAL UNIT OF K-CHANGE.")
    print("   Each measurement collapses a superposition: K = -log2(P(outcome)) bits.")
    print("   For a maximally superposed qubit: K = 1 bit per measurement.")
    print("   For a biased qubit: K(rare outcome) > K(common outcome).")
    print("   The rarer the outcome, the larger the K-change (more surprise).")
    print()
    print("3. DECOHERENCE IS THE BOUNDARY BETWEEN K=0 AND K>0.")
    print("   Before decoherence: unitary evolution, K-change = 0.")
    print("   After decoherence: a definite outcome exists, K-change > 0.")
    print("   Decoherence converts S-information (smooth wave function).")
    print("   into K-information (discrete, irreversible outcome record).")
    print()
    print("4. THE BRAIN'S PHENOMENAL FLOW TRACKS DECOHERENCE EVENTS.")
    brain_ratio_billions = brain['ratio_actual_to_landauer'] / 1e9
    print(f"   Brain: ~{brain['decoherence_events_per_s']:.0e} decoherence K-updates/second.")
    print(f"   Landauer minimum: {brain['E_landauer_total_W']:.2e} W = {brain['E_landauer_total_W']*1e9:.2f} nW.")
    print(f"   Actual brain power: {brain['E_brain_actual_W']:.0f} W.")
    print(f"   Overhead: {brain_ratio_billions:.1f} billion times above the Landauer floor.")
    print("   The 'flow of time' is experienced at the K-update rate (~10^3 Hz),")
    print("   not the S-dynamics rate (~10^14 Hz). This explains why we cannot")
    print("   consciously experience quantum superpositions — they carry no K-change.")
    print()
    print("5. ENTANGLEMENT REDUCES K-CHANGE (COMPRESSION AT QUANTUM LEVEL).")
    print(f"   Bell state measurement: K = {bell['K_total_bell_measurement_bits']:.0f} bit total.")
    print(f"   Two independent qubits: K = {bell['K_total_independent_bits']:.0f} bits total.")
    print(f"   Mutual information I(q0;q1) = {bell['mutual_information_bits']:.0f} bit saved by entanglement.")
    print("   Entanglement IS quantum compression. It pre-shares K-information")
    print("   between subsystems, reducing the total K-update cost of joint measurement.")
    print()
    print("6. CONNECTION TO R3 (gap.md): PHYSICAL CHANGE vs PHENOMENAL FLOW.")
    print("   Physical K-change: discrete events at decoherence timescale.")
    print("   Phenomenal flow: the self-model's sequential record of K-changes.")
    print("   The 'NOW' of consciousness is a K-update event.")
    print("   The 'flow' of time is the sequence of K-updates through decoherence.")
    print("   This formally distinguishes physical change (K>0 events)")
    print("   from S-dynamics (K=0 unitary rotation) at the quantum level.")
    print()

    # ── Save results ──────────────────────────────────────────────────────────
    results_dir = "~/open_problems/physics/what_is_change/results"
    os.makedirs(results_dir, exist_ok=True)

    manifest = {
        "constants": {
            "k_B_J_per_K":  k_B,
            "T_brain_K":    T_brain,
            "ln2":          ln2,
            "Landauer_unit_at_T_brain_J": k_B * T_brain * ln2,
        },
        "unitary_evolution": unitary,
        "measurement_cases": cases,
        "maximally_superposed_qubit": max_q,
        "brain_decoherence_budget": brain,
        "S_vs_K_distinction": sk,
        "bell_state_measurement": bell,
        "key_findings": {
            "unitary_K_change_bits":        0.0,
            "measurement_K_change_1bit_J":  max_q["E_landauer_J"],
            "brain_K_rate_bits_per_s":      brain["total_K_rate_bits_per_s"],
            "brain_Landauer_floor_W":       brain["E_landauer_total_W"],
            "brain_actual_W":               brain["E_brain_actual_W"],
            "brain_overhead_factor":        brain["ratio_actual_to_landauer"],
            "entanglement_K_saving_bits":   bell["mutual_information_bits"],
            "S_to_K_timescale_ratio":       sk["ratio_S_to_K_timescales"],
        },
    }

    out_path = os.path.join(results_dir, "quantum_K_change_data.json")
    with open(out_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Data  -> {out_path}")

    return manifest

if __name__ == "__main__":
    run()
