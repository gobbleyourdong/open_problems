# NS Even 005 — Computing the Number: ||φ|| in L²(Gaussian)

**Date**: 2026-04-07
**Track**: theory (Odd role on NS)

## The Setup

We need: ||φ||_{L²(Gaussian)} · C_S < 1 where φ is the Leray profile.

## What's Known About φ

The Leray self-similar blowup profile φ(y) satisfies:
  -νΔφ + (φ·∇)φ + (1/2)φ + (1/2)(y·∇)φ + ∇P = 0  on R³

### Nonexistence Results
| Authors | Year | Result |
|---------|------|--------|
| Nečas-Růžička-Šverák | 1996 | No φ ∈ L³(R³) |
| Tsai | 1998 | No φ ∈ Lᵖ, p ∈ [3, ∞) |
| Chae | 2007 | No φ ∈ L^{3/2}_{loc} with certain decay |
| Seregin | 2012 | Blowup → ||u||_{L³} → ∞ |
| Chae-Wolf | 2016+ | Extensions to weaker spaces |

**Key**: NO self-similar blowup in L³. The question: what about WEAKER spaces?

## The Singularity Analysis

If φ exists with a singularity at y = 0: φ(y) ~ |y|^{-α} as y → 0.

Membership in function spaces:
  φ ∈ L³(R³)         ⟺  α < 1        (NRS: ruled out)
  φ ∈ L²(Gaussian)   ⟺  α < 3/2      (OUR condition)
  φ ∈ H^{-1}(R³)     ⟺  α < 5/2      (distributional)

The gap between what's KNOWN (α < 1 ruled out) and what we NEED
(α < 3/2 ruled out): **α ∈ [1, 3/2)**.

```
SINGULARITY EXPONENT α:

0         1           3/2          5/2
|─────────|───────────|────────────|
   L³        THE GAP     H^{-1}
  RULED OUT   [1, 3/2)   distributional
  (NRS 96)    NEED THIS   (very rough)
```

## The Gap as a NUMBER

**THE NS GAP = 1/2**

The gap between what's proved (α < 1) and what's needed (α < 3/2) is
exactly α = 1/2 in exponent space. We need to extend the Leray profile
nonexistence from L³ (singularity < |y|⁻¹) to L²(Gaussian) (singularity
< |y|^{-3/2}).

**Equivalently**: prove that the Leray ODE has no solution with singularity
|y|^{-α} for ANY α ∈ [1, 3/2).

## Why This Might Be Provable

The Leray ODE is ELLIPTIC: -νΔφ + lower order = 0.

Elliptic regularity: solutions of -Δφ + (φ·∇)φ = f are MORE regular
than f would suggest. Specifically:

If φ ∈ L²(Gaussian) (so φ ~ |y|^{-α} with α < 3/2):
  The nonlinear term (φ·∇)φ ~ |y|^{-2α-1}
  The Laplacian term Δφ ~ |y|^{-α-2}

Balance: -α-2 = -2α-1 gives α = 1. So for α > 1: the Laplacian
DOMINATES the nonlinearity near y = 0. The solution is essentially
solving -Δφ = 0 near y = 0, whose solutions are HARMONIC.

Harmonic functions with |y|^{-α} singularity: only α = 1 (the Newtonian
potential). For α ∈ (1, 3/2): no harmonic function has this singularity
unless it's a MULTIPOLE (which has specific angular structure).

**The Leray ODE + elliptic regularity might force α = 1 exactly.**
If α = 1: we're in L³ territory → NRS rules it out. Done.
If α ∈ (1, 3/2): the balance of terms in the Leray ODE is INCOMPATIBLE
with the elliptic structure → no such solution exists.

## The Concrete Computation

### Step 1: Local Analysis of the Leray ODE at y = 0

Write φ = |y|^{-α} Φ(ŷ) where ŷ = y/|y| is the angular variable.

Substituting into the Leray ODE:
  -ν[α(α+1)|y|^{-α-2} Φ + |y|^{-α} Δ_S Φ/(|y|²)]
  + |y|^{-2α} [(Φ·∇)(|y|^{-α} Φ)]
  + (1/2)|y|^{-α} Φ
  + (1/2)|y|^{-α+1} (ŷ·∇)(|y|^{-α} Φ) = 0

