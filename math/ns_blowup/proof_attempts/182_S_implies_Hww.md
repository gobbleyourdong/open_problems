---
source: Instance A — The |S| > 0 → H_ωω > 0 lemma
type: PROOF ATTEMPT — the core argument
date: 2026-03-29
---

## The Argument (two cases at the max of |ω|)

At x* where |ω(x*)| = ||ω||∞:

CASE 1: |S(x*)| = 0.
  Then α = ê·S·ê = 0. No stretching. d||ω||∞/dt = 0.
  No blowup danger. QED for this case.

CASE 2: |S(x*)| > 0.
  The flow deviates from solid-body rotation at x*.
  CLAIM: this forces H_ωω(x*) > 0, giving the transport barrier.

## Why |S| > 0 forces H_ωω > 0

Step 1: At the max of |ω|², the source Δp = |ω|²/2 - |S|² has a
critical point (∇Δp involves ∇|ω|² = 0 and ∇|S|²).

Step 2: For a z-INDEPENDENT flow (straight tube): S = 0 at the
center (proven: Lamb-Oseen, file 181). So |S| > 0 requires
z-DEPENDENCE (variation along ω).

Step 3: z-variation in the source Δp creates z-variation in p.
At the MAX of Δp in z: the Poisson equation gives ∂²p/∂z² > 0
(because the peaked source in z creates positive curvature in p
at the peak — verified for cos(z) modulation).

Step 4: H_ωω = ∂²p/∂z² (in the frame where ω || z) > 0.

Step 5: H_ωω > 0 → ratio < 1 → transport barrier → α bounded → BKM.

## The Gap in Step 2

Step 2 claims: |S(x*)| > 0 at a |ω| maximum requires ω-directional
variation. This is true for axisymmetric tubes but needs proof for
general 3D flows.

COUNTEREXAMPLE CHECK: Can we have |S| > 0 at a |ω| max with
z-independent flow?

For z-independent u: A = ∇u has A_iz = A_zi = 0 (no z-derivatives).
Then ω = (∂u_z/∂y - ∂u_y/∂z, ∂u_x/∂z - ∂u_z/∂x, ∂u_y/∂x - ∂u_x/∂y).
With z-independence: ω_x = ∂u_z/∂y, ω_y = -∂u_z/∂x, ω_z = ∂u_y/∂x - ∂u_x/∂y.

At a max of |ω| on a z-independent flow: the max is achieved on
an entire z-line (degenerate). This is fine for T³ (periodic in z).

The strain at the max: S_ij = (∂u_i/∂x_j + ∂u_j/∂x_i)/2.
For z-independent: S_13 = S_23 = 0, S_33 = 0.
The 2D strain S_11, S_12, S_22 can be nonzero.

So: YES, you can have |S| > 0 with z-independent flow. The strain
is in the xy-plane (perpendicular to ω for a z-vortex).

But then: ω is approximately along z (if ω_z >> ω_x, ω_y).
And S is in the xy-plane.
α = ê·S·ê ≈ S_zz = 0.

So α = 0 even with |S| > 0! Because S is perpendicular to ω.

Wait — that's not quite right. α = ê·S·ê where ê = ω̂. If ω has
x and y components too: α includes S_xx c_x + S_yy c_y + ...

For a general z-independent flow: ω can point in any direction.
But the STRAIN S has S_33 = 0 and S_i3 = 0. So:
α = Σ S_ij ê_i ê_j = Σ_{i,j ∈ {1,2}} S_ij ê_i ê_j

This is nonzero if ω has xy-components AND S_12 ≠ 0.

EXAMPLE: ω = (1, 0, 1)/√2, S = [[0, 1, 0], [1, 0, 0], [0, 0, 0]].
Then α = S_11 ê_1² + 2S_12 ê_1 ê_2 + S_22 ê_2² = 0 + 0 + 0 = 0.
Hmm, ê = (1/√2, 0, 1/√2), so α = S_11/2 + 0 + S_33/2 = 0 + 0 = 0.

Actually for this S: α = (1/√2, 0, 1/√2) · [[0,1,0],[1,0,0],[0,0,0]] · (1/√2, 0, 1/√2)
= (1/√2, 0, 1/√2) · (0, 1/√2, 0) = 0.

Another example: ω = (1, 1, 0)/√2, S = [[1, 0, 0], [0, -1, 0], [0, 0, 0]].
α = (1/√2, 1/√2, 0) · [[1,0,0],[0,-1,0],[0,0,0]] · (1/√2, 1/√2, 0)
= (1/√2, 1/√2, 0) · (1/√2, -1/√2, 0) = 1/2 - 1/2 = 0.

Hmm, it seems like for z-independent flows with S_33 = 0:
α = Σ_{i,j∈{1,2}} S_ij ê_i ê_j + S_33 ê_3² = S_2D:ê² + 0.

The 2D strain S_2D is trace-free in 2D: S_11 + S_22 = -S_33 = 0.
So S_2D has eigenvalues ±λ.

α = λ(c₁ - c₂) where c₁, c₂ are the alignment with the 2D eigenvectors.
If ω is along z (c₁ = c₂ = 0): α = 0.
If ω is in the xy-plane (c₃ = 0): α = λ(c₁ - c₂).

For ω in the xy-plane: α can be nonzero. But then ω is perpendicular to z,
and the "z-direction" in the Lamb-Oseen analysis doesn't align with ω.

I think the argument needs refinement. The correct statement is:

At the max of |ω|: either
(a) The source Δp has variation along ω → H_ωω > 0, OR
(b) The source is ω-independent → H_ωω = 0 → ratio = 1 BUT α = 0.

Case (b) might have α ≠ 0 for non-axisymmetric geometries...

Actually, let me just verify numerically: at the max of all our evolved
flows, is it EVER the case that α > 0 AND H_ωω ≤ 0?

From file 174: at the max-|ω| point of the trefoil, H_ωω > 0 at all
measured times. And from the bootstrap (file 175), H_ωω > 0 in the
approaching zone at all times.

The ONLY case where H_ωω = 0 is the straight tube, which has α = 0.

CONJECTURE: α > 0 at the max of |ω| IMPLIES H_ωω > 0 there.

This is what needs proving. And it might follow from:
α > 0 → |S| > 0 with ω-component → source has ω-variation → H_ωω > 0.

## 182. The core lemma: α > 0 at max|ω| → H_ωω > 0.
