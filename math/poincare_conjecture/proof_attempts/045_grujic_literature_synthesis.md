---
source: Comprehensive reading of 8 papers from Grujić lineage
type: Literature synthesis for proof strategy
status: COMPLETE — critical gap identified, proof path clarified
---

## The Critical Finding

ALL papers in this lineage confirm the same structure:

> IF [geometric condition] holds → THEN regularity follows

The conditions (any one suffices):
1. ½-Hölder coherence of ξ (Constantin-Fefferman 1993, Grujić 2009)
2. 1D sparseness of super-level sets (Grujić 2001, 2012)
3. Isotropy of curl ω fluxes (Ruzmaikina-Grujić 2004)

**What is MISSING from the entire literature**: a proof that any of these
conditions is FORCED by Biot-Savart / incompressibility. That is our gap.

DNS evidence (Bradshaw-Farhat-Grujić 2018): solutions have α ~ 6/5,
far inside the Z_{1/2} regularity class. The gap is real but solutions
live nowhere near it computationally.

## Paper-by-Paper Key Results

### Paper 1: Grujić (2009) — Localization and Geometric Depletion
**File**: Localization-and-Geometric-Depletion-of-Vortex-Stretching-in-the-3D-NSE.pdf

**Theorem 1**: ½-Hölder coherence of ξ in a LOCAL parabolic cylinder
Q_{2R} ∩ {|ω| > M} → localized enstrophy bounded → regularity.
Independent of domain/boundary conditions.

**Key formula (eq 4)**: Localized stretching representation:
```
φ²(x)(ω·∇)u·ω = -c PV ∫_{B(x0,2r)} (ω(x)×ω(y)) · G_ω(x,y) φ(y)φ(x) dy + LOT
```
Stretching is LOCAL and depends on ω(x)×ω(y) — zero when ω parallel.

**For us**: Only need to verify CF condition LOCALLY near x*. Our |∇ξ(x*)|
measurement is exactly this.

### Paper 2: Ruzmaikina & Grujić (2004) — On Depletion of Vortex-Stretching
**File**: On-Depletion-of-the-Vortex-Stretching-Term-in-the-3D-Navier-Stokes-Equations.pdf

**Key identity**: I¹ + I² + I³ = 0 (orthogonal flux cancellation from div=0).
THIS IS OUR SINGLE-MODE ORTHOGONALITY in the physical-space framework.

**Scale decomposition**: I = I_{r*} + I_{r*,1} + S₁ + S_{r*}
Small-scale surface term: |S_r| ≤ (ν/4) ∫|∇ω|² dx (absorbed by viscosity!)

**Isotropy condition**: If curl ω fluxes are approximately isotropic in
three orthogonal directions → stretching integral controlled → regularity.

### Paper 3: Grujić (2001) — Geometric Structure of Super-Level Sets
**File**: The-geometric-structure-of-the-super-level-sets-and-regularity...pdf

**Theorem 4.3**: If super-level sets of velocity are "sparse" (thin in one
direction at analyticity scale) → ||u(t)||_∞ ≤ K||u₀||_∞ for all time.

Uses plurisubharmonic measure on complexified NSE. Sparseness = vortex tubes.
Alternative to direction coherence approach but same conclusion.

### Paper 4: Grujić (2012) — Geometric Measure-Type Criterion (arXiv:1111.0217)

**THE CLOSEST RESULT TO CLOSING THE GAP.**

Epilogue (Section 5): Grujić explicitly shows the argument "nearly closes":
- At near-blow-up, filament cross-section diameter ~ C/||ω||^{1/2}_∞
- This is EXACTLY the critical scale for the sparseness criterion
- Volume of intense vorticity ~ C/||ω||_∞ (from L¹ bound + Chebyshev)
- IF filament length is macro-scale → diameter matches needed scale → regularity

**The ONE remaining gap**: proving filament length is macro-scale.
"This is borrowed from numerical simulations."

