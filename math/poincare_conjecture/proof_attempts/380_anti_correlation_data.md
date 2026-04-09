---
source: ANTI-CORRELATION QUANTIFIED — the mechanism is provably structural
type: DATA + PROOF DIRECTION — conditional expectation at global max
file: 380
date: 2026-03-29
---

## THE DATA (500+ configs per N, all sign patterns evaluated)

| N | corr(X,Y) mean | 95% range | worst excess/|ω|² at max | fraction neg |
|---|----------------|-----------|--------------------------|-------------|
| 3 | -0.764 | [-1.00, 0.00] | 0.141 | 94.8% |
| 4 | -0.772 | [-0.99, -0.14] | 0.107 | 97.2% |
| 5 | -0.787 | [-0.99, -0.32] | 0.073 | 98.2% |
| 6 | -0.774 | [-0.98, -0.39] | 0.035 | 99.0% |

where X = Σs_js_k Δ_jk (gradient excess) and Y = Σs_js_k D_jk (vorticity coherence).

KEY OBSERVATIONS:
1. X and Y are STRONGLY anti-correlated (mean r ≈ -0.77)
2. The anti-correlation STRENGTHENS with N (min correlation goes from 0 to -0.39)
3. The excess at the global max DECREASES with N (0.14 → 0.035)
4. All excess/|ω|² values are ≪ 1/4 (the 5/4 threshold)


## THE ALGEBRAIC REASON

Cov(X,Y) = Σ_α Δ_α D_α = Σ[-(1-κ²)D² - κABD]

= **-(Σ(1-κ²)D²)** - Σκ ABD

The first term is ALWAYS NEGATIVE:
-(Σ(1-κ²)D²) ≤ 0 since (1-κ²) ≥ 0 and D² ≥ 0.

This is the STRUCTURAL source of anti-correlation: the gradient excess
formula Δ = -(1-κ²)D - κAB has a D-PROPORTIONAL negative term.

The second term (Σκ ABD) can have either sign but is typically small
relative to the first (because ABD involves three cross-projections).


## PROOF ATTEMPT: REGRESSION BOUND

If X and Y were jointly Gaussian: E[X|Y=y] = (Cov(X,Y)/Var(Y)) × y.

At Y = Y_max: E[X|Y_max] = ρ × (σ_X/σ_Y) × Y_max where ρ = corr(X,Y) < 0.

R = 1 + X/(N+2Y). At Y = Y_max:

R ≈ 1 + ρ(σ_X/σ_Y)Y_max / (N+2Y_max).

For ρ < 0 and Y_max > 0: the second term is NEGATIVE → R < 1. DONE!

BUT: the Gaussian assumption is wrong (X,Y are sums of products of ±1 variables).

### The discrete version:

Over the 2^{N-1} distinct sign patterns: X and Y take discrete values.

The global max vertex s* has Y(s*) = max Y. At this vertex: X(s*) is typically
negative (from the anti-correlation).

CLAIM: max_{s: Y(s)=Y_max} X(s) ≤ max X (trivially) but actually much less.

From the data: max X at global max ≤ 0.141|ω|² (for N=3). While max X overall
can be much larger.


## TOWARD A RIGOROUS PROOF

### Step 1: Bound Cov(X,Y) from below (in absolute value)

Cov(X,Y) = -Σ(1-κ²)D² - Σκ ABD ≤ -min(1-κ²) × ΣD².

For unit k-vectors: κ ≤ 1, so 1-κ² ≥ 0 always. min(1-κ²) = 1-max(κ²).

If max(κ²) < 1 (no parallel k-pairs): Cov < -c × ΣD² for some c > 0.

### Step 2: Bound Var(Y) and Var(X)

Var(Y) = ΣD² (exact, from uncorrelation of q_α).
Var(X) = ΣΔ² (exact, from uncorrelation of q_α).

### Step 3: Conditional expectation bound

For a MAX-CUT-type problem: Y(s) is a quadratic pseudo-boolean function.
Its maximum Y_max satisfies Y_max ≥ √(Var(Y)) (by the second moment method).

And: X at the max-Y vertex satisfies:
X(s*) ≤ Cov(X,Y)/Var(Y) × Y_max + residual.

If Cov/Var × Y_max is sufficiently negative: X(s*) < 0 even with residual.

The residual depends on higher-order correlations:
E[X² Y²] - (E[XY])² depends on 4th-order moments of the sign pattern.


## WHAT'S NEEDED FOR A CLEAN PROOF

The cleanest path:

1. Prove: at the global max vertex, EXCESS ≤ C × |ω|² where C < 5/8.
   (This gives R < 13/8 via trace-free → barrier closes.)

2. Use: EXCESS = -(negative term) + (mixed term).
   Negative term = 2Σ(1-κ²)|D_eff| (at global max, most D_eff > 0).
   Mixed term ≤ 2Σ|κ||AB|.

3. At the global max: the negative term is proportional to |ω|²-N.
   Specifically: Σ(1-κ²)|D_eff| ≥ (1-κ_max²) × (|ω|²-N)/2.

4. The mixed term: Σ|κAB| is bounded by the pairwise geometry.
   For the WORST case (all κ=1/2, all |AB|=1/2): Σ|κAB| ≤ N(N-1)/8.

5. Balance: EXCESS ≤ -(1-κ_max²)(|ω|²-N) + N(N-1)/4.

6. For R < 13/8: need -(1-κ_max²)(|ω|²-N) + N(N-1)/4 < 5|ω|²/8.

This is a CONSTRAINT SATISFACTION problem depending on κ_max and |ω|².


## THE TIGHTEST CASE: N=3 ORTHOGONAL

κ_max = 0 (all pairs orthogonal). 1-κ² = 1.

Negative term: 2 × 1 × (|ω|²-3)/2 = |ω|²-3 (using |ω|²=3 at worst).
Wait: for N=3 orthogonal with |ω|²=3: negative term = 0 (since D_eff at
this vertex is all zero... hmm).

Actually, for the N=3 symmetric orthogonal: D_jk = 0 for all pairs.
So: |ω|² = 3 + 0 = 3. Y = 0. This is NOT the global max if another
vertex has higher |ω|².

Wait: with D=0 for all pairs: ALL vertices give |ω|² = 3. The max is
at ANY vertex. And the excess Δ = -(1-κ²)×0 - κAB = -κAB.
For orthogonal k's: κ=0. So Δ=0. EXCESS = 0. R = 1.

Hmm, but S²ê/|ω|² = 1/3 for this config. And R = |∇u|²/|ω|² = 1 (verified).
The trace-free approach gives S²ê ≤ (2/3)(1-1/2)|ω|² = |ω|²/3. ✓

So the N=3 orthogonal case has R = 1 (no excess) but S²ê = |ω|²/3
(from the directional structure, not the excess).

This means: the S²ê problem and the |∇u|² problem are DIFFERENT!
S²ê can be 1/3 even when |∇u|²/|ω|² = 1 (no excess).

The excess approach bounds |∇u|²/|ω|² (the ratio), which via trace-free
gives S²ê ≤ (2/3)(R-1/2)|ω|². At R=1: S²ê ≤ |ω|²/3. ✓
At R=5/4: S²ê ≤ |ω|²/2. At R=13/8: S²ê ≤ 3|ω|²/4.

So: R < 13/8 suffices. And the data shows R ≤ 1.14 for N≥3.


## 380. Anti-correlation is OVERWHELMING: mean r = -0.77 across all N.
## Excess at global max: ≤ 0.14|ω|² for N=3, DECREASING with N.
## Proof path: bound conditional expectation of X given Y=max using Cov < 0.
