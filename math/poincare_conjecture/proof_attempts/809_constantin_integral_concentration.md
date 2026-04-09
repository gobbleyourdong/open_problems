---
source: CONSTANTIN INTEGRAL + CONCENTRATION — does vorticity concentration deplete α?
type: ANALYSIS — the most precise picture of the gap yet
file: 809
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE INTEGRAL REPRESENTATION (Constantin 1994)

At any point x where |ω(x)| > 0:

    α(x) = (3/4π) P.V. ∫ D(ŷ, ξ(x+y), ξ(x)) |ω(x+y)| dy/|y|³

where:
- ŷ = y/|y| is the direction from x to x+y
- ξ = ω/|ω| is the vorticity direction
- D(e₁,e₂,e₃) = (e₁·e₃) Det(e₁,e₂,e₃) is the geometric kernel
- |D| ≤ |sin φ| where φ is the angle between ξ(x+y) and ξ(x)

## SELF-VANISHING AT y = 0

At y = 0: ξ(x+y) = ξ(x), so Det(ŷ, ξ(x), ξ(x)) = 0. The kernel D
vanishes when two of the three vectors coincide.

This is EXACTLY our self-vanishing identity |S_k·ê|² = (a²/4)sin²γ
from the Fourier representation — in the integral form.

For small |y|: D ~ |y| · |∇ξ(x)| (Taylor expand ξ(x+y) ≈ ξ(x) + y·∇ξ).
The singularity 1/|y|³ is softened to 1/|y|² by the self-vanishing.

## DECOMPOSITION AT THE VORTICITY MAXIMUM x*

Split α(x*) into near-field and far-field at scale ℓ:

    α = α_near + α_far

    α_near = (3/4π) P.V. ∫_{|y|≤ℓ} D · |ω(x*+y)|/|y|³ dy
    α_far = (3/4π) ∫_{|y|>ℓ} D · |ω(x*+y)|/|y|³ dy

### Near-field (|y| ≤ ℓ):

Using D ~ |y| · |∇ξ| and |ω(x*+y)| ≤ ||ω||∞:

    |α_near| ≲ ||ω||∞ · |∇ξ(x*)| · ∫_0^ℓ r · r²/r³ dr = ||ω||∞ · |∇ξ| · ℓ

### Far-field (|y| > ℓ):

Using |D| ≤ 1 and Cauchy-Schwarz on T³:

    |α_far| ≲ ||ω||_{L²} · (∫_{|y|>ℓ} 1/|y|⁶ dy)^{1/2} = C · ||ω||_{L²}/ℓ^{3/2}

### Optimization:

    |α| ≲ ||ω||∞ · |∇ξ| · ℓ + C||ω||_{L²}/ℓ^{3/2}

Minimize over ℓ → optimal ℓ ~ (||ω||_{L²}/(||ω||∞ · |∇ξ|))^{2/5}:

    |α|_opt ≲ C · ||ω||∞^{3/5} · |∇ξ|^{3/5} · ||ω||_{L²}^{2/5}

## TYPE I SCALING ANALYSIS

Near Type I blowup at T*:
- ||ω||∞ ~ C₀/(T*-t)
- ||ω||_{L²} ~ Ω^{1/2} ~ (T*-t)^{-1/4} (parabolic concentration)
- |∇ξ| ~ 1/√(T*-t) (Type I spatial gradients)

Substituting:
    |α| ≲ C · (T*-t)^{-3/5} · (T*-t)^{-3/10} · (T*-t)^{-1/10}
        = C · (T*-t)^{-3/5 - 3/10 - 1/10}
        = C · (T*-t)^{-1}

So |α| ~ ||ω||∞. THE CONCENTRATION EFFECT IS EXACTLY BALANCED BY THE
DIRECTION GRADIENT GROWTH. Type I is the CRITICAL SCALING.

## THE RATIO α/||ω||∞

    α/||ω||∞ ~ C · |∇ξ|^{3/5} · (||ω||_{L²}/||ω||∞)^{2/5}

