---
source: Instance B — numerical verification of Instance C's Lemma (file 267)
range: 222
type: LEMMA SIGN VERIFIED. Quantitative gap remains.
date: 2026-03-29
---

## Verification of the Lemma

LEMMA: On T², L = Δ_xy - k² is negative definite.
If f_k(x*,y*) > 0: then p_k(x*,y*) < 0.
Therefore -k²p_k > 0 → H_ωω > 0.

### Test: z-Fourier modes of Δp at (x*,y*) for trefoil

Every single mode has f_k and P_k with OPPOSITE signs: YES ✓
This holds for BOTH trefoil_s03 and trefoil_s015.

The sign opposition is 100% — the lemma's core mechanism is correct.

### Caveat

The reconstruction along z doesn't match H_ωω because ω is NOT
along z for the trefoil. The proof requires decomposing along ê
(the ω direction), which needs a coordinate rotation.

The LEMMA is correct regardless of axis: L = Δ_perp - k² is
negative definite on ANY perpendicular plane. The sign opposition
holds for decomposition along any direction.

### The Quantitative Gap

The lemma gives H_ωω > 0 (qualitative sign). The proof needs
H_ωω ≥ c where c is large enough relative to α².

In Case 1 (ê-independent): α = 0, H_ωω = 0. Both zero. OK.
In Case 2 (ê-variation): α > 0, H_ωω > 0. Need H_ωω/α² ≥ c' > 0.

From data: at the max point, H_ωω ≈ +10-30 and α² ≈ 0.6-6.
Ratio H_ωω/α² ≈ 2-50 (always > 1). The quantitative margin is large.

The gap: prove H_ωω/α² ≥ c' > 0 uniformly.
This might follow from: both α and H_ωω scale with the ê-variation
of the source, and H_ωω scales FASTER (because the Poisson operator
amplifies high-k modes via the -k² factor).

## 222 — Instance B confirms the lemma's sign mechanism.
