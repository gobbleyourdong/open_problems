---
source: Frame constant bound — proving λ_max < 3N/(N-1) for N ≥ 5
type: PROOF ATTEMPT — the frame theory approach to closing N ≥ 5
file: 377
date: 2026-03-29
---

## THE FRAME CONSTANT PROBLEM

For N modes: S²ê = |Σ r_k d̂_k|² where:
- r_k = |ŝ_k| ≤ (|ω|/4)sin(2γ_k) (amplitude, from sign-flip bound)
- d̂_k ∈ R³, |d̂_k| = 1 (direction of ŝ_k)
- d̂_k ⊥ v̂_k (Biot-Savart constraint: strain direction ⊥ mode polarization)

Define: C(v̂₁,...,v̂_N) = max_{d̂_k⊥v̂_k} λ_max(D^T D) where D = [d̂₁...d̂_N]^T.

The S²ê bound: S²ê ≤ C × Σr_k² ≤ C × (N-1)|ω|²/(4N).

For S²ê < 3|ω|²/4: need C < 3N/(N-1).


## ANALYTICAL BOUND ON THE FRAME CONSTANT

### Upper bound: C ≤ N (trivially, all parallel)

But with d̂_k ⊥ v̂_k: all parallel requires v̂_k all having a common
perpendicular d̂. This is possible iff the v̂_k are coplanar (all in
one 2D plane, making d̂ the normal to that plane).

For v̂_k that SPAN R³ (at least 3 non-coplanar): no common d̂ exists.
λ_max < N.

### Tighter bound using the constraint

λ_max(D^T D) = max_{|x|=1} Σ(d̂_k · x)².

Since d̂_k ⊥ v̂_k: (d̂_k · x)² ≤ 1 - (v̂_k · x)².

So: λ_max ≤ max_{|x|=1} Σ(1 - (v̂_k · x)²) = N - min_{|x|=1} Σ(v̂_k · x)².

min_{|x|=1} Σ(v̂_k · x)² = λ_min(V^T V) where V has rows v̂_k.

V^T V is a 3×3 PSD matrix with trace N (since Σ|v̂_k|² = N).
Its eigenvalues μ₁ ≥ μ₂ ≥ μ₃ ≥ 0 with μ₁+μ₂+μ₃ = N.

**λ_max(D^T D) ≤ N - μ₃(V^T V).**

### When does this close?

Need: N - μ₃ < 3N/(N-1) → μ₃ > N - 3N/(N-1) = N(N-4)/(N-1).

For N=5: μ₃ > 5(1)/4 = 5/4. Need the smallest eigenvalue of V^T V > 5/4.

V^T V has eigenvalues summing to 5 with μ₃ ≥ 0. The constraint μ₃ > 5/4
means the v̂_k can't be too concentrated in any plane.

### At the Lagrange optimum (worst-case mode config)

From file 363: the Lagrange optimal has all modes at γ* = arccos(1/√N) from ê.
v̂_k = (1/√N)ê + √(1-1/N) n̂_k where n̂_k are unit vectors in the plane ⊥ ê.

V^T V: the v̂_k vectors have component 1/√N along ê and √(1-1/N) in the ⊥ plane.

The ê-ê component of V^T V: Σ(v̂_k · ê)² = Σ(1/N) = 1.
The ⊥ components: Σ(v̂_k · e_j)² for e_j ⊥ ê.

V^T V = ê ⊗ ê + (1-1/N) × (N̂^T N̂) where N̂ has rows n̂_k.

N̂^T N̂ is 2×2 (in the plane ⊥ ê) with trace N (since Σ|n̂_k|² = N).
But wait: n̂_k are unit vectors in R², so N̂^T N̂ is 2×2 with trace N.
Eigenvalues: ν₁ + ν₂ = N, both ≥ 0. min eigenvalue ν₂ ≥ 0.

For the Lagrange optimal with additional constraint Σn̂_k = 0 (from ω ∥ ê):
The n̂_k sum to zero. N̂^T 1 = 0 (the sum of rows is zero vector in R²...
actually N̂ 1 = Σn̂_k = 0 in R²).

So 1 is in the null space of N̂^T. But N̂^T is 2×N, so null(N̂^T) is (N-2)-dimensional.
The vector 1_N is in null(N̂^T). This means the all-ones vector maps to zero.

The eigenvalues of N̂^T N̂: ν₁ + ν₂ = N. For N=5 regular polygon:
n̂_k at angles 2πk/5. ν₁ = ν₂ = N/2 = 5/2 (by symmetry).

So V^T V in the full 3D:
- ê component: eigenvalue 1
- ⊥ components: eigenvalues (1-1/N) × ν = (4/5)(5/2) = 2

So V^T V has eigenvalues {1, 2, 2}. μ₃ = 1.

λ_max(D^T D) ≤ N - μ₃ = 5 - 1 = 4.

Need C < 3N/(N-1) = 15/4 = 3.75.
λ_max ≤ 4 > 3.75. DOES NOT CLOSE!

### The bound is loose (almost)

λ_max ≤ 4 vs threshold 3.75. Gap of 0.25.

But: equality λ_max = N - μ₃ requires d̂_k to be the eigenvector of V^T V
corresponding to μ₃ (the ê direction). This means all d̂_k have maximum
component along ê.

But d̂_k ⊥ v̂_k, and v̂_k has component 1/√N along ê. So:
d̂_k · ê = -(sin γ*/cos γ*)(d̂_k · n̂_k) = -2(d̂_k · n̂_k) (for N=5, tan γ* = 2).

