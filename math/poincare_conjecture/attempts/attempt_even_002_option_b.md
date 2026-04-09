# NS Even 002 — Option (b): Bound ωSω ≤ C|∇ω|²

**Date**: 2026-04-07
**Instance**: Even (Odd role on NS)

## The Question

Can we prove: |∫ ωᵢSᵢⱼωⱼ e^{-f} dx| ≤ C ∫ |∇ω|² e^{-f} dx  for some C < 1?

If yes: the W-entropy dW/dt ≥ (1-C) × (perfect square) ≥ 0 → regularity.

## What ωSω Actually Is

ω = vorticity, S = strain = (∇u + ∇uᵀ)/2.
The Biot-Savart law: u = K * ω where K is the singular integral kernel.
So S = (∇K * ω + (∇K * ω)ᵀ)/2 — a NONLOCAL function of ω.

ωᵢSᵢⱼωⱼ = the rate at which strain STRETCHES vorticity along itself.
This is the VORTEX STRETCHING term. It's what drives potential blowup.

## Known Bounds (No Weight)

Without the e^{-f} weight, the standard bounds are:

### Bound 1: Sobolev
|∫ ωSω dx| ≤ ||ω||_{L³} ||S||_{L³} ||ω||_{L³} ≤ C ||ω||_{H^{1/2}}² ||ω||_{H^{1/2}}

This gives: |∫ ωSω dx| ≤ C ||ω||_{H^{1/2}}³

The problem: ||ω||_{H^{1/2}} is NOT controlled by ||∇ω||_{L²} alone.
It's an intermediate norm: ||ω||_{L²} ≤ ||ω||_{H^{1/2}} ≤ ||ω||_{H¹}.

### Bound 2: Interpolation
|∫ ωSω dx| ≤ C ||ω||_{L²}^{3/2} ||∇ω||_{L²}^{3/2}

This is the standard Ladyzhenskaya inequality applied to the vorticity.
Compared to ||∇ω||² (which has exponent 2): the stretching has exponent 3/2.

**At small enstrophy** (||ω||_{L²} small): stretching ≪ diffusion. ✓
**At large enstrophy**: stretching ~ ||ω||^{3/2} ||∇ω||^{3/2} can EXCEED diffusion ~ ||∇ω||². This is the blowup regime.

### Bound 3: The Critical Ratio
Define: R = |∫ ωSω dx| / ∫ |∇ω|² dx

By the interpolation bound: R ≤ C ||ω||_{L²}^{3/2} / ||∇ω||_{L²}^{1/2}

For R < 1 (what we need): require ||∇ω||_{L²}^{1/2} > C ||ω||_{L²}^{3/2}
i.e., ||∇ω||_{L²} > C² ||ω||_{L²}³

This is a CONDITIONAL bound: R < 1 IF the enstrophy gradient is large
relative to the enstrophy itself. This is the "Prodi-Serrin" type condition.

## With the e^{-f} Weight

The weight e^{-f} localizes the integral. If f is chosen so that e^{-f}
is small where ω is large:

|∫ ωSω e^{-f} dx| ≤ ||ωSω||_{L^p(e^{-f}dx)} for appropriate p

The CONJUGATE HEAT EQUATION for f:
  ∂f/∂t = -νΔf + |∇f|² - |ω|² + 3/(2τ)

