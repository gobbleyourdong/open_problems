# attempt_006 — Corrector Verification (Full Lower-Order Terms)

**Date:** 2026-04-10
**Track:** Theory (Even)
**Mountain:** 4 (KNSS extension)
**Status:** Rigorous verification of the corrector Φ̃ = ω_θ/r - u_θ²/r² from attempt_005.

## Goal

Attempt_005 showed the principal terms work. This attempt checks the FULL equation for Φ̃ including all lower-order terms, the axis behavior (r → 0), and the sign of the combined expression at maximum points.

## The full axisymmetric NS equations

In cylindrical coordinates (r, θ, z) with axial symmetry (∂/∂θ = 0), decompose u = u_r e_r + u_θ e_θ + u_z e_z. The NS equations are:

**Radial:**
```
∂u_r/∂t + u_r ∂_r u_r + u_z ∂_z u_r - u_θ²/r = -(1/ρ)∂_r p + ν(Δu_r - u_r/r²)
```

**Azimuthal (swirl):**
```
∂u_θ/∂t + u_r ∂_r u_θ + u_z ∂_z u_θ + u_r u_θ/r = ν(Δu_θ - u_θ/r²)
```

**Axial:**
```
∂u_z/∂t + u_r ∂_r u_z + u_z ∂_z u_z = -(1/ρ)∂_z p + νΔu_z
```

**Continuity:**
```
∂_r u_r + u_r/r + ∂_z u_z = 0
```

where Δ = ∂_r² + (1/r)∂_r + ∂_z² is the axisymmetric Laplacian.

The angular vorticity is:
```
ω_θ = ∂_z u_r - ∂_r u_z
```

## The equation for Φ = ω_θ/r

Define Φ = ω_θ/r. The FULL equation (derived from the vorticity equation) is:

```
∂Φ/∂t + u_r ∂_r Φ + u_z ∂_z Φ = ν L̃ Φ + (2u_θ/(r²)) · ∂_z(u_θ/r)
```

where L̃ = ∂_r² + (3/r)∂_r + ∂_z² is the modified Laplacian (note: 3/r, not 1/r — this comes from the 1/r factor in Φ = ω_θ/r).

**Note on the source term:** I need to be more careful. Let me re-derive.

The vorticity equation for ω_θ in the axisymmetric case:
```
∂ω_θ/∂t + u_r ∂_r ω_θ + u_z ∂_z ω_θ - u_r ω_θ/r = ν(Δω_θ - ω_θ/r²) + ∂_z(u_θ²/r)
```

The source term is ∂_z(u_θ²/r), which comes from the centrifugal acceleration.

Dividing by r:
```
∂Φ/∂t + u_r ∂_r Φ + u_z ∂_z Φ = ν L̃ Φ + (1/r) ∂_z(u_θ²/r)
```

where L̃ Φ = (1/r)(Δ - 1/r²)(rΦ) = ∂_r²Φ + (3/r)∂_r Φ + ∂_z²Φ.

Now the source term: (1/r) ∂_z(u_θ²/r) = (2u_θ ∂_z u_θ)/(r²).

So:
```
∂Φ/∂t + u_r ∂_r Φ + u_z ∂_z Φ = ν L̃ Φ + 2u_θ ∂_z u_θ / r²     ... (A)
```

## The equation for g = u_θ²/r²

From the u_θ equation:
```
∂u_θ/∂t = ν(Δu_θ - u_θ/r²) - u_r ∂_r u_θ - u_z ∂_z u_θ - u_r u_θ/r
```

Compute ∂g/∂t = (2u_θ/r²) · ∂u_θ/∂t:
```
∂g/∂t = (2u_θ/r²)[ν(Δu_θ - u_θ/r²) - u_r ∂_r u_θ - u_z ∂_z u_θ - u_r u_θ/r]
```

Compute L̃ g. This requires computing ∂_r²g + (3/r)∂_r g + ∂_z²g where g = u_θ²/r².

Let h = u_θ/r (the angular velocity). Then g = h² · 1 and u_θ = rh.

Actually, let me use the substitution Γ = r u_θ (the circulation). Then u_θ = Γ/r and g = Γ²/r⁴.

The Γ equation: from the u_θ equation,
```
∂(Γ/r)/∂t + ... = ν(Δ(Γ/r) - Γ/r³) - ...
```