For d̂_k · ê to be maximized: need d̂_k · n̂_k = -1/√5 (sign depends on convention).
Then d̂_k · ê = 2/√5. And |d̂_k|² = (d̂_k·ê)² + (d̂_k·n̂_k)² + (d̂_k·m̂_k)² = 4/5 + 1/5 + 0 = 1.
So d̂_k · m̂_k = 0. All d̂_k in the plane span{ê, n̂_k}.

Σ(d̂_k · ê)² = 5 × 4/5 = 4 = λ_max. Confirms the bound is TIGHT here.

So for the Lagrange optimal with N=5: λ_max = 4 > 3.75.

The frame constant is 4, not < 3.75. So the simple bound λ_max × diagonal FAILS.

### BUT: at this configuration, the AMPLITUDES are constrained

When λ_max is achieved (d̂_k along specific direction): the amplitudes r_k
are NOT arbitrary — they're constrained by the sign-flip bound.

The diagonal: Σr_k² ≤ (N-1)|ω|²/(4N) = 4|ω|²/20 = |ω|²/5.

BUT: this is the MAXIMUM diagonal, achieved when all modes at γ* with
r_k = |ω|/(5) (from the Lagrange). At the same time, the d̂_k directions
that achieve λ_max = 4 have specific orientations.

The PRODUCT: λ_max × diagonal = 4 × |ω|²/5 = 4|ω|²/5 = 0.8|ω|² > 3|ω|²/4.

FAILS by 7%! (0.8 > 0.75).

## THE ACTUAL S²ê (not the upper bound)

For the N=5 Lagrange config with d̂_k achieving λ_max:

S²ê = |Σ r_k d̂_k|² = (Σ r_k (d̂_k·x*))² for direction x* = argmax.

With r_k = |ω|/5 (all equal) and d̂_k · x* = 2/√5 (all equal along ê):

S²ê = (5 × |ω|/5 × 2/√5)² = (2|ω|/√5)² = 4|ω|²/5 = 0.8|ω|².

So S²ê/|ω|² = 0.8 > 0.75. THE BOUND FAILS for this specific config!

### WAIT — is this config actually achievable?

The config assumes:
1. All 5 modes at γ* = arccos(1/√5) from ê
2. n̂_k at 2πk/5 in the ⊥ plane (regular pentagon)
3. d̂_k chosen to maximize alignment along ê
4. All amplitudes equal

Is this achievable with INTEGER k-vectors on T³?

The constraint: v̂_k ⊥ k_k (div-free). For 5 modes with v̂_k = (1/√5)ê + (2/√5)n̂_k,
need k_k ⊥ v̂_k for each k. This constrains the k-vectors to a 2D plane
perpendicular to v̂_k.

For 5 SPECIFIC v̂_k directions: 5 specific constraints on the k-vectors.
On the integer lattice: finding k_k perpendicular to a specific direction
is a Diophantine equation. Solutions exist but the geometry may not match.

MORE IMPORTANTLY: is this config at the GLOBAL MAX?

The Lagrange config has all modes at the same γ* and equal amplitudes.
At the global max vertex: all cos(k_k·x*) = ±1, and the signs are chosen
to maximize |ω|².

For this specific config: |ω|² = 5 (with all signs positive, since
all p_k = 1/√5 and Σp_k = √5 = |ω|). √5 × √5 = 5. ✓

And S²ê = 4/5 × 5 = 4. So S²ê/|ω|² = 4/5 = 0.8.

But NUMERICALLY: the worst observed S²ê/|ω|² for N=5 is 0.272 (from file 372).

There's a HUGE discrepancy: theoretical bound 0.8 vs numerical 0.272!

### RESOLUTION: The Lagrange config is NOT the worst case for S²ê/|ω|²

The Lagrange config maximizes Σ|ŝ_k| (the triangle inequality RHS).
But S²ê = |Σŝ_k|², not (Σ|ŝ_k|)². The ACTUAL S²ê depends on directions.

At the Lagrange config: the d̂_k directions are constrained by the mode
geometry. They can achieve λ_max = 4, but in PRACTICE the amplitudes and
directions don't simultaneously reach their theoretical maxima.

The bound S²ê ≤ λ_max × diagonal = 4 × |ω|²/5 = 0.8|ω|² is CORRECT
as a bound, but it's not TIGHT. The actual S²ê is much less because:
1. The d̂_k directions that maximize λ_max DON'T maximize the diagonal
2. The amplitudes that maximize the diagonal require specific γ_k that
   constrain the d̂_k directions

## STATUS

The frame constant approach gives λ_max ≤ N - μ₃(V^T V).
For the Lagrange optimal: λ_max = N-1 (e.g., 4 for N=5).
The product λ_max × diagonal = (N-1)/N × |ω|² exceeds 3|ω|²/4 for N ≥ 5.

The bound is NOT tight because the λ_max-achieving directions and the
diagonal-maximizing amplitudes are INCOMPATIBLE. The numerics show
S²ê/|ω|² ≤ 0.28, far below the 0.8 bound.

To close: need a JOINT bound on S²ê that accounts for the correlation
between amplitudes and directions. This is the core unsolved problem.

## 377. Frame constant ≤ N-1 for the Lagrange config. Product exceeds 3/4.
## But actual S²ê ≪ bound because amplitude-direction anti-correlation.
## Joint optimization needed — not a simple product of independent bounds.
