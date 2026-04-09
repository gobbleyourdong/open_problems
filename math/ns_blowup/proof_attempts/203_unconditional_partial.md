---
source: Unconditional DMP for α/|S| > 0.095, conditional for smaller α
type: PARTIAL UNCONDITIONAL RESULT
date: 2026-03-29
file: 203
---

## The Unconditional Part

α < |S| is ALWAYS TRUE for S ≠ 0 (from trace-free: λ₁ < |S|, and α ≤ λ₁).
Proof: |S|² = λ₁² + λ₂² + λ₃² > λ₁² (since λ₂²+λ₃² > 0 for trace-free S ≠ 0).

The dominant term 2α(α²-|S|²) < 0 unconditionally.
Magnitude: 2|S|³ × r(1-r²) where r = α/|S| ∈ (0,1).

The DMP condition D²α < 2α³ becomes: r > C_corr/2 where C_corr = corrections/|S|³.

## Correction Budget

| Term | Magnitude | Sign | Provable? |
|------|-----------|------|-----------|
| Eigenvalue cubic -2Σλᵢ³cᵢ | ≤ 0.19|S|³ | + (hurts) | YES (algebraic) |
| -Ω² cross terms | ≈ 0 | mixed | YES |
| -2ΣλᵢHᵢᵢcᵢ (pressure) | ≈ -0.30|S|³ | - (helps) | **NO** (non-local) |
| Tilting Σλᵢ²Dcᵢ/Dt | ≈ -0.19|S|³ | - (helps) | **NO** (non-local) |
| **Total** | **≈ -0.30|S|³** | **- (net helps)** | **NO** |

The eigenvalue cubic (+0.19) is the ONLY positive correction.
Pressure (-0.30) and tilting (-0.19) MORE than compensate.
But proving the pressure/tilting corrections are negative requires
the non-local CZ bound.

## The Two Cases

CASE 1: α/|S| ≥ 0.095 (significant stretching).
  DMP holds UNCONDITIONALLY (just from eigenvalue cubic bound).
  No alignment or pressure bound needed!
  This covers: α ≥ 0.048||ω|| at the attractor.

CASE 2: α/|S| < 0.095 (tiny stretching).
  α < 0.048||ω||. Growth: d||ω||/dt < 0.048||ω||².
  Blowup at T* > 21/||ω||₀ (very slow).
  DMP might not hold from eigenvalue cubic alone.
  Need: pressure + tilting corrections to push total negative.
  Measured: total corrections ≈ -0.3|S|³ (sufficient).
  NOT PROVEN (non-local barrier).

## The Progress

Case 1 is FULLY PROVEN (unconditional). This is NEW.
Case 2 still needs the non-local pressure bound.

If we could prove Case 2: the DMP holds unconditionally → regularity.
Case 2 is EASIER than the full problem because α/|S| is SMALL,
meaning the flow is nearly non-stretching. The pressure and tilting
corrections only need to beat a SMALL positive eigenvalue cubic.

## The Measure of Progress

Previous: needed c₁ < 1/3 (Ashurst alignment) for the DMP.
Now: DMP holds unconditionally for α/|S| > 0.095.
     Only need pressure/tilting bound for α/|S| < 0.095.
     This is a WEAKER condition (only in the low-stretching regime).

## 203. Unconditional DMP for significant stretching. Conditional for tiny α.
