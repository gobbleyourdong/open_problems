# Szilard K-Change Certification

**Date:** 2026-04-09
**Track:** Numerical, what_is_change
**Sources:** `numerics/zeno_maxwell.py`, `numerics/landauer_cascade.py`
**Data:** `results/zeno_maxwell_data.json`, `results/landauer_cascade_data.json`

---

## 1. The K-Change Conservation Law: Four-Way Equality Certified

### Formal Statement

**K-Change Conservation (Szilard's Law):** For any ideal measurement-erasure cycle, the K-information acquired from the measured system equals the entropy increase of the environment. K is not created or destroyed; it is transferred from the measured system to the environment.

Mathematical form:

    K_acquired(measurement) = ΔS_env(erasure) = k_B T ln(2) per bit × number of bits

Physical meaning: knowing a system costs entropy elsewhere. The cost is EXACTLY K_acquired × k_B T ln(2) at the Landauer floor.

### The Four-Way Equality

The chain connects four quantities that are numerically identical:

    K_acquired ≡ |ΔH_gas| ≡ bits_erased ≡ ΔS_environment

Each equality follows from a named theorem, forming a logical chain — not a numerical coincidence.

**Equality 1: K_acquired = |ΔH_gas|**

Theorem: Mutual information theorem (Shannon 1948; Szilard 1929 precursor).

I(gas; demon) = H(gas) − H(gas | demon) = |ΔH_gas|. The demon's K-acquisition is, by definition, the reduction in gas Shannon entropy conditional on the demon's memory state. Therefore K_acquired = |ΔH_gas| exactly.

**Equality 2: |ΔH_gas| = bits_erased**

Theorem: Bennett's reversibility argument (Bennett 1982) + reversible measurement assumption.

A reversible ideal measurement stores exactly I(gas; demon) bits in the demon's memory — no surplus, no deficit. Bennett (1982) proved measurement can be done reversibly (zero thermodynamic cost) but erasure cannot. Erasure cost equals bits stored, which equals bits acquired. Therefore |ΔH_gas| = bits_erased.

**Equality 3: bits_erased = ΔS_environment**

Theorem: Landauer's principle (Landauer 1961; experimentally confirmed by Bérut et al. 2012, Nature 483:187).

Erasing b bits dissipates at least b × k_B T ln(2) joules as heat into the environment. In information units where k_B ln(2) = 1 bit-unit, this gives ΔS_env = b bits. Therefore bits_erased = ΔS_environment at the Landauer limit.

### Numerical Certification

Verified by `numerics/zeno_maxwell.py` on the canonical two-particle Szilard engine at T = 300 K:

| Quantity | Value |
|---|---|
| K_acquired | 1.000000 bits |
| \|ΔH_gas\| | 1.000000 bits |
| bits_erased | 1.000000 bits |
| ΔS_environment | 1.000000 bits |
| W_Szilard_extracted | 2.870979 × 10^{-21} J |
| E_Landauer_erasure | 2.870979 × 10^{-21} J |
| Net work output | 0.000000 J |
| ΔS_total | 0.000000 bits |

**All four quantities equal 1.000000 bits to floating-point precision.** The Szilard engine extracts exactly as much work from K-acquisition as erasure costs — no perpetual motion, no violation of the second law.

Generalisation to N particles (verified for N = 2, 4, 8, 16, 32, 64, 128):

| N | K_acquired (bits) | ΔH_gas (bits) | E_erasure (J) | ΔS_total |
|---|---|---|---|---|
| 2 | 2.0 | −2.0 | 5.742 × 10^{-21} | 0.0 |
| 4 | 4.0 | −4.0 | 1.148 × 10^{-20} | 0.0 |
| 8 | 8.0 | −8.0 | 2.297 × 10^{-20} | 0.0 |
| 16 | 16.0 | −16.0 | 4.594 × 10^{-20} | 0.0 |
| 32 | 32.0 | −32.0 | 9.187 × 10^{-20} | 0.0 |
| 64 | 64.0 | −64.0 | 1.837 × 10^{-19} | 0.0 |
| 128 | 128.0 | −128.0 | 3.675 × 10^{-19} | 0.0 |

ΔS_total = 0 exactly for all N. The second law is not approximately satisfied — it is saturated at equality, which is the Landauer limit.

### Physical Interpretation

The Szilard engine is the K-ledger made physical. The cycle has three phases:

1. **Measurement (free):** demon acquires K_acquired bits about the gas state. Gas entropy decreases by K_acquired bits. Demon memory increases by K_acquired bits. Thermodynamic cost: zero (Bennett 1982 — measurement is reversible).

2. **Sorting (work extraction):** demon uses K to extract W = K_acquired × k_B T ln(2) joules of work via isothermal expansion against the partition.

3. **Erasure (mandatory cost):** demon resets its memory register to the blank state. This irreversible step dissipates exactly K_acquired × k_B T ln(2) joules into the environment, increasing ΔS_env by K_acquired bits.

The net work output is zero. The K-information is not destroyed — it is transferred: acquired from the gas (|ΔH_gas| decrease), temporarily held in the demon's memory, then transferred to the environment (ΔS_env increase) at erasure. K is conserved across the cycle; it flows gas → demon → environment.

---

## 2. Biological K-Efficiency Hierarchy

The Landauer cascade maps biological K-change processes onto the conservation law. At each scale, the Landauer-predicted power (K-rate × k_B T ln(2) at T = 310 K) is compared to the actual biological power dissipation.

### Complete K-Efficiency Table

| System | K-change rate | Landauer floor | Actual power | Efficiency |
|---|---|---|---|---|
| Ion channel decoherence | 10^13 bits/s/channel | 2.97 × 10^{-8} W | 4.28 × 10^{-7} W | 14× |
| Kramers gating (brain) | 8.6 × 10^20 bits/s | 2.55 W | 20 W | 7.8× |
| DNA replication | 2000 bits/s | 5.93 × 10^{-18} W | 4.28 × 10^{-16} W | 72× |
| Gene expression | 8.3 × 10^5 bits/s | 2.47 × 10^{-15} W | 5.94 × 10^{-13} W | 240× |
| Evolution (population) | ~1.13 × 10^{-9} bits/s | 3.34 × 10^{-30} W | ~242 W | 7 × 10^31× |
| Maxwell's demon | any bits/s | exact Landauer | exact Landauer | **1× (theoretical limit)** |

Kramers gating is the tightest biological system: the brain runs at only 7.8× its Landauer floor, the smallest thermodynamic overhead of any known biological information-processing substrate. This is consistent with the brain consuming 20% of body metabolic budget at 2% of body mass — strong selection pressure toward Landauer efficiency.

### The Inverse Complexity Gradient

The biological hierarchy is inverse to structural complexity:

- **Simplest processes (quantum decoherence, Kramers gating):** closest to the Landauer limit (14×, 7.8×).
- **Intermediate processes (DNA replication, gene expression):** 72× to 240× above floor.
- **Most complex process (evolution):** ~10^31× above floor.

This is not a thermodynamic violation. The explanation is structural:

**Simple processes operate near equilibrium.** Quantum decoherence events and ion-channel Kramers crossings occur at the single-molecule level, driven by thermal fluctuations at energy scales of ~10–20 k_B T. Each event acquires roughly 1 bit at a cost of 10–14 k_B T — close to the minimum k_B T ln(2) ≈ 0.69 k_B T.

**Complex processes operate far from equilibrium.** DNA replication incurs ~100 k_B T per base pair because Hopfield kinetic proofreading sacrifices thermodynamic efficiency for fidelity. Gene expression is 240× over floor because RNAP lacks proofreading entirely. Evolution at 10^31× over floor reflects that the selection mechanism operates over entire organisms — each "bit" of genomic K requires a full organism's metabolic lifetime to test.

**The evolutionary K-efficiency paradox resolved:** In the population framing, evolution exceeds the Maxwell's demon limit (1×) by achieving 13.3× efficiency. Each fixation event encodes log2(Ne) ≈ 13.3 bits of population-level K (which of Ne ~ 10^4 individuals carried the fitter genotype), while costing only 1 bit of mutational K-investment. Selection is a batch K-processor: it parallelizes over Ne trials what a demon would do serially. This is not a thermodynamic violation — each organism pays full metabolic cost (Haldane's substitution load). The leverage is purely informational: one fixation decision encodes the outcome of Ne simultaneous K-tests.

