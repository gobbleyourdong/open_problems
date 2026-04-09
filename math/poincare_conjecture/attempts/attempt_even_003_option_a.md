# NS Even 003 — Option (a): Make ωSω Fit a Perfect Square

**Date**: 2026-04-07
**Instance**: Even (Odd role on NS)

## The Idea

In Perelman: dW/dt = 2τ∫|Ric + Hess(f) - g/(2τ)|² u dV ≥ 0.

The Ricci tensor (which contains the nonlinear curvature) is INSIDE the
square. It doesn't appear as a leftover. The Hess(f) and g/(2τ) are
"conjugate corrections" that make everything fit.

**For NS**: can we define a tensor T such that dW_NS/dt = ∫|T|² u dx,
with the vortex stretching INSIDE T, not as a leftover?

## The Vorticity Equation as the Algebraic Constraint

The vorticity equation: ∂ω/∂t = νΔω + (ω·∇)u - (u·∇)ω

In Perelman's setup, the Ricci flow equation ∂g/∂t = -2Ric IS the
gradient of the F-entropy. The equation itself generates the square.

**Key question**: Is the NS vorticity equation the gradient of ANYTHING?

### The Energy Functional
E = ∫ |u|²/2 dx. Then: dE/dt = -ν∫|∇u|² dx ≤ 0.
NS is DISSIPATIVE for energy. But E is not the right functional (no square).

### The Enstrophy Functional
Ω = ∫ |ω|²/2 dx. Then: dΩ/dt = -ν∫|∇ω|² dx + ∫ ωᵢSᵢⱼωⱼ dx.
The stretching appears explicitly. NOT a gradient flow.

### The Helicity Functional
H = ∫ u·ω dx. Then: dH/dt = -2ν∫ ω·(∇×ω) dx.
Helicity is conserved for Euler (ν=0) and dissipated for NS.
No stretching term — but doesn't control |ω|.

## The Gradient Flow Perspective

Ricci flow IS a gradient flow: ∂g/∂t = -∇F(g) (Perelman).
This is WHY dF/dt = -||∇F||² ≤ 0 (F decreases = W increases).

NS is NOT a gradient flow. It's HAMILTONIAN (Euler) + DISSIPATION (viscosity):
  ∂u/∂t = (Euler part) + νΔu

The Euler part preserves energy. The viscosity dissipates it.
No functional F has ∂u/∂t = -∇F(u) for NS.

**This is the FUNDAMENTAL algebraic obstruction.**

Ricci flow: gradient → perfect square → monotone W. AUTOMATIC.
NS: not gradient → no automatic square → stretching is a leftover.

## Can We MAKE It a Gradient Flow?

### Idea 1: Change Variables
Write u in terms of a "potential" ψ such that the NS equation
for ψ IS a gradient flow. Example: stream function in 2D.

In 2D: u = ∇⊥ψ, ω = -Δψ. The vorticity equation becomes:
  ∂(-Δψ)/∂t = νΔ²ψ + J(ψ, Δψ)

where J is the Jacobian. The bilinear J term is NOT a gradient.
Still not a gradient flow. The 3D case is worse (no stream function).

### Idea 2: Add a Correction Term
Find a functional G(ω) such that:
  ∂ω/∂t = -∇G(ω) + (remainder)

