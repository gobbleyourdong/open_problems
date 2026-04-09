# Eigenvector Mechanism at Key Lemma Worst Cases

## Date: 2026-04-08, Odd Cycle 12

## Discovery: Three Distinct Mechanisms

### N=2: Pure Depletion
- cos(Sê, ê) = 0 — strain PERPENDICULAR to vorticity
- α = 0 — zero stretching rate
- S eigenvalues: {0.707, 0, -0.707}
- ê equidistributed between λ₁ and λ₃
- S²ê/|ω|² = (λ₁² + λ₃²)/2 / |ω|² = 0.5/2 = 1/4

### N=3: Compression Alignment
- cos(Sê, ê) = 1 — strain PARALLEL to vorticity (compressive)
- α = -1 — maximum compression rate
- S eigenvalues: {0.5, 0.5, -1.0} — DEGENERATE pair!
- ê aligned 100% with λ₃ = -1 (compressive eigenvector)
- S²ê/|ω|² = λ₃²/|ω|² = 1/3
- The degeneracy {0.5, 0.5} forces ê to the unique direction

### N=4: Distributed Depletion (Peak)
- cos(Sê, ê) = 0.05 — strain nearly perpendicular to vorticity
- α ≈ 0 — near-zero stretching
- S eigenvalues: {1.42, -0.07, -1.35}
- ê splits between λ₁ (46%) and λ₃ (53%)
- S²ê/|ω|² = 0.362 (GLOBAL PEAK)
- Larger eigenvalues than N=3 but more vorticity → still bounded

## Why N=4 is the Peak
1. N=4 modes create larger strain eigenvalues than N=3
2. But ê doesn't align with a single eigenvector (no degeneracy)
3. |ω|² = 5.2 (less constructive interference than ideal 8)
4. The balance: large strain / moderate vorticity → maximum ratio
5. For N≥5: vorticity grows faster than strain → ratio decreases
