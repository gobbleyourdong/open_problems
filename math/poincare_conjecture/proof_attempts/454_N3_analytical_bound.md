---
source: N=3 ANALYTICAL BOUND — proving C > -5|ω|²/16 for 3-mode fields
type: PROOF ATTEMPT — explicit algebraic analysis of the 3-pair correction
file: 454
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## SETUP

3 modes on T³ with k₁, k₂, k₃ (integer, linearly independent).
Amplitudes a₁, a₂, a₃. Polarizations v̂₁, v̂₂, v̂₃ (each ⊥ respective k).

At the GLOBAL MAX vertex: signs s_j = ±1 chosen to maximize |ω|².

|ω|² = Σ a_j² + 2(s₁s₂ D₁₂ + s₁s₃ D₁₃ + s₂s₃ D₂₃)
C = s₁s₂ P₁₂ + s₁s₃ P₁₃ + s₂s₃ P₂₃

where D_{jk} = v_j · v_k and P_{jk} = (v_j·n̂_{jk})(v_k·n̂_{jk}) sin²θ_{jk}.

## THE RELATIONSHIP BETWEEN P AND D

From the cross-term identity (file 511):
2 Tr(S_j S_k) = D_{jk} - 2P_{jk}

So: P_{jk} = (D_{jk} - 2 Tr(S_j S_k)) / 2 = D_{jk}/2 - Tr(S_j S_k).

And: C = Σ P_{jk} s_j s_k = Σ [D_{jk}/2 - Tr(S_j S_k)] s_j s_k
       = (1/2) Σ D_{jk} s_j s_k - Σ Tr(S_j S_k) s_j s_k.

Now: Σ D s_j s_k = (|ω|² - Σ a²)/2 (the cross-term part of |ω|²).

And: |S|² = Σ |S_j|² + 2Σ Tr(S_j S_k) s_j s_k = Σ a²/2 + 2Σ Tr(S_j S_k) s_j s_k.

So: Σ Tr(S_j S_k) s_j s_k = (|S|² - Σ a²/2) / 2.

Therefore: C = (|ω|² - Σ a²)/4 - (|S|² - Σ a²/2)/2
             = |ω|²/4 - Σa²/4 - |S|²/2 + Σa²/4
             = |ω|²/4 - |S|²/2

Wait: that gives |S|² = |ω|²/2 - 2C. Substituting C = |ω|²/4 - |S|²/2:
|S|² = |ω|²/2 - 2(|ω|²/4 - |S|²/2) = |ω|²/2 - |ω|²/2 + |S|². ✓ (tautology)

So the derivation is consistent but doesn't give new information.

## NUMERICAL DATA FOR N=3

| Shell K² | Worst C/|ω|² | Worst |S|²/|ω|² | Worst S²ê/|ω|² |
|----------|-------------|----------------|----------------|
| 2 | -0.046 | 0.592 | 0.173 |
| 5 | -0.066 | 0.632 | 0.078 |
| 9 | -0.072 | 0.644 | 0.173 |
| 11 | -0.098 | 0.697 | 0.077 |

**ALL below the threshold -5/16 = -0.3125 by 68%+ margin.**

The worst case (K²=11): C/|ω|² = -0.098. The threshold is -0.3125.
Even 3× this worst case would pass: 3 × 0.098 = 0.294 < 0.3125. ✓

## THE BOUND ON C FOR N=3

C = Σ P_{jk} s_j s_k.

Each |P_{jk}| ≤ |v_j||v_k| sin²θ (since |v·n̂| ≤ |v|).

So: |C| ≤ Σ a_j a_k sin²θ_{jk}.

