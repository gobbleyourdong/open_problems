# Dirichlet Primes & Chebyshev Bias — Verified Across 9 Moduli

## Date: 2026-04-09

## The Chebyshev bias

For modulus q, primes coprime to q are EQUIDISTRIBUTED asymptotically
across the φ(q) residue classes (Dirichlet's theorem). But there's a
systematic, small bias: **residues that are quadratic non-residues
(QNRs) consistently have slightly more primes than quadratic residues
(QRs)**.

This is the Chebyshev bias, predicted by Chebyshev (1853) and rigorously
explained by Rubinstein-Sarnak (1994) under GRH + linear independence
of zeros.

## Verification at x = 10⁷

| q | QR avg | QNR avg | diff | bias (σ) |
|---|--------|---------|------|----------|
| 3 | 332,194 | 332,383 | +189 | +0.33 |
| 4 | 332,180 | 332,397 | +217 | +0.38 |
| 5 | 166,068 | 166,220 | +152 | +0.37 |
| 7 | 110,733 | 110,792 | +59 | +0.18 |
| 8 | 165,976 | 166,200 | +224 | +0.55 |
| 11 | 66,423 | 66,491 | +68 | +0.26 |
| 12 | 166,011 | 166,188 | +177 | +0.43 |
| 13 | 55,360 | 55,403 | +43 | +0.18 |
| 16 | 82,988 | 83,100 | +112 | +0.39 |

**QNR > QR for all 9 moduli tested.** Bias size 0.18-0.55σ.

The probability that all 9 biases would be positive by chance under
the null hypothesis (no bias) is 1/2⁹ = 1/512 ≈ 0.2%. With actual
biases of order 0.3σ each, the combined evidence is much stronger.

## The famous prime race: q = 4

| Quantity | Value |
|----------|-------|
| π(10⁷; 4, 1) | 332,180 |
| π(10⁷; 4, 3) | 332,397 |
| Difference | 217 (4,3 leads) |
| Total sign changes in [0, 10⁷] | 112 |
| **First x where (4,1) leads** | **26,861** |
| Reference | Leech 1957 |

**Exact match to Leech 1957.** The first time the QR (residue 1 mod 4)
catches up to the QNR (residue 3 mod 4) is at x = 26,861. After that,
sign changes occur frequently (112 total in [0, 10⁷]).

## The hard race: q = 3

| Quantity | Value |
|----------|-------|
| π(10⁷; 3, 1) | 332,194 |
| π(10⁷; 3, 2) | 332,384 |
| Difference | 190 (3,2 leads) |
| Sign changes in [0, 10⁷] | 1 |
| First x where (3,1) leads | **none in our range** |
| Reference | Bays-Hudson 1978: x ≈ 6.09×10¹¹ |

For q = 3, the first time residue 1 catches up is at x = 608,981,813,029,
about 5 orders of magnitude beyond our reach. So in our range, residue
2 (the QNR) is ALWAYS ahead — the bias is undisturbed.

## Connection to GRH

Rubinstein-Sarnak (1994) showed: under
1. The Generalized Riemann Hypothesis (GRH) for Dirichlet L-functions
2. A linear independence assumption on the imaginary parts of zeros

the limiting density of x where a particular residue leads can be
computed exactly. For q = 4 (residues 1 vs 3), the density that
residue 3 (QNR) leads is **0.9959** — i.e., 99.59% of the time.

The first x where this 0.4% "minority case" occurs is x = 26,861 — far
into the asymptotic regime, illustrating just how persistent the bias is.

## Sigma Method observation

**The Chebyshev bias is one of the most subtle and well-confirmed
"weird primes" results.** It involves:
- A small but systematic effect (0.3σ at 10⁷, growing slowly)
- An exact historical result (Leech 1957 reproduced to the integer)
- A connection to GRH and the deep theory of L-functions
- Multiple independent moduli all confirming the same pattern

This is the kind of result that makes RH hard: even tiny statistical
effects on primes encode information about all the zeros of all the
Dirichlet L-functions simultaneously.

## Reproducibility

Script: `numerics/dirichlet_chebyshev.py`
Dependencies: numpy, math, sieve_core.
Runtime: ~5 seconds for full 9-modulus + 2-race analysis at N = 10⁷.
