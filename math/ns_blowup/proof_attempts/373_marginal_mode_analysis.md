---
source: Marginal mode analysis — proving 2-mode extremality of |∇u|²/|ω|²
type: PROOF ATTEMPT — the final step for NS regularity
file: 373
date: 2026-03-29
---

## GOAL

Prove: For any N-mode div-free field on T³ at the global max of |ω|:

    |∇u(x*)|² ≤ (5/4)|ω(x*)|²

Proven for N=2 (file 364). Numerically verified for N≤7 (file 372).

If proven → S²ê ≤ |ω|²/2 < 3|ω|²/4 → barrier → Type I → Seregin → **REGULARITY**.


## STRATEGY: MARGINAL MODE ANALYSIS

Show that the ratio F = |∇u|²/|ω|² at the global max DECREASES when adding
any mode to a 2-mode configuration. Combined with the proven N=2 bound (F ≤ 5/4):
this gives F ≤ 5/4 for all N.


## SETUP

Optimal 2-mode config (from file 364):
- k₁, k₂ with cos(angle) = κ* = 1/2 (60° between wavevectors)
- Equal amplitudes a₁ = a₂ = a
- Polarization angles such that d = v̂₁·v̂₂ = 0 (perpendicular polarizations)
- ψ₁ = ψ₂ (symmetric alignment with ê)

At the global max vertex x* (all cos(k·x*) = 1):
- ω = a(v̂₁ + v̂₂) = 2a cos(ψ)ê  [since d=0, |ω| = a√2]
- ê = (v̂₁+v̂₂)/|v̂₁+v̂₂| = (v̂₁+v̂₂)/√2
- |ω|² = 2a² (for d=0)
- |∇u|² = 2a² + 2a² Δ₁₂ = 2a²(1 + 1/4) = 5a²/2
- F = 5/4

Add a perturbation: mode 3 with amplitude ε, wavevector k₃, polarization v̂₃.

ω_new = a(v̂₁+v̂₂) + εv̂₃ at x* (assuming x* remains the global max vertex).


## FIRST-ORDER ANALYSIS

### Change in |ω|²:
|ω_new|² = |ω|² + 2ε(ω·v̂₃) + ε² = 2a² + 2εa√2 cosψ₃ + ε²

where ψ₃ = angle(v̂₃, ê).

d|ω|²/dε|₀ = 2a√2 cosψ₃ = 2|ω| cosψ₃

### Change in |∇u|²:
∇u_new = ∇u_old + ε(k₃×v̂₃)⊗k₃/|k₃|²

|∇u_new|² = |∇u_old|² + 2ε × (∇u_old : ∇u₃) + ε²

d|∇u|²/dε|₀ = 2(∇u_old : ∇u₃) = 2 Σ_{j=1,2} a(w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²)

where w_i = k_i × v̂_i.

### Change in ratio:
dF/dε|₀ = [d|∇u|²/dε × |ω|² - |∇u|² × d|ω|²/dε] / |ω|⁴

    = [2A × 2a² - (5a²/2) × 2|ω|cosψ₃] / (4a⁴)

where A = Σ_j a(w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²).

For dF/dε ≤ 0 at ε = 0:

    4a² A ≤ 5a² |ω| cosψ₃ = 5a² × a√2 × cosψ₃

    4A ≤ 5a√2 cosψ₃

    A ≤ (5√2/4) a cosψ₃


## KEY: THE CONSTRAINT a₃ ≤ |ω|cosψ₃

From the global max constraint (file 363): a₃ = ε ≤ |ω|cosψ₃ = a√2 cosψ₃.

For cosψ₃ = 0: ε = 0. No perturbation possible. ✓ (trivial)
For cosψ₃ > 0: ε ≤ a√2 cosψ₃. The perturbation is bounded.

But: we're looking at dF/dε at ε = 0, which is BEFORE the constraint binds.
The constraint affects which directions can be explored but not the derivative itself.


## BOUNDING A

A = Σ_{j=1,2} a(w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²)

= a [(w₁·w₃)(k₁·k₃)/(|k₁|²|k₃|²) + (w₂·w₃)(k₂·k₃)/(|k₂|²|k₃|²)]

Using the BAC-CAB identity: w_j·w₃ = (k_j·k₃)(v̂_j·v̂₃) - (k_j·v̂₃)(k₃·v̂_j).

A = a Σ_j [(k_j·k₃)²(v̂_j·v̂₃) - (k_j·k₃)(k_j·v̂₃)(k₃·v̂_j)] / (|k_j|²|k₃|²)

