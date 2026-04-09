---
source: ANTI-CORRELATION PROOF — the ω-weight is inversely related to strain factor
type: PROOF PATH — the Chebyshev mechanism for closing the gap
file: 521
date: 2026-03-30
instance: CLAUDE_OPUS
---

## THE DECOMPOSITION

At x* = argmax|ω|²:

    budget/|ω| = Σⱼ wⱼ × fⱼ

where:
  wⱼ = aⱼ|cⱼ|cosγⱼ / |ω|   (normalized vorticity weight, Σ ≈ 1)
  fⱼ = (tanγⱼ × |tanφⱼ|)/2  (per-mode strain-to-vorticity ratio)
  cⱼ = cos(kⱼ·x*), qⱼ = sin(kⱼ·x*), γⱼ = angle(v̂ⱼ, ê)

**Need**: Σ wⱼ fⱼ < √(3/4) ≈ 0.866

## THE ANTI-CORRELATION

The weights wⱼ and factors fⱼ are ANTI-CORRELATED:

**Large wⱼ** (dominant modes, large a × |c| × cosγ):
  → cosγ ≈ 1 → tanγ ≈ 0 → fⱼ ≈ 0
  → |c| ≈ 1 → |tanφ| ≈ 0 → fⱼ ≈ 0

**Large fⱼ** (high strain-to-vorticity ratio):
  → tanγ large → cosγ small → wⱼ small (less aligned)
  → |tanφ| large → |c| small → wⱼ small (less in phase)

**This is a double anti-correlation**: both factors in fⱼ (tanγ and |tanφ|)
are inversely related to the corresponding factors in wⱼ (cosγ and |c|).

## THE AM-GM BOUND

For each mode: wⱼ × fⱼ = [aⱼ|cⱼ|cosγⱼ/|ω|] × [(sinγⱼ|qⱼ|)/(2|cⱼ|cosγⱼ)]
= (aⱼ sinγⱼ |qⱼ|) / (2|ω|)

So: budget/|ω| = Σ (aⱼ sinγⱼ |qⱼ|)/(2|ω|) = budget/|ω| [tautology!]

The decomposition doesn't help directly because it's an identity.

## THE CAUCHY-SCHWARZ APPROACH

budget² = (Σ (aⱼ/2) sinγⱼ |qⱼ|)²

By Cauchy-Schwarz with weights aⱼ|cⱼ|cosγⱼ (= |ω| × wⱼ):
(Σ uⱼ vⱼ)² ≤ (Σ uⱼ²/αⱼ)(Σ αⱼ vⱼ²)

Choose uⱼ = (aⱼ/2) sinγⱼ |qⱼ| and αⱼ = aⱼ |cⱼ| cosγⱼ:

budget² ≤ [Σ (aⱼ² sin²γⱼ qⱼ²)/(4aⱼ|cⱼ|cosγⱼ)] × [Σ aⱼ|cⱼ|cosγⱼ]
= [Σ (aⱼ sin²γⱼ qⱼ²)/(4|cⱼ|cosγⱼ)] × |ω|

So: budget²/|ω|² ≤ [Σ (aⱼ sin²γⱼ qⱼ²)/(4|cⱼ|cosγⱼ)] / |ω|

Hmm, the bracketed term can be large when |cⱼ| or cosγⱼ is small.

## THE PER-MODE BOUND

For each mode at the max: define rⱼ = sin²γⱼ × qⱼ²/(|cⱼ|² cos²γⱼ)
= tan²γⱼ × tan²φⱼ (the squared per-mode ratio).

Then: budget/|ω| = Σ wⱼ × √(rⱼ)/2

By Jensen's (with convex √): Σ wⱼ √rⱼ ≤ √(Σ wⱼ rⱼ)... NO, Jensen gives
Σ wⱼ √rⱼ ≤ √(Σ wⱼ rⱼ) only for concave √. √ IS concave. So:

budget/|ω| = (1/2) Σ wⱼ √rⱼ ≤ (1/2) √(Σ wⱼ rⱼ) [Jensen]

So: need Σ wⱼ rⱼ < 3 (since (1/2)√3 = √(3/4) = 0.866).

Σ wⱼ rⱼ = Σ [aⱼ|cⱼ|cosγⱼ/|ω|] × [tan²γⱼ tan²φⱼ]
= Σ [aⱼ sin²γⱼ qⱼ²] / [|ω| |cⱼ| cosγⱼ]

This is worse than before (can blow up when cosγ or |c| → 0).

## THE HESSIAN CONSTRAINT

At the max: the Hessian trace gives |∇ω|² ≤ K²|ω|² (single shell).

|∇ω|² includes terms like Σ aⱼ² |kⱼ|² qⱼ² = K² Σ aⱼ² qⱼ² (diagonal).

If cross terms ≥ 0: Σ aⱼ² qⱼ² ≤ |ω|².

Then: budget² ≤ (1/4)(Σ aⱼ² sin²γⱼ)(Σ qⱼ²) by standard CS.
And: Σ aⱼ² sin²γⱼ ≤ Σ aⱼ².
And: Σ qⱼ² = N - Σ cⱼ².

From Σ aⱼ² qⱼ² ≤ |ω|² and qⱼ² ≤ 1:
Σ qⱼ² = Σ qⱼ²(aⱼ²/aⱼ²) ≤ (1/min aⱼ²) Σ aⱼ² qⱼ² ≤ |ω|²/min aⱼ²

This depends on the amplitude ratio, not useful in general.

## THE CORRECT APPROACH (sketch)

The budget is bounded by the PRODUCT of two independent "smallness" measures.

Define: P = Σ aⱼ² qⱼ² (the "sine energy")
        Q = Σ aⱼ² sin²γⱼ (the "misalignment energy")

From Hessian: P ≤ |ω|² (on single shell, if cross terms help).
From self-vanishing: Q ≤ Σ aⱼ² = 2E (total mode energy).
From Parseval: E = ||ω||₂²/(2×vol(T³)).

Budget² ≤ (1/4) Q × (P/min(aⱼ²))... still amplitude-dependent.

## NUMERICAL STATE

| Metric | Worst | Threshold | Margin |
|--------|-------|-----------|--------|
| budget/|ω| | 0.489 | 0.866 | 43.5% |
| weighted avg of f | 0.463 | 0.866 | 46.5% |
| S²ê/|ω|² | 0.091 | 0.750 | 87.9% |

The 43% margin in budget/|ω| is the TIGHTEST bound we can hope to prove.
It's equivalent to S²ê/|ω|² ≤ 0.24 (since budget²/|ω|² ≤ 0.24).

## 521. Anti-correlation: ω-weight × strain-factor inversely related.
## Jensen + CS give partial bounds but blow up when cosγ or |c| → 0.
## The Hessian gives Σ a²q² ≤ |ω|² but coupling to sin²γ is the gap.
## Numerically: budget/|ω| < 0.49 (43% margin). Robust but unproven.
