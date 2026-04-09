---
source: Signed kernel spectral analysis — additional cancellation from complex phases
type: FINDING — signed kernel has 62% less spectral mass than positive kernel
status: PROMISING — ratio decreases with N_j but limited data
date: 2026-03-26
---

## Signed vs Positive Kernel

The Schur test uses the POSITIVE kernel |M(k̂,k̂')| = cos(α/2)/2.
The actual bilinear form uses the SIGNED matrix-valued kernel
(2×2 blocks with phases that depend on relative orientation).

### Spectral Analysis

| N_j | ||F_positive||_op | ||M_signed||_op | Ratio | θ_signed |
|-----|-------------------|-----------------|-------|----------|
| 92 | 30.5 | 15.4 | 0.506 | 0.335 |
| 98 | 32.6 | 13.8 | 0.422 | 0.281 |
| 224 | 74.6 | 28.6 | 0.382 | 0.255 |

The ratio DECREASES with N_j (more modes → more sign cancellation).

### Positive Kernel Structure

The positive kernel f(α) = cos(α/2)/2 on S² has:
- λ_0 = 74.6 (66.6% of trace) — l=0 harmonic, nearly constant eigenvector
- λ_1 = λ_2 = λ_3 = 15.0 (20% each) — l=1 harmonics
- λ_4+ < 1 (higher harmonics negligible)

The kernel is approximately RANK 4 (l=0 and l=1 harmonics).

### Signed Kernel Structure

The signed kernel (2N×2N) has:
- Spectral norm = 28.6 (38% of positive kernel)
- Frobenius/spectral = 3.8 (effective rank ~14)
- Top 10 eigenvalues spread from 21 to 29 (no single dominant mode)

The signed kernel is MUCH more spread out than the positive kernel.
The div-free constraint + complex phases destroy the rank-1 dominance.

### Why the Signed Kernel is Better

1. The positive kernel is rank-1 dominated (l=0 harmonic).
   The l=0 mode corresponds to a UNIFORM ω̂ — all modes in the same direction.
   But div-free requires ω̂(k) ⊥ k, so different k's have ω̂ in different planes.
   The div-free constraint is approximately ORTHOGONAL to the top eigenvector.

2. The signed kernel includes the PHASE structure:
   The 2×2 blocks have entries that oscillate with the relative orientation.
   The oscillation creates cancellation in the eigenvalues.
   The effective spectral radius is reduced by ~60%.

### Scaling Question

If the ratio decreases as N_j^{-α}:
- α = 0.32 from fit (3 data points, unreliable)
- θ_signed ~ N_j^{-0.32} × (2/3) × (N_j^{-1}) ≈ N_j^{-1.32}

Since N_j ~ 2^{2j}, this gives θ ~ 2^{-2.64j} — very fast decay!

But we cannot reliably determine the exponent from only 3 data points
at small N_j. The asymptotic scaling might be different.

### Connection to Proof

If the signed kernel's spectral norm grows as N_j^β with β < 1:
- Positive kernel: ||F||_op ~ N_j (β = 1)
- Signed kernel: ||M||_op ~ N_j^β with β < 1

Then θ_signed ~ N_j^{β-1} ~ N_j^{-(1-β)} which DECREASES with N_j.
In terms of shells: θ(j) ~ 2^{-2(1-β)j}.

For β = 0.68 (our estimate): θ ~ 2^{-0.64j}

The shell ODE critical threshold is 2^{-j} (β ≤ 0.5).
Our estimate β ≈ 0.68 gives 2^{-0.64j}, which is MARGINAL
(between the safe and unsafe regimes in the ODE model).

### What's Needed

1. More data: compute ||M_signed|| at larger N_j (1000+ modes)
2. Better: PROVE that ||M_signed|| ~ N_j^β with β < 1
3. Best: PROVE β ≤ 0.5, which gives θ ~ 2^{-j} → regularity

The key technique: exploit the fact that the signed kernel's top
eigenspace is approximately ORTHOGONAL to div-free fields.
The l=0 harmonic (constant ω̂ direction) is killed by div-free.
If the l=1 harmonics are also partially killed, β < 1 follows.

## 116 proof files. The signed kernel is significantly better than positive.
