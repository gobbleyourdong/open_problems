---
source: Non-degenerate max of |ω| forces Q < 0
type: PROOF ATTEMPT — the peaked source argument
date: 2026-03-29
---

## Key Insight

At a NON-DEGENERATE max of |ω|²: the Hessian ∇²(|ω|²) has all
negative eigenvalues. The vorticity forms a PEAK in space.

The pressure source Δp = |ω|²/2 - |S|² inherits this peak structure
(since Δp ≈ |ω|²/2 is the dominant term at high |ω|).

A PEAKED source in the Poisson equation creates a pressure whose
Hessian is MORE ISOTROPIC than a flat source (the peak contributes
positively to H_zz from the z-curvature).

## The Peaked Source Decomposition

At x* (max of |ω|²): expand Δp in the local frame where ê = ω̂ ∥ z:

Δp(x*+r) = Δp(x*) + 0 (gradient = 0)
           - (1/2)(μ_x r_x² + μ_y r_y² + μ_z r_z²) + O(|r|³)

where μ_x, μ_y, μ_z > 0 are the curvatures of the peak (negative of
the Hessian eigenvalues, all positive for a non-degenerate max of Δp).

The ISOTROPIC part: (μ_x+μ_y+μ_z)/3 = Δ(Δp)/6 at x*.
The ANISOTROPIC part: deviations from the mean curvature.

## How Peak Curvature Creates H_zz > 0

For a source peaked in z (μ_z > 0):
The Poisson equation creates pressure that responds to the z-peak.
At the peak: ∂²p/∂z² > 0 (the pressure curves UPWARD to match the
source that curves DOWNWARD).

More precisely: Δp = f where f has a local max at x*.
Near x*: f ≈ f₀ - (1/2)μ·r². The PARTICULAR solution:
p_part ≈ f₀|r|²/6 - (1/2)μ·(|r|⁴ terms)/... (complex)

The HESSIAN of p at x*: H_ij = ∂²p/∂x_i∂x_j.
From the constant part: H_ij = f₀/3 × δ_ij (isotropic).
From the quadratic correction: involves Δ(Δp) and the curvatures μ.

## The Critical Calculation

For f(r) = f₀ - (1/2)(μ_⊥(x²+y²) + μ_∥z²) (axisymmetric peak):

The Poisson solve: Δp = f on T³.
Local contribution to H_zz at origin:

H_zz = f₀/3 + (correction from the peak curvatures)

The correction: from the peaked source, the z-curvature μ_∥ creates
ADDITIONAL positive H_zz (the Poisson responds to the z-peak).

The calculation: for the peaked source on R³ (ignoring periodicity):
p(0) = -∫ f(y)/(4π|y|) dy
H_zz(0) = ∫ (3z²/|y|⁵ - 1/|y|³) f(y)/(4π) dy + f(0)/3

The integral: with f = f₀ - μ⊥(x²+y²)/2 - μ∥z²/2:
The constant f₀ gives: ∫(3z²/|y|⁵ - 1/|y|³) f₀/(4π) dy → PV = 0 (zero for constant).
The quadratic: -∫(3z²/|y|⁵ - 1/|y|³) (μ⊥r⊥² + μ∥z²)/(8π) dy

By symmetry (integrating the P₂ kernel against r²-type functions):
∫(3z²-|y|²)(μ⊥(x²+y²)+μ∥z²)/(4π|y|⁵) dy

= ∫(3cos²θ-1)(μ⊥sin²θ+μ∥cos²θ)|y|² dΩ/(4π|y|⁵) × ∫r² dr/r³

The radial integral ∫dr/r diverges (need regularization by periodicity).
On T³: the integral is finite but depends on the torus geometry.

## The Sign

The angular integral:
∫(3cos²θ-1)(μ⊥sin²θ+μ∥cos²θ) sinθ dθ

= μ⊥∫(3cos²θ-1)sin²θ sinθ dθ + μ∥∫(3cos²θ-1)cos²θ sinθ dθ