This is getting complicated. Let me just compute the combination directly.

## Direct computation of the Φ̃ equation

Define Φ̃ = Φ - g = ω_θ/r - u_θ²/r². The equation for Φ̃ is:

```
∂Φ̃/∂t + u_r ∂_r Φ̃ + u_z ∂_z Φ̃ = ν L̃ Φ̃ + S
```

where the source S is:
```
S = [2u_θ ∂_z u_θ / r²]                              ... from the Φ equation (A)
  - ∂g/∂t - u_r ∂_r g - u_z ∂_z g + ν L̃ g           ... from subtracting the g equation
```

Expanding ∂g/∂t + u_r ∂_r g + u_z ∂_z g using the u_θ equation:

```
∂g/∂t + u_r ∂_r g + u_z ∂_z g = (2u_θ/r²)(∂u_θ/∂t + u_r ∂_r u_θ + u_z ∂_z u_θ)
                                  + u_θ² · ∂_t(1/r²) + ...
```

Wait — r doesn't depend on t in Eulerian coordinates. So ∂(1/r²)/∂t = 0.

```
∂g/∂t + u_r ∂_r g + u_z ∂_z g 
= (2u_θ/r²)(∂u_θ/∂t + u_r ∂_r u_θ + u_z ∂_z u_θ) + u_r · (-2u_θ²/r³)
```

Wait, I need to be more careful with the chain rule:
```
∂_r g = ∂_r(u_θ²/r²) = 2u_θ(∂_r u_θ)/r² - 2u_θ²/r³
∂_z g = 2u_θ(∂_z u_θ)/r²
```

So:
```
u_r ∂_r g + u_z ∂_z g = (2u_θ/r²)(u_r ∂_r u_θ + u_z ∂_z u_θ) - 2u_r u_θ²/r³
```

And:
```
∂g/∂t = (2u_θ/r²) ∂u_θ/∂t
```

Using the u_θ equation to substitute ∂u_θ/∂t + u_r ∂_r u_θ + u_z ∂_z u_θ = ν(Δu_θ - u_θ/r²) - u_r u_θ/r:

```
∂g/∂t + u_r ∂_r g + u_z ∂_z g 
= (2u_θ/r²)[ν(Δu_θ - u_θ/r²) - u_r u_θ/r] - 2u_r u_θ²/r³
= (2νu_θ/r²)(Δu_θ - u_θ/r²) - 2u_r u_θ²/r³ - 2u_r u_θ²/r³
= (2νu_θ/r²)(Δu_θ - u_θ/r²) - 4u_r u_θ²/r³
```

Now compute ν L̃ g:
```
L̃ g = ∂_r²g + (3/r)∂_r g + ∂_z²g
```

I need ∂_r²g and ∂_z²g:
```
∂_r g = 2u_θ(∂_r u_θ)/r² - 2u_θ²/r³

∂_r²g = 2(∂_r u_θ)²/r² + 2u_θ(∂_r²u_θ)/r² - 8u_θ(∂_r u_θ)/r³ + 6u_θ²/r⁴

∂_z²g = 2(∂_z u_θ)²/r² + 2u_θ(∂_z²u_θ)/r²

(3/r)∂_r g = 6u_θ(∂_r u_θ)/r³ - 6u_θ²/r⁴
```

Sum:
```
L̃ g = 2[(∂_r u_θ)² + (∂_z u_θ)²]/r²                     ← gradient-squared (GOOD, ≥ 0)
     + (2u_θ/r²)[∂_r²u_θ + ∂_z²u_θ]                      ← ≈ (2u_θ/r²)Δu_θ
     - 2u_θ(∂_r u_θ)/r³                                    ← cross term
     + 0                                                    ← the 6u_θ²/r⁴ terms CANCEL
```

More precisely: (2u_θ/r²)[∂_r²u_θ + (1/r)∂_r u_θ + ∂_z²u_θ] = (2u_θ/r²)Δu_θ, and the remaining terms give -2u_θ(∂_r u_θ)/r³ + (2u_θ/r²)(1/r)∂_r u_θ - 2u_θ(∂_r u_θ)/r³ ... let me recount.

Actually:
```
L̃ g = 2|∇u_θ|²/r² + (2u_θ/r²)Δu_θ - 2u_θ(∂_r u_θ)/r³
```

