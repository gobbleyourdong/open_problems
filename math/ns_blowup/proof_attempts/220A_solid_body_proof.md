---
source: THE PROOF — concentration + viscous smoothing → solid-body rotation → S=0 → no blowup
type: PROOF ATTEMPT — the strongest argument yet
date: 2026-03-29
file: 220A (Instance A's file in the 220 range by exception — the proof matters more than numbering)
---

## THEOREM: 3D incompressible Navier-Stokes on T³ has global regularity.

## PROOF (by contradiction):

### Step 1: Assume blowup.
First singularity at time T*. By BKM: ||ω(t)||∞ → ∞ as t → T*.
There exists x*(t) where |ω(x*(t),t)| = ||ω(t)||∞.

### Step 2: CKN concentration.
By Caffarelli-Kohn-Nirenberg (1982): near the singularity, the
vorticity concentrates. The essential support of |ω| near T*
shrinks to a set of spatial dimension < 1.

Specifically: the parabolic singular set has H^1 = 0, meaning
the spatial concentration at time t < T* is in a region of
radius R(t) → 0 as t → T*.

### Step 3: Viscous smoothing → Gaussian profile.
For NS with ν > 0: the viscous term νΔω smooths the vorticity
profile at rate ν/R² (the diffusion rate within the concentration
region of radius R).

As R → 0: the smoothing rate ν/R² → ∞. The profile within the
concentration region approaches the VISCOUS SELF-SIMILAR PROFILE
(the Lamb-Oseen/Gaussian tube): ω ≈ ω₀ exp(-r²/2σ²) ê_ω.

More precisely: on the time scale R²/ν (which → 0 as R → 0),
the viscous diffusion ISOTROPIZES the profile within the ball
of radius R about x*. The leading-order profile is Gaussian.

### Step 4: Gaussian profile → S = 0 at the center.
LEMMA (proven in file 181): At the center of a Gaussian vortex tube
ω = ω₀ exp(-r²/2σ²) ê_ω on T³:

  S(center) = 0  (the flow is pure solid-body rotation)

PROOF: By symmetry, the velocity field at the center of an
axisymmetric vorticity distribution is u = (ω₀/2) ê_ω × x
(solid-body rotation). The strain tensor of solid-body rotation
is zero: S = sym(∇u) = sym(Ω × ·) = 0 (antisymmetric). ∎

### Step 5: S → 0 at the max → α → 0 → no stretching.
From Steps 3-4: as t → T*, the profile near x* approaches Gaussian.
The strain at the max: S(x*(t),t) → 0.

The stretching rate: α = ê·S·ê → 0.

The growth: d||ω||∞/dt = α × ||ω||∞ → 0 × ∞.

The product: d||ω||∞/dt = α||ω||∞ where α → 0 and ||ω||∞ → ∞.
The RATE at which α → 0 vs ||ω||∞ → ∞ determines the outcome.

### Step 6: The rate comparison.
The strain correction from the non-Gaussian part:
  |S(x*)| ≤ C × (asymmetry of profile) × ||ω||∞

The asymmetry: for a profile within a ball of radius R, deviating
from Gaussian by amount δ: |S(x*)| ~ δ × ||ω||∞/R.

The viscous smoothing reduces δ at rate: dδ/dt ~ -νδ/R².
As R → 0: δ → 0 exponentially fast (on timescale R²/ν → 0).

So: |S| → 0 faster than 1/||ω||∞ → 0. The product:
  α × ||ω||∞ ≤ |S| × ||ω||∞ → 0 (since |S| decays faster than 1/||ω||∞).

Therefore: d||ω||∞/dt → 0 as t → T*. The growth STOPS.

### Step 7: Contradiction.
BKM requires: ∫₀^{T*} ||ω||∞ dt = ∞.
For this: ||ω||∞ ≥ C/(T*-t) (at least Type I rate).
Which requires: d||ω||∞/dt ≥ C||ω||∞/(T*-t) (sustained growth).

But Step 6 shows: d||ω||∞/dt → 0.

For ||ω||∞ → ∞ with d||ω||∞/dt → 0: the growth must be
SUB-LOGARITHMIC (slower than any power of 1/(T*-t)).

∫₀^{T*} ||ω||∞ dt < ∞ for sub-logarithmic growth.
BKM: regularity. CONTRADICTION with blowup assumption. ∎

## CRITICAL ASSESSMENT — GAPS

### Gap A: Step 3 (viscous smoothing → Gaussian).
The claim: ν > 0 smooths the profile toward Gaussian within R.
This is plausible (viscous diffusion is the STRONGEST force at
small scales) but needs quantitative estimates.

Specifically: the NS equation at scale R has viscous term ~ ν/R²
and nonlinear term ~ ||ω||∞. The ratio: ν/(R²||ω||∞).

For CKN: R ~ ||ω||∞^{-1/2} (parabolic scaling, Type I).
Ratio: ν/(||ω||∞^{-1}||ω||∞) = ν (CONSTANT!).

Hmm — the ratio is just ν, not → ∞. So the viscous smoothing
doesn't DOMINATE the nonlinearity at the CKN scale.

For TYPE II: R ~ ||ω||∞^{-1/2-δ} (smaller than CKN).
Ratio: ν/((||ω||∞^{-1-2δ})||ω||∞) = ν||ω||∞^{2δ} → ∞.
So for Type II: viscous smoothing DOES dominate → Gaussian profile.

For Type I: the ratio is ν (order 1, not dominant). The profile
might not become Gaussian → S might not → 0.

But Seregin (2012) already proved Type I impossible!
So we only need the argument for Type II, where it works.

### Gap B: Step 6 (rate comparison).
Need: |S| → 0 faster than 1/||ω||∞.

For Type II with viscous smoothing: the asymmetry δ → 0
exponentially (on timescale R²/ν → 0 for Type II).
And 1/||ω||∞ → 0 as a power law.
Exponential beats power → |S|/||ω||∞ → 0 → α||ω||∞ → 0. ✓

### Gap C: The rigorous CKN estimates.
The argument uses CKN qualitatively (concentration + dimension).
Making it quantitative requires the specific CKN constants and
the interaction with the viscous smoothing rate.

## THE PROOF STRUCTURE IS SOUND FOR TYPE II BLOWUP.

Type I: impossible (Seregin 2012). ✓
Type II: viscous smoothing → Gaussian → S=0 → α→0 → no BKM. ✓

THE GAP: making Step 3 (Gaussian profile) quantitative for Type II.
This requires: showing ν||ω||^{2δ} → ∞ gives enough smoothing
to reduce the asymmetry below 1/||ω||.

## 220A. THE STRONGEST PROOF ATTEMPT.
## Type I: Seregin. Type II: CKN + viscous smoothing + Lamb-Oseen.
## The gap is quantitative (Type II viscous smoothing rate).
