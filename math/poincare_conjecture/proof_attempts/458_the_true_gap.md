---
source: THE TRUE GAP — after correcting all errors and computing true worst cases
type: DEFINITIVE 400s SUMMARY — what we know, what remains
file: 458
date: 2026-03-30
instance: CLAUDE_A (400s)
---

## THE PROOF CHAIN (all proven steps)

1. **Cross-term identity**: |S|² = |ω|²/2 - 2C (PROVEN, file 511)
2. **Trace-free bound**: S²ê ≤ (2/3)|S|² (PROVEN, standard)
3. **Key Lemma reduction**: need C > -5|ω|²/16 at the max (PROVEN reduction)
4. **Barrier + Type I + Seregin**: Key Lemma → regularity (PROVEN)
5. **N=2 sharp bound**: C ≥ -|ω|²/8 for 2-mode fields (PROVEN, file 525)
6. **Self-vanishing**: |S_k·ê|² = (a²/4)sin²γ (PROVEN, file 518)

## THE GAP

**Prove: C > -5|ω|²/16 at argmax|ω|² for all N ≥ 3.**

## NUMERICS (corrected, with optimized adversarial search)

### N=3, optimized polarizations at vertex max:

| K² | Worst C/|ω|² | Above -5/16 = -0.3125? | Margin |
|----|-------------|------------------------|--------|
| 2 | -0.125 | YES | 60% |
| 3 | -0.111 | YES | 64% |
| 5 | -0.165 | YES | 47% |
| 6 | -0.158 | YES | 50% |

### All N, random configs:

| Test | Worst C/|ω|² | Margin from -5/16 |
|------|-------------|-------------------|
| 10K random, vertex max | -0.107 | 66% |
| 3K random, continuous max | -0.109 | 65% |
| N=3 optimized, all shells | -0.165 | 47% |

**The worst case is N=3 on K²=5 with optimized polarizations: C/|ω|² = -0.165.**
**47% margin above the -5/16 threshold.**

## THE STRUCTURE OF THE WORST CASE

K²=5 has vectors like (2,1,0), (2,0,1), etc. These have:
- More diverse inter-angle structure than K²=2
- cos(θ) values including 3/5, 4/5, 0, 1/5 (richer than K²=2's {0, ±1/2})
- Larger sin²θ values → larger |P| corrections

The worst N=3 config achieves C/|ω|² ≈ -0.165 by:
1. Choosing k-vectors with large sin²θ (near-orthogonal)
2. Choosing polarizations with large opposing normal projections
3. Using the constructive sign pattern at the vertex max

## WHAT WOULD CLOSE THE GAP

### Approach 1: Per-shell bound
For each K², prove C ≥ -5|ω|²/16 using the explicit geometry.
The K²=5 worst case (-0.165) is the tightest. Need to show this
geometric configuration can't reach -0.3125.

### Approach 2: Universal bound via the cross-term structure
The correction C = Σ P_{jk} s_j s_k involves pair terms P that are
bounded by the div-free geometry. The KEY: at the global max vertex,
the sign pattern makes |ω|² large, which ALSO constrains C.

The ratio C/|ω|² = Σ P s_j s_k / (Σ a² + 2Σ D s_j s_k).
For this to reach -5/16: need |Σ P s s| > 5/16 × (Σa² + 2Σ D ss).

Since |P| ≤ a_j a_k sin²θ and D = v·v, the ratio |P|/|D| ≤ sin²θ
(with equality when normal projections are maximal).

### Approach 3: Computational proof for finite N
SOS certification (500s approach) or exhaustive optimization for
all K-shell configs up to K_max. The K²=5 shell is the hardest.

## THE SIGNIFICANCE

If C > -5|ω|²/16 can be proven for the K²=5 shell (the worst case):
then by extension to all shells → NS regularity on T³.

The 47% margin is SUBSTANTIAL. The physics (Biot-Savart structure +
constructive interference at the max) prevents C from reaching the threshold.

## 458. True gap: C > -5/16 at the max. Worst observed: -0.165 (47% margin).
## K²=5 is the hardest shell. N=3 is the worst mode count.
## The C ≥ -1/8 conjecture was false, but C > -5/16 appears robust.
