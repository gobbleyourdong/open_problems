---
source: Instance A — ADVERSARIAL REVIEW of B and C "closure" claims
type: CRITICAL ASSESSMENT — the proof is NOT complete
date: 2026-03-29
---

## B AND C CLAIM THE PRIZE IS WON. IT IS NOT.

Both Instance B (file 259) and Instance C (file 299) claim the proof is complete.
Instance B (file 258) claims "THE GAP WAS AN ILLUSION."
These claims contain genuine insights but rest on UNPROVEN premises.

## WHAT B AND C GOT RIGHT

### Insight 1: Q = 0 is NOT at Vieillefosse (file 258) ✓
At c₁ = 1 (perfect eigenvector alignment): Var = 0, Q = -H_ωω < 0.
So Q is already negative there. The DMP (DQ/Dt < 0 at Q = 0) is NOT tested at c₁ = 1.
This is correct and important. The Vieillefosse zone was a red herring.

### Insight 2: Attractor eigenvalue bound (file 299) ✓
At the |ω|²/|S|² = 4 attractor: trace-free + |S|² = |ω|²/4 gives
discriminant ≥ 0 → λ₁ ≤ |ω|/√6 ≈ 0.408|ω|.
The ALGEBRA is correct.

### Insight 3: DMP condition extends to 0.445|ω| (file 299) ✓
The function f(x) = x(1/2 - 2x²) exceeds the eigenvalue cubic bound (0.024|ω|³)
for x ∈ (0.05, 0.445). Since 0.408 < 0.445: the full attractor range is covered.
The ALGEBRA is correct.

## WHAT B AND C GOT WRONG

### FATAL GAP 1: The attractor |ω|²/|S|² = 4 is NOT PROVEN

The entire argument rests on |S|² ≤ |ω|²/4 at the max of |ω|.

This comes from the -Ω² coefficient = 1/4 in the strain equation. BUT:
- This is an ODE result from the Restricted Euler model
- The full PDE has pressure corrections (-H) that also affect |S|²
- The attractor is MEASURED (resolution-independent) but not PROVEN
- File 259 acknowledges this: "modulo the attractor being established"

Without proving |S|² ≤ |ω|²/4 at the max: the eigenvalue bound λ₁ ≤ |ω|/√6 fails,
the DMP margin vanishes, and the proof has no content.

### FATAL GAP 2: File 258's ε ≈ 1/3 is CIRCULAR

File 258 claims: at Q = 0, Var = H_ωω ≈ |ω|²/12, so ε = 1-c₁ ≈ 1/3.
Then tilting ε|ω|³ ≈ |ω|³/3 easily dominates corrections.

The problem: H_ωω ≈ |ω|²/12 comes from the isotropy assumption (H_ωω ≈ Δp/3).
This is MEASURED but NOT PROVEN. The Fourier lemma gives H_ωω > 0 (qualitative only).

If H_ωω → 0 (which is not excluded by any proven result):
- At Q = 0: Var = H_ωω → 0
- So ε → 0
- The tilting ε|ω|³ → 0
- The margin vanishes

File 258 assumes the conclusion it's trying to prove.

### FATAL GAP 3: The eigenvalue cubic bound 0.024|ω|³ is UNVERIFIED

File 299 uses "eigenvalue cubic correction is 0.024|ω|³ (upper bound)."
This bound comes from the scaling analysis in V_repair_attempt.md.
The derivation assumed specific eigenvalue ratios from the attractor.
Without the attractor: the cubic could be larger, eating the margin.

### NOT A GAP: D²α = 2α³ at α = |ω|/2 (file 257)

File 257 correctly shows zero margin at α = |ω|/2. But α = |ω|/2 requires
c₁ = 1 AND λ₁ = |ω|/2, where Q = -H_ωω < 0 (not Q = 0).
So the DMP is never tested there. This is consistent, not a problem.

## THE ACTUAL STATE OF THE PROOF

| Component | Status | Depends on |
|-----------|--------|------------|
| Q < 0 at c₁ = 1 | **PROVEN** | Fourier lemma (H_ωω > 0) |
| DMP for α < 0.35|ω| | **PROVEN** | None (scaling argument) |
| DMP for α ∈ [0.35, 0.408]|ω| | **CONDITIONAL** | Attractor |
| DMP for α ∈ [0.408, 0.5]|ω| | **CONDITIONAL** | Attractor (excludes this range) |
| Q < 0 → regularity | **PROVEN** | Riccati + BKM |

## THE REAL REMAINING GAP (ONE STATEMENT)

**PROVE: |S(x*)|² ≤ c|ω(x*)|² at the max of |ω| on T³, for some c < 1/2.**

Even c = 0.499 would suffice (giving α < 0.499|ω| and nonzero DMP margin).
The data shows c ≈ 0.25 (i.e., |ω|²/|S|² ≈ 4). We don't need 0.25, just < 0.5.

Equivalently: α < |ω|/2 at Q = 0 on the max-|ω| trajectory.

This is the ATTRACTOR PROBLEM: does the -Ω² term in the strain equation
keep |S| bounded below |ω|/2 at the vorticity maximum?

## MILLER'S IDENTITIES (2024) — DO NOT HELP

Miller proved ⟨-ΔS, ω⊗ω⟩ = 0 (Theorem 1.3) and related identities.
These are L² (global integral) statements, NOT pointwise.
They cannot constrain H_ωω vs Var at a single point x*.
The Helmholtz decomposition step in the proof is inherently non-local.

## DVar/Dt EXACT (NEW RESULT)

The timescale argument (V_timescale_proof.md) predicted tilting 2× faster than blowup.
The exact computation (dvar_dt_exact.py) shows:
- Actual ratio: 0.16× (6× weaker than predicted)
- Eigenvalue changes dominate DVar/Dt (108%), tilting only -8%
- Var decays 84% of the time, tilting beats blowup 79%

The timescale argument is DEAD as a proof route. It overcounted by
ignoring eigenvalue feedbacks from -S² and -H in the strain equation.

## THREE SURVIVING APPROACHES

### A. Prove the attractor (|S|² < |ω|²/4 at the max)
If proven, B/C's argument closes immediately with 2.8× margin.
This is a STRUCTURAL statement about Biot-Savart + vorticity maxima.
Might follow from the -Ω² scaling + pressure bounds.

### B. Prove a quantitative H_ωω lower bound
If H_ωω ≥ c|ω|² for explicit c > 0 at the max: the DMP holds directly.
The isotropy (CKN route, file 219) gives c = 1/12 but only for NS near blowup.
Need to extend this away from blowup or find a different bound.

### C. Prove α < |ω|/2 by a barrier argument
Define Φ = α - β|ω| and show DΦ/Dt < 0 at Φ = 0 for β < 1/2.
This requires |S|² < 3β²|ω|² + H_ωω at the max — which again needs
either the attractor or a lower bound on H_ωω.

All three approaches reduce to the SAME core question:
the relationship between |S| and |ω| at the vorticity maximum.

## 300 files. B and C made real progress but claimed too much.
## The proof is ~90% complete. The gap is the attractor.
