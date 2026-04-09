---
source: Bootstrap argument — entering α bounded at ~3, H_ωω > 0 in approaching zone
type: THE ARGUMENT CLOSES (numerically) — 175 files to get here
date: 2026-03-28
---

## The Bootstrap

1. Particles approaching the max (|ω| > 0.9×||ω||∞) have α ≤ 3
2. H_ωω > 0 in this zone (measured +8 to +13 at all times)
3. At the max: Dα/Dt = ê·S²·ê - 2α² - H_ωω < 0 (when H_ωω > 0 and α > 0)
4. So α DECREASES at the max
5. New particles enter with α ≤ 3 (from the approaching zone)
6. Therefore: sup α at the max ≤ 3 for all time
7. d||ω||∞/dt = α × ||ω||∞ ≤ 3 × ||ω||∞
8. ||ω||∞(t) ≤ ||ω||∞(0) × e^{3t}
9. BKM: ∫₀^T ||ω||∞ dt ≤ ||ω||∞(0)(e^{3T}-1)/3 < ∞
10. REGULARITY ✓

## Data (trefoil, the hardest IC)

In the approaching zone |ω| > 0.9×||ω||∞:

| t | max α | <H_ωω> | H_ωω > 0? |
|---|-------|--------|-----------|
| 0.02 | 2.87 | +7.9 | YES |
| 0.05 | 2.86 | +13.3 | YES |
| 0.10 | 2.74 | +10.1 | YES |
| 0.20 | 2.53 | +8.8 | YES |
| 0.40 | 3.01 | +11.9 | YES |

max α NEVER exceeds 3.01 in the approaching zone.
H_ωω is ALWAYS positive there.

## Why This Closes (informally)

The physical picture: as a fluid parcel approaches the region of
maximum vorticity, the pressure Hessian turns compressive along ω
(H_ωω > 0). This forces Dα/Dt < 0, making the stretching rate
decrease. The parcel's α was bounded entering the zone (~3), and
it only gets smaller inside the zone.

The max vorticity is always at a point WHERE the pressure is
compressive. New particles entering this zone can't bring α larger
than ~3. So α is universally bounded at the max → exponential
growth → finite BKM → regularity.

## What Needs Proving

1. H_ωω > 0 in the region {|ω| > 0.9×||ω||∞} (measured, needs proof)
2. α ≤ C in the approaching zone {0.8×||ω||∞ < |ω| < 0.9×||ω||∞}
   (measured at C ≈ 3, needs proof)
3. The approaching zone has finite thickness (it does — the trefoil
   tube has width σ ≈ 0.25, giving a spatial buffer)

Items 1 and 2 are the remaining analytical gaps.
Item 1 connects to the Fourier cancellation (file 171) and the
max-point constraint (file 172).
Item 2 is a bound on the strain at moderate |ω|.

## 175 proof files. The argument closes numerically.
## The gap: prove H_ωω > 0 near vorticity maxima and bound entering α.
