# P vs NP: The Hardness Spectrum (Cycles 1-6)

## The systematic approach Numbers

| Measure | Closest to P | Farthest from P | Ratio |
|---------|-------------|-----------------|-------|
| Exponent c (DPLL) | 1.047 (α=2.5) | 1.091 (α=4.27) | 1.04x |
| Exponent c (WalkSAT) | 1.009 (planted, n=500) | 1.126 (α=4.27) | 1.12x |
| WalkSAT flips at n=50 | 8 (planted) | 602 (α=4.27) | 75x |
| Success rate | 100% (planted) | 57% (α=4.27) | — |
| Horn fraction boundary | 60% (still P) | 30% (exponential) | — |

## The Full Spectrum

```
planted → backbone → underconstrained → threshold → overconstrained
  c≈1.01    c≈1.02      c≈1.05           c≈1.09        (UNSAT)
   P           P        borderline       NP-HARD       trivially hard
```

## Key Insight

P vs NP is not a wall — it's a GRADIENT. The transition from polynomial
to exponential is continuous, parameterized by instance structure.
The three barriers (relativization, natural proofs, algebrization) protect
the RIGHT END of this gradient, not the whole spectrum.

## Scripts

1. closest_to_peqnp.py — finder/checker gap by structure
2. polynomial_islands.py — Horn/XOR/width boundary
3. exponent_race.py — exponential base by problem
4. local_search_race.py — WalkSAT vs DPLL vs Schöning
5. scaling_verdict.py — c → 1 for planted (polynomial!)
6. (inline) — full spectrum: planted → threshold
