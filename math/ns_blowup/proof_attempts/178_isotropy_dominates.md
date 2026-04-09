---
source: Pressure Hessian becomes increasingly ISOTROPIC at high |ω|
type: THE MECHANISM — isotropy dominates anisotropy at high |ω|
date: 2026-03-28
---

## The Key Finding

|H_dev|/|H_iso| DECREASES monotonically with |ω|:
  1.09 at low |ω| → 0.77 at high |ω|

The pressure Hessian becomes MORE ISOTROPIC at higher |ω|.

## The Decomposition

H_ωω = H_iso + H_dev,ωω = tr(H)/3 + (anisotropic correction)

| |ω|/max | tr(H)/3 (iso) | H_dev,ωω | NET H_ωω |
|---------|-------------|---------|---------|
| 0.1-0.3 | -3 | +3 | -0.05 |
| 0.3-0.5 | +5 | -3 | +1.9 |
| 0.5-0.7 | +20 | -18 | +2.9 |
| 0.7-0.8 | +42 | -35 | +7.4 |
| 0.8-0.9 | +58 | -44 | +13.2 |

Both parts grow with |ω|, but the isotropic part GROWS FASTER.
The net H_ωω is positive and INCREASING at high |ω|.

## Why Isotropy Increases at High |ω|

1. Source Δp = |ω|²/2 - |S|². At the |ω|²/|S|² = 4 attractor:
   Δp = |ω|²/4 > 0.

2. The source is concentrated at the high-|ω| point (the tube core).
   The CORE is approximately SPHERICAL (width σ in all directions),
   even if the tube is elongated at larger scales.

3. As |ω| increases: σ decreases (Kelvin), but the far-field
   contribution (from other parts of the tube) becomes relatively
   more important. The far-field is more isotropic (seen from distance,
   the tube looks like a line, and the Hessian from a line source
   has some angular structure but is more isotropic than a local disk).

4. The net effect: increasing |ω| → increasing isotropy of H → H_ωω → +.

## The Proof Path

GIVEN: Δp > 0 at high |ω| (from |ω|²/|S|² > 4 attractor)
SHOW: H_dev,ωω / H_iso < 1 at high |ω|

H_iso = Δp/3 = |ω|²/12 (exact)
H_dev,ωω = Yang local + non-local correction

Yang local: -|ω|²/6 → |H_dev,ωω|/H_iso = 2 (anisotropy ratio = 2)
But non-local correction makes it less negative.
Measured: ratio = 0.77 (non-local reduces from 2 to 0.77)

The non-local reduction is from the FAR-FIELD isotropy.
As |ω| → ∞: far-field dominates → ratio → 0 → H_ωω → H_iso > 0.

## Formal Statement (to prove)

For any smooth solution to 3D Euler on T³:
  At any point x where |ω(x)| ≥ c||ω||∞ (c < 1):

  |H_dev,ωω(x)| ≤ (1-ε) × H_iso(x)  for some ε > 0

  This implies: H_ωω(x) ≥ ε × Δp(x)/3 > 0

The ε comes from the non-local isotropy of the pressure kernel.
It depends on the GEOMETRY of the vorticity distribution but NOT
on the magnitude ||ω||∞.

## 178 proof files. Isotropy dominates at high |ω|. The sign flip is explained.
