---
source: Lei-Zhang (2025) connection — vorticity direction chaos required for blowup
type: NEW PROOF ROUTE — combine Q < 0 with Lei-Zhang geometric criterion
date: 2026-03-29
file: 212
---

## Lei-Zhang (2025): arXiv:2501.08976

"A geometric characterization of potential Navier-Stokes singularities"

KEY RESULT: Near a potential singularity at (x*, T*):
  The vorticity directions ω/|ω| must COVER EVERY GREAT CIRCLE
  on the unit sphere in the high-|ω| region.

  CONTRAPOSITIVE: If vorticity stays in a DOUBLE CONE (directions
  bounded within a cone of half-angle < π/2) in {|ω| > M}:
  the solution is REGULAR.

## The Connection to Our Work

Our measurements show: at high |ω|, vorticity DOES stay in a cone.
  c₂ ≈ 0.5 (ω near e₂, half-angle ~45° from e₂ axis)
  The alignment is ORGANIZED, not chaotic.

If we can prove ω stays in a cone at high |ω|: Lei-Zhang → regularity.

## The Q < 0 Connection

Q < 0 at the max → α bounded → the vorticity direction ê evolves as
  Dê/Dt = (S-αI)·ê
with |α| bounded. The RATE of direction change is bounded by |S-αI| ≤ 2|S|.

For the direction to cover every great circle: it must rotate through
ALL possible orientations. The rotation rate is bounded by 2|S| ~ |ω|.
In time (T*-t): the direction can rotate by at most ~ |ω|(T*-t) radians.

For blowup (|ω| → ∞, T*-t → 0): the product |ω|(T*-t) ~ 1 (BKM rate).
So the direction can rotate by ~ 1 radian near the blowup.

But Lei-Zhang requires covering EVERY great circle (2π radians of rotation
in every direction). This needs |ω|(T*-t) >> 1 for many independent
directions. With |ω| ~ C/(T*-t): the rotation is ~ C (bounded).

So: the rotation is BOUNDED near blowup → directions stay in a CONE
→ Lei-Zhang → REGULARITY.

## Wait — Is This Already Known?

This argument ALMOST works but has a subtlety: the strain eigenvectors
e_i ALSO rotate (they're not fixed). The cone is relative to e₂, which
moves. The absolute direction of ω is ê rotating in the frame of
rotating eigenvectors.

If the eigenvectors rotate INDEPENDENTLY of ω: the absolute ω direction
could cover the sphere even if relative alignment stays in a cone.

But: the eigenvectors and ω are COUPLED through the strain-rotation
interaction (file 154-155). The eigenvectors track ω (e₃ rotates toward ω,
file 154). So the cone in the eigenvector frame corresponds to a
LIMITED range in the absolute frame.

## The Proof Route

1. PROVE: Q < 0 at the max (or the weaker: α bounded at the max).
2. α bounded → rotation rate of ω bounded → ω directions in a cone.
3. Lei-Zhang (2025): ω in a cone → REGULARITY.

Steps 2-3 are rigorous (step 2 is an ODE estimate, step 3 is Lei-Zhang).
Step 1 is the same gap (Q < 0 or α bounded).

BUT: Step 2 might be WEAKER than needing Q < 0. It only needs α bounded,
not the full Riccati. And α ≤ |S| ≤ C|ω| is always true (trivial bound).

The question for Lei-Zhang: does α ≤ C|ω| (trivial) give enough
to keep ω directions in a cone?

From the Dê/Dt equation: |Dê/Dt| = |(S-αI)·ê| ≤ |S| + |α| ≤ 2|S|.

The angular change of ω in time dt: dθ ≤ 2|S|dt.
Total angular change: Δθ ≤ ∫₀^{T*} 2|S| dt ≤ 2||S||_{L¹_t(L∞)}.

For BKM blowup: ∫||ω||∞ dt → ∞. And ||S||∞ ≤ C||ω||∞.
So ∫||S||∞ dt → ∞ too.

This means: the total angular rotation is INFINITE near blowup.
The ω direction CAN cover the sphere.

So the trivial bound doesn't work. We need α bounded (not just ≤ C|ω|)
to limit the rotation.

## The Refined Connection

If α is BOUNDED (by some constant A, independent of |ω|):
  |Dê/Dt| ≤ |S| + A ≤ C|ω| + A

This doesn't help — |ω| → ∞ still gives infinite rotation.

The rotation is controlled by |S|, not α. And |S| ~ |ω|/2 → ∞.
So the direction ALWAYS has infinite rotation range near blowup.

The Lei-Zhang criterion is about the DISTRIBUTION of ω directions
in SPACE, not time. It says: at a fixed time near T*, the set of
directions {ω(x)/|ω(x)| : |ω(x)| > M} must cover every great circle.

This is a SPATIAL condition, not temporal. The Q < 0 mechanism controls
the TEMPORAL evolution of ω at the max, not the spatial distribution.

For the spatial distribution: if Q < 0 at the max, the max doesn't
blow up. But OTHER points might have different ω directions.

The connection is indirect: Q < 0 at the max prevents the max from
blowing up → ||ω||∞ bounded → the high-|ω| set has bounded measure
→ the ω directions in this set can't cover every great circle
→ Lei-Zhang → regularity.

But this requires ||ω||∞ bounded FIRST (circular).

## BOTTOM LINE

Lei-Zhang (2025) provides a GEOMETRIC regularity criterion that's
complementary to our approach. But connecting Q < 0 to the Lei-Zhang
condition requires the same bound we're trying to prove.

The most promising NEW angle: use Lei-Zhang's TECHNIQUE (control of
local vorticity fluxes, Kelvin-Helmholtz) as a tool for bounding
the pressure Hessian. Their method might provide the CZ-free bound
we need.

## 212. Lei-Zhang (2025) is relevant but doesn't directly close the gap.
## Their TECHNIQUE (vorticity flux control) might be the new tool we need.
