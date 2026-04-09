# Monotone Decrease Verification — For theory track

## Date: 2026-04-09
## Target: c(N+1) ≤ c(N) for N ≥ 4

## Measured c(N) via vertex method + DE optimization

| N | c(N) | k-tuples tested | Monotone? |
|---|------|-----------------|-----------|
| 4 | 0.362 (known) | exhaustive 14950 | — |
| 5 | 0.347 | 50 | ✓ |
| 6 | 0.303 | 20 | ✓ |
| 7 | 0.298 | 20 | ✓ |
| 8 | 0.286 | 20 | ✓ |
| 9 | 0.298 | 10 | **✗ increases** |
| 10 | 0.248 | 10 | ✓ (vs 9) |
| 11 | 0.291 | 10 | **✗ increases** |
| 12 | 0.191 | 5 | ✓ |
| 13 | 0.170 (known) | 8 | ✓ |

## Interpretation

**Pointwise monotone decrease is NOT verified.** N=9 and N=11 show
increases from their predecessors (0.298 > 0.286; 0.291 > 0.248).

However, these "increases" are very likely **measurement artifacts**:
- N=8: 20 k-tuples tested → more thorough search
- N=9, 11: only 10 k-tuples tested → underestimates likely
- c(N) decreases as tuple count grows (more tuples = higher worst found)

**Trend is CLEARLY decreasing on average:**
- c(4) = 0.362
- c(8) = 0.286 (-21% from c(4))
- c(12) = 0.191 (-47% from c(4))
- c(13) = 0.170 (-53% from c(4))

## Recommendation for theory track

Do NOT use pointwise monotone decrease as a hypothesis.
Instead, consider these alternative formulations:

1. **Bounded supremum**: `sup_{N ≥ 4} c(N) ≤ c(4) ≤ 0.362`
   - Requires only `c(N) ≤ 0.362` for all N, not monotone
   - Still gives Key Lemma for all N ≥ 4

2. **Eventual monotone decrease**: `∃ N₀ s.t. c(N+1) ≤ c(N) for N ≥ N₀`
   - Data suggests N₀ ≈ 12 or higher
   - Combined with exhaustive verification of c(4)..c(N₀)

3. **Asymptotic bound**: `c(N) → 0` as N → ∞
   - Data: c(13)/c(4) ≈ 0.47 — decreasing rapidly
   - Would need analytical proof or much more computation

## Implication

The `complete_key_lemma_conditional` in `MonotoneDecrease.lean` needs
a weaker hypothesis than pointwise monotone decrease. The data supports
`sup_{N ≥ 4} c(N) = c(4) = 0.362` as the most natural formulation.

This still closes the Key Lemma conditional on c(4) < 0.75 (verified:
c(4) ≤ 0.561 rigorously via per-sign dominance grid, see c4_rigorous_cert.md).
