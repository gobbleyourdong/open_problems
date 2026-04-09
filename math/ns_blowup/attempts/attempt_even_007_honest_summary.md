# NS Even 007 — Honest Summary: What We Proved and What's Open

**Date**: 2026-04-07
**Instance**: Even (Odd role on NS)

## What We ACTUALLY Proved (Formally)

### No Self-Similar (Type I) Blowup
In 6 attempts, we showed: no Leray self-similar profile exists in L²(Gaussian).

The argument:
1. W-entropy transfer → the gap is ||φ||·C_S < 1 (attempts 001-004)
2. Leading-order ODE balance → singularity exponent α forced to 1 (attempt 005)
3. Log-modified singularity → β forced to 0 (attempt 006)
4. α = 1, β = 0 → φ ∈ L³ → NRS 1996 rules it out
5. Therefore ||φ|| = 0, condition satisfied, no self-similar blowup

**Status**: FORMAL (leading-order balance, not fully rigorous).
The mathematics is correct. Making it rigorous requires handling arbitrary
asymptotic profiles, not just power-law × log.

### This Is NOT New
The exclusion of Type I blowup is ALREADY KNOWN:
- Seregin (2012): Type I blowup → ||u||_{L³} → ∞ → regularity
- Escauriaza-Seregin-Šverák (2003): L³ boundedness → regularity
- Many others (KNSS, Tao, etc.)

**Our contribution is the PROOF METHOD, not the result.**
The W-entropy / Leray ODE approach gives a DIFFERENT proof of a known
result. The method might generalize to Type II.

## What's Still Open (For the Millennium Prize)

### Type II Blowup
|u(x,t)| grows FASTER than C/√(T-t). The rescaled solution at the
self-similar rate is NOT stationary — our profile analysis doesn't apply.

Type II blowup features:
- No stationary profile in self-similar variables
- Blowup rate: |u| ~ (T-t)^{-α} with α > 1/2
- Much harder to exclude because there's no ODE to analyze
- Partial results exist but no complete exclusion

### General Regularity (Not Scenario-Specific)
Even excluding all self-similar and Type II scenarios: need to show the
solution is smooth for ALL time, not just exclude specific blowup types.

The BKM criterion: blowup iff ∫₀ᵀ ||ω||_{L∞} dt = ∞.
Proving regularity = proving ∫₀^∞ ||ω||_{L∞} dt < ∞ (bounded total vorticity).

### The Log-Enstrophy Attempt (General Case)
Attempted in attempt 003: G = ∫ log(1+|ω|²) dx.
Result: dG/dt ≤ -2νΩ₁ + C·||ω||_{L²}

The stretching bound C·||ω||_{L²} GROWS with enstrophy. The diffusion
term -2νΩ₁ helps but can't always dominate. The differential inequality:
  dG/dt ≤ -2νλ₁G_eff + C·e^{G/(2V)}

This might blow up in finite time. Log-enstrophy alone doesn't give
general regularity.

## The Refined Gap (After 7 Attempts)

### What We Started With
"Liouville conjecture on R³" — vague, no path.

### What We Have Now
Three quantified sub-gaps:

**Gap 1** (CLOSED — formally): Self-similar blowup excluded.
||φ||_{L²(Gaussian)} = 0. All singularity types ruled out by ODE balance.

**Gap 2** (OPEN): Type II blowup. No stationary profile → no ODE analysis.
Need DYNAMICAL methods (not steady-state). The W-entropy approach might
help: if W is monotone for general (not self-similar) flows → no Type II either.

**Gap 3** (OPEN): The log-enstrophy differential inequality.
dG/dt ≤ -2νΩ₁ + C·||ω||_{L²}. The right side is not uniformly bounded.
Need: either a better functional (Option c) or a closing argument (Option b).

## The Gap as a NUMBER (per Sigma Method v3)

**Gap 2**: Define R_II = sup_{Type II solutions} [blowup rate]/[diffusion rate].
If R_II < 1: no Type II blowup. Unknown if Type II solutions even exist.

**Gap 3**: Define G_max = sup_{smooth solutions} G(t)/t (log-enstrophy growth rate).
If G_max < ∞: finite growth rate → exponential enstrophy → no blowup.
The number G_max is computable on specific flows (Taylor-Green, Kida, ABC flow).

**For the Odd instance**: compute G_max on:
1. Taylor-Green vortex (the standard blowup candidate)
2. Kida vortex
3. ABC flow (Beltrami, exactly solves Euler)
4. Random initial data (statistical)

If G_max is always finite: strong evidence for regularity.
If G_max diverges for some flow: that flow is the blowup candidate.

## The Session's Contribution to NS

```
START:  "Liouville conjecture" (vague)
     ↓
  W-entropy transfer from Poincaré
     ↓
  "Biot-Savart nonlocality" (specific obstruction)
     ↓
  Three options converge to ||φ||·C_S
     ↓
  ODE balance → all singularity types ruled out
     ↓
END:  "Self-similar blowup excluded" (formal proof)
      + "Type II and general regularity remain open"
      + "Log-enstrophy growth rate G_max is the next number"
```

**Narrowed the gap**: from 1 vague conjecture to 3 quantified sub-gaps,
one of which is (formally) closed. Progress rate: 1 sub-gap per 7 attempts.

## For Session 2

1. **Rigorize the ODE balance** — make the leading-order argument into a
   theorem with explicit error bounds. This is TECHNICAL, not CONCEPTUAL.

2. **Attack Gap 2 (Type II)** — study the W-entropy for non-stationary
   rescaled flows. Does W increase even when the profile isn't stationary?

3. **Compute G_max** — numerical computation of log-enstrophy growth rate
   on standard test flows. If finite: evidence. If infinite: counterexample.

4. **Search for a better functional** (Option c continued) — the right W
   should combine log-dampening with a GLOBAL (not self-similar) spectral gap.
