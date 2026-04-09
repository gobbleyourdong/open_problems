# Riemann Hypothesis — Gap Assessment

## Phase: 0 → 1 (Paper Arsenal in progress)

## The Problem

Every non-trivial zero of ζ(s) = Σ_{n=1}^∞ n^{-s} has real part 1/2.

Equivalently: if ζ(ρ) = 0 and 0 < Re(ρ) < 1, then Re(ρ) = 1/2.

## Key Formulations

### The Zeta Function
ζ(s) = Σ n^{-s} (Re(s) > 1), analytically continued to ℂ \ {1}.
Functional equation: ξ(s) = ξ(1-s) where ξ(s) = s(s-1)/2 · π^{-s/2} Γ(s/2) ζ(s).
ξ(s) is entire, real on Re(s) = 1/2, and ξ(1/2 + it) is real for real t.

### Equivalent Statements
1. **Prime counting**: π(x) = Li(x) + O(x^{1/2} log x)
2. **Mertens**: |M(x)| = |Σ_{n≤x} μ(n)| = O(x^{1/2+ε}) for all ε > 0
3. **Li's criterion**: λ_n = Σ_ρ [1 - (1-1/ρ)^n] ≥ 0 for all n ≥ 1
4. **Robin's inequality**: σ(n) < e^γ n log log n for all n > 5040
5. **Nyman-Beurling**: The fractional parts {θ/k} span L²(0,1)
6. **de Branges**: Certain entire functions in the de Branges space have no real zeros

## What's Known

### Numerical
- ~10^13 non-trivial zeros verified on Re(s) = 1/2 (Platt 2021, rigorous)
- Zero failures in 170+ years of computation
- GUE statistics match to extraordinary precision (Odlyzko)

### Analytical
- Zero-free region: Re(s) > 1 - c/(log |t|)^{2/3} (log log |t|)^{1/3} (Vinogradov-Korobov)
- >40% of zeros on the critical line (Conrey 1989)
- 100% of zeros in Re(s) ∈ (1/2 - ε, 1/2 + ε) for ε > 0 (density hypothesis level)
- N(T) = (T/2π) log(T/2πe) + O(log T) (Riemann-von Mangoldt)

### Structural
- Weil proved RH for curves over F_q (1948)
- Deligne proved Weil conjectures for varieties (1974, Fields Medal)
- Montgomery: zeros correlate like GUE eigenvalues (1973)
- Selberg: positive proportion on critical line (1942)

## Initial Route Map (to be refined)

### Route 1: Hilbert-Pólya (Spectral)
Find self-adjoint operator H with eigenvalues = imaginary parts of zeros.
RH ⟺ H is self-adjoint (eigenvalues real).

### Route 2: Arithmetic Geometry (Weil analog)
Lift the Weil proof from F_q to Q. Needs an "arithmetic site" or
"field with one element" that makes ζ(s) look like a zeta function
of a curve over a finite field.

### Route 3: Analytic (Push zero-free region to 1/2)
Improve Vinogradov-Korobov. Current: 1 - c/(log t)^{2/3+ε}.
Need: 1 - c/f(t) where f(t)/log t → ∞ (would give RH).

### Route 4: Criterion-Based (Li, Nyman-Beurling, Robin)
Prove one of the equivalent criteria. Li's criterion (λ_n ≥ 0)
reduces RH to positivity of specific sums.

### Route 5: Random Matrix / Probabilistic
Use GUE statistics to constrain zero locations. Not yet a proof strategy
but may inform the right framework.

## Status (Updated 2026-04-08)
- [x] Paper arsenal built (attempt_002, attempt_004)
- [x] Lean definitions started (Definitions.lean: ζ partial, Li, Robin, Λ, rh_iff_lambda_zero)
- [x] Routes ranked (attempt_004: Connes ★★★★★, Λ=0 ★★★★, Li ★★★)
- [x] Computational targets identified (Li n≤60, Robin n≤100K, Turing T≤1000)
- [x] Phase 1 begun (689 zeros verified, GUE confirmed, Weil explicit verified)
- [ ] Phase 2: Connes' archimedean result formalized
- [ ] Phase 2: Λ upper bound improved below 0.22
- [ ] THEWALL identified: Type 3 (Conceptual) — no framework, no closable gap
