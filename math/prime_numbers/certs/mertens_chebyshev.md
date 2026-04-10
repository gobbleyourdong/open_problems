# Mertens Function and Chebyshev ψ — Verified to N = 10⁷

## Date: 2026-04-09

## Mertens function M(x) = Σ_{n ≤ x} μ(n)

| x | M(x) | |M(x)|/√x |
|---|------|----------|
| 100 | +1 | 0.10 |
| 1,000 | +2 | 0.06 |
| 10,000 | -23 | 0.23 |
| 100,000 | -48 | 0.15 |
| 1,000,000 | +212 | 0.21 |
| 10,000,000 | +1,037 | 0.33 |

### Distribution of |M(x)|/√x in [10, 10⁷]
- Maximum: **0.832** at x = 13 (small-x volatility)
- 99th percentile: **0.367**
- 95th percentile: **0.314**
- 50th percentile: **0.121**
- Sign flips: **15,292** in [1, 10⁷]

### Mertens conjecture (1897)
**Conjecture**: |M(x)| < √x for all x.
**Status**: Disproved by Odlyzko & te Riele (1985) — they showed
counterexamples exist (above 10¹⁴) but did not exhibit one.
**In tested range [1, 10⁷]**: HOLDS. Max ratio 0.832 (well below 1).

The disproof is non-constructive. Best known bounds for the first
counterexample x₀: 10¹⁴ < x₀ < 10⁴⁰. Our range is far below this.

## Chebyshev ψ(x) = Σ_{p^k ≤ x} log p

| x | ψ(x) | ψ(x) - x | (ψ-x)/√x |
|---|------|----------|----------|
| 100 | 94.05 | -5.95 | -0.60 |
| 1,000 | 996.68 | -3.32 | -0.10 |
| 10,000 | 10,013.40 | +13.40 | +0.13 |
| 100,000 | 100,051.56 | +51.56 | +0.16 |
| 1,000,000 | 999,586.60 | -413.40 | -0.41 |
| 10,000,000 | 9,998,539.40 | -1,460.60 | -0.46 |

### PNT and RH error terms
- **PNT**: ψ(x) ~ x. Verified — ratio ψ(x)/x → 1 as x grows.
- **RH**: |ψ(x) - x| = O(√x · log² x).
- Observed (ψ-x)/√x is bounded — at x=10⁷ it's 0.46, well within
  the predicted bound √x · log²x / √x = log²x ≈ 259.

### Comparison with π(x) error
At x = 10⁷:
- |Li(x) - π(x)| / √x ≈ 338 / 3162 = 0.11
- |ψ(x) - x| / √x ≈ 1461 / 3162 = 0.46

ψ has a slightly larger relative error than π, which is expected:
ψ counts WITH log p weighting, so each prime contributes more.

## Equivalences with RH

| Statement | Implies | Equivalent to RH? |
|-----------|---------|-------------------|
| M(x) = O(x^(1/2 + ε)) | weak Mertens | YES |
| |M(x)| < √x (Mertens 1897) | strong Mertens | YES (but FALSE) |
| |ψ(x) - x| = O(√x · log² x) | refined PNT | YES |
| Li(x) - π(x) = O(√x · log x) | refined PNT for π | YES |

**The disproof of strong Mertens DID NOT disprove RH** — only ruled out
that specific quantitative form. RH is consistent with M(x) growing
slightly faster than √x (e.g., as √x · log log x).

## Reproducibility

Script: `numerics/mertens_chebyshev.py`
Dependencies: numpy, math.
Runtime: ~5 seconds for both functions up to N = 10⁷.

Pushing to N = 10⁸ would take ~50 seconds (sieve scales linearly).
The Möbius sieve via SPF is the bottleneck.
