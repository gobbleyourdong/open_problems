---
source: PROVING S²ê < 3|ω|²/4 at the vorticity maximum
type: PROOF ATTEMPT — the last lemma
file: 361
date: 2026-03-29
---

## The Statement

LEMMA: For any smooth divergence-free ω on T³ with u = BS(ω), at the
global max x* of |ω|:

  |S(x*)·ê|² ≤ C |ω(x*)|² for some C < 3/4.

where ê = ω(x*)/|ω(x*)| and S = sym(∇u).

## Fourier Decomposition

ω(x) = Σ_k ω̂_k e^{ikx} (sum over k ∈ Z³\{0}, ω̂_{-k} = ω̂_k*).

Div-free: k · ω̂_k = 0 for all k.

Biot-Savart: û_k = i(k × ω̂_k)/|k|².

Strain Fourier: Ŝ_k = -(1/2)(k ⊗ (k×ω̂_k) + (k×ω̂_k) ⊗ k)/|k|².

## S·ê decomposition

At x*: S(x*)·ê = Σ_k Ŝ_k·ê e^{ikx*} = Σ_k s_k

where s_k = Ŝ_k·ê × e^{ikx*} is a 3-vector for each k.

Explicitly: s_k = -(e^{ikx*}/(2|k|²)) [(ê·k)(k×ω̂_k) + (ê·(k×ω̂_k))k]

## Decompose ω̂_k relative to ê

For each k, decompose: ω̂_k = p̂_k ê + q̂_k where q̂_k ⊥ ê.

p̂_k = (ω̂_k · ê) (scalar, complex).
q̂_k = ω̂_k - p̂_k ê (vector in the plane ⊥ ê, complex).

Div-free: k · ω̂_k = 0 → (k·ê)p̂_k + k·q̂_k = 0.

## SELF-TERM VANISHING

For mode k with only the parallel part (q̂_k = 0, so ω̂_k = p̂_k ê):
k·ω̂_k = p̂_k(k·ê) = 0 requires k·ê = 0 (or p̂_k = 0).

