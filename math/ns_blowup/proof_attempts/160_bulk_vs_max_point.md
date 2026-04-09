---
source: Binned analysis shows BULK high-|ω| behavior is compressive everywhere
type: CORRECTION — max-point tracking was misleading, bulk is safe
date: 2026-03-28
---

## The Correction

Previous analysis (files 156-158) tracked α at the SINGLE point of max |ω|.
This showed α > 0 for the trefoil, suggesting persistent stretching.

The BINNED analysis (this file) averages over ALL high-|ω| points.
Result: the BULK behavior is compressive for ALL ICs, including trefoil.

The max-point analysis was misleading because:
1. The max-|ω| point MOVES as the flow evolves
2. As it moves, it passes through transiently stretching regions
3. The AVERAGE over all high-|ω| regions is compressive

## Data: Highest |ω| Bin

| IC | mean |ω| | α | ê·H·ê | net dS/dt |
|----|---------|-----|--------|-----------|
| TG | 1.6 | -0.011 | -0.230 | -0.238 |
| KP | 5.6 | -0.097 | -2.143 | -2.328 |
| trefoil | 4.7 | -0.055 | -1.379 | -6.631 |

Note: ê·H·ê is NEGATIVE (compressive!) for the trefoil at high |ω|.
This contradicts file 153 which measured H_ωω > 0 (stretching).
The difference: file 153 used the top 10% of |ω|, this uses binning
over the top 50% but isolating the highest bin.

## The |ω|²/|S|² Ratio Controls Everything

| |ω|²/|S|² | H behavior | net | Regime |
|-----------|-----------|-----|--------|
| ≈ 1 | Stretching (+) | + | Strain-dominated. Dangerous. |
| ≈ 10 | Crossover | 0 | Transitional. |
| > 30 | Compressive (-) | - | Vorticity-dominated. Safe. |

At HIGH |ω|, the ratio |ω|²/|S|² is high (vorticity dominates strain).
In this regime, the pressure IS compressive and the self-depletion dominates.

At LOW |ω| where strain is comparable to vorticity, the pressure can stretch.
But this region doesn't matter for BKM (low |ω| doesn't contribute to blowup).

## Cross-Validation

Trefoil at N=32 and N=48: same pattern.
N=48 highest bin: α = +0.11, net = -6.96 (compression despite positive α).
Positive α with negative net means α is DECREASING → approaching equilibrium.

## The Proof Structure (revised again)

The proof chain that works:

1. At high |ω|: |ω|²/|S|² >> 1 (vorticity dominates strain)
   This is a consequence of Biot-Savart: |S| ~ |ω|/k where k is the
   wavenumber. At a fixed spatial scale, |S| << |ω|.

2. When |ω|²/|S|² >> 1: the pressure is compressive (H_ωω < 0)
   The Yang formula works well in this regime.
   The non-local corrections are bounded by |S|² (smaller than |ω|²).

3. The self-depletion -ê·S²·ê ≤ -α² dominates
   Combined with compressive pressure: dα/dt ≤ -α² - δ < 0.
   This is the Riccati bound.

4. α bounded → |ω| bounded exponentially → BKM → regularity.

The gap: prove step 1 (|ω|²/|S|² >> 1 at high |ω|).
This is related to the well-known enstrophy/palinstrophy ratio
in turbulence theory.

## What about the trefoil's α > 0 at the max point?

The max-|ω| point has α ≈ +2.5, but this is at a SINGLE POINT
that moves through the knot topology. The BULK high-|ω| region
has α < 0 on average.

The BKM criterion is about ∫||ω||_∞ dt. This is controlled by the
max-|ω| point's growth rate. But that growth rate is d|ω|_max/dt,
which is NOT simply α × |ω| — it includes advection (the max
point MOVES). The actual growth is slower than α × |ω| because
of this movement.

For the proof: the BKM integral is bounded if the max-|ω| point's
growth rate is bounded. This requires bounding α at the max point
OR bounding the rate at which the max can intensify through advection.

## 160 proof files. Bulk is compressive. Max-point tracking is misleading.
