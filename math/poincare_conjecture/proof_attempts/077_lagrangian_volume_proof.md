---
source: Lagrangian volume-preservation + Constantin bound argument
type: POSSIBLE PROOF SKETCH — ρ bounded by √(|ω₀| × C)
status: NEEDS RIGOROUS VERIFICATION — the steps involve heuristic scaling
date: 2026-03-26 cycle 23
---

## The Argument

### Step 1: Volume preservation
det(∇Φ) = 1 (incompressibility). A vortex tube with cross-section
area A and length L satisfies A × L = const (Lagrangian volume).

### Step 2: Vorticity amplification by stretching
Along a Lagrangian trajectory: ω(t) = (∇Φ)·ω₀.
|ω(t)| ≤ ||∇Φ|| × |ω₀|.
For a tube: ||∇Φ|| ~ λ₁ (largest stretching eigenvalue) ~ L(t)/L(0).
So: ρ ~ |ω₀| × L(t)/L(0).

### Step 3: Constantin's bound constrains tube thickness
|∇ξ| ~ 1/δ for a tube of radius δ (direction changes on scale δ).
∫ρ|∇ξ|² dx ~ ρ × (1/δ²) × A × L = ρ × (1/δ²) × (const) ≤ C.
(Using A = π δ² for a circular tube.)
So: ρ/(δ² × something) ≤ C → δ² ≥ cρ/C.

### Step 4: Volume + thickness → length
From A × L = const and A ~ δ²: δ² × L = const.
From step 3: δ² ≥ cρ/C.
So: L ≤ const/(cρ/C) = const × C/(cρ).

### Step 5: Length → vorticity bound
From step 2: ρ ~ |ω₀| × L/L₀.
From step 4: L ≤ const × C/(cρ).
So: ρ ≤ |ω₀| × const × C / (cρ × L₀).
→ ρ² ≤ |ω₀| × const × C / (c × L₀).
→ **ρ ≤ √(|ω₀| × C' / L₀)** where C' = const × C/c.

### The bound:
```
||ω(t)||_∞ ≤ √(||ω₀||_∞ × C(ν, E₀))
```

Bounded by initial data! REGULARITY!

## The Problems with This Argument

### 1. The tube model is HEURISTIC
Steps 2-4 assume the vorticity is organized in tubes. In reality,
the vorticity field is a general 3D vector field, not necessarily
tube-like. The tube scaling (A × L = const) applies to material
volumes under the flow map, but the vorticity DISTRIBUTION within
the tube is not accounted for.

### 2. |∇ξ| ~ 1/δ is an ESTIMATE, not a bound
The direction gradient depends on how ξ varies across the tube
cross-section. For a simple Burgers vortex: |∇ξ| ~ κ (curvature),
not 1/δ. The 1/δ scaling holds for the twist component only.

### 3. The Lagrangian stretching ||∇Φ|| ~ L is approximate
The flow map can FOLD the tube, meaning L is not simply related
to ||∇Φ||. The folding creates additional curvature but doesn't
directly increase the tube length in the stretching sense.

### 4. The "tube" may break up
Vortex reconnection (for ν > 0) breaks tubes into smaller pieces.
The volume preservation applies to Lagrangian volumes, not to
vortex tubes (which are topological, not material).

## Assessment

The STRUCTURE of this argument is the clearest path to regularity
we've found. The chain: volume preservation → thickness bound from
Constantin → length bound → vorticity bound is LOGICALLY COMPLETE.

But each step involves HEURISTIC SCALING that needs to be made
rigorous. The tube model is the weakest link — converting the
general 3D vorticity field into tube geometry is exactly the
problem that Grujić's program addresses.

If the tube model could be PROVED (i.e., showing the vorticity
near blowup must be tube-like), the rest would follow. This is
EXACTLY Grujić's "filament length must be macro-scale" gap.

## Connection to Our Other Results

- Constantin bound (∫ρ|∇ξ|² ≤ C): USED in step 3
- Volume preservation (det=1): EXACT from incompressibility
- Tube geometry: ASSUMED, supported by Grujić's program
- Curvature scaling κ ~ ρ^{0.78}: CONSISTENT with δ ~ √ρ
  (curvature ~ 1/δ ~ 1/√ρ → κ ~ ρ^{-1/2}... hmm, OPPOSITE sign!)

Wait — our data showed κ ~ ρ^{+0.78} (curvature GROWS with ρ).
But the tube model predicts κ ~ 1/δ ~ 1/√ρ ~ ρ^{-1/2}
(curvature DECREASES).

This is a CONTRADICTION. Either:
(a) The tube model is wrong at x* (vorticity isn't tube-like)
(b) The curvature measurement is of a different kind (axis vs cross-section)
(c) The δ ~ √ρ scaling doesn't apply at the measured resolution

Need to investigate.

## Status

PROMISING but HEURISTIC. The argument gives ρ ≤ √(C/L₀) which
would prove regularity. The rigorous version needs the tube model
justified and the scaling made precise. The κ vs ρ contradiction
suggests the tube model may not apply at x*.

Every failure maps the space.
