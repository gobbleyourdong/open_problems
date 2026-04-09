---
source: Computational verification
type: PROVEN LEMMA
status: VERIFIED — stronger than expected
---

## Lemma (Single-Mode Orthogonality)
For any single Fourier mode ω̂_k of a divergence-free field,
the vorticity direction is EXACTLY PERPENDICULAR to the principal
strain direction: cos²θ = 0, hence ω·S·ω = 0.

## Proof
Let k be any wavevector, ω̂ ⊥ k (div-free).
Velocity: û = ik × ω̂ / |k|²
Since k × ω̂ ⊥ ω̂ (cross product), û ⊥ ω̂.
Strain: Ŝ_ij = (k_i û_j + k_j û_i)/2
The strain tensor lies in the (k, û) plane.
ω̂ ⊥ k and ω̂ ⊥ û, so ω̂ ⊥ (k, û) plane.
Therefore ω̂ is perpendicular to ALL eigenvectors of Ŝ in that plane.
Hence ω̂·Ŝ·ω̂ = 0. □

## Verified computationally
- 10 random (k, ω) pairs, all with cos²θ = 0.000000
- θ = 90.0° exactly in every case
- This is EXACT, not approximate

## Consequence
Vortex stretching is ENTIRELY a multi-mode interaction phenomenon.
A single-mode flow cannot stretch itself. Stretching requires at least
two modes to interact via the triadic convolution.

This means:
1. The stretching term is controlled by the CONVOLUTION structure
2. At high k, the number of triadic partners is large but each
   contributes with a RANDOM alignment
3. The more modes, the more the random alignments cancel

## Connection to Exponential Decay
If each triadic interaction contributes stretching with RANDOM sign
(due to the random alignment angles), then the total stretching at
a point is a SUM of random contributions.

By CLT: the stretching fluctuation ~ √(number of triads) ~ √(N^d)
The dissipation scales as ~ N² (from |k|²)

For stretching to exceed dissipation:
  √(N^d) > N² → N^{d/2} > N² → d > 4

In 3D (d=3): N^{3/2} < N². Dissipation wins at large N.
The excess probability: P(stretching > dissip) ~ exp(-N^{4-d}) = exp(-N)

THIS GIVES exp(-N) in 3D!

## The Provable Chain
1. Single-mode stretching = 0 (PROVEN above)
2. Multi-mode stretching is a sum of triadic interactions with random phases
3. Central limit: total stretching ~ √(#triads) × typical_magnitude
4. Dissipation grows as N² (exact, from Parseval)
5. For d < 4: dissipation dominates stretching at high N
6. The excess probability decays as exp(-N^{4-d})
7. In 3D: exp(-N) ← matches our data

## Status
Steps 1 and 4 are PROVEN.
Steps 2-3 need the "random phases" assumption formalized.
Steps 5-7 are consequences.

The key gap: proving that the triadic interaction phases are
effectively random (decorrelated) for div-free fields.
This is where the Riesz transform structure and the 90° orthogonality
provide the decorrelation mechanism.