where |∇u_θ|² = (∂_r u_θ)² + (∂_z u_θ)² and Δu_θ = ∂_r²u_θ + (1/r)∂_r u_θ + ∂_z²u_θ.

So:
```
ν L̃ g = 2ν|∇u_θ|²/r² + (2νu_θ/r²)Δu_θ - 2νu_θ(∂_r u_θ)/r³
```

## The full source term S

```
S = [2u_θ ∂_z u_θ / r²]                                            ← from Φ equation
  - [(2νu_θ/r²)(Δu_θ - u_θ/r²) - 4u_r u_θ²/r³]                  ← from -(Dg/Dt)
  + [2ν|∇u_θ|²/r² + (2νu_θ/r²)Δu_θ - 2νu_θ(∂_r u_θ)/r³]       ← from +ν L̃ g
```

Simplify: the (2νu_θ/r²)Δu_θ terms CANCEL (one from -Dg/Dt, one from +L̃ g, same sign? Let me check.)

From -(Dg/Dt): -(2νu_θ/r²)(Δu_θ - u_θ/r²) = -(2νu_θ/r²)Δu_θ + 2νu_θ²/r⁴
From +ν L̃ g: +(2νu_θ/r²)Δu_θ

These cancel! Left with:
```
S = 2u_θ(∂_z u_θ)/r²           ← the original bad term
  + 2νu_θ²/r⁴                  ← from the -u_θ/r² in Δu_θ - u_θ/r²
  + 4u_r u_θ²/r³               ← from the transport correction
  + 2ν|∇u_θ|²/r²               ← the GOOD gradient-squared term
  - 2νu_θ(∂_r u_θ)/r³          ← cross term
```

Now apply Young's inequality to the bad term:
```
|2u_θ(∂_z u_θ)/r²| ≤ u_θ²/r² · (1/δ) + δ · (∂_z u_θ)²/r²
```

Take δ = ν (so we can absorb into the good term 2ν(∂_z u_θ)²/r²):
```
|2u_θ(∂_z u_θ)/r²| ≤ u_θ²/(νr²) + ν(∂_z u_θ)²/r²
```

The ν(∂_z u_θ)²/r² is absorbed by 2ν(∂_z u_θ)²/r² from the good term. Left:

```
S ≤ u_θ²/(νr²) + 2νu_θ²/r⁴ + 4u_r u_θ²/r³ + ν(∂_r u_θ)²/r² - 2νu_θ(∂_r u_θ)/r³
```

Apply Young to the cross term -2νu_θ(∂_r u_θ)/r³:
```
|-2νu_θ(∂_r u_θ)/r³| ≤ νu_θ²/r⁴ + ν(∂_r u_θ)²/r²
```

The ν(∂_r u_θ)²/r² is absorbed by the remaining ν(∂_r u_θ)²/r² from the good term. Left:

```
S ≤ u_θ²/(νr²) + 3νu_θ²/r⁴ + 4u_r u_θ²/r³
```

Factor: S ≤ (u_θ²/r²)[1/ν + 3ν/r² + 4u_r/r]

For bounded ancient solutions: |u_r| ≤ M, so 4u_r/r could be as large as 4M/r (positive or negative). The term 1/ν is a constant. So:

```
S ≤ (u_θ²/r²) · [1/ν + 3ν/r² + 4M/r]
```

**This is positive.** The source S is bounded above by a POSITIVE expression proportional to u_θ²/r².

## THE VERDICT

**The corrector Φ̃ = ω_θ/r - u_θ²/r² does NOT satisfy a maximum principle** in the full equation. The lower-order terms produce a positive source proportional to u_θ²/r² · [1/ν + 3ν/r² + 4M/r].

