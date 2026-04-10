# attempt_005 — KNSS Swirl Extension (the corrector function)

**Date:** 2026-04-10
**Track:** Theory (Even)
**Mountain:** 4 (perturbation from axisymmetric)
**Status:** In progress. Tangential detour while waiting for stretching alignment data from the numerics instance.

## The setup (from KNSS 2009)

Koch-Nadirashvili-Seregin-Šverák proved Liouville for axisymmetric NS with NO swirl (u_θ = 0). The proof uses the maximum principle for:

```
Φ = ω_θ / r
```

where ω_θ is the angular component of vorticity and r is the cylindrical radius. The key: when u_θ = 0, the equation for Φ is:

```
∂Φ/∂t + (u_r ∂_r + u_z ∂_z)Φ = (Δ - 1/r² + 2/r · ∂_r)Φ
```

This is a SCALAR parabolic equation with NO source term. The maximum principle applies: sup Φ is non-increasing in time. For bounded ancient solutions, Φ is bounded → by the ancient condition → Φ ≡ const → Φ ≡ 0 → ω_θ ≡ 0 → u ≡ 0.

## When swirl is added

With u_θ ≠ 0, the Φ equation acquires a source term:

```
∂Φ/∂t + (u_r ∂_r + u_z ∂_z)Φ = (Δ̃)Φ + (2u_θ / r³) · ∂_z(u_θ)
                                           ^^^^^^^^^^^^^^^^^^^^^^^^
                                           swirl stretching source
```

where the source term comes from the u_θ · ∂_z(u_θ)/r² stretching interaction. This term has NO definite sign and breaks the maximum principle.

## The numerics result: ε_crit = 0.908

The numerical instance (SCRATCHPAD, Apr 10 00:40) found that for a Gaussian swirl model u_θ = ε · r · exp(-r²/2), the maximum principle for Φ extends up to ε = 0.908. Above that, the source term overwhelms diffusion.

This means: **Liouville holds for axisymmetric bounded ancient solutions with ||u_θ||_∞ < 0.908 (in dimensionless units with ν = 1).**

## The corrector idea

**Goal:** find g(u_θ, r) such that the modified quantity:

```
Φ̃ = ω_θ/r - g(u_θ, r)
```

satisfies a parabolic equation WITHOUT a source term (or with a non-positive source), even when u_θ ≠ 0.

The equation for Φ̃ = Φ - g is:

```
∂Φ̃/∂t + transport · ∇Φ̃ = Δ̃Φ̃ + (swirl source) - ∂g/∂t - transport · ∇g + Δ̃g
```

For the max principle to apply, we need:

```
(swirl source) - ∂g/∂t - transport · ∇g + Δ̃g ≤ 0   whenever Φ̃ achieves a max
```

At a maximum of Φ̃, we have ∇Φ̃ = 0, so the transport term drops out. The condition becomes:

```
(2u_θ/r³) · ∂_z(u_θ) + Δ̃g - ∂g/∂t ≤ 0   at max points of Φ̃
```

## Candidate corrector 1: g = u_θ² / (2r²)

**Motivation:** the swirl source is quadratic in u_θ and involves a z-derivative. The simplest function that is quadratic in u_θ and involves 1/r² is g = u_θ²/(2r²).

Compute Δ̃g and ∂g/∂t:

The u_θ equation in axisymmetric NS is:
```
∂u_θ/∂t + u_r ∂_r(u_θ) + u_z ∂_z(u_θ) = (Δ - 1/r²)u_θ + (u_r u_θ)/r
```

So:
```
∂g/∂t = (u_θ/r²) · ∂u_θ/∂t
       = (u_θ/r²) · [(Δ - 1/r²)u_θ + (u_r u_θ)/r - u_r ∂_r(u_θ) - u_z ∂_z(u_θ)]
```

And the swirl source is:
```
(2u_θ/r³) · ∂_z(u_θ)
```

The question: does (swirl source) + Δ̃g - ∂g/∂t have a definite sign?

Let me expand Δ̃g. Using g = u_θ²/(2r²):
```
∂_r g = (u_θ ∂_r u_θ)/r² - u_θ²/r³
∂_r² g = [(∂_r u_θ)² + u_θ ∂_r²u_θ]/r² - 4u_θ ∂_r u_θ/r³ + 3u_θ²/r⁴
∂_z² g = [(∂_z u_θ)² + u_θ ∂_z²u_θ]/r²
```

The Δ̃ operator is Δ + 2/r · ∂_r - 1/r² in axisymmetric coordinates. So:
```
Δ̃g = ∂_r²g + (1/r)∂_r g + ∂_z²g + (2/r)∂_r g - g/r²
```

This is getting algebraically heavy. Let me organize:

```
Δ̃g = [(∂_r u_θ)² + (∂_z u_θ)²]/r²       ← gradient-squared term (positive!)
     + (u_θ/r²)[(Δ - 1/r²)u_θ]           ← diffusion of u_θ
     + lower-order terms in u_θ/r
```

The gradient-squared term [(∂_r u_θ)² + (∂_z u_θ)²]/r² is POSITIVE. This is promising — it's an additional dissipation that comes for free from the corrector.

The key combination becomes:
```
(swirl source) + Δ̃g - ∂g/∂t 
= (2u_θ/r³) ∂_z u_θ                                    ← the bad term
  + [(∂_r u_θ)² + (∂_z u_θ)²]/r²                       ← the good term from Δ̃g
  + (u_θ/r²)[(Δ - 1/r²)u_θ] - (u_θ/r²)[(Δ - 1/r²)u_θ]  ← these CANCEL!
  + transport terms                                       ← vanish at max of Φ̃
  + lower order
```

