---
source: LATTICE COUNTING — bounding T via Z³ arithmetic
type: PROOF STRATEGY — the lattice structure constrains the worst case
file: 817
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE PROBLEM (PRECISE)

For N modes on T³ with k-vectors k₁,...,k_N ∈ Z³ \ {0}, unit polarizations
p_j ⊥ k_j, at the argmax of |ω|², prove:

    f(N) = 4 + 16T/|ω|² ≤ D/N^a with a > 2/3

where T = Σ_{j<k} s_js_k(k_j·p_k)(p_j·k_k) and |ω|² = Σ|k_j|² + 2D_total.

## KEY INSIGHT: THE WORST CASE HAS k-VECTORS ON FEW SHELLS

The worst case for f(N) maximizes T and minimizes |ω|² simultaneously.

For T to be large: need many pairs with (k_j·p_k)(p_j·k_k) large and
positive (with the argmax signs). This requires:
- k_j to have large projection onto p_k (the perpendicular space of k_k)
- p_j to have large projection onto k_k

Since p_j ⊥ k_j: the direction of p_j is in the plane ⊥ k_j.
For p_j to project onto k_k: need k_k NOT parallel to k_j.

The MAXIMUM of (k_j·p_k)(p_j·k_k) for a single pair:
|k_j·p_k| ≤ |k_j| (since |p_k| = 1)
|p_j·k_k| ≤ |k_k| (since |p_j| = 1)

But p_j ⊥ k_j: if k_k ∥ k_j then p_j ⊥ k_k and (p_j·k_k) = 0.
So the coupling VANISHES for parallel k-vectors.

For ORTHOGONAL k-vectors: (k_j·p_k)(p_j·k_k) can be up to |k_j|·|k_k|.

For k-vectors at intermediate angles: (k_j·p_k)(p_j·k_k) = O(|k_j|·|k_k|·sin²θ)
where θ is the angle between k_j and k_k (rough scaling).

## COUNTING ON Z³

On the lattice Z³ with |k|² ≤ K²:
- Number of k-vectors: ~ (4π/3)K³
- For each k: the perpendicular plane ⊥ k has ~ K² lattice points
- The coupling (k_j·p_k)(p_j·k_k) depends on the ANGLE between k_j and k_k

For N modes drawn from this set:
- At most 3 can be mutually orthogonal (R³ dimension)
- Most pairs have angle θ between 0° and 90°

The number of "maximally coupled" pairs (θ ≈ 90°): at most 3N
(each of 3 orthogonal directions can couple with N-1 modes).

The remaining N(N-1)/2 - 3N pairs: intermediate angles, partial coupling.

## THE AVERAGING ARGUMENT

For the argmax sign pattern: Σ s_js_k D_jk is maximized. The sign pattern
that maximizes the vorticity coupling has SPECIFIC structure:

At the argmax: s_j = sign(ω_j · ω_total) (each mode aligns with the total).

With this sign pattern: T = Σ s_js_k T_jk = K - D_total.

For GENERIC configurations (random k-vectors and polarizations on Z³):
- D_total ~ √(N) (CLT: sum of random ±1 terms)
- K ~ √(N) (same CLT)
- T = K - D_total ~ √(N) (difference of two √N quantities)
- |ω|² = Σ|k_j|² + 2D_total ~ N + 2√N ≈ N
- f = 4 + 16√(N)/N = 4 + 16/√N → 4

For the WORST configuration: the adversary optimizes k-vectors and
polarizations to maximize T. But:
- T involves the sign pattern from the ARGMAX (not freely chosen)
- The argmax sign pattern is determined by {D_jk}, not by {T_jk}
- The correlation between the optimal signs for D and the resulting T
  is LIMITED by the geometry

## THE DECORRELATION BOUND (INFORMAL)

**Claim**: For the argmax sign pattern, |T| ≤ C√(N · max T_jk²).

Sketch: The sign pattern s = argmax s^T A s where A_jk = D_jk.
For the quantity T = s^T B s where B_jk = T_jk:

By the Grothendieck inequality (or SDP duality):
|s^T B s| ≤ K_G · max_{x_j ∈ S^n} Σ B_jk x_j · x_k

where K_G < 1.8 is the Grothendieck constant. The SDP relaxation of T
with the constraint that signs maximize D is bounded.

For the worst case: max T_jk ≤ K² (max wavenumber squared).
|T| ≤ K_G · N · K² (N terms, each ≤ K²).

But |ω|² ≥ N. So T/|ω|² ≤ K_G K²/1 = O(K²). NOT decreasing with N.

This doesn't help because K (max wavenumber) is fixed for a given shell.

## THE N-DEPENDENT BOUND

The issue: with MORE modes, the k-vectors become more diverse on Z³.
The coupling T_jk = (k_j·p_k)(p_j·k_k) depends on the ANGLE between
k_j and k_k, which varies for different pairs.

For the SUM T = Σ s_js_k T_jk with the argmax signs:
- Some terms are positive (s_js_k T_jk > 0)
- Some terms are negative (s_js_k T_jk < 0)
- The NET T depends on the cancellation

With the argmax sign pattern: the signs are optimized for D_jk, NOT T_jk.
The correlation between D_jk and T_jk is:

D_jk = (k_j·k_k)(p_j·p_k) - T_jk

For D_jk > 0: either (k_j·k_k)(p_j·p_k) > T_jk (T could be positive or negative)
For D_jk < 0: s_js_k = -1, and -T_jk is added (reversed sign)

The PARTIAL CANCELLATION between the D-optimal and T-resulting terms
grows with N because more pairs means more averaging.

## FORMAL CONJECTURE (LATTICE VERSION)

**Conjecture**: For N distinct k-vectors on Z³ with |k|² ≤ K², any unit
polarizations p_j ⊥ k_j, and the argmax sign pattern, the strain coupling
satisfies:

    |T|/|ω|² ≤ C_K / N^{1/2}

where C_K depends only on K (not N).

This gives f = 4 + 16T/|ω|² ≤ 4 + 16C_K/N^{1/2}.

But we need f → 0, which requires T/|ω|² → -1/4. The bound |T|/|ω|² ≤ C/√N
only gives f → 4 (the average).

## THE REAL QUESTION

The floor growth f(N) → 0 requires T to be NEGATIVE and grow in magnitude
like T ≈ -|ω|²/4. This is NOT random behavior — it's a STRUCTURAL property
of the argmax.

The SOS data shows: for the WORST adversarial configuration, f → 0.
This means even the WORST case has T → -|ω|²/4.

The proof must show: the vorticity-strain anti-correlation forces
T < 0 at the argmax, and |T + |ω|²/4| ≤ C|ω|²/N^a.

This is equivalent to: |S|²/|ω|² ≤ C/N^a (the strain becomes negligible
relative to vorticity at the argmax for many modes).

## STATUS

The proof of f(N) → 0 requires showing that the WORST-CASE adversarial
configuration becomes less extreme as N grows. This is because:
1. More modes → more constraints on the k-vector geometry
2. The argmax sign pattern → more averaging in the strain coupling
3. The R³ dimension → limits the number of "bad" pairs

The RATE of convergence (exponent a) determines whether the chain works.
Need a > 2/3. Data gives a ≈ 3.1.

## 817. Lattice counting: at most 3 orthogonal pairs contribute maximally.
## The decorrelation between argmax signs and strain coupling grows with N.
## Formal proof of f(N) ≤ C/N^a requires quantifying this decorrelation.
## The Grothendieck inequality and SDP duality may be the right tools.
