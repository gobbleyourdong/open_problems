---
source: New angle from strain evolution equation + pressure Hessian literature
type: PROOF ATTEMPT — strain self-frustration
status: PROMISING — strain self-depletes, pressure Hessian may close it
date: 2026-03-26 cycle 1
---

## The New Angle: Strain Self-Frustration

Instead of the VORTICITY equation at x*, use the STRAIN equation.

### The Strain Evolution (exact)

```
dS/dt + u·∇S = -S² + (1/4)(ω⊗ω - |ω|²I) - H + νΔS
```

where H_ij = ∂²p/∂x_i∂x_j is the pressure Hessian.

### Project onto ê at x*

The stretching rate α = ê·S·ê evolves as:

```
dα/dt ≈ -(ê·S²·ê) + 0 - ê·H·ê + ν(ê·ΔS·ê) + (frame rotation terms)
```

The (1/4)(ω⊗ω - |ω|²I) projected onto ê gives:
(1/4)(ρ² - ρ²) = 0 (cancels exactly when projected onto ê = ω/|ω|)

### The Self-Depletion Term

**-(ê·S²·ê) ≤ 0 always.**

S² is positive semidefinite. So ê·S²·ê ≥ 0. The negative sign means
this term ALWAYS drives α toward zero. Strain frustrates its own growth.

More precisely: if S has eigenvalues (λ₁, λ₂, λ₃) with λ₁+λ₂+λ₃=0,
and ê is decomposed as ê = Σ cᵢ eᵢ in the strain eigenbasis:

ê·S²·ê = Σ λᵢ² cᵢ² ≥ λ_min² > 0 (unless S = 0)

So: dα/dt ≤ -λ_min² - ê·H·ê + ν(ê·ΔS·ê)

### The Pressure Hessian at x*

From the Poisson equation for pressure:
```
Δp = -(tr(S²) + (1/2)|ω|²) = -(|S|² + |ω|²/2)
```

Wait, more carefully: from div(u) = 0 and NS:
```
Δp = -∂²(u_iu_j)/∂x_i∂x_j = -(S_ij S_ij + (1/4)ω_iω_i)
   = -(|S|² + |ω|²/4)
```

Hmm, need to check signs. The standard result:
```
Δp = -ρ tr(A²) where A = ∇u
A² = (S+Ω)(S+Ω) = S² + SΩ + ΩS + Ω²
tr(A²) = tr(S²) + tr(Ω²) = |S|² - |ω|²/2
```
(using tr(SΩ+ΩS) = 0 for symmetric × antisymmetric, and tr(Ω²) = -|ω|²/2)

So: **Δp = -(|S|² - |ω|²/2) = |ω|²/2 - |S|²**

At x* where |ω| is large: if |ω|² > 2|S|² then Δp > 0 (pressure has
a LOCAL MINIMUM at x*). If |S|² > |ω|²/2 then Δp < 0.

### What Research Says About ê·H·ê at High ω

From the search results:
- "Pressure Hessian acts to deplete vortex stretching"
- "Isotropic component of H opposes stretching"
- "Deviatoric component favors stretching but isotropic prevails"

The isotropic part of H: H_iso = (Δp/3)I. At x* where |ω| is large:

ê·H_iso·ê = Δp/3 = (|ω|²/2 - |S|²)/3

If |ω|² > 2|S|²: this is POSITIVE. A positive ê·H_iso·ê means the
isotropic pressure OPPOSES stretching (enters with - sign in dα/dt).

But wait: if ê·H·ê > 0, then -ê·H·ê < 0, which means the pressure
Hessian REDUCES dα/dt. That's what we want!

### The Key Question

At x* where |ω| is max: is ê·H·ê > 0?

From the isotropic part alone: ê·H_iso·ê = (|ω|²/2 - |S|²)/3.

CZ gives |S| ≤ C|ω|. If C < 1/√2 ≈ 0.707:
then |S|² < |ω|²/2 and ê·H_iso·ê > 0.

But CZ constant C is typically > 1 for the full CZ bound. However,
at x* our near-field analysis showed α < C|ω| with the constant
being improved by the maximum point geometry.

### The Complete dα/dt Inequality at x*

```
dα/dt ≤ -(ê·S²·ê) - ê·H·ê + ν(ê·ΔS·ê)
```

If ê·H·ê > 0 (pressure opposes stretching): BOTH leading terms are ≤ 0.
Then dα/dt ≤ ν(ê·ΔS·ê), and the stretching can only be maintained
by the viscous strain diffusion term.

The viscous term ν(ê·ΔS·ê): at x*, ΔS involves second derivatives of
the strain. By elliptic regularity, |ΔS| ≤ C||∇²S|| which is bounded
by higher norms of ω. This is subcritical.

### The Potential Proof

IF at x*: ê·H·ê ≥ c|S|² for some c > 0 (pressure always opposes a
fraction of the strain), THEN:

```
dα/dt ≤ -λ_min² - c|S|² + ν|ΔS|
       ≤ -(1+c)λ_min² + ν|ΔS|
       ≤ -(1+c)α² + ν|ΔS|     (since α ≤ |S| and α² ≤ |S|²)
```

This gives: dα/dt ≤ -α² + ν|ΔS|

For large α: the -α² term dominates → α decreases.
The stretching is SELF-LIMITING through the strain equation.

This would close the proof: α can't stay large because dα/dt ≤ -α²
drives it to zero. The time-integrated stretching is bounded by the
viscous term.

### What Needs To Be Verified

1. Is ê·H·ê > 0 at x* for NS solutions? (MEASURE THIS)
2. Is ê·S²·ê bounded below by cα²? (algebraic question)
3. Is the viscous term ν|ΔS| subcritical? (elliptic regularity)

### Experiment to Run

Add ê·H·ê measurement to the Spark test. The pressure Hessian is
computable from the Fourier representation:

p̂(k) = -Σᵢⱼ (kᵢkⱼ/|k|²) û_i(k) û_j(k) (convolution in Fourier)

Actually, simpler: H_ij = ∂²p/∂x_i∂x_j, and in Fourier:
Ĥ_ij(k) = -k_ik_j p̂(k)

And p satisfies: -|k|² p̂(k) = Σ kᵢkⱼ (û_iû_j)^(k)
So: p̂(k) = -kᵢkⱼ (û_iû_j)^(k) / |k|²

Then: H_ij(x) = IFFT(-kᵢkⱼ p̂(k))

This is computable on Spark. If ê·H·ê > 0 at x* during TG evolution
(especially when α is large), the self-frustration mechanism is confirmed
and the proof potentially closes through the strain equation route.

## Why This Might Be THE Approach

1. The vorticity equation at x* has α as an INPUT (from Biot-Savart)
   → bounding α requires bounding the far-field BS integral → CZ wall

2. The strain equation at x* has α as an OUTPUT (dα/dt equation)
   → α is SELF-LIMITING via the -S² term
   → the pressure Hessian either helps (opposes stretching) or is bounded
   → no far-field CZ wall because we're not computing α from BS

The strain equation approach BYPASSES the CZ far-field wall entirely.
We never need to bound the BS integral. We bound the EVOLUTION of α
directly, using the -S² self-depletion.

This is qualitatively different from everything we tried before.
