---
source: DIRECTION DIVERSITY — strain directions are 55-68° apart (near-uniform)
type: DATA + PROOF DIRECTION — diversity bound would close the Key Lemma
file: 423
date: 2026-03-30
---

## THE DATA

At the global max of |ω| for N=5 modes (K=√2 shell):

Average pairwise angle between ŝ_k directions: **55-68°**
(Expected for random vectors in R³: 60°. So directions are near-uniform.)

S²ê/|ω|² = 0.01-0.10 (vs triangle bound: 0.25, vs threshold: 0.75)

## THE PROOF PATH

### Step 1: Prove d̂_k diversity ≥ 45° average (from Biot-Savart)

d̂_k ∈ plane ⊥ v̂_k (Biot-Savart constraint).
v̂_k ⊥ k_k (div-free constraint).
Different k_k → different v̂_k planes → different d̂_k directions.

For N ≥ 4 modes in R³: the v̂_k planes can't all coincide (pigeonhole).
The d̂_k must span ≥ 2 dimensions → average angle ≥ 45°.

### Step 2: Diversity bound → S²ê bound

|Σ r_k d̂_k|² = Σ r_k² + 2Σ_{j<k} r_j r_k (d̂_j·d̂_k)

If average cos(angle) ≤ c (where c < 1):
cross-terms ≤ c × (Σr_k)² - c × Σr_k² = c × [(Σr_k)² - Σr_k²]

S²ê ≤ Σr_k² + c[(Σr_k)² - Σr_k²] = (1-c)Σr_k² + c(Σr_k)²

With Σr_k² ≤ (N-1)|ω|²/(4N) and (Σr_k)² ≤ (N-1)|ω|²/4:

S²ê ≤ (1-c)(N-1)|ω|²/(4N) + c(N-1)|ω|²/4
= (N-1)|ω|²/4 × [(1-c)/N + c]
= (N-1)|ω|²/4 × [c + (1-c)/N]

For c = 0.5 (cos 60°): [0.5 + 0.5/N] = [0.5 + 0.1] = 0.6 (N=5)
S²ê ≤ 4/4 × 0.6 × |ω|² = 0.6|ω|² < 0.75. ✓ (margin 20%)

For c = 0 (cos 90°, orthogonal): [0 + 1/N] = 0.2
S²ê ≤ 0.2|ω|² < 0.75. ✓ (margin 73%)

### Step 3: What c is achievable?

From the data: average cos(angle) ≈ cos(60°) = 0.5.

For the WORST case: all d̂_k in the same HEMISPHERE (max alignment).
Then average cos ≤ 1/2 (for uniform distribution on hemisphere).

For Biot-Savart-constrained d̂_k: the constraint v̂_k ⊥ k_k FORCES
diversity when the k_k vectors are diverse (which they are on Z³).

## THE REMAINING STEP

Prove: for N ≥ 5 modes with div-free constraint, at the global max:

    average cos(d̂_j, d̂_k) ≤ 1/2

This is a geometric constraint from the Biot-Savart structure.
If proven: S²ê ≤ 0.6|ω|² < 3|ω|²/4 for N ≥ 5. QED.

Combined with N ≤ 4 (proven per-mode): REGULARITY.

## 423. Diversity ≈ 60° (near-uniform). If avg cos ≤ 1/2: proof closes.
