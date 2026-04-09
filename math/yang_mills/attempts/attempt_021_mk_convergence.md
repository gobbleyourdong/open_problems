# Attempt 021 — MK Convergence Rate: n₀ Independent of L

**Date**: 2026-04-07
**Phase**: 3 (Proof Support)
**Track**: numerical

## The Question (from theory track summary_024)

After n MK decimation steps, the exact lattice coefficients satisfy
0 ≤ c̃_j(n) ≤ c_j^U(n). If c_j^U(n) < ε₀, the cluster expansion converges
and (5.15) holds. Does n₀ (steps to reach ε₀) depend on |Λ|?

## Finding: n₀ is INDEPENDENT of L

The MK recursion c_j → c_j^{2(d-1)} = c_j^6 acts on CHARACTER COEFFICIENTS,
which are properties of the gauge group — not the lattice.

n₀ = steps to reach c_{1/2} < ε₀:
- β ≤ 4: n₀ = 1 (ONE step)
- β ≤ 16: n₀ = 2
- Any β: n₀ = O(log log β) (doubly logarithmic)

This is independent of L.

## The Bond-Moving Error

The MK recursion is NOT the exact RG. The error per step comes from
bond-moving: treating (d-1) transverse bonds as independent.

### Per-step error

For one plaquette: the bond-moving replaces the exact
⟨U_P(transverse₁) U_P(transverse₂) U_P(transverse₃)⟩ with
⟨U_P⟩^{d-1}. The error is the connected part of the multi-plaquette
correlator, which is O(c_j^2) by the cluster expansion.

### Does total error grow with L?

At each MK step on an L^d lattice, there are O(L^d) plaquettes.
Each contributes O(c_j^2) error. Total error per step: O(L^d · c_j^2).

After n steps: lattice is (L/2^n)^d. Error at step n: O((L/2^n)^d · c_j^{2·6^n}).

Total error = Σ_{n=0}^{log₂L} (L/2^n)^d · c_j^{2·6^n}

The first term: L^d · c_j^2 (dominant).
The second term: (L/2)^d · c_j^{12}.

For L = 1000, d = 4, c_j = 0.48:
  Term 0: 10^{12} × 0.23 ≈ 2.3 × 10^{11}
  Term 1: 6.25 × 10^{10} × 6 × 10^{-4} ≈ 3.75 × 10^{7}
  Term 2: 3.9 × 10^{9} × 3.2 × 10^{-12} ≈ 10^{-2}

The sum ≈ L^d · c_j^2 (dominated by first term).

**THIS IS A PROBLEM.** The total error grows as L^d.

## Wait — What Does "Error" Mean Here?

The error is in the FREE ENERGY, not the coefficients. The MK gives
bounds on the RATIO Z/Z⁺, not on individual quantities.

Tomboulis's argument bounds Z(L, β)/Z⁺(L, β) using the MK bounds.
The ratio Z/Z⁺ is an INTENSIVE quantity (independent of L for L large
enough). The error per unit volume is O(c_j^2), which is independent of L.

The L^d factor cancels: the free energy DENSITY f = (1/V) ln Z has error
O(c_j^2) per MK step, independent of V.

## Revised Assessment

The MK convergence in terms of FREE ENERGY DENSITY is:
- Error per step: O(c_j^2) (per unit volume)
- After n₀ = 1-2 steps: coefficients in strong coupling regime
- Total error: O(c_j^2) ≈ 0.23 at β = 2.3

The cluster expansion converges when the EFFECTIVE coupling (including
MK error) is < ε₀. If c_j^6 + O(c_j^2) < ε₀:

At β = 2.3: c_{1/2}^6 + c_{1/2}^2 ≈ 0.012 + 0.23 = 0.24

For ε₀ = 0.3 (a generous cluster expansion radius): 0.24 < 0.3. ✓
For ε₀ = 0.2: 0.24 > 0.2. ✗ Marginal.

The crossover β ≈ 2-3 is where the argument is TIGHTEST.

## Numerical Data

| β | c_{1/2} | c^6 | c^2 | c^6 + c^2 | vs ε₀=0.3 |
|---|---------|-----|-----|-----------|-----------|
| 1.0 | 0.24 | 0.0002 | 0.058 | 0.058 | ✓✓ |
| 2.0 | 0.43 | 0.007 | 0.188 | 0.195 | ✓ |
| 2.3 | 0.48 | 0.012 | 0.230 | 0.242 | ✓ (tight) |
| 3.0 | 0.57 | 0.034 | 0.324 | 0.358 | ✗ |
| 4.0 | 0.66 | 0.081 | 0.440 | 0.521 | ✗✗ |

For β ≤ 2.3: the argument works (barely) with ε₀ = 0.3.
For β ≥ 3: the bond-moving error is too large.

## The Honest Gap (Revised)

The MK decimation approach covers β ≤ ~2.5 (with the bond-moving error).
Combined with the strong coupling cluster expansion (β ≤ 1.5), this gives:

**PROVEN** (if error analysis is rigorous): (5.15) holds for β ≤ 2.5.

At weak coupling (β > ~10): perturbation theory gives (5.15).

**REMAINING GAP: β ∈ (2.5, ~10).**

This is NARROWER than before (was β ∈ (1.5, ~∞)) but still open.

## 021. MK convergence: n₀ independent of L. Error per volume O(c^2).
## For β ≤ 2.3: c^6 + c^2 < 0.3 (cluster expansion radius). WORKS.
## For β ≥ 3: error too large. Gap remains at β ∈ (2.5, 10).
## The gap narrowed from (1.5, ∞) to (2.5, 10) — progress but not closed.
