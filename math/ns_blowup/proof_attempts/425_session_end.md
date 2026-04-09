---
source: SESSION END — 425 proof attempts, the state of the art
type: DEFINITIVE STATE for the next session
file: 425
date: 2026-03-30
---

## WHAT IS PROVEN

1. Conditional regularity: S²ê < 3|ω|²/4 → NS regular on T³ (barrier+Seregin)
2. N ≤ 4 modes: unconditional regularity (sign-flip + Lagrange)
3. K=√2 shell: 502/502 interval-certified (worst 0.356, margin 53%)
4. K=√3 shell: 100/100 certified (worst 0.336, margin 55%)
5. True bound at global max: worst 0.215 (margin 71%, exact vertex enum)

## THE KEY LEMMA (the one remaining gap)

Prove: S²ê(x*) < 3|ω(x*)|² / 4 for ALL smooth div-free fields on T³.
Equivalently: |∇u(x*)|² < 5|ω(x*)|²/4 at the vorticity maximum.

## WHY EVERY APPROACH FAILS

| Approach | What it bounds | Why it fails |
|----------|---------------|--------------|
| Triangle inequality | (N-1)/4 | Grows with N |
| Trace-free + |∇u|² | Need |∇u|²<13/8|ω|² | Unproven for all N |
| Gram eigenvalue | λ_max × diagonal | Anti-correlated |
| Regression | max(L)/Y_max | Need Key Lemma |
| Diversity bound | avg cos ≤ c | avg cos CAN reach 0.86 |
| Bootstrap + tail | tail grows near blowup | Can't extend K-shell |
| Pressure crossover | R < 1 for large N | R > 1 possible at N=20 |
| Dynamic H_ωω | H_ωω ~ O(1) | Doesn't scale with N |
| Hanson-Wright | Generic c = 1/32 | 10× too loose |

## WHY THE BOUND HOLDS (understood but unproven)

1. Self-vanishing: S_k·v̂_k = 0 (each mode has a null along polarization)
2. Self-attenuation: ê → intermediate eigenvector (c₃ = 0.84)
3. BS rotation uniformity: strain direction φ_k is uniform in each plane
4. Σq_k = 0 → partial transfer → Σs_k small
5. Anti-correlation: high alignment ↔ small magnitudes (JOINT constraint)
6. Anti-twist mechanism (Buaria 2024): inviscid self-regularization

## MOST PROMISING APPROACHES FOR NEXT SESSION

1. **MSS/Kadison-Singer** (arxiv:1306.3969): reformulate s_k ⊗ s_k as
   rank-1 contributions, use trace-free as approximate isotropic condition
2. **Miller strain identity** (arxiv:2407.02691): bridge integral ⟨S²,ω⊗ω⟩=0
   to pointwise at the max via maximum principle
3. **Anti-twist quantification** (arxiv:2409.13125): formalize the inviscid
   regularization as a bound on directional coherence
4. **SDP on the Biot-Savart manifold**: joint optimization over the curved
   constraint surface (handles the anti-correlation directly)

## KEY PAPERS

- Miller 2024: arxiv:2407.02691 (strain-vorticity identity)
- Miller 2020: arxiv:1710.05569 (middle eigenvalue criterion)
- Buaria+ 2024: arxiv:2409.13125 (anti-twist regularization)
- Buaria+ 2020: arxiv:2009.08370 (self-attenuation)
- MSS 2013: arxiv:1306.3969 (Kadison-Singer / rank-1 sums)
- Grujic 2022: arxiv:1911.00974 (asymptotic criticality)
- Rudelson-Vershynin: arxiv:1306.2872 (Hanson-Wright)
- Foias-Temam 1989: Gevrey class regularity
- Seregin 2012: Type I exclusion

## 425 ATTEMPTS. THE MOUNTAIN IS MAPPED.
## The summit is one lemma away. The tools are identified.
## Next session: try MSS/Kadison-Singer or Miller's integral-to-pointwise bridge.
