---
source: α is NOT universally self-correcting, but a TRANSPORT BARRIER limits it at high |ω|
type: MECHANISM REFINEMENT — the bound is spatial, not pointwise
date: 2026-03-28
---

## What Broke

At α > 2.5 (all grid points): Dα/Dt > 0 at 58% of points.
Mean Dα/Dt = +1.8. Self-depletion does NOT dominate universally.
The simple bound "Dα/Dt < 0 when α > threshold" FAILS.

## What Still Holds

In the approaching zone (|ω| > 85% of max): max α ≤ 3.19 (file 175).
At the max-|ω| point: Dα/Dt < 0 (Lagrangian, file 174).

## The Resolution: Transport Barrier

High-α points at low |ω| CAN'T reach the max-|ω| zone because:

1. To enter the zone, a particle needs |ω| > 0.85×||ω||∞
2. Growing |ω| requires sustained positive α × |ω|
3. But as |ω| grows, H_ωω turns positive (the sign flip from file 174)
4. Positive H_ωω forces Dα/Dt < 0, reducing α
5. The particle arrives at the approaching zone with α ≈ 3 (measured)

The sign flip of H_ωω with |ω| creates a TRANSPORT BARRIER:
high-α material at low |ω| gets its α reduced as it approaches
the high-|ω| region. The barrier filters out high-α particles.

## The Three Layers

| |ω| range | H_ωω sign | α behavior | Dangerous? |
|-----------|-----------|-----------|-----------|
| Low (< 50% max) | < 0 | Can grow | NO (far from max) |
| Mid (50-85% max) | mixed | α filtered | Barrier zone |
| High (> 85% max) | > 0 | Decreasing | NO (compressive) |

The middle layer is the filter. As particles transit through it,
their α gets capped at ~3 by the increasing H_ωω.

## Why the ODE Misses This

The coupled Riccati ODE dα/dt = -α² + C|ω|² has CONSTANT C.
In reality, C depends on |ω| — it's NEGATIVE at high |ω| (helping)
and POSITIVE at low |ω| (hurting). The ODE uses the worst-case C
from low |ω| and misses the improvement at high |ω|.

## Proof Implications

The proof needs to formalize the transport barrier:
1. H_ωω(x) flips sign at |ω(x)| ≈ some threshold
2. Above the threshold: Dα/Dt < 0 (from H_ωω > 0 + self-depletion)
3. Particles can't cross the threshold with α > 3 because
   the transition zone reduces α
4. Therefore α ≤ 3 at the max → exponential growth → BKM finite

This requires an |ω|-DEPENDENT bound on the pressure Hessian,
not a uniform bound. The sign flip is the key structural feature
that the proof must capture.

## 176 proof files. The transport barrier is the mechanism.
