# Reduced Volume Certificate — Perelman's Most Sophisticated Invariant

## Date: 2026-04-09
## Script: numerics/reduced_volume.py

## CERTIFICATE

Perelman's reduced volume V(τ) on round S³ shrinking soliton:

| Quantity | Value | Status |
|----------|-------|--------|
| l(p, τ) at basepoint | 3/2 (constant) | EXACT |
| V(τ) on round S³ | 2·e^(-3/2)·√π ≈ 0.790976 | EXACT (constant) |
| V_R³ | 1.0 | by definition |
| V_S³ ≤ V_R³ | 0.7910 ≤ 1.0 | YES (Perelman bound) |
| Monotonicity at soliton | 0.000000 change | YES (equality) |

## Key Identity

  V_S³(τ) = 2 · e^(-3/2) · √π = 0.790976...  ∀ τ > 0

This is the reduced volume of the round S³ shrinking soliton,
constant in τ because round S³ is a soliton (equality in monotonicity).

## Connection to κ-Noncollapsing

Perelman: V(τ) ≥ κ ⟹ κ-noncollapsing.
Round S³: κ ≥ V_S³ ≈ 0.7910 (reduced-volume κ).
Compare volume bound: vol/r³ = 2π² ≈ 19.7392.

The reduced-volume κ is much smaller but is the one PRESERVED under
Ricci flow with surgery. This is the technical content of Perelman's
no-local-collapsing theorem.

## Reproducibility

Dependencies: numpy. Runtime: < 1 second.
