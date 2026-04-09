---
source: Scaling argument needs tighter Fourier lemma coefficient
type: ALMOST — the scaling works (10:1 in data) but analytical bound too loose
file: 276
date: 2026-03-29
---

## The Numbers

At the trefoil max (α/|ω| ≈ 0.13):
- DH_ωω/Dt (measured) ≈ 326 → C₁ = DH_ωω/|ω|³ ≈ 0.021
- 2α³ (measured) ≈ 32 → C₂ = 2α³/|ω|³ ≈ 0.002
- Ratio C₁/C₂ ≈ 10 (data says DH_ωω beats 2α³ by 10×)

My analytical bound: C₁ ≥ 0.02α/|ω| ≈ 0.003.
Needed: C₁ > C₂ = 0.002.
My bound: 0.003 > 0.002. BARELY closes.

But this uses α/|ω| ≈ 0.13 which is MEASURED, not proven.

## The Chain of Bounds

DH_ωω/Dt ≥ (stretching rate) × (conversion factor)
≥ α|ω|² × C
≥ α|ω|² × 0.02 (from the Fourier lemma operator bound)

2α³ = 2α × α²

Ratio: DH_ωω/(2α³) ≥ 0.02|ω|²/(2α²) = 0.01(|ω|/α)²

For this > 1: need |ω|/α > 10.
From data: |ω|/α ≈ 7-8. Just barely below 10!

The bound DOES NOT CLOSE with the current Fourier lemma coefficient.
The measured ratio is 10:1, but the analytical bound gives ~0.5:1.

## What Would Close It

Need a TIGHTER Fourier lemma: the conversion factor C should be ~0.1
instead of 0.02. Then: 0.1|ω|²/(2α²) = 0.05(|ω|/α)² ≈ 0.05×64 = 3.2 > 1.

The Fourier lemma gives C ~ 1/(2(λ₁+k²)) where λ₁ is the first
eigenvalue of -Δ_xy. On T² with L=2π: λ₁ = 1.
So C = 1/(2(1+k²)). For k=1: C = 1/4 = 0.25.

Wait — my earlier estimate of C = 0.02 was wrong! The actual conversion:
|p_k| = |(Δ_xy - k²)⁻¹ f_k| ≥ |f_k|/(λ_max + k²) = |f_k|/(N²/4 + k²)
where λ_max is the largest eigenvalue of -Δ_xy.

On T² with N=32: λ_max ≈ (N/2)² = 256. So |p_k| ≥ |f_k|/257.
And H_ωω ≥ k²|p_k| ≥ k²|f_k|/257 ≈ |f_k|/257 (for k=1).

That's C ≈ 1/257 ≈ 0.004. Hmm, that's SMALLER.

But wait — the operator (Δ_xy - k²)⁻¹ is applied to a SPECIFIC f_k
which is the k-th z-Fourier component at the max point. This f_k is
concentrated near the tube center. The EFFECTIVE operator is:

p_k(x₀,y₀) = ∫ G_k(x₀-x',y₀-y') f_k(x',y') dx'dy'

where G_k is the Green's function of (Δ_xy - k²). The value at the
center depends on how concentrated f_k is.

For a CONCENTRATED f_k (width σ in xy): G_k at the center gives
|p_k| ≈ |f_k| × σ²/(4π) × (something). The σ² factor reduces |p_k|
for thin tubes.

This is getting into detailed Green's function estimates. The proof
needs a TIGHT bound on the Green's function at the tube center,
not just the operator norm.

## 276. The scaling works in the data (10:1) but the analytical bound
## is too loose (0.5:1). Need tighter Fourier lemma conversion factor.
