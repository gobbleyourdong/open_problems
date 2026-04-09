---
source: Viscosity attempt — NS (ν>0) combined with unconditional DMP
type: PROOF ATTEMPT #16 — using viscosity to close the gap
date: 2026-03-29
file: 206
---

## The NS Vorticity Equation at the Max

d||ω||∞/dt = α*||ω||∞ + ν(ω·Δω)/|ω| ≤ α*||ω||∞ - ν|∇ω|²/||ω||∞

(Using ω·Δω ≤ -|∇ω|² at the max of |ω|².)

## Two Regimes (from file 203)

HIGH-α (α/|S| > 0.095): DMP holds. α decreases. Stretching stops.
LOW-α (α/|S| < 0.095): α ≤ 0.048||ω||∞ (at attractor). Stretching:

d||ω||∞/dt ≤ 0.048||ω||∞² - ν|∇ω|²/||ω||∞

## The Gradient Estimate

At the max, the gradient |∇ω|² depends on the CONCENTRATION of ω.

LOWER BOUND on |∇ω|² at a max: from Δ|ω|² = 2|∇ω|² + 2ω·Δω ≤ 0:
|∇ω|² ≥ -ω·Δω ≥ 0 (trivially).

But we need a POSITIVE lower bound. From the interpolation:
||ω||∞ ≤ C||ω||₂^{1-3/(2p)} ||∇ω||₂^{3/(2p)} (Gagliardo-Nirenberg, 3D)

Wait, this bounds ||ω||∞ from ABOVE in terms of ||∇ω||₂, not the pointwise
|∇ω|² at the max.

The POINTWISE bound: |∇ω(x*)| ≥ ... is hard to establish without
knowing the spatial structure of ω near x*.

## The Tube Scaling Argument

IF ω is concentrated in a tube of width σ at the max:
|∇ω|_max ≈ ||ω||∞/σ → |∇ω|² ≈ ||ω||∞²/σ².

With Kelvin: σ² = Γ/(π||ω||∞):
|∇ω|² ≈ π||ω||∞³/Γ.

Viscous term: ν×π||ω||∞³/(Γ×||ω||∞) = νπ||ω||∞²/Γ.

d||ω||∞/dt ≤ (0.048 - νπ/Γ)||ω||∞².

For ν > 0.048Γ/π ≈ 0.015Γ: d||ω||/dt < 0 → ||ω|| DECREASING.

## The Problem

1. The tube scaling assumes tube-like structure. General flows might
   have BROAD maxima (large σ, small |∇ω|²).

2. Γ depends on the solution. For fixed initial data: Γ is bounded.
   But the bound gives regularity only for ν > CΓ(u₀), not universally.

3. The scaling |∇ω|² ~ ||ω||³ and stretching ~ ||ω||² give the SAME
   power of ||ω|| in both terms (||ω||²). The viscous advantage is only
   in the constant (ν/Γ), not the scaling.

## What Would Close It

For ν > 0 to guarantee regularity: need |∇ω|² at the max to grow
FASTER than ||ω||∞² as ||ω|| → ∞. Specifically:

  |∇ω|²_max ≥ C||ω||∞^{2+δ} for some δ > 0.

Then: viscous term ~ ν||ω||^{1+δ} vs stretching ~ ||ω||².
For δ > 1: viscosity dominates at large ||ω||.
For δ = 1 (tube scaling): same power, constant competition.
For δ < 1: stretching dominates.

From the tube scaling with attractor: |∇ω|² ~ ||ω||³ → δ = 1.
EXACTLY CRITICAL. Again.

## Can δ > 1?

If the core thins FASTER than Kelvin: σ → 0 faster than 1/√||ω||.
This would give |∇ω|² growing faster than ||ω||³ → δ > 1 → viscosity wins.

Super-Kelvin thinning: could happen if the STRAIN compresses the core
faster than stretching extends the tube. From the attractor: |S| ~ ||ω||/2.
The compression rate: σ' ~ -|S|σ ~ -||ω||σ/2.
The Kelvin balance: σ'_Kelvin ~ -α_tube σ/2 (from tube stretching).

If compression > Kelvin: σ thins faster → δ > 1 → viscosity wins.

This requires the PERPENDICULAR strain (compression of the core)
to exceed the PARALLEL strain (tube stretching). From the alignment:
perp compression = -(λ₁+λ₃)/2 (average of ⊥ω eigenvalues).
par stretching = α.

For α/|S| < 0.095: the par stretching is small. The perp compression
is large (from the trace-free constraint: λ₁+λ₃ = -λ₂ → perp = λ₂/2).

If λ₂ > 0 (positive intermediate eigenvalue, typical in turbulence):
perp compression = -λ₂/2... wait, λ₁+λ₃ = -λ₂. If ω is near e₂:
the ⊥ω eigenvalues are λ₁ and λ₃. The area element ⊥ω:
dA/dt = (λ₁+λ₃)A = -λ₂A.

If λ₂ > 0: dA/dt < 0 → core SHRINKS → super-Kelvin concentration.
If λ₂ < 0: dA/dt > 0 → core GROWS → sub-Kelvin.

In typical turbulence: λ₂ > 0 (positive intermediate eigenvalue).
This gives super-Kelvin thinning → |∇ω|² grows faster than ||ω||³
→ δ > 1 → viscosity WINS → REGULARITY!

## The Chain

1. Ashurst alignment: ω near e₂ (well-established).
2. ⊥ω eigenvalues: λ₁ + λ₃ = -λ₂.
3. λ₂ > 0 (positive intermediate, typical): dA_⊥/dt = -λ₂A_⊥ < 0.
4. Core area SHRINKS: σ² → 0 faster than Kelvin (super-Kelvin).
5. |∇ω|² grows faster than ||ω||³ (δ > 1).
6. Viscous term: ν||ω||^{1+δ} beats stretching ||ω||² for large ||ω||.
7. ||ω||∞ bounded → regularity.

## The Gap in This Chain

Step 3: λ₂ > 0. In typical turbulence this holds (measured).
But λ₂ can be negative (in regions of 2D-like strain).

Step 1: Ashurst alignment. Same as file 202.

AGAIN: the proof needs Ashurst alignment + positive λ₂.
Both are MEASURED but UNPROVEN from the PDE.

## 206. Viscosity helps but doesn't close without alignment.
## The critical scaling (both ||ω||²) is the same wall.
