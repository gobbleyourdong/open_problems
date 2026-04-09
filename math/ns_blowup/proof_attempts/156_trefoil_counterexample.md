---
source: Trefoil knot shows persistent α > 0, growing |ω|, c₃ < 1/3
type: COUNTEREXAMPLE to -Ω² dominance — IC-dependent mechanism
date: 2026-03-28
---

## The Trefoil Data (Euler, N=32 and N=48)

| t | |ω|_max | c₃ (top 10%) | α (top 10%) | c₃ ≥ 1/3? | α ≤ 0? |
|---|--------|-------------|-------------|-----------|--------|
| 0.00 | 16.0 | 0.261 | -0.010 | NO | YES |
| 0.04 | 17.1 | 0.250 | +0.064 | NO | **NO** |
| 0.10 | 19.8 | 0.241 | +0.102 | NO | **NO** |
| 0.20 | 23.2 | 0.252 | +0.156 | NO | **NO** |
| 0.30 | 25.7 | 0.242 | +0.214 | NO | **NO** |
| 0.38 | 27.1 | 0.219 | +0.303 | NO | **NO** |

At the top 1% |ω| at t=0.4: c₃ = 0.132, α = +1.07.

Confirmed at N=48: same pattern. Well-resolved (spec < 10⁻³).

## What This Means

1. The trefoil has PERSISTENT positive stretching at high |ω|
2. c₃ is BELOW 1/3 and DECREASING (moving away from 1/3)
3. α is POSITIVE and GROWING (not bounded so far)
4. |ω| is growing (16 → 27) but this is EULER with no viscosity
5. The -Ω² dominance over -H is NOT universal

## Why the Trefoil is Different

The trefoil knot has:
- Concentrated vorticity along a curve (1D structure in 3D)
- Self-linking (topological complexity)
- Reconnection events that concentrate vorticity

Unlike TG/KP which are spatially extended (volume-filling), the trefoil
has localized vortex tubes. The strain field around a single tube has
ω aligned with e₂ (Ashurst), NOT e₃.

The -Ω² term does push e₃ toward ω, but the pressure response for a
localized tube is STRONGER (better approximated by the Biot-Savart
integral of a line vortex).

## Is This Fatal for the Proof?

NOT NECESSARILY. Key observations:

1. **This is Euler, not NS.** With viscosity, the trefoil core diffuses
   and the stretching rate α gets damped.

2. **BKM needs ∫||ω||_∞ dt = ∞, not just α > 0.**
   Even with α = +0.3, the growth is at most exponential (e^{0.3t}),
   which gives finite BKM integral on any finite interval.

3. **The self-depletion dα/dt ≤ -α² + (pressure) still applies.**
   If α → large, the -α² term kills it. But the pressure grows too.

4. **The trefoil may eventually resolve** — at longer times, the
   reconnection reduces topology and the flow settles into TG/KP-like
   behavior. We haven't run long enough.

## What the Trefoil Teaches Us

The mechanism is NOT simply "-Ω² beats -H at all flows."
The mechanism is GEOMETRY-DEPENDENT:

- Volume-filling vorticity (TG, KP, curl noise): -Ω² wins, c₃ > 1/3
- Localized tubes (rings, trefoil): Ashurst alignment c₂ ≈ 1
  - Rings: α ≈ 0 (quasi-2D)
  - Trefoil: α > 0 (active stretching from reconnection)

The proof must handle BOTH cases:
- Volume-filling: use the c₃ ≥ 1/3 → compression route
- Localized tubes: need a DIFFERENT argument (maybe BKM directly
  from the tube dynamics, or use viscosity)

## Revised Gap

The gap is now TWO-PART:
1. For volume-filling flows: prove c₃ ≥ 1/3 (may work via -Ω²)
2. For localized tubes: prove α stays bounded (needs different tools)

Or find a UNIFIED argument that handles both.

## 156 proof files. Trefoil is a genuine counterexample to the simple story.