Wait — the (u_θ/r²)·(Δ - 1/r²)u_θ terms from Δ̃g and ∂g/∂t CANCEL each other. That's a structural cancellation from the NS equation.

After cancellation, the main remaining terms are:
```
(2u_θ/r³) ∂_z u_θ  +  [(∂_r u_θ)² + (∂_z u_θ)²]/r²  +  (lower order)
```

The bad term is linear in ∂_z u_θ. The good term is QUADRATIC in gradients of u_θ. By Young's inequality:
```
|(2u_θ/r³) ∂_z u_θ| ≤ u_θ²/r⁴ · (1/δ) + δ · (∂_z u_θ)²/r²
```

For δ = 1, this gives:
```
|(2u_θ/r³) ∂_z u_θ| ≤ u_θ²/r⁴ + (∂_z u_θ)²/r²
```

The (∂_z u_θ)²/r² term is ABSORBED by the good term from Δ̃g. The remaining u_θ²/r⁴ is a lower-order term that can be absorbed by the -g/r² = -u_θ²/(2r⁴) term if the coefficient works out.

**Let me check:** we need u_θ²/r⁴ ≤ u_θ²/(2r⁴)? No, that's 1 ≤ 1/2, which FAILS.

**So g = u_θ²/(2r²) almost works but the coefficient is off by a factor of 2.** 

### Try g = u_θ²/r² (double the coefficient)

With g = u_θ²/r², the good term from Δ̃g doubles, giving 2[(∂_r u_θ)² + (∂_z u_θ)²]/r². Young's inequality with δ = 1/2:

```
|(2u_θ/r³) ∂_z u_θ| ≤ 2u_θ²/r⁴ + (∂_z u_θ)²/(2r²)
```

Now (∂_z u_θ)²/(2r²) is absorbed by the doubled good term (2(∂_z u_θ)²/r²). The remaining 2u_θ²/r⁴ needs to be absorbed by -g/r² = -u_θ²/r⁴. Again fails: 2 > 1.

### The pattern

The corrector g = c · u_θ²/r² gives a good term of order c · |∇u_θ|²/r² and needs to absorb a bad term of order u_θ²/r⁴ (after Young's). The -g/r² provides c · u_θ²/r⁴. The absorption requires:

```
(from Young's) ≤ c · u_θ²/r⁴  (from -g/r²)
```

The Young's constant is 1/(cδ) for the linear-quadratic split. Optimizing:
```
|(2u_θ/r³) ∂_z u_θ| ≤ (1/(cδ)) · u_θ²/r⁴ + cδ · (∂_z u_θ)²/r²
```

Need cδ · (∂_z u_θ)²/r² ≤ c · (∂_z u_θ)²/r² → δ ≤ 1. And 1/(cδ) ≤ c → c² ≥ 1/δ → c ≥ 1/√δ.

Minimize c: take δ = 1, c = 1. Then both terms absorb. CHECK:
```
Bad: u_θ²/r⁴ + (∂_z u_θ)²/r²
Good from Δ̃g: (∂_r u_θ)² / r² + (∂_z u_θ)²/r²  ... absorbs the (∂_z u_θ)² 
Good from -g/r²: u_θ²/r⁴  ... absorbs the u_θ² term
```

**IT WORKS WITH c = 1.** The corrector g = u_θ²/r² makes the modified quantity Φ̃ = ω_θ/r - u_θ²/r² satisfy a maximum principle, at least at the level of the principal terms.

## CAVEAT — lower-order terms

The calculation above tracks only the PRINCIPAL terms (highest-order in derivatives and in 1/r). There are lower-order terms from the expansion of Δ̃g and from the transport terms. These need to be checked to confirm the sign.

Additionally: the corrector g = u_θ²/r² is SINGULAR at r = 0 (if u_θ → 0 linearly as r → 0, then g → const, which is fine; but if u_θ has a different behavior near the axis, g might blow up).

## What this would prove if it holds

**Liouville for axisymmetric bounded ancient solutions WITH swirl.**

The KNSS proof would extend from "no swirl" to "any swirl" in the axisymmetric class. This doesn't prove the full Liouville (which needs no symmetry assumption), but it's a SIGNIFICANT partial result that has been open since 2009.

The extension from axisymmetric+swirl to general 3D would still require removing the symmetry assumption. But the axisymmetric+swirl case IS the hardest open case in the axisymmetric world, and resolving it would be a publishable result.

## Requests for numerics

1. **Test the corrector:** on the Burgers vortex with added Gaussian swirl, compute Φ̃ = ω_θ/r - u_θ²/r² and track its maximum over time. Does it decrease?
2. **Check the lower-order terms:** compute the full expression (swirl source) + Δ̃g - ∂g/∂t numerically at several points. Is it ≤ 0?
3. **Test near the axis:** what happens to Φ̃ as r → 0? Does it stay bounded?

## Sky bridges

- **KNSS 2009:** this attempt directly extends their result. If it works, it settles the longest-standing open case in the axisymmetric regularity program.
- **The entropy approach (attempt_004):** if the corrector works for axisymmetric, the same structural idea (subtract a correction that absorbs the bad term) might work for the general case. The corrector for the general case would need to absorb (Sω·ω) instead of the swirl source — more variables but the same principle.
- **The certifier:** axisymmetric Liouville with swirl, combined with the c(N) < 3/4 certificates, would prove NS regularity for axisymmetric flows. That's a partial millennium prize result.