If k·ê = 0: then k × ω̂_k = k × (p̂_k ê) = p̂_k(k×ê).
s_k = -(e^{ikx*}p̂_k/(2|k|²)) [(ê·k)(k×ê) + (ê·(k×ê)×(?))... hmm.

Let me redo. ê·k = k_ê (projection). ê·(k×ω̂_k):

If ω̂_k = p̂_k ê: k × ω̂_k = p̂_k(k × ê).
ê · (k × ê) = 0 (since k×ê ⊥ ê).

So: s_k = -(e^{ikx*}/(2|k|²)) [k_ê × p̂_k(k×ê) + 0 × k]
         = -(e^{ikx*}p̂_k k_ê/(2|k|²)) (k×ê)

This is nonzero when k_ê ≠ 0 and p̂_k ≠ 0. Wait — I said for the
parallel-only case we need k·ê = 0. So k_ê = 0 and s_k = 0. ✓

CONFIRMED: Modes where ω̂_k ∥ ê (purely parallel) contribute s_k = 0.

## PERPENDICULAR-ONLY CONTRIBUTION

For mode k with only perpendicular part (p̂_k = 0, ω̂_k = q̂_k ⊥ ê):
k · q̂_k = 0 (div-free, separate from the parallel condition).
k × q̂_k = k × ω̂_k.

ê · k = k_ê.
ê · (k × q̂_k): Let k_⊥ = k - k_ê ê (perpendicular part of k).
k × q̂_k has components in all directions. ê · (k × q̂_k) = ê · (k_⊥ × q̂_k + k_ê ê × q̂_k)
= ê · (k_⊥ × q̂_k) + k_ê (ê · (ê × q̂_k)) = ê · (k_⊥ × q̂_k) + 0.

Since k_⊥ and q̂_k are both ⊥ ê: k_⊥ × q̂_k has a component along ê.
ê · (k_⊥ × q̂_k) = (k_⊥ × q̂_k)_ê = the "z-component" in the ê-frame.

In 2D (the plane ⊥ ê): k_⊥ × q̂_k = |k_⊥||q̂_k|sin(ψ_k) (scalar).
Where ψ_k = angle between k_⊥ and q̂_k in the perpendicular plane.

So: s_k = -(e^{ikx*}/(2|k|²)) [k_ê(k × q̂_k) + |k_⊥||q̂_k|sin(ψ_k) × k]

This has components BOTH along ê and ⊥ ê.

## BOUND ON |s_k|

|s_k| ≤ (1/(2|k|²)) [|k_ê||k×q̂_k| + |k_⊥||q̂_k||sin ψ_k||k|]

|k × q̂_k| ≤ |k||q̂_k| (since k·q̂_k = 0 for div-free, equality holds: |k×q̂_k| = |k||q̂_k|).

So: |s_k| ≤ (|q̂_k|/(2|k|)) [|k_ê| + |k_⊥||sin ψ_k|]
         ≤ (|q̂_k|/(2|k|)) [|k_ê| + |k_⊥|]
         ≤ (|q̂_k|/(2|k|)) × √2|k| (by AM-QM since |k_ê|²+|k_⊥|²=|k|²)
         = |q̂_k|/√2.

So: |s_k| ≤ |q̂_k|/√2 for each mode.

## BOUND ON S²ê = |Σs_k|²

S²ê = |Σ_k s_k|² ≤ (Σ_k |s_k|)² ≤ (Σ_k |q̂_k|/√2)² = (1/2)(Σ_k |q̂_k|)².

## BOUND ON Σ|q̂_k|

At x*: ω(x*) = Σ_k ω̂_k e^{ikx*} = (Σp_k)ê + Σq_k.

Where p_k = Re(p̂_k e^{ikx*}) and q_k = q̂_k e^{ikx*}.

Σq_k = 0 (perpendicular components cancel at x*).
|ω(x*)| = Σp_k (all positive at global max, constructive interference).

Wait — Σq_k = 0 doesn't bound Σ|q̂_k|. The individual |q̂_k| can be large
as long as the vectors cancel when summed with the phases.

From the total energy: Σ(|p̂_k|² + |q̂_k|²) = Σ|ω̂_k|² = ||ω||²_{L²}/(2π)³.

And at x*: |ω(x*)|² = (Σp_k)² ≤ (Σ|p̂_k|)² (triangle inequality for p_k).

## THE KEY CONSTRAINT: GLOBAL MAX

For x* to be the GLOBAL max of |ω|²: for ALL x,
|ω(x)|² ≤ |ω(x*)|².

This means: max_x |ω(x)|² = (Σp_k)² (at x*, where phases align).

For any other point x: |Σω̂_k e^{ikx}|² ≤ (Σp_k)².

In particular: the L² energy is related to the max by
||ω||² = (2π)³ Σ|ω̂_k|² ≤ (2π)³ × (Σp_k)² = (2π)³|ω_max|².
(This is just the trivial Vol × max² ≥ L² bound.)

More usefully: consider points where the perpendicular part q(x) is
maximized. max_x |q(x)|² ≤ |ω(x)|² - 0 ≤ |ω_max|² (since p(x) could be 0).

But this just gives max|q| ≤ |ω_max|, which we knew.

## THE ENERGY PARTITION AT x*

Σ|q̂_k|² = Σ|ω̂_k|² - Σ|p̂_k|² (Pythagorean in Hilbert space).

At x*: (Σp_k)² = |ω_max|². And p_k ≤ |p̂_k| (since p_k = Re(p̂_k e^{ikx*}) ≤ |p̂_k|).

So: (Σp_k)² ≤ (Σ|p̂_k|)². And by Cauchy-Schwarz: (Σ|p̂_k|)² ≤ N × Σ|p̂_k|²
where N is the number of active modes.

This gives: Σ|p̂_k|² ≥ (Σ|p̂_k|)²/N ≥ (Σp_k)²/N = |ω_max|²/N.

And: Σ|q̂_k|² = Σ|ω̂_k|² - Σ|p̂_k|² ≤ Σ|ω̂_k|² - |ω_max|²/N.

For the S²ê bound: S²ê ≤ (1/2)(Σ|q̂_k|)² ≤ (1/2)(√N × √(Σ|q̂_k|²))²
= (N/2)Σ|q̂_k|² ≤ (N/2)(Σ|ω̂_k|² - |ω_max|²/N) = (N/2)Σ|ω̂_k|² - |ω_max|²/2.

For S²ê < (3/4)|ω_max|²: need
(N/2)Σ|ω̂_k|² - |ω_max|²/2 < (3/4)|ω_max|²
(N/2)Σ|ω̂_k|² < (5/4)|ω_max|²
Σ|ω̂_k|² < (5/(2N))|ω_max|².

But Σ|ω̂_k|² ≥ |ω_max|²/(Vol) (from ||ω||∞ ≤ √(Vol/... wait, this is backwards.

||ω||²_{L²} = (2π)³ Σ|ω̂_k|². And ||ω||²_{L²} ≤ (2π)³ |ω_max|² (since L² ≤ L∞ × √Vol).

Actually: ||ω||²_{L²} = ∫|ω|²dx ≤ (2π)³|ω_max|². So Σ|ω̂_k|² ≤ |ω_max|².

Then: (N/2)|ω_max|² < (5/4)|ω_max|²  →  N < 5/2. So N ≤ 2.

This only works for N ≤ 2 modes! For more modes, the bound is too loose.

## THE PROBLEM

The Cauchy-Schwarz step (Σ|q̂_k|)² ≤ N × Σ|q̂_k|² loses a factor of N.
For many modes: the bound degrades.

A better approach: use the ZERO-SUM constraint Σq_k = 0.

## USING THE ZERO-SUM

Σs_k = Σ L_k q_k where L_k is the linear map from q_k to s_k.

Since Σq_k = 0: Σs_k = Σ(L_k - L₀)q_k for any fixed L₀.

|Σs_k| ≤ Σ|L_k - L₀||q_k| ≤ max_k|L_k - L₀| × Σ|q_k|.

The operator L_k depends on k and ê. Its "size" is bounded by |s_k|/|q̂_k| ≤ 1/√2.

The diameter of {L_k}: max_{k,k'} |L_k - L_k'| ≤ 2/√2 = √2.

With optimal L₀ (Chebyshev center): max_k|L_k - L₀| ≤ 1/√2.

So: |Σs_k| ≤ (1/√2) Σ|q_k| where |q_k| = |q̂_k| (magnitudes at x*).

And: S²ê = |Σs_k|² ≤ (1/2)(Σ|q_k|)².

We need: (1/2)(Σ|q_k|)² < (3/4)|ω_max|².
i.e., Σ|q_k| < √(3/2)|ω_max| ≈ 1.225|ω_max|.

From Σq_k = 0: the triangle inequality gives |q₁| ≤ Σ_{k≠1}|q_k|.
But this doesn't bound Σ|q_k| in terms of |ω_max|.

The issue: Σ|q_k| can be much larger than |ω_max| if there are many
modes with large perpendicular components that cancel.

## THE MISSING INGREDIENT

The bound S²ê ≤ (1/2)(Σ|q_k|)² is too loose because:
1. The phase e^{ikx*} varies with k, causing CANCELLATION in Σs_k
2. The L_k operators point in DIFFERENT directions, causing more cancellation

The numerical data (S²ê < 0.287|ω|²) suggests the actual S²ê is much
smaller than the bound. The proof needs to capture the cancellations.

## POSSIBLE APPROACHES

### A. Parseval-type bound at x*
|S·ê|² at x* ≤ |S·ê|²_max ≤ ||S·ê||²_∞.
||S·ê||∞ ≤ ||S||∞ ≤ C||ω||∞ (CZ bound with C depending on regularity).
If C < √(3/4) ≈ 0.866: done. But CZ constants on T³ are > 1 generally.

### B. Variance bound using the max condition
At x*: Σp_k = |ω_max| with all p_k > 0 (constructive).
The "phase alignment" condition means: the ω̂_k phases at x* are
chosen to maximize |ω|. This CONSTRAINS the q_k phases at x*.

Specifically: ∂|ω|²/∂x_j = 0 at x* gives:
Σ_k ik_j ω̂_k · ω* e^{ikx*} = 0 (for j=1,2,3).

This is 3 complex constraints on the Fourier structure at x*.
Combined with Σq_k = 0: this gives 9 real constraints.
These constraints might force the phases of s_k to partially cancel.

### C. Direct computation for Beltrami + perturbation
Any smooth ω decomposes into Beltrami components. For small perturbations
from Beltrami: S·ê scales linearly with the perturbation, while |ω| is
O(1). So S²ê/|ω|² ~ ε² for ε-perturbation. This is « 3/4. But for
large perturbations: need the energy partition argument.

## STATUS

The S²ê < 3|ω|²/4 bound is the RIGHT target (replaces α < |ω|/2).
It holds numerically with 62% margin. The proof is stuck on bounding
Σ|q_k| or using the phase cancellations in Σs_k.

The most promising approach: use the max condition + zero-sum + phase
constraints to get a TIGHTER bound than the triangle inequality.

## 361. S²ê bound attempt: needs the phase cancellation.
## The triangle inequality loses too much; need Parseval-type argument.
