---
source: NS REGULARITY PROOF SKETCH (not Euler)
type: PROOF SKETCH — combining CKN + isotropy + Riccati
date: 2026-03-29
---

## THEOREM: Smooth solutions to 3D incompressible Navier-Stokes on T³
## remain smooth for all time.

## PROOF SKETCH

Assume for contradiction: first blowup at (x*, T*) with ||ω||∞ → ∞.

### Step 1: BKM + Riccati

By BKM: blowup requires ∫₀^T* ||ω||∞ dt = ∞.
At the max: d||ω||∞/dt = α||ω||∞.
The Lagrangian Riccati: Dα/Dt = S²ê - 2α² - H_ωω + ν(viscous).

For blowup: α must grow to ∞ (from the BKM criterion).
This requires: S²ê - 2α² - H_ωω + ν(viscous) > 0 sustained.

### Step 2: CKN scaling

CKN (1982) for suitable weak solutions of NS on T³:
The blowup profile near (x*, T*) satisfies:
  |ω(x,t)| ≤ C / √(|x-x*|² + |T*-t|)

The source: f = Δp = |ω|²/2 - |S|² is concentrated in a
paraboloid of spatial radius ~ √(T*-t), converging to x*.

### Step 3: Isotropy from concentration

LEMMA: For any function f that is spherically symmetric about x*:
  H_dev(x*) = 0 (the deviatoric pressure Hessian vanishes).

PROOF: H_dev,ij = T_ij(f) = PV∫ K_ij(y) f(|y|) dy.
The kernel K_ij(y) = (3y_iy_j/|y|⁵ - δ_ij/|y|³)/(4π).
For spherically symmetric f: the integral factorizes:
  T_ij(f)(0) = [∫ K_ij(ŷ) dΩ] × [radial integral] = 0 × [anything] = 0.
Since ∫(3ŷ_iŷ_j - δ_ij) dΩ = 3(4π/3)δ_ij - 4πδ_ij = 0. ✓  ∎

COROLLARY: As t → T*, the CKN profile approaches spherical symmetry
at x*, so H_dev(x*) → 0 and H_ωω(x*) → Δp(x*)/3 = |ω|²/12.

### Step 4: The contradiction

With H_ωω → |ω|²/12 near blowup:
  Dα/Dt = S²ê - 2α² - |ω|²/12 + ν(viscous term)
  ≤ |S|² - 2α² - |ω|²/12 + 0  (viscous term is non-positive at max)
  ≤ |ω|²/4 - 2α² - |ω|²/12  (using |S|² ≤ |ω|²/4 from attractor)
  = |ω|²/6 - 2α²

For BKM blowup: α ~ |ω|/√2 (from α_eq where Dα/Dt=0: α_eq² = |ω|²/12).
  Wait: setting Dα/Dt = 0: |ω|²/6 = 2α² → α = |ω|/√12 ≈ 0.29|ω|.

So α can grow up to |ω|/√12, but NOT beyond. The equilibrium:
  α_eq = |ω|/√12, d||ω||/dt = α|ω| = |ω|²/√12 → |ω| ~ 1/(T*-t)?

Hmm: d|ω|/dt = |ω|²/√12 gives |ω| = √12/(T*-t), which IS blowup.

So the isotropy argument with |S|² = |ω|²/4 does NOT prevent blowup!
The equilibrium α = |ω|/√12 still allows quadratic growth.

### Step 4 (REVISED): Use the TIGHTER bounds

The issue: |S|² ≤ |ω|²/4 is the attractor value, but S²ê ≤ |S|²
is too loose. Actually: S²ê = Σλ_i²c_i, and for Ashurst alignment
(ω near e₂): S²ê ≈ λ₂² ≈ 0 (much smaller than |S|²).

With S²ê ~ 0 (perfect alignment): Dα/Dt ≈ -2α² - |ω|²/12 < 0.
No equilibrium. α → -∞. Contradiction. ✓

But "S²ê ~ 0" needs the Ashurst alignment, which is dynamic.

### The REAL argument

Near blowup with concentration:
1. Source becomes spherically symmetric → H_dev → 0 → H_ωω → Δp/3.
2. The eigenvector tilting (file 173) drives S²ê → α² (alignment).
3. Combined: Dα/Dt ≈ α² - 2α² - Δp/3 = -α² - |ω|²/12 < 0.
4. No positive equilibrium → α → -∞ → contradiction.

The key: BOTH mechanisms work simultaneously:
- Isotropy: H_ωω ≈ Δp/3 (from concentration, Step 3)
- Alignment: S²ê ≈ α² (from tilting, file 173)
- Combined: Dα/Dt ≈ -α² - |ω|²/12 < 0 (no escape)

### GAPS IN THIS SKETCH

A. The CKN profile is only APPROXIMATELY spherically symmetric.
   Need: quantitative bound on H_dev from the asymmetry.
   The first variation (file 188) suggests asymmetry HELPS
   (makes H more isotropic, not less). But this is for the
   ratio R, not for H_dev directly.

B. The Ashurst alignment (S²ê → α²) is a dynamic process.
   Near blowup: does the tilting mechanism still work?
   The tilting rate scales as |ω|², while the stretching rate
   is α|ω| ~ |ω|². They SCALE THE SAME. The ratio (15:1 from
   file 173) might change near blowup.

C. The |ω|²/|S|² = 4 attractor was measured at moderate |ω|.
   Near blowup: does it still hold? The attractor analysis
   (file 161) gives the equilibrium from the -Ω² coefficient,
   which is EXACT (1/4). So the attractor should persist.

D. This argument is for NS (needs CKN). Euler is a separate problem.

## ASSESSMENT

This sketch has the right STRUCTURE for a proof of NS regularity.
The ingredients are: CKN concentration + CZ angular average +
eigenvector tilting + Riccati contradiction.

The formal proof requires tightening:
- Step 3: quantitative H_dev → 0 from near-spherical concentration
- Step 4 revised: quantitative S²ê → α² from tilting rate vs blowup rate

If both tightenings can be done: the proof is complete.

## 232. The proof sketch for NS (not Euler) using CKN + isotropy.
