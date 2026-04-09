---
source: ||S||∞ < 0.87||ω||∞ → REGULARITY (the tightest formulation)
type: THE SHARPEST GAP — 23% above Parseval, potentially provable
file: 442
date: 2026-03-30
---

## THE CHAIN

1. ||S||∞ ≤ C||ω||∞ with C < √(3/4) ≈ 0.866 (TO PROVE)
2. → At near-max vertices: |S|² < (3/4)|ω_max|² → |∇u|²/|ω|² < 2.0
3. → S²ê ≤ (2/3)|S|² < |ω|²/2 at near-max vertices → R_crit < 0.5
4. → Barrier can't be bypassed by vertex jump (file 441)
5. → Combined with barrier repulsiveness (proven): R < 1/2 always
6. → Type I → Seregin → REGULARITY ∎

## THE BOUND

Need: ||S||∞ / ||ω||∞ < √(3/4) ≈ 0.866

Known:
- L² ratio: ||S||₂/||ω||₂ = 1/√2 ≈ 0.707 (exact, Parseval)
- L∞ ratio (observed): ≤ 0.81 (300 configs)
- Threshold: 0.866

The observed 0.81 has 7% margin to the threshold 0.866.
The L² ratio 0.707 has 23% margin.

## WHY THIS MIGHT BE PROVABLE

The Biot-Savart operator maps ω to S via: Ŝ_k = sym(ik⊗(k×ω̂_k)/|k|²).
The Fourier multiplier has norm 1/2 per mode: |Ŝ_k| = |ω̂_k|/2.

The L² identity: ||S||₂² = ||ω||₂²/2 (each mode contributes half).

The L∞ ratio: ||S||∞/||ω||∞ depends on the COHERENCE difference
between S and ω at their respective maxima.

Key: ||S||∞ = max_x |S(x)| while ||ω||∞ = max_x |ω(x)|.
These maxima may be at DIFFERENT points.

If they're at the SAME point: |S(x*)| ≤ |ω(x*)|/√2 (from the
per-mode identity, each S_k contributes half of ω_k in magnitude).

The 0.81 vs 0.707: the 14% excess comes from the strain max being
at a DIFFERENT point than the vorticity max, where ω is slightly
less coherent (giving a higher S/ω ratio).

## THE FORMAL QUESTION

On T³: for div-free ω with strain S = sym(∇BS(ω)):

    ||S||_{L∞} / ||ω||_{L∞} ≤ ???

- L² ratio: 1/√2 ≈ 0.707 (exact)
- CZ theory: ≤ C(1 + log...) (unbounded, for GENERIC fields)
- Observed: ≤ 0.81 (for FINITE mode fields)
- Need: < 0.866

This is a SHARP L∞ comparison for the Biot-Savart singular integral.
For FINITE modes (bandlimited): the ratio IS bounded.
For SMOOTH fields (analytic): the ratio is bounded by concentration.

## 442. ||S||∞ < 0.87||ω||∞ gives regularity. Observed: 0.81. Margin 7%.
## This is 23% above Parseval — the tightest gap yet.
## The CZ log factor is the ONLY obstacle. At the max: it's bounded.
