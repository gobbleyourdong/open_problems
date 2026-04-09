---
source: Lamb vector constraint ξ·(ω×u) = 0 → pressure along ξ is lower-order
type: NEW ANGLE — exact identity constraining ê·H·ê
status: PROMISING — needs quantification
date: 2026-03-26 cycle 29
---

## The Exact Identity

From NS momentum: ∂u/∂t + ω×u = -∇B + νΔu where B = p + |u|²/2.

Project onto ξ = ω/|ω|:

```
ξ·(ω×u) = 0    (exact, everywhere, always)
```

Therefore: **ξ·∇B = -ξ·∂u/∂t + νξ·Δu** (exact).

The Bernoulli gradient in the vorticity direction is determined
ONLY by the time derivative and viscous term — NOT by the Lamb vector.

## Consequence for ê·H·ê

The pressure Hessian ê·H·ê = ê·∇²p·ê = ê·∇²B·ê - ê·∇²(|u|²/2)·ê.

The ê·∇²B·ê term involves the second derivative of B in the ê direction.
From the identity ξ·∇B = lower order: B varies SLOWLY in the ξ direction
(only through time derivative + viscous terms, not through the dominant
Lamb vector).

If B varies slowly in ê direction: ê·∇²B·ê is SMALL.

The remaining ê·∇²(|u|²/2)·ê involves the Hessian of kinetic energy
in the ê direction. At x*: u ⊥ ω (our measurement), so u·ê = 0.
The kinetic energy |u|²/2 has ∂/∂ê(|u|²/2) = u·(∂u/∂ê). This is
NOT zero (u varies in the ê direction even though u⊥ê at x*).

## Quantification

ê·∇B = -ê·∂u/∂t + νê·Δu

|ê·∇B| ≤ |∂u/∂t| + ν|Δu|

From NS: |∂u/∂t| ≤ |ω×u| + |∇B| + ν|Δu| ~ ρ|u| (dominant term).

But we're computing ê·∂u/∂t, not |∂u/∂t|. The ê component of ∂u/∂t
is determined by the ê component of the NS equation:

ê·∂u/∂t = -ê·(ω×u) - ê·∇B + νê·Δu = 0 - ê·∇B + νê·Δu

This is CIRCULAR (ê·∂u/∂t depends on ê·∇B).

The identity ξ·∇B = νξ·Δu - ξ·∂u/∂t can be rewritten as:
ξ·∇B + ξ·∂u/∂t = νξ·Δu

This relates the sum ξ·∇B + ξ·∂u/∂t to viscous terms only.

## The Non-Circular Content

The identity **ξ·(ω×u) = 0** removes the DOMINANT nonlinear term
from the ξ-projected NS equation. What remains:

```
ξ·∇B + ξ·∂u/∂t = νξ·Δu    (viscous only)
```

The LHS involves pressure + time derivative in ξ direction.
The RHS is O(ν) (small for small ν).

For small ν: ξ·∇B ≈ -ξ·∂u/∂t. The pressure gradient in the ξ
direction is approximately the NEGATIVE of the velocity time derivative
in the ξ direction. These are both lower order compared to ρ|u|
(the Lamb vector magnitude).

## Impact on ê·H·ê

If ξ·∇B is small (O(ν)): the Bernoulli function is approximately
constant in the ξ direction. Its Hessian ê·∇²B·ê is bounded by
∇(ξ·∇B) which is O(ν × derivatives of Δu).

This could give: |ê·H·ê| ≤ C(ν) instead of Cρ².

If |ê·H·ê| = O(ν): the strain ODE becomes:
dα/dt ≤ -α² + O(ν) → α ≤ max(√ν, α₀) → BOUNDED!

## Status

VERY PROMISING if the quantification works. The identity ξ·(ω×u)=0
is exact and removes the dominant nonlinear term. But converting
"ξ·∇B is small" to "|ê·H·ê| is small" requires bounding the
second derivative, which involves ∇(viscous terms).

The key question: is ∇(νξ·Δu) bounded by something that doesn't
involve ρ²? If νξ·Δu ~ ν × ρ × (some power of kmax): then
∇(νξ·Δu) ~ ν × ρ × kmax × (...). For fixed N: bounded.

THIS MIGHT CLOSE FOR THE GALERKIN SYSTEM (fixed N)!

83 proof files. New direction: Lamb vector identity constrains ê·H·ê.
