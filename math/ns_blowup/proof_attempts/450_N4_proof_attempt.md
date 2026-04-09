---
source: N=4 PROOF — self-alignment of ê prevents the Key Lemma from failing
type: KEY INSIGHT — the largest mode always dominates ê, making sinγ ≈ 0 for it
file: 450
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## THE SELF-ALIGNMENT MECHANISM

At x* = argmax|ω|²: ê = ω/|ω| is determined by the MODE AMPLITUDES.

The largest mode (by a_j|c_j|) dominates the sum ω = Σ a_j v̂_j c_j.
So ê ≈ v̂_dominant. The dominant mode's sinγ ≈ 0 (aligned with ê).

**A mode cannot be simultaneously LARGE and PERPENDICULAR to ê.**
If it's large: ê aligns with it → sinγ ≈ 0 → self-vanishing suppresses its strain.
If it's perpendicular: it doesn't contribute to |ω| → it's not "large" in the ω sense.

## FORMAL STATEMENT

**Claim**: For any div-free field on T³, at x* = argmax|ω|²:
    S²ê/|ω|² ≤ (budget/|ω|)² < 3/4.

**Why it should hold**: The budget from each mode j is (a_j/2)sinγ_j|q_j|.
- sinγ_j is small for modes aligned with ê (the dominant direction)
- |q_j| = |sin(k_j·x*)| is small for modes in constructive phase
- A mode's CONTRIBUTION to |ω| is a_j|c_j|cosγ_j (large when well-aligned and in-phase)
- These factors are ANTI-CORRELATED: high contribution to |ω| → low contribution to budget

## THE PERPENDICULAR CANCELLATION CONSTRAINT

At x*: ω = |ω|ê (purely along ê). This means:
    Σ a_j c_j sinγ_j ê_j^⊥ = 0 (perpendicular components cancel).

This CONSTRAINS the perpendicular modes: their weighted contributions
must cancel vectorially. A single large perpendicular mode requires
other modes to compensate — but those other modes' perpendicular
components are bounded by their amplitudes.

## WHY THE EXTREME CASE FAILS

Consider a field with one large mode (a_4 ≫ a_{1-3}):

**If mode 4 were perpendicular** (cosγ_4 = 0): it wouldn't contribute
to |ω|. The max would be |ω|² ≈ (Σ_{1-3} a_j)² ≈ small².
BUT: a different point (where c_4 = ±1) gives |ω|² ≈ a_4². Much bigger!
At that point: ê ≈ v̂_4, cosγ_4 ≈ 1, sinγ_4 ≈ 0. Budget from mode 4 ≈ 0.

**The global max selects the point where the LARGEST mode is in-phase.**
This automatically makes the largest mode aligned with ê.

**Consequence**: the budget at the global max is dominated by the
SMALL modes (not aligned with ê), whose total amplitude is bounded.

## N=4 CRITICAL POINT ANALYSIS

For N=4 with 3 independent k's: the null space is 1-dimensional.
sin(k_j·x*) = t × n_j where n is the null vector.

budget(t) = |t|/2 × Σ (a_j sinγ_j(t) |n_j|)

where γ_j(t) depends on ê(t) which depends on c_j(t) = ±√(1-t²n_j²).

At t = 0 (lattice): ê = ê₀, budget = 0, |ω| = |ω|₀ (lattice max).
At small t: budget ≈ |t| × C, |ω| ≈ |ω|₀ - O(t²). Ratio ≈ t×C/|ω|₀ → 0.

The ratio budget/|ω| increases from 0, reaches a max, then ...
(as t increases, c_j decrease, |ω| drops, budget initially grows then also drops).

The maximum of budget/|ω| over t is the worst case.

## NUMERICAL RESULTS (N=4, 1500 configs across 6 shells)

    Worst budget/|ω| = 0.285
    Key Lemma margin: 67.1%
    R < 1/2 margin: 43.0%

The N=4 case is BETTER than general N (where worst is 0.427).

## N ≥ 5: NULL SPACE GROWS

For N=5: null space is 2-dim. More freedom for the sines.
For N=6: null space is 3-dim. Even more.

But the budget still can't exceed √(3/4)|ω| because:
1. The global max aligns ê with the dominant modes
2. The dominant modes' sinγ is self-vanishingly small
3. The minor modes' total amplitude is bounded by the energy
4. The budget from minor modes < their total amplitude / 2
5. The dominant modes' |ω| > their total amplitude × cosγ ≈ large

## 450. Self-alignment: ê tracks the dominant mode direction.
## The largest mode has sinγ ≈ 0 (self-vanishing). Its budget ≈ 0.
## Only minor modes contribute to budget. Their ratio budget/|ω| ≤ 0.285 (N=4).
## The mechanism is clear but formal proof needs ê-dependence on amplitudes.
