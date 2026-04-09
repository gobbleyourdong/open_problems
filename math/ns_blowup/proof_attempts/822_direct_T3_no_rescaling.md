---
source: DIRECT T³ ARGUMENT — avoiding rescaling entirely
type: NEW APPROACH — use energy equality in time-reversed coordinates
file: 822
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE IDEA

Instead of rescaling (which sends T³ → R³), work DIRECTLY on T³.
Use the energy equality in a time-reversed coordinate to exploit
both the Key Lemma AND the energy dissipation.

## TIME-REVERSED ENERGY ON T³

For NS on T³ × [0, T*) with potential blowup at T*:

Energy equality (EXACT on T³, no boundary terms):
    ||u(t₂)||² + 2ν ∫_{t₁}^{t₂} ||ω||² dτ = ||u(t₁)||²

Set τ = T* - t (time remaining). As t → T*: τ → 0.

||u(T*-τ)||² increases as τ increases (going backward from blowup).

## THE KEY CONSTRAINT

Under Type I: ||ω||∞ ≤ C_TI/τ. On T³:
    ||ω||² ≤ ||ω||∞² · |T³| ≤ C_TI² (2π)³ / τ²

But the actual ||ω||² is SMALLER (concentration):
    ||ω||² ~ C_TI² V(τ) / τ² where V(τ) is the concentration volume.

For parabolic concentration: V ~ τ^{3/2}, ||ω||² ~ τ^{-1/2}.

The energy dissipation near T*:
    2ν ∫_0^ε ||ω||² dτ ~ 2ν ∫_0^ε τ^{-1/2} dτ = 4ν√ε → 0

So the dissipation near blowup is FINITE and small. The energy
||u(T*-ε)||² approaches a LIMIT as ε → 0:
    ||u(T*)||² := lim_{ε→0} ||u(T*-ε)||² = ||u₀||² - 2ν ∫_0^{T*} ||ω||² dτ

This limit EXISTS (energy decreasing, bounded below by 0).

## THE VORTICITY DIRECTION EQUATION

The evolution of ξ = ω/|ω| involves:
    Dξ/Dt = (S - αI)ξ⊥ + viscous terms

The perpendicular strain: |S_⊥ξ| = √(S²ê - α²) ≤ √((3/4-ε)|ω|²) at the max.

The rate of rotation of the vorticity direction is bounded by the
perpendicular strain. Near blowup: the direction ξ can change, but
the rate is bounded by |ω| (from the Key Lemma).

## THE DIRECT ARGUMENT (ATTEMPT)

Assume Type I blowup at T* on T³.

Step 1: The solution u(·,t) is smooth on [0,T*) and has:
- ||u||_{L²} ≤ ||u₀||_{L²} (energy decreasing)
- ||ω||∞ ≤ C_TI/(T*-t) (Type I from Key Lemma)
- ||ω||_{L²} ≤ C(T*-t)^{-1/4} (concentration)

Step 2: The Fourier coefficients û_k(t) are smooth functions of t.
By Parseval: Σ |û_k|² = ||u||²/(2π)³ ≤ ||u₀||²/(2π)³.

Each |û_k(t)|² ≤ ||u₀||²/(2π)³ (bounded).

Step 3: As t → T*: the high-k modes grow (to accommodate ||ω||∞ → ∞).
But each |û_k|² stays bounded. The SUPPORT in k-space expands.

The effective K(t) (highest active mode): K ~ 1/ρ(t) where ρ is the
analyticity radius. Under Type I: ρ ~ T*-t, K ~ 1/(T*-t).

Step 4: The NUMBER of active modes: N_eff ~ K³ ~ (T*-t)^{-3}.

Step 5: The KEY LEMMA on the N_eff-mode truncation gives:
α < (√3/2)|ω| at the argmax. This is the SAME bound regardless of N_eff.

Step 6: The Type I growth d/dt||ω||∞ ≤ (√3/2)||ω||∞² is not improved.

## WHY THIS FAILS

The direct argument doesn't give anything beyond Type I because the
Key Lemma bound is CONSTANT (doesn't improve with N_eff).

The floor growth hypothesis WOULD improve it, but that's unproven.

## ALTERNATIVE: USE THE POINCARÉ INEQUALITY

On T³: ||u||_{L²}² ≤ (1/λ₁)||ω||_{L²}² where λ₁ = 1.

The energy at blowup: ||u(T*)||² ≥ 0. And:
||u(T*)||² = ||u₀||² - 2ν ∫_0^{T*} ||ω||² dτ

For blowup: ||ω||² → ∞ (enstrophy must blow up). But the INTEGRAL
is bounded: ∫||ω||² ≤ ||u₀||²/(2ν).

This gives: the enstrophy can blow up POINTWISE but its integral is finite.
With ||ω||² ~ (T*-t)^{-β}: ∫(T*-t)^{-β} converges iff β < 1.

So ||ω||² = o((T*-t)^{-1}).

Under Type I: ||ω||∞ ~ (T*-t)^{-1}. The L² enstrophy:
||ω||² ≤ ||ω||∞² |T³| ~ (T*-t)^{-2}. This has β=2 > 1: integral DIVERGES.

But wait: ||ω||² ≤ ||ω||∞² |T³| is the CRUDE bound. The actual ||ω||²
with concentration is ~ (T*-t)^{-1/2} (β=1/2 < 1). Converges. ✓

No contradiction from the energy budget for Type I with concentration.

## THE MISSING INGREDIENT

To get a contradiction on T³ without rescaling: need to show that
Type I blowup with concentration is INCONSISTENT with the NS
evolution on T³. This requires MORE than just the Key Lemma and
energy equality — it needs the DYNAMIC structure of NS.

The energy equality + Key Lemma = necessary conditions. They're
INSUFFICIENT for a contradiction because Type I with concentration
satisfies all the necessary conditions.

The DYNAMIC structure (how the solution evolves in Fourier space,
the specific nonlinear interactions, the pressure feedback) is needed.
This is equivalent to proving depletion along NS trajectories.

## WHAT WOULD WORK

A contradiction on T³ requires ONE of:
1. A GLOBAL bound (not just at max) that makes the enstrophy integral diverge
2. A DYNAMIC argument that tracks the solution's Fourier structure
3. A completely new conservation law or monotonicity formula on T³

None of these are currently available.

## 822. Direct T³: energy + Key Lemma insufficient for contradiction.
## Type I with concentration satisfies all known constraints on T³.
## The gap: need either global depletion or dynamic NS-specific structure.
## 22 proof attempts. The mountain is real.
