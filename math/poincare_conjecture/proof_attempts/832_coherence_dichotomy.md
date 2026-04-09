---
source: COHERENCE DICHOTOMY — the argument that almost closes the gap
type: PROOF ATTEMPT — dichotomy on the coherence exponent β
file: 832
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE DICHOTOMY

Define: D_total(t) = (|ω|² - Σ|k_j|²)/2 (vorticity cross-term at argmax).
N_eff(t) = number of significantly active Fourier modes.
β = log(D)/log(N_eff) (the coherence exponent).

### Case β > 1: Coherent vorticity
|S|²/|ω|² ≈ Σ|k|²/(2|ω|²) ≈ N/(2·2D) ≈ N/(4N^β) = N^{1-β}/4 → 0.
α ≤ √((2/3)·N^{1-β}/4) · |ω| = C · N^{(1-β)/2} · |ω| → 0 · |ω|.
Sublinear stretching → no blowup. ✓

### Case β ≤ 1: Incoherent vorticity
|ω|² = Σ|k|² + 2D ≤ CₖN + 2CN^β ≤ C'N (for β ≤ 1).
||ω||∞ ≤ C'√N.
For blowup: need ||ω||∞ → ∞. Requires N → ∞.

BUT: even with N → ∞, ||ω||∞ ~ √N. The growth rate:
d/dt ||ω||∞ ≤ (3/4)||ω||∞² ≤ (3/4)C'N(t).

If N(t) grows polynomially: ||ω||∞ grows polynomially. No finite-time blowup.
If N(t) grows exponentially: ||ω||∞ grows exponentially. No finite-time blowup.
For finite-time blowup: need N(t) → ∞ in finite time.

### Does N(t) → ∞ in finite time force blowup?

N(t) = #{active modes} ~ K_eff³ where K_eff is the effective wavenumber.
For N → ∞ in finite time: K_eff → ∞ in finite time.

But the energy is bounded: ||u||² ≤ ||u₀||². The energy per mode:
|û_k|² ~ ||u||²/N → 0 as N → ∞. Each mode gets weaker.

The enstrophy: ||ω||² = Σ|k|²|û_k|² ≤ K² Σ|û_k|² = K²||u||² ≤ K²||u₀||².
So ||ω||∞ ≤ √(Σ|ω_j|²) ≤ √(||ω||²) ≤ K||u₀||.

For K → ∞: ||ω||∞ could grow as K. With K ~ (T*-t)^{-1/2} (parabolic):
||ω||∞ ~ (T*-t)^{-1/2}. Then d/dt||ω|| ~ ||ω||² ~ (T*-t)^{-1}.
∫(T*-t)^{-1/2} dt converges. BKM SATISFIED. NO BLOWUP!

Wait: if ||ω||∞ ~ (T*-t)^{-1/2} (sub-Type-I): the BKM integral
∫||ω||∞ dt ~ ∫(T*-t)^{-1/2} dt = 2√(T*-t) → 0. CONVERGES.
BKM: ∫||ω||∞ < ∞ → regularity. NO BLOWUP. ✓

### The refined analysis for β = 1 (borderline)

At β = 1: D ~ N, |ω|² ~ 3N. ||ω||∞ ~ √(3N).
For each mode: |ω_j| ~ |k_j| ~ K. With N ~ K³:
||ω||∞ ~ √(3K³) = √3 · K^{3/2}.

d/dt ||ω||∞ ≤ (3/4)||ω||∞² = (3/4)·3K³ ≈ (9/4)K³.

K changes as new modes are activated. The activation rate depends on
the energy cascade. Under viscous damping: modes with |k| > K_d are
damped, where K_d ~ (ε/ν³)^{1/4} (Kolmogorov dissipation wavenumber).

For ||ω||∞ ~ K^{3/2}: the dissipation rate ε ~ ν||ω||² ~ νK³.
K_d ~ (νK³/ν³)^{1/4} = (K³/ν²)^{1/4} = K^{3/4}/ν^{1/2}.

The effective mode count: N_eff ~ K_d³ ~ K^{9/4}/ν^{3/2}.

