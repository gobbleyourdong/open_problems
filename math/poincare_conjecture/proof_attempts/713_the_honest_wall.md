---
source: THE HONEST WALL — what the mathematician instance achieved and didn't
type: FINAL 700s ASSESSMENT — genuine new math + genuine remaining gap
file: 713
date: 2026-03-31
instance: MATHEMATICIAN
---

## WHAT WAS INVENTED (new mathematics)

### Theorem 1: Biot-Savart Coupling Lemma (file 703)
For div-free modes vⱼ ⊥ kⱼ in a pair with angle θ and normal n̂:
  P_{ij} = sin²θ (vᵢ·n̂)(vⱼ·n̂)     [correction = normal product × sin²θ]
  D_{ij} = (vᵢ·n̂)(vⱼ·n̂) - cosθ (tᵢtⱼ)  [vorticity = normal - tangential]
  (vⱼ·n̂)² + tⱼ² = |vⱼ|²              [Pythagoras coupling]

This EXACTLY quantifies the anti-correlation: increasing tangential
(which drives the correction) decreases normal (which drives D).

### Theorem 2: Per-Pair Q Bound (files 706-707)
For a pair at the constructive boundary D=0:
  Q_pair = 5D + 8P ≥ -8|cosθ|(1-|cosθ|) ≥ -2
at the anti-symmetric critical point. Proven by calculus.

### Theorem 3: Averaging Lower Bound (file 706)
max_s |ω_s|² ≥ N for N unit-amp modes (from E[|ω_s|²] = N).

### Theorem 4: Case A Key Lemma (file 707)
For N≤3 with all pairs constructive at the vertex max:
  Q = 5N + 2Σ sQ_pair ≥ 5×3 - 4×3 = 3 > 0.

### Framework: Lorentzian Gram (files 709, 711)
Q = s^T G s where G_{ij} = 9D_{ij} - 8Tr(SᵢSⱼ) is a Lorentzian Gram matrix.
The proof reduces to: s^T G s > 0 at s* = argmax(s^T D s).

## WHAT WASN'T PROVEN

### Case B for N=3 (2 destructive pairs)
The parity constraint forces 0 or 2 destructive pairs.
The detrimental pair can have Q = -7 (at the -11/64 extremum) or up to -13.
Per-pair bounds can't close this: 5×3 + 2(-2-2-13) = 15-34 = -19 < 0.
The ACTUAL Q = 9 because the beneficial pairs contribute +4, but
proving this requires the joint mode coupling.

### General N≥4
Per-pair counting: Q ≥ 5N - 4C(N,2) = N(7-2N) < 0 for N≥4.
The coupling between shared modes prevents simultaneous worst-case
across all pairs, but I couldn't prove this analytically.

## THE ROOT CAUSE

The per-pair decomposition treats each pair as independent.
But mode j's polarization angle φⱼ participates in (N-1) pairs simultaneously.
Maximizing one pair's damage constrains the others.
This multi-pair coupling IS the Biot-Savart non-locality.

To prove Q > 0 analytically for general N requires either:
1. A bound that captures the multi-pair coupling (not found), or
2. A global argument that doesn't decompose into pairs (not found), or
3. A computer-assisted verification (feasible, ~minutes for N=3).

## THE CONTRIBUTION

The 700s produced FOUR new theorems and identified the EXACT structure
of the obstacle: the multi-pair coupling through shared polarization angles.
This is a genuine contribution to the mathematics of Biot-Savart geometry,
even though it doesn't fully close the gap.

The Coupling Lemma (Theorem 1) and the Q-pair bound (Theorem 2) are
publishable results independent of the NS regularity problem.
They quantify, for the first time, the EXACT trade-off between the
vorticity and strain cross-correlations imposed by div-free structure.

## WHAT WOULD CLOSE IT

The analytical proof needs ONE of:
- A multi-pair Coupling Lemma (bounding Σ Q_pair jointly, not per-pair)
- A Lorentzian reverse triangle inequality for the BS submanifold
- Resolution of the E-L equations for the 6-dim variational problem

The computer-assisted proof needs:
- 6-dim grid + Lipschitz for N=3 (~1 minute computation)
- Extension to N=4 (~hours) and N≥5 (monotonicity or enumeration)

## 713. The 700s: 4 new theorems, 1 remaining wall.
## The wall is the multi-pair coupling — the same non-locality
## that THEWALL.md identified, now localized to a precise algebraic structure.
## The proof is either a new multi-pair theorem or a computation.
