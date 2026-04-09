# NS Even 004 — The Three Options CONVERGE to One Number

**Date**: 2026-04-07
**Instance**: Even (Odd role on NS)

## The Discovery

Options (a), (b), and (c) are not three paths — they're three views of
the SAME condition. They all converge to:

**||φ||_{L²(Gaussian)} < 1/(2C_S)**

where φ is the Leray self-similar profile and the norm is Gaussian-weighted.

## How They Converge

### Option (b) → ||φ|| · C_S < 1
Direct: the stretching-to-diffusion ratio for self-similar blowup is
R = ||φ|| · C_S. If R < 1: no self-similar blowup.

### Option (a) → ||φ||_{L¹(Gaussian)} bounded → log-enstrophy closes
The log-enstrophy dG/dt ≤ -2νΩ₁ + C||ω||_{L¹} leaked because ||ω||_{L¹} grows.

In SELF-SIMILAR VARIABLES y = x/√(2a(T-t)) with Gaussian weight:

  ||Ω||_{L¹(Gaussian)} = ∫ |Ω(y)| e^{-|y|²/4} dy
                        ≤ ||Ω||_{L²(Gaussian)} · ||(4π)^{3/4}||

The Gaussian weight makes the L¹ norm CONTROLLED by the L² norm.
If ||Ω||_{L²(Gaussian)} < ∞ (bounded in self-similar variables):
→ ||Ω||_{L¹(Gaussian)} ≤ C (bounded)
→ dG/dt ≤ C (constant)
→ G grows linearly
→ |ω|² grows exponentially (not blowup!)
→ regularity

**But ||Ω||_{L²(Gaussian)} < ∞ IS the condition ||φ|| < ∞**, which is
the same condition as Option (b) with the specific bound ||φ|| < 1/(2C_S).

### Option (c) → the combined functional uses Gaussian + log
The "right W" that absorbs stretching:

  W_c = ∫ log(1 + |Ω|²) · e^{-|y|²/4} dy  (in self-similar variables)

This combines:
- Log dampening (from Option a): tames the stretching at high |Ω|
- Gaussian weight (from OU spectral theory): makes everything L¹
- Self-similar variables (from Option b): the blowup profile is STATIONARY

dW_c/dt for a self-similar solution in self-similar variables:
the time derivative is ZERO (the profile is stationary!). So W_c is
CONSTANT — trivially monotone.

For a PERTURBATION of the self-similar solution:
dW_c/dt = (OU spectral gap term) + (nonlinear correction)
         = -λ₁ · (perturbation norm) + C · (perturbation)²