So N grows as K^{9/4}, and ||ω||∞ ~ K^{3/2}. Eliminating K:
K ~ N^{4/9}, ||ω||∞ ~ N^{4/9 · 3/2} = N^{2/3}.

d/dt ||ω||∞ ≤ (3/4)·||ω||∞² = (3/4)N^{4/3}.
d/dt N ~ d/dt K³ = 3K²·dK/dt. The growth of K...

This analysis is getting circular. The point is:

## THE CLEAN ARGUMENT

1. **Blowup ⟹ N_eff → ∞** (Galerkin regularity). PROVEN.

2. **Blowup ⟹ ||ω||∞ → ∞** (by definition).

3. **||ω||∞ → ∞ with N_eff modes ⟹ β > 1** (the modes must be coherent).
   Because: ||ω||∞² ≤ Σ|ω_j|² + 2D = Σ|k_j|² + 2D.
   For ||ω||∞ → ∞: need Σ|k_j|² + 2D → ∞.
   Σ|k_j|² ≤ N·K² (bounded per mode). For Σ|k_j|² → ∞: need N or K → ∞.
   If K is bounded: Σ|k_j|² ≤ NK², ||ω||∞² ≤ NK² + 2D.
   For ||ω||∞ ≫ √N: need D ≫ N, i.e., β > 1.

   ACTUALLY: ||ω||∞ ~ C/(T*-t) → ∞. And N_eff → ∞.
   BUT ||ω||∞ is NOT just √(N + 2D). It's the maximum of |ω(x)| over x ∈ T³.
   The maximum can be large even if the L² norm is moderate.

   ||ω||∞ ≤ C||ω||_{L²}^{1/4}||ω||_{H²}^{3/4} (Agmon on T³).
   So ||ω||∞ can be large if ||ω||_{H²} is large (high derivatives).
   ||ω||_{H²} is NOT bounded by the mode count — it depends on the
   distribution of energy across modes.

4. **THE HOLE**: ||ω||∞ can blow up even with D ~ O(1) if the energy
   concentrates at high k. The L^∞ norm depends on SPATIAL concentration,
   not just on the coherence of the Fourier modes.

   A single mode with |k| = K and unit amplitude has ||ω||∞ = K.
   As K → ∞: ||ω||∞ → ∞ with N_eff = 1. And D = 0 (single mode).
   β = 0. But α = 0 (self-vanishing for single mode). No blowup.

   For 2 modes with |k₁| = K, |k₂| = K: ||ω||∞ ≤ 2K.
   α ≤ (3/4)·2K (Key Lemma). Still Type I.

   For N modes at large K: ||ω||∞ ≤ NK. α ≤ (3/4)·NK·(from SOS at N).
   α/||ω||∞ ≤ c(N) where c(N) → 0 from the SOS data.
   BUT α·||ω||∞ ≤ c(N)·(NK)² = c(N)N²K².
   For c(N) ~ 1/√N: α·||ω||∞ ~ N^{3/2}K². This can blow up with K.

   The growth: d/dt||ω||∞ ≤ c(N)||ω||∞² = c(N)N²K².
   Under the cascade: K grows → ||ω||∞ grows → K grows more.

   The question: does c(N) decrease FAST ENOUGH to offset the K growth?

## THE BOTTOM LINE

The dichotomy argument has a HOLE at the borderline β = 1.
The modes can be incoherent (D small) but at HIGH wavenumber (K large),
making ||ω||∞ large from spatial concentration rather than coherence.

The SOS floor growth c(N) → 0 would close this IF c(N) decreases fast
enough relative to the K growth. With c(N) ~ 1/√N and K ~ ||ω||∞/N:
d/dt||ω||∞ ≤ (1/√N)||ω||∞² = ||ω||∞²/√N.
With N growing with K which grows with ||ω||∞: this MIGHT close.

The precise relationship between N_eff, K, and ||ω||∞ under NS dynamics
determines whether the gap closes.

## 832. Coherence dichotomy: β > 1 → depletion, β ≤ 1 → can't blow up...
## EXCEPT at borderline β ≈ 1 with high K. The hole: spatial concentration
## at high wavenumber allows ||ω||∞ → ∞ even with incoherent modes.
## Closing requires: c(N_eff) decreases faster than K²/||ω||∞² grows.
