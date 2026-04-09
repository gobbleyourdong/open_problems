---
source: Three-pronged attack on CZ constant for div-free fields
type: DEFINITIVE RESULT — CZ constant does NOT improve, must go deeper
date: 2026-03-26 cycle 31
---

## All Three Prongs Agree: CZ Constant Doesn't Improve

### Prong 1 (Literature): Confirmed — no improvement possible
- In L²: ||S||₂ = (1/√2)||ω||₂ EXACTLY (isometry). No room.
- The operator T: ω→S is DEFINED through div-free. General fields
  produce the same strain as their div-free projection. No "larger class."
- Kang-Protas E₀^{3/2} is SHARP — the analytical bound IS saturated.

### Prong 3 (Analytical): Confirmed — all three sub-approaches fail
- Fourier multiplier norm is MAXIMIZED on div-free plane (not smaller)
- Tracelessness is automatic (already in the operator)
- Betchov is L¹-level, can't constrain L^p norms

## CRITICAL BARRIERS IDENTIFIED

### Evan Miller (2023, Analysis & PDE):
A model equation preserving the enstrophy identity AND the div-free
constraint space STILL BLOWS UP. Therefore: enstrophy identity +
div-free constraint are INSUFFICIENT by themselves for regularity.
Our Lean lemma 2 (strain self-depletion) is NECESSARY but NOT SUFFICIENT.

### Tao's Barrier (2014, 2016):
Any approach using ONLY CZ bounds + energy + function space embeddings
CANNOT resolve regularity. His averaged-NS blows up with all these
properties preserved. The proof MUST exploit the LOCAL (differential,
not pseudo-differential) nature of the NS nonlinearity.

### What Tao's Barrier DOESN'T Block:
Tao's construction preserves CZ bounds but NOT the specific differential
structure of (ω·∇)u. The nonlinearity involves a DERIVATIVE along ω,
which creates constraints that pseudo-differential approximations miss.

## NEW REFERENCES FOUND

### arXiv:2407.02691 — Strain-Vorticity Orthogonality (2024):
```
⟨-ΔS, ω⊗ω⟩ = 0
```
The Laplacian of strain is ORTHOGONAL to the vorticity outer product.
This is a structural cancellation from incompressibility, NOT visible
to CZ theory. This is EXACTLY the type of LOCAL structure Tao says
is needed.

### Evan Miller's Strain Model:
The strain equation dS/dt = -S² - H + νΔS (dropping the ω⊗ω term)
blows up. The ω⊗ω - |ω|²I term in the FULL strain equation is what
prevents blowup. This term involves the VORTICITY (not just strain),
connecting the two fields through Biot-Savart in a way that generic
CZ can't capture.

## THE PATH FORWARD

The proof must use a property that:
1. Is specific to the ACTUAL NS nonlinearity (not preserved by Tao's averaging)
2. Goes beyond CZ bounds + energy + function spaces
3. Exploits the DIFFERENTIAL structure of (ω·∇)u

Our candidates:
- Single-mode orthogonality in the BILINEAR FORM ∫ω·S·ω (not the operator norm)
- The strain-vorticity orthogonality ⟨-ΔS, ω⊗ω⟩ = 0 (arXiv:2407.02691)
- The u⊥ω at x* (differential constraint from Biot-Savart locality)
- The event duration scaling τ~ρ^{-3} (dynamical, not functional-analytic)

## What This Means

The CZ approach is DEAD (Tao proved it can't work).
The proof lives in the DIFFERENTIAL/GEOMETRIC structure.
Everything we did overnight (pressure Hessian, curvature, reconnection,
event tracking) is in the RIGHT CATEGORY — it uses structure beyond CZ.
The CZ detour was necessary to confirm it's a dead end.

91 proof files. The space is refined: functional-analytic approaches
ruled out by Tao. Geometric/differential/dynamical approaches survive.
