# Transfer from Poincaré: The W-Entropy for Navier-Stokes

> Multiple Mountains doctrine: the solution to NS might come from Ricci flow.
> Perelman's W-entropy killed 4 walls simultaneously. Can a vorticity
> entropy do the same for NS?

## The Analogy

| Ricci Flow | Navier-Stokes |
|-----------|---------------|
| Metric g(t) | Velocity u(t) |
| ∂g/∂t = -2Ric | ∂u/∂t = νΔu - (u·∇)u + ∇p |
| Scalar curvature R | Enstrophy density \|ω\|² |
| Singularity: \|Rm\| → ∞ | Blowup: \|ω\| → ∞ |
| W-entropy: monotone → no collapse | ???-entropy: monotone → no blowup? |
| Surgery at necks | ??? |

## Perelman's W-Entropy (What Worked)

W(g, f, τ) = ∫_M [τ(R + \|∇f\|²) + f - n] · (4πτ)^{-n/2} e^{-f} dV

Under Ricci flow + conjugate heat equation for f + dτ/dt = -1:

dW/dt = 2τ ∫ \|Ric + Hess(f) - g/(2τ)\|² · u dV ≥ 0

**Why it works**: the variation is a PERFECT SQUARE. Non-negative by construction.
The test function f and scale τ are AUXILIARY — they don't add physics,
they add an ACCOUNTING FRAMEWORK that makes the monotonicity visible.

## The NS Candidate

Replace curvature with vorticity:

**W_NS(u, f, τ) = ∫_{T³} [τ(\|ω\|² + \|∇f\|²) + f - 3] · (4πτ)^{-3/2} e^{-f} dx**

with:
- ω = curl(u) (vorticity)
- f solves a conjugate equation: ∂f/∂t = -νΔf + \|∇f\|² - \|ω\|² + 3/(2τ)
- dτ/dt = -1 (backward scale parameter)
- (4πτ)^{-3/2} e^{-f} dx is a probability measure on T³

## Computing dW_NS/dt

The key computation: does dW_NS/dt have a definite sign?

### The Good Terms (from diffusion)
The viscous term νΔu in NS acts like diffusion — it SMOOTHS ω.
This contributes POSITIVELY to dW/dt (entropy increases under heat flow).
Analogous to the ΔR term in Ricci flow.

### The Bad Term (vortex stretching)
The nonlinear term (ω·∇)u = ω_i S_{ij} ê_j (stretching of vorticity by strain).
This has NO SIGN. It can increase \|ω\|² without bound.

In the W-entropy framework: the stretching term appears as:

∫ τ · 2ω_i S_{ij} ω_j · (4πτ)^{-3/2} e^{-f} dx

This is τ · 2⟨Sω, ω⟩ weighted by e^{-f}.

### The Critical Question

Does the coupling to f (via e^{-f}) TAME the stretching term?

In Ricci flow: the analog of stretching is the Rm² term in the curvature
evolution. Perelman's trick: the e^{-f} weight LOCALIZES the integral so
that the bad terms are controlled by the good terms.

For NS: the e^{-f} weight localizes around regions where f is small
(= where ω is controlled). If the stretching is worst where ω is large
(= where f is large = where e^{-f} is small), the weight SUPPRESSES
the bad term.

**Physical intuition**: the test function f tracks the "temperature" of
the vorticity field. Where vorticity is intense (high temperature),
the weight e^{-f} is small, suppressing the contribution. The entropy
measures the "coolest" parts of the flow, where regularity is maintained.

## What Would Make This Work

For dW_NS/dt ≥ 0, need:

dW_NS/dt = (diffusion terms ≥ 0) + (stretching term) + (pressure term)

The stretching term must be ABSORBED by the diffusion or controlled by
the e^{-f} weight. Specifically:

\|stretching\| ≤ C · (diffusion) + C' · τ^{-1}

If this holds: dW_NS/dt ≥ -C'/something, and the total W stays bounded below.
Bounded W → bounded enstrophy on the support of e^{-f} → regularity.

## What Would Make This FAIL

The stretching term τ · 2⟨Sω, ω⟩ involves the STRAIN S, which is controlled
by the velocity gradient ∇u, which involves BOTH ω and the pressure.
The pressure is nonlocal (it's determined by a Poisson equation).

In Ricci flow: everything is LOCAL (the curvature depends only on the
metric and its derivatives at a point). This locality is what makes the
perfect-square structure possible.

In NS: the NONLOCALITY of the pressure might prevent the perfect-square
structure. The variation dW/dt might not factor as a square.

## The Honest Assessment

The Poincaré → NS transfer is:
- **Structurally motivated** (both are nonlinear parabolic flows)
- **The right idea** (monotone entropy = regularity)
- **Possibly blocked** by the nonlocality of pressure in NS

The transfer works IF the e^{-f} weight can localize the stretching.
This is a CONCRETE, CHECKABLE computation:

1. Write out dW_NS/dt explicitly (all terms)
2. Group into diffusion (positive), stretching (unknown), pressure (unknown)
3. Check: does the stretching + pressure combination have bounded ratio
   to the diffusion?

## For the NS Campaign

This is a CONCRETE proposal for your Phase 5 work:

1. **Compute dW_NS/dt** for the candidate functional above
2. **Identify** whether the variation has a perfect-square structure
3. **If yes**: W-entropy → regularity → NS solved
4. **If no**: identify the SPECIFIC term that prevents monotonicity
   (this becomes the new gap — more refined than "Liouville conjecture")
5. **If partially**: maybe a MODIFIED W (different coupling of ω to f)
   gives monotonicity. Search over functionals of the form
   W = ∫ [τ·g(\|ω\|², \|∇f\|²) + h(f)] · e^{-f} dx

The search over functionals g, h is a SYSTEMATIC computation (not a
genius insight). This is the Sigma Method applied to functional design.
