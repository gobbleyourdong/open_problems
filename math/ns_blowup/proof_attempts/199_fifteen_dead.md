---
source: 15th approach dead. Complete failure inventory.
type: STATUS — everything tried, the gap is sharp and narrow
date: 2026-03-29
---

## All 15 Approaches Tried

| # | Approach | How it died | File |
|---|----------|------------|------|
| 1 | Shell transfer Schur test | θ₀ = 2/3 insufficient | 113 |
| 2 | Spatial disjointness | IC-dependent | 124 |
| 3 | cos² ~ 1/|ω| decay | ODE artifact | 140 |
| 4 | c₂ ≤ c₁ ordering | Wrong assumption | 143 |
| 5 | Yang H_ωω < 0 | Non-local reverses sign | 153 |
| 6 | c₃ ≥ 1/3 universal | Trefoil counterexample | 156 |
| 7 | -Ω² dominates pressure | Fails for localized ω | 157 |
| 8 | Energy <α>_vol small | Wrong average | 166 |
| 9 | Riccati ODE alone | Blows up for any C > 0 | 167 |
| 10 | Concavity of 1/||ω|| | Not uniformly positive | 169 |
| 11 | Constantin-Fefferman | CF number grows for trefoil | 170 |
| 12 | Generic f ≥ 0 bound | 45% counterexample | 189 |
| 13 | Peak curvature → H_zz | μ_par << μ_perp | 197 |
| 14 | Kelvin + core width | Doesn't bound independently | 168 |
| 15 | Energy prevents concentration | Forward cascade breaks it | 198 |

## What SURVIVES (numerically confirmed, not proven)

- Q < 0 at the max after transient (100% compliance, file 192)
- |H_dev|/|H_iso| < 0.955 (36/36 measurements, Instance B)
- Hou-Li curvature positive at 3 resolutions (file 165)
- α ≤ 3 in approaching zone (80 measurements, file 175)
- ||ω||∞ grows sub-quadratically (γ = 1.08, file 162)
- D²α/Dt² < 2α³ between jumps (100%, file 193)

## The GAP (one sentence)

Prove that the 3D Euler dynamics on T³ maintain the quantity
Q = Dα/Dt + α² < 0 at vorticity maxima of smooth solutions.

This is a DYNAMIC STABILITY statement that requires the full
non-local pressure structure of the incompressible Euler equations.
It cannot be proven by:
- Static bounds on CZ operators (files 189-190)
- Local analysis at the max (files 196-197)
- Energy conservation alone (file 198)
- Alignment statistics alone (files 145-157)
- ODE models (file 167)

It CAN be confirmed numerically (100%, all ICs, all resolutions).
The Euler dynamics create non-local pressure correlations at
vorticity maxima that make Q < 0 — but PROVING this requires
understanding how the dynamics build these correlations.

## 199 proof files. The gap is clear. The proof awaits.
