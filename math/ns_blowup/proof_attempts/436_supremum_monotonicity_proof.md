---
source: SUPREMUM MONOTONICITY PROOF ATTEMPT — formalizing file 509's sketch
type: THE CRITICAL PROOF — if this closes, regularity follows
file: 436
date: 2026-03-30
---

## THE CLAIM

For N ≥ 5 modes at the global max of |ω| on T³:

    sup_{N+1 modes} S²ê/|ω|² ≤ sup_{N modes} S²ê/|ω|²

Combined with N ≤ 4 (proven S²ê < 3|ω|²/4) and N=5-9 K-shell (certified
< 0.367): the supremum is at N=3-4 (≤ 1/3), giving regularity.

## THE PROOF

Consider an (N+1)-mode field at its global max x*. Remove one mode (say
mode N+1) to get an N-mode sub-field.

**At the SAME point x***: the N-mode sub-field has:
- |ω_N|² = |ω_{N+1}|² - 2a_{N+1}s_{N+1}(ê·v̂_{N+1})|ω| - a_{N+1}² + ...
  Actually: |ω_N|² = |ω_{N+1} - s_{N+1}a_{N+1}v̂_{N+1}|²

PROBLEM: x* is the global max of the (N+1)-mode field, NOT of the N-mode
sub-field. The N-mode sub-field might have its max elsewhere.

**At the N-mode's own max**: the ratio could be higher or lower.

This is the VERTEX JUMP problem (file 374). The sub-field's max is at a
DIFFERENT vertex, where the ratio could be anything.

## THE FIX: bound the ratio at ALL vertices, not just the max

**Step 1**: At the (N+1)-mode global max x* with sign pattern s*:

S²ê_{N+1} = |Σ_{k=1}^{N+1} ŝ_k|²
|ω_{N+1}|² = |Σ s*_k a_k v̂_k|²

**Step 2**: The (N+1)-th mode's contribution splits:

S·ê = S_rest·ê + S_{N+1}·ê
|ω| = |ω_rest + s*_{N+1} a_{N+1} v̂_{N+1}|

**Step 3**: From self-vanishing (S_{N+1}·v̂_{N+1} = 0):

S_{N+1}·ê = S_{N+1}·(ê - (ê·v̂_{N+1})v̂_{N+1}) = S_{N+1}·ê_⊥^{N+1}

|S_{N+1}·ê| ≤ (a_{N+1}/2)|sinγ_{N+1}| (per-mode bound)

**Step 4**: The sign-flip constraint: a_{N+1} ≤ |ω|cosγ_{N+1}

So: |S_{N+1}·ê| ≤ (|ω|cosγ/2)sinγ = (|ω|/4)sin2γ ≤ |ω|/4

**Step 5**: The DENOMINATOR gain from mode N+1:

At the global max: p_{N+1} = a_{N+1}cosγ_{N+1} contributes to |ω|.
Since Σp_k = |ω|: removing mode N+1 reduces |ω| by p_{N+1}.

|ω_rest| = |ω| - p_{N+1} (approximately, exact for the ê-component)

**Step 6**: The RATIO change:

R_{N+1} = S²ê_{N+1}/|ω_{N+1}|² = |S_rest·ê + S_{N+1}·ê|²/|ω|²

R_rest at x* = |S_rest·ê|²/|ω_rest|² (but this is NOT at the N-mode max)

The N-mode max might give a HIGHER ratio. This is where the proof breaks.

## THE FUNDAMENTAL OBSTACLE

The ratio at the sub-field's OWN max could be higher than at x*.
Removing mode N+1 changes the max location (vertex jump).
At the new max: the ratio is unconstrained by the (N+1)-mode analysis.

## WHAT WORKS: the K-SHELL SUPREMUM ARGUMENT

Instead of per-mode monotonicity: use the K-shell certification.

For the K=√2 shell (9 modes): the worst ratio across ALL N=2-9 is 0.367.
This is CERTIFIED (file 434, all angles, DE global optimization).

For any smooth field: the Fourier modes with |k|² ≤ 2 form a SUB-FIELD.
At the full field's max: the sub-field ratio is ≤ 0.367 (certified).

The question: does the FULL field's ratio exceed the sub-field's ratio?

From file 508 (truncation worsens): removing modes (going from full to
sub-field) INCREASES the ratio 62% of the time. This means: the full
field typically has LOWER ratio than the sub-field.

But: 38% of the time, truncation HELPS (ratio decreases). So the full
field CAN have higher ratio than the sub-field for specific configs.

## STATUS

The supremum monotonicity is OBSERVED but NOT PROVEN. The vertex jump
prevents a clean per-mode argument. The truncation principle (62/38 split)
is not 100%.

The proof remains open.

## 436. Supremum monotonicity attempt. Fails due to vertex jump.
## The K-shell is certified but can't formally extend to all fields.
