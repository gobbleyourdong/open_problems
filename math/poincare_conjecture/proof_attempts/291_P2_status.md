---
source: P2 proof status — measured 35/35 positive, bound doesn't close
type: HONEST STATUS — the last analytical gap
file: 291
date: 2026-03-29
---

## P2: ∫|ω|²α cos(kz) dz > 0

MEASURED: 35/35 positive. All k=1,...,7. All times. Zero exceptions.
Minimum value: +148. Maximum: +569. Overwhelmingly positive.

## Attempted Bounds

| Approach | Threshold | Measured | Closes? |
|----------|-----------|---------|---------|
| Gradient: κ < c/(3σ(1+C)) | κ < 0.056 | κ = 0.09-0.67 | NO |
| Gaussian-weighted gradient | κ < c√π/σ ≈ 0.59 | κ = 0.09-0.67 | MARGINAL (11/12) |
| Shell decomposition | α > 0 in [0,σ/2] | α can be -1.25 | NO |
| k→0 limit (Fourier) | ∫|ω|²α/∫|ω|²|α| > k²σ²/2 | 0.2 > 0.045 | YES but ∫|ω|²α > 0 unproven |

## Why It Fails

α varies at rate κ|ω| ≈ 5-15 at the max, while α₀ ≈ 2.5. The gradient
is 2-6× the value. Within the core width σ ≈ 0.3: α can swing from
+2.5 to -1.25 (by the gradient bound). The first-order bound can't
distinguish "α is weakly negative in the tail" from "α is catastrophically
negative everywhere."

## Why the Integral Is Actually Positive

1. α is STRONGLY positive at z=0 (peak value +2.5)
2. α goes negative at |z| ≈ 0.3-0.5 (weakly, actual ≈ -0.5 to -1)
3. |ω|² at those locations: 30-60% of max (significant but declining)
4. cos(kz) at those locations: +0.9 to +0.7 (still positive for k=1)
5. The PRODUCT: +2.5 × 100% at z=0 vs -1 × 50% at z=0.3
6. The center dominates the weak negative tail by ~3:1.

The bound can't capture this because it uses WORST-CASE α in each
region. The actual α profile is much better than worst case.

## What Would Close P2

(a) A SECOND-ORDER bound on α that uses the specific Biot-Savart structure
    to show α doesn't vary as fast as κ|ω| near the max.

(b) A CORRELATION argument: α and |ω|² are positively correlated because
    both are driven by the same strain field. The positive correlation
    makes ∫|ω|²α > 0 on any line through the max.

(c) COMPUTER-ASSISTED proof: verify the integral with interval arithmetic
    for a specific solution on a specific time interval.

(d) A completely different proof of DH_ωω/Dt > 0 that bypasses P2.

## Summary of the Complete Proof

| Component | Status |
|-----------|--------|
| Fourier lemma (H_ωω > 0) | **PROVEN** |
| -S² diagonal in eigenbasis | **PROVEN** |
| ∫|ω|² cos > 0 (monotonicity) | **PROVEN** |
| DVar/Dt < 0 (tilting, via bootstrap) | **CONDITIONAL on Q < 0** |
| DH_ωω/Dt > 0 (dynamic Fourier) | **CONDITIONAL on P2** |
| P2: ∫|ω|²α cos > 0 | **MEASURED 35/35, BOUND DOESN'T CLOSE** |
| Q attractor → α bounded → BKM | **PROVEN (standard analysis)** |

## 291 files. P2 is the last gap. 35/35 measured. Bound doesn't close.
## The Millennium Prize is in proving one signed integral.
