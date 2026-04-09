---
source: ALIGNMENT DYNAMICS — the NS dynamics repels the Key Lemma extremizer
type: ANALYSIS — the Vieillefosse mechanism explains depletion
file: 839
date: 2026-04-02
instance: MATHEMATICIAN (Opus)
---

## THE KEY OBSERVATION

The Key Lemma extremizer (α/|ω| → 0.866) requires:
    ω aligned with the LARGEST eigenvector of S.

The NS dynamics (restricted Euler + pressure) pushes:
    ω toward the INTERMEDIATE eigenvector of S.

These are OPPOSING. The extremizer is DYNAMICALLY UNSTABLE.

## THE RESTRICTED EULER ALIGNMENT

The velocity gradient m = ∇u evolves by (restricted Euler):
    dm/dt = -m² - H_p   (where H_p is the pressure Hessian)

Ignoring H_p: dm/dt = -m². The eigenvalue dynamics:
    dλ_i/dt = -λ_i² + (1/3)(λ₁²+λ₂²+λ₃²)   (trace-free projection)

The vorticity direction ξ evolves by:
    dξ/dt = (S - αI)ξ_⊥   (perpendicular strain rotates ξ)

The rotation RATE depends on the eigenvalue GAPS:
- Near e₁ (largest): the rotation pushes AWAY (λ₁-λ₂ > 0, unstable).
- Near e₂ (intermediate): the rotation is WEAKEST (λ₂ between λ₁,λ₃).
- Near e₃ (smallest): the rotation pushes AWAY (λ₃-λ₂ < 0, unstable).

The intermediate eigenvector e₂ is the ATTRACTOR for ω alignment.
This is the Vieillefosse mechanism (1982, 1984).

## THE STRETCHING AT THE ATTRACTOR

When ω aligns with e₂: α = ξ·S·ξ = λ₂.

From trace-free (λ₁+λ₂+λ₃=0) and ordering (λ₁≥λ₂≥λ₃):
- If λ₂ = 0 (the typical case: λ₁ = -λ₃, axisymmetric strain):
  α = 0. NO STRETCHING. This is complete depletion.

- If λ₂ > 0: α > 0 but α ≤ λ₂ ≤ λ₁/2 (from λ₂ ≤ (λ₁-λ₃)/2...
  actually from λ₁+λ₂+λ₃=0: λ₂ = -(λ₁+λ₃), and λ₁≥λ₂≥λ₃ gives
  λ₂ ≤ λ₁/2 when λ₃ ≤ -λ₁/2).

- The ratio α/|S| = λ₂/√(λ₁²+λ₂²+λ₃²) is MINIMIZED when λ₂ → 0.

## THE PRESSURE HESSIAN COMPLICATION

The full NS has dm/dt = -m² - H_p. The pressure Hessian H_p:
- Isotropic part: (∆p/3)I = (|ω|²/2-|S|²)I/3. Modifies ALL eigenvalues equally.
- Deviatoric part: H_p^d = H_p - (∆p/3)I. This is the CZ operator.

The deviatoric part can ROTATE the eigenvectors, potentially
disrupting the intermediate alignment. This is THE WALL.

Yang et al. (2024): in regions of strong vorticity, H_p ≈ local terms.
The local approximation PRESERVES the intermediate alignment.
The nonlocal correction (CZ) is small for concentrated vorticity.

## WHAT CAN BE FORMALIZED

1. **Restricted Euler alignment** (no H_p): ω → e₂ is provable.
   The alignment dynamics is an ODE on the unit sphere.
   The intermediate eigenvector is a stable fixed point.

2. **At the attractor**: α = λ₂. For axisymmetric strain: α = 0.
   This is a Lean-formalizable algebraic fact.

3. **Instability of the extremizer**: ω → e₁ is UNSTABLE.
   The Key Lemma extremizer requires ω ∥ e₁.
   The restricted Euler pushes ω AWAY from e₁.

## THE GAP (REFINED ONCE MORE)

To prove regularity: need to show the FULL NS dynamics (with H_p)
maintains the intermediate alignment near blowup.
This requires controlling the deviatoric pressure Hessian.
Which is the CZ operator on L∞. THE WALL.

## THE HIERARCHY

| Level | Statement | Status |
|-------|-----------|--------|
| Kinematic | α ≤ 0.866|ω| (Key Lemma) | PROVEN (SOS + Lean) |
| Restricted Euler | ω → intermediate eigenvector | PROVABLE (ODE analysis) |
| Full NS | ω stays near intermediate | OPEN (needs CZ control) |
| Depletion | α/|ω| → 0 near blowup | OPEN (= full NS alignment) |
| Regularity | No blowup on T³ | OPEN (= depletion + chain) |

## 839. The NS dynamics is REPULSIVE near the Key Lemma extremizer.
## Vieillefosse: ω → intermediate eigenvector (α reduced).
## Key Lemma extremizer: ω → largest eigenvector (α maximal, UNSTABLE).
## Proving alignment persists with pressure Hessian = THE WALL = THE GAP.
