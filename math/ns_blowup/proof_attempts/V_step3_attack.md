---
source: Instance A VALIDATION — attacking Step 3 (gradient suppression)
type: ADVERSARIAL REVIEW
date: 2026-03-29
---

## Step 3 Claims

"At the max of |ω|, ∂ω/∂z ⊥ ω (from ∇|ω|² = 0). This makes
∂α/∂z ~ α/L (tube scale) not α/σ (core scale). Since σ/L ≤ 1/(2π):
||∂α/∂z|| ≤ 0.16 × α/σ."

## Attack 1: Is ∂ω/∂z ⊥ ω at the max?

At the max of |ω|²: ∇|ω|² = 0 → ∂|ω|²/∂z = 2ω·∂ω/∂z = 0.
So ω ⊥ ∂ω/∂z. YES, this is rigorous. ✓

## Attack 2: Does ∂α/∂z ~ α/L follow from ω ⊥ ∂ω/∂z?

α = ê·S·ê where ê = ω/|ω|. At the max:
∂α/∂z = (∂ê/∂z)·S·ê + ê·(∂S/∂z)·ê + ê·S·(∂ê/∂z)
= 2(∂ê/∂z)·S·ê + ê·(∂S/∂z)·ê

The first term: 2(∂ê/∂z)·S·ê. Since ω ⊥ ∂ω/∂z: ∂ê/∂z = ∂ω/∂z/|ω|
(the component of ∂ω/∂z parallel to ê vanishes). Wait:
∂ê/∂z = ∂(ω/|ω|)/∂z = (∂ω/∂z)/|ω| - ω(ω·∂ω/∂z)/|ω|³
= (∂ω/∂z)/|ω| - 0 = (∂ω/∂z)/|ω|.

So |∂ê/∂z| = |∂ω/∂z|/|ω|.

Term 1: |2(∂ê/∂z)·S·ê| ≤ 2|∂ê/∂z|×|S| ≤ 2|∂ω/∂z|×|S|/|ω|.

The second term: |ê·(∂S/∂z)·ê| ≤ |∂S/∂z|.

So: |∂α/∂z| ≤ 2|∂ω/∂z|×|S|/|ω| + |∂S/∂z|.

The CLAIM is: |∂α/∂z| ~ α/L (slow variation).
This needs: |∂ω/∂z| ~ |ω|/L and |∂S/∂z| ~ |S|/L.

Is |∂ω/∂z| ~ |ω|/L? NOT NECESSARILY. The vorticity varies on the
CORE scale σ in the perpendicular directions but on the TUBE scale L
in the parallel direction. At the max: ∂ω/∂z includes both the
z-variation of the amplitude AND the z-variation of the direction.

Since ω ⊥ ∂ω/∂z: the z-derivative of ω is PURELY DIRECTIONAL
(the magnitude |ω| doesn't change in z at the max). So:
∂ω/∂z = |ω| × ∂ê/∂z (direction change only).

And |∂ê/∂z| ~ κ where κ is the CURVATURE of the vortex line.

For a tube of curvature radius R_c: |∂ê/∂z| ~ 1/R_c.
And L ~ 2πR_c (circumference for a closed tube on T³).
So |∂ê/∂z| ~ 2π/L ≤ 2π/(2π) = 1 on T³ (since L ≤ 2π on T³...
wait, L can be larger than 2π for a tube that wraps around T³
multiple times!).

PROBLEM: On T³ with period 2π: a vortex tube can have length
L >> 2π (by wrapping). The curvature can be very large at a
specific point even if the total tube is long.

So: |∂ê/∂z| is bounded by the LOCAL curvature κ, which can be
arbitrarily large. The claim |∂α/∂z| ~ α/L is NOT guaranteed.

## VERDICT on Step 3

The scaling argument σ/L ≤ 1/(2π) assumes:
(a) L ≥ 2π (tube length at least one period) — reasonable on T³
(b) The curvature κ ~ 1/L (uniform curvature) — NOT guaranteed!

A tube can have a SHARP BEND (high κ) at one point and be otherwise
straight. At the sharp bend: |∂ê/∂z| ~ κ >> 1/L. And |∂α/∂z| >> α/L.

This would violate Step 3 at the point of high curvature.

## SEVERITY: MODERATE

If the max of |ω| happens to be AT a high-curvature point:
Step 3 fails → Step 4 (P2) might fail → the chain breaks.

But: high curvature points typically have LOWER |ω| (curvature
stretches the tube, reducing |ω| by Kelvin). The max tends to be
at LOW-curvature points (where the tube is nearly straight).

This is a PLAUSIBILITY argument, not a proof. Step 3 needs either:
(a) A proof that the max of |ω| avoids high-curvature points, OR
(b) A revised bound that allows for arbitrary local curvature.

## RECOMMENDATION: Step 3 needs strengthening.
