# Known Ancient NS Solutions — Phase 1 Census

**Date:** 2026-04-09
**Script:** `numerics/known_ancient_solutions.py`
**Track:** Numerical

## The Critical Observation

**Every known non-trivial ancient NS solution is UNBOUNDED.**

| Solution | Bounded? | Ancient? | Liouville |
|----------|----------|----------|-----------|
| u ≡ 0 (trivial) | bounded | ancient | constant ✓ |
| u ≡ c (constant) | bounded | ancient | constant ✓ |
| Lamb-Oseen vortex | UNBOUNDED (t→0) | NOT ancient | vacuous |
| Burgers vortex | UNBOUNDED (z→∞) | eternal | vacuous |
| Beltrami flow | UNBOUNDED (t→-∞) | ancient | vacuous |
| ABC flow | UNBOUNDED (t→-∞) | ancient | vacuous |
| Poiseuille/Couette | not on R³ | steady | n/a |

No bounded non-constant ancient solution has EVER been found.

## Lamb-Oseen Vortex (2D)

u_θ(r,t) = Γ/(2πr) · (1 - e^(-r²/(4νt))) for t > 0.
As t → 0⁺: vorticity concentrates at origin (→ δ-function),
velocity → point vortex Γ/(2πr). UNBOUNDED.

## Burgers Vortex (3D, steady)

u_r = -αr/2, u_θ = Γ/(2πr)(1 - e^(-αr²/2ν)), u_z = αz.
The axial strain u_z = αz makes this UNBOUNDED in z.
Key quantities at α = Γ = ν = 1:
- Max stretching |ω·∇u| ≈ 0.079
- Max diffusion |Δω| ≈ 0.155
- Stretching/diffusion ratio up to 18.3 (stretching can dominate locally!)
- Dirichlet integral DIVERGES (|∇u|² ~ α² from u_z)

## Beltrami Flows (curl u = λu)

Exact: u(x,t) = e^(-νλ²t) u₀(x). Forward: exponential decay.
Ancient (t → -∞): exponential GROWTH. At t = -20: |u| ~ 5×10⁸.

## Implications for the Attack

1. **We cannot study the target object directly** — no non-trivial
   bounded ancient solution exists to compute on
2. **Any proof must be indirect** — via monotone invariants,
   contradictions, or exclusion arguments
3. **The Poincaré parallel is exact**: Perelman didn't find ancient
   Ricci flows by construction; he proved they must be solitons
   via five monotone detectors. Liouville needs the NS analog.
4. **The Burgers vortex is the richest test case** — it has 3D
   structure, vortex stretching, and exact formulas, but it's
   unbounded. Its KEY QUANTITIES (stretching/diffusion ratio,
   frequency function, Dirichlet integral) set benchmarks for
   what bounded solutions would need to satisfy.
