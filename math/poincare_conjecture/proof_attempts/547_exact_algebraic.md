---
source: EXACT ALGEBRAIC STRUCTURE — all values at -11/64 are clean algebraic numbers
type: THE COMPLETE EXTREMAL CONFIGURATION — ready for formal verification
file: 547
date: 2026-03-31
instance: CLAUDE_OPUS (500s)
---

## THE EXACT EXTREMAL CONFIGURATION FOR N=3

### k-vectors (unit sphere)
k₀ = (0, 0, 1)
k₁ = (√7/4, 0, -3/4)
k₂ = (-5√7/28, √(3/14), -3/4)

Pairwise angles: cosθ₀₁ = cosθ₀₂ = -3/4, cosθ₁₂ = 1/4.

### Vorticity direction
ê = (√6, -1, 0) / √7

(Perpendicular to k₀. ex² = 6/7, ey² = 1/7.)

### Perpendicular direction
b̂ = (1, √6, √7) / √14

(φ = π/4: equal weight to in-plane and z-direction.)

### Mode amplitudes
w₀ = ê (perfectly aligned, γ₀ = 0°)
w₁ = (1/2)ê + (√3/2)b̂ (γ₁ = 60°)
w₂ = (1/2)ê - (√3/2)b̂ (γ₂ = 60°)

### Verification of div-free
w₀ · k₀ = 0 ✓ (ê has no z-component)
w₁ · k₁ = 0 ✓ (verified to 10⁻¹⁶)
w₂ · k₂ = 0 ✓ (verified to 10⁻¹⁶)

### Correction values (EXACT fractions)
P₀₁ = P₀₂ = -1/16
P₁₂ = -9/16

**C = -1/16 - 1/16 - 9/16 = -11/16**

### Vorticity magnitude
|ω|² = |w₀+w₁+w₂|² = |2ê|² = **4**

### The ratio
**C/|ω|² = (-11/16)/4 = -11/64** ∎

## THE ALGEBRAIC PROOF PATH

Every quantity is an exact algebraic number:
- k-angles: -3/4, 1/4 (rationals)
- e_hat components: √(6/7), 1/√7 (square roots of rationals)
- phi: π/4 (clean angle)
- Mode parameters: a={1, 1/2, 1/2}, |b|={0, √3/2, √3/2}
- P values: -1/16, -9/16 (rationals)
- C: -11/16 (rational)
- |ω|²: 4 (integer)

To PROVE C ≥ -11/64 for ALL N=3 configurations:
Express C/|ω|² as a function of the geometry (k-angles + polarizations),
compute its gradient, verify the critical point, and check second-order
conditions + boundary behavior. All in exact arithmetic.

## SUMMARY TABLE

| Quantity | Exact value |
|----------|-------------|
| cosθ₀₁ = cosθ₀₂ | -3/4 |
| cosθ₁₂ | 1/4 |
| sin²θ₀₁ = sin²θ₀₂ | 7/16 |
| sin²θ₁₂ | 15/16 |
| ex² | 6/7 |
| ey² | 1/7 |
| φ (b̂ tilt) | π/4 |
| a₀, a₁, a₂ | 1, 1/2, 1/2 |
| |b₁|, |b₂| | √3/2 |
| P₀₁ = P₀₂ | -1/16 |
| P₁₂ | -9/16 |
| C | -11/16 |
| |ω|² | 4 |
| **C/|ω|²** | **-11/64** |

## 547. Complete algebraic characterization of the N=3 extremum.
## All values are exact: rationals and square roots of rationals.
## The configuration is ready for Euler-Lagrange verification.
