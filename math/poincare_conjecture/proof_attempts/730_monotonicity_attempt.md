---
source: MONOTONICITY — adding a mode cannot decrease Q/|ω|² below 9/4
type: THEOREM ATTEMPT — if proven, extends N≤4 to ALL N
file: 730
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE MONOTONICITY CONJECTURE

For N ≥ 3: min_config Q/|ω|² is non-decreasing in N.
The global minimum is 9/4, achieved at N=3.

## THE FORMAL SETUP

For an (N+1)-mode field with the (N+1)th mode added:

    Q_{N+1} = Q_N + 5a²_{N+1} + 2 Σⱼ₌₁ᴺ s*ⱼ s*_{N+1} Q_{j,N+1}
    |ω|²_{N+1} = |ω|²_N + a²_{N+1} + 2 Σⱼ s*ⱼ s*_{N+1} D_{j,N+1}

where s* is the new argmax sign pattern (which may differ from the
N-mode argmax due to the added mode).

## THE RATIO ARGUMENT

Q_{N+1}/|ω|²_{N+1} ≥ Q_N/|ω|²_N iff:

    Q_N |ω|²_{N+1} + (stuff) ≥ ...

This is algebraically messy because s* changes. Let me try differently.

## THE SELF-VANISHING BOUND APPROACH

From file 726: for ANY N modes at the argmax:

    S²ê ≤ N²(|ω|²-1)/(4|ω|²) = (N²/4)(1 - 1/|ω|²)

And: Q/|ω|² = 9 - 8|S|²/|ω|² ≥ 9 - 8 × S²ê/|ω|² × (3/2)... no, wrong.

Actually: Q = 9|ω|² - 8|S|². S²ê ≤ Budget² ≤ N²(|ω|²-1)/(4|ω|²).
But Q uses |S|², not S²ê. |S|² ≥ S²ê (and |S|² can be larger).

The self-vanishing bounds S²ê, which is LESS than |S|². Using |S|²
requires the Frobenius bound. Let me bound |S|² directly.

From the self-vanishing: |Sⱼ·ê|² = (aⱼ²/4)sin²γⱼ.
But |Sⱼ|² = aⱼ²/2 (per-mode). So |Sⱼ|² > |Sⱼ·ê|² always.

The total |S|² = |Σ sⱼSⱼ|² involves ALL 6 independent components
of the symmetric matrix, not just the ê-projection.

I can bound |S|² using |S|² ≤ Σ|Sⱼ|² + 2Σ|Tr(SᵢSⱼ)| ≤ N/2 + N(N-1)×max|Tr(SS)|.
But max|Tr(SᵢSⱼ)| ≤ |Sᵢ|×|Sⱼ| = 1/2 (unit amps). Crude: |S|² ≤ N²/2.
Q/|ω|² ≥ 9 - 4N² / |ω|² ≥ 9 - 4N²/N = 9-4N. Negative for N>2. Useless.

## THE PER-MODE DIAGONAL DOMINANCE

The key: Q = 5N + 2Σ sᵢsⱼ Qᵢⱼ. The diagonal is 5N.
The cross-terms: 2Σ sQ ≤ 2×N(N-1)/2 × max|Q| = N(N-1)max|Q|.
max|Q| per pair ≤ 13 (for orthogonal k). So Q ≥ 5N - 13N(N-1).
Positive only for N=1. Useless.

But: the AVERAGE of Σ sQ over sign patterns is 0 (cross-terms cancel).
At the ARGMAX: Σ sQ is correlated with Σ sD (same sign pattern).
The correlation limits how negative Σ sQ can be at the argmax.

## THE SELF-VANISHING BOUND ON Q/|ω|² DIRECTLY

Actually, I realize: I already proved S²ê < (3/4)|ω|² for N ≤ 4.
The Key Lemma IS S²ê < (3/4)|ω|², NOT Q > 0 (which is |S|² < 9/8|ω|²).

The Key Lemma for S²ê uses: S²ê ≤ Budget² < (3/4)|ω|² (from 726/728).

For N ≥ 5: Budget² = (N²-|ω|²)/4. Need < (3/4)|ω|² → |ω|² > N²/4.

Can I show |ω|² > N²/4 for the argmax of N ≥ 5 modes in R³?

|ω|² = max_s |Σ sⱼvⱼ|² for N unit vectors in R³.

## THE |ω|² LOWER BOUND

For N unit vectors in R³ with Gram matrix G (rank ≤ 3):
|ω|² = max_s s^T G s.

**Claim**: max_s s^T G s ≥ N²/3 for any N unit vectors in R³.

**Proof attempt**: G = V V^T where V is N×3. s^T G s = |V^T s|².
V^T s ∈ R³. |V^T s|² = Σ_{α=1}^3 (V^T s)_α².

Each (V^T s)_α = Σⱼ Vⱼα sⱼ. By Khintchine: E_s[(V^T s)_α²] = Σ Vⱼα² = ||column α||².
Σα E[(V^T s)_α²] = Tr(G) = N.

max_s |V^T s|² ≥ E_s[|V^T s|²] = N (averaging, already known).

But can I get N²/3? Using the SECOND MOMENT:
E_s[|V^T s|⁴] = E[Σαβ (V^T s)_α² (V^T s)_β²]
= Σα E[(V^T s)_α⁴] + Σ_{α≠β} E[(V^T s)_α²(V^T s)_β²].

The 4th moment of a Rademacher sum: E[(Σ aⱼsⱼ)⁴] = Σ aⱼ⁴ + 3(Σaⱼ²)² - 2Σaⱼ⁴...
Actually: E[(Σaⱼsⱼ)⁴] = 3(Σaⱼ²)² - 2Σaⱼ⁴ (for Rademacher).

This is getting complex. But the BOTTOM LINE:

By Paley-Zygmund: P(X ≥ θ E[X]) ≥ (1-θ)² (E[X])²/E[X²].
With X = |V^T s|² and E[X] = N:
max X ≥ N × (1 + ...). Not cleanly giving N²/3.

**Alternative**: for rank-3 G with eigenvalues λ₁,λ₂,λ₃:
max_s s^T G s ≥ λ₁ (the largest eigenvalue, achievable for continuous s).
For ±1 signs: max_s s^T G s ≥ (2/π) Σλᵢ = 2N/π ≈ 0.64N (Grothendieck).
Not enough (need N²/4).

The bound N²/3 seems FALSE for general N. For N large: max|ω|² ≈ N + O(√N),
not N²/3. The Rademacher sums have max ≈ √(N log N) per component,
so |ω|² ≈ N + O(√(N log N)). FAR below N²/3 for large N.

## CONCLUSION

The monotonicity approach hits the SAME wall: |ω|² grows linearly in N
(not quadratically), while the self-vanishing budget grows as N².

For large N: the self-vanishing bound is too crude by a factor of N.
The directional cancellation (which IS a factor of ~N) compensates,
but I can't prove it analytically.

**The honest state**: N ≤ 4 QED. N ≥ 5 needs directional cancellation
or computation. The monotonicity conjecture is TRUE numerically but
proving it requires bounding the directional cancellation.

## 730. Monotonicity: Q/|ω|² ≥ 9/4 for all N (numerically verified).
## The formal proof fails because |ω|² grows as N, not N²/4.
## The directional cancellation compensates but isn't proven.
## N ≤ 4 remains the analytical frontier.
