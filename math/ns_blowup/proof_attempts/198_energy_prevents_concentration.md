---
source: Energy conservation prevents vortex concentration → regularity?
type: PROOF ATTEMPT #15 — topological/energy argument
date: 2026-03-29
---

## The Argument

For blowup: ||ω||∞ → ∞ requires vorticity CONCENTRATION.
By Kelvin: |ω|σ² = Γ (conserved), so σ² = Γ/|ω| → 0.

A vortex tube of circulation Γ, core width σ, length L has
kinetic energy (from Biot-Savart self-induction):

  E_tube ≈ (Γ²L/4π) × ln(L/σ) + O(1)

As σ → 0 (concentration): E_tube → ∞ (logarithmic divergence).

But: kinetic energy E_kin = (1/2)∫|u|² is CONSERVED in Euler.

Therefore: σ cannot go to zero. More precisely:
  σ ≥ L × exp(-4πE_kin/(Γ²L))

This gives a LOWER BOUND on σ (positive).

And: ||ω||∞ = Γ/(πσ²) ≤ Γ/(πL²) × exp(8πE_kin/(Γ²L))

This is a FINITE upper bound on ||ω||∞!

## Does This Work?

The argument assumes:
1. Vorticity concentrates into a SINGLE tube of circulation Γ.
2. The tube has well-defined core width σ and length L.
3. The self-induction energy formula applies.
4. L stays bounded (the tube doesn't stretch to infinite length).

PROBLEM with assumption 4: the tube LENGTH L can grow!

In Euler: the vortex line length grows (stretching). The stretching
rate is dL/dt = ∫α ds ≤ ||α||_∞ L ≤ (||ω||∞/2) L.

If ||ω||∞ ~ 1/σ² and σ ~ √(Γ/ω) ~ ω^{-1/2}:
dL/dt ~ ω L → L ~ exp(∫ω dt) → BKM integral!

So: L grows exponentially (or faster) as ω grows.
The energy formula: E ~ Γ²L ln(L/σ) grows as L grows.
But E is conserved → L can't grow without bound either.

## The Bootstrap

E = (Γ²L/4π)ln(L/σ) = conserved.

With σ = √(Γ/(πω)): ln(L/σ) = ln(L) + (1/2)ln(πω/Γ).

E = (Γ²L/4π)(ln L + (1/2)ln(πω/Γ))

If ω → ∞: the second term grows as ln(ω). But L might also grow.

Constraint: E = constant. So: Γ²L ln(Lω^{1/2}) ~ constant.

If L grows as L ~ L₀ exp(Ct): Γ²L₀e^{Ct} × (Ct + ln(ω)/2) ~ E.

For large t: L × ln(ω) ~ E/Γ² → ω ~ exp(2E/(Γ²L)) → finite if L stays finite.

But L grows exponentially... so ω ~ exp(2E/(Γ²L₀e^{Ct})) → exp(very small) → 1.

WAIT: if L → ∞: ω → exp(0) = 1? That can't be right.

Let me redo. E = (Γ²L/4π)ln(L√(πω/Γ)).

If L → ∞ and E fixed: need ln(L√ω) → 0, which means L√ω → 1,
i.e., ω → 1/L² → 0 as L → ∞.

But we assumed ω → ∞ (blowup). Contradiction!

## THE PROOF?

If L → ∞ (tube stretches): energy constraint forces ω → 0 (not blowup).
If L stays bounded: energy forces σ bounded → ω bounded (not blowup).

EITHER WAY: ω can't blow up!

## Critical Check: Is the Energy Formula Correct?

The self-induction energy of a vortex tube:
  E = (Γ²/4π) ∫₀^L [ln(L/σ) + C₁] ds

where the integral is over the tube centerline.

For a THIN tube (σ << L): E ≈ (Γ²L/4π)ln(L/σ).
For a THICK tube (σ ~ L): E ≈ Γ²L/4π × O(1).

The formula assumes σ << L (thin tube limit).

PROBLEM: as the tube stretches, the core ALSO thins (Kelvin: σ²ω = Γ).
If L grows by factor K: σ² = Γ/(πω) and the tube volume ~ Lσ².
Conservation of... hmm, what's conserved?

Enstrophy: ∫|ω|² dx ≈ ω² × πσ² × L = ω² × (Γ/ω) × L/π = ωΓL/π.
So enstrophy ≈ ωΓL/π. If enstrophy grows: ωL can grow.

Kinetic energy: E ≈ (Γ²/4π)L ln(L/σ) ≈ (Γ²/4π)L × (1/2)ln(πω/Γ).

With ωL/π = πE_ω/Γ (from enstrophy = ωΓL/π):
L = πE_ω/(Γω)

Substitute: E_kin = (Γ²/4π) × (πE_ω/(Γω)) × (1/2)ln(πω/Γ)
= (ΓE_ω/(4ω)) × ln(πω/Γ)/2

So: E_kin = ΓE_ω ln(ω)/(8ω) (keeping leading terms)

For ω → ∞: E_kin ~ E_ω ln(ω)/ω. If E_ω grows slower than ω/ln(ω):
E_kin stays bounded → OK.

But E_ω = enstrophy can grow! From the enstrophy equation:
dE_ω/dt = 2∫ω·Sω ≤ 2||ω||_∞ E_ω = 2ω E_ω.

So E_ω ≤ E_ω(0) exp(2∫ω dt). For BKM blowup: ∫ω dt → ∞.
Then E_ω → ∞. And E_kin = ΓE_ω ln(ω)/(8ω).

If E_ω ~ exp(2ω t) and ω growing: E_kin could blow up,
contradicting conservation. Unless ω grows slowly enough.

For E_kin = const: ΓE_ω ln(ω)/(8ω) = const → E_ω = Cω/ln(ω).
From dE_ω/dt ≤ 2ωE_ω: d(Cω/ln ω)/dt ≤ 2ω × Cω/ln ω.
C(ω'/ln ω - ω ω'/(ω ln²ω)) ≤ 2Cω²/ln ω.
ω'(1/ln ω - 1/ln²ω) ≤ 2ω²/ln ω.
ω' ≤ 2ω² × ln ω / (ln ω - 1) ≈ 2ω² (for large ln ω).

So ω' ≤ 2ω² → blowup at T* = 1/(2ω₀). CONTRADICTION
because we derived ω must satisfy E_ω = Cω/ln ω but the
enstrophy equation allows E_ω to grow as exp(2ωt).

The FLAW: the energy formula is for a SINGLE THIN TUBE.
Real flows have complex geometry — multiple tubes, sheets,
reconnections. The simple formula doesn't apply.

## 198. Energy argument: promising but the tube geometry
## assumption is too restrictive. Real flows are more complex.
