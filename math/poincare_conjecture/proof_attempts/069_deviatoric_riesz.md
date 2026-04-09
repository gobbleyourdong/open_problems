---
source: Riesz transform analysis of deviatoric pressure Hessian
type: ANALYTICAL INSIGHT — H^D is a Riesz transform of f(y)-f(x*)
status: Connects deviatoric part to SHAPE anisotropy of vorticity max
date: 2026-03-26 cycle 16
---

## The Deviatoric Pressure Hessian as Riesz Transform

H^D_ij(x*) = PV ∫ R_ij(x*-y) (f(y) - f(x*)) dy

where f = |ω|²/2 - |S|² and R_ij is the traceless Riesz kernel.

Key: f(x*) drops out (Riesz of constant = 0 on T³).

## The Source f(y) - f(x*) ≤ 0 Near x*

Since |ω(x*)| = ρ (max): |ω(y)|² - ρ² ≤ 0 for all y.
So f(y) - f(x*) = (|ω(y)|² - ρ²)/2 - (|S(y)|² - |S(x*)|²) ≤ (negative) + (bounded).

Near x*: f drops below f(x*) — the source is NEGATIVE in a neighborhood.

## The Deviatoric Part Depends on SHAPE, Not Just Magnitude

For an isotropic blob of negative f: Riesz transform gives H^D = 0.
For an anisotropic filament: Riesz gives H^D proportional to the anisotropy.

The filament geometry controls |H^D|:
- Round blob: |H^D| = 0 (isotropic → deviatoric zero)
- Long thin filament: |H^D| ~ ρ² × (aspect ratio / some power)
- The SHAPE determines the ratio |H^D|/H^I

## Connection to Buaria & Pumir

Their finding |H^D| ~ ρ^{2γ} with γ < 1 means:
the anisotropy (shape factor) DECREASES with ρ.

Physical interpretation: as vorticity intensifies:
1. The filament becomes MORE circular in cross-section (less anisotropic)
2. The anti-twist mechanism rounds out the filament
3. The Riesz transform sees a more isotropic source → |H^D| grows subquadratically

This is the geometric content of the anti-twist:
**the pressure dynamics isotropize the vorticity maximum region**.

## What Would Close the Proof

Prove: as ρ → ∞, the vorticity maximum region becomes more isotropic
(aspect ratio → 1, or some measure of anisotropy → 0).

This is a GEOMETRIC statement about the shape of super-level sets,
closely related to Grujić's (2012) filament geometry arguments.

From our data:
- At low ρ: TG is highly anisotropic (vortex sheet, aspect ratio >> 1)
- At high ρ: pressure isotropizes → |H^D|/H^I decreases → crossover

The proof needs: isotropization is a CONSEQUENCE of the NS dynamics
(not just an observed tendency). The pressure Poisson equation forces
the isotropization because the source f = |ω|²/2 - |S|² is dominated
by the isotropic |ω|² term at high ρ.

## Status

This is a FRAMEWORK, not a proof. The connection between:
- Deviatoric H ↔ Riesz transform ↔ anisotropy of f near x*
- Anisotropy ↔ filament shape ↔ anti-twist mechanism
- Shape dynamics ↔ pressure Poisson equation ↔ isotropization

is conceptually clear but quantitatively unproven.
The measurement of f's spatial structure (running on CPU) will show
whether the anisotropy decreases with ρ as predicted.