And: |ω|² ≥ (max_j a_j)² (the global max is at least one mode's contribution).

For equal amplitudes (a_j = a): |C| ≤ 3a² × max(sin²θ) ≤ 3a².
And |ω|² ≥ a² (at least). Often |ω|² ≈ 9a² (all constructive).

C/|ω|² ≥ -3a²/a² = -3 (too loose!).
C/|ω|² ≥ -3a²/(9a²) = -1/3 (if constructive, still > -5/16? No, -1/3 = -0.333 < -0.3125).

So the crude bound |C|/|ω|² ≤ Σ sin²θ / N fails when sin²θ is large
and modes are constructive.

## THE KEY: CONSTRUCTIVE INTERFERENCE WEAKENS |P|

At the global max: the signs s_j are chosen for |ω|² maximal.
The D_{jk} cross-terms are POSITIVE (constructive): s_j s_k D_{jk} > 0.

Now P = (v·n̂)(v·n̂)sin²θ. For the SAME sign pattern that makes D positive:
what sign does P have?

From: P = (v_j·n̂)(v_k·n̂) sin²θ.

The sign of P depends on whether (v_j·n̂) and (v_k·n̂) have the same sign.
This is a geometric property: do v_j and v_k project onto the same side
of the k-plane normal?

For constructive interference (D = v_j·v_k > 0): v_j and v_k point
in similar directions. Their projections onto n̂ tend to have the SAME SIGN.
So P tends to be POSITIVE at constructive vertices.

**When P > 0: it ADDS to C (makes C more positive = better for Key Lemma).**

The worst case: P < 0 at the constructive vertex. This happens when v_j, v_k
are similar (D > 0) but their n̂-projections have opposite signs.

This requires specific geometry: v's similar but on opposite sides of the k-plane.

## TOWARD A PROOF

For each pair (j,k): P_{jk} and D_{jk} are related through the geometry.

Decompose: v_j = (v_j·n̂)n̂ + v_j^∥ (normal + in-plane components).
D_{jk} = (v_j·n̂)(v_k·n̂) + v_j^∥ · v_k^∥.
P_{jk} = (v_j·n̂)(v_k·n̂) sin²θ.

So: P_{jk} = sin²θ × [D_{jk} - v_j^∥ · v_k^∥].

At a constructive vertex (s_j s_k = sgn(D)):
s_j s_k P = |D - v^∥·v^∥| sin²θ × sgn(D-v^∥·v^∥) × sgn(D)... complex.

Simpler: P = sin²θ D - sin²θ (v^∥ · v^∥).

The first term: sin²θ D has the SAME SIGN as D (positive at constructive vertex).
The second term: -sin²θ (v^∥ · v^∥). The sign depends on v^∥ · v^∥.

For the in-plane dot product: v^∥ · v^∥ = v_j^∥ · v_k^∥. This can be positive
or negative depending on the in-plane orientations.

If v^∥ · v^∥ < 0: the second term is positive → P > sin²θ D > 0. Good!
If v^∥ · v^∥ > D: the second term dominates → P < 0. Bad.

v^∥ · v^∥ > D requires |v^∥ · v^∥| > |D|. Since D = (v·n̂)² + v^∥·v^∥:
v^∥·v^∥ > (v·n̂)² + v^∥·v^∥ → 0 > (v·n̂)² → impossible.

Wait: D = v_j·v_k = (v_j·n̂)(v_k·n̂) + v_j^∥·v_k^∥. So:
P = sin²θ [(v_j·n̂)(v_k·n̂) + v_j^∥·v_k^∥] - sin²θ v_j^∥·v_k^∥
  = sin²θ (v_j·n̂)(v_k·n̂).

That's circular — P IS sin²θ (v·n̂)(v·n̂) by definition.

So: P = sin²θ (v_j·n̂)(v_k·n̂) = sin²θ [D - v^∥·v^∥]. And:
D - v^∥·v^∥ = (v·n̂)·(v·n̂) = P/sin²θ.

The sign of P = sign of (v_j·n̂)(v_k·n̂). This is positive when both
projections have the same sign, negative otherwise.

For the WORST CASE: P negative and constructive (D positive).
Need: (v_j·n̂)(v_k·n̂) < 0 AND v_j·v_k > 0.
This means: v_j and v_k are similar overall but project onto opposite
sides of the k-plane normal.

The maximum |P| with P < 0 and D > 0:
|P| = sin²θ |(v·n̂)(v·n̂)|. And D = (v·n̂)² + v^∥·v^∥ > 0.
With (v·n̂) have opposite signs and D > 0: v^∥·v^∥ > (v·n̂)² (in-plane
dominates over normal).

## STATUS

The N=3 case has 68% margin. The algebraic analysis shows P and D
are related through geometric projections. For the worst case:
P can be negative at constructive vertices, but bounded by sin²θ × a_j a_k.

The proof needs: at the GLOBAL MAX vertex, |Σ P s_j s_k| < 5|ω|²/16.

This is a CONSTRAINED optimization: signs s_j maximize |ω|² (which involves D),
and we need C = Σ P s_j s_k > -5|ω|²/16.

## 454. N=3 analysis: worst C/|ω|² = -0.098 (margin 68.5%).
## P and D related through normal/in-plane decomposition.
## P < 0 at constructive vertex when normal projections oppose.
## Proof needs: bound the negative P at the argmax vertex.
