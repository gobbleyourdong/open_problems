---
source: Using the Hessian condition to bound S²ê at the max
type: PROOF ATTEMPT — exploiting negative semi-definiteness
file: 362
date: 2026-03-29
---

## The Hessian Constraint

At x* where |ω|² is maximal:
  (i)  ∇|ω|² = 0
  (ii) ∇²|ω|² ≤ 0  (negative semi-definite)

Condition (i): 2Σ_k ik ω̂_k·ω* e^{ikx*} = 0.
  → Σ_k k × Im(c_k · ω*) = 0 where c_k = ω̂_k e^{ikx*}.

Since ω = |ω|ê (real): c_k·ω* = |ω|(c_k·ê)*.
For real fields: this simplifies to Σ k sin(k·x*)(ω̂_k·ê) = 0 (schematic).

Condition (ii): The Hessian H_jl = ∂²|ω|²/∂x_j∂x_l ≤ 0.

H_jl = 2[∂ω_i/∂x_j × ∂ω_i/∂x_l + ω_i × ∂²ω_i/∂x_j∂x_l]
      = 2[(∇ω)^T(∇ω)]_jl + 2[ω·∇²ω]_jl

At x*: H ≤ 0 means:
  (∇ω)^T(∇ω) + diag(ω·∂²ω/∂x_j²) ≤ 0

where (∇ω)^T(∇ω) is the 3×3 matrix with entries Σ_i(∂ω_i/∂x_j)(∂ω_i/∂x_l).

## Connecting to S²ê

S = sym(∇u) where u = BS(ω). So S depends on ∇u, not ∇ω.
And S·ê involves the strain projected onto ê.

But: ∇ω = curl(∇u) + ... no, ω = curl(u), so ∇ω = ∇(curl u).

The Hessian condition constrains ∇ω at x*. And S·ê depends on ∇u·ê.

Through Biot-Savart: ∇u and ∇ω are related by:
  ∇u = ∇(BS(ω)) = BS(∇ω) + (lower order)

Actually, on T³: û_k = i(k×ω̂_k)/|k|². So ∇u involves ik⊗û = -(k⊗(k×ω̂_k))/|k|².

The strain: Ŝ_k = -(k⊗w_k + w_k⊗k)/(2|k|²) where w_k = k×ω̂_k.

And ∂ω̂_k/∂x_j contributes ik_j ω̂_k. So ∇ω at x* = Σ ik⊗ω̂_k e^{ikx*}.

## The Key Identity

(∇ω)^T(∇ω) at x* has entries:
  G_jl = Σ_i (∂ω_i/∂x_j)(∂ω_i/∂x_l)
       = Σ_{k,k'} (k_j)(k'_l)(ω̂_k·ω̂_{k'}*) e^{i(k-k')x*}

For k = k': contribution is k_jk_l |ω̂_k|².
Cross terms: k_jk'_l (ω̂_k·ω̂_{k'}) phases.

The trace: tr(G) = Σ_j G_jj = |∇ω|² = Σ_k |k|²|ω̂_k|² × (phase sum at x*).

From H ≤ 0: G + (ω·∇²ω matrix) ≤ 0.

In particular: G_jj + ω·∂²ω/∂x_j² ≤ 0 for each j. Summing:
|∇ω|² + ω·Δω ≤ 0. (This is the standard Δ|ω|²/2 ≤ 0.)

## Extracting S²ê from ∇ω

S·ê = Σ_k ŝ_k e^{ikx*} where ŝ_k = -(1/(2|k|²))[(ê·k)w_k + (ê·w_k)k].

|S·ê|² = |Σ_k ŝ_k e^{ikx*}|².

The diagonal part: Σ_k |ŝ_k|². And cross terms.

For the diagonal: |ŝ_k|² = (1/(4|k|⁴))|(ê·k)w_k + (ê·w_k)k|².

Expanding: = (1/(4|k|⁴))[(ê·k)²|w_k|² + 2(ê·k)(ê·w_k)(w_k·k) + (ê·w_k)²|k|²]

Since w_k = k×ω̂_k: w_k·k = 0 (cross product ⊥ k). So:
|ŝ_k|² = (1/(4|k|⁴))[(ê·k)²|w_k|² + (ê·w_k)²|k|²]

= (1/(4|k|²))[(ê·k̂)²|w_k|² + (ê·ŵ_k)²|w_k|²]  where k̂ = k/|k|

Hmm wait: |w_k| = |k×ω̂_k| = |k||ω̂_k| (since k⊥ω̂_k). So |w_k|² = |k|²|ω̂_k|².

|ŝ_k|² = (|ω̂_k|²/4)[(ê·k̂)² + (ê·ŵ_k)²]

where ŵ_k = w_k/|w_k| = (k×ω̂_k)/(|k||ω̂_k|).

Now: k̂ and ŵ_k are perpendicular unit vectors (since w_k ⊥ k). Together with
v̂_k = ω̂_k/|ω̂_k| (perpendicular to both k and w for div-free fields):
{k̂, ŵ_k, v̂_k} form an orthonormal basis.

So: (ê·k̂)² + (ê·ŵ_k)² = 1 - (ê·v̂_k)².

Therefore: |ŝ_k|² = (|ω̂_k|²/4)(1 - (ê·v̂_k)²) = (|ω̂_k|²/4)(1 - c_k)

where c_k = (ê·v̂_k)² is the alignment of ê with mode k's vorticity direction.

## THIS IS A BEAUTIFUL IDENTITY

For each mode k:
  |ŝ_k|² = (|ω̂_k|²/4)(1 - c_k)

