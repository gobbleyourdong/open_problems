---
source: MONOTONICITY STATUS — per-config FALSE, universal likely TRUE
type: KEY FINDING for the proof architecture
file: 544
date: 2026-03-31
instance: CLAUDE_OPUS (500s)
---

## PER-CONFIG MONOTONICITY: FALSE

Adding a 5th mode to a given N=4 config can make C/|ω|² MORE negative:
- 6/15 configs improved when adding optimal 5th mode
- Max worsening: 0.045 (from -0.115 to -0.148)

So proving "adding a mode helps" per-config is IMPOSSIBLE.

## UNIVERSAL MONOTONICITY: LIKELY TRUE

The UNIVERSAL worst (over all configs) improves:

| N | Universal worst C/|ω|² | Source |
|---|----------------------|--------|
| 2 | -0.125 | Proven |
| 3 | -0.172 (exact -11/64) | Verified |
| **4** | **-0.172** | **Definitive (50 seeds)** |
| 5 | -0.157 | Adversarial search |
| 6 | -0.095 | Search |
| 7 | -0.095 | Search |

worst(N=5) = -0.157 > worst(N=4) = -0.172 ✓

**But proving this analytically is hard because per-config monotonicity fails.**

## THE WORST N=4 CONFIG IS SPECIAL

Adding ANY 5th mode to the worst N=4 config IMPROVES it:
- 74 possible 5th modes tested (all |k|² ≤ 6)
- ALL 74 improve the worst C/|ω|²
- Best improvement: -0.172 → -0.167 (2.8% better)

The worst N=4 config is an ISOLATED extremum that CANNOT be extended
to a worse N=5 config by adding any mode. This is a structural property
of the specific k-vector geometry [(-2,-2,0), (-2,-1,0), (-2,0,-1), (0,-1,0)].

## IMPLICATIONS FOR THE PROOF

### Option A: Prove universal monotonicity for N ≥ 5
Show worst(N+1) ≤ worst(N) for the universal worst (not per-config).
HARD: per-config fails, so the argument must be about the EXTREMAL config.

### Option B: Finite certification for N ≤ 5
Certify all N ≤ 5 configs on K² ≤ K_max. For N=5: 40⁵ = 102M points
per config. Very expensive but feasible.

### Option C: Prove worst is at N = 3-4
Show that N ≤ 4 is always the worst (the universal worst stabilizes).
Combined with N ≤ 4 certification: completes the proof.

### Option D: Computational proof for ALL N ≤ N_max
Certify all N-tuples with N ≤ N_max on K² ≤ K²_max.
For N_max = 4, K²_max = 25: ~50K configs × grid. ~days.
For N ≥ 5: use search evidence + spectral tail.

## 544. Per-config monotonicity FALSE. Universal likely TRUE.
## The worst N=4 config cannot be extended to worse N=5.
## Proof options: finite N≤4 cert + N≥5 argument, OR full cert.