Using ∫P₂(cosθ) sin²θ sinθ dθ = -4/15
and ∫P₂(cosθ) cos²θ sinθ dθ = +4/15:

= μ⊥(-4/15) × 2 + μ∥(+4/15) × 2 = (8/15)(μ∥ - μ⊥)

So the correction to H_zz from the peak curvatures is proportional to
(μ∥ - μ⊥): the EXCESS z-curvature relative to ⊥-curvature.

If the peak is MORE CURVED in z than in ⊥ (μ∥ > μ⊥): correction > 0.
If the peak is LESS curved in z (μ∥ < μ⊥): correction < 0.

For the STRAIGHT TUBE: μ∥ = 0 (no z-curvature), μ⊥ > 0.
Correction = -8μ⊥/15 < 0 → H_zz reduced → ratio = 1.

For ISOTROPIC peak (μ∥ = μ⊥): correction = 0 → H_zz = f₀/3 (isotropic).

For z-ELONGATED peak (μ∥ > μ⊥): correction > 0 → H_zz > f₀/3 → ratio < 1.

## THE KEY: What determines μ∥?

μ∥ is the curvature of the |ω|² peak in the ω DIRECTION.

μ∥ = -∂²|ω|²/∂z² at the max = 2|∂ω/∂z|² + 2ω·∂²ω/∂z² evaluated at max.

At the max: ∂|ω|²/∂z = 0 → ω·∂ω/∂z = 0 → ∂ω/∂z ⊥ ω.

So: μ∥ = -2|∂ω/∂z|² - 2ω·∂²ω/∂z² (from Δ(|ω|²) expansion)

μ∥ > 0 (since it's a max): |ω|² curves downward in z → μ∥ > 0.

The MAGNITUDE of μ∥ depends on how sharply |ω| peaks in the ω direction.

For flows with STRAIN along ω (α > 0): the vorticity is being
stretched, creating |∂ω/∂z| > 0 → μ∥ > 0.

For the straight tube: |∂ω/∂z| = 0 (z-independent) → μ∥ = 0.

## CONNECTION TO α > 0

CLAIM: α > 0 at the max implies μ∥ > 0 (the peak is non-degenerate in z).

ARGUMENT: α > 0 means ê·S·ê > 0. The strain stretches along ω.
Stretching creates VARIATION of ω along ω (the stretching deforms
the vortex, making |ω| change along ω). This gives |∂ω/∂z| > 0 → μ∥ > 0.

If μ∥ > 0 and μ∥ ≥ μ⊥ (the z-variation is at least as strong as ⊥):
The peak correction is ≥ 0 → H_zz ≥ f₀/3 → ratio ≤ 1 → Q ≤ 0.

## THE REMAINING QUESTION

Does α > 0 imply μ∥ ≥ μ⊥?

NOT NECESSARILY in general. α > 0 means stretching ALONG ω, which
creates z-variation. But the ⊥-variation (from the tube core profile)
could be even larger.

However: at HIGH |ω| (at the attractor): the core is THIN (σ small),
making μ⊥ ~ 1/σ² (large). And the z-variation from stretching:
μ∥ depends on the GLOBAL tube structure.

For the TREFOIL: the tube curves → μ∥ comes from the curvature.
The curvature radius R ~ 1 (fixed). So μ∥ ~ |ω|²/R² ~ |ω|².
And μ⊥ ~ |ω|/σ² (from the core). With σ² = Γ/(π|ω|):
μ⊥ ~ |ω|/(Γ/(π|ω|)) = π|ω|²/Γ.

Both μ∥ and μ⊥ scale as |ω|². The RATIO μ∥/μ⊥ depends on the
geometry (curvature vs core width) and doesn't simplify easily.

## 196. The peaked source argument quantifies how peak curvature
## determines H_zz. The sign depends on μ∥ vs μ⊥.
## α > 0 gives μ∥ > 0 but doesn't guarantee μ∥ ≥ μ⊥.
