---
source: THE PROOF ATTEMPT — NS regularity via CKN + isotropy + Seregin
type: PROOF — combining three existing results with the isotropy mechanism
date: 2026-03-29
file: 219
---

## THEOREM: Smooth solutions to 3D incompressible Navier-Stokes on T³
## with smooth initial data remain smooth for all finite time.

## PROOF (by contradiction):

Assume the first singularity occurs at (x*, T*).

### STEP 1: Classification by Type.

By Beale-Kato-Majda (1984): ||ω(t)||∞ → ∞ as t → T*.

EITHER:
(a) Type I: ||ω(t)||∞ ≤ C(T*-t)^{-1/2} (parabolic rate)
(b) Type II: limsup (T*-t)^{1/2} ||ω(t)||∞ = ∞ (faster than parabolic)

### STEP 2: Type I is impossible.

By Seregin (2012) [1]: Smooth NS solutions cannot develop Type I
singularities. The rescaled profile converges to an ancient solution
that vanishes at T*, and backward uniqueness forces it to be zero. ∎

### STEP 3: Type II forces super-concentration.

For Type II: there exist times tₙ → T* with ||ω(tₙ)||∞ (T*-tₙ)^{1/2} → ∞.

At time tₙ: the vorticity is concentrated in a region of radius
  Rₙ ≤ C||ω(tₙ)||∞^{-1} → 0
(from dimensional analysis: the concentration scale is 1/||ω||∞).

The source f = Δp = |ω|²/2 - |S|² is concentrated in the SAME region
(since |S| ≤ C||ω|| from the Biot-Savart law on T³).

### STEP 4: Concentration → isotropy of pressure Hessian.

At x* (the blowup point), decompose f into multipoles:
  f(x*+y) = f₀₀(|y|) + Σ_{l≥1} f_l(|y|) Y_l(ŷ) (spherical harmonics)

The l=0 (monopole) part: f₀₀ = (1/4π)∫f dΩ (angular average).
The l≥1 parts: the anisotropic corrections.

The CZ kernel for H_dev: K(y) ~ P₂(cosθ)/|y|³ (l=2 harmonic).
By orthogonality: K only couples to the l=2 part of f.

H_dev(x*) = ∫ K(y) f₂(|y|) Y₂(ŷ) d³y

The l=2 content of f relative to l=0:
  |f₂|/|f₀₀| ≤ (anisotropy ratio of the concentration region)

CLAIM: As Rₙ → 0 (concentration tightens), the anisotropy ratio → 0.

PROOF OF CLAIM: The source f = |ω|²/2 - |S|² at scale Rₙ.
At the smallest resolved scale (Rₙ → 0): the NS viscous smoothing
isotropizes the solution. Specifically: for NS with ν > 0, the
solution within the concentration ball of radius Rₙ satisfies
|∇f| ≤ C/Rₙ² (controlled by the NS regularity up to T*).

The anisotropy of f within the ball: |f₂|/|f₀₀| ≤ C × Rₙ/L
where L is the scale at which anisotropy is O(1) (the tube length).

As Rₙ → 0: |f₂|/|f₀₀| → 0 → H_dev → 0 → H_ωω → Δp/3 > 0.

### STEP 5: Isotropy prevents Type II growth rate.

Near the singularity: H_ωω ≈ Δp/3 = |ω|²/12 (from isotropy).

The Lagrangian Riccati at x*:
  Dα/Dt = S²ê - 2α² - H_ωω ≤ |S|² - 2α² - |ω|²/12

At the |ω|²/|S|² ≈ 4 attractor: |S|² = |ω|²/4.
  Dα/Dt ≤ |ω|²/4 - 2α² - |ω|²/12 = |ω|²/6 - 2α²

Equilibrium: α_eq = |ω|/(2√3) ≈ 0.29|ω|. For α > α_eq: Dα/Dt < 0.

So: α is bounded above by C||ω||∞ (proportional, not unbounded).

Growth rate: d||ω||∞/dt = α||ω||∞ ≤ C||ω||∞²
→ ||ω||∞ ≤ C/(T*-t) (Type I rate).

But we ASSUMED Type II: ||ω||∞ >> C/(T*-t)^{1/2}. The bound ||ω|| ≤ C/(T*-t)
is CONSISTENT with Type II... wait.

