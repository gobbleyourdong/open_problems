# Riemann Hypothesis — Paper Arsenal

> Built: 2026-04-07 | Even Instance Phase 1

## Tier 1: The Problem and Classical Results

### 1.1 The Zeta Function
- **Riemann** (1859). "Über die Anzahl der Primzahlen unter einer gegebenen Grösse."
  - Defined ζ(s), analytic continuation, functional equation
  - Stated RH as a conjecture
  - THE founding document

### 1.2 Prime Number Theorem
- **Hadamard, de la Vallée-Poussin** (1896). Independent proofs.
  - PNT: π(x) ~ x/log x
  - Requires: ζ(s) ≠ 0 on Re(s) = 1

### 1.3 Zero-Free Regions
- **Vinogradov, Korobov** (1958). Re(s) > 1 - c/(log|t|)^{2/3}(log log|t|)^{1/3}
  - STATE OF THE ART for 65+ years. No improvement to the 2/3 exponent.
- **Ford** (2002). Optimized constants.
- **Mossinghoff-Trudgian** (2015). arXiv:1501.02003. Explicit improvements.

### 1.4 Density Estimates
- **Selberg** (1942). Positive proportion of zeros on Re(s) = 1/2.
- **Levinson** (1974). ≥ 1/3 of zeros on critical line.
- **Conrey** (1989). ≥ 2/5. J. reine angew. Math. 399, 1-26.
- **Bui-Conrey-Young** (2011). arXiv:1002.4127. ≥ 41.05%.

## Tier 2: Major Approaches

### 2.1 Hilbert-Pólya (Spectral)
- **Berry-Keating** (1999). H = xp conjecture.
- **Connes** (1999). Trace formula, noncommutative geometry. Selecta Math.
- **Sierra-Townsend** (2008). arXiv:0805.4079. Regularized xp.
- **Bender-Brody-Müller** (2017). arXiv:1608.03679. PRL 118, 130201.
  - PT-symmetric approach. Criticized (self-adjointness issues).
- **No credible operator constructed as of 2026.**

### 2.2 Arithmetic Geometry
- **Weil** (1948). RH for curves over F_q. Intersection theory.
- **Deligne** (1974). Weil conjectures for varieties. Fields Medal.
- **Deninger** (1992+). Conjectural foliated space framework.
- **Connes-Consani** (2010-2024). F₁ geometry, arithmetic site.
  - arXiv:1405.4527, arXiv:1407.4981, arXiv:2406.13748
- **Connes** (2023). arXiv:2310.18663. Weil positivity at archimedean place PROVED.
  - Reduces RH to positivity at finite primes. The hard part remains.

### 2.3 Random Matrix Theory
- **Montgomery** (1973). Pair correlation matches GUE.
- **Odlyzko** (1987+). Numerical confirmation to high precision.
- **Keating-Snaith** (2000). Moment conjectures. CMP 214.
- **Katz-Sarnak** (1999). Symmetry types of L-function families.

### 2.4 Equivalences
- **Li** (1997). λ_n ≥ 0 ⟺ RH. J. Number Theory 65.
- **Robin** (1984). σ(n) < e^γ n log log n for n > 5040 ⟺ RH.
- **Nyman-Beurling** (1950s). L² approximation criterion.
- **Báez-Duarte** (2003). arXiv:math/0202141. Sharpened Nyman-Beurling.

## Tier 3: Recent Breakthroughs (2020-2026)

### 3.1 Guth-Maynard (2024)
- arXiv:2405.20552. **Major breakthrough in analytic number theory.**
- New large-value estimates for Dirichlet polynomials.
- Improves density estimates near σ = 1. Does NOT prove RH.
- First significant advance in exponential sum technology in decades.

### 3.2 Rodgers-Tao (2020)
- arXiv:1801.05914. Newman conjecture: Λ ≥ 0.
- Combined with Ki-Kim-Lee: **RH ⟺ Λ = 0** (de Bruijn-Newman constant).
- Shows RH is "barely true" — zeros at boundary of heat-flow stability.

### 3.3 Polymath 15 (2019)
- Λ ≤ 0.22 (improved from 1/2). So 0 ≤ Λ ≤ 0.22.

### 3.4 Platt-Trudgian (2021)
- arXiv:2004.09765. Verified RH up to T = 3 × 10^12 (12.4 trillion zeros).
- RIGOROUS (interval arithmetic, Turing's method).

### 3.5 Connes Archimedean Positivity (2023)
- arXiv:2310.18663. Proved Weil positivity at the archimedean place.
- Partial progress on the Connes program. Hard part (finite primes) remains.

## The Obstruction Table

| Approach | What works | What's missing |
|----------|-----------|----------------|
| Zero-free regions | Near σ=1 | Can't reach σ=1/2 (65 years stuck) |
| Density | 41% on line | Need 100% (barrier at ~50%) |
| Hilbert-Pólya | Heuristic H=xp | No self-adjoint operator found |
| Connes | Archimedean done | Finite prime positivity (= new AG over F₁) |
| RMT | Predicts everything | Proves nothing (model, not mechanism) |
| Weil analog | Works over F_q | No Frobenius for Spec(Z) |
| Equivalences | Beautiful reformulations | Just as hard in new language |
| Guth-Maynard | New ideas near σ=1 | Can't reach σ=1/2 |