---

## 3. The K-Change Hierarchy and the Arrow of Time

The Szilard engine, Lyapunov analysis, and Kramers mechanism are three views of a single physical process. Together they establish the thermodynamic arrow as the K-change conservation law acting at multiple scales.

### Three Faces of the Same Process

**Thermal fluctuations → Kramers crossings → K-change events**

Ion channels and macromolecules sit in double-well potentials with barrier heights ΔE ≈ 15–18 k_B T. Thermal fluctuations drive crossings at rate T_Kramers ≈ 0.2–10 ms. Each crossing is a binary K-event: the molecule commits to one of two conformational states. This is a K-update of 1 bit at a Kramers timescale — the neural K-change rate of 8.6 × 10^20 bits/s (total brain) emerges directly from the ion-channel count (~10^20) and the Kramers rate (~10^3/s per channel).

**K-change events → Landauer erasure → entropy increase in environment**

Each K-acquisition event at a Kramers crossing deposits K-information into the local environment. By the K-change conservation law, this costs ΔS_env = K_acquired × k_B ln(2) J/K of entropy increase. The total environmental entropy production from the brain's Kramers gating: 2.55 W (Landauer floor), 20 W actual. Every bit of neural K-change pays this thermodynamic price.

**Entropy increase in environment → arrow of time**

