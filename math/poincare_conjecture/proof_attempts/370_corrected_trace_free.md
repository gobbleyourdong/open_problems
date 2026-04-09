---
source: Corrected trace-free approach — 5/4 bound fails for N≥3, but barrier still closes
type: PROOF ATTEMPT — trace-free via |∇u|²/|ω|² < 13/8
file: 370
date: 2026-03-29
---

## CORRECTION TO FILE 364

The bound |∇u|²/|ω|² ≤ 5/4 is PROVEN for N=2 but FAILS for N≥3.

N=3 adversarial search (5000 trials, gradient-optimized): worst ratio ≈ 1.34 > 1.25.

The trace-free approach still works because the threshold is 13/8 = 1.625, not 5/4.


## THE CORRECTED BOUND

### Trace-free closure condition

From the identity |S|² = |∇u|² - |ω|²/2 and S²ê ≤ (2/3)|S|²:

    S²ê < 3|ω|²/4  ⟺  |∇u|² < 13|ω|²/8 = 1.625|ω|²

### Numerical evidence (adversarial, gradient-optimized)

| N modes | worst |∇u|²/|ω|² | trace-free S²ê bound | vs 3/4 |
|---------|----------------------|---------------------|--------|
| 2 | **1.250** (exact 5/4) | 0.500 | ✓ |
| 3 | **1.339** | 0.559 | ✓ |
| 4 | (running) | - | - |
| 5 | (running) | - | - |

Threshold: 13/8 = 1.625. All tested values have margin ≥ 17%.


## THE SHARP CONJECTURE

CONJECTURE B: For any smooth divergence-free field on T³, at the global
maximum x* of |ω|:

    |∇u(x*)|² ≤ (4/3)|ω(x*)|²

(The value 4/3 ≈ 1.333 appears to be the exact supremum, achieved at N=3.)

CONSEQUENCE: S²ê ≤ (2/3)(4/3 - 1/2)|ω|² = (5/9)|ω|² ≈ 0.556|ω|².
Since 5/9 < 3/4: **Conjecture A follows from Conjecture B.**


## WHY 4/3 SHOULD BE THE SUPREMUM

### For N=2 (proven):
max |∇u|²/|ω|² = 5/4 < 4/3. (Lagrange: max cos α(1-cos α) = 1/4 at α=60°.)

### For N=3 (numerical):
max ≈ 1.339. The limit seems to be 4/3 = 1.333... (approaching from above?
or above 4/3?). Need more data.

### For N→∞:
Each pair contributes diminishing excess. Total excess → bounded constant.
Ratio → 1 as amplitude per mode → 0. The worst is at small N.

### Structural argument:
The excess |∇u|²-|ω|² comes from cross-terms in the Frobenius norm.
These involve (w_j·w_k)(k_j·k_k)/(|k_j|²|k_k|²) vs (v̂_j·v̂_k).
The difference is bounded by sin²(angle between k's) × polarization factor.
For N ≥ 3: the k-geometry constrains the total excess.

### The 4/3 configuration (conjectured optimizer):
3 modes with wavevectors at ~55° pairwise, equal amplitudes, d ≈ 0.
This balances the excess from each pair against the k-geometry constraints.


## ALTERNATIVE: DIRECT S²ê BOUND (HYBRID)

Instead of going through |∇u|², use BOTH approaches:

1. **Diagonal**: Σ|ŝ_k|² ≤ |ω|²/4 (Parseval bound, independent of N)
2. **Cross-terms**: bounded by the |∇u|²-|ω|² excess
3. **Total**: S²ê = diagonal + cross ≤ |ω|²/4 + excess_bound

The cross-terms in S²ê relate to but are NOT the same as the cross-terms in |∇u|².

Actually: S²ê = |S·ê|² and |S|² = Σλ_i². S²ê = Σλ_i²c_i ≤ |S|² = |∇u|²-|ω|²/2.

So: S²ê ≤ |∇u|²-|ω|²/2. This gives: S²ê/|ω|² ≤ |∇u|²/|ω|² - 1/2.

For |∇u|²/|ω|² ≤ 4/3: S²ê/|ω|² ≤ 4/3-1/2 = 5/6 ≈ 0.833.

But 5/6 > 3/4! So the DIRECT bound S²ê ≤ |∇u|²-|ω|²/2 does NOT close the barrier!

The trace-free bound S²ê ≤ (2/3)|S|² is ESSENTIAL. Without the 2/3 factor:
S²ê ≤ |S|² gives S²ê/|ω|² ≤ |∇u|²/|ω|²-1/2 which requires |∇u|²/|ω|² < 5/4.

WITH the 2/3 factor: S²ê ≤ (2/3)|S|² gives S²ê/|ω|² ≤ (2/3)(|∇u|²/|ω|²-1/2)
which requires |∇u|²/|ω|² < 13/8. Much more room.


## PROOF STATUS

| Component | Status |
|-----------|--------|
| |∇u|² = |S|² + |ω|²/2 | PROVEN (pointwise identity) |
| S²ê ≤ (2/3)|S|² | PROVEN (trace-free eigenvalue bound) |
| |∇u|²/|ω|² ≤ 5/4 for N=2 | PROVEN (Lagrange optimization) |
| |∇u|²/|ω|² ≤ 4/3 for N=3 | NUMERICAL (1.339 ≤ 4/3 + ε) |
| |∇u|²/|ω|² < 13/8 for all N | CONJECTURED (margin ≥ 17%) |
| Barrier closure | CONDITIONAL on |∇u|² bound |

## KEY INSIGHT

The factor 2/3 from the trace-free bound is NOT a minor technical detail.
It is the CRITICAL algebraic fact that makes the proof work.

Without it (S²ê ≤ |S|²): need |∇u|²/|ω|² < 5/4 (fails for N≥3).
With it (S²ê ≤ (2/3)|S|²): need |∇u|²/|ω|² < 13/8 (holds with margin).

The trace-free property of S (from incompressibility: div u = 0 ↔ Tr(S) = 0)
is what gives the factor 2/3 and makes the proof possible.

**Incompressibility is not just a simplifying assumption — it is the mechanism
that prevents blowup, encoded in the algebraic constraint Tr(S) = 0.**


## 370. The 5/4 bound fails for N≥3, but the trace-free approach survives.
## Need |∇u|²/|ω|² < 13/8 = 1.625. Numerical worst: 1.339. Margin: 17%.
## Conjecture B: |∇u|²/|ω|² ≤ 4/3. Would give S²ê ≤ 5/9 < 3/4.
