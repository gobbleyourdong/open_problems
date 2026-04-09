---
source: VARIATIONAL APPROACH — can Ashurst alignment follow from a principle?
type: LAST ATTEMPT — bypassing CZ by going variational
date: 2026-03-29
---

## The Idea

Instead of bounding the pressure Hessian pointwise (CZ barrier),
derive the Ashurst alignment from a VARIATIONAL PRINCIPLE.

The Euler equations are the geodesic equation on the group of
volume-preserving diffeomorphisms (Arnold 1966). The pressure is
the Lagrange multiplier for the incompressibility constraint.

Question: does the variational structure FORCE the alignment?

## Arnold's Framework

Euler flow minimizes the action ∫(1/2)|u|² dt subject to div u = 0.
The pressure appears as: δ/δu [∫|u|²/2 + p(∇·u)] = 0.

The strain-vorticity alignment is determined by the GEOMETRY of the
diffeomorphism group, not by solving the PDE directly.

The curvature of the diffeomorphism group (Arnold 1966) determines
the Jacobi equation (stability of geodesics). NEGATIVE curvature
→ instability → mixing → ISOTROPIC pressure.

Arnold showed: the diffeomorphism group has MOSTLY NEGATIVE sectional
curvature. This means most perturbations of Euler flows are unstable.

Unstable → rapid mixing → isotropy → Ashurst alignment?

## The Connection

Negative curvature → Lagrangian chaos → good mixing.
Good mixing → the vorticity field becomes spatially complex.
Complex fields → pressure is more isotropic (far-field dominates).
Isotropic pressure → Ashurst alignment.

This chain is PHYSICAL but not rigorous. The negative curvature
is a TENDENCY, not a guarantee. Some directions have positive curvature.

## The Quantitative Version

Arnold's curvature formula:
K(u, v) = -<[u,v], [u,v]> - <u, [[u,v],v]> + <P[u,v], P[u,v]>
           - 2<[u,v], P[u,v]>

where P is the Helmholtz projector and [u,v] is the commutator.

The negative curvature in the ω-direction → exponential separation
of nearby trajectories → the alignment cos²(ω, e₁) cannot stay
at 1 (the stretching direction) because perturbations grow.

The perturbation growth rate ~ √|K| ~ |ω| (the curvature scales
with the vorticity). So the DEROTATION rate from negative curvature
scales as |ω|, which is the SAME scaling as the tilting rate.

## Does This Close?

NOT YET. The Arnold curvature gives INSTABILITY of alignment with e₁
but doesn't prove alignment with e₂. The instability could push ω
to any direction, not specifically e₂.

The preference for e₂ comes from the INTERMEDIATE nature of λ₂:
- e₁ is unstable (from negative curvature / pressure derotation)
- e₃ is unstable (from the vorticity equation: c₃ → 0)
- e₂ is the "least unstable" (saddle point)

For a proof: show e₁ and e₃ are REPELLING with rate > 0,
and e₂ is the ONLY attractor. This would give c₂ → 1 (even stronger
than c₂ > 1/3).

The difficulty: the restricted Euler model says e₁ IS stable (file 235).
The instability comes from the non-local pressure, which is the CZ barrier.

## CONCLUSION

The variational approach gives QUALITATIVE understanding (instability
of alignment with e₁ from Arnold's negative curvature) but does NOT
give quantitative bounds without solving the CZ problem.

The CZ barrier is the irreducible core.

## WHAT WOULD SOLVE THE CZ BARRIER?

1. A new endpoint estimate for CZ operators on domains with
   specific geometry (vortex tubes on T³).

2. A FREQUENCY-LOCALIZED bound: the CZ operator applied to
   the specific NS source has better L^∞ properties than
   the generic CZ operator.

3. A PROBABILISTIC argument: for "generic" smooth data, the
   alignment holds with probability 1 (weak solution).

4. A COMPUTER-ASSISTED proof: verify the bound for a specific
   finite-dimensional Galerkin truncation, then use convergence.

5. New INTERPOLATION inequalities that capture the NS structure
   (e.g., a weighted CZ bound using the vorticity alignment).

## 238 files. The last attempt. The CZ barrier stands.