CORRECTION: Type II means ||ω|| grows FASTER than (T*-t)^{-1/2}.
||ω|| ≤ C/(T*-t) is Type I (which is faster than (T*-t)^{-1/2}).
So the bound doesn't contradict Type II — it shows Type II
implies TYPE I RATE at worst.

### STEP 5 (corrected): The α bound prevents SUPER-TYPE-I growth.

For Type II: ||ω||∞ ≥ C(T*-t)^{-1/2-δ} for some δ > 0.

From the isotropy: α ≤ α_eq = ||ω||/(2√3).
d||ω||/dt = α||ω|| ≤ ||ω||²/(2√3).
→ ||ω|| ≤ 2√3/(T*-t) (Type I rate, bounded constant).

But for Type II: ||ω|| ≥ C(T*-t)^{-1/2-δ} which for δ > 0
is o((T*-t)^{-1}) only if T*-t is small enough...

Actually: (T*-t)^{-1/2-δ} vs (T*-t)^{-1}: for 1/2+δ < 1 (i.e., δ < 1/2):
the Type II rate is SLOWER than our Type I bound. No contradiction.

For δ ≥ 1/2: (T*-t)^{-1} or faster. Our bound gives (T*-t)^{-1} exactly.
So Type II with δ ≥ 1/2 gives ||ω|| ~ (T*-t)^{-1}, which IS Type I.

Hmm, the standard definition:
  Type I: ||ω|| ≤ C(T*-t)^{-1/2}
  Type II: NOT Type I, i.e., limsup (T*-t)^{1/2}||ω|| = ∞

Our bound: ||ω|| ≤ C(T*-t)^{-1}. This allows ||ω||(T*-t)^{1/2} ≤ C(T*-t)^{-1/2} → ∞.
So our bound is CONSISTENT with Type II (the blowup rate (T*-t)^{-1}
has (T*-t)^{1/2}||ω|| ~ (T*-t)^{-1/2} → ∞ = Type II).

### THE PROBLEM

The isotropy argument gives ||ω|| ≤ C/(T*-t) which IS a blowup (Type I rate).
It doesn't prevent blowup — it just caps the rate.

But ||ω|| ~ C/(T*-t) gives ∫||ω||dt ~ C log(1/(T*-t)) → ∞ (BKM diverges).
So this rate DOES blow up in the BKM sense.

The isotropy argument CAPS α at C||ω|| (proportional) but doesn't
make α BOUNDED (independent of ||ω||). The proportional bound
still allows quadratic growth → BKM blowup.

### WHAT'S NEEDED TO CLOSE

Need: α bounded by a CONSTANT (not proportional to ||ω||).
The isotropy argument gives: α ≤ ||ω||/(2√3) (proportional).
This is NOT enough — it's the SAME scaling as the generic bound α ≤ |S| ≤ ||ω||/2.

The 2√3 factor is an IMPROVEMENT over 2 (from the isotropy gaining |ω|²/12
back from the pressure), but it's still proportional to ||ω||.

### WHY THE ARGUMENT FALLS SHORT

The isotropy makes H_ωω = |ω|²/12 (positive, proportional to |ω|²).
But the S²ê term is ALSO |ω|²/4 (proportional to |ω|²).
The difference: |ω|²/4 - |ω|²/12 = |ω|²/6 (still O(|ω|²)).
The Riccati equilibrium: 2α² = |ω|²/6 → α = |ω|/√12 → still proportional.

For α to be BOUNDED: need H_ωω > S²ê (not just H_ωω > 0).
The isotropy gives H_ωω = |ω|²/12. We need S²ê < |ω|²/12.
But S²ê can be up to |S|² = |ω|²/4 > |ω|²/12.

The gap: S²ê ≤ |ω|²/4 is too LOOSE. The actual S²ê ≈ |ω|²/100
(from Ashurst alignment). But proving S²ê << |ω|²/12 requires
the alignment condition again.

## VERDICT

The CKN + isotropy argument improves the constant (from α ≤ |ω|/2
to α ≤ |ω|/3.5) but doesn't change the SCALING (still proportional).

To close: need either
(a) S²ê < |ω|²/12 (requires Ashurst alignment + stronger variance bound)
(b) H_ωω > |ω|²/4 (requires the source to be more than 1/3 of Δp)

Neither is provided by the isotropy argument alone.

## 219. The CKN + isotropy argument IMPROVES the bound but doesn't close.
## The proportional scaling α ~ ||ω|| survives. Still need alignment.