= a Σ_j [κ_j₃²(v̂_j·v̂₃) - κ_j₃(k̂_j·v̂₃)(k̂₃·v̂_j)]

where κ_j₃ = (k̂_j·k̂₃).

Also: d|ω|²/dε = 2|ω|cosψ₃ = 2a√2 (ê·v̂₃).

The condition 4A ≤ 5a√2 cosψ₃ becomes:

4Σ_j [κ_j₃² d_j₃ - κ_j₃ A_j₃ B_j₃] ≤ 5√2 cosψ₃

where d_j₃ = v̂_j·v̂₃, A_j₃ = k̂_j·v̂₃, B_j₃ = k̂₃·v̂_j.

And cosψ₃ = ê·v̂₃ = (v̂₁+v̂₂)·v̂₃/√2 = (d₁₃+d₂₃)/√2.


## WHAT NEEDS TO BE SHOWN

For the 2-mode extremality: need

    4 Σ_j [κ_j₃² d_j₃ - κ_j₃ A_j₃ B_j₃] ≤ 5(d₁₃ + d₂₃)     (★)

for ALL k₃, v̂₃ satisfying v̂₃ ⊥ k₃.

This is a FINITE-DIMENSIONAL inequality involving the geometric quantities
κ_j₃, d_j₃, A_j₃, B_j₃ constrained by the orthogonality relations.


## WHAT WE KNOW ABOUT THE CONSTRAINT

Each term: κ_j₃²d_j₃ - κ_j₃ A_j₃ B_j₃ = Δ_j₃ (the pairwise excess from file 364).

From file 364: Δ_j₃ = -(1-κ_j₃²)d_j₃ - κ_j₃ A_j₃ B_j₃ WAIT that's not the same.

Actually: from |∇u|²-|ω|² formula:
Δ_j₃ = (w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²) - d_j₃ = κ_j₃² d_j₃ - κ_j₃ A_j₃ B_j₃ - d_j₃

NOPE. Let me re-derive.

|∇u|² cross-term for pair (j,3): 2a × ε × (w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²)
|ω|² cross-term for pair (j,3): 2a × ε × d_j₃

So d|∇u|²/dε contribution from pair (j,3): 2a(w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²) = 2a(κ_j₃² d_j₃ - κ_j₃ A_j₃ B_j₃)

Hmm wait: (w_j·w₃)(k_j·k₃)/(|k_j|²|k₃|²) = [(k_j·k₃)d_j₃ - (k_j·v̂₃)(k₃·v̂_j)] × (k_j·k₃)/(|k_j|²|k₃|²)

= [(k_j·k₃)²d_j₃ - (k_j·k₃)(k_j·v̂₃)(k₃·v̂_j)]/(|k_j|²|k₃|²)

= κ_j₃² d_j₃ - κ_j₃ (k̂_j·v̂₃)(k̂₃·v̂_j)

OK so: d|∇u|²/dε = 2a Σ_j [κ_j₃² d_j₃ - κ_j₃ A_j₃ B_j₃]

And: d|ω|²/dε = 2a(d₁₃ + d₂₃) [since d_j₃ = v̂_j·v̂₃ and ε only appears once]

WAIT: d|ω|²/dε = 2(ω·v̂₃) = 2a(v̂₁+v̂₂)·v̂₃ = 2a(d₁₃+d₂₃). ✓

For dF/dε ≤ 0:
d|∇u|²/dε × |ω|² ≤ |∇u|² × d|ω|²/dε
2a Σ_j Q_j × 2a² ≤ (5a²/2) × 2a(d₁₃+d₂₃)

where Q_j = κ_j₃² d_j₃ - κ_j₃ A_j₃ B_j₃.

4a³(Q₁+Q₂) ≤ 5a³(d₁₃+d₂₃)

**4(Q₁+Q₂) ≤ 5(d₁₃+d₂₃)**                 (★)


## ANALYSIS OF (★)

Q_j = κ_j₃² d_j₃ - κ_j₃ A_j₃ B_j₃.

From file 364's analysis: Q_j - d_j₃ = (κ_j₃²-1)d_j₃ - κ_j₃ A_j₃ B_j₃ = Δ_j₃ (the excess).

So: Q_j = d_j₃ + Δ_j₃.

The condition (★) becomes:

4(d₁₃+d₂₃+Δ₁₃+Δ₂₃) ≤ 5(d₁₃+d₂₃)

4(Δ₁₃+Δ₂₃) ≤ (d₁₃+d₂₃)

**Δ₁₃ + Δ₂₃ ≤ (d₁₃+d₂₃)/4**               (★★)

