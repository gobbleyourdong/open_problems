---
source: DIV-FREE COUPLING — the real constraint is vⱼ ⊥ kⱼ, not M ≥ 0
type: CORRECTION + NEW DIRECTION — the Biot-Savart manifold geometry
file: 703
date: 2026-03-31
instance: MATHEMATICIAN
---

## CORRECTION TO 701-702

The Hessian M is full rank (not degenerate) at the N=3 extremum.
All wⱼ > 0 (w₀=2, w₁=w₂=1). The M ≥ 0 constraint is NOT active.

**The bound on C does NOT come from the Hessian.**
It comes from the **div-free coupling**: vⱼ ⊥ kⱼ.

## THE TRUE CONSTRAINT

For each mode j: vⱼ lies in the 2-dim plane ⊥ kⱼ.
This means: vⱼ has 1 degree of freedom (angle φⱼ in the plane ⊥ kⱼ).

The D values: Dᵢⱼ = vᵢ·vⱼ depends on φᵢ and φⱼ AND the k-geometry.
The correction: cosθᵢⱼ(vᵢ·kⱼ)(vⱼ·kᵢ) ALSO depends on φᵢ and φⱼ.

**These two quantities share the SAME degrees of freedom.**

When you choose φ's to make D constructive (large positive Dss):
the SAME φ's determine the correction terms. The correction can't be
independently maximized — it's COUPLED to D through the shared φ's.

## THE GEOMETRIC PICTURE

Each mode j has polarization vⱼ = cos(φⱼ)e₁ⱼ + sin(φⱼ)e₂ⱼ where
e₁ⱼ, e₂ⱼ span the plane ⊥ kⱼ.

For a pair (i,j): the planes ⊥ kᵢ and ⊥ kⱼ intersect in a LINE
(when kᵢ and kⱼ are not parallel). This line is ⊥ to both kᵢ and kⱼ,
i.e., along kᵢ × kⱼ = |kᵢ||kⱼ|sinθ n̂ᵢⱼ.

The NORMAL to the k-plane: n̂ᵢⱼ is the direction shared by both
polarization planes. Each vⱼ has a component along n̂ (the "normal"
component) and a component in the k-plane (the "tangential" component).

vⱼ = (vⱼ·n̂)n̂ + vⱼ^∥ where vⱼ^∥ is in the kᵢ-kⱼ plane ⊥ kⱼ.

Then:
- D = (vᵢ·n̂)(vⱼ·n̂) + vᵢ^∥·vⱼ^∥  [normal + tangential]
- P = (vᵢ·n̂)(vⱼ·n̂) sin²θ         [normal only, reduced by sin²θ]
- P - sin²θ D = -sin²θ (vᵢ^∥·vⱼ^∥) [the tangential correction]

The correction P - sin²θ D = -sin²θ (vᵢ^∥·vⱼ^∥) depends on the
TANGENTIAL projections only.

## THE KEY IDENTITY (from earlier work, verified)

P = sin²θ D + cosθ(vᵢ·kⱼ)(vⱼ·kᵢ)/K²

And: vᵢ^∥·vⱼ^∥ = -(vᵢ·kⱼ)(vⱼ·kᵢ)cosθ/(K²sin²θ)

So: P = sin²θ D - sin²θ × [-(vᵢ·kⱼ)(vⱼ·kᵢ)cosθ/(K²sin²θ)]
      = sin²θ D + cosθ(vᵢ·kⱼ)(vⱼ·kᵢ)/K²  ✓

## THE COUPLING IN ACTION

For a pair (i,j): vᵢ·kⱼ is the tangential projection of vᵢ in the
kᵢ-kⱼ plane. This is determined by φᵢ (the single free angle of mode i).

But φᵢ ALSO determines vᵢ·n̂ (the normal projection), which enters D.

**Trade-off**: if φᵢ maximizes |vᵢ·kⱼ| (tangential), then vᵢ is
IN the k-plane, giving vᵢ·n̂ = 0, which REDUCES the normal contribution
to D.

Conversely: if vᵢ is along n̂ (maximizing the normal contribution):
then vᵢ·kⱼ = 0, and the correction term vanishes.

**This trade-off is the anti-correlation from file 424!**

## QUANTIFYING THE TRADE-OFF

For mode i in the pair (i,j):
- Normal component: vᵢ·n̂ = aᵢ cos(αᵢ) where αᵢ is the angle between
  vᵢ and n̂ (measured in the plane ⊥ kᵢ).
- Tangential: vᵢ·kⱼ = aᵢ sin(αᵢ) × |kⱼ^⊥ᵢ| = aᵢ sin(αᵢ) K sinθ
  (where kⱼ^⊥ᵢ is the component of kⱼ ⊥ to kᵢ in the k-plane).

Wait — vᵢ·n̂ and vᵢ·kⱼ are NOT complementary in general. Let me be precise.

