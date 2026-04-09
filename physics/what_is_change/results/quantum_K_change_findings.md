# quantum_K_change_findings.md

**Script:** `numerics/quantum_K_change.py`
**Data:** `results/quantum_K_change_data.json`
**Date:** 2026-04-09
**Track:** Numerical (Odd instance), what_is_change

---

## Purpose

Demonstrate the quantum-mechanical bifurcation of the S/K framework:

- Unitary evolution (Schrodinger equation): K(state(t+dt) | state(t)) = 0.
- Quantum measurement (collapse): K(outcome | psi) = -log2(P(outcome)) bits.
- Decoherence is the boundary that converts K=0 dynamics into K>0 events.

This directly addresses **gap.md R3**: "physical change vs phenomenal flow."

---

## Section 1: Unitary Evolution — K-change = 0

A 2-qubit system was taken through three unitary gates:
|00> → (H⊗I) → |+>|0> → CNOT → Bell state → (T⊗I) → phase-rotated Bell.

| Step | State | Fidelity with prev. | K-change (bits) |
|------|-------|---------------------|-----------------|
| 0 | \|00> | — | 0 |
| 1 | (H⊗I)\|00> = \|+>\|0> | 0.5000 | 0 |
| 2 | CNOT applied: Bell state | 0.2500 | 0 |
| 3 | (T⊗I) Bell state | 0.8536 | 0 |

**Result:** Fidelities dropped as low as 0.25 (the states genuinely differed), yet K-change was identically 0 at every step. Given the prior state and the known gate U, the new state is computed exactly as `|psi_new> = U|psi_old>`. No new information is created. Entanglement creation is K-zero.

---

## Section 2: Measurement K-Change by Superposition

For |psi> = sqrt(p0)|0> + sqrt(p1)|1>, measured in the computational basis:

| Superposition | P(|0>) | K if |0> (bits) | K if |1> (bits) | H (bits) | Landauer (J) |
|---|---|---|---|---|---|
| maximally mixed | 0.5000 | 1.0000 | 1.0000 | 1.0000 | 2.97e-21 |
| slightly biased | 0.7000 | 0.5146 | 1.7370 | 0.8813 | 2.61e-21 |
| strongly biased | 0.9000 | 0.1520 | 3.3219 | 0.4690 | 1.39e-21 |
| nearly classical | 0.9900 | 0.0145 | 6.6439 | 0.0808 | 2.40e-22 |
| near pure |0> | ~1.0 | ~0 | 33.22 | ~0 | ~0 |
| symmetric 30/70 | 0.3000 | 1.7370 | 0.5146 | 0.8813 | 2.61e-21 |
| symmetric 25/75 | 0.2500 | 2.0000 | 0.4150 | 0.8113 | 2.41e-21 |

**Pattern:** K-change is maximised (1 bit) for the maximally superposed case. As the state approaches a classical eigenstate, the common outcome carries negligible K (it was expected), but the rare outcome carries large K (deep surprise). The expected K-change equals the Shannon entropy H — the average surprisal.

---

## Section 3: The Key Case — Maximally Superposed Qubit

State: |psi> = (|0> + |1>) / sqrt(2), with |alpha|^2 = |beta|^2 = 0.5.

| Quantity | Value |
|---|---|
| Unitary rotation K-change | 0.0 bits (free) |
| Measurement K-change | 1.0 bit |
| Shannon entropy H | 1.0 bit |
| Landauer floor at T=310K | 2.9667e-21 J |
| Landauer floor at T=310K | 1.8517e-02 eV |

This is the **fundamental quantum of K-change**: 1 bit per maximally uncertain measurement, costing a Landauer minimum of 2.97e-21 J at brain temperature.

---

## Section 4: Brain Decoherence K-Change Budget

| Quantity | Value |
|---|---|
| Neurons | 1.00e+11 |
| Firing rate | 100 Hz |
| Decoherence events/second | 1.00e+12 |
| K-bits per event | 1.0 bit |
| Total K-rate | 1.00e+12 bits/s |
| Landauer/event | 2.9667e-21 J |
| Landauer minimum (total) | 2.9667e-09 W = **2.97 nW** |
| Actual brain power | 20.0 W |
| Overhead ratio | **6.74 billion x** |

The brain's actual power is 6.74 billion times above the Landauer floor for its decoherence K-update rate. This is comparable to (but distinct from) the landauer_change.py result for action potentials (~700 million x). The difference: that computation was per firing (1 bit), this one sums over all estimated decoherence events at the functional channel level.

**Comparison across scripts:**

