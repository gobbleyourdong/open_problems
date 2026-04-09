---
source: CASCADE FAILS — exponent 5/4 is subquadratic but still superlinear
type: FAILED APPROACH — the self-limiting cascade doesn't prevent blowup
file: 801
date: 2026-04-01
instance: MATHEMATICIAN
---

## THE CALCULATION

From the SOS floor increasing with N and Kolmogorov scaling K ~ Ω^{1/2}:
  N_eff ~ Ω^{3/2}
  S²ê/|ω|² ~ 1/N_eff ~ Ω^{-3/2}
  α ~ Ω^{1/4} (from α/|ω| ~ Ω^{-3/4})
  d/dt Ω ~ Ω^{5/4}

Exponent 5/4 > 1 → still blows up in finite time.
(5/4 < 2, so slower than Type I, but still superlinear.)

For NO blowup: need exponent ≤ 1, i.e., α ≤ C (constant).
This would require N_eff ~ Ω^3 (K ~ Ω), which means the
dissipation scale shrinks as 1/Ω. Not physical.

## THE FUNDAMENTAL ISSUE

Any bound of the form α/|ω| ≤ f(||ω||∞) with f(Ω) → 0 as Ω → ∞
gives d/dt Ω ≤ f(Ω)Ω². For no blowup: need f(Ω)Ω² ≤ CΩ, i.e.,
f(Ω) ≤ C/Ω. This means α ≤ C (BOUNDED stretching rate).

The Kolmogorov cascade gives f(Ω) ~ Ω^{-3/4}. We need f ~ Ω^{-1}.
The gap: one power of Ω^{1/4}.

## THE WALL (AGAIN)

The Type I → regularity gap cannot be closed by:
- The Key Lemma alone (fixed ratio α/|ω| < √3/2)
- The cascade + Kolmogorov scaling (exponent 5/4 > 1)
- The Prodi-Serrin criteria (all require integrable norms)
- Seregin's L³ condition (consistent with Type I)

The gap IS the Liouville conjecture (or equivalent).

## WHAT WE ACHIEVED

We reduced NS regularity to: "Type I blowup cannot occur on T³."
This is known for axisymmetric flows (Seregin-Sverak 2009) and
equivalent to the Liouville conjecture for general flows.

Our Key Lemma (804K SOS certificates) is the HARD PART.
The Type I exclusion is the STANDARD PART (open but well-studied).

## 801. The cascade gives exponent 5/4 > 1. Still blows up.
## Need exponent ≤ 1 for regularity. Gap = one power of Ω^{1/4}.
## The Type I → regularity problem IS the Millennium Prize.
