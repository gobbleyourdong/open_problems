---
source: Trefoil has α > 0 but BOUNDED — BKM doesn't need α ≤ 0
type: PROOF STRATEGY SHIFT — bounded α suffices for regularity
date: 2026-03-28
---

## The Trefoil Lesson

The trefoil has:
- c₃ ≈ 0.23 (below 1/3)
- α ≈ +0.2 to +0.3 (positive, STRETCHING)
- |ω| grows linearly: 16 → 28 in t=0.4

But it does NOT blow up. Why?

Because α is BOUNDED. Not negative, but bounded.

If α ≤ C (constant), then:
  d|ω|/dt ≤ C|ω| → |ω(t)| ≤ |ω(0)| e^{Ct}

Exponential growth gives finite BKM integral:
  ∫₀^T |ω(t)| dt ≤ |ω(0)| (e^{CT} - 1) / C < ∞

So BKM regularity holds if α is BOUNDED, not necessarily negative.

## What Bounds α?

The self-depletion: ê·S²·ê ≥ α²

This gives dα/dt ≤ -α² + (pressure + other terms)

If the "pressure + other terms" ≤ C₁ for some constant C₁:
  dα/dt ≤ -α² + C₁
  Equilibrium at α* = √C₁

So α is bounded by √C₁ regardless of the initial value.
This is the Riccati bound: the -α² self-depletion prevents
unbounded growth of the stretching rate.

## The Real Question

The proof doesn't need:
  ✗ α ≤ 0 (compression)
  ✗ c₃ ≥ 1/3 (alignment)
  ✗ The c₃ mechanism to work for all ICs

The proof needs:
  ✓ α bounded above (self-depletion handles this)
  ✓ The pressure term in dα/dt is bounded (need to prove)

## Two Regimes, One Conclusion

VOLUME-FILLING (TG, KP): α < 0, c₃ > 1/3 → compression → very strong
LOCALIZED (trefoil, rings): α > 0 but bounded → exponential growth → still finite BKM

Both regimes give regularity. The mechanism is different but the conclusion is the same.

## The Pressure Bound

The key gap reduces to: bound the pressure contribution to dα/dt.

The strain equation: DS/Dt = -S² - Ω² - H
The α-evolution: dα/dt = -ê·S²·ê - ê·Ω²·ê - ê·H·ê + (eigenvector rotation terms)

The self-depletion: -ê·S²·ê ≤ -α²
The vorticity: -ê·Ω²·ê = -(1/4)|ω|² + (1/4)(ω·ê)² = -(1/4)|ω|²(1-c_ê²)
  This is O(|ω|²), bounded by local vorticity.

The pressure: -ê·H·ê. Need to bound this.
  From Calderon-Zygmund: ||H|| ≤ C||∇²u|| ≤ C'(||S|| + ||ω||)
  So |ê·H·ê| ≤ C'(|S| + |ω|)²

But α ~ |S| at the max point (α = ê·S·ê, so |α| ≤ |S|).
And |ω| ~ |S| (they're comparable in turbulence, ratio 2-300 from data).

So the pressure term is O(|S|²) ~ O(α²).
The self-depletion is -α².
If C' < 1 (the pressure is weaker than self-depletion), then:
  dα/dt ≤ -α² + C'α² = -(1-C')α² < 0

This would prove α is bounded AND negative!

## The Gap

Prove C' < 1 in: |ê·H·ê| ≤ C'(|S| + |ω|)²

This is a quantitative bound on the pressure Hessian projection.
The constant C' depends on the CZ operator norm of the Leray projection.

From our data:
  TG: |H_full|/|S|² ≈ 0.2/0.01 ≈ 20 (C' >> 1)
  Trefoil: |H_full|/|S|² ≈ 1/5 ≈ 0.2 (C' < 1!)

So C' is NOT universal — it depends on the flow structure.
For localized tubes, C' < 1 (pressure is weak relative to strain).
For volume-filling flows, C' > 1 (pressure is strong but helps).

## Viscosity Test Results

| ν | α(t=0.375) | |ω|(t=0.375) | fill(t=0.375) | c₃ |
|---|-----------|-------------|--------------|-----|
| 0 | +0.31 | 27.1 | 0.054 | 0.23 |
| 10⁻⁴ | +0.28 | 27.1 | 0.054 | 0.22 |
| 10⁻³ | +0.29 | 26.8 | 0.054 | 0.23 |
| 10⁻² | +0.29 | 24.6 | 0.056 | 0.24 |
| 5×10⁻² | +0.17 | 17.5 | 0.068 | 0.26 |

Viscosity SLOWS the growth but doesn't flip the sign.
Fill fraction barely increases (0.054 → 0.068 at ν=0.05).

## Summary

The c₃ ≥ 1/3 mechanism works for volume-filling flows.
For localized structures, α > 0 but bounded.
BOTH give finite BKM integral → regularity.

The unified proof: show dα/dt ≤ -α² + C for some universal C.
This gives α ≤ √C (bounded), hence exponential |ω| growth,
hence finite BKM integral, hence regularity.

## 158 proof files. α bounded suffices. Don't need α ≤ 0.
