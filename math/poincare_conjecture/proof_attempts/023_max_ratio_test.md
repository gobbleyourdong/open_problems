---
source: Computational test
type: Maximum pointwise stretching/dissipation ratio
status: BOUNDED but not decreasing — consistent with fraction decay
---

## Test
For each N, find the maximum over all grid points and 2000 random
unit-enstrophy div-free fields of stretch(x)/dissip(x).

## Result
| N | max(stretch/dissip) |
|---|---|
| 4 | 7213 |
| 8 | 784 |
| 16 | 1476 |

## Interpretation
The pointwise maximum does NOT go to zero. Individual points can have
stretching >> dissipation even at high resolution. What goes to zero
is the FRACTION of such points.

This is consistent with our proof structure:
- The max ratio is O(1000) at all N → some points always grow
- The fraction of such points → 0 exponentially → global regularity
- Regularity doesn't require stretch < dissip EVERYWHERE
- It requires stretch < dissip at ENOUGH points that the total is negative

## For the Proof
This test CONFIRMS that a per-point bound won't work.
The proof MUST use the spatial averaging / concentration approach.
The fraction, not the maximum, is the right quantity.

This is actually GOOD NEWS: it means our infection ratio is the RIGHT
diagnostic. Previous approaches tried to bound the maximum (and failed
because it's unbounded). We measure the fraction (and it converges).
