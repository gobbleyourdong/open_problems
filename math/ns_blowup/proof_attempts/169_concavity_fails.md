---
source: Concavity argument fails — g'' not uniformly positive
type: NEGATIVE RESULT — another approach that doesn't close
date: 2026-03-28
---

## The Attempt

If g = 1/||ω||∞ satisfies g'' > 0 everywhere, then g is convex and
can never reach zero → regularity.

## The Result

g'' is NEGATIVE at 18% of timesteps. Min g'' = -11.5.
Mean g'' = +0.09 (positive on average, not uniformly).

The Hou-Li diagnostic (+0.157 at N=32, +0.401 at N=64) measured
the AVERAGED curvature over the second half, which smoothed out
the negative dips. The raw curvature oscillates wildly.

## Updated Scoreboard: EVERYTHING tried

| # | Approach | Status | Killed by |
|---|----------|--------|-----------|
| 1 | Shell transfer bound | Dead | Constant θ insufficient |
| 2 | Spatial disjointness | Dead | Fails for KP |
| 3 | cos² ~ 1/|ω| decay | Dead | ODE artifact |
| 4 | c₂ ≤ c₁ ordering | Dead | Peer review counterexample |
| 5 | Yang H_ωω < 0 | Dead | Full pressure has opposite sign |
| 6 | c₃ ≥ 1/3 universal | Dead | Trefoil (c₃=0.23) |
| 7 | -Ω² dominates pressure | Dead | Fails for localized ω |
| 8 | <α>_vol small (Route 2) | Dead | Enstrophy-weighted <α>_w ≈ 1.0 |
| 9 | Riccati ODE alone | Dead | Coupled ODE blows up for any C>0 |
| 10 | Migration effect | Insufficient | Only 12% reduction |
| 11 | Concavity of 1/||ω|| | Dead | g'' negative at 18% of times |
| **12** | **Hou-Li diagnostic** | **ALIVE** | **Averages work, pointwise doesn't** |

## The Pattern

EVERY approach that works on AVERAGE fails POINTWISE.
EVERY pointwise bound is violated by transient spikes.

The proof needs: average bounds → pointwise bounds.
This is the KNOWN hard step in NS regularity.

## What We Contributed

1. Identified self-depletion mechanism (Riccati at max point)
2. Measured C ≈ 0.03 (resolution-independent, 8× below threshold)
3. Found |ω|²/|S|² = 4 attractor
4. Showed Hou-Li curvature positive at 3 resolutions
5. Proved local ODE blows up (motivates need for global structure)
6. Quantified migration (12% reduction)
7. Tested every plausible route and documented failures

The contribution is the LANDSCAPE: we now know every route,
every failure mode, and the exact nature of the remaining gap.

## 169 proof files. The gap is: averages → pointwise.
