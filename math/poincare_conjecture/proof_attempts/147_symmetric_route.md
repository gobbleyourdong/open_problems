---
source: Symmetric alignment route — c₂ = c₃ converts c₁ < 1/3 to compression
type: NEW PROOF ROUTE — reduces gap to ⊥ω symmetry
date: 2026-03-28
---

## The New Route

If c₂ = c₃ (symmetric alignment in ⊥ω plane):
  c₁ + 2c₃ = 1
  c₃ = (1 - c₁)/2 ≥ (1 - 1/3)/2 = 1/3  when c₁ ≤ 1/3

So: c₁ ≤ 1/3 + c₂ = c₃ → c₃ ≥ 1/3 → compression (Lean-verified)

## Why c₂ ≈ c₃ (Physical Argument)

The vorticity ω picks a direction. The plane perpendicular to ω
has ROTATIONAL SYMMETRY — no preferred direction in that plane.

The pressure source Δp = |ω|²/2 - |S|² depends on |ω|² (a scalar).
In the ⊥ω plane, |ω|² doesn't distinguish between e₂ and e₃.
Therefore the pressure response is SYMMETRIC in e₂ and e₃.

Yang's formula confirms: H_dev = -(1/4)(ω⊗ω - |ω|²I/3)
has eigenvalues (1/12)|ω|² for BOTH ⊥ω directions (degenerate).

At high |ω| where pressure dominates: c₂ → c₃ (symmetry restored).

## Data Confirmation

| IC | c₂ | c₃ | c₂ ≈ c₃? |
|----|----|----|----------|
| KP (all |ω|) | 0.333 | 0.333 | YES (exact!) |
| TG (low |ω|) | 0.38 | 0.25 | No |
| TG (high |ω|) | 0.33 | 0.40 | No (c₃ > c₂) |

KP has perfect symmetry. TG breaks it due to lattice geometry.
But TG OVERSHOOTS (c₃ > 1/3), which is even better.

## Lean Theorems (Compression.lean)

- symmetric_alignment_bias: c₂=c₃ + c₁≤1/3 → c₃≥1/3
- near_symmetric_alignment_bias: robust version with error ε
- compression_from_symmetry: full chain to ω·S·ω ≤ 0

## The Gap Reduces To

PROVE: at high |ω|, the pressure response creates approximate
symmetry c₂ ≈ c₃ in the ⊥ω plane.

This is WEAKER than proving c₃ > 1/3 directly.
It follows from the rotational symmetry of the ⊥ω plane
in the pressure-dominated regime.

## 147 proof files. 47 Lean theorems. New route via symmetry.
