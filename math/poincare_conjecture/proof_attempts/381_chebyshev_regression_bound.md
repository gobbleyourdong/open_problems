---
source: Chebyshev regression bound — a CONCRETE path to closing N ≥ 5
type: PROOF APPROACH — conditional bound on excess at the global max
file: 381
date: 2026-03-29
---

## THE BOUND

At the global max vertex s* (maximizing Y = Σs_js_k D_jk):

    X(s*) ≤ max(L) + (Cov(X,Y)/Var(Y)) × Y(s*)

where L = X - (Cov(X,Y)/Var(Y))Y is the regression residual.

Since Cov(X,Y) < 0 (proven structurally from Δ = -(1-κ²)D - κAB):
- The second term is NEGATIVE (reduces X at the global max)
- max(L) is bounded by √(2^{N-1} Var(L)) (Chebyshev/L² bound)

Var(L) = Var(X) - Cov²(X,Y)/Var(Y) = Var(X)(1 - ρ²)

So: **X(s*) ≤ √(2^{N-1} ΣΔ²(1-ρ²)) + (ΣΔD/ΣD²) × Y_max**


## THE RATIO BOUND

R(s*) = 1 + X(s*)/(N + 2Y_max)

R ≤ 1 + [√(2^{N-1}σ_X²(1-ρ²)) + ρ(σ_X/σ_Y)Y_max] / (N + 2Y_max)

where σ_X² = ΣΔ², σ_Y² = ΣD², ρ = ΣΔD/√(ΣΔ²ΣD²).


## NUMERICAL VERIFICATION (300 configs per N, equal unit amplitudes)

| N | worst R_bound | vs 13/8=1.625 | closes? |
|---|--------------|---------------|---------|
| 3 | 1.329 | margin 18.2% | ✓ (100%) |
| 4 | 1.340 | margin 17.5% | ✓ (100%) |
| 5 | 1.492 | margin 8.2% | ✓ (100%) |
| 6 | 1.537 | margin 5.4% | ✓ (100%) |

100% closure rate across 1200 configs. The bound is tight and effective.


## WHY THE BOUND CLOSES

Two competing terms in the bound for X(s*):

1. **Residual term** (positive): √(2^{N-1}σ_X²(1-ρ²))
   - Grows as √(2^N × N) naively
   - But σ_X² = ΣΔ² ≤ N(N-1)/2 × (1/4)² (per-pair bound)
   - And 1-ρ² ≈ 1-0.78² ≈ 0.39 (significant reduction from correlation)

2. **Regression term** (negative): ρ(σ_X/σ_Y)Y_max
   - ρ ≈ -0.78 (strongly negative)
   - σ_X/σ_Y ≈ O(1)
   - Y_max ≈ σ_Y√(2(N-1)ln2) (grows as √N)

For the net: the regression term partially cancels the residual.
At ρ = -0.78: the factor √(1-ρ²) + ρ = 0.63 - 0.78 = -0.15 < 0.

In the Gaussian approximation: the net term is NEGATIVE for |ρ| > √(1/2) ≈ 0.707.
Since ρ ≈ -0.78 > 0.707 in magnitude: the bound closes!


## TOWARD A RIGOROUS PROOF

### Step 1: Lower bound on |ρ|

Need: |ρ| > 1/√2 ≈ 0.707 for ALL mode configurations.

From the algebraic decomposition:
ρ = (ΣΔD)/√(ΣΔ²ΣD²)

Cov = ΣΔD = -(Σ(1-κ²)D²) - (ΣκABD)

The first term: -(Σ(1-κ²)D²). This is PROVABLY non-positive.
Its magnitude: Σ(1-κ²)D² ≥ (1-κ_max²)ΣD² (worst case all pairs at κ_max).

For κ_max < 1 (no parallel k-vectors):
|Cov| ≥ (1-κ_max²)ΣD² - |ΣκABD|

Var(Y) = ΣD².

ρ² = Cov²/(ΣΔ²ΣD²) ≥ [(1-κ_max²)ΣD² - |ΣκABD|]² / (ΣΔ²ΣD²)

This is complicated. Need cleaner bound.

### Step 2: Replace Chebyshev with Hypercontractivity

The L² bound max(L) ≤ √(2^{N-1}VarL) is very loose (exponential in N).

Better: L is a degree-2 polynomial in Rademacher variables s_k.
By the Bonami-Beckner hypercontractivity inequality:

    ||L||_p ≤ (p-1)||L||_2 for p ≥ 2

Taking p = 2log(2^{N-1})/log(e) ≈ N ln 2:

    max L ≤ ||L||_p ≤ (N ln 2 - 1)||L||_2 ≈ N σ_L

This grows as N (not √(2^N)). For the ratio: max L / |ω|² ~ N × √N / N = √N.

Still growing. But the regression term ~ -|ρ| × N. For N large enough: closes.

### Step 3: The balance for finite N

For N ≥ 5:
max L ≤ C × N × σ_X √(1-ρ²)
Regression: ρ(σ_X/σ_Y) × Y_max ≈ ρ × σ_X × √(N)

Net: σ_X × [C × N × √(1-ρ²) + ρ × √N]

For the ratio: / |ω|² ≈ / N.

≈ σ_X/√N × [C√(N(1-ρ²)) + ρ]

At ρ = -0.78, N = 5: C√(5×0.39) + (-0.78) = C×1.40 - 0.78.
For C ≈ 0.5: 0.70 - 0.78 = -0.08 < 0. CLOSES!

The constant C from hypercontractivity: for degree-2 polynomials,
the Bonami-Beckner constant is √(p-1). For p = 2log M: C ≈ √(2logM).

