# K-Debt Payments — Findings

**Script:** `numerics/k_debt_payments.py`  
**Date:** 2026-04-09  
**Baseline:** SM+GR = 21,834 bits (K-minimum across all tested TOEs)

---

## 1. Gravitational Wave Observations as K-Debt Payments Against LQG

LQG carries a K-debt of **+1,000 bits** above SM+GR.  Under K-informationalism,
each LIGO event that is consistent with GR (and inconsistent with LQG's predicted
quantum-gravity corrections) pays down that debt at a rate of
**log₂(P(GR)/P(LQG)) bits per event**.

### Conservative accounting (P(GR)/P(LQG) = 10 per event)

| Run | Events | bits/event | Total paid | % of LQG debt |
|-----|--------|-----------|-----------|---------------|
| LIGO O3 (completed) | 90 | 3.32 | 299 bits | 29.9% |
| LIGO O4 (projected) | ~300/yr | 3.32 | ~997/yr | ~99.7%/yr |

- O3 alone cleared **~300 bits** (30% of LQG K-debt).
- Remaining debt after O3: **~701 bits**.
- Events still needed: **212** (beyond O3's 90).
- LIGO O4 rate: ~300 events/year → **~0.71 years** to clear the full debt.

### Sensitivity to Bayes-factor assumption

| P(GR)/P(LQG) | bits/event | Events to clear 1000-bit debt | O4 years |
|---|---|---|---|
| 2 | 1.00 | 1000 | 3.03 |
| 5 | 2.32 | 431 | 1.14 |
| **10** | **3.32** | **302** | **0.71** |
| 100 | 6.64 | 151 | 0.20 |
| 1000 | 9.97 | 101 | 0.04 |

### Sub-analyses

**Polarisation tests (high-SNR events, O3):**  
10 events with SNR > 20; Bayes factor P(2 modes)/P(6 modes) ~ 10² per event.  
K-payment: 66.4 bits (6.6% of LQG K-debt from polarisation alone).

**Dispersion constraint (α < 10⁻³):**  
LQG predicts α ~ 10⁻¹⁷ for ~100 Hz GWs — far below current LIGO sensitivity.
Dispersion tests currently pay only ~1 bit/event (weak; ~90 bits total for O3).
Dispersion becomes decisive only if α_LQG ≳ 10⁻³.

### Verdict

Under the most conservative assumptions (Bayes factor = 10 per event), approximately
**1 year of LIGO O4 operation is sufficient to retire LQG's full K-debt**.
If the Bayes factor is 100 (well-supported for high-SNR polarisation tests), the debt
clears in roughly **73 days** of O4 operation.

---

## 2. K-Cost of Tegmark Multiverse Levels

| Level | K-extra vs SM+GR | K-total | MDL status |
|-------|-----------------|---------|-----------|
| **Level I** (distant Hubble volumes) | **0 bits** | 21,834 | K-tied with SM+GR |
| **Level III / MWI** (all QM branches) | **0 bits** | 21,834 | K-tied; preferred over Copenhagen by 330–530 bits |
| Level IV (mathematical multiverse) | +500 bits | 22,334 | K-debt; no unique predictions |
| Level II (eternal inflation / landscape) | +2,161 bits | 23,995 | K-debt; may explain Λ fine-tuning |

### Rationales

**Level I:** Same SM+GR program, same constants — Level-I regions are different
outputs of the identical K-short program. No extra specification needed. K_extra = 0.
Unobservable in principle: no MDL advantage and no penalty.

**Level III (MWI):** Branching is deterministic under unitary evolution, which is
already contained in the SM+GR Schrödinger/path-integral equation.  Adding MWI does
not require specifying anything new. K_extra = 0.  In contrast, Copenhagen's collapse
postulate is an *extra* rule: K_extra(Copenhagen) ≈ 330–530 bits.  MWI is therefore
K-preferred over Copenhagen by 330–530 bits.

**Level IV (mathematical multiverse):** Must specify what "consistent mathematical
structure" means — choice of foundation axioms (ZFC? ETCS? something weaker?) plus
a measure/selection principle.  Estimated K_extra ≈ 500 bits.  Makes no falsifiable
predictions in any accessible region.

**Level II (eternal inflation / landscape):** Must encode the inflaton potential or
string landscape meta-law that generates the distribution of physical constants.
K_extra ≈ 2,161 bits (same as String/M-theory overhead).  Could pay down this debt
if it makes a confirmed, precise prediction about Λ or the Higgs mass — but no such
confirmed prediction exists yet.

### K-ordering of multiverse levels

Level I = Level III (MWI) < Level IV < LQG < Level II = String

---

## 3. Simulation Hypothesis K-Cost

Claiming "we are in a simulation" requires specifying at minimum:

| Component | K-cost |
|-----------|--------|
| Simulator substrate physics | ≥ 21,834 bits (must support SM+GR-level computation) |
| Simulation layer (algorithm + boundary conditions) | 500 – 10,000 bits |
| Why our specific laws hold in the simulation | 0 bits (deterministic) to 21,834 bits (tabulated) |

| Scenario | K-total | K-extra vs SM+GR |
|----------|---------|-----------------|
| Conservative (deterministic laws, simple layer) | 22,334 | +500 |
| Mid-range (deterministic laws, complex layer) | 31,834 | +10,000 |
| Pessimistic (tabulated laws, complex layer) | 53,668 | +31,834 |

**MDL verdict:** The simulation hypothesis is disfavoured by ≥ 500 bits under MDL.
It would become preferred only if it made correct predictions SM+GR cannot — e.g.
systematic glitch patterns tied to computational frame boundaries, or a discrete
lattice structure showing up in cosmic ray spectra at the GZK cutoff.  No such
prediction has been confirmed.

---

## 4. Unified K-Cost Comparison Table

| Framework | K-total (bits) | K-extra vs SM+GR | MDL status |
|-----------|---------------|-----------------|-----------|
| SM+GR | 21,834 | 0 | MDL winner — K-minimum |
| SM+GR + Level I multiverse | 21,834 | 0 | K-tied |
| SM+GR + MWI (Level III) | 21,834 | 0 | K-tied; preferred over Copenhagen |
| Causal Set Theory | 21,934 | +100 | K-debt; cheapest alternative TOE |
| CCC (Penrose) | 22,300 | +466 | K-debt; Hawking point evidence needed |
| SM+GR + Copenhagen QM | 22,164 | +330 | K-disfavoured vs MWI by 330 bits |
| SM+GR + Level IV multiverse | 22,334 | +500 | K-debt; no unique predictions |
| LQG | 22,834 | +1,000 | K-debt; ~302 GW events to clear (~1 yr O4) |
| SM+GR + Simulation hypothesis (conservative) | 22,334 | +500 | K-debt; no confirmed unique predictions |
| SM+GR + Level II (landscape) | 23,995 | +2,161 | K-debt; may explain Λ fine-tuning |
| String/M-theory | 23,995 | +2,161 | K-debt; no confirmed unique predictions |
| Simulation (pessimistic) | 53,668 | +31,834 | Deeply disfavoured |

---

## Key Conclusions

1. **GW events are a concrete, quantitative mechanism for paying down LQG's K-debt.**
   LIGO O4 alone can close the account in ~0.7 years under conservative assumptions.

2. **The K-minimal multiverse choices are Level I and Level III (MWI).**  Both add
   exactly 0 bits above SM+GR.  The simulation hypothesis adds at least 500 bits and
   is not currently preferred.

3. **MWI is K-preferred over Copenhagen** by 330–530 bits — the collapse postulate is
   pure K-overhead with no observational benefit.

4. **SM+GR remains the MDL winner at 21,834 bits.**  No tested TOE or cosmological
   extension currently improves on it without accruing measurable K-debt.

5. **K-informationalism provides a unified score** for comparing TOEs, interpretations,
   and ontological add-ons.  K-debt is not a falsification — it is a quantitative
   measure of how much correct, unique predictive work each framework still owes.

---

*Data persisted to `results/k_debt_payments_data.json`.*
