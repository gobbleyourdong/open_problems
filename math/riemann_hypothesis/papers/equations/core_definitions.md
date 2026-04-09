# RH — Core Equations and Computational State

## What Mathlib4 Already Has

| Result | Lean Name | Status |
|--------|-----------|--------|
| ζ(s) definition + continuation | `riemannZeta` | PROVED |
| Completed zeta Λ(s) | `completedRiemannZeta` | PROVED |
| Functional equation | `riemannZeta_one_sub` | PROVED |
| ζ(2) = π²/6 | `riemannZeta_two` | PROVED |
| Euler product | `riemannZeta_eulerProduct` | PROVED |
| ζ(s) ≠ 0 for Re(s) ≥ 1 | (nonvanishing) | PROVED |
| RH statement | `RiemannHypothesis` | STATED (not proved) |
| Dirichlet L-functions | continuation + functional eq | PROVED |
| Primes in AP (Dirichlet) | full proof | PROVED |
| PNT | Wiener-Ikehara | PROVED (merging) |

Source: Loeffler (2025), arXiv:2503.00959

## What Mathlib4 LACKS (critical for RH campaign)

- Laurent series
- Residue theorem
- Meromorphic functions (general theory)
- Argument principle / winding number
- Contour integration of continuous functions

**The residue theorem gap blocks**: zero-counting (N(T) formula),
explicit formulae, and Turing's method formalization.

## Computational Certificates

### Platt-Trudgian (2021): 3 × 10¹² zeros verified
- Method: Turing's method + Arb interval arithmetic
- RIGOROUS (every float has proven error bound)
- NOT formally verified (not in Lean/Coq/Isabelle)
- Uses FLINT/Arb library (Fredrik Johansson)

### Robin's Inequality: verified to n ~ 10¹³
- σ(n) < e^γ n log log n for n > 5040
- Purely arithmetic — no complex analysis needed
- FORMALIZABLE in Lean right now

### Li's Criterion: λ_n computed to n ~ 10⁴
- Numerically unstable (needs O(n) bits for λ_n)
- All positive. No rigorous certification yet.

### de Bruijn-Newman: 0 ≤ Λ ≤ 0.22
- Rodgers-Tao (2020): Λ ≥ 0
- Polymath 15 (2019): Λ ≤ 0.22
- RH ⟺ Λ = 0

## Key Equations

### Riemann Zeta
ζ(s) = Σ_{n=1}^∞ n^{-s} = ∏_p (1 - p^{-s})^{-1}  (Re(s) > 1)

### Functional Equation
ξ(s) = ξ(1-s) where ξ(s) = s(s-1)/2 · π^{-s/2} · Γ(s/2) · ζ(s)

### Zero Counting
N(T) = #{ρ : ζ(ρ)=0, 0 < Im(ρ) < T} = T/(2π) log(T/2πe) + O(log T)

### Hardy's Z-function
Z(t) = e^{iθ(t)} ζ(1/2 + it) where θ(t) = arg(π^{-it/2} Γ(1/4 + it/2))
Z(t) is real for real t. Zeros of Z = zeros of ζ on the critical line.

### Weil Explicit Formula
Σ_ρ h(ρ) = ĥ(0) + ĥ(1) - Σ_p Σ_k (log p/p^{k/2})[ĥ(k log p) + ĥ(-k log p)] + (integral)

RH ⟺ Weil positivity: Σ_ρ h(ρ) ≥ 0 for suitable test functions h ≥ 0.

### de Bruijn-Newman
H_t(z) = ∫_0^∞ e^{tu²} Φ(u) cos(zu) du where Φ is the Jacobi theta derivative.
Λ = inf{t : H_t has only real zeros}. RH ⟺ Λ ≤ 0. Proved: Λ ≥ 0.
Currently: 0 ≤ Λ ≤ 0.22.
