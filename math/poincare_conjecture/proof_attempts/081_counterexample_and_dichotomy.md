---
source: Counterexample to codimension argument + dichotomy analysis
type: BUG FIX — codimension argument fails for 2D-type data, but dichotomy saves it
status: Dichotomy works conceptually, quantitative bound is ∫α²/ρ ≤ C (too weak)
date: 2026-03-26 cycle 27
---

## Counterexample to |∇ξ| ≥ c/σ₃

ω = f(x,y) ẑ on T³. Then ξ = ẑ (constant), |∇ξ| = 0, but |ω| = |f|
can have arbitrary sharp maximum. So |∇ξ| ≥ c/σ₃ is FALSE.

This is a 2D-type flow — known to be regular (no stretching when
ω is unidirectional). But it breaks the codimension argument.

## The Dichotomy

Two cases at x*:

### Case 1: |∇ξ(x*)| > c₀ (direction varies)
The codimension/Lagrangian argument gives constraints on ρ.
But the exact exponents depend on the model (tube vs sheet).

### Case 2: |∇ξ(x*)| < c₀ (direction nearly constant)
From Buaria identity: α ≤ Cρ|∇ξ| ≤ Cρc₀ (stretching is small).
Small α → slow growth → long-time existence.

### Combined: α ≤ Cρ × max(|∇ξ|, some lower bound)
The key: α is ALWAYS bounded by Cρ|∇ξ| through the Buaria identity.
So: α/(Cρ) ≤ |∇ξ| → |∇ξ| ≥ α/(Cρ)

Substituting into Constantin: ∫ρ × (α/(Cρ))² dt ≤ C₂
→ **∫α²/ρ dt ≤ C₁²C₂** — UNCONDITIONAL time-integrated bound!

## What ∫α²/ρ ≤ C Gives

By CS: (∫α dt)² ≤ (∫α²/ρ dt)(∫ρ dt) ≤ C × ∫ρ dt

For blowup: (log ρ)² ≤ C × ∫ρ dt. Since ∫ρ dt diverges at blowup:
no contradiction. The bound is TOO WEAK.

Need: ∫α dt ≤ C (directly) or ∫α²/ρ^{1-ε} ≤ C for some ε > 0.

## The Remaining Gap

α ≤ Cρ|∇ξ| + Constantin gives ∫α²/ρ ≤ C.
Regularity needs ∫α ≤ C or ∫α²/ρ^{1-ε} ≤ C.
The gap: the 1/ρ weight in ∫α²/ρ is too generous for large ρ.

To close: need a TIGHTER bound on α in terms of |∇ξ|.
If α ≤ Cρ^{1-δ}|∇ξ| for some δ > 0: then ∫α²/ρ^{1+2δ} ≤ C,
which would give regularity for δ > 1/2.

But α ≤ Cρ|∇ξ| is SHARP from the Buaria identity (no δ improvement).

## Status

The counterexample killed the clean ρ⁵ ≤ C|ω₀|⁴ bound.
The dichotomy gives ∫α²/ρ ≤ C (new, but too weak for regularity).
The gap: the Buaria bound α ≤ Cρ|∇ξ| has the wrong ρ power.

81 proof files. The space is FULLY MAPPED. Every analytical path
hits the same wall in different disguise. The computer-assisted
theorems (59 verified) remain the strongest results.
