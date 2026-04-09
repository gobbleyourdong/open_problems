# T-Sign Verification at Vertex Maxima

## For Even Instance (ExistingChainConnection.lean)

The T ≤ 0 hypothesis does NOT hold pointwise at all worst cases.
Specifically: the N=4 worst case has T > 0.

## Measured T values

T_{jl} = c_j c_l (k_j · v_l)(v_j · k_l), summed j < l.

### Trial statistics (30 random k-tuples per N)

| N | mean T | T ≤ 0 | T > 0 | Range |
|---|--------|-------|-------|-------|
| 3 | +0.04 | 17/30 | 13/30 | [-2.47, +3.41] |
| 4 | -0.51 | 16/30 | 14/30 | [-3.88, +4.01] |
| 5 | -1.06 | 20/30 | 10/30 | [-5.02, +4.00] |
| 6 | -0.05 | 17/30 | 13/30 | [-3.36, +4.51] |
| 8 | +0.82 | 9/30  | 21/30 | [-1.99, +6.26] |

**T > 0 is common.** The "T ≤ 0 pointwise" hypothesis fails.

### Specific N=4 worst case

k = {[-1,0,0], [-1,1,1], [1,0,1], [1,1,1]}
Optimal signs: (1, -1, -1, 1) (note: different from (1,1,-1,1) for other sign
                                conventions; flipping signs gives same |ω|²)
|ω|² = 5.2207
S²ê/|ω|² = 0.3616

T_{jl} breakdown at this vertex:
  T_{1,2} = +0.907  (k_1·v_2 × v_1·k_2)
  T_{1,3} = +0.494
  T_{1,4} = -0.747
  T_{2,3} = -0.325
  T_{2,4} = +2.170  ← dominant positive term
  T_{3,4} = -0.525
  
  T_total = +1.972 > 0 ✗

## Implication for ExistingChainConnection.lean

The chain as written (Stage 3 requires T ≤ 0) cannot be directly activated.
Three paths forward:

1. **Find a different hypothesis that DOES hold at the worst case.** Maybe
   |T| ≤ some_bound suffices instead of T ≤ 0. The chain would need to be
   re-derived: Q_cross = 10K - 26T ≥ 0 requires K ≥ 2.6T. For T_max = 1.97
   at N=4, need K ≥ 5.12 there. Measure K at the worst case.

2. **Average-T approach**: show that Σ T_{jl} weighted by some probability
   is ≤ 0 overall, activating a weaker form of the chain.

3. **Skip the T path entirely**: use the direct eigenvalue approach
   (Tier 3 Item 6 data: λ₁²/||S||²_F = 0.525, well below 2/3).

## Also from the data

- Middle eigenvalue alignment: a₂² ≈ 0 at the N=4 worst case
  (the vorticity is perpendicular to the middle eigenvector)
- Extreme eigenvalues contribute nearly equally: a₁² = 0.46, a₃² = 0.53
- TraceFreeAlignment bound (λ₁² ≤ (2/3)||S||²_F) has 35% slack at worst case
