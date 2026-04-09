---
source: CF criterion fails for trefoil. Kimi analysis confirms the gap.
type: ATTEMPT #12 dead. External validation of gap.
date: 2026-03-28
---

## Attempt #12: Constantin-Fefferman Direction Criterion

CF (1993): |∇(ω/|ω|)| ≤ C/|ω|^{1/2} → regularity.
CF number = |∇ξ| × |ω|^{1/2}.

| IC | CF(99%) | Trend | Status |
|----|---------|-------|--------|
| TG | 0.9→1.0 | Stable | WORKS |
| trefoil | 17→62 | Growing | **FAILS** |

The trefoil's vorticity direction becomes MORE singular at high |ω|.
CF criterion dead for localized structures.

## Kimi 2.5 Analysis (external validation)

Kimi correctly derives: f'' = (2α² - R)/||ω||∞

This connects the Hou-Li curvature to the Riccati residual R.
For f'' > 0 (regularity): need 2α² > R, i.e., α² > dα/dt.

Our data:
- α ≈ 2.5, so α² ≈ 6.25
- dα/dt ranges from -5 to +5 (fluctuates)
- α² > dα/dt holds MOST but not ALL of the time

Kimi correctly identifies the gap:
"Prove R = dα/dt + α² remains bounded for all time."

This is the SAME gap we identified in files 167-169.

## Complete Scoreboard: 12 approaches

| # | Approach | Dead? | Reason |
|---|----------|-------|--------|
| 1 | Shell transfer | Yes | θ insufficient |
| 2 | Spatial disjointness | Yes | IC-dependent |
| 3 | cos² decay | Yes | ODE artifact |
| 4 | c₂ ordering | Yes | Wrong assumption |
| 5 | Yang pressure sign | Yes | Non-local reverses |
| 6 | c₃ ≥ 1/3 universal | Yes | Trefoil |
| 7 | -Ω² dominance | Yes | Localized ω |
| 8 | Energy <α>_vol | Yes | Wrong average |
| 9 | Riccati ODE alone | Yes | Blows up for any C |
| 10 | Migration effect | Insufficient | Only 12% |
| 11 | Concavity uniform | Yes | g'' negative 18% |
| 12 | Constantin-Fefferman | Yes | CF grows for trefoil |

## The ONE thing that works: Hou-Li (averaged)

The averaged curvature IS positive. All three resolutions.
The instantaneous curvature oscillates but the mean is positive.

The proof needs: averaged curvature bounds → pointwise bounds.
This is the Millennium Prize gap.

Kimi's reformulation: d²/dt²(log ||ω||∞) ≤ C.
This is equivalent to: ||ω||∞ grows at most exponentially.
Which is equivalent to BKM regularity.

## 170 files. 12 dead approaches. 1 average bound that works.