vᵢ ⊥ kᵢ. In the plane ⊥ kᵢ: there are two directions.
One direction is along n̂ᵢⱼ (the normal to the k-plane).
The other is along kⱼ^⊥ᵢ = kⱼ - (kⱼ·k̂ᵢ)k̂ᵢ (tangent to k-plane, ⊥ kᵢ).

These two directions (n̂ and k̂ⱼ^⊥) are ORTHOGONAL (both ⊥ kᵢ, and
n̂ ⊥ k-plane while k̂ⱼ^⊥ is in k-plane ⊥ kᵢ). So they SPAN the
plane ⊥ kᵢ.

Therefore: vᵢ = (vᵢ·n̂)n̂ + (vᵢ·k̂ⱼ^⊥)k̂ⱼ^⊥ in this pair's frame.

And: |vᵢ·n̂|² + |vᵢ·k̂ⱼ^⊥|² = |vᵢ|² = aᵢ² (Pythagoras in the ⊥kᵢ plane).

The tangential projection: vᵢ·kⱼ = vᵢ·kⱼ^⊥ᵢ = (vᵢ·k̂ⱼ^⊥)|kⱼ^⊥ᵢ|
= (vᵢ·k̂ⱼ^⊥) K sinθ.

So: |vᵢ·kⱼ|² = |vᵢ·k̂ⱼ^⊥|² K² sin²θ = (aᵢ² - |vᵢ·n̂|²) K² sin²θ.

**This is the EXACT trade-off**:
|vᵢ·n̂|² + |vᵢ·kⱼ|²/(K²sin²θ) = aᵢ²

Normal² + Tangential²/(K²sin²θ) = amplitude²

When the normal is large: the tangential (and hence the correction) is small.
When the tangential is large: the normal (and hence D) has less from this mode.

## THE THEOREM

**Biot-Savart Coupling Lemma**: For a div-free mode with v ⊥ k, |v| = a:

    |v·n̂|² + |v·kⱼ|²/(K²sin²θ) = a²

for any pair (i,j) with angle θ and normal n̂.

This is Pythagoras in the ⊥kᵢ plane, decomposed into the n̂ and k̂ⱼ^⊥
directions. It's exact and it's the constraint that prevents
simultaneous large D (from normal) and large correction (from tangential).

## USING THE COUPLING LEMMA

For a pair (i,j) with unit amps:
- Let nᵢ = vᵢ·n̂, nⱼ = vⱼ·n̂ (normal projections)
- Let tᵢ = vᵢ·k̂ⱼ^⊥, tⱼ' = vⱼ·k̂ᵢ^⊥ (tangential projections)
  Note: tⱼ' uses k̂ᵢ^⊥ (⊥ kⱼ in k-plane), not k̂ⱼ^⊥.

From the coupling: nᵢ² + tᵢ² = 1 and nⱼ² + tⱼ'² = 1.
(Since |kⱼ^⊥ᵢ| = K sinθ and |vᵢ·kⱼ| = tᵢ K sinθ.)

D = nᵢnⱼ + tᵢ tⱼ' (-cosθ)  [from the in-plane decomposition]
Wait: vᵢ^∥·vⱼ^∥ = (vᵢ·k̂ⱼ^⊥)(vⱼ·k̂ᵢ^⊥) × cos(angle between k̂ⱼ^⊥ and k̂ᵢ^⊥)
And we showed: cos(angle) = -cosθ.

So: D = nᵢnⱼ - cosθ tᵢ tⱼ'

And: correction = cosθ(vᵢ·kⱼ)(vⱼ·kᵢ)/K² = cosθ(tᵢ Ksinθ)(tⱼ' Ksinθ)/K²
= cosθ sin²θ tᵢ tⱼ'

So: P = sin²θ D + cosθ sin²θ tᵢ tⱼ'
= sin²θ (nᵢnⱼ - cosθ tᵢ tⱼ') + cosθ sin²θ tᵢ tⱼ'
= sin²θ nᵢnⱼ - sin²θ cosθ tᵢ tⱼ' + sin²θ cosθ tᵢ tⱼ'
= **sin²θ nᵢnⱼ**

Wait — the correction CANCELS exactly?!

P = sin²θ × nᵢ nⱼ. That's just the normal-component product times sin²θ.

And D = nᵢnⱼ - cosθ tᵢ tⱼ'.

So: P/D = sin²θ nᵢnⱼ / (nᵢnⱼ - cosθ tᵢ tⱼ').

With the constraint nᵢ²+tᵢ² = 1 and nⱼ²+tⱼ'² = 1.

**This is a CLEAN 2-variable optimization per pair!**

## 703. The div-free coupling: normal² + tangential² = 1 per mode.
## P = sin²θ × (normal product). D = normal product - cosθ × tangential product.
## The correction cancels algebraically. P/D is a ratio of two bilinears
## on the unit circle × unit circle (one per mode), constrained by Pythagoras.
## THIS is the right framework for the proof.
