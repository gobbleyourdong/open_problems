---
source: Global enstrophy evolution attempt
type: DEAD END — reduces to same bounds
status: No new information from global approach
date: 2026-03-26 cycle 14
---

## Attempt: Use global enstrophy equation + single-mode orthogonality

The enstrophy equation:
d/dt ||ω||_2² = 2∫ω·S·ω dx - 2ν||∇ω||_2²

In Fourier: ∫ω·S·ω dx = Σ_{triads} ω̂·Ŝ·ω̂*
Diagonal (self-interaction) terms are ZERO (our lemma).
Only off-diagonal (cross-mode) contribute.

## Why It Doesn't Help

The diagonal terms were already zero by the lemma.
Removing them doesn't improve the CZ bound on the total.
The off-diagonal bound ≤ ||ω||_2² × ||S||_∞ is the same
whether or not diagonals are included (they contribute 0 either way).

## The Real Issue

Global (integral) approaches naturally avoid the pointwise wall,
but they lose the information about what happens AT x*.
The enstrophy controls ||ω||_2, not ||ω||_∞.
Going from L² to L∞ requires Sobolev embedding with derivative loss.

This is the same gap from a different direction:
- Local approach: pointwise at x*, needs far-field bound
- Global approach: integral over space, needs Sobolev embedding to get pointwise
Both need ||∇ω||_2 or higher, which isn't independently controlled.

## Lesson

The single-mode orthogonality is a POINTWISE (per-mode) result.
Its power is in the local geometry at x*, not in global integrals.
The global enstrophy equation doesn't gain from it.

Dead end. Every failure maps the space.
