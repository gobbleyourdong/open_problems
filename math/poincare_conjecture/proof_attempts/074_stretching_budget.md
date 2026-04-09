---
source: Stretching budget analysis from L¹ vorticity evolution
type: STRUCTURAL IDENTITY — positive and negative stretching are linked
status: Conservation law found, doesn't bound either part individually
date: 2026-03-26 cycle 20
---

## The Stretching Budget Identity

From d/dt ||ω||_1 = ∫ρ(α₊-α₋) dx - ν∫ρ|∇ξ|² dx:

```
∫₀ᵀ∫ρα₊ dx dt - ∫₀ᵀ∫ρα₋ dx dt = ||ω(T)||_1 - ||ω(0)||_1 + ν∫₀ᵀ∫ρ|∇ξ|² dx dt
```

The RHS is bounded by CE₀/ν (unconditionally).

So: **positive stretching = negative stretching + bounded correction**

```
∫∫ρα₊ = ∫∫ρα₋ + O(E₀/ν)
```

## Interpretation

The positive stretching is PAID FOR by negative stretching plus
a bounded "credit" from the initial energy. Each positive stretching
event must be followed (or preceded) by negative stretching of
comparable magnitude.

This is the stretching BUDGET: the flow has a finite credit
(E₀/ν) that it can spend on net positive stretching. Beyond that,
every positive stretch must be balanced by a negative stretch.

## Why It Doesn't Close

The budget bounds the NET stretching (∫∫ρα dx dt = O(E₀/ν)).
It does NOT bound the POSITIVE part (∫∫ρα₊) alone.
The negative stretching ∫∫ρα₋ could be large (many anti-twist
events), enabling equally large ∫∫ρα₊.

For regularity: need ∫ρ_max α₊ dt bounded (POINTWISE at x*).
The global budget gives ∫∫ρα₊ dx dt → includes all points.
Pointwise extraction → same wall.

## For the Paper

This is a nice structural result: the total net stretching budget
is finite and bounded by initial energy / viscosity. Combined with
the anti-twist mechanism, it explains why ∫stretch₊ → 0: the
negative stretching (anti-twist) consumes the budget faster
than positive stretching can accumulate.

74 proof attempt files. Dead end for the proof, useful for the paper.