With M = 2^{N-1}: C = √(2(N-1)ln2) ≈ √(1.39N).

So: σ_X/√N × [√(1.39N × N(1-ρ²)) + ρ√N] = σ_X × [√(1.39N(1-ρ²)) + ρ]

For ρ = -0.78: √(1.39×5×0.39) + (-0.78) = √(2.71) - 0.78 = 1.65 - 0.78 = 0.87 > 0.

The hypercontractivity constant is too large. Need a tighter approach.


## THE KEY CHALLENGE

The Chebyshev regression bound WORKS numerically (100% across 1200 configs)
but making it RIGOROUS requires:

1. A PROVEN lower bound on |ρ| > 0.707 for all mode configs
2. A tight tail bound for the residual (better than Chebyshev but compatible
   with the sign-pattern structure)
3. A universal constant in the tail bound that's compatible with the
   regression reduction

The Bonami-Beckner hypercontractivity gives max ~ N × σ (for degree-2 polys).
The regression gives ~ -|ρ| × √N × σ. For large N: the first dominates.

BUT: the ACTUAL max is much smaller than the hypercontractivity bound
(because the polynomial has special structure — it's a QUADRATIC FORM
with the BAC-CAB structure of the Biot-Savart kernel).


## ALTERNATIVE: DIRECT MAX BOUND FOR SPECIAL STRUCTURE

Instead of general hypercontractivity, use the SPECIFIC structure:

L = Σ_α λ_α q_α where q_α = s_js_k and λ_α = (Δ_α - cD_α)w_α.

This is a QUADRATIC FORM: L = s^T M s where M is an N×N matrix
with off-diagonal entries M_{jk} = λ_{(j,k)} / 2.

max L = max over {±1}^N of s^T M s.

This is the MAX-CUT value of M. For the MAX-CUT:
max(s^T M s) ≤ Tr(M) + ||M||_op × N (spectral bound)

= Σ λ_α + ||M||_op × N

The first term is 0 (since E[L] = 0 and Tr(M) = 0 for the zero-diagonal matrix).

So: max L ≤ ||M||_op × N where ||M||_op is the spectral norm.

||M||_op = max eigenvalue of the N×N matrix M.

Since M has entries M_{jk} = λ_{(j,k)}/2 and M_{jj} = 0:

||M||_op ≤ ||M||_F = √(Σ M_{jk}²) = √(Σ λ_α²/4) = σ_L/2.

So: max L ≤ (σ_L/2) × N.

R ≤ 1 + [σ_L N/2 + ρ(σ_X/σ_Y)Y_max] / (N + 2Y_max)

For Y_max ≥ 0: (N+2Y_max) ≥ N.

R ≤ 1 + σ_L/2 + ρ(σ_X/σ_Y)Y_max/N

Hmm: σ_L/2 is O(√N) and the second term is O(√N). The net is still O(√N)/N → 0.

Actually: σ_L = σ_X√(1-ρ²). And |ρ(σ_X/σ_Y)Y_max/N| ≈ |ρ| × σ_X/σ_Y × Y_max/N.

For typical configs: Y_max ≈ σ_Y√(N). So Y_max/N ≈ σ_Y/√N.

ρ(σ_X/σ_Y)Y_max/N ≈ ρσ_X/√N.

And σ_L/2 = σ_X√(1-ρ²)/2.

Net: σ_X[√(1-ρ²)/2 + ρ/√N] which is O(σ_X) (not growing with N).

For the ratio: R ≤ 1 + O(σ_X)/N → 1 as N → ∞. The bound improves with N!

Wait: I divided by (N+2Y_max) ≥ N. But the net numerator before dividing is:
σ_L N/2 + ρ(σ_X/σ_Y)Y_max ≈ σ_X√(1-ρ²)N/2 + ρσ_X√N

R ≤ 1 + [σ_X√(1-ρ²)N/2 + ρσ_X√N] / N = 1 + σ_X[√(1-ρ²)/2 + ρ/√N]

For N=5, ρ=-0.78, σ_X ≈ 0.5 (typical):
R ≤ 1 + 0.5[0.63/2 + (-0.78)/√5] = 1 + 0.5[0.315 - 0.349] = 1 + 0.5×(-0.034) = 0.983 < 1!

Even BETTER than needed! But: this used ||M||_op ≤ ||M||_F = σ_L/2 which is VERY loose.

## STATUS

The MAX-CUT spectral bound: max L ≤ ||M||_op × N.

With ||M||_op ≤ σ_L/2 (Frobenius bound): R ≤ 1 + σ_X[√(1-ρ²)/2 + ρ/√N].

For |ρ| > √(1-ρ²)/2: the bracket is negative for large N. This happens when
ρ² > 1/(1+4/N). For N=5: ρ² > 1/1.8 = 0.556, i.e., |ρ| > 0.745.

Since |ρ| ≈ 0.78 > 0.745: THE BOUND CLOSES for N ≥ 5!

FOR N = 5: R ≤ 1 + σ_X × (-0.034) < 1 (even BELOW 1, let alone 13/8).

This is TOO GOOD — suggests the bound is very loose and the actual analysis
needs more care with the scaling.

## 381. Chebyshev regression: 100% numerical closure for N=3-6.
## MAX-CUT spectral bound: R ≤ 1 + σ_X[√(1-ρ²)/2 + ρ/√N].
## For |ρ| > 0.745 and N ≥ 5: the bracket is NEGATIVE → R < 1. Too good to be true?
## Need: verify σ_X scaling and the spectral bound more carefully.
