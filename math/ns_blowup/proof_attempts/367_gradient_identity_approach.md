---
source: New approach via |S|² = |∇u|² - |ω|²/2 identity
type: PROOF — clean short proof for orthogonal modes + general extension path
file: 367
date: 2026-03-29
---

## THE KEY IDENTITY (pointwise, exact, no approximation)

For any smooth velocity field u with S = sym(∇u) and ω = curl u:

  **|S|² = |∇u|² - |ω|²/2**

PROOF: ∇u = S + Ω where Ω = asym(∇u). By orthogonality:
  |∇u|² = |S|² + |Ω|²
Standard identity: |Ω|²_F = |ω|²/2 (for 3D).
So: |S|² = |∇u|² - |ω|²/2. ∎

## CONSEQUENCE FOR THE BARRIER

S²ê ≤ (2/3)|S|² (trace-free, largest eigenvalue bound)

Combined: **S²ê ≤ (2/3)(|∇u|² - |ω|²/2)**

For S²ê < 3|ω|²/4: sufficient that |∇u|² < 13|ω|²/8.

## PROOF FOR N ORTHOGONAL MODES (equal amplitude)

THEOREM: For N ≤ 3 modes with mutually orthogonal wavevectors on T³,
at the global maximum of |ω|: S²ê ≤ |ω|²/3 < 3|ω|²/4.

### Step 1: |∇u|² = N at lattice vertices

For N modes ω = Σ v̂_k cos(k_k·x) with orthogonal k_k (unit amplitude):

u = Σ (k_k × v̂_k) sin(k_k·x) / |k_k|²

∇u = Σ (k_k × v̂_k) ⊗ k_k cos(k_k·x) / |k_k|²

At a vertex x* where cos(k_k·x*) = ±1 for all k:

  ∇u(x*) = Σ s_k (k_k × v̂_k) ⊗ k_k / |k_k|²

where s_k = cos(k_k·x*) = ±1. Let A_k = s_k (k_k × v̂_k) ⊗ k_k / |k_k|².

|A_k|²_F = |k_k × v̂_k|² × |k_k|² / |k_k|⁴ = |v̂_k|² / 1 = 1
(using k_k ⊥ v̂_k for div-free, so |k_k × v̂_k| = |k_k|·|v̂_k|)

Cross terms: A_j : A_k = s_j s_k (w_j · w_k)(k_j · k_k) / (|k_j|²|k_k|²)
where w_k = k_k × v̂_k.

For ORTHOGONAL k's: k_j · k_k = 0 for j ≠ k. So A_j : A_k = 0.

Therefore: **|∇u(x*)|² = Σ|A_k|² = N**. ∎

### Step 2: |S|² = N - |ω|²/2 at vertices

From Step 1: |∇u|² = N.
From the identity: |S|² = |∇u|² - |ω|²/2 = N - |ω|²/2. ∎

### Step 3: |ω|² ≥ N at the global max

At vertex x*, ω(x*) = Σ s_k v̂_k.

Average over all 2^N sign choices: <|Σ s_k v̂_k|²> = Σ|v̂_k|² = N
(cross-terms <s_j s_k> = 0 for j ≠ k).

The MAXIMUM over sign choices ≥ average: max |ω|² ≥ N.

The global max of |ω|² over ALL x is at a vertex (for orthogonal k's with
trig dependence, the max of |Σ a_k cos(k_k·x) v̂_k|² factors into products
and is maximized when each cos = ±1). So: |ω(x*)|² ≥ N. ∎

### Step 4: Combine

S²ê ≤ (2/3)|S|² = (2/3)(N - |ω|²/2) ≤ (2/3)(N - N/2) = N/3.

S²ê/|ω|² ≤ (N/3)/N = 1/3.

Since 1/3 < 3/4: **S²ê < 3|ω|²/4**. ∎

TIGHTER: S²ê ≤ (2/3)(N - |ω|²/2). Since |ω|² ≥ N:
  S²ê/|ω|² ≤ (2/3)(N/|ω|² - 1/2) ≤ (2/3)(1 - 1/2) = 1/3.

### Verification against known results

N=1: S²ê ≤ 1/3. Exact: S²ê = 0. Bound is loose (0 < 1/3). ✓
N=2: S²ê ≤ 2/3. Exact: S²ê = |ω|²/4 ≤ 1 (when |ω|²=4).
     Bound: 2/3 < 3/4 ✓ but looser than the exact 1/4.
N=3: S²ê ≤ 1. Exact max: S²ê = 1 (at |ω|²=3).
     Bound: 1 ≤ 1 (TIGHT!). And 1/|ω|² = 1/3 < 3/4 ✓

## EXTENSION TO GENERAL FIELDS: THE KEY QUESTION

For general smooth div-free ω = Σ ω̂_k e^{ikx} (infinitely many modes,
k's not necessarily orthogonal):

  |∇u(x*)|² = |Σ (∇u)_k e^{ikx*}|² where |(∇u)_k|_F = |ω̂_k| for each k.

So |∇u| and |ω| are built from the same "amplitudes" but different "directions"
(matrix-valued vs vector-valued).

The question: can |∇u(x*)|²/|ω(x*)|² be bounded at the max of |ω|?

For orthogonal k's: ratio ≤ 1 (proven above via |∇u|²=N, |ω|²≥N).
For general k's: the cross-terms k_j·k_k ≠ 0 modify |∇u|².

SPECIFICALLY: at x* where e^{ikx*} has specific phases:

|∇u|² = Σ|ω̂_k|² + 2Σ_{j<k} Re[A_j:A_k* · e^{i(k_j-k_k)·x*}]

where A_k = ik_k ⊗ û_k.

The cross-terms COULD be positive (increasing |∇u|²) or negative.

THE CRUCIAL STRUCTURE: At the max of |ω|, the phases e^{ikx*} are chosen
to maximize |ω|². The same phases affect |∇u|². The question is whether
maximizing |ω|² also constrains |∇u|².

## NUMERICAL TEST NEEDED

Test: compute |∇u|²/|ω|² at the max of |ω| for:
1. Random multi-mode fields (N = 2,3,5,10,20,50)
2. Non-orthogonal k-vectors
3. Random amplitudes and polarizations
4. Find the WORST CASE ratio

If |∇u|²/|ω|² < 13/8 = 1.625 universally: then S²ê < 3|ω|²/4 follows
from the trace-free bound.

From file 360 Monte Carlo: worst |S|²/|ω|² = 0.78.
|∇u|²/|ω|² = |S|²/|ω|² + 1/2 = 0.78 + 0.5 = 1.28 < 1.625. ✓

## STATUS

This provides:
1. A CLEANER proof for orthogonal modes than the CS approach (files 363-365)
2. A clear TARGET for the general case: |∇u|²/|ω|² < 13/8
3. A MECHANISM: the identity |S|² = |∇u|² - |ω|²/2 shows strain is
   bounded by the "excess" of ∇u over ω (which is small at the max).

## 367. Clean proof via |∇u|² = N for orthogonal modes.
## General case reduces to: |∇u|²/|ω|² < 13/8 at max of |ω|.