| Script | Process | Slack above Landauer |
|---|---|---|
| landauer_change.py | Neuron firing (1 bit) | ~7.1e+08 x |
| landauer_change.py | DNA mutation (2 bits) | ~36 x |
| quantum_K_change.py | Brain decoherence budget | ~6.7e+09 x |

---

## Section 5: S-Information vs K-Information in Quantum Mechanics

| Property | S-dynamics (Schrodinger) | K-dynamics (measurement) |
|---|---|---|
| Frequency | ~10^14 Hz (molecular/optical) | ~10^3 Hz (neural) |
| Type | Continuous, reversible | Discrete, irreversible |
| K-change | 0 (deterministic) | -log2(P) bits per event |
| Bit rate (2-qubit) | ~5.12e+16 bits/s (precision) | ~10^3 bits/s |
| K/S rate ratio | — | 1.95e-14 (K is negligible fraction of S flow) |

The Schrodinger equation drives enormous S-information dynamics at optical frequencies. K-information updates happen only at decoherence events, at the functional neural timescale — eleven orders of magnitude slower.

---

## Section 6: Bell State Measurement — Entanglement Compresses K-Change

Measuring both qubits of the Bell state (|00> + |11>) / sqrt(2):

| Scenario | K-change (bits) | Landauer (J) |
|---|---|---|
| Measure q0 | 1.0 | 2.97e-21 |
| Measure q1 given q0 | 0.0 | 0 |
| **Bell state total** | **1.0** | **2.97e-21** |
| Two independent qubits | 2.0 | 5.93e-21 |

Entanglement saves exactly 1 bit = I(q0; q1) = 1 bit of mutual information. The Bell state pre-compresses its K-content: once qubit 0 is measured, qubit 1's state is already known. **Entanglement is quantum K-compression** — it pre-distributes correlations so that joint measurement costs less K-update.

---

## Key Findings

**F1. Unitary evolution is K-change-free.**
The Schrodinger equation generates no K-change, regardless of how much the wave function rotates. K(|psi(t+dt)> | |psi(t)>, U) = 0 for any unitary U. Superposition, interference, and entanglement creation are all K-zero.

**F2. Quantum measurement is the fundamental unit of K-change.**
K(outcome | psi) = -log2(P(outcome)) bits. For maximally uncertain qubits: 1 bit per measurement, costing 2.97e-21 J at T=310K (Landauer floor). The rarer the outcome, the larger the K-update.

**F3. Decoherence is the K-zero/K-nonzero boundary.**
Before decoherence: K=0 unitary dynamics. After decoherence: K>0 definite record. Decoherence converts S-information (wave-function rotation) into K-information (irreversible outcome). This is the physical mechanism of K-change at the quantum level.

**F4. The brain's phenomenal flow tracks decoherence, not unitary dynamics.**
Functional decoherence rate: ~10^12 events/s. Unitary S-dynamics: ~10^14 Hz. The conscious timescale (~10^3 Hz, neural) aligns with functional K-updates, not with the Schrodinger rotation rate. This is why quantum superpositions are not experienced: they carry no K-change, so the self-model cannot track them.

**F5. Entanglement is quantum K-compression.**
The Bell state stores 1 bit of mutual information I(q0;q1) = 1 bit. Measuring both qubits costs K = 1 bit total (not 2). Entanglement pre-compresses joint K-update cost by exactly the mutual information. This extends the S/K compression framework to the quantum domain.

**F6. Formal answer to gap.md R3 (physical change vs phenomenal flow).**
- Physical change = K-update event at a decoherence boundary.
- Phenomenal flow = the self-model's sequential record of K-updates.
- The "now" of experience is a decoherence event.
- The "flow" of time is the ordered sequence of K>0 events.
- S-dynamics (unitary rotation) constitutes physical process but NOT K-change and NOT phenomenal event. Only at the decoherence boundary does process become change in the K-sense.

---

## Connection to Previous Results

- **landauer_change.py:** Established thermodynamic floor for K-updates across scales (neuron: 7e+08 x slack; DNA: 36x; photon: 140x; black hole: information frozen at horizon).
- **quantum_K_change.py:** Identifies WHICH quantum events generate K-change (measurement/decoherence only) and shows unitary evolution is K-zero. Brain overhead: 6.7 billion x above Landauer floor for all functional decoherence events.
- **Synthesis:** K-change in the brain is generated exclusively at decoherence events. Unitary quantum dynamics between decoherence events is informationally silent in the K-sense. The ratio between actual brain power and Landauer floor (~10^9 x) represents the cost of the physical mechanism (ion channels, pumps, neurotransmitters) that implements each K-update, not the K-content itself.

---

*Generated by `numerics/quantum_K_change.py`, 2026-04-09.*
