---
source: Instance A — Transport equation for Q = S²ê - α² - H_ωω
type: PROOF ATTEMPT — derive DQ/Dt and show Q < 0 is attracting
date: 2026-03-29
---

## Setup

At a material point following the flow:
  Dα/Dt = S²ê - 2α² - H_ωω = Q - α²  where Q = S²ê - α² - H_ωω

Q < 0 ⟹ Dα/Dt < -α² (strong Riccati bound).

Need: DQ/Dt < 0 when Q ≥ 0 (maximum principle).

## Expanding DQ/Dt

Q = ê·S²·ê - (ê·S·ê)² - ê·H·ê

where ê = ω̂. All three terms evolve:

DQ/Dt = D(S²ê)/Dt - D(α²)/Dt - D(H_ωω)/Dt

## Term 1: D(S²ê)/Dt

S²ê = ê·S²·ê = Σ λ_i² c_i (eigenvalue representation).

D(S²ê)/Dt = Σ (Dλ_i²/Dt) c_i + Σ λ_i² (Dc_i/Dt)
= Σ 2λ_i(Dλ_i/Dt) c_i + (eigenvector tilting of S²ê)

Dλ_i/Dt = e_i·(DS/Dt)·e_i = e_i·(-S² - Ω² - H)·e_i
= -λ_i² - e_i·Ω²·e_i - e_i·H·e_i

So: Σ 2λ_i(Dλ_i/Dt) c_i = -2Σλ_i³c_i - 2Σλ_i(e_i·Ω²·e_i)c_i - 2Σλ_i(e_i·H·e_i)c_i

## Term 2: D(α²)/Dt = 2α·Dα/Dt = 2α(Q - α²) = 2αQ - 2α³

## Term 3: D(H_ωω)/Dt

This involves the EVOLUTION of the pressure Hessian projected onto ω.
This is the most complex term — it involves:
- The evolution of H (from the pressure Poisson equation applied to the evolving source)
- The rotation of ê (from Dω̂/Dt = (S-αI)·ω̂)

D(H_ωω)/Dt = ê·(DH/Dt)·ê + 2(Dê/Dt)·H·ê

The first part: DH/Dt is the material derivative of the pressure Hessian.
From the momentum equation and pressure Poisson:
DH_ij/Dt = ... (involves third derivatives of u and second derivatives of p)

This is EXTREMELY complex. The pressure Hessian evolution involves:
  D(∂²p/∂x_i∂x_j)/Dt = ∂²/∂x_i∂x_j(Dp/Dt) + (advection corrections)

And Dp/Dt involves the material derivative of pressure, which from the
momentum equation: Dp/Dt = -|∇p|²/(something)... actually it's simpler:

From the NS equation: ∂u/∂t + (u·∇)u = -∇p (Euler).
Taking ∂/∂x_i: DA_ij/Dt = -A²_ij - H_ij (this is the vel gradient eq).
Taking ∂/∂x_j of the vel gradient eq:
D(∂A_ij/∂x_j)/Dt = -∂(A²_ij)/∂x_j - ∂H_ij/∂x_j + (advection corrections)

This gives the evolution of ∇·(∇u) = ∇(∇·u) = 0 (div-free).
Not directly useful for DH/Dt.

## A Simpler Approach

Instead of deriving DQ/Dt explicitly (too complex), use an ENERGY argument.

Define the GLOBAL quantity: <Q>_ω = ∫ Q(x) |ω(x)|² dx / ∫ |ω|² dx
(the enstrophy-weighted average of Q).

From the data:
- <Q>_ω < 0 after the initial transient (measured in multiple files)
- The MEAN Q is negative, meaning the AVERAGE point has Q < 0

For the max-point Q: it's typically more negative than the average
(the max point has the strongest compression).

## Alternative: Use the KNOWN Transport Equations

The vortex stretching equation: Dω/Dt = S·ω (Euler).
The strain equation: DS/Dt = -S² - Ω² - H.
The enstrophy: D|ω|²/Dt = 2|ω|²α.

These give: D(α)/Dt = S²ê - 2α² - H_ωω (known).

For Q = Dα/Dt + α²: the evolution DQ/Dt requires differentiating
Dα/Dt along the flow. This is a SECOND MATERIAL DERIVATIVE:

D²α/Dt² = D(S²ê - 2α² - H_ωω)/Dt

= D(S²ê)/Dt - 4α·Dα/Dt - D(H_ωω)/Dt

= D(S²ê)/Dt - 4α(Q - α²) - D(H_ωω)/Dt

For Q → 0⁺ (approaching the boundary):
D²α/Dt² = D(S²ê)/Dt - 4α(0 - α²) - D(H_ωω)/Dt
= D(S²ê)/Dt + 4α³ - D(H_ωω)/Dt

For DQ/Dt < 0 at Q = 0: need D²α/Dt² < Dα/Dt (since DQ/Dt = D²α/Dt² - D(α²)/Dt
and at Q=0: Dα/Dt = -α², so D(α²)/Dt = -2α³).

DQ/Dt = D²α/Dt² + 2α³ < 0 at Q = 0.

This requires: D²α/Dt² < -2α³ when Q = 0 (i.e., when Dα/Dt = -α²).

## Is This Plausible?

At Q = 0: S²ê - α² = H_ωω. The pressure Hessian exactly balances the variance.

The evolution from this balance point: if the pressure GROWS faster
than the variance (DH_ωω/Dt > D(S²ê - α²)/Dt): then Q decreases (becomes negative).

From the data: after the initial transient, Q is ALREADY negative
and stays negative. The evolution maintains Q < 0.

The RATE at which Q decreases is proportional to |ω|² (from the
strain equation scales). For large |ω|: Q becomes MORE negative → self-reinforcing.

## The Self-Reinforcing Mechanism

When Q < 0: Dα/Dt < -α² → α decreases fast → |ω| growth slows →
the pressure has more time to "catch up" → Q stays negative.

When Q would approach 0: the pressure (from the global Poisson solve)
responds to the changing vorticity field and maintains compression.
This is the "transport barrier" from file 176.

The self-reinforcement: Q < 0 → slower |ω| growth → more time for
pressure to act → Q stays negative. It's a STABLE EQUILIBRIUM.

## What This Means

The proof via transport equation is PLAUSIBLE but:
1. DQ/Dt is extremely complex (involves DH/Dt which needs third derivatives)
2. The self-reinforcement is a STABILITY argument, not a direct bound
3. The complexity of D(H_ωω)/Dt may be intractable analytically

## 191. Transport equation approach: plausible but complex.
## The self-reinforcing stability of Q < 0 is the right picture.
## Formal derivation of DQ/Dt requires DH/Dt (third-order PDE analysis).
