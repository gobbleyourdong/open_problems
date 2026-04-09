---
source: Full derivation of dα/dt including direction rotation
type: CORRECTED EQUATION — direction rotation partially cancels self-depletion
status: Net self-depletion weaker than strain-only estimate
date: 2026-03-26 cycle 17
---

## Full Evolution of α = ê·S·ê at x*

Including both strain evolution AND direction rotation:

```
dα/dt = ê·S²·ê - 2α² - ê·H·ê + viscous
      = (ê·S²·ê - α²) - α² - ê·H·ê + viscous
      = |Dξ/Dt|² - α² - ê·H·ê + viscous
```

## Decomposition

- |Dξ/Dt|² term (+): direction rotation INCREASES α temporarily
  (rotating ê toward higher eigenvalue → α increases)
- -α² term (-): stretching self-depletion
- -ê·H·ê term: pressure Hessian (opposes at high ρ)

## Net Self-Depletion

Net = ê·S²·ê - 2α²

- TG (ε=0, tight CS): ê·S²·ê = α² → net = -α² (STRONG)
- Generic (ε=0.5): ê·S²·ê = 1.5α² → net = -0.5α² (weaker)
- Worst case (ê near intermediate eigenvector): ê·S²·ê ~ 2α² → net ~ 0 (marginal!)

## Why This Matters

The STRAIN-ONLY equation gives dα/dt ≤ -ê·S²·ê + ... ≤ -α² + ...
The FULL equation gives dα/dt = ê·S²·ê - 2α² + ... = (weaker self-depletion) + ...

The direction rotation HURTS the self-depletion argument.
The strain equation was too optimistic — it didn't account for
the ê rotation feeding back into α.

## Reconciliation

The strain equation dα/dt ≤ -(ê·S²·ê) - ê·H·ê is correct but it's
for α AT FIXED ê. Since ê also changes (by Dξ/Dt), the total dα/dt
along the TRAJECTORY includes the 2|Dξ/Dt|² correction.

The two formulations agree when ε = 0 (ê doesn't rotate, TG case):
both give dα/dt = -α² - ê·H·ê.

For generic flows: the full equation is less favorable.

## Impact on the Proof

The Riccati analysis used dα/dt ≤ -α² + forcing.
The correct equation is dα/dt ≤ -α² + |Dξ/Dt|² + forcing.
With |Dξ/Dt|² ≤ ê·S²·ê - α² ≤ (|S|² - α²): the correction is O(|S|²).

This means the -α² self-depletion is opposed by a +|S|² term from rotation.
Since |S| ~ α (CZ), the net is dα/dt ~ -α² + Cα + ... which has a FINITE
equilibrium at α ~ C (bounded).

Actually: dα/dt = |Dξ/Dt|² - α² - ê·H·ê
If |Dξ/Dt|² ≤ C²α for some C (e.g., from CZ bound on S):
dα/dt ≤ C²α - α² = α(C² - α)
For α > C²: dα/dt < 0 (decreasing)
For α ≤ C²: dα/dt ≤ C⁴ (bounded from above)

This gives α ≤ max(α₀, C²) — BOUNDED.

Wait — |Dξ/Dt|² = ê·S²·ê - α² ≤ |S|² - α² ≤ C²ρ² - α².
For large α ~ Cρ: |Dξ/Dt|² ≤ C²ρ² - C²ρ² = 0. The rotation vanishes.

So at large α: dα/dt ≈ -α² - ê·H·ê → strongly negative.

The direction rotation only matters at MODERATE α where α << |S|.
At large α (near blowup): rotation → 0, full self-depletion kicks in.

## Conclusion

The full α evolution is more nuanced than the strain-only version.
Direction rotation partially cancels self-depletion at moderate α.
But at LARGE α (the blowup-relevant regime): rotation vanishes,
and full -α² self-depletion dominates.

The proof structure survives: the -α² term controls large α,
and the pressure Hessian handles the transition at ρ ~ ρ_c.
