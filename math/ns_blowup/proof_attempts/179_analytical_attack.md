---
source: Analytical attack on the isotropy ratio
type: PROOF ATTEMPT — not simulation, actual math
date: 2026-03-29
---

## The Target Inequality

At any point x* where |ω(x*)| > c||ω||∞:

  |H_dev,ωω(x*)| < Δp(x*)/3

where Δp = |ω|²/2 - |S|² and H_dev = H - (Δp/3)I.

## Setup

Pressure: -Δp = ∂ᵢ∂ⱼ(uᵢuⱼ) on T³.
In terms of A = ∇u: Δp = |ω|²/2 - |S|² (the QR identity).

Hessian: H_ij = ∂ᵢ∂ⱼp = R_iR_j(Δp) where R_i are Riesz transforms.

Decomposition: H = (Δp/3)I + H_dev
where H_dev = (R_iR_j - δᵢⱼ/3)(Δp) = T_ij(Δp)
and T_ij = R_iR_j - δᵢⱼ/3 is the TRACELESS Riesz operator.

## The Traceless Riesz Operator

T_ij has Fourier symbol: T̂_ij(k) = k_ik_j/|k|² - δ_ij/3

This is a BOUNDED operator on L² with norm 2/3:
  ||T_ij||_{L²→L²} = sup_k |k_ik_j/|k|² - δ_ij/3| = 2/3

