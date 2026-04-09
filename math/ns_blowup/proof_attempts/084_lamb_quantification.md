---
source: Quantification of Lamb vector constraint
type: SCALING CHECK — does νξ·Δu give subcritical forcing?
status: Gives γ=15/8 from Kolmogorov scaling (worse than 7/5), hits derivative loss
date: 2026-03-26 cycle 29 continued
---

## The Chain

1. ξ·(ω×u) = 0 (exact) → ξ·∇B = νξ·Δu - ξ·∂u/∂t
2. ê·H·ê involves ∂/∂ê(ξ·∇B) → bounded by ∇(νξ·Δu)
3. |∇(νΔu)| ≤ ν||∇Δu||_∞ ≤ ν × C × ||Δω||_p (Sobolev + CZ)
4. ||Δω|| involves higher derivatives → derivative loss → same wall

## Kolmogorov Scaling (heuristic)

|νΔu| ~ ν × k_d² × |û| ~ ν × (ρ/ν)^{3/2} × |u| ~ ρ^{3/2}/ν^{1/2}

Then: |ê·H·ê| ~ ∂/∂x(νΔu) ~ ν × k_d × |Δu| ~ ρ^{7/4}/ν^{1/4}

dα/dt ≤ -α² + Cρ^{7/4}/ν^{1/4} → α ~ ρ^{7/8}/ν^{1/8}
dρ/dt ≤ ρ^{15/8}/ν^{1/8}

γ = 15/8 = 1.875. WORSE than our γ=7/5=1.4 from the near/far splitting.

## Why the Lamb Vector Doesn't Help

The identity removes ω×u from the ξ-projected equation. But what
remains (νΔu) involves the LAPLACIAN of velocity, which has a
HIGHER derivative than the strain (one more derivative).

The extra derivative costs one power of k ~ ρ^{1/4} (Kolmogorov),
which MORE THAN OFFSETS the gain from removing the Lamb vector.

Net effect: the Lamb vector identity replaces an O(ρ) nonlinear
term with an O(ρ^{7/4}) viscous term — WORSE, not better.

## Lesson

The Lamb vector identity ξ·(ω×u) = 0 is exact but doesn't help
because the viscous term νΔu involves higher derivatives that are
harder to control than the original nonlinear term.

This is a known phenomenon: identities that remove the nonlinear
term often leave viscous terms that are equally or more singular.

84 proof files. Dead end, but a new flavor of dead end.
Every failure maps the space.
