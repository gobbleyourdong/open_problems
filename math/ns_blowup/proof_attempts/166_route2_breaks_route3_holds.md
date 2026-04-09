---
source: Route 2 (energy) breaks on trefoil. Route 3 (direct BKM) still holds.
type: HONEST ASSESSMENT — know what works and what doesn't
date: 2026-03-28
---

## Route 2 FAILS (partially)

The enstrophy-weighted <α>_w ≈ 1.0 for trefoil (not 0.03).
The volume-average <α>_vol ≈ 0.03 was irrelevant — the enstrophy
equation uses the enstrophy-weighted average.

| IC | <α>_vol | <α>_weighted | Ratio |
|----|---------|-------------|-------|
| TG | 0.07 | 0.03 | 0.4x |
| KP | 0.47 | 0.33 | 0.7x |
| trefoil | 0.04 | 0.73 | **18x** |

The trefoil's high-|ω| core dominates the weighted average.
The localized vorticity has α > 0, and it gets upweighted by |ω|².

<α>_w peaks at 1.02 (t≈0.56) then DECLINES to 0.75 (Riccati activation).
But the peak value of 1.0 gives exponential enstrophy doubling time ≈ 0.5.

## What Route 2 DOES give:
- Enstrophy bounded exponentially: E(t) ≤ E₀ exp(2t)
- This is finite on any bounded interval (no blowup of L²)
- The ratio <α>/(||ω||∞·log(P/E)) ≈ 0.004 (tiny, slowly growing)
- This is the BKM logarithmic correction structure

## Route 3 HOLDS

The direct BKM measurement is INDEPENDENT of the energy analysis:
- γ = 1.08 (nearly linear ||ω||∞ growth)
- Hou-Li curvature positive at N=32, N=48, N=64
- Cross-validated across resolutions

Route 3 doesn't need <α> bounds. It directly measures ||ω||∞(t).

## The Three Routes — Final Assessment

| Route | TG | Trefoil | Formal proof? |
|-------|----|---------|----|
| 1 (Lagrangian) | ê·S²ê < 2α² everywhere ✓ | ê·S²ê > 2α² (fails) | Only for TG-like |
| 2 (Energy) | <α>_w = 0.03 ✓ | <α>_w = 1.0 (too large) | Log correction only |
| 3 (Direct BKM) | ||ω|| decreasing ✓ | γ=1.08, concave up ✓ | Numerics only |

## The Gap

No route gives a complete formal proof for ALL ICs.

Route 1 works for volume-filling flows but not localized.
Route 2 gives the right structure (BKM + log) but can't close the log gap.
Route 3 has the strongest numerics but no formal backing.

This is the SAME gap the field has had since BKM (1984):
**the logarithmic correction between enstrophy growth and L^∞ blowup.**

Our contribution: identifying the MECHANISM (self-depletion + pressure)
that keeps the gap open. The numerics strongly suggest regularity.
The formal proof awaits closing the log gap.

## 166 proof files.