This makes f LARGE where |ω|² is large (the -|ω|² drives f negative...
wait, that's wrong. Let me think.)

Actually: ∂f/∂t includes -|ω|², which makes f DECREASE where ω is large.
So e^{-f} is LARGE where ω is large. That's the WRONG direction!

Hmm. In Perelman's setup: f tracks the "temperature" and e^{-f} is the
probability measure. The measure concentrates where f is SMALL = where
curvature is LOW. For NS: f small where |ω|² is large means the measure
concentrates at HIGH vorticity — the DANGEROUS region.

This is actually CORRECT for the entropy argument: you want W to measure
the "information" at the most dangerous points. But it means the weight
DOESN'T suppress the stretching.

## A Different Weight?

What if we use a DIFFERENT weight — not e^{-f} but e^{+f} or e^{g(|ω|²)}?

If the weight is e^{-α|ω|²}: then e^{-α|ω|²} is SMALL where |ω|² is large.
This WOULD suppress the stretching term.

But: the entropy W with this weight would need a different conjugate equation,
and the "perfect square" structure might break.

**SEARCH**: find a weight function w(x, t) such that:
1. dW/dt = (square) + ∫ ωSω · w dx
2. The weight w suppresses ωSω enough that |∫ ωSω · w dx| < (square)
3. The conjugate equation for w is well-posed

This is Option (c) — finding a different W. Options (b) and (c) converge.

## The Leray Self-Similar Route

The other instance's work: put the Leray self-similar profile in a Hermite
basis, use the Ornstein-Uhlenbeck operator (spectral gap = 1/2).

The Leray blowup ansatz: u(x,t) = (1/√(2a(T-t))) U(x/√(2a(T-t)))
The profile U satisfies: -νΔU + (U·∇)U + aU + a(y·∇)U + ∇P = 0

In the Hermite basis: the Ornstein-Uhlenbeck operator L = -Δ + y·∇ has
eigenvalues n = 0, 1, 2, ... (spectral gap = 1).

The KEY BOUND: ||φ|| < 1/(2C_S) where:
- φ = the Leray profile in some norm
- C_S = the Sobolev constant connecting stretching to diffusion

**This IS Option (b) quantified.** The ratio R = C_S · ||φ||.
If R < 1/2: the diffusion dominates → no blowup → regularity.

## Computing the Numbers

### C_S (the Sobolev constant)
The best constant in |∫ ωSω dx| ≤ C_S ||ω||_{L²} ||∇ω||_{L²}²:

From the Biot-Savart kernel K(x) = -x/(4π|x|³):
|S| ≤ C_BM |ω| (Biot-Savart-Calderón-Zygmund bound)

C_BM = the operator norm of the Riesz transform = 1/(2π)... no, the
exact constant depends on the dimension and the specific CZ kernel.

For T³: the Biot-Savart operator has ||S||_{L²} ≤ ||ω||_{L²} (energy equality).
The stretching: |∫ ωSω dx| ≤ ||ω||_{L∞} ||S||_{L²} ||ω||_{L²}
                             ≤ ||ω||_{L∞} ||ω||_{L²}²

Using Agmon's inequality: ||ω||_{L∞} ≤ C ||ω||_{H¹}^{1/2} ||ω||_{H²}^{1/2}

So: |∫ ωSω dx| ≤ C ||ω||_{H¹}^{1/2} ||ω||_{H²}^{1/2} ||ω||_{L²}²

Compared to diffusion ~ ν||∇ω||_{L²}² = ν||ω||_{H¹}²:

R ≤ C ||ω||_{H²}^{1/2} ||ω||_{L²}² / (ν ||ω||_{H¹}^{3/2})

**This is NOT bounded by a constant < 1 in general.** The ratio R
depends on ||ω||_{H²} which can be large.

### The Self-Similar Constraint
For a SELF-SIMILAR blowup: ||ω||_{H²} ~ (T-t)^{-3/2} and ||ω||_{L²} ~ (T-t)^{-1/2}.

R ~ C (T-t)^{-3/4} (T-t)^{-1} / (ν (T-t)^{-3/4}) = C / ν

**For self-similar blowup**: R is a CONSTANT (independent of T-t).
This constant is ||φ|| · C_S. If it's < 1: no self-similar blowup.

This is the ||φ|| < 1/(2C_S) condition.

## Result

Option (b) reduces to:
- **General flows**: R depends on regularity (can't bound uniformly)
- **Self-similar blowup**: R = ||φ|| · C_S (a COMPUTABLE constant)

The Millennium Prize (if approached via self-similar exclusion):
  Compute ||φ|| and C_S. If ||φ|| · C_S < 1: no Type I blowup.
  Then: combine with known results (Seregin, KNSS) to get full regularity.

**The two numbers to compute**:
1. C_S: best constant in the CZ/Sobolev inequality for Biot-Savart
2. ||φ||: norm of the Leray self-similar profile in the Hermite basis

Both are computable. The question is whether their product is < 1.

## For Next Tick
Move to Option (a): can ωSω be made algebraic (fit into a square)?
This would bypass the Sobolev constants entirely.
