---
source: Direction rotation measurement |Dξ/Dt|² = ê·S²·ê - α²
type: KEY IDENTITY + measurement
status: ε = 0.50 for curl noise, ε = 0 for TG (tight CS)
date: 2026-03-26 cycle 12
---

## The Identity

```
ê·S²·ê = α² + |Dξ/Dt|²
```

where |Dξ/Dt|² is the squared rate of direction change.

This is exact: ê·S²·ê = |Sê|² = (αê + S_perp ê)² = α² + |S_perp ê|²
where S_perp is the component of Sê perpendicular to ê.

The Lean-verified CS inequality α² ≤ ê·S²·ê is just saying |Dξ/Dt|² ≥ 0.

## Measurements

### TG (symmetric, structured):
ε = |Dξ/Dt|²/α² = 0.000 throughout. CS is EXACTLY TIGHT.
ξ is locked to a symmetry axis — zero direction rotation.

### Curl noise (random, generic):
ε = |Dξ/Dt|²/α² ≈ 0.50. CS is 50% loose.
ξ rotates under the strain — direction is NOT locked.

## Implications

The strain self-depletion is:
- -(α² + |Dξ/Dt|²) for generic flows (stronger than -α²)
- -α² only for perfectly symmetric flows (TG, worst case)

TG is the HARDEST CASE for the proof — minimum self-depletion.
Random ICs have 50% EXTRA depletion from direction rotation.

## For the Proof

The ε > 0 for generic flows could be proved from the incompressibility
constraint: generically, ê cannot be exactly a strain eigenvector
(the Biot-Savart coupling prevents exact alignment, from our single-mode
orthogonality). The only exceptions are symmetric ICs where symmetry
locks the direction.

Proving ε > 0 generically would strengthen dα/dt ≤ -(1+ε)α² + f(t),
making the Riccati timescale shorter and the per-event ∫α smaller.

But TG (ε = 0) still works if the pressure Hessian provides the
additional restoring force. And our data shows it does (crossover at ρ ≈ 12).

## Lean Formalization

The identity ê·S²·ê = α² + |Dξ/Dt|² could be a third Lean lemma.
It follows from the Pythagorean theorem: |Sê|² = |proj_ê(Sê)|² + |proj_⊥(Sê)|².
This is simpler than the CS inequality and gives the physical interpretation.
