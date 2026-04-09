---
source: Flick vs Fall scaling — PHASE TRANSITION at |ω| ≈ 12
type: CRITICAL FINDING — not a power law, it's a sudden crossover
date: 2026-03-28
---

## The Data (TG, N=64, t=5, 30K sampled points)

| |ω| range | λ₁c₁ (flick) | λ₃c₃ (fall) | net α | c₃ |
|-----------|-------------|-------------|-------|-----|
| 0.3-0.5 | +0.17 | -0.28 | -0.11 | 0.38 |
| 0.5-1.0 | +0.18 | -0.25 | -0.06 | 0.42 |
| 1.0-1.7 | +0.20 | -0.27 | -0.05 | 0.38 |
| 1.7-3.0 | +0.31 | -0.24 | +0.14 | 0.21 |
| 3.0-5.4 | +0.57 | -0.29 | +0.39 | 0.17 |
| 5.4-9.5 | +1.15 | -0.49 | +0.70 | 0.21 |
| 9.5-12.7 | +1.46 | -0.66 | **+0.82** | 0.21 |
| **12.7-17.0** | **+0.74** | **-1.12** | **-0.31** | **0.47** |

## The Phase Transition

At |ω| ≈ 12:
- Flick COLLAPSES: 1.46 → 0.74 (halved)
- Fall SURGES: -0.66 → -1.12 (70% increase)
- Net α FLIPS: +0.82 → -0.31 (sign change!)
- c₃ JUMPS: 0.21 → 0.47 (more than doubles!)

This is NOT a smooth power law. The power law fits (flick ~ |ω|^0.79,
fall ~ |ω|^0.53) are WRONG because they average over the transition.

## The Correct Picture

Two regimes with a sharp crossover at |ω|* ≈ 12:

**Below |ω|* (stretching regime):**
- Flick dominates: λ₁c₁ > |λ₃c₃|
- Net α > 0 (positive stretching)
- c₃ ≈ 0.2 (below 1/3, vorticity near e₂)
- The top wobbles but stays upright

**Above |ω|* (compression regime):**
- Fall dominates: |λ₃c₃| > λ₁c₁
- Net α < 0 (compression!)
- c₃ ≈ 0.47 (well above 1/3, vorticity shifted to e₃)
- The top CRASHES

## The Threshold = Pressure Hessian Crossover

The transition at |ω| ≈ 12 matches:
- Our earlier pressure Hessian crossover measurement (ρ ≈ 12)
- The sign flip threshold (|ω| ≈ 13-17 across N=32,64,128)
- The ODE model activation threshold

All the same number. The pressure Hessian isotropization
triggers a catastrophic alignment shift at |ω| ≈ 12.

## Physical Mechanism (JB's spinning top)

Below threshold: the top wobbles around e₂ (neutral equilibrium).
Stretching flicks it toward e₁, pressure pushes it back.
The oscillation is symmetric around e₂.

Above threshold: the pressure response is so strong that e₁
becomes violently unstable. The top can't reach e₁ at all.
It falls through e₂ and into the e₃ valley (compression).
The oscillation center shifts from e₂ to e₃.

The fall is SUDDEN, not gradual. It's a phase transition
in the alignment dynamics, not a smooth decay.

## Implications for the Proof

The proof structure changes from "prove cos² decays as 1/|ω|"
to "prove there exists a threshold |ω|* above which
λ₃c₃ dominates λ₁c₁."

This is more tractable because:
1. The threshold comes from the Yang pressure Hessian (known, published)
2. The dominance of |λ₃c₃| over λ₁c₁ is the RICCATI structure
   dα/dt ≤ -α² acting on the e₁ component specifically
3. The collapse of c₁ (from 0.3 to 0.15) and surge of c₃ (from 0.2 to 0.47)
   are the SAME event — vorticity can't stay at e₁, must go to e₃

## 145 proof files. The gap is a phase transition, not a scaling law.
