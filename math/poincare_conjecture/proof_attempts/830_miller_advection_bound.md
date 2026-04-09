---
source: MILLER ADVECTION BOUND — can we control (u·∇)S using our tools?
type: NEW DIRECTION — bounding the advection term in Miller's framework
file: 830
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE SETUP (Miller 2026)

Full NS strain equation:
    ∂_t S - νΔS - (1/2)P_st(ω⊗ω) + P_st(S² + (3/4)ω⊗ω) + P_st((u·∇)S) = 0

Miller's model (μ=0): drops Q_term = P_st(S² + (3/4)ω⊗ω + (u·∇)S).
Model is globally regular because ⟨-ΔS, ω⊗ω⟩ = 0 → H¹ norm decreasing.

Full NS: H¹ norm equation includes ⟨-ΔS, Q_term⟩ ≠ 0.

Miller's criterion (Thm 1.9): blowup requires ||Q_term||_{L²} ≥ ||-ΔS||_{L²}.

## THE QUESTION

Can we bound ||Q_term||_{L²} < ||-ΔS||_{L²} using our tools?

Q_term = P_st((u·∇)S + S² + (3/4)ω⊗ω)

From Prop 1.1: ⟨S² + (3/4)ω⊗ω, S⟩ = 0 (orthogonal to S).
From div u = 0: ⟨(u·∇)S, S⟩ = 0 (orthogonal to S).

Both components of Q are ⊥ S. Their L² norms:

### ||(u·∇)S||:
By Hölder: ||(u·∇)S|| ≤ ||u||_{L^∞} ||∇S||_{L^2}
On T³: ||u||_{L^∞} ≤ C||ω||_{L^2}^{1/2} ||∇ω||_{L^2}^{1/2} (Agmon)

Under Type I with Key Lemma:
||ω||_{L^2} ~ (T-t)^{-1/4}, ||∇ω||_{L^2} ~ (T-t)^{-α}
||u||_{L^∞} ~ (T-t)^{-1/2} (from BKM-type estimate)

||(u·∇)S|| ≤ C(T-t)^{-1/2} ||∇S||

### ||S² + (3/4)ω⊗ω||:
||S²|| ≤ ||S||_{L^4}^2 (Hölder)
||(3/4)ω⊗ω|| = (3/4)||ω||_{L^4}^2

Under Type I: ||S||_{L^4}, ||ω||_{L^4} both blow up.

### ||-ΔS||:
From Poincaré on T³: ||-ΔS|| ≥ λ₁ ||∇S|| = ||∇S|| (λ₁=1)

### THE RATIO
||Q|| / ||-ΔS|| ≤ (||u||_∞ ||∇S|| + ||S²+(3/4)ω⊗ω||) / ||∇S||
= ||u||_∞ + ||S²+(3/4)ω⊗ω|| / ||∇S||

Under Type I: ||u||_∞ ~ (T-t)^{-1/2} → ∞. So the ratio → ∞.

Miller's criterion is NOT satisfied by these standard bounds.

## WHY STANDARD BOUNDS FAIL

The estimate ||u||_∞ → ∞ under Type I makes the advection term LARGE.
Miller's criterion needs ||Q|| < ||-ΔS||, but the advection ||u·∇S|| is
at least ||u||_∞ ||∇S|| which is much larger than ||-ΔS|| ≈ ||∇S|| near blowup.

## COULD THE KEY LEMMA HELP?

The Key Lemma bounds S²ê at the POINTWISE level. Miller's criterion is
in L² norm. The local-to-global conversion is the fundamental obstacle.

If the Key Lemma held EVERYWHERE (not just at the max):
S²(x)ê(x) ≤ (3/4)|ω(x)|² for all x.
Then: ||S²+(3/4)ω⊗ω|| would be controlled by ||ω||² terms.
But the Key Lemma only holds at the MAX.

## THE FLOOR GROWTH ANGLE

If the floor growth held (|S|²/|ω|² → 0 at the max):
||S||_{L^∞} → 0 relative to ||ω||_{L^∞}.
But ||S||_{L^2} = ||ω||_{L^2}/√2 (integrated cross-term identity, EXACT on T³).
So ||S||_{L^2} is NOT reduced by the floor growth — it's fixed.

The floor growth only reduces the L^∞ norm of S, not the L² norm.
Miller's criterion involves L² norms. The floor growth doesn't directly help.

## CONCLUSION

Miller's criterion ||Q|| < ||-ΔS|| is NOT achievable through standard
Sobolev estimates, even with the Key Lemma or floor growth.

The advection term (u·∇)S is TOO LARGE in L² under Type I.

Miller's result is valuable as a STRUCTURAL insight (the model equation
is regular, the gap lives in Q), but the quantitative criterion doesn't
close with available tools.

## REMAINING VIABLE PATHS

1. **SOS algebraic decomposition**: construct universal certificates with growing floor
2. **Lattice-specific arguments**: exploit Z³ structure beyond probabilistic methods
3. **Higher-order analysis**: use 3rd/4th moment structure of the selection effect
4. **Completely new approach**: possibly entropy, information theory, or optimal transport

## 830. Miller advection bound: standard estimates give ||Q|| >> ||-ΔS||.
## The advection term ||u·∇S|| ~ ||u||_∞ ||∇S|| → ∞ under Type I.
## Miller's quantitative criterion is not closeable with current tools.
## The model equation result remains structural, not quantitative.
