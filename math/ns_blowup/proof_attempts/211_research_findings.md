---
source: Research findings — Perelman entropy, Li-Ni, Galanti-Gibbon-Heritage
type: LITERATURE REVIEW — what exists, what's missing
date: 2026-03-29
file: 211
---

## Key Findings from Literature Search

### 1. No Perelman Entropy for NS Exists
Nobody has constructed a monotone Perelman-type entropy for NS.
Li-Ni (2004) proved it for the LINEAR heat equation on manifolds.
Extension to NS is OPEN.

### 2. Galanti-Gibbon-Heritage (1997) — THE RELEVANT PAPER
"Vorticity alignment results for Euler and Navier-Stokes"
Nonlinearity vol. 10, pp. 1675-1694.

KEY RESULTS:
- Derived CLOSED ODEs for alignment evolution including pressure Hessian
- Showed vorticity aligns with INTERMEDIATE strain eigenvector (Ashurst)
- The Burgers vortex is a LAGRANGIAN FIXED POINT of their system
- Provided the eigenframe analysis of the pressure Hessian

THIS IS EXACTLY OUR FRAMEWORK. Their closed ODEs are what we need
to analyze Q at the max. The Burgers vortex fixed point might give
Q < 0 explicitly.

### 3. Recent Claims (unverified)
- arXiv:2401.17147: Claims regularity for bounded initial data. Unverified.
- arXiv:2504.21000: Self-similar solutions approach. Claims regularity.
- arXiv:2507.03881: WITHDRAWN due to errors.

### 4. No One Has Proven Ashurst Alignment from PDE
The alignment is universally MEASURED but never PROVEN from the equations.
Our conditional theorem (c₁ < 1/3 → regularity) is new.

## Action Items

1. READ Galanti-Gibbon-Heritage (1997) carefully.
   Their closed ODE system for alignment + pressure Hessian is what
   we need. They may have computed Q (or something equivalent)
   in their framework.

2. COMPUTE Q for the Burgers vortex (exact stationary solution).
   If Q < 0 for Burgers: it proves the mechanism at the fixed point.
   Stability analysis around Burgers → Q < 0 nearby.

3. Try the Li-Ni entropy approach for the NS-adapted heat equation.
   The NS vorticity equation is: Dω/Dt = Sω + νΔω.
   This is a heat equation with a transport + stretching term.
   Li-Ni's monotone entropy might extend if the stretching is
   treated as a "curvature" term.

## The Burgers Vortex Approach

The Burgers vortex: ω = (0, 0, ω₀ exp(-r²γ/(4ν))), u_z = γz,
u_r = -γr/2 (axisymmetric straining flow).

At the center: α = γ (the strain rate). S = diag(-γ/2, -γ/2, γ).
|ω| = ω₀. |S|² = 3γ²/2.

Q = Dα/Dt + α² = 0 + γ² (steady state → Dα/Dt = 0).

So Q = γ² > 0 for the Burgers vortex! This is POSITIVE (bad).

But: the Burgers vortex is a STEADY STATE with CONSTANT ||ω||∞.
Q > 0 doesn't cause blowup because α = γ is constant (not growing).
The Riccati: Dα/Dt = 0 ≠ -α² (the bound doesn't need to hold at
steady state because there's no blowup danger).

The DMP only needs to hold when ||ω||∞ is GROWING (approaching blowup).
For the Burgers vortex: ||ω||∞ is constant → not approaching blowup.

## 211. Literature confirms: no existing tools solve the gap.
## Galanti-Gibbon-Heritage (1997) is the most relevant paper.
## Burgers vortex has Q > 0 (steady state, not dangerous).
