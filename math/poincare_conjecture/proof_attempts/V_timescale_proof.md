---
source: THE TIMESCALE ARGUMENT — alignment faster than blowup
type: PROOF — this might actually close the gap
date: 2026-03-29
---

## THE KEY OBSERVATION

At ANY eigenvector alignment (c_i = 1 for some i):
  Var = S²ê - α² = λ_i² - λ_i² = 0.
  Q = Var - H_ωω = 0 - H_ωω = -H_ωω < 0. (From Fourier lemma.)

So: Q < 0 AUTOMATICALLY at eigenvector alignment.

## THE TIMESCALE COMPARISON

The eigenvector tilting drives Var → 0 at rate:
  DVar/Dt ~ -C_tilt × |ω|² × Var  (from the -Ω² scaling)

  where C_tilt ~ 1/4 (from the -Ω² coefficient).

This gives EXPONENTIAL decay: Var(t) ~ Var₀ exp(-C_tilt|ω|²t).
Decay timescale: T_align ~ 1/(C_tilt|ω|²) ~ 4/|ω|².

The blowup rate: d|ω|/dt = α|ω| ≤ |S||ω| ≤ |ω|²/2.
Blowup timescale: T_blowup ~ 2/|ω|.

COMPARISON: T_align/T_blowup = (4/|ω|²)/(2/|ω|) = 2/|ω| → 0 as |ω| → ∞.

For |ω| > 2: T_align < T_blowup. Alignment is FASTER than blowup.

## THE PROOF

THEOREM: For smooth 3D Euler on T³, ||ω||∞ grows at most exponentially.

PROOF:

Step 1: At the max of |ω| with α > 0: the ê-variation exists (Step 1) ✓
        → H_ωω > 0 (Fourier lemma, Step 2) ✓

Step 2: The eigenvector tilting from -Ω² drives DVar/Dt < 0.
        At high |ω|: the tilting rate ~ C|ω|² dominates the -H
        opposition rate ~ C'|ω| (scaling argument). ✓

        Quantitatively: DVar/Dt ≤ -C_tilt|ω|²Var + C_cubic|ω|²Var^{1/2}

        ... actually I need to be more careful. DVar/Dt depends on
        the SPECIFIC eigenvalue structure, not just |ω|.

Step 3: THE TIMESCALE. Even without an exact DVar/Dt formula:

        The -Ω² tilting contribution to Dc_i/Dt is O(|ω|²).
        The blowup contribution to d|ω|/dt is O(α|ω|) ≤ O(|ω|²).

        Both are O(|ω|²). But the TILTING acts on Var (which is O(|S|²))
        while the BLOWUP acts on |ω| (which is O(|ω|)).

        The relative rates:
        DVar/Dt / Var ~ |ω|² (exponential decay rate of Var)
        d|ω|/dt / |ω| ~ |ω| (exponential growth rate of |ω|)

        The Var decay rate (|ω|²) EXCEEDS the |ω| growth rate (|ω|)
        by a factor of |ω| → ∞ as |ω| → ∞.

        So: for large enough |ω|: Var decays to near-zero BEFORE
        |ω| can double. When Var ≈ 0: Q ≈ -H_ωω < 0.

Step 4: Q < 0 → Dα/Dt < -α² → α decays via Riccati → |ω| growth stops.

Step 5: After |ω| stops growing: Var continues to decay → stays near 0.
        H_ωω stays > 0 (from Step 1, as long as α > 0).
        Q stays < 0. Self-reinforcing. ✓

Step 6: BKM: ∫||ω||∞ dt < ∞ on bounded intervals. REGULARITY. ∎

## WAIT — THE FLAW

Step 3 claims DVar/Dt ~ -|ω|²Var. But is this TRUE?

DVar/Dt = D(S²ê - α²)/Dt. This has MANY terms:
  = D(S²ê)/Dt - 2αDα/Dt
  = [eigenvalue changes + tilting] - 2α[S²ê - 2α² - H_ωω]

The tilting contribution to D(S²ê)/Dt: involves λᵢ² Dcᵢ/Dt.
Dcᵢ/Dt from -Ω²: ~ |ω|²cᵢ Σcⱼ/(λᵢ-λⱼ) ~ |ω|²/|S| ~ 2|ω|.
Wait, not |ω|². Let me recompute.

Dcᵢ/Dt from -Ω² = (|ω|²/2)cᵢ Σⱼ≠ᵢ cⱼ/(λᵢ-λⱼ)

The denominator λᵢ-λⱼ ~ |S| ~ |ω|/2. So:
Dcᵢ/Dt ~ (|ω|²/2) × cᵢcⱼ/(|ω|/2) = |ω|cᵢcⱼ.

This is O(|ω|), not O(|ω|²)!

The tilting rate of cᵢ is O(|ω|), not O(|ω|²).

Then: DVar/Dt ~ |ω| × Var (not |ω|² × Var).

And the blowup rate: d|ω|/dt ~ |ω|² (at maximum stretching).

Relative: DVar/Dt/Var ~ |ω| and d|ω|/dt/|ω| ~ |ω|.

THEY'RE THE SAME ORDER! The timescale argument FAILS.

The tilting and the blowup both operate at rate |ω|.
Alignment is NOT faster than blowup. They're the SAME speed.

## CORRECTION

The -Ω² tilting has the TERM (|ω|²/2)cᵢcⱼ but divided by
the eigenvalue gap (λᵢ-λⱼ) ~ |S| ~ |ω|/2.