For Type I: ||ω||_{L²}/||ω||∞ ~ (T*-t)^{-1/4}/(T*-t)^{-1} = (T*-t)^{3/4}

So: α/||ω||∞ ~ (T*-t)^{-3/10} · (T*-t)^{3/10} = 1

EXACTLY ONE. The ratio α/||ω||∞ stays constant near Type I blowup.
This is why Type I is the borderline case.

## WHAT WOULD GIVE SUBLINEAR α

For α = o(||ω||∞), we need α/||ω||∞ → 0 as T*-t → 0. This requires:

    |∇ξ|^{3/5} · (||ω||_{L²}/||ω||∞)^{2/5} → 0

This happens if EITHER:
(a) |∇ξ| grows SLOWER than (T*-t)^{-1/2} (vorticity direction more coherent)
(b) ||ω||_{L²}/||ω||∞ decays FASTER than (T*-t)^{3/4} (more concentration)
(c) Some combination

### Option (a): Coherent vorticity direction
If |∇ξ| ≤ C (bounded): α/||ω||∞ ~ (T*-t)^{3/10} → 0. SUBLINEAR!
This is essentially the Constantin-Fefferman condition.

### Option (b): Super-concentration
If ||ω||_{L²}/||ω||∞ ~ (T*-t)^{3/4+ε}: α/||ω||∞ ~ (T*-t)^{2ε/5} → 0.
This means the vorticity is MORE concentrated than parabolic.
But on T³: the energy budget constrains ||ω||_{L²} from BELOW...
Actually no, it constrains the TIME INTEGRAL of ||ω||²_{L²}.
More concentration (smaller ||ω||_{L²}) actually helps the energy budget.

### Option (c): Key Lemma improvement
Our Key Lemma gives α < (√3/2)||ω||∞ (constant improvement).
This reduces the CONSTANT but not the SCALING.
α/||ω||∞ < √3/2 ≈ 0.866 instead of < 1. Still O(1), not o(1).

## THE PRECISE GAP (FINAL FORM)

**Proven**: α/|ω| < √3/2 at vorticity maxima (constant bound < 1).

**Needed**: α/|ω| → 0 as |ω| → ∞ (the ratio vanishes).

**The integral representation shows**: this ratio is determined by the
BALANCE between:
- Self-vanishing (algebraic depletion, near-field): depletes by |∇ξ|·ℓ
- Concentration (spatial decay of ω, far-field): depletes by ||ω||_{L²}/ℓ^{3/2}
- Direction gradient growth (|∇ξ| scaling): OPPOSES depletion

At Type I: all three are in PERFECT BALANCE. The ratio α/||ω||∞ is O(1).

**The gap is not about constants. It's about SCALING.**
Any constant-factor improvement (Key Lemma, better SOS floor) cannot
change the scaling. Only a STRUCTURAL change in how |∇ξ| or ||ω||_{L²}
scale near blowup would close the gap.

## CONNECTION TO EXISTING RESULTS

| Regularity Criterion | What it bounds |
|---------------------|----------------|
| Constantin-Fefferman | |∇ξ| ≤ C → coherent → sublinear α |
| Beirao da Veiga | |∇ξ| ≤ C|y|^{-1/2} → ½-Hölder coherent |
| Grujić (localized) | ½-Hölder on parabolic cylinder |
| Ruzmaikina-Grujić | Isotropy of curlω → far-field depleted |
| **Key Lemma (ours)** | α < (√3/2)|ω| → constant depletion |

All existing depletion results are CONDITIONAL: they assume coherence or
isotropy. None proves coherence/isotropy unconditionally.

The Key Lemma is UNCONDITIONAL but only gives constant depletion.
Bridging unconditional + sublinear = THE MILLENNIUM PRIZE.

## 809. Constantin integral + Type I concentration: α/||ω||∞ stays O(1).
## Self-vanishing depletes near-field. Concentration depletes far-field.
## Direction gradient growth opposes both. Type I is exact balance.
## Constants don't matter. Scaling matters. Gap = scaling gap.
