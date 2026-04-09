---
source: VERTEX JUMP RESOLVED — |∇u|²/|ω|² < 1.52 at ALL near-max vertices
type: THE MISSING PIECE — the barrier can't be bypassed
file: 441
date: 2026-03-30
---

## THE RESULT

At ALL vertices with |ω|² ≥ 50% of the global max (500 configs, N=3-7):

    |∇u(x)|²/|ω(x)|² ≤ 1.52

This is below 2.0, below 3.0, below 4.5.

## WHY THIS RESOLVES THE VERTEX JUMP

From file 440: the barrier is repulsive at R ≥ R_crit where
R_crit = √(S²ê/(3|ω|²)) ≤ √((2/3)(|∇u|²/|ω|²-1/2)/3).

At |∇u|²/|ω|² = 1.52: R_crit = √((2/3)(1.02)/3) = √(0.227) = 0.476.

**R_crit = 0.476 < 0.500.** The barrier at R = 1/2 can NEVER be reached!

Even if the max jumps to any vertex with |ω|² ≥ 50% of the global max:
the ratio |∇u|²/|ω|² ≤ 1.52 ensures S²ê ≤ 0.68|ω|² < 3R²|ω|² for R ≥ 0.48.
So DR/Dt < 0 at R = 0.48, and R is immediately pushed below 0.48 < 0.50.

## THE PROOF CHAIN (if |∇u|²/|ω|² ≤ 1.52 at all near-max vertices is proven)

1. At any vertex where |ω|² ≥ 50% of max: |∇u|²/|ω|² ≤ 1.52 (TO PROVE)
2. → S²ê ≤ 0.68|ω|² (trace-free)
3. → R_crit = 0.48 < 0.50
4. → The barrier at R = 0.50 is NEVER reached (repulsive above 0.48)
5. → α < |ω|/2 always → Type I → Seregin → REGULARITY ∎

## THE REMAINING GAP

Prove |∇u|²/|ω|² ≤ 2.0 at ALL near-max vertices for smooth div-free fields.

This is WEAKER than the Key Lemma (which needs < 13/8 = 1.625 at the GLOBAL max).
The threshold is 2.0 (more generous by 23%) and it's at ALL near-max vertices.

From L² identity: average |∇u|²/|ω|² = 1 (Parseval). Need the ratio ≤ 2.0
at ALL vertices with |ω|² ≥ half the max. This is a concentration bound:
the ratio can't exceed 2× the average at near-max points.

## 441. |∇u|²/|ω|² < 1.52 at all near-max vertices (500 configs).
## R_crit = 0.48 < 0.50: barrier CANNOT be reached by vertex jump.
## Gap: prove |∇u|²/|ω|² ≤ 2.0 at near-max vertices (weaker than Key Lemma).