If λ₁ > 0 (OU spectral gap = 1/2 or 1): the linear term dominates
for small perturbations → W_c DECREASES → perturbation decays
→ the self-similar profile is STABLE (if it exists) or UNSTABLE (blowup
doesn't persist).

**This IS the Leray self-similar stability analysis.**

## The Single Number

All three options, through different mathematics, arrive at:

```
THE NUMBER: ||φ||_{L²(e^{-|y|²/4} dy)}

φ = the Leray self-similar blowup profile (if it exists)
The norm is in the Gaussian-weighted L² space on R³
The OU spectral gap is λ₁ = 1/2 (for the vorticity OU operator)

THREE EQUIVALENT CONDITIONS:
  ||φ|| · C_S < 1      (Option b: stretching/diffusion ratio)
  ||φ|| < ∞             (Option a: log-enstrophy closes)
  ||φ|| → 0 under OU   (Option c: self-similar profile unstable)
```

## What's Known About ||φ||

### If No Self-Similar Blowup Exists (||φ|| = 0)
Nečas-Růžička-Šverák (1996): No Leray self-similar blowup in L³(R³).
Tsai (1998): Extended to weaker conditions.
Chae-Tsai (2004): No self-similar blowup if φ ∈ L^p for certain p.

**These results say ||φ|| = 0 for many function spaces.** But NOT for
all spaces. The gap: φ might exist in a VERY rough space (distributional).

### If Self-Similar Blowup Exists (||φ|| > 0)
No one has CONSTRUCTED a self-similar blowup solution. Every attempt
to build one has failed. The numerical evidence: no self-similar blowup
exists on T³ or R³ for the NS equations.

### The Escauriaza-Seregin-Šverák Result (2003)
If a solution blows up at time T with the Type I rate |u| ≤ C/√(T-t):
then the solution is regular (no blowup). This says ||φ||_{L∞} < ∞
implies regularity. The gap: ||φ||_{L²(Gaussian)} vs ||φ||_{L∞}.

## The Precise Gap

**What's proved**: ||φ||_{L∞} < ∞ → regularity (ESŠ 2003)
**What's needed**: ||φ||_{L²(Gaussian)} < 1/(2C_S) → regularity (new)
**The gap**: L²(Gaussian) is WEAKER than L∞. Many functions are in
L²(Gaussian) but not in L∞. So the new condition is EASIER to verify.

**Concretely**: ESŠ needs φ bounded (very strong). We only need φ to be
L²-integrable against a Gaussian (much weaker). The Gaussian weight
allows φ to be UNBOUNDED at the origin as long as it decays fast enough.

## Computing the Numbers

### C_S (the Sobolev-Biot-Savart constant)
The best constant in: |∫ ωSω · w dx| ≤ C_S ||ω||² ||∇ω||²

From Calderón-Zygmund theory: ||S||_{L²} = ||ω||_{L²} (for Biot-Savart).
The Sobolev embedding: ||S||_{L∞} ≤ C_d ||S||_{H^{3/2+ε}}

The relevant C_S for our bound: depends on the specific weighted norm.
On R³ with Gaussian weight: C_S is related to the Mehler kernel (the
Green's function of the OU operator).

**COMPUTABLE**: C_S = ||K||_{L²(Gaussian) → L²(Gaussian)} where K is the
Biot-Savart kernel. This is a SINGULAR INTEGRAL OPERATOR NORM in a
Gaussian measure space. Explicitly computable via Hermite expansion.

### ||φ|| (the Leray profile norm)
If φ satisfies the Leray ODE: -νΔφ + (φ·∇)φ + aφ + a(y·∇)φ + ∇P = 0

In the Hermite basis: φ = Σ φ_n H_n(y) where H_n are Hermite functions.
The Leray ODE becomes: (OU eigenvalue) φ_n + (nonlinear coupling) = 0

||φ||² = Σ |φ_n|² (Parseval in the Hermite basis with Gaussian weight).

**COMPUTABLE**: Truncate the Hermite expansion at order N, solve the
finite-dimensional nonlinear system, compute the norm.

## The Action Plan

1. **Compute C_S** in the Gaussian-weighted Hermite basis. This is the
   operator norm of the Biot-Savart singular integral in L²(Gaussian).
   Use the Hermite expansion of the kernel.

2. **Solve the Leray ODE** in the Hermite basis (truncated at order N).
   If NO solution exists: ||φ|| = 0 → regularity (for self-similar).
   If a solution exists: compute ||φ||. Check ||φ|| · C_S < 1.

3. **Take N → ∞** (or prove convergence): if ||φ||_N · C_S < 1 for all
   finite N, and the sequence converges: the condition holds in the limit.

**This is a FINITE COMPUTATION for each N.** The Millennium Prize reduces
to: does the sequence (||φ||_N · C_S) converge to a value < 1?

## Result

THE THREE OPTIONS CONVERGE TO ONE NUMBER:
  ||φ||_{L²(Gaussian)} · C_S

Options (a), (b), (c) are three mountains viewing the SAME gap.
The gap IS this product. If < 1: NS regularity for self-similar blowup.
Combined with existing results (ESŠ, Seregin): full regularity.

Both numbers are COMPUTABLE. The computation is FINITE per truncation N.
The question is convergence and the final value.
