---
source: W1 = E/||ω||²∞ is monotonically decreasing (measured)
type: CANDIDATE MONOTONE FUNCTIONAL — Perelman-type
date: 2026-03-29
file: 210
---

## The Discovery

W1(t) = ∫|ω|²dx / ||ω||²∞ = E / M²

is MONOTONICALLY DECREASING for the trefoil (Euler, N=32).
14/14 measurements show dW1/dt < 0.

## What W1 Measures

W1 = E/M² is the INVERSE CONCENTRATION of vorticity.
  W1 large: vorticity spread out (||ω||∞ small relative to total)
  W1 small: vorticity concentrated (||ω||∞ large relative to total)

W1 ≥ 0 always. W1 → 0 means total concentration at a point.

## Why W1 Decreasing is Significant

dW1/dt = 2∫|ω|²(α - α*) dx / M²

where α* = stretching at the max-|ω| point.

dW1/dt < 0 ⟺ <α>_E < α* (enstrophy-weighted mean α < α at max).

This says: the MAX POINT has MORE stretching than the average.
The vorticity concentrates toward the max.

## Can W1 Decreasing Give Regularity?

W1 ≥ 0 and dW1/dt ≤ 0: so W1 → some limit L ≥ 0.

E(t) = W1(t) × M(t)². If W1 → L > 0: E ~ L × M².
And dE/dt = 2∫|ω|²α ≤ 2||α||_∞ E ≤ 2||S||_∞ E ≤ C × M × E.

So: dE/dt ≤ C × M × E. And E ~ L × M²: d(LM²)/dt ≤ C × M × LM².
2LM dM/dt ≤ CLM³ → dM/dt ≤ CM²/2 → possible blowup (quadratic).

So W1 → L doesn't directly bound M. The concentration COULD continue
until W1 = 0 (delta function), which allows M → ∞.

## BUT: W1 → 0 Requires Infinite Concentration

W1 → 0 means ALL the enstrophy concentrates to measure zero.
On T³ with smooth solutions: this requires ω to become MORE
AND MORE concentrated. The RATE of concentration is bounded
by the dynamics (stretching can only compress so fast).

If the concentration rate is SLOWER than the growth rate:
W1 stays bounded away from 0, and M is controlled.

## Cross-Validation Needed

Test W1 on TG and KP. If W1 is ALWAYS decreasing for ALL ICs:
it's a UNIVERSAL monotone functional. Then proving dW1/dt ≤ 0
from the PDE would be a significant step.

## The Connection to Perelman

Perelman's μ-functional is analogous: it measures the CONCENTRATION
of the geometry (how peaked the curvature is relative to the average).
μ non-decreasing → geometry doesn't collapse → no singularity.

Our W1 non-increasing: inverse concentration decreasing.
But we need non-increasing, and W1 is decreasing (concentration increases).
This is the WRONG direction for preventing singularity!

For regularity: we'd need a functional that PREVENTS concentration.
W1 decreasing means concentration IS happening (but slowly).

## 210. W1 = E/M² is monotone decreasing. Interesting but doesn't
## directly give regularity (it tracks concentration, not bounds it).
