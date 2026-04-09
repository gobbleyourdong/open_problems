---
source: VALIDATION — Step 5 — checking for circular reasoning
type: ADVERSARIAL CHECK
date: 2026-03-29
---

## Step 5 uses: ||H|| ~ |ω|²/12 (from isotropy)

The correction bound (file 251): |correction|/|main| ≤ 1/(24C).

This uses ||H||_op ≈ |ω|²/12 (the isotropic value).

## IS THIS CIRCULAR?

||H|| = ||H_iso + H_dev|| ≤ H_iso + ||H_dev||.
H_iso = Δp/3 = |ω|²/12 (from the attractor, proven).
||H_dev|| ≤ R × H_iso (from the isotropy bound R < 1).

So: ||H|| ≤ (1+R) × |ω|²/12 ≤ 2 × |ω|²/12 = |ω|²/6.

This gives: |correction|/|main| ≤ (|ω|/2 × |ω|²/6) / (C|ω|³) = 1/(12C).

With C ≥ 0.87: 1/(12 × 0.87) = 1/10.4 ≈ 0.096. Still < 1. ✓

## DOES THIS NEED THE BOOTSTRAP?

The bound ||H_dev|| ≤ R × H_iso uses R < 1.
R < 1 comes from the bootstrap (Q < 0 → H_ωω > Var → R < 1).
But Step 5 is PART of the bootstrap (it's used to prove DH > 0 in Step 9).

IS THIS CIRCULAR? Let me trace the logic:

1. ASSUME Q < 0 (bootstrap hypothesis)
2. → R < 1 (from Q < 0 → H_ωω > Var)
3. → ||H_dev|| ≤ R × H_iso < H_iso = |ω|²/12
4. → ||H|| < 2|ω|²/12 = |ω|²/6
5. → correction in Step 5 ≤ 10% of main
6. → DH > 0 (Step 5)
7. → DQ < 0 (Step 9)
8. → Q < 0 maintained (Step 10)

Steps 1 → ... → 8 form the bootstrap. Q < 0 is both assumed and concluded.
This IS circular, but it's a VALID BOOTSTRAP:

The initialization: Q < 0 at T₀ (from file 245, NOT using the bootstrap).
The continuation: Q < 0 at t → Q < 0 at t + δ (from the chain above).
By induction: Q < 0 for all t > T₀.

THE CIRCULARITY IS IN THE CONTINUATION, NOT THE INITIALIZATION.
This is standard bootstrap technique. ✓

## But: does the initialization use ||H||?

File 245 (initialization): α > 0 → ê-variation → H_ωω > 0 (Fourier lemma).
The Fourier lemma (Step 2) does NOT use ||H|| bounds. It's a direct
computation from the Poisson equation structure. ✓

File 246 (Gap 1): α > 0 → NOT z-independent. Algebraic. No ||H||. ✓

The initialization is INDEPENDENT of the bootstrap. ✓

## VERDICT: No circular reasoning. The bootstrap is properly structured.
## Step 5 uses R < 1 from the bootstrap hypothesis, which is initialized
## independently and maintained self-consistently. Standard technique. ✓
