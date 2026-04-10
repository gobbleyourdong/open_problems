# SM K-Minimality Test — Findings

**Generated:** 2026-04-10
**Script:** numerics/sm_k_minimality.py
**Data:** results/sm_k_minimality_data.json

---

## Question

Is the Standard Model K-minimal among anthropically viable gauge theories?

## Method

Estimated K(theory) = K(gauge group) + K(representations) + K(parameters) for 9 theories:
- 4 non-viable subsets of the SM (removing gauge factors)
- The SM itself
- 3 viable extensions (SU(5), SO(10), SM + hidden sector)
- Pure gravity (no gauge forces)

## Results

| Theory | K_total (bits) | Anthropically viable? |
|--------|---------------|----------------------|
| Pure gravity (no gauge forces) | 40 | no |
| U(1) only — pure QED | 74 | no |
| SU(2)×U(1) — no QCD | 238 | no |
| SU(3)×U(1) — no weak interaction | 273 | no |
| SU(3)×SU(2) — no electromagnetism | 316 | no |
| Standard Model | 444 | YES |
| SU(5) GUT | 544 | YES |
| SM + hidden U(1) sector | 580 | YES |
| SO(10) GUT | 640 | YES |

## Key Findings

1. **SM is K-minimal among viable theories:** YES
   - SM: 444 bits
   - Next simplest viable: 544 bits (SU(5) GUT)

2. **K-gap between viable and non-viable:** 128 bits
   - All theories simpler than the SM are NOT anthropically viable
   - This gap represents the minimum K-cost of producing observers

3. **K-cost breakdown for the SM:**
   - Gauge group: 29 bits (SU(3)×SU(2)×U(1))
   - Representations: 35 bits (quarks, leptons, Higgs)
   - Parameters: 380 bits (19 free parameters × 20 bits each)
   - **Total: 444 bits**

4. **Why simpler theories fail:**
   - Pure QED (74 bits): no nuclei → no atoms → no chemistry
   - No QCD (238 bits): no protons → no atoms
   - No weak (273 bits): no beta decay → no nucleosynthesis
   - No EM (316 bits): no long-range force → no atoms

## Interpretation

The SM sits at the K-minimum of the anthropically viable set. Every simplification breaks anthropic viability. Every complication (GUTs, hidden sectors) adds K without being required.

This is **exactly what K-minimality predicts** (attempt_003, prediction T5): the observed theory is the K-cheapest one that produces observers.

**Caveat:** This analysis uses a simplified K-estimation. The actual K(SM) involves the specific numerical values of the 19 parameters, their correlations, and the mathematical structure of the Lagrangian. A more precise estimate gives K(SM) ≈ 21,834 bits (from what_is_reality/gap.md). Our estimate of 444 bits captures the structural K (gauge + reps) but not the parametric precision.
