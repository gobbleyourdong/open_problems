---
source: THE NEGATIVE CORRELATION — D and Δ anti-correlate by structure
type: KEY INSIGHT — the algebraic reason the global max protects
file: 379
date: 2026-03-29
---

## THE ALGEBRAIC IDENTITY

For each pair (j,k): G_{jk} = D_{jk} + Δ_{jk} (tautology).

G = (w_j·w_k)(k_j·k_k)/(|k_j|²|k_k|²) (gradient cross-term, FIXED by geometry)
D = v̂_j·v̂_k (vorticity cross-term, FIXED by geometry)
Δ = G - D (excess per pair)

At a vertex with signs s_k:
|ω|² = N + 2Σs_js_k D_{jk}
|∇u|² = N + 2Σs_js_k G_{jk} = |ω|² + 2Σs_js_k Δ_{jk}

## THE STRUCTURAL CONSTRAINT

Using BAC-CAB: G_{jk} = κ²D_{jk} - κA_{jk}B_{jk}

where κ = k̂_j·k̂_k, A = k̂_j·v̂_k, B = k̂_k·v̂_j.

So: **Δ_{jk} = (κ²-1)D_{jk} - κA_{jk}B_{jk} = -(1-κ²)D_{jk} - κAB**

KEY: Δ has a NEGATIVE D-proportional term: -(1-κ²)D.

At the GLOBAL MAX vertex s*: each s*_js*_k D_{jk} ≥ 0 (signs chosen for max |ω|²).
So: s*_js*_k Δ_{jk} = -(1-κ²)s*_js*_k D_{jk} - κs*_js*_k AB
                     = -(1-κ²)|D_eff| - κ(s*_js*_k AB)

The first term is ALWAYS ≤ 0 (negative contribution to excess!).
The second term has indefinite sign (can be + or -).

## EXCESS DECOMPOSITION

EXCESS(s*) = 2Σ_{j<k} s*_js*_k Δ_{jk}
= -2Σ(1-κ²)|D_eff| - 2Σκ(s*_js*_k AB)

= **NEGATIVE TERM** + **MIXED TERM**

The negative term: -2Σ(1-κ²_{jk})|D_{jk}|_{eff} ≤ 0 (always non-positive).

The mixed term: -2Σκ_{jk}(s*_js*_k A_{jk}B_{jk}) (can be + or -).

For the ratio: R = 1 + EXCESS/|ω|² = 1 + (negative + mixed)/|ω|².

If the mixed term is small relative to |ω|²: R < 1 + 0 = 1 < 5/4. DONE.

## BOUNDING THE MIXED TERM

|mixed| = |2Σκ(s*AB)| ≤ 2Σ|κ||A||B| ≤ 2Σ|κ| (since |A|,|B| ≤ 1).

And |ω|² = N + 2Σ|D_eff| (at the global max).

For the ratio: R ≤ 1 + 2Σ|κ|/|ω|² (using negative term ≤ 0).

**R ≤ 1 + 2Σ|κ_{jk}| / |ω|²**

## FOR WHICH N DOES THIS CLOSE?

Need: 2Σ|κ| / |ω|² ≤ 1/4 for R ≤ 5/4.

|ω|² ≥ N (average over sign patterns). So need 2Σ|κ|/N ≤ 1/4 → Σ|κ| ≤ N/8.

For unit k-vectors: κ_{jk} = k̂_j·k̂_k. For N(N-1)/2 pairs:
avg |κ| ≈ 1/2 (for random directions in R³). So Σ|κ| ≈ N(N-1)/4.

Need N(N-1)/4 ≤ N/8 → (N-1)/4 ≤ 1/8 → N ≤ 3/2. Only N=1!

The bound Σ|κ|/|ω|² is too loose for general N because the mixed term
is bounded by the TOTAL |κ| not by the ALIGNED subset.

## TIGHTER: USE THE CONSTRAINT ON AB

A = k̂_j·v̂_k and B = k̂_k·v̂_j. The div-free condition gives v̂·k̂ = 0,
so A_jj = B_kk = 0 (self-terms vanish).

For each pair: |A| ≤ |sin(angle(k_j, v̂_k))| and |B| ≤ |sin(angle(k_k, v̂_j))|.

At the Lagrange optimum with all modes at γ* to ê: A and B depend on
the relative orientation of the k-vector pairs.

For modes with k perpendicular to v (div-free): the angles are constrained.
The product AB is bounded by the pairwise k-geometry.

## WHAT THE NUMERICS SHOW

For the N=5 Lagrange config on the lattice:
- Correlation(D_sum, EXCESS) = -0.577 across all vertices
- At global max: EXCESS = 1.38, |ω|² = 8.64. Ratio = 1.16.
- Negative term = -2Σ(1-κ²)|D_eff| (strongly negative for pairs with κ small)
- Mixed term partially cancels the negative term

The net effect: EXCESS/|ω|² ≈ 0.16, far below 1/4.

## PROOF STATUS

The algebraic decomposition EXCESS = negative + mixed shows:
1. The negative term ALWAYS helps (reduces ratio)
2. The mixed term is the only threat
3. The mixed term is bounded by 2Σ|κ| (k-geometry dependent)
4. For practical configs: the mixed term is partially canceled by the negative term

For a RIGOROUS proof: need to bound the mixed term at the GLOBAL MAX.
This requires understanding how the max-|ω|² sign pattern affects the AB terms.

The most promising route: show that at the global max, the modes with
large |D_eff| (contributing to |ω|²) also have large |1-κ²| (making the
negative term dominate), while modes with large |κAB| (the mixed threat)
have small |D_eff| (not contributing to |ω|²).

## 379. EXCESS = -(1-κ²)D_eff - κAB. First term always negative.
## The negative correlation is STRUCTURAL: maximizing D minimizes Δ.
## Mixed term κAB is the remaining challenge. Bounded by 2Σ|κ|.