where the remainder is "small" or "antisymmetric" (doesn't affect dG/dt).

The viscous term: -∇(ν∫|∇ω|²/2) = νΔω. This IS a gradient.
The stretching: (ω·∇)u is NOT obviously a gradient.
The advection: -(u·∇)ω is antisymmetric (transport, preserves all norms).

So: ∂ω/∂t = -∇G + (stretching) + (antisymmetric advection)

The advection is harmless (it doesn't change ∫|ω|² or any L^p norm).
The stretching is the problem. If stretching = ∇H for some H:
  ∂ω/∂t = -∇(G - H) + (antisymmetric)
  → gradient flow → perfect square → monotone entropy!

**Is (ω·∇)u a gradient of something?**

(ω·∇)u = ω_j ∂u_i/∂x_j. In terms of ω only (via Biot-Savart):
(ω·∇)u = ω_j ∂(K*ω)_i/∂x_j = ω_j (∂K/∂x_j * ω)_i

This is a BILINEAR NONLOCAL operator applied to ω. It's the Fréchet
derivative of the Biot-Savart operator applied in the ω-direction.

For this to be a gradient: need ∂/∂ω [(ω·∇)u] to be SYMMETRIC.
The Fréchet derivative of (ω·∇)(K*ω) with respect to ω is:

δ[(ω·∇)(K*ω)]/δω · h = (h·∇)(K*ω) + (ω·∇)(K*h)

This is NOT symmetric in h and ω (the first term has h acting on K*ω,
the second has ω acting on K*h). So (ω·∇)u is NOT a gradient.

**The stretching is algebraically NOT a gradient. Option (a) fails
in the direct sense.** The NS vorticity equation cannot be written
as a gradient flow, period.

## The Partial Rescue: PROJECTED Gradient Flow

Even though the full NS is not gradient, the DISSIPATION PART is:

  ∂ω/∂t = νΔω + (non-gradient terms)

If we can show: the non-gradient terms are ORTHOGONAL to the gradient
direction (in L² or some weighted space), then:

  dG/dt = ⟨-∇G, ∂ω/∂t⟩ = ⟨-∇G, νΔω⟩ + ⟨-∇G, stretching + advection⟩

If the second inner product is ≤ 0 (the non-gradient part doesn't increase G):
  dG/dt ≤ ⟨-∇G, νΔω⟩ = -ν||∇G||² ≤ 0 → G decreases → monotonicity!

**This would work if**: ⟨∇G, (ω·∇)u⟩ ≤ 0 for the right G.

## What G to Choose?

If G = ∫ |ω|²/2 dx: ∇G = ω.
  ⟨ω, (ω·∇)u⟩ = ∫ ωᵢωⱼSᵢⱼ dx = ∫ ωSω dx  (the stretching!)

We need this to be ≤ 0. But ωSω can be POSITIVE. So G = enstrophy doesn't work.

If G = ∫ |ω|^p/p dx for p > 2: ∇G = |ω|^{p-2} ω.
  ⟨|ω|^{p-2} ω, (ω·∇)u⟩ = ∫ |ω|^{p-2} ωSω dx

For large p: this weights the stretching by |ω|^{p-2}, amplifying it
at high vorticity. WORSE, not better.

If G = -∫ log(1 + |ω|²) dx: ∇G = -2ω/(1+|ω|²).
  ⟨-2ω/(1+|ω|²), (ω·∇)u⟩ = -2 ∫ ωSω/(1+|ω|²) dx

This DIVIDES by (1+|ω|²), suppressing the stretching at high vorticity!
If |ωSω| ≤ C|ω|²: then |ωSω/(1+|ω|²)| ≤ C (bounded). And if the
diffusion term gives something of order |∇ω|²/(1+|ω|²) ~ 1/|ω|² (large),
then for large |ω| the diffusion dominates.

**This is promising.** The logarithmic functional G = -∫ log(1+|ω|²) dx
naturally TAMES the stretching by dividing by (1+|ω|²).

## The Log-Enstrophy Functional

Define: G = ∫ log(1 + |ω|²) dx (positive, grows with vorticity)

dG/dt = ∫ 2ω·(∂ω/∂t) / (1+|ω|²) dx
      = 2ν ∫ ω·Δω/(1+|ω|²) dx + 2 ∫ ωSω/(1+|ω|²) dx - (advection = 0)

The diffusion term: ∫ ω·Δω/(1+|ω|²) dx = -∫ |∇ω|²/(1+|ω|²) dx + (lower order)
  (integration by parts, with correction from ∇(1/(1+|ω|²)))

The stretching: ∫ ωSω/(1+|ω|²) dx ≤ C (bounded if |S| ≤ C'|ω| from Biot-Savart)

**If diffusion term ~ -∫ |∇ω|²/(1+|ω|²) dx = -Ω₁ (a kind of "log-dissipation")
and stretching ≤ C (bounded constant)**:

dG/dt ≤ -2νΩ₁ + 2C

**This would give**: G(t) ≤ G(0) + 2Ct - 2νΩ₁t. If Ω₁ is large enough
(the flow is "spread out"), G decreases. If Ω₁ is small (vorticity
concentrating), G can grow — but only at rate 2C, which is BOUNDED.

**Linear growth of log-enstrophy → at most EXPONENTIAL growth of enstrophy
→ NO FINITE-TIME BLOWUP!**

Wait — is that right? If G = ∫ log(1+|ω|²) dx ≤ G(0) + 2Ct, then:

  max |ω|² ≤ exp(G) ≤ exp(G(0) + 2Ct) = exp(G(0)) · e^{2Ct}

This is EXPONENTIAL growth in time, not finite-time blowup.
Regularity requires bounded growth, but exponential is OK — it's not blowup.

**EXPONENTIAL GROWTH IS FINE FOR REGULARITY.** The Millennium Prize asks
for NO FINITE-TIME BLOWUP, not bounded growth. Exponential growth is
smooth (C^∞ for all finite t).

## THE POTENTIAL BREAKTHROUGH

If the log-enstrophy dG/dt ≤ -2νΩ₁ + 2C bound is RIGOROUS:

  G(t) ≤ G(0) + 2Ct (linear growth)
  → |ω|² ≤ e^{G(0)+2Ct} (exponential growth)
  → |ω| < ∞ for all finite t
  → NO FINITE-TIME BLOWUP
  → NS REGULARITY

## What Needs to Be Checked

1. The diffusion term: ∫ ω·Δω/(1+|ω|²) dx = -∫ |∇ω|²/(1+|ω|²) dx + ???
   The "???" comes from differentiating 1/(1+|ω|²). Need to bound it.

2. The stretching bound: |∫ ωSω/(1+|ω|²) dx| ≤ C.
   Need: |S| ≤ C₁|ω| (from Biot-Savart CZ theory) to get:
   |ωSω/(1+|ω|²)| ≤ C₁|ω|³/(1+|ω|²) ≤ C₁|ω| (for large |ω|)
   Then ∫ C₁|ω| dx ≤ C₁ ||ω||_{L¹}... which is NOT bounded.

**PROBLEM**: ||ω||_{L¹} can grow. The bound |∫ ωSω/(1+|ω|²) dx| ≤ C
requires ||ω||_{L¹} ≤ const, which is NOT guaranteed.

Actually: ||ω||_{L¹} ≤ C ||ω||_{L²}^{1/2} ||ω||_{L²}^{1/2} = C||ω||_{L²}
(by Cauchy-Schwarz on T³). And the enstrophy ||ω||_{L²}² can grow.

So: ∫ ωSω/(1+|ω|²) dx ≤ C ||ω||_{L²} which grows.
And dG/dt ≤ C||ω||_{L²} which gives G ≤ G(0) + C ∫₀ᵗ ||ω(s)||_{L²} ds.
This is NOT linear growth — it depends on the enstrophy trajectory.

**The argument doesn't close.** The log-enstrophy helps but doesn't give
a uniform bound. Back to square one — but with MORE INFORMATION.

## Result

Option (a) exploration reveals:
1. NS is NOT a gradient flow (algebraically proven — stretching is not a gradient)
2. The log-enstrophy G = ∫ log(1+|ω|²) TAMES the stretching by dividing by (1+|ω|²)
3. BUT: the bound dG/dt ≤ C||ω||_{L²} is not uniform (depends on enstrophy)
4. The approach ALMOST works — the log dampens the stretching but not enough

**The noise mapped the space**: Option (a) is algebraically blocked (NS ≠ gradient flow)
but the log-enstrophy functional is a GENUINE new tool that partially helps.
The gap narrows from "stretching is uncontrolled" to "stretching/|ω|² is bounded
but the L¹ norm of |ω| still grows."

## For Next Tick
Option (c): search for a DIFFERENT W. The log-enstrophy hint: the right
functional should divide by a power of |ω|² to tame the stretching.
Combine with the Hermite basis / OU spectral gap approach.
