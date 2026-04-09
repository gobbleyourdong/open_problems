---
source: Analytical attempt to prove |ω|_max is bounded
approach: Single-mode orthogonality → strain misalignment at max point → BKM
status: IN PROGRESS — the bridge between Lemma 1 and regularity
---

## The Goal
Prove: for divergence-free fields on T³, |ω|_max(t) ≤ |ω|_max(0) for all t.
Combined with BKM: this gives global regularity.

## The Argument

### Setup
Let x* be the point where |ω(t)| achieves its maximum at time t.
At x*, the vorticity evolution is:

```
d/dt |ω|² = 2 ω_i S_ij ω_j - 2ν |∇ω|²    (at x*)
```

For |ω|_max to grow: ω·S·ω > ν|∇ω|² at x*.
For |ω|_max to be bounded: ω·S·ω ≤ ν|∇ω|² at x*.

### The strain at x* decomposes by Fourier mode

```
S_ij(x*) = Σ_k Ŝ_ij(k) e^{ikx*}
```

Each Fourier mode k contributes to the strain via Biot-Savart:
```
Ŝ_ij(k) = i(k_i û_j(k) + k_j û_i(k))/2
```
where û(k) = ik × ω̂(k) / |k|²

### Lemma 1 applied at x*

For each mode k, the Biot-Savart strain Ŝ(k) has eigenvectors
PERPENDICULAR to ω̂(k) (proven in file 014).

At x*, the vorticity direction is ê = ω(x*)/|ω(x*)|.
The stretching contribution from mode k is:
```
ê · Ŝ(k) · ê = |Ŝ(k)| cos²(θ_k)
```
where θ_k is the angle between ê and the strain eigenvector of mode k.

### The alignment angle θ_k

Lemma 1 says: θ_k depends on the angle between ê (vorticity at x*)
and the strain eigenvector of mode k (which is perpendicular to ω̂(k)).

For the strain eigenvector of mode k to align with ê at x*:
- ê must be in the plane ⊥ to ω̂(k) at that mode
- This requires ê · ω̂(k) = 0

But ω̂(k) is the Fourier coefficient of vorticity, and ê is the
direction of the TOTAL vorticity at x*. The total vorticity is:
```
ω(x*) = Σ_k ω̂(k) e^{ikx*}
```

The direction ê = ω(x*)/|ω(x*)| is a WEIGHTED AVERAGE of ω̂(k) directions.

### The key inequality

For perfect stretching at x*: ê · Ŝ(k) · ê must be maximized for ALL k.
This requires ê ⊥ ω̂(k) for ALL k (so the strain eigenvector aligns with ê).

But ê is the sum of all ω̂(k) weighted by e^{ikx*}. It CANNOT be
perpendicular to all of its own components simultaneously (unless they
all cancel, which means ω(x*) = 0).

### Quantification

Decompose:
```
ω(x*) = Σ_k ω̂(k) e^{ikx*} = |ω(x*)| ê
```

The component of ω̂(k) along ê:
```
ω̂_∥(k) = (ω̂(k) · ê) ê    (parallel to ê)
ω̂_⊥(k) = ω̂(k) - ω̂_∥(k)  (perpendicular to ê)
```

By definition:
```
Σ_k ω̂_∥(k) e^{ikx*} = |ω(x*)| ê    (sums to the total)
Σ_k ω̂_⊥(k) e^{ikx*} = 0             (perpendicular parts cancel)
```

The parallel component ω̂_∥(k) controls the alignment:
- If ω̂_∥(k) is large: mode k's strain eigenvector is MISALIGNED with ê
  (because strain eigenvector ⊥ ω̂(k), and ω̂(k) has a large component along ê)
- If ω̂_∥(k) is small: mode k's strain eigenvector CAN align with ê

### The bound on total stretching

```
ω·S·ω at x* = Σ_k |ω|² |Ŝ(k)| cos²(θ_k)
```

The cos²(θ_k) depends on ω̂_∥(k):
```
cos²(θ_k) ≤ 1 - c|ω̂_∥(k)|² / |ω̂(k)|²
```
(modes with large parallel component have SMALLER alignment)

By Parseval-like identity:
```
Σ_k |ω̂_∥(k)|² |e^{ikx*}|² = |ω(x*)|²
```

This means the TOTAL parallel component is exactly |ω(x*)|².
The modes can't all have small ω̂_∥(k) because they sum to |ω(x*)|.

### The punchline

The stretching at x* is bounded:
```
ω·S·ω ≤ |ω|² Σ_k |Ŝ(k)| (1 - c|ω̂_∥(k)|²/|ω̂(k)|²)
       = |ω|² [Σ_k |Ŝ(k)| - c Σ_k |Ŝ(k)| |ω̂_∥(k)|²/|ω̂(k)|²]
```

The first term is the TOTAL strain magnitude (bounded by CZ: ||S||₁ ≤ C||ω||₁).
The second term is the DEPLETION due to parallel alignment.

For the maximum to grow, the first term must exceed ν|∇ω|² + the depletion.

The depletion is proportional to the average |ω̂_∥(k)|²/|ω̂(k)|² weighted
by |Ŝ(k)|. By the Parseval identity, this average is bounded below:
```
Σ_k |Ŝ(k)| |ω̂_∥(k)|²/|ω̂(k)|² ≥ ... (need to bound this)
```

## Where This Stands

The argument shows that:
1. Perfect stretching requires ê ⊥ ω̂(k) for all k (from Lemma 1)
2. This is impossible because ê is the sum of ω̂(k) (definition)
3. The DEPLETION from this impossibility reduces stretching
4. The reduction is proportional to the parallel component Σ|ω̂_∥|²

The gap: quantifying the depletion strongly enough to beat ν|∇ω|²
(or to show that the total strain minus depletion is bounded by |ω|²
times a constant < 1).

## What's Needed
- A lower bound on Σ_k |Ŝ(k)| |ω̂_∥(k)|²/|ω̂(k)|²
- This is the "depletion coefficient" — how much the orthogonality kills stretching
- If depletion coefficient > 0 uniformly → total stretching < total strain
- Combined with CZ bound ||S|| ≤ C||ω|| → growth rate bounded
- Growth rate bounded → |ω|_max bounded → BKM → regularity

## Status
The structure of the proof is clear. The gap is one inequality:
bounding the depletion coefficient from below. This is a geometric
property of the Biot-Savart operator — how much does the orthogonality
FORCE depletion at the maximum point?

If this coefficient is computable, the interval arithmetic library
can verify it rigorously. That would be the proof.
