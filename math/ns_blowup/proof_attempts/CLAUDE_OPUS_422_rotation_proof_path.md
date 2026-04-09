---
source: THE ROTATION PROOF PATH — N-3 free azimuthal angles prevent alignment
type: PROOF DIRECTION — the deepest insight, may close the Key Lemma
file: 422
date: 2026-03-30
---

## THE ALGEBRAIC STRUCTURE

For each mode k with wavevector k̂_k and vorticity direction ê:

The polarization v̂_k ⊥ k̂_k has ONE free parameter: the azimuthal angle θ_k.

As θ_k varies:
- cos γ_k = v̂_k · ê changes (determines the parallel projection p_k)
- The strain direction φ_k = arctan(B_k/A_k) rotates through [0°, 360°)

Crucially: A_k = cos(θ_k)(e₂·ê) - sin(θ_k)(e₁·ê) is sinusoidal in θ_k.
While B_k = k̂_k · ê is INDEPENDENT of θ_k.

## THE GLOBAL MAX CONSTRAINT

At the global max: the θ_k are chosen to maximize |ω|².

|ω| = |Σ a_k s_k v̂_k(θ_k)| where s_k = ±1 (sign pattern).

This optimization fixes:
- The sign pattern s_k (from the vertex maximization)
- The cos γ_k values (from the global max condition on p_k = a_k cos γ_k)

But it does NOT fix φ_k (the strain direction within each mode's plane).

## THE PERPENDICULAR CONSTRAINT

Σ q_k = 0 (where q_k = a_k sin γ_k × azimuthal direction of v̂_k)

This is 3 equations (one per R³ component) constraining N azimuthal angles.

For N ≤ 3: all angles determined → φ_k can align → S²ê up to 1/3.
For N ≥ 4: N - 3 ≥ 1 FREE angles → φ_k diversify → S²ê decreases.

## THE COUNTING ARGUMENT

The s_k vectors in the sum S·ê = Σ s_k live in R³.
Each s_k is in a different 2D plane (the plane ⊥ v̂_k).
Its direction within that plane is φ_k.

For N modes: N direction angles φ_k.
Constraints: 3 from Σq_k = 0 + N from cos γ_k values.
FREE parameters: N angles θ_k - N cos γ_k constraints - 3 Σq_k constraints
= N - N - 3 = -3. OVER-CONSTRAINED?

Wait: cos γ_k and φ_k are BOTH functions of θ_k (the single angle per mode).
So there's only N free parameters total (the θ_k's).

The cos γ_k conditions: N equations.
The Σq_k = 0 condition: 3 equations (but q_k depends on θ_k too).

For the global max: the optimization over θ_k determines cos γ_k(θ_k).
This is one equation per mode: cos γ_k = prescribed value.
→ θ_k is determined up to ±1 sign (two values per mode).

Then Σq_k = 0 constrains some of the ± choices.

The remaining freedom: the ± choices that satisfy Σq_k = 0.
For N modes: 2^N sign choices, 3 constraints → ~2^{N-3} solutions.

Each solution gives DIFFERENT φ_k values. The max of S²ê over these
solutions is what matters. With 2^{N-3} options: the worst φ_k alignment
is limited.

## STATUS

This counting argument suggests S²ê is controlled for N ≥ 4 because
the perpendicular constraint Σq_k = 0 prevents full alignment of φ_k.

The formalization requires: showing that among all solutions to Σq_k = 0,
none achieves S²ê > |ω|²/4 (or 3|ω|²/4).

This is a FINITE-DIMENSIONAL optimization over discrete sign choices +
continuous azimuthal angles. Potentially computer-certifiable for each N.

## 422. The Biot-Savart rotation angle φ_k is UNIFORM (verified).
## This uniformity prevents constructive interference of s_k vectors.
## The counting argument: N-3 free angles for N ≥ 4 → S²ê bounded.
## Formalization: show Σq_k = 0 prevents φ_k alignment → Key Lemma.
