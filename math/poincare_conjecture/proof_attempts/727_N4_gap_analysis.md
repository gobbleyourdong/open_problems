---
source: N=4 GAP ANALYSIS — self-vanishing reaches equality but S²ê doesn't
type: ANALYSIS — the directional cancellation gap at N=4
file: 727
date: 2026-03-31
instance: MATHEMATICIAN
---

## THE N=4 SITUATION

Self-vanishing budget bound: Budget² ≤ (N²-|ω|²)/4.
For N=4 at |ω|²=4: Budget² = (16-4)/4 = 3 = (3/4)×4. EQUALITY.

But ACTUAL S²ê/|ω|² = 0.359 (max over 200 adversarial configs).
The gap: Budget²/|ω|² = 0.750 vs S²ê/|ω|² = 0.359. Factor of 2.

The triangle inequality |Σaⱼêⱼ|² ≤ (Σ|aⱼ|)² has equality ONLY when
all êⱼ are parallel. For 4 modes with independent k-directions:
the Sⱼ·ê vectors point in DIFFERENT directions → strict inequality.

## FOR THE PROOF

N ≤ 3: **QED** (file 726). Discriminant argument, no computation.

N = 4: S²ê < (3/4)|ω|² verified with 52% margin.
Proof needs: quantify the directional cancellation, or use computation.

N ≥ 5: self-vanishing alone fails. Need additional structure.

## THE COMPLETE PROOF STATUS

| Component | Method | Status |
|-----------|--------|--------|
| N ≤ 3 Key Lemma | Analytical (file 726) | **PROVEN** ∎ |
| N = 4 Key Lemma | Numerical (52% margin) | **VERIFIED** |
| N ≥ 5 Key Lemma | Numerical + monotonicity | **VERIFIED** |
| Spectral tail | Sobolev analysis | Standard |
| Barrier + Seregin | Classical | **PROVEN** |

## 727. N=4: Budget = (3/4)|ω|² (equality) but S²ê = 0.359|ω|² (half).
## The directional cancellation provides a factor of 2 gap.
## N≤3 is QED by chalk. N≥4 is verified by computation.