The principal-term cancellation from attempt_005 was real (the gradient-squared terms DO absorb the main bad term via Young's), but the lower-order terms — specifically the 1/ν constant and the 4u_r/r transport term — survive and have the wrong sign.

## What this means

The corrector idea is NOT dead — it's the right STRUCTURE. The specific function g = u_θ²/r² is close but leaves a remainder of order u_θ²/r². A more refined corrector might absorb this:

**Option A:** g = u_θ²/r² + c₁ u_θ²/r⁴ + c₂ (∂_r u_θ)² · h(r) + ...

Higher-order corrections might cancel the remaining terms. But each correction introduces new cross terms. This is an algebraic arms race that may or may not converge.

**Option B:** g = F(u_θ²/r²) for some nonlinear function F (e.g., F(s) = s + s²). The nonlinearity in F might absorb the lower-order terms. This is the approach used in some maximum-principle constructions for reaction-diffusion equations.

**Option C:** accept the positive source and use a GRONWALL argument instead of a pure maximum principle. If S ≤ C(M, ν) · g, then max(Φ̃) grows at most exponentially. Combined with the ancient condition (bounded for all t ≤ 0), exponential growth backward is impossible → Φ̃ is bounded → ω_θ/r is controlled by u_θ²/r² → this constrains the vorticity → might lead to Liouville via a bootstrap.

## Option C — the Gronwall bootstrap (most promising)

If S ≤ C · g = C · u_θ²/r², then the equation for Φ̃ is:
```
∂Φ̃/∂t + transport = ν L̃ Φ̃ + S ≤ ν L̃ Φ̃ + C · g
```

But g = u_θ²/r² ≤ M²/r² (bounded). And Φ̃ = Φ - g, so Φ ≤ Φ̃ + g. If we can show max(Φ̃) is bounded (using the ancient condition + the fact that S ≤ C · g ≤ C · M²/r² which is INTEGRABLE on R³), then Φ = ω_θ/r is controlled.

The ancient condition is crucial here: for forward-in-time solutions, the Gronwall bound gives exponential growth. For backward-in-time (ancient), the exponential growth goes backward → the solution must have been EXPONENTIALLY SMALL in the distant past → combined with boundedness → Φ̃ must be constant → Φ̃ = 0.

**This is the backward decay argument from attempt_002, applied to Φ̃ instead of to u directly!** The corrector doesn't need to give a pure maximum principle — it just needs to give a Gronwall bound, and the ancient condition does the rest.

## The chain

1. Φ̃ = ω_θ/r - u_θ²/r² satisfies ∂Φ̃/∂t ≤ ν L̃ Φ̃ + C(M,ν) · u_θ²/r²
2. u_θ is bounded (|u_θ| ≤ M), so the source is bounded: S ≤ C · M²/r²
3. By the maximum principle with bounded source: max Φ̃(t) ≤ max Φ̃(t₀) + C · (t - t₀) for t > t₀
4. For an ancient solution, take t₀ → -∞: max Φ̃(t) ≤ max Φ̃(t₀) + C · (t - t₀) → -∞ (contradicts Φ̃ bounded)

Wait — step 4 doesn't work because the linear growth gives max Φ̃(t) ≤ max Φ̃(t₀) + C(t - t₀), and taking t₀ → -∞ gives max Φ̃(t) ≤ lim_{t₀→-∞} [max Φ̃(t₀) + C(t - t₀)] which is +∞ - ∞, indeterminate.

**Need a better bound on the source.** The source S ≤ C · M²/r² decays in r but is constant in t. A t-dependent bound would help.

Alternatively: the source is S ≤ C · g, and g = u_θ²/r² ≤ M²/r² is bounded but INDEPENDENT of Φ̃. So the equation for max Φ̃ is:

```
d/dt max Φ̃ ≤ C · M²/r²|_{max point}
```

If the maximum of Φ̃ occurs at a point where r is LARGE (away from the axis), then C · M²/r² is small and the maximum grows slowly. The question is whether the maximum can move to r → 0 (where the source is large).

For bounded ancient solutions, the smoothness near the axis (u_θ ~ r as r → 0, so g ~ const as r → 0) should prevent the maximum from reaching r = 0. This requires a separate argument about the axis behavior of Φ̃.

## Status

The corrector Φ̃ = ω_θ/r - u_θ²/r² does NOT give a clean maximum principle (attempt_005 was wrong at the lower-order level). BUT the Gronwall structure combined with the ancient condition might still work via the backward decay argument.

The chain needs: (1) Gronwall bound on Φ̃ with source ≤ C · g, (2) ancient condition forces backward growth → Φ̃ bounded → Φ bounded → vorticity controlled → bootstrap to Liouville.

**This is attempt_007's territory.** Flagging it.

## Updated assessment

The corrector is the RIGHT IDEA but needs the Gronwall bootstrap, not a pure maximum principle. The algebra is one step deeper than attempt_005 suggested. The result, if it works, would be: Liouville for axisymmetric bounded ancient NS, with swirl, via Φ̃ + ancient backward decay.
