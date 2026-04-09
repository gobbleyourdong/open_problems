---
source: PROVING S²ê < (3/4)|ω|² via per-mode structure + Cauchy-Schwarz
type: PROOF ATTEMPT
file: 333
date: 2026-03-29
---

## Setup

At x* where |ω| is maximal. ê = ω/|ω|.

S·ê = Σ_k s_k where s_k is the mode-k contribution to S·ê at x*.

From file 361: s_k = -(c_k/(2|k|²)) [(ê·k)w_k + (ê·w_k)k]
where c_k = cos(k·x*) (for real fields) and w_k = k × v̂_k (with ω̂_k ~ v̂_k).

## Per-Mode Self-Vanishing

For mode k contributing ω_k = a_k v̂_k cos(k·x):
At the SPECIFIC max of |ω_k| (where cos(k·x) = 1):
  s_k = -(a_k/(2|k|²)) [(v̂_k·k)(k×v̂_k) + (v̂_k·(k×v̂_k))k]
  = -(a_k/(2|k|²)) [0 + 0] = 0  (since v̂_k ⊥ k and v̂_k ⊥ k×v̂_k)

So s_k = 0 when ê = v̂_k (the mode's own polarization). ✓

## At the Mixture Max

ê ≠ v̂_k for any specific k. Instead ê is the AVERAGE direction.

Decompose ê = p_k v̂_k + q_k (where q_k ⊥ v̂_k, |p_k|²+|q_k|²=1).

Then: ê·k = p_k(v̂_k·k) + q_k·k = 0 + q_k·k = q_k·k (since v̂_k ⊥ k).
And: ê·w_k = p_k(v̂_k·w_k) + q_k·w_k = 0 + q_k·w_k (since v̂_k ⊥ w_k).

So: s_k = -(c_k/(2|k|²)) [(q_k·k)w_k + (q_k·w_k)k]

The s_k is proportional to |q_k| — the PERPENDICULAR component of ê
relative to mode k's polarization.

## Bounding |s_k|

|s_k| ≤ (|c_k|/(2|k|²)) [|q_k·k|×|w_k| + |q_k·w_k|×|k|]

Since w_k = k × v̂_k: |w_k| = |k| (because v̂_k ⊥ k, both unit-ish).
Actually |w_k| = |k||v̂_k|sin(angle) = |k| (since v̂_k ⊥ k → sin=1).

And q_k is in the plane spanned by k̂ and ŵ_k (both ⊥ v̂_k).
So: |q_k·k̂| ≤ |q_k| and |q_k·ŵ_k| ≤ |q_k|.

|s_k| ≤ (|c_k|/(2|k|²)) × |q_k| × [|k|² + |k|²] = |c_k||q_k|

Wait, let me be more careful:
|s_k| ≤ |c_k|/(2|k|²) × [|q_k||k| × |k| + |q_k||k| × |k|]
       = |c_k||q_k| × |k|²/(|k|²) = |c_k||q_k|

So: |s_k| ≤ |c_k| × |q_k| where |q_k| = sin(angle(ê, v̂_k)).

## S²ê = |Σ s_k|² ≤ (Σ|s_k|)² ≤ (Σ|c_k||q_k|)²

By Cauchy-Schwarz:
(Σ|c_k||q_k|)² ≤ (Σc_k²)(Σq_k²)

And |ω|² = |Σ a_k v̂_k c_k|².

## The Key Bound

Σc_k² = Σcos²(k·x*) (sum of squared phases at x*).
Σq_k² = Σsin²(angle(ê, v̂_k)) = N - Σp_k² = N - Σcos²(angle(ê, v̂_k)).

And |ω|² = |Σa_k v̂_k c_k|² ≥ ... depends on the alignment of v̂_k.

For EQUAL amplitudes (a_k = 1) and v̂_k all parallel (worst case for S²ê):
|ω| = Σ|c_k|. And Σq_k² = 0 (all ê = v̂_k). So S²ê = 0. Too easy.

For perpendicular v̂_k: |ω|² = Σc_k² (no cross-terms in ω). And Σq_k² ≈ N-1.
S²ê ≤ Σc_k² × (N-1) = |ω|² × (N-1).

Hmm, that gives S²ê/|ω|² ≤ N-1 which GROWS with N. Wrong direction!

The Cauchy-Schwarz bound is too LOOSE. The actual S²ê is much smaller
because the s_k vectors have different DIRECTIONS (not all parallel).

## The Vector Cancellation

S²ê = |Σ s_k|² = Σ|s_k|² + 2Σ_{j<k} s_j · s_k.

The cross-terms s_j · s_k involve the DOT PRODUCT of two mode contributions.
For random mode directions: s_j · s_k averages to zero.
For coherent modes: could be positive.

The cancellation comes from the STRAIN structure: s_k involves (q_k·k̂)w_k + (q_k·ŵ_k)k.
Different modes have different k and w, so the s_k point in different directions.
The coherence is limited by the angular spread of the k vectors.

## STATUS

The Cauchy-Schwarz bound on scalar sums (Σ|s_k|) is too loose.
The VECTOR cancellation in Σs_k is what keeps S²ê small.
Proving this cancellation requires understanding the angular distribution
of the s_k vectors, which depends on the k-vector geometry on Z³.

The per-mode bound |s_k| ≤ |c_k||q_k| is tight.
The SUMMATION bound |Σs_k|² << (Σ|s_k|)² is where the margin comes from.
This is a VECTOR CANCELLATION problem.

## A BETTER APPROACH

Instead of bounding |Σs_k|: bound Σ|s_k|² directly.

|s_k|² ≤ c_k² q_k².

Σ|s_k|² ≤ Σc_k² q_k².

At the max: Σa_k c_k p_k = |ω| (the parallel components add up to |ω|).
And: Σa_k c_k v̂_k = |ω|ê → parallel: Σa_k c_k p_k = |ω|, perp: Σa_k c_k q_k = 0.

The ZERO-SUM constraint on perpendicular: Σa_k c_k q_k = 0.
This means the perpendicular vorticity components CANCEL at x*.

Each s_k is proportional to q_k (the perpendicular component).
The q_k satisfy Σa_k c_k q_k = 0 (zero sum, weighted by a_k c_k).

For vectors with a weighted zero-sum constraint: the norm |Σs_k|²
is bounded by the variance of the s_k (not the sum of magnitudes).

## THE VARIANCE BOUND

From Σa_k c_k q_k = 0 and q_k in 2D (⊥ê plane):

The s_k are functions of q_k. With the zero-sum constraint:
|Σs_k|² ≤ (Σ|s_k|²) × (1 - (Σ|s_k|w_k)² / (Σ|s_k|²)(Σw_k²))

where w_k = a_k c_k / Σa_k c_k (the weights in the zero-sum).

This is related to the Bessel inequality for the projection onto
the constraint direction.

## TOO COMPLICATED

This analysis is getting unwieldy. Let me try a CLEANER approach.

## THE CLEAN BOUND: |S·ê|² ≤ |∇ω|² - |ω·∇ê|² ... no.

Actually: S = (∇u+∇u^T)/2. And u = BS(ω). On T³: û = i(k×ω̂)/|k|².

|S·ê|² = ê_j S_{ji} S_{ik} ê_k. This is a quadratic form in S.

From the spectral decomposition: S²ê = Σλ_i²c_i where c_i = (ê·e_i)².

We need: Σλ_i²c_i < (3/4)|ω|².

At the attractor |S|² = Σλ_i² = |ω|²/4: S²ê ≤ |S|² = |ω|²/4 < 3|ω|²/4. ✓

WAIT — |S|² = |ω|²/4 gives S²ê ≤ |ω|²/4 < 3|ω|²/4 TRIVIALLY!

If the attractor holds: S²ê ≤ |S|² = |ω|²/4 = 0.25|ω|² < 0.75|ω|². ✓

The margin: 0.75 - 0.25 = 0.50 (67% margin). MATCHES the Monte Carlo!

## THE ATTRACTOR GIVES THE BOUND

IF |S|² ≤ |ω|²/4 at the max: THEN S²ê ≤ |S|² ≤ |ω|²/4 < 3|ω|²/4. ✓

We don't need a bound on S²ê specifically. We need |S|² ≤ |ω|²/4.
Which is the ATTRACTOR (files 161, 299).

BUT: we're going in circles. The attractor is what Instance A flagged
as unproven (file 300). S²ê < 3|ω|²/4 follows from |S|² < |ω|²/2.
And |S|² < |ω|²/2 is the attractor condition.

HOWEVER: the threshold for S²ê is 3/4 (not 1/4). So even |S|² = |ω|²/2
(NOT at the attractor) gives S²ê ≤ |ω|²/2 < 3|ω|²/4. ✓

WE ONLY NEED |S|² < 3|ω|²/4. This is MUCH weaker than the attractor!

|S|² < 3|ω|²/4 ↔ |ω|²/|S|² > 4/3.

The attractor gives |ω|²/|S|² = 4. We only need > 4/3!

Can we prove |S|² < 3|ω|²/4 at the max?

## 333. The S²ê bound follows from |S|² < 3|ω|²/4 (weaker than attractor).
## Need: |ω|²/|S|² > 4/3 at the max. The attractor gives 4. Margin 3×.