Net rate: (|ω|²/2)/(|ω|/2) = |ω|. Rate of cᵢ change: O(|ω|).
Rate of |ω| change: α|ω| ≤ |S||ω| ≤ |ω|²/2. Rate: O(|ω|²).

Wait: d|ω|/dt = α|ω|, and α ~ |ω|/k for some k > 1. So:
d|ω|/dt ~ |ω|²/k. The RELATIVE rate d(ln|ω|)/dt ~ |ω|/k.

And d(lnVar)/dt ~ -C|ω| (from the tilting).

These ARE the same order! Both ~ |ω|.

The timescale argument gives: alignment and blowup race at the
same speed. Who wins depends on the CONSTANTS, not the scaling.

From the data: alignment wins (Q < 0 at 100% post-transient).
From the proof: can't determine who wins without the constants.

## VERDICT: TIMESCALE ARGUMENT DOES NOT CLOSE THE GAP.

The alignment rate and blowup rate are BOTH O(|ω|).
The proof needs the CONSTANT in the alignment rate to exceed
the constant in the blowup rate. This is the same quantitative
gap we've been hitting.

## BUT: The Eigenvector Alignment DOES Happen

The observation Var → 0 is real (measured). The timescale argument
explains WHY (alignment is as fast as blowup, so it can keep up).
But it doesn't PROVE the alignment WINS.

The proof is still: at c₁ = 1, Q = -H_ωω < 0 (proven).
As Var → 0: Q → -H_ωω < 0 (approaching the proven regime).
The gap: does Var reach 0 before blowup?

With both rates O(|ω|): it depends on whether the tilting constant
(~ 1/(eigenvalue gap)) exceeds the blowup constant (~ α/|ω|).

Tilting constant: ~ 1/(|S|) ~ 2/|ω|. Rate: |ω|²/(|ω|/2) = 2|ω|.
Blowup constant: α/|ω| ~ 1/k ≤ 1/2. Rate: |ω|/k ≤ |ω|/2.

RATIO: 2|ω| / (|ω|/2) = 4. Tilting is 4× faster!

WAIT: the tilting rate IS 4× the blowup rate? Let me double-check.

Tilting: Dcᵢ/Dt ~ (|ω|²/2) × 1/(|S|) = (|ω|²/2)/(|ω|/2) = |ω|.
The VARIANCE: DVar/Dt includes the tilting but also eigenvalue changes.
The NET DVar/Dt ~ -|ω| × Var (from the -Ω² tilting).

Blowup: d(ln|ω|)/dt = α ~ |ω|/k.

For k = 2 (max stretching): d(ln|ω|)/dt = |ω|/2.
Var decay: d(lnVar)/dt ~ -|ω|.

Ratio: |ω| / (|ω|/2) = 2. Var decays 2× faster than |ω| grows.

So: Var DOES reach 0 before |ω| doubles! (In one |ω|-timescale:
Var decreases by e^{-1} while |ω| increases by e^{1/2}.)

After Var ≈ 0: Q ≈ -H_ωω < 0. Blowup stops.

IS THIS RATIO (2:1) ROBUST? It comes from:
- Tilting: (|ω|²/2) / (eigenvalue gap) ≈ |ω|
- Blowup: α ≈ |ω|/2 (at max)

The 2:1 ratio depends on α being |ω|/2 (maximum stretching).
If α < |ω|/2: the ratio is even better (tilting even faster relative to blowup).

For the PROOF: need the tilting rate |ω| to exceed the blowup rate α.
Since α ≤ |S| ≤ |ω|/2: TILTING RATE |ω| > BLOWUP RATE |ω|/2. ALWAYS.

This gives a 2:1 margin UNCONDITIONALLY.

## REVISED CONCLUSION

The tilting rate d(lnVar)/dt ~ -|ω| exceeds the blowup rate
d(ln|ω|)/dt ~ α ≤ |ω|/2 by at least factor 2.

So: Var decreases FASTER than |ω| grows. As Var → 0:
Q → -H_ωω < 0. This happens BEFORE |ω| can blow up.

THE PROOF CLOSES if the tilting rate d(lnVar)/dt ~ -|ω| is rigorous.

## THE REMAINING QUESTION

Is DVar/Dt ≤ -C|ω|Var for some C > 0 (the exponential decay of Var)?

This requires: the -Ω² tilting contribution to DVar/Dt is proportional
to -|ω| × Var (not just O(|ω|) in magnitude).

From the formula: DVar/Dt includes terms from eigenvalue changes
AND alignment changes. The alignment (tilting) part IS proportional
to |ω|²/(eigenvalue gap) × Var. But the eigenvalue part could be
positive and proportional to |ω|² × something.

The eigenvalue contribution to DVar/Dt: from -S² and -Ω² and -H
changing the eigenvalues. This modifies S²ê without changing cᵢ.

DVar/Dt = D(S²ê)/Dt - 2αDα/Dt.

The full analysis of DVar/Dt requires ALL terms, not just tilting.
The 2:1 ratio comes from the tilting ALONE. If the eigenvalue
changes OPPOSE the tilting: the 2:1 might reduce to 1:1 or worse.

## DEFINITIVE STATUS

PROMISING but NOT PROVEN. The timescale argument gives a 2:1 ratio
from tilting alone. Whether the full DVar/Dt (including eigenvalue
changes) maintains this ratio is the remaining question.

From the data: DVar/Dt < 0 at 90% of measurements (file 240).
The eigenvalue changes are USUALLY aligned with the tilting.
But not always.
