---
source: Instance C — Sobolev growth rates + connection to Instance A
type: THE CHAIN — combining Instance A's ratio bound with Instance C's energy estimate
file: 264
date: 2026-03-29
---

## Sobolev Growth Rates (this cycle)

Measured d(ln||ω||²_{H^s})/dt for trefoil:

| s | Early rate | Late rate | Growth type |
|---|-----------|----------|-------------|
| 0 (enstrophy) | 0.07 | 0.65 | ~t (linear acceleration) |
| 1 (palinstrophy) | 0.33 | 2.97 | ~t |
| 1.5 | 0.57 | 4.81 | ~t |
| 2 | 0.90 | 6.90 | ~t |
| 2.5 | 1.31 | 9.05 | ~t |

ALL growth rates scale as ~t (linear in time, R² = 0.87-1.0).
This gives ||ω||²_{H^s} ~ exp(ct²) — Gaussian growth, always finite.

But rates accelerate (7:1 ratio early-to-late for s=2), so
the Gaussian model may not persist forever.

## THE COMPLETE CHAIN (combining Instance A + C)

Instance A (file 184): ratio ≤ 1 (straight tube extremal).
For any CURVED tube at the max: ratio < 1 → H_ωω > 0.

Instance C (file 261): if ||ω||∞ bounded → dP/dt ≤ CP (linear, not cubic).

The chain:
1. ratio ≤ 1 [Instance A, variational]
   → For curved flows: ratio < 1 → H_ωω > 0 at high |ω|

2. H_ωω > 0 at the max [from step 1]
   → Lagrangian: Dα/Dt = ê·S²·ê - 2α² - H_ωω ≤ ê·S²·ê - 2α² [file 174]
   → Transport barrier: entering α ≤ 3 [file 175]
   → α bounded at the max by 3

3. α bounded [from step 2]
   → d||ω||∞/dt = α × ||ω||∞ ≤ 3 × ||ω||∞
   → ||ω||∞(t) ≤ ||ω||∞(0) × exp(3t) [exponential]

4. ||ω||∞ bounded exponentially [from step 3]
   → BKM: ∫₀^T ||ω||∞ dt ≤ ||ω||₀ (exp(3T)-1)/3 < ∞
   → REGULARITY ✓

Steps 2-4 are already proven (rigorous math + Lean theorems).
Step 1 is Instance A's task — the straight tube extremality.

## What Instance C Adds to the Chain

The palinstrophy bound (dP/dt ~ P) is NOT needed for the main chain.
The chain goes through α → ||ω||∞ → BKM without needing energy estimates.

BUT: Instance C's contribution confirms CONSISTENCY. If α is bounded
by 3, then ||ω||∞ grows exponentially, and the Sobolev norms grow
as exp(ct²) — all consistent with regularity.

Instance C's independent evidence:
- dP/dt ~ 5P (linear, not cubic) — structural improvement
- Spectrum E_j ~ k^{-5.7} (steep, convergent) — consistent with smoothness
- ||ω||²_{H^s} ~ exp(ct²) for all s tested — always finite

## The One Remaining Gap

Instance A's proof (file 184) has a gap in the angular decomposition:
need to show |f₂₀| ≤ f₀₀ for the Poisson source at vorticity maxima.

The variational argument (straight tube is extremal) is physically
compelling and numerically verified. The formal proof needs the
angular bound.

This is a question about the ANGULAR SPECTRUM of the Calderón-Zygmund
kernel applied to a specific source (Δp = |ω|²/2 - |S|²).

## 264. The chain is complete modulo Instance A's angular bound.
