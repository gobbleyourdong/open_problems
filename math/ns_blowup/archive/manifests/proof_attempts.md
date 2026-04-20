# Proof Attempts — Viscous Enhancement of Interior Blowup

## Target Lemma
For the Hou 2022 IC u₁(0,r,z) = A(1-r²)¹⁸ sin(2πz)/(1+12.5sin²(πz)):
Adding viscosity ν > 0 does NOT prevent finite-time blowup.

## Attempt 1: Direct sign analysis of Δ₃u₁ at r=0

u₁ = A(1-r²)¹⁸ f(z) where f(z) = sin(2πz)/(1+12.5sin²(πz))

At r=0:
  ∂ᵣu₁ = -36Ar(1-r²)¹⁷f(z) → 0
  ∂ᵣᵣu₁ = -36A[(1-r²)¹⁶((1-r²) - 34r²)]f(z) → -36Af(z)
  (3/r)∂ᵣu₁ → 3·∂ᵣᵣu₁ = -108Af(z)  [L'Hôpital, 4× rule]
  Wait: L'Hôpital gives (3/r)∂ᵣ → 3∂ᵣᵣ, so total = ∂ᵣᵣ + 3∂ᵣᵣ = 4∂ᵣᵣ

  Δ₃u₁|_{r=0} = 4·(-36A)f(z) + Af''(z) = -144Af(z) + Af''(z)

Since f(z) > 0 near z=0 and |f''| << 144f for the given profile:
  Δ₃u₁|_{r=0} < 0

Therefore ν·Δ₃u₁ < 0 at r=0: diffusion DAMPS u₁ at the axis.

RESULT: Direct damping at r=0. Cannot prove enhancement by sign analysis.
STATUS: ✗ FAILED — the enhancement mechanism is INDIRECT through Poisson coupling.

## Attempt 2: Enstrophy growth rate comparison

The enstrophy identity: dE/dt = S - νP

For Euler (ν=0): dE/dt = S_euler
For NS (ν>0):   dE/dt = S_ns - νP

If blowup is enhanced: S_ns - νP > S_euler
Therefore: S_ns > S_euler + νP

Question: does the viscous modification of the velocity field increase S?

S = ∫ ω·(ω·∇)u dx

The stretching S depends on the ALIGNMENT between ω and the strain tensor ∇u.
Viscosity changes u (by smoothing), which changes ∇u, which changes S.

The question reduces to: does viscous smoothing improve vortex-strain alignment?

For the (1-r²)¹⁸ IC at r=0: viscosity broadens the vortex core.
A broader core means the strain field (from the Poisson-reconstructed velocity)
acts on a larger volume of aligned vorticity.

This is plausible but NOT a proof. It's a physical argument.

RESULT: Identified the mechanism (alignment enhancement via broadening) but
cannot close the inequality rigorously without bounding the Poisson kernel.
STATUS: ✗ PARTIAL — mechanism identified, quantification missing.

## Attempt 3: ODE comparison for ω₁ at r=0

At r=0, the ω₁ equation simplifies (uʳ=0 by symmetry):
  ∂ₜω₁ = uᶻ∂zω₁ + 2u₁u₁,z + ν·4∂ᵣᵣω₁ + ν∂zzω₁

The stretching term 2u₁u₁,z drives growth.
The diffusion term ν(4∂ᵣᵣω₁ + ∂zzω₁) acts on ω₁.

At t=0: ω₁=0, so ∂ᵣᵣω₁=0 and diffusion of ω₁ is zero.
The FIRST step creates ω₁ from the stretching of u₁.

After one step: ω₁ ~ δt · 2u₁u₁,z
The diffusion of this NEW ω₁ depends on its spatial structure.

For u₁ concentrated at r=0 (via (1-r²)¹⁸):
  u₁u₁,z is also concentrated at r=0.
  Therefore ω₁ starts concentrated at r=0.
  Δ₃ω₁ at r=0 will be NEGATIVE (radial maximum → Laplacian negative)
  → ν·Δ₃ω₁ < 0 → diffusion damps ω₁ too.

But the POISSON coupling changes ψ₁ (and hence uᶻ = 2ψ₁ + r·ψ₁,r),
which changes the advective term uᶻ∂zω₁, which can CONCENTRATE ω₁
faster than diffusion can spread it.

RESULT: The direct terms (stretching, diffusion) both behave predictably.
The enhancement comes from the Poisson-mediated feedback on the advection.
STATUS: ✗ PARTIAL — again, the Poisson coupling is the key.

## Insight after 3 attempts

The enhancement is NOT in any single term. It's in the CLOSED LOOP:
  ω₁ → [Poisson] → ψ₁ → [velocity] → uᶻ → [advection] → ω₁

Viscosity modifies ALL parts of this loop simultaneously.
The loop gain with viscosity > loop gain without.
Proving this requires bounding the full loop, not individual terms.

This is why Chen-Hou needed 200 pages. The loop analysis IS the proof.

## Possible simpler approach: energy method

Instead of tracking individual terms, track a FUNCTIONAL:
  F(t) = ∫ w(r,z) · ω₁² dr dz

for some weight function w(r,z) chosen to make dF/dt > c·F^α with α > 1.

If such w exists, blowup follows from ODE comparison (our Lemma 3).

The weight w must be chosen so that:
  - The stretching contribution to dF/dt is positive
  - The diffusion contribution is bounded by the stretching
  - The weight suppresses boundary terms

This is exactly the weighted energy estimate approach of Chen-Hou.
The weight IS the 200-page content.

Can PySR find the weight? That's the question.