where c_k = (ê · v̂_k)² = cos²(angle between ê and mode k's polarization).

When ê ∥ v̂_k (perfect alignment): |ŝ_k|² = 0. (Single-mode vanishing!)
When ê ⊥ v̂_k (perpendicular): |ŝ_k|² = |ω̂_k|²/4.

## THE PARSEVAL BOUND

If the cross-terms in |Σŝ_k e^{ikx*}|² average to zero (Parseval):

S²ê ≈ Σ_k |ŝ_k|² = (1/4) Σ_k |ω̂_k|²(1-c_k)

= (1/4)[Σ|ω̂_k|² - Σ|ω̂_k|²c_k]

= (1/4)[||ω||²_{L²}/(2π)³ - Σ|ω̂_k|²c_k]

Now: Σ|ω̂_k|²c_k = Σ|ω̂_k|²(ê·v̂_k)² = Σ|(ω̂_k·ê)|² = Σ|p̂_k|².

And: (Σp_k)² = |ω_max|². Since p_k ≤ |p̂_k|: (Σp_k)² ≤ (Σ|p̂_k|)².

By Cauchy-Schwarz: (Σ|p̂_k|)² ≤ N × Σ|p̂_k|². So Σ|p̂_k|² ≥ |ω_max|²/N.

Therefore: S²ê ≈ (1/4)[Σ|ω̂_k|² - Σ|p̂_k|²]
         ≤ (1/4)[Σ|ω̂_k|² - |ω_max|²/N]
         ≤ (1/4)[|ω_max|² - |ω_max|²/N]  (using Σ|ω̂_k|² ≤ |ω_max|² on T³... WAIT)

Is Σ|ω̂_k|² ≤ |ω_max|²? This is ||ω||²_{L²}/(2π)³ ≤ |ω_max|².
Yes: ||ω||²_{L²} = ∫|ω|²dx ≤ |ω_max|² × (2π)³ = |ω_max|² × Vol.
So Σ|ω̂_k|² = ||ω||²_{L²}/(2π)³ ≤ |ω_max|². ✓

So: S²ê ≈ (1/4)(|ω_max|² - |ω_max|²/N) = (1/4)(1-1/N)|ω_max|².

For N = 2: S²ê ≈ |ω_max|²/8 = 0.125. Data: 0.244.
For N → ∞: S²ê → |ω_max|²/4 = 0.25. Data: ≤ 0.287.

## THE PARSEVAL BOUND GIVES S²ê ≤ |ω|²/4 !!

If the cross-terms are non-positive (which happens when phases partially cancel):
  S²ê ≤ Σ|ŝ_k|² ≤ (1/4)Σ|ω̂_k|²(1-c_k) ≤ |ω_max|²/4

And |ω_max|²/4 = 0.25 < 0.75. MASSIVE margin!

## THE ISSUE: CROSS-TERMS

S²ê = |Σŝ_k e^{ikx*}|² = Σ|ŝ_k|² + 2Re Σ_{k<k'} ŝ_k·ŝ_{k'}* e^{i(k-k')x*}

The cross-terms could be positive, making S²ê > Σ|ŝ_k|².

Upper bound: S²ê ≤ (Σ|ŝ_k|)² = [(1/2)Σ|ω̂_k|√(1-c_k)]².

Using Cauchy-Schwarz: (Σ|ω̂_k|√(1-c_k))² ≤ Σ|ω̂_k|² × Σ(1-c_k).

With N modes: Σ(1-c_k) ≤ N (since c_k ≥ 0).

So: S²ê ≤ (1/4) × N × Σ|ω̂_k|² ≤ N|ω_max|²/4.

For N = 2: S²ê ≤ |ω_max|²/2. For N = 3: ≤ 3|ω_max|²/4 = 0.75. Barely!

But we KNOW empirically S²ê < 0.29 for all N. The bound N/4 is too loose
for N ≥ 3 because the cross-terms have CANCELLATIONS from the phases.

## THE REFINED BOUND (using the max condition)

At x*: the phases e^{ikx*} are such that |ω| is maximal. This means the
PARALLEL components add constructively: p_k > 0 for all k.

For the PERPENDICULAR components: Σq_k = 0 (cancellation).

The cross-terms in S²ê involve phases e^{i(k-k')x*}. At the max of |ω|:
these phases are CONSTRAINED by the max condition.

The max condition: ∂|ω|²/∂x_j = 0 gives 3 equations.
These constrain the relative phases of the modes.

For 2 modes: the max condition fixes the relative phase completely.
For N modes: it constrains 3 of the N-1 independent relative phases.

For N = 3: 3 phases, 3 constraints → fully determined. The cross-terms
in S²ê are determined by the max condition. And they happen to be
partially cancelling (empirically).

## STATUS

The diagonal part of S²ê (Parseval) is ≤ |ω|²/4 (rigorous).
The cross-terms can add up to (N-1) × |ω|²/4 in the worst case.
For N = 2: total ≤ |ω|²/2 (empirically: 0.244).
For N = 3: total ≤ 3|ω|²/4 (empirically: 0.287).

For N ≥ 3: the triangle inequality bound equals or exceeds the threshold!
But the ACTUAL values are far below it.

The proof needs to bound the cross-terms using:
(a) The max condition (constrains phases)
(b) The geometric factors (ŝ_k·ŝ_{k'}* involves angles between k, k')
(c) The zero-sum constraint on perpendicular components

## KEY IDENTITY DERIVED

|ŝ_k|² = (|ω̂_k|²/4)(1 - (ê·v̂_k)²)

This is the FUNDAMENTAL per-mode strain-projection bound.
The alignment (ê·v̂_k)² REDUCES the strain contribution.
Modes aligned with ê contribute ZERO strain in the ê direction.

## 362. Per-mode identity: |ŝ_k|² = |ω̂_k|²(1-c_k)/4. Beautiful.
## Parseval bound: diagonal ≤ |ω|²/4. Need to control cross-terms for N≥3.