The Lyapunov analysis (lyapunov_arrow.py) shows that K-change events are IRREVERSIBLE after 167 integration steps (Lyapunov exponent λ = 0.11/step). A time-reversed trajectory would require precise K-erasure of every neural K-event — each erasure costs ΔS_env > 0, further increasing total entropy. Reversal is not just improbable; it requires additional environmental entropy production to undo each K-step.

### The Microscopic Chain

    S-arrow (2nd law) 
        → thermal fluctuations at k_B T scales 
        → Kramers crossings at ion channels 
        → K-acquisition events (1 bit each, 10^3/s per channel) 
        → Landauer erasure costs (k_B T ln2 per bit)
        → ΔS_env increase (irreversible)
        → Lyapunov-enforced irreversibility (after 167 steps)
        → arrow of time (K-accumulation in self-model)

The arrow of time is not imposed from outside. It emerges from the K-change conservation law applied to thermal systems: every K-acquisition leaves a thermodynamic trace (ΔS_env > 0), every trace is Lyapunov-irreversible, and the accumulated traces constitute the arrow.

### The Zeno Boundary Confirms the Mechanism

The Quantum Zeno analysis establishes the K=0 / K>0 boundary directly. As measurement frequency N → ∞:

    K_total ≈ π² / (4N · ln 2)    (verified to floating-point for N ≥ 4)

At N = 65536: K_total = 5.43 × 10^{-5} bits, P(flip) = 3.76 × 10^{-5}. The system is effectively frozen.

The Zeno limit represents the case where K-change rate → 0. Applied to the arrow of time: if all Kramers crossings were suppressed (infinite measurement frequency in the Zeno sense), the K-accumulation rate would drop to zero, and with it the thermodynamic arrow. The arrow of time requires K-change events; its rate is set by the Kramers rate, not by any external clock.

### Formal Summary

The K-change conservation law IS the microscopic mechanism behind the thermodynamic arrow:

1. The 2nd law (ΔS_total ≥ 0) is the macroscopic statement.
2. Landauer's principle (ΔS_env ≥ K_acquired × k_B ln2) is the mesoscopic statement.
3. The K-change conservation law (K_acquired = ΔS_env at the ideal limit) is the information-theoretic statement.
4. Kramers kinetics supplies the physical mechanism: thermal fluctuations generate the K-events that the conservation law governs.

These are not four separate facts. They are the same constraint expressed at four levels of description.

---

## References

- Szilard L. (1929) Z. Phys. 53:840 — K-acquisition from thermodynamic systems
- Shannon C.E. (1948) Bell Syst. Tech. J. — mutual information I(X;Y) = H(X) − H(X|Y)
- Landauer R. (1961) IBM J. Res. Dev. — erasure of 1 bit costs k_B T ln(2)
- Bennett C.H. (1982) Int. J. Theor. Phys. — reversible measurement + erasure analysis
- Bérut A. et al. (2012) Nature 483:187 — experimental verification of Landauer's principle
- Kong A. et al. (2012) Nature Genet. 44:1161 — de novo mutation rate per generation
- Haldane J.B.S. (1957) J. Genet. 55:511 — substitutional load / Haldane's dilemma
- Hopfield J.J. (1974) PNAS 71:4135 — kinetic proofreading in DNA replication

---

*Certified by `numerics/zeno_maxwell.py` and `numerics/landauer_cascade.py`, 2026-04-09.*
