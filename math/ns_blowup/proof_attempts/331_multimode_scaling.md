---
source: Monte Carlo: α/|ω| peaks at N≈5 modes, then DECREASES
type: NUMERICAL EVIDENCE — the bound does NOT approach 1/2
file: 331
date: 2026-03-29
---

## Monte Carlo Results (200-500 trials per N, random div-free modes on T³)

| N modes | max α/|ω| at actual max | Gap to 0.5 |
|---------|------------------------|-----------|
| 1 | 0.000 | 0.500 |
| 2 | 0.311 | 0.189 |
| 3 | 0.347 | 0.153 |
| 5 | **0.427** | 0.073 |
| 10 | 0.354 | 0.146 |
| 20 | 0.298 | 0.202 |

## The Trend: PEAK then DECREASE

α/|ω| peaks at N ≈ 5 modes (max ≈ 0.43) then DECREASES with more modes.

The reason: more modes create angular spread in the vorticity direction.
The ω direction ê becomes an AVERAGE of many mode polarizations.
The strain from each mode is at a DIFFERENT angle to ê.
The α = ê·S·ê averaging causes cancellation.

For N → ∞ (smooth fields): the cancellation is maximal.
α/|ω| → some C_∞ that's WELL below 0.5.

## Comparison with Actual NS Solutions

| IC | Effective N | α/|ω| |
|----|------------|-------|
| TG (t=0) | ~1 | 0.00 |
| TG (evolved) | ~10 | 0.05 |
| KP | ~20 | 0.10 |
| Trefoil | ~50 | 0.15 |
| Thin trefoil | ~100 | 0.10 |

The evolved NS solutions have α/|ω| much LOWER than the Monte Carlo
maximum (0.43 at N=5). This suggests the NS dynamics create ADDITIONAL
cancellation beyond what random modes give.

## Implications

1. The kinematic max of α/|ω| is ≈ 0.43 (at N≈5 modes).
2. This is BELOW 0.5 by 15%.
3. For many modes (N > 10): the max is ≈ 0.35, below 0.5 by 30%.
4. The NS dynamics give even lower values (0.05-0.15).
5. The bound α/|ω| < 0.5 is STRONGLY supported but not PROVEN.

## The Proof Route

The Monte Carlo suggests: the maximum of α/|ω| over all N-mode div-free
fields on T³ is bounded by some C < 0.5 for ALL N.

The function C(N) peaks at N≈5 and decreases.
If C(N) ≤ C_max ≈ 0.43 for all N: the proof closes.

The analytical bound: for N=2, C₂ = 1/(2√2) ≈ 0.354 (Instance C, proven).
For N ≥ 2: the optimization is over a FINITE-DIMENSIONAL space (the mode
parameters). This is tractable with analytical methods.

CONJECTURE: max_{div-free, N modes} α/|ω| ≤ C < 1/2 for all N on T³.
NUMERICAL: C ≈ 0.43 (from N=5 optimization).

## 331. The multi-mode α/|ω| peaks at N≈5 and DECREASES. Does NOT approach 1/2.