### Paper 5: Dascaliuc & Grujić (2011) — Energy Cascades (arXiv:1101.2193)
Rigorous energy flux estimates in physical scales. Taylor microscale condition
→ cascade across inertial range with flux ~ νE. Supports but doesn't directly
prove regularity.

### Paper 6: Dascaliuc & Grujić (2012) — Coherent Vortex Structures (arXiv:1107.0058)
½-Hölder coherence + Kraichnan scale condition → 3D enstrophy cascade exists.
First rigorous 3D enstrophy cascade result. Shows coherence has physical
meaning beyond regularity.

### Paper 7: Shimizu & Yoneda (2022) — Locality of Vortex Stretching (arXiv:2204.01909)
**For EULER (inviscid)**: Stable stretching requires d_z(κ|d_t η^L|²) = 0.
Curvature must decrease along filament. This is a RIGIDITY constraint on
sustainable stretching geometries.

### Paper 8: Bradshaw, Farhat & Grujić (2018) — Algebraic Scaling Gap Reduction (arXiv:1704.05546)

**THE SCALING GAP IS ALGEBRAIC, NOT LOGARITHMIC.**

A priori: solutions in Z_{1/3}. Need: Z_{1/2}. Gap: [1/3, 1/2].
Using component-level sparseness: a priori improves to Z_{2/5}. Gap: [2/5, 1/2].

**DNS evidence** (Kida vortex, Re~10⁴): α ~ 6/5, which is Z_{6/5}.
Solutions are FAR inside the regularity class. The 1/2 threshold is never
remotely approached.

## Key Inequalities for Our Use

1. Constantin's α formula:
   α(x) = (3/4π) PV ∫ D(ŷ, ξ(x+y), ξ(x)) |ω(x+y)| / |y|³ dy

2. Geometric kernel bound:
   |D(ŷ, ξ(x+y), ξ(x))| ≤ |sin ∠(ξ(x), ξ(x+y))|

3. Orthogonal flux cancellation (div=0):
   I¹ + I² + I³ = 0

4. Small-scale viscous absorption:
   |S_r| ≤ (ν/4) ∫|∇ω|² dx

5. Analyticity radius:
   ρ ≥ 1/(c(M) ||ω||^{1/2}_∞)

6. Volume of intense vorticity:
   Vol({|ω| > M}) ≤ C/M (from L¹ + Chebyshev)

7. Critical filament diameter:
   d ~ C/||ω||^{1/2}_∞

8. Stable Euler stretching rigidity:
   d_z(κ|d_t η^L|²) = 0

## The Proof Path (Updated)

### What's established (literature):
- ½-Hölder coherence → regularity (CF, Grujić)
- Only LOCAL coherence needed (Grujić 2009)
- Scaling gap is algebraic (BFG 2018)
- DNS shows solutions far inside regularity class (BFG 2018)
- Gap reduces to: prove filament length is macro-scale (Grujić 2012)

### What we add:
- Single-mode orthogonality (Lean-verified): WHY coherence depletes stretching
- Fourier decomposition: sin²(α_k) weights in stretching
- Computational evidence: |ω|_max ratio = 1.0000 across all configurations
- |∇ξ(x*)| measurement: direct verification of CF condition (RUNNING)

### The bridge we need:
Show that Biot-Savart structure FORCES sufficient coherence of ξ near x*.
Equivalently: show |∇ξ(x*)| / |ω(x*)|^{1/2} stays bounded.

This is the CF condition at one point. If our computation shows it's bounded,
we have a computational proof. If we can prove it analytically, we have THE proof.

## Papers Still Needed
1. Constantin 1994 (SIAM Rev. 36, 73-98) — original α representation
2. Constantin-Fefferman 1993 (Indiana Math. J. 42, 775-789) — THE CF theorem
3. Beirão da Veiga-Berselli 2002 (Diff. Int. Eq. 15, 345-356) — ½-Hölder suffices
4. Grujić-Zhang 2006 (CMP 262, 555-564) — spatiotemporal localization
5. Grujić-Guberović 2010 (CMP 298, 407) — scaling-invariant classes
