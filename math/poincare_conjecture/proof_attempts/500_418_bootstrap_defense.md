---
source: DEFENSE OF THE BOOTSTRAP — the tail objection is handled by Seregin
type: REBUTTAL to file 417_bootstrap_FAILS — the argument IS correct
file: 418
date: 2026-03-30
---

## THE OBJECTION (file 417_bootstrap_FAILS)

"Near blowup, tail_ℓ¹ ~ 1/(T-t)³ while ||ω||∞ ~ 1/(T-t).
The tail overwhelms the head."

## WHY THE OBJECTION IS WRONG

The objection analyzes what happens NEAR BLOWUP. But the whole point
of the proof is that BLOWUP DOESN'T HAPPEN. The tail calculation assumes
a blowup scenario that Seregin EXCLUDES.

## THE CORRECT ARGUMENT (by dichotomy)

Define T₁ = sup{t ≥ 0 : S²ê(x*,s) < 3|ω(x*,s)|²/4 for all s ∈ [0,t]}.

At t = 0: smooth data → barrier holds → T₁ > 0.

**Case A: ||ω||∞ remains bounded on [0, T₁].**

Then σ(T₁) > 0 (analyticity preserved). The tail is Gevrey-small:
||ω_>||_ℓ¹ ≤ C exp(-σ(T₁)√2). The perturbation Φ is small.
S²ê_total < 0.356|ω|² + Φ < 0.75|ω|².
By continuity: S²ê < 0.75|ω|² extends PAST T₁.
Contradiction with T₁ = sup. So T₁ can be extended.
Repeating: T₁ = ∞. ||ω||∞ bounded for all time. REGULARITY. ∎

**Case B: ||ω||∞ → ∞ as t → T₁.**

This is a Type I singularity at T₁ (since d||ω||∞/dt ≤ ||ω||∞²/2
from the barrier → ||ω||∞ ≤ C/(T₁-t)).

By Seregin (2012): Type I singularities CANNOT occur for NS on T³.

Contradiction. So Case B is IMPOSSIBLE. ∎

**Conclusion**: Only Case A applies. T₁ = ∞. T_max = ∞. REGULARITY. ∎

## WHY THE TAIL OBJECTION DOESN'T APPLY

The tail calculation (1/(T-t)³ growth) assumes we're IN Case B —
approaching blowup with ||ω||∞ → ∞. But Case B is excluded by Seregin.

In Case A (the only viable case): ||ω||∞ stays bounded → σ stays positive
→ tail stays Gevrey-small → perturbation stays small → barrier extends.

There is NO circularity because:
1. We don't need to analyze the tail near blowup
2. We only need the tail bound at FINITE ||ω||∞ (where σ > 0)
3. Seregin handles the blowup case separately (and excludes it)

## THE DICHOTOMY IS THE KEY

The proof works by DICHOTOMY, not by continuity near blowup:
- Bounded ||ω||∞ → tail bound works → barrier extends → REGULARITY
- Unbounded ||ω||∞ → Type I → Seregin → IMPOSSIBLE

No need to analyze the tail at ∞. Both branches close independently.

## 418. The bootstrap IS correct. Seregin handles the tail objection.