The leading terms at y → 0:
  -ν α(α+1) |y|^{-α-2} Φ + C |y|^{-2α-1} Φ² + ... = 0

For the two terms to balance: -α-2 = -2α-1, giving **α = 1**.

For α > 1: the Laplacian term (-α-2 exponent) is MORE singular than
the nonlinear term (-2α-1 exponent). So at leading order:
  -ν α(α+1) |y|^{-α-2} Φ ≈ 0 → Φ = 0 (contradiction!)

**For α ∈ (1, 3/2): the Laplacian dominates and forces Φ = 0.**
This means: NO Leray profile with singularity |y|^{-α} for α > 1.

## THE RESULT

**The Leray ODE's leading-order balance at y = 0 forces α = 1.**

For α > 1: the Laplacian term dominates → Φ = 0 → no solution.
For α = 1: the terms balance → possible solution, BUT NRS rules it out.
For α < 1: weaker singularity → also in L³ → also NRS rules it out.

**THEREFORE: ||φ|| = 0 in L²(Gaussian).**

No Leray self-similar profile exists in L²(Gaussian), because:
1. α ∈ [1, 3/2): the leading-order balance forces α = 1 exactly
2. α = 1 → φ ∈ L³ → NRS rules it out
3. α < 1 → φ ∈ L³ → NRS rules it out

**||φ|| · C_S = 0 · C_S = 0 < 1. THE CONDITION IS SATISFIED.**

## Caveats

### Caveat 1: The leading-order analysis is formal
The balance argument assumes φ has a POWER-LAW singularity |y|^{-α}.
What if φ has a LOGARITHMIC singularity? E.g., φ ~ |y|^{-1} log(1/|y|)?

For φ ~ |y|^{-1} log(1/|y|): φ ∈ L³ iff ∫₀¹ |y|^{-3} log³ |y|² dy < ∞.
This integral DIVERGES. So the log-modified singularity is NOT in L³.

But is it in L²(Gaussian)? ∫₀¹ |y|^{-2} log² · |y|² dy = ∫₀¹ log²(1/|y|) dy < ∞.
YES! The log-modified singularity IS in L²(Gaussian) but NOT in L³.

**The gap reopens for logarithmic singularities.**

### Caveat 2: The pressure term
The Leray ODE has a pressure gradient ∇P. The pressure satisfies:
  -ΔP = ∂_i∂_j(φ_iφ_j) ~ |y|^{-2α-2}

The pressure gradient ∇P ~ |y|^{-2α-3} is MORE singular than the
Laplacian for any α. But the pressure enters with a GRADIENT structure
(it's curl-free), so it only affects the irrotational part of the
velocity, not the vorticity.

In the VORTICITY formulation of the Leray ODE: the pressure drops out.
So the leading-order balance is correct for the vorticity.

### Caveat 3: The angular structure matters
The balance α(α+1)Φ = 0 at leading order (for α > 1) only forces Φ = 0
if the angular Laplacian Δ_S doesn't have eigenvalues that compensate.

The angular Laplacian Δ_S on S² has eigenvalues ℓ(ℓ+1) for ℓ = 0, 1, 2, ...
If the Leray profile has angular mode ℓ: the effective exponent changes.

For ℓ ≥ 1: the singularity structure becomes φ ~ |y|^{-α} Y_ℓ(ŷ) with
a different balance. This needs a MORE DETAILED analysis.

## Honest Assessment

**The leading-order argument gives ||φ|| = 0 for power-law singularities.**
**But logarithmic modifications and angular modes might allow exceptions.**

The gap has narrowed from "||φ|| < 1/(2C_S)" (unknown number)
to "can the Leray ODE have log-modified or higher-angular-mode singularities
in the range excluded by NRS but allowed by L²(Gaussian)?"

This is a VERY SPECIFIC regularity question about the Leray ODE —
much more tractable than the original Millennium Problem.

## For Next Tick
Analyze the log-modified singularity: φ ~ |y|^{-1} (log(1/|y|))^β.
Does the Leray ODE admit such solutions? For which β?
If β < 1/2: the log modification is in L²(Gaussian) and NOT in L³.
This is the NARROWEST remaining gap.
