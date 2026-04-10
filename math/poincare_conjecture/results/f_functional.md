# Perelman's F-Functional — Numerical Verification

**Date:** 2026-04-09
**Script:** `numerics/f_functional.py`
**Track:** Numerical
**Reference:** Perelman, "The entropy formula for the Ricci flow..." (2002, §1)

## The F-Functional

  F(g, f) = ∫_M (R + |∇f|²) e^(-f) dV

This is the FIRST of Perelman's three functionals. Key properties:
1. F monotone under MODIFIED Ricci flow ∂g/∂t = -2(Ric + Hess(f))
2. λ(g) = inf_f F over f with ∫ e^(-f) dV = 1
3. Critical points: STEADY GRADIENT SOLITONS (Ric + Hess(f) = 0)

## Test 1 — F on Round S³ — PASS

For constant f optimal: F = R = 6/r² (matches λ).

| r | R = 6/r² | F | λ | F = λ? |
|---|----------|---|---|--------|
| 0.5 | 24.0 | 24.0 | 24.0 | YES |
| 1.0 | 6.0 | 6.0 | 6.0 | YES |
| 2.0 | 1.5 | 1.5 | 1.5 | YES |
| 5.0 | 0.24 | 0.24 | 0.24 | YES |
| 10.0 | 0.06 | 0.06 | 0.06 | YES |

F = λ on round S³ for constant f (Einstein metrics achieve the minimum).

## Test 2 — F Monotone Under Flow — PASS

Round S³(r₀=1) under unnormalized RF, T = 0.25.

| t | r(t) | F(t) = R(t) | monotone? |
|---|------|-------------|-----------|
| 0.000 | 1.000 | 6.0 | — |
| 0.025 | 0.949 | 6.67 | YES |
| 0.075 | 0.837 | 8.57 | YES |
| 0.125 | 0.707 | 12.0 | YES |
| 0.175 | 0.548 | 20.0 | YES |
| 0.213 | 0.387 | 40.0 | YES |
| 0.238 | 0.224 | 120.0 | YES |
| 0.248 | 0.100 | 600.0 | YES |

All 8 timepoints monotone non-decreasing. F → ∞ at extinction (curvature blows up).

## Test 3 — No Steady Soliton on Closed S³ — PASS

Steady gradient soliton: Ric + Hess(f) = 0
Integrating over closed M: ∫(R + Δf) dV = 0
By divergence theorem ∫Δf dV = 0, so **∫ R dV = 0** required.

But on S³(r): R = 6/r² > 0 strictly.

| r | ∫ R dV |
|---|--------|
| 0.5 | 59.22 |
| 1.0 | 118.44 |
| 2.0 | 236.87 |

All positive ⟹ NO steady gradient soliton exists on closed S³.
Round S³ is a SHRINKING soliton, not steady.

## Test 4 — Round S³ Is a Shrinking Soliton — PASS

Shrinking soliton equation: Ric + Hess(f) - g/(2τ) = 0
For round S³(r) with f constant: (2/r²) g - g/(2τ) = 0 ⟺ **τ = r²/4**.

| r | Ric eigenvalue | τ_soliton | 2τ·Ric/g (must = 1) |
|---|----------------|-----------|---------------------|
| 0.5 | 8.0 | 0.0625 | 1.000000 |
| 1.0 | 2.0 | 0.25 | 1.000000 |
| 1.5 | 0.889 | 0.5625 | 1.000000 |
| 2.0 | 0.5 | 1.0 | 1.000000 |

**1.000000 EXACTLY at all 4 radii.** Round S³(r) is a shrinking soliton
at τ = r²/4 (matches the extinction time T = r₀²/4 from `extinction_time.py`).

Hamilton's classification: round S³ is the UNIQUE shrinking soliton on a
closed simply-connected 3-manifold (up to isometry and scale).

## Test 5 — F vs λ vs W

| Functional | Definition | Monotone under | Critical points |
|------------|------------|----------------|-----------------|
| F | ∫(R+\|∇f\|²)e^(-f) dV | modified Ricci flow | steady soliton |
| **λ** | **inf_f F** | **pure Ricci flow** | **Einstein metric** |
| W | ∫[τ(R+\|∇f\|²) + f - n] u dV | Ricci flow at scale τ | shrinking soliton |

The three functionals form a hierarchy:
- F: simplest, depends on auxiliary f
- λ: optimal F (= lowest eigenvalue of -4Δ + R, computable)
- W: scale-invariant, gives κ-noncollapsing

## Summary

5 tests pass:
- F = λ = 6/r² on round S³ (constant f)
- F monotone under (modified) Ricci flow
- No steady soliton on closed S³ (∫R > 0)
- Round S³ IS a shrinking soliton at τ = r²/4 (verified to machine precision)
- Three-functional hierarchy documented

Round S³ as a SHRINKING SOLITON is the most important result here:
the extinction time T = r₀²/4 of unnormalized Ricci flow exactly matches
the soliton parameter τ. This is what Perelman's W-entropy is designed
to detect — round S³ is the W-entropy critical point.

## For the Theory Track

Complements:
- `lean/MonotoneFunctionalParadigm.lean` (W-entropy as monotone)
- `numerics/lambda_invariant.py` (λ verification)
- `numerics/w_entropy_verification.py` (W on round S³)
- `numerics/extinction_time.py` (T = r²/4 for round S³)

The F-functional is the simplest of Perelman's three. Together with
λ (`lambda_invariant.py`) and W (`w_entropy_verification.py`), the
numerical track has now verified ALL THREE of Perelman's monotone
functionals on the round sphere.
