# NS Methodology Correction (Cycle Post-mortem)

## The Discrepancy

A late-finishing adversarial DE search (adversarial_S2e_directional.py) gave:
  N=3: 0.451  vs vertex method: 0.333 (proven 1/3 exactly)
  N=4: 0.465  vs vertex method: 0.362
  N=5: 0.422  vs vertex method: 0.333
  N=6: 0.508  vs vertex method: 0.316
  N=8: 0.482  vs vertex method: 0.280

The OLD method consistently reports HIGHER values.

## Root Cause

The OLD method computes S²ê/|ω|² at a LOCAL maximum of |ω|² found by
Nelder-Mead (8 random starts). When Nelder-Mead converges to a suboptimal
local max instead of the global max, |ω|² is artificially small, and the
ratio is inflated.

The DE optimizer then EXPLOITS this by finding polarization configs where
the gap between local and global is largest, producing apparent worst cases
that don't correspond to any actual vorticity maximum.

## The Correct Method

The VERTEX METHOD uses the proven vertex property (max |ω|² at c_i = ±1)
combined with EXHAUSTIVE enumeration of all 2^N sign patterns. This gives
the EXACT global vorticity max for each polarization configuration.

The vertex method's c(N) values are correct:
  c(2) = 1/4  (proven, Lean)
  c(3) = 1/3  (proven, Lean)
  c(4) ≈ 0.362
  c(N) decreases for N ≥ 5

## Implication

The Key Lemma bound c(N) < 3/4 holds with margin ≥ 52% for all tested N.
The old adversarial DE was a methodological artifact, not a counterexample.

The vertex property is the CORRECT tool for measuring c(N).
Future certificates should use vertex enumeration, not spatial optimization.
