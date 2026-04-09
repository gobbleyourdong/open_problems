---
source: TRUNCATION WORSENS — attempting to prove adding modes helps
type: PROOF ATTEMPT — the most promising remaining path
file: 435
date: 2026-03-30
---

## THE CLAIM (from Instance B, file 508)

Removing a mode from a field INCREASES S²ê/|ω|² at the global max
(62% of cases). The K=√2 shell (finite modes) is the worst case.

## WHY IT SHOULD BE TRUE

Each mode k contributes:
1. To |ω|² (denominator): a_k cos γ_k component along ê (ADDS to |ω|)
2. To S·ê (numerator): |ŝ_k| = (a_k/2)sin γ_k (ADDS to strain)
3. Self-cancellation: S_k·v̂_k = 0 (mode k's strain CANCELS part of others)

Effect 1 (denominator boost) typically DOMINATES effects 2+3:
- The mode is AT THE GLOBAL MAX → it adds constructively to |ω|
- The sign-flip constraint a_k ≤ |ω|cos γ_k means the parallel
  component (effect 1) is BOUNDED ABOVE the perpendicular (effect 2)
- The self-cancellation (effect 3) REDUCES the numerator

## WHY THE PROOF IS HARD

Per-mode: removing mode k changes the global max vertex (vertex jump).
The new max might have DIFFERENT sign pattern → different S²ê.

The 36% of cases where truncation HELPS: these are cases where the
removed mode's cross-term contributions were NEGATIVE (reducing S·ê).
Removing it lets the remaining modes' S·ê add more constructively.

## THE AVERAGED VERSION (easier to prove)

Instead of per-mode monotonicity: prove the SUPREMUM over all configs
decreases with N.

sup_{N modes} S²ê/|ω|² ≥ sup_{N+1 modes} S²ê/|ω|²

From the data:
N=3: sup ≈ 0.32, N=4: sup ≈ 0.32, N=5: sup ≈ 0.28, N=9: sup ≈ 0.15

This holds numerically. But proving it requires showing that the
EXTREMAL (worst) N+1 mode config has lower ratio than the worst N-mode.

## 435. Truncation-worsening is the path. Proof needs supremum monotonicity.
