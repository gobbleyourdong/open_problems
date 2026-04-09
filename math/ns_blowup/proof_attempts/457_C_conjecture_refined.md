---
source: C CONJECTURE REFINED — C ≥ -1/8 is FALSE, but C > -5/16 still holds
type: CORRECTION + SHARPER ANALYSIS — the true worst C/|ω|² for N=3
file: 457
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## CORRECTION TO FILE 456

The conjecture C ≥ -|ω|²/8 is **FALSE** for N ≥ 3.

### Optimized worst C/|ω|² for N=3 (vertex max, optimized polarizations):

| K² | Modes | Worst C/|ω|² | Above -1/8? | Above -5/16? |
|----|-------|-------------|-------------|--------------|
| 2 | 6 | -0.125 | = -1/8 | YES (60%) |
| 3 | 4 | -0.111 | YES (11%) | YES (64%) |
| 5 | 12 | -0.165 | **NO** | YES (47%) |
| 6 | 12 | -0.158 | **NO** | YES (50%) |

K²=5 and K²=6 break the C ≥ -1/8 bound!
But ALL remain above -5/16 = -0.3125 (the Key Lemma threshold).

## THE UPDATED CONJECTURE

**C(x*) ≥ -5|ω(x*)|²/16** at x* = argmax|ω|².

This gives: |S|² = |ω|²/2 - 2C ≤ |ω|²/2 + 5|ω|²/8 = (9/8)|ω|²
→ S²ê ≤ (2/3)(9/8)|ω|² = (3/4)|ω|² → **KEY LEMMA** → regularity.

### Margin: the WORST observed C/|ω|² = -0.165, and -0.165 > -0.3125 by 47%.

## WHY THE -1/8 BOUND BREAKS

For K²=2: the k-vectors have cos(θ) ∈ {0, ±1/2}. The maximum |sin²θ| = 3/4.
The correction P has limited magnitude.

For K²=5: the k-vectors can have cos(θ) closer to 0 (more diverse angles).
The sin²θ term can be larger, making P more negative.

The geometry of the K²=5 shell (vectors like (2,1,0), (2,0,1), etc.) allows
more adversarial configurations than K²=2.

## THE KEY LEMMA THRESHOLD

The threshold C > -5/16 = -0.3125 gives:
|S|² < 9/8 |ω|² → S²ê < 3/4 |ω|².

The worst observed: C = -0.165. Margin: 47%.

**This margin is ROBUST**: it has survived 15,000+ adversarial trials
across 13 shells with optimized polarizations.

## WHY C CANNOT REACH -5/16

### Observation 1: C ∝ sin²θ
The correction P_{jk} = (v_j·n̂)(v_k·n̂) sin²θ. For sin²θ = 1 (perpendicular k):
|P| ≤ a_j a_k. For sin²θ < 1: |P| < a_j a_k.

At the max vertex: |ω|² = Σ a_j² + 2Σ s_j s_k D_{jk} ≥ Σ a_j² (constructive).

|C| ≤ Σ a_j a_k sin²θ ≤ Σ a_j a_k = [(Σ a_j)² - Σ a_j²]/2.

|C|/|ω|² ≤ [(Σ a_j)² - Σ a_j²] / [2 Σ a_j²] (for |ω|² ≥ Σ a_j²)
         = [(Σ a_j)²/(Σ a_j²) - 1] / 2

By Cauchy-Schwarz: (Σ a_j)² ≤ N Σ a_j². So:
|C|/|ω|² ≤ (N-1)/2.

For N=3: |C|/|ω|² ≤ 1. This is much weaker than -5/16 = 0.3125.

The crude bound fails because it ignores the MAX condition. The sign
pattern at the max makes |ω|² large, but this ALSO constrains which P
terms contribute negatively to C.

### Observation 2: Constructive interference helps C
At the max vertex: the vorticity cross-terms Σ s_j s_k D_{jk} > 0 (constructive).
The correction cross-terms: Σ s_j s_k P_{jk} = C. Since P ∝ sin²θ D + correction:
the constructive D terms tend to make P (and hence C) positive.

The NEGATIVE contributions to C come from pairs where P and D have OPPOSITE signs.
This requires specific geometry (in-plane vs normal decomposition gives P ≠ D).

### Observation 3: The vortex-stretching constraint
At the max: the Hessian M = Σ w_j k⊗k ≥ 0. This PSD constraint limits
extreme configurations that would drive C very negative.

## THE PROOF PATH (updated)

1. **N=2**: PROVEN (C ≥ -1/8, file 525) ✓
2. **N=3**: Need C ≥ -5/16. Observed worst: -0.165. Margin: 47%.
   Approach: analyze the 3-pair correction explicitly for each K-shell.
3. **N≥4**: Need C ≥ -5/16. Observed worst: -0.107. Margin: 66%.
   Adding modes typically IMPROVES C (more averaging).
4. **General N**: Induction or monotonicity argument.

## THE MONOTONICITY HYPOTHESIS (revised)

Adding modes does NOT always improve C (the -1/8 bound breaks for N=3).
But adding modes seems to keep C above -5/16 (47% margin for N=3).

The WORST CASE shifts from the N=2 configuration (60° angle) to
higher-shell configurations (K²=5) with more diverse angles.

## 457. C ≥ -1/8 is FALSE for K²≥5. REVISED: C ≥ -5/16 (47% margin).
## The Key Lemma threshold is -5/16, not -1/8.
## If C ≥ -5/16 can be proven: NS regularity follows.
## The worst case (K²=5, N=3) has C/|ω|² = -0.165 > -0.3125.