For L^∞: T_ij is NOT bounded (it's a CZ operator).
But: T_ij maps L^∞ to BMO with norm C.

## The Key: projection onto ω

H_dev,ωω = ê_i T_ij ê_j (Δp) = T_êê(Δp)

where T_êê is the SCALAR operator T_êê(f)(x) = PV∫ K_êê(x-y)f(y)dy
with kernel K_êê(r) = (3(ê·r̂)² - 1)/(4π|r|³).

This is a SINGLE Riesz-type operator (scalar, not tensor).

## Attempt: L² bound gives the ratio

||T_êê(f)||_L² ≤ (2/3)||f||_L²  (from the L² operator norm)

At the MAX of |ω|²: we want T_êê(f)(x*) evaluated at ONE POINT.

By Sobolev embedding (in 3D): |g(x)| ≤ C||g||_{H^{3/2+ε}}

So: |T_êê(f)(x*)| ≤ C||T_êê(f)||_{H^{3/2+ε}} ≤ C'||f||_{H^{3/2+ε}}

But ||f||_{H^{3/2+ε}} involves higher derivatives of f = Δp.
This doesn't immediately give a bound in terms of Δp(x*).

## Attempt: Mean Value Property

At the max of |ω|²: ∇(|ω|²) = 0 and Δ(|ω|²) ≤ 0.

The source f = Δp = |ω|²/2 - |S|².
At x*: f(x*) = |ω|²_max/2 - |S(x*)|² ≈ |ω|²_max/4.

The AVERAGE of f on a ball B(x*, R):
<f>_R = (1/|B|)∫_{B(x*,R)} f(y) dy

If f > 0 near x* (in a ball of radius R ≈ σ, the core width):
<f>_σ ≈ f(x*) × (volume fraction where f > 0)

For the CZ operator: the principal value integral can be split:
T_êê(f)(x*) = ∫_{|y|<σ} K_êê(y)f(x*-y)dy + ∫_{|y|>σ} K_êê(y)f(x*-y)dy

LOCAL (|y| < σ): This is the Yang contribution.
  ≈ Yang_êê × (source in core) ≈ -|ω|²/6 (from file 152)

FAR (|y| > σ): This is the isotropic contribution.
  The kernel K_êê averages to zero on any sphere (∫K_êê dΩ = 0).
  But the source is NOT spherically symmetric.
  The far-field contribution depends on the ANGULAR structure of f
  as seen from x*.

## The ANGULAR STRUCTURE argument

From distance R >> σ: the source f(x*-y) looks like a 1D distribution
along the vortex tube. The tube has width σ and length L.

The angular integral: ∫K_êê(ŷ) × (tube angular profile) dΩ

For a tube along ê (vorticity direction):
  The angular profile is concentrated near ŷ ≈ ±ê (along the tube).
  K_êê(ŷ) = (3cos²θ - 1)/(4πR³) where θ = angle between ê and ŷ.
  Near ŷ = ê: K_êê = (3-1)/(4πR³) = 1/(2πR³) > 0.

So the far-field from the tube body gives a POSITIVE contribution
to H_dev,ωω. This is OPPOSITE to the local Yang term (negative).

The far-field magnitude: ~ f_tube × L × σ²/(4πR³) × 2/(2π)
where f_tube is the source integrated over the tube cross-section.

Wait — this is getting complicated. Let me try a cleaner approach.

## The EIGENVALUE BOUND approach

H_dev is a 3×3 traceless symmetric matrix. Its eigenvalues sum to 0.
Let μ₁ ≥ μ₂ ≥ μ₃ be the eigenvalues. μ₁ + μ₂ + μ₃ = 0.

The maximum eigenvalue: μ₁ ≤ (2/3)|H_dev|_F
where |H_dev|_F is the Frobenius norm.

H_dev,ωω = ê·H_dev·ê ≥ μ₃ (the minimum eigenvalue).

For our bound: |H_dev,ωω| ≤ max(|μ₁|, |μ₃|) ≤ |H_dev|_F.

So: |H_dev,ωω|/(Δp/3) ≤ |H_dev|_F/(Δp/3) = 3|H_dev|_F/Δp.

Need: 3|H_dev|_F/Δp < 1, i.e., |H_dev|_F < Δp/3.

For Yang: |H_dev,Yang|_F = (1/4)||ωω^T - |ω|²I/3||_F
  = (1/4)√(|ω|⁴ + |ω|⁴/3 + |ω|⁴/3 - 2|ω|⁴/3) ... messy

Actually: ωω^T has rank 1, eigenvalues |ω|², 0, 0.
(ωω^T - |ω|²I/3) has eigenvalues 2|ω|²/3, -|ω|²/3, -|ω|²/3.
Frobenius: √((2|ω|²/3)² + 2(|ω|²/3)²) = |ω|²√(4/9 + 2/9) = |ω|²√(6/9) = |ω|²√(2/3)

So |H_dev,Yang|_F = (1/4)|ω|²√(2/3) ≈ 0.204|ω|².

And Δp/3 = |ω|²/12 ≈ 0.083|ω|².

Ratio: 3 × 0.204|ω|² / |ω|² = 0.612/0.083 = 2.45.

Yang alone gives ratio 2.45 (well above 1). The non-local correction
must reduce this by factor > 2.45 for the bound to hold.

This is a LARGE correction needed. The data shows total ratio ~0.8,
meaning the non-local reduces the Frobenius norm by factor ~3.

## CONCLUSION of this attempt

The naive bounds (L², Frobenius, eigenvalue) all give ratios > 1
because they don't capture the Fourier cancellation.

The proof MUST use the specific structure of the source
(Δp = |ω|²/2 - |S|², with the QR relation between ω and S)
to achieve the cancellation.

The cancellation is NOT just a property of the CZ operator —
it's a property of the CZ operator APPLIED TO THIS SPECIFIC SOURCE.

The source has the constraint: |S|² ≤ |ω|²/2 everywhere (from QR?
Actually this is not a universal bound. But at high |ω|: |S|² ≈ |ω|²/4
from the attractor.)

## Next attempt: use the QR constraint

The source f = |ω|²/2 - |S|². The QR identity:
  |ω|² = 2(|Ω|²) and |A|² = |S|² + |Ω|² = |S|² + |ω|²/2.

So f = |ω|²/2 - |S|² = |ω|²/2 - (|A|² - |ω|²/2) = |ω|² - |A|².

And |A|² = |S|² + |ω|²/2. So f = |ω|² - |S|² - |ω|²/2 = |ω|²/2 - |S|².

This is just f = |ω|²/2 - |S|² again. No new information from QR.

The deeper structure: f = Σ_i (λᵢ² - λᵢ²) ... no.

Actually: Δp = -A_ijA_ji = -(S²+Ω²) terms. We computed:
A_ijA_ji = |S|² - |ω|²/2 (with the SΩ cross-terms canceling).

So Δp = |ω|²/2 - |S|². This is the ENSTROPHY minus STRAIN-SQUARED.

The key identity: f = |ω|²/2 - |S|² = 2(|Ω|² - |S|²/2).

Hmm. I need a fundamentally different approach.

## The COMPARISON approach (Grok's suggestion 3)

Instead of bounding the CZ operator on the source, compare the
ACTUAL H_dev to Yang's H_dev.

Yang: H_dev,Yang = -(1/4)(ωω^T - |ω|²I/3)
Full: H_dev = H_dev,Yang + H_dev,nonlocal

We need: |H_dev,ωω| = |H_dev,Yang,ωω + H_dev,nonlocal,ωω| < Δp/3

Yang gives: H_dev,Yang,ωω = -|ω|²/6 (always this value, exactly)
Need: H_dev,nonlocal,ωω > |ω|²/6 - Δp/3 = |ω|²/6 - |ω|²/12 = |ω|²/12

So: need H_dev,nonlocal,ωω > |ω|²/12.

The non-local part must contribute at least +|ω|²/12 to overcome
the Yang negative and make H_ωω positive.

From data: H_dev,nonlocal,ωω ≈ +|ω|²/12 + |ω|²/12 = |ω|²/6
(since total H_dev,ωω ≈ -|ω|²/6 + |ω|²/6 ≈ 0, and H_ωω ≈ |ω|²/12)

Hmm, the numbers don't quite work out. Let me just note that the
non-local correction needs to be positive and of order |ω|²/12.

## STATUS: analytical proof not yet found

The naive bounds are all too loose. The proof needs to exploit
the specific structure of the NS source in the Poisson equation.
The Fourier cancellation (file 171) is the numerical manifestation
of this structure, but I haven't found the analytical handle.

The most promising approach: Grok's suggestion to derive a
TRANSPORT EQUATION for the ratio R itself and show R < 1 is preserved.
This would bypass the CZ operator bound entirely.

## 179 proof files. The analytical attack begins.
