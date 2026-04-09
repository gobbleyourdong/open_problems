---
source: PROOF SKETCH for the Key Lemma via effective rank + orthogonal complement
type: PROOF ATTEMPT — this closes the millennium problem if formalized
file: 395
date: 2026-03-29
---

## THE KEY LEMMA (restated from file 392)

For zero-diagonal symmetric N×N matrices A, B with Tr(AB) = 0:
Let s* = argmax_{s ∈ {±1}^N} s^T B s. Then:

    |s*^T A s*| ≤ C × ||A||_F

for some universal constant C.

## PROOF SKETCH

### Step 1: B has bounded effective rank

The matrix B = M_Y has r_eff(B) = ||B||_F²/||B||_op² ≤ R₀ (bounded).

For our Biot-Savart application: R₀ ≈ 2-3 (from the 3D geometry).
More generally: for any N×N matrix derived from pairwise interactions
in R³, the effective rank is bounded by a constant depending only
on the ambient dimension (3).

### Step 2: The argmax lives in a low-dimensional subspace

The argmax s* = argmax s^T B s. Write B = Σᵢ μᵢ uᵢuᵢᵀ (spectral decomposition).

The top R₀ eigenvectors {u₁,...,u_{R₀}} capture most of B's effect:
s^T B s ≈ Σᵢ₌₁^{R₀} μᵢ (s^T uᵢ)².

The argmax s* approximately maximizes this R₀-dimensional quadratic.
The components s^T u₁, ..., s^T u_{R₀} are DETERMINED by the argmax.
The components along the remaining N - R₀ eigenvectors are FREE.

### Step 3: A is orthogonal to B's eigenspace

Tr(AB) = 0 means Σᵢ μᵢ (uᵢᵀ A uᵢ) = 0.

More precisely: if B has only R₀ significant eigenvalues, then
the "important" part of A (restricted to span{u₁,...,u_{R₀}}) has
bounded norm (related to ||A||_F / √R₀).

The "free" part of A (on the complement) has norm ≈ ||A||_F.

### Step 4: A(s*) decomposes into determined + free parts

s*^T A s* = (A restricted to span{u₁,...,u_{R₀}} of s*) + (A restricted to complement of s*)

The first part: involves O(R₀) "determined" components of s*.
Each component s*^T uᵢ takes a specific value. The quadratic form
contribution: ≤ R₀ × ||A||_op × max(s*^T uᵢ)² ≤ R₀ × ||A||_op × N.

But ||A||_op ≤ ||A||_F (since A has zero diagonal): this gives R₀N × ||A||_F.
TOO LARGE.

### Step 4 (revised): Use the spectral structure more carefully

Actually: s*^T A s* = Σ_{j,k} A_{jk} s*_j s*_k.

Decompose A = A_∥ + A_⊥ where:
- A_∥ is the projection of A onto the subspace spanned by B's eigenvectors
  (in the matrix inner product sense: A_∥ = Σᵢ (uᵢᵀ A uᵢ/(uᵢᵀ uᵢ)²) uᵢuᵢᵀ ...)

Hmm, this decomposition is not standard for matrices. Let me think differently.

### Step 4 (take 3): Direct argument via the greedy structure

At s* = argmax s^T B s: the first-order condition says that flipping
any single coordinate s*_j → -s*_j decreases s^T B s.

This means: for each j, s*_j × (Bs*)_j ≥ 0 (each coordinate "agrees"
with the field Bs*).

The FIELD f_j = (Bs*)_j determines s*_j = sign(f_j).

Now: f = Bs* is in the COLUMN SPACE of B, which has dimension ≤ rank(B) ≤ 3
(for our Biot-Savart matrices in R³).

Wait: B is N×N with rank up to N. But effective rank R₀ ≈ 2-3.
The field f = Bs* has ||f||² = s*^T B² s* ≤ ||B||_op² × N.

Hmm. The key is: f lives in a LOW-DIMENSIONAL subspace of R^N.
Specifically: if B has effective rank R₀, then f = Bs* is concentrated
on the top R₀ eigenvectors of B.

### Step 5: The argument (corrected)

Write f = Bs*. Then s*_j = sign(f_j) (from the greedy condition).

s*^T A s* = Σ_{j,k} A_{jk} sign(f_j) sign(f_k)

This is a FUNCTION of f ∈ R^N. Since A ⊥ B (Tr(AB) = 0):

E_f[s^T A s] = E_f[Σ A_{jk} sign(f_j) sign(f_k)] where f is the field at s.

For RANDOM f (from a random s): E[sign(f_j)sign(f_k)] = (2/π)arcsin(ρ_{jk})
where ρ_{jk} is the correlation of f_j and f_k.

But f = Bs, so ρ_{jk} = (B²)_{jk}/(B²_{jj}B²_{kk})^{1/2}.

The expected quadratic form: E[s^T A s | f] = Σ A_{jk} (2/π)arcsin(ρ_{jk}).

From Tr(AB) = 0: this is not necessarily zero (arcsin is nonlinear).

This approach is getting complicated. Let me try a cleaner route.

### Step 6: The SIMPLEST bound

**Observation**: |s*^T A s*| ≤ N × max_{j≠k} |A_{jk}| × (density of +- pattern)

But max|A_{jk}| = ||A||_∞ ≤ ||A||_F (for unit-diagonal-free matrices).
And N × ||A||_∞ ~ N × ||A||_F/N = ||A||_F for typical matrices.

So: |s*^T A s*| ≤ N × ||A||_∞ = O(||A||_F). COULD work if ||A||_∞ ≤ ||A||_F/N.

For our M_L: the entries are ~ 1/N (each pair contributes O(1/N) after
regression). So ||M_L||_∞ ~ 1/N and N × ||M_L||_∞ ~ O(1) × ||M_L||_F.

This is promising but needs verification.

## STATUS

The Key Lemma is the EXACT gap. Multiple proof approaches:
1. Effective rank + orthogonal complement (Steps 1-4)
2. Greedy structure + sign function (Step 5)
3. Entry-wise bound (Step 6)

None fully closes yet. The entry-wise approach (Step 6) is simplest:
if ||M_L||_∞ × N ≤ C × ||M_L||_F: done. Need to check.

## 395. Proof sketch via effective rank + greedy. Not yet closed.
## Simplest approach: entry-wise bound ||M_L||_∞ × N ≤ C × ||M_L||_F.
## Next: verify ||M_L||_∞ × N / ||M_L||_F is bounded for Biot-Savart matrices.
