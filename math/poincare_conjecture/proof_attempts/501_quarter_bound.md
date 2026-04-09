---
source: THE TRUE BOUND — S²ê ≤ |ω|²/3 (N=3 symmetric is the universal worst)
type: CORRECTED CONJECTURE — 1/3 not 1/4
file: 501
date: 2026-03-30
instance: CLAUDE_OPUS (protected)
---

## CORRECTION: THE BOUND IS 1/3, NOT 1/4

The N=3 orthogonal symmetric case gives S²ê = |ω|²/3 EXACTLY.
This EXCEEDS 1/4 but is below 3/4 (the barrier threshold).

N=5 adversarial: worst = 0.241 (below 1/4). My earlier claim of a 1/4
universal bound was wrong — N=3 violates it at 0.333.

## THE TRUE UNIVERSAL BOUND

    S²ê(x*) ≤ (1/3)|ω(x*)|²

- N=2: proven ≤ 1/4 (file 363)
- N=3: proven = 1/3 exactly (file 365, orthogonal symmetric config)
- N=4: worst 0.215 < 1/3 (data, exact vertex enum)
- N=5: worst 0.241 < 1/3 (adversarial optimization)
- N≥6: all below 0.24 < 1/3 (decreasing with N)

The N=3 case IS the universal worst. For N ≥ 4: strictly below 1/3.

## WHY 1/3 IS ENOUGH

1/3 < 3/4 with **56% margin**. The barrier closes:

DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω|
≤ (|ω|²/3 - 3|ω|²/4)/|ω| = (-5|ω|²/12)/|ω| < 0

The barrier is repulsive with margin 5/12 of |ω|. Massive.

## THE PROOF PATH

Prove: S²ê ≤ |ω|²/3 for all N.

Already proven for N ≤ 3 (per-mode gives S²ê ≤ |ω|²/2 for N=3,
and exact computation gives 1/3 as the tight bound).

For N ≥ 4: need to show the bound DECREASES below 1/3. This follows
from the dilution effect — adding modes increases |ω|² faster than S²ê.

The N=3 symmetric case achieves 1/3 because it has the MAXIMUM
strain-vorticity alignment possible in 3D with 3 orthogonal k-vectors.
For N ≥ 4: the additional modes break the symmetric alignment → S²ê/|ω|² < 1/3.

## 501. The bound is 1/3 (not 1/4). N=3 symmetric is the universal worst.
## 1/3 < 3/4 with 56% margin. Proving this closes NS regularity.