where Δ_j₃ = -(1-κ_j₃²)d_j₃ - κ_j₃ A_j₃ B_j₃.

This says: the TOTAL excess from adding mode 3 to both existing modes
must be ≤ 1/4 of the vorticity coupling.


## EVALUATION OF (★★)

LHS: Δ₁₃+Δ₂₃ = -(1-κ₁₃²)d₁₃-(1-κ₂₃²)d₂₃ - κ₁₃A₁₃B₁₃ - κ₂₃A₂₃B₂₃

RHS: (d₁₃+d₂₃)/4

Condition: -(1-κ₁₃²)d₁₃-(1-κ₂₃²)d₂₃ - κ₁₃A₁₃B₁₃ - κ₂₃A₂₃B₂₃ ≤ (d₁₃+d₂₃)/4

Rearranging:
-d₁₃(1-κ₁₃²+1/4) - d₂₃(1-κ₂₃²+1/4) ≤ κ₁₃A₁₃B₁₃ + κ₂₃A₂₃B₂₃

-d₁₃(5/4-κ₁₃²) - d₂₃(5/4-κ₂₃²) ≤ κ₁₃A₁₃B₁₃ + κ₂₃A₂₃B₂₃

For this to hold: the LHS (which has -d terms, potentially positive if d < 0)
must be ≤ the RHS (which has mixed-sign κAB terms).


## SPECIAL CASES

### Case: k₃ ⊥ k₁ and k₃ ⊥ k₂ (orthogonal to both existing modes)
κ₁₃ = κ₂₃ = 0. LHS: -5d₁₃/4 - 5d₂₃/4 = -5(d₁₃+d₂₃)/4. RHS: 0.
Condition: -5(d₁₃+d₂₃)/4 ≤ 0 ↔ d₁₃+d₂₃ ≥ 0 ↔ cosψ₃ ≥ 0.
Since cosψ₃ = (d₁₃+d₂₃)/√2 ≥ 0 at the global max: ✓

### Case: k₃ = k₁ (same direction as mode 1)
κ₁₃ = 1, κ₂₃ = κ₁₂ = 1/2. Mode 3 combines with mode 1.
A₁₃ = k̂₁·v̂₃, B₁₃ = k̂₃·v̂₁ = k̂₁·v̂₁ = 0 (div-free: v̂₁ ⊥ k₁).
So κ₁₃A₁₃B₁₃ = 0. And Δ₁₃ = 0 (same-k modes: no excess).
Condition reduces to: Δ₂₃ ≤ (d₁₃+d₂₃)/4. ✓ (each pair excess ≤ 1/4 × d, from per-pair bound)


## NEXT STEPS

1. **Verify (★★) numerically** for random k₃, v̂₃ geometries
2. **Prove (★★) analytically** using the div-free constraints v̂_j ⊥ k_j
3. The constraint might follow from the AM-GM structure of Δ + d terms
4. If (★★) holds: the 2-mode extremality is proven → 5/4 for all N → NS regular

## ISSUE: MARGINAL ANALYSIS IS ILL-CONDITIONED

Numerical test (200K trials): condition (★★) is VIOLATED when cosψ₃ → 0
(mode 3 nearly perpendicular to ê). The denominator (d₁₃+d₂₃) → 0 while
the excess stays finite.

However: the global max constraint forces a₃ ≤ |ω|cosψ₃ → 0 in this limit.
The ACTUAL change in F is ΔF = (dF/dε)×ε, and dF/dε × ε → 0/0 × 0 (indeterminate).

The infinitesimal approach fails at degenerate points. Need FINITE perturbation.

## ALTERNATIVE: DIRECT BOUND

Instead of marginal analysis, prove the bound DIRECTLY for all N:

|∇u|² ≤ (5/4)|ω|² at the global max.

From the pairwise formula + global max constraint:

|∇u|²-|ω|² = Σ 2s_js_k a_ja_k (Q_jk - d_jk)

Each excess |Q_jk - d_jk| ≤ 1/4 (per-pair). Need total excess ≤ |ω|²/4.

The challenge: proving total excess ≤ |ω|²/4 requires accounting for
the amplitude distribution AND pairwise geometry simultaneously.

## STATUS

The marginal mode approach (★★) does NOT directly close the gap.
The proof remains:
- N ≤ 4: PROVEN (file 363 + H_ωω)
- N ≥ 5: OPEN (numerically verified to 50K trials)
- Conjecture A': |∇u|²/|ω|² ≤ 5/4 (would close for all N)

## 373. Marginal analysis is ill-conditioned at cosψ₃→0. Need different approach.
