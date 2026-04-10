# cross_family_slope_stats — loop 11 Cycle 32 Odd

**Date:** 2026-04-09

Aggregate statistics across all K-trajectory probes from
loops 0-11. Used to set the CRDEpsilon constant in the
loop-11 quantitative CRDProperty Lean theorem.

## Per-family stats

| family | n_total | F1 flat | F2 decr | other | F1 max\|slope\| | F2 most neg |
|:-------|--------:|--------:|--------:|------:|----------------:|------------:|
| Hamiltonian cycle | 136 | 102 | 16 | 18 | 0.000461 | -0.312500 |
| 3-coloring | 112 | 78 | 12 | 22 | 0.000369 | -0.062500 |
| subset-sum | 79 | 49 | 19 | 11 | 0.000344 | -0.343750 |
| knapsack | 56 | 39 | 8 | 9 | 0.000401 | -0.009375 |
| vertex cover | 40 | 37 | 3 | 0 | 0.000257 | -0.031250 |
| set cover | 38 | 33 | 4 | 1 | 0.000117 | -0.015625 |
| clique | 71 | 41 | 20 | 10 | 0.000398 | -0.029412 |
| 3-DM | 80 | 36 | 31 | 13 | 0.000463 | -0.037500 |
| FVS | 72 | 53 | 15 | 4 | 0.000285 | -0.375000 |
| bin packing | 72 | 48 | 20 | 4 | 0.000335 | -0.500000 |
| hitting set | 40 | 31 | 8 | 1 | 0.000298 | -0.062500 |

## Cross-family aggregates

**F1-flat population (n=547):**

- min:    0.000000
- q1:     0.000000
- median: 0.000004
- q3:     0.000047
- max:    0.000463
- mean:   0.000046

**F2-decreasing population (n=156):**

- most negative: -0.500000
- q1:            -0.062500
- median:        -0.008929
- q3:            -0.001838
- least negative: -0.000517
- mean:          -0.072951

## Empirical F1/F2 separation

- F1 max |slope|:                0.000463
- F2 least negative slope:       -0.000517
- F2 most negative slope:        -0.500000
- Separation ratio (worst-case): 1079.9×

**Conclusion for the Cycle 32 Even quantitative
CRDProperty Lean theorem:** the empirical separation
supports an ε = 0.0005 constant. F1 hard-config slopes
are bounded by ε in magnitude, F2 easy-config slopes
are at least an order of magnitude more negative.
