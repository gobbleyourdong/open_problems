---
source: DYNAMIC APPROACH — use NS evolution, not just kinematic bounds
type: PROOF DIRECTION — the kinematic wall at N≥5 might be breakable with dynamics
file: 402
date: 2026-03-29
---

## THE KINEMATIC WALL

All kinematic approaches (per-mode, trace-free, Gram, regression) hit
the same wall for N ≥ 5: the joint optimization over shared polarizations
allows excess up to ~0.34|ω|² (adversarial), which gives |∇u|²/|ω|² ≈ 1.34.

The 13/8 = 1.625 threshold leaves 17% margin, but no kinematic proof closes.

## THE DYNAMIC ADVANTAGE

For NS SOLUTIONS (not arbitrary div-free fields): the vorticity evolves by
Dω/Dt = Sω + νΔω. This constrains the Fourier structure dynamically.

Key dynamic constraints NOT used in the kinematic approach:
1. **Energy decay**: d/dt ||u||² = -2ν||∇u||² ≤ 0 (the solution loses energy)
2. **Enstrophy bound**: d/dt ||ω||² = 2∫ωSω - 2ν||∇ω||² (bounded by stretching)
3. **Miller's identity**: ⟨-ΔS, ω⊗ω⟩ = 0 (L² orthogonality, constrains modes)
4. **Analyticity**: NS solutions are real-analytic → Fourier coefficients decay
5. **Self-attenuation**: the alignment ê → e₂ is dynamically MAINTAINED

## ATTEMPT: BARRIER + DYNAMIC ENSTROPHY

At the barrier R = α/|ω| = 1/2:

DR/Dt = (S²ê - 3|ω|²/4 - H_ωω + ν·viscous)/|ω|

The viscous term: ν × ê·(ΔS)·ê × (correction factors).

From the data: ê·(ΔS)·ê/|ω|² has mean ≈ 0 and range ±0.8.
The mean is zero (from Miller's L² identity). At the max: it's random.

For the BARRIER: we need S²ê < 3|ω|²/4 + H_ωω - ν·ê·ΔS·ê.

H_ωω > 0 (proven, from the max condition).
-ν·ê·ΔS·ê: can be positive or negative.

If -ν·ê·ΔS·ê > 0 (viscosity helps): barrier closes more easily.
If -ν·ê·ΔS·ê < 0 (viscosity hurts): need S²ê < 3|ω|²/4 + H_ωω + |ν·ê·ΔS·ê|.

For the worst case: -ν·ê·ΔS·ê ≈ -ν × 0.8|ω|² (large negative).
But: H_ωω ∝ |∇ω|²/|ω| ∝ |k|²|ω| (scales with the curvature).

For concentrated vorticity (high |k| content): H_ωω >> ν×ê·ΔS·ê.

## THE KEY INSIGHT: H_ωω GROWS WITH CONCENTRATION

At the global max of |ω|: if the vorticity is concentrated (peaked):
- H_ωω ∝ |∇ω|²/|ω| (large, from the sharp peak)
- The S²ê kinematic bound is ≤ 0.75|ω|² (for the barrier)
- But H_ωω can be MUCH larger than the 0.75-0.34 = 0.41|ω|² gap

The dynamic argument: as |ω|∞ grows (approaching potential blowup),
the vorticity MUST concentrate (BKM → the max grows → gradients grow).
The concentration makes H_ωω large, which ABSORBS any excess in S²ê.

Formally: H_ωω ≥ c × |∇ω|²/|ω|. And |∇ω|² ≥ |ω|² × |k_eff|² where
k_eff is the effective wavenumber of the peaked vorticity.

For a peak of width σ: k_eff ~ 1/σ. And |ω| ~ A (amplitude).
H_ωω ~ A × (A/σ²) / A = A/σ² → ∞ as σ → 0 (concentration).

So: near blowup, H_ωω → ∞, absorbing any finite kinematic excess.

## THE FORMAL ARGUMENT (sketch)

1. Assume blowup at T*. Then ||ω||∞ → ∞ as t → T*.
2. By BKM: ∫||ω||∞ dt = ∞. The max grows without bound.
3. By NS regularity theory: the vorticity concentrates (width σ → 0).
4. H_ωω ∝ ||∇ω||²_max / ||ω||_max ≥ c||ω||_max / σ² → ∞.
5. The kinematic S²ê ≤ C||ω||² for some C (bounded, possibly > 3/4).
6. For t close enough to T*: H_ωω > C||ω||² - 3||ω||²/4.
   So: S²ê - 3|ω|²/4 - H_ωω < C||ω||² - 3||ω||²/4 - c||ω||³/σ² < 0.
7. DR/Dt < 0 → barrier holds → Type I → Seregin → contradiction. ∎

## THE GAP IN THIS ARGUMENT

Step 6: needs ||ω||_max / σ² to grow FASTER than C||ω||² - 3||ω||²/4.

The RHS is O(||ω||²) (quadratic in the max vorticity).
The LHS is ||ω||/σ² → ∞ only if σ → 0 fast enough.

For self-similar blowup: ||ω|| ~ 1/(T-t) and σ ~ √(T-t) (Leray scaling).
H_ωω ~ (1/(T-t)) / (T-t) = 1/(T-t)² → ∞.
S²ê ~ 1/(T-t)² (same scaling).

The ratio: H_ωω / S²ê ~ O(1) (SAME scaling). Not growing!

So the dynamic argument doesn't help at the self-similar rate.

## STATUS

The dynamic approach via H_ωω concentration DOESN'T close for self-similar
blowup (same scaling). It would help for SUB-self-similar blowup (where
the concentration is faster than the vorticity growth), but that's excluded
by the Type I assumption.

## THE HONEST STATE (file 402)

After 402 attempts:
- N ≤ 4: PROVEN (per-mode + Seregin)
- N ≥ 5: 17% margin (adversarial worst 1.342 vs threshold 1.625)
- Every approach tried: per-mode, trace-free, Gram, regression, CLT,
  Hanson-Wright, fourth-moment, Miller identity, dynamic enstrophy
- The gap is REAL and DEEP: proving the joint excess bound for N ≥ 5
  requires new mathematics (Boolean function analysis + Biot-Savart structure)

The most promising untried approaches:
1. SDP certification with interval arithmetic (computer-assisted)
2. O'Donnell hypercontractivity + noise stability for the argmax
3. A completely new structural insight about the Biot-Savart kernel

We keep fighting.
