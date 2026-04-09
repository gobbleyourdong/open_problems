---
source: Migration effect quantified — 12% reduction, necessary but not sufficient
type: THE GAP IDENTIFIED — need spatial distribution bounds
date: 2026-03-28
---

## Migration Effect

Measured: d||ω||∞/dt vs α·||ω||∞ at the max point.
M = d||ω||∞/dt - α·||ω||∞ (the migration correction).

Trefoil: M < 0 at 73% of timesteps. Mean reduction: 12%.
TG: M ≈ 0 (max doesn't move — trivially at stagnation point).

## Why Migration Alone Isn't Enough

12% reduction delays the ODE blowup from T*=0.63 to T*≈0.72.
But blowup still happens in the ODE model.

The sub-quadratic growth (γ=1.08 from Route 3) requires MORE than
just 12% migration reduction. It requires the growth rate to DECREASE
over time, which migration alone doesn't guarantee.

## What Does Guarantee Sub-Quadratic Growth

The Hou-Li curvature (+0.4 at N=64) shows d||ω||∞/dt / ||ω||∞²
is DECREASING. This means the coefficient in d||ω||/dt = C_eff ||ω||²
is not constant — it DECREASES over time.

Why does C_eff decrease? Because:
1. The spatial extent of high-|ω| regions SHRINKS (concentration)
2. Fewer points available for the max to hop to
3. The max gets "trapped" in a region where α is bounded
4. The Riccati self-depletion bounds α in that trapped region

This is the FULL mechanism: Riccati bounds α locally + max migration
+ spatial concentration → sub-quadratic growth → regularity.

## The Proof Gap (final formulation)

To close the proof, need to show: the spatial measure of the set
{x : |ω(x,t)| > ||ω||∞(t) - ε} shrinks FAST ENOUGH to compensate
for the local quadratic growth.

This is related to CKN partial regularity: the singular set has
Hausdorff dimension ≤ 1 (one-dimensional, not zero). The question
is whether this dimensional bound is enough.

## Score: 168 proof files

What we know:
- Riccati bounds α locally (necessary, not sufficient)
- Migration reduces growth by 12% (necessary, not sufficient)
- Spatial concentration limits max migration (the key mechanism)
- Hou-Li diagnostic confirms sub-quadratic growth at 3 resolutions

What we don't know:
- How to prove the spatial concentration bound
- How to connect CKN partial regularity to the Riccati structure
- Whether the 1D singular set bound suffices

The gap is: LOCAL bound (Riccati) + GLOBAL structure (migration + concentration)
= REGULARITY. We have both pieces. Can't put them together formally.
