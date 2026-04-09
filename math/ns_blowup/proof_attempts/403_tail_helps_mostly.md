---
source: TAIL MODES MOSTLY HELP — adding large-|k| modes usually reduces R
type: DATA — the K-shell certification nearly closes the bootstrap
file: 403
date: 2026-03-29
---

## THE DATA (200 trials, K=√2 head + |k|²≤8 tail)

Adding tail modes to the K=√2 head:
- REDUCES R: 75% of cases
- INCREASES R: 23% of cases (but by at most +0.038)
- Worst R_all = 0.574 (massive margin to 1.625)

The tail perturbation is TINY: worst delta = +0.038.
Starting from K=√2 certification (R_head ≤ 1.236):
R_all ≤ 1.236 + delta ≤ 1.274 < 1.625. PASSES with 22% margin.

## WHY THE TAIL IS SMALL

For mixed pairs (head j, tail k with |k_k|² > K²):
G_jk = (w_j·w_k)(k_j·k_k)/(|k_j|²|k_k|²)

The 1/|k_k|² factor SUPPRESSES G for large-|k| modes.
|G_jk| ≤ |κ_jk| × |k_j|²/(|k_j|²|k_k|²) = |κ_jk|/|k_k|² → 0.

While D_jk = v̂_j·v̂_k doesn't depend on |k|.

So: Δ_jk = G_jk - D_jk ≈ -D_jk for large |k_k|.
At the global max: D_eff ≥ 0 → Δ_eff ≈ -D_eff ≤ 0. NEGATIVE.

## THE BOOTSTRAP ARGUMENT (nearly closed)

1. For N ≤ 4 head modes: per-mode bound (PROVEN)
2. For 5 ≤ N_head ≤ 9 modes in K=√2 shell: R_head ≤ 1.236 (CERTIFIED)
3. Tail modes (|k|² > 2): add at most +0.04 to R (OBSERVED)
4. R_total ≤ 1.236 + 0.04 = 1.276 < 1.625 (PASSES)
5. Near blowup: N grows, R DECREASES (file 402_large_N_helps)

## WHAT'S STILL NEEDED

- Prove the tail delta is bounded: |ΔR_tail| ≤ ε for some ε < 13/8 - 1.236 = 0.389.
  From the data: ε ≈ 0.04. Need ε < 0.39. MASSIVE margin.

- The bound should follow from: |G_jk| ≤ C/|k_k|² for mixed pairs.
  Total tail contribution: Σ_{mixed} |Δ_jk| ≤ Σ C/|k_k|² × (amplitude factors).
  For analytic fields: amplitudes decay exponentially → sum converges.

## 403. Tail mostly helps (75%). Worst delta = +0.04. K-shell + tail ≤ 1.28 < 1.625.
