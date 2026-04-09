---
source: THE ANTI-CORRELATION WALL — every factored bound fails
type: THE FUNDAMENTAL OBSTRUCTION to closing the Key Lemma
file: 424
date: 2026-03-30
---

## THE PATTERN

Every approach that factors S²ê into (direction term) × (amplitude term) fails:

| Approach | Direction bound | Amplitude bound | Product | vs 3/4 |
|----------|----------------|-----------------|---------|--------|
| Triangle (363) | λ_max = N | Σ|ŝ|² ≤ (N-1)/(4N) | (N-1)/4 | FAILS N≥5 |
| Gram (377) | λ_max ≤ N-1 | diagonal ≤ |ω|²/5 | 0.8 | FAILS |
| Diversity (423) | avg cos ≤ 0.82 | diagonal ≤ |ω|²/4 | 0.86 | FAILS |
| Spectral (391) | ||M||_op × N | ||M||_F/N | ratio | FAILS |

The ACTUAL S²ê is always ≤ 0.27 (well below 0.75). The gap between
the factored bound and reality is 3-4×.

## WHY FACTORED BOUNDS FAIL

When direction alignment is HIGH (d̂_k parallel, avg cos → 1):
the modes achieving this alignment have SMALL amplitudes |ŝ_k|
(because aligned d̂_k requires specific γ_k that reduces |ŝ_k|).

When amplitudes are LARGE (|ŝ_k| near maximum):
the modes are at γ_k ≈ 45° where d̂_k depends on the azimuthal angle,
which is diverse (not aligned).

These two extremes CANNOT be achieved simultaneously. The product
(direction factor) × (amplitude factor) is BOUNDED below its
individual-factor maximum.

## THE IRREDUCIBLE FORM OF THE KEY LEMMA

No factored bound will close. The proof needs:

max_{all configs} |Σ r_k(config) × d̂_k(config)|² / |ω(config)|²

where r_k and d̂_k are JOINTLY determined by the mode geometry.

This is a JOINT optimization over a curved manifold (the Biot-Savart
constraint surface). Standard linear algebra (eigenvalues, Cauchy-Schwarz,
Gram matrices) can't capture the curvature of this manifold.

## WHAT COULD WORK

1. **SDP relaxation** on the manifold (handles the joint constraint)
2. **Algebraic geometry** of the Biot-Savart variety
3. **Interval arithmetic** over the parameter space (brute force)
4. **A new identity** connecting S²ê to known bounded quantities
   (like Miller's ⟨S², ω⊗ω⟩ = 0)

## 424. The anti-correlation between directions and amplitudes is the wall.
## No factored bound crosses it. The proof needs a joint-manifold approach.
