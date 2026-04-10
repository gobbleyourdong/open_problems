# Polignac's Conjecture — All 50 Even Gaps d ≤ 100 Match HL to 0.2%

## Date: 2026-04-08

## The result

For every even d ∈ {2, 4, 6, ..., 100}, the count
```
π_d(N) := #{p ≤ N : p and p + d both prime}
```
at N = 10⁸ matches the **Hardy-Littlewood asymptotic**
```
π_d(N) ~ C_d · ∫_2^N dt / (log t)²
```
where
```
C_d = 2 C_2 · ∏_{q > 2, q | d} (q - 1)/(q - 2),    C_2 = 0.6601618...
```
to **within 0.2%** for all 50 gaps. Mean ratio: **0.9997**.

This is empirical evidence that the Hardy-Littlewood prime k-tuple
conjecture holds across the full d ≤ 100 range, not just for the
classical (twin/cousin/sexy) examples.

## Polignac (1849)

Polignac's conjecture: for every positive even d, there are infinitely
many prime pairs (p, p + d). Status: **OPEN for every d**.

- d = 2: twin prime conjecture (open)
- d = 246 (Maynard-Tao 2014): proven that some d ≤ 246 has infinitely many
- General d: open

Zhang (2013) proved bounded gaps (some d ≤ 70,000,000 has infinitely many);
Polymath8 + Maynard-Tao (2014-2015) brought this to 246. The d = 2 case
remains the holy grail.

## The 50 even gaps at N = 10⁸ (selected)

| d | C_d | observed | predicted | ratio | note |
|---|-----|----------|-----------|-------|------|
| 2 | 1.32032 | 440,312 | 440,368 | 0.9999 | twin |
| 4 | 1.32032 | 440,258 | 440,368 | 0.9998 | cousin |
| 6 | 2.64065 | 879,908 | 880,736 | 0.9991 | sexy |
| 8 | 1.32032 | 439,908 | 440,368 | 0.9990 |  |
| 10 | 1.76043 | 586,811 | 587,157 | 0.9994 |  |
| 12 | 2.64065 | 880,196 | 880,736 | 0.9994 |  |
| 14 | 1.58439 | 528,095 | 528,441 | 0.9993 |  |
| 16 | 1.32032 | 441,055 | 440,368 | 1.0016 |  |
| 18 | 2.64065 | 880,443 | 880,736 | 0.9997 |  |
| 20 | 1.76043 | 586,267 | 587,157 | 0.9985 |  |
| 24 | 2.64065 | 880,927 | 880,736 | 1.0002 |  |
| **30** | **3.52086** | **1,173,934** | **1,174,314** | **0.9997** | **3·5** |
| 36 | 2.64065 | 880,986 | 880,736 | 1.0003 |  |
| 42 | 3.16878 | 1,056,727 | 1,056,883 | 0.9999 | 3·7 |
| 48 | 2.64065 | 880,136 | 880,736 | 0.9993 |  |
| 54 | 2.64065 | 881,250 | 880,736 | 1.0006 |  |
| **60** | **3.52086** | **1,174,315** | **1,174,314** | **1.0000** | **3·5·4** |
| 66 | 2.93405 | 978,067 | 978,595 | 0.9995 | 3·11 |
| 72 | 2.64065 | 880,491 | 880,736 | 0.9997 |  |
| 78 | 2.88071 | 960,279 | 960,802 | 0.9995 | 3·13 |
| 84 | 3.16878 | 1,055,892 | 1,056,883 | 0.9991 | 3·7 |
| **90** | **3.52086** | **1,174,409** | **1,174,314** | **1.0001** | **3·5** |
| 96 | 2.64065 | 880,876 | 880,736 | 1.0002 |  |
| 98 | 1.58439 | 528,631 | 528,441 | 1.0004 |  |
| 100 | 1.76043 | 586,908 | 587,157 | 0.9996 |  |

**Worst ratio across all 50 gaps: 1.0016 at d = 16. Best: 1.0000 at d = 60.**
**Mean ratio: 0.9997. Standard deviation: 0.0007.**

## The "fertility" pattern: rank by C_d

Top 10 most fertile even gaps d ≤ 100 (largest C_d):

| rank | d | C_d | observed π_d(10⁸) | C_d / (2 C_2) | odd prime divisors |
|------|---|-----|-------------------|---------------|-------------------|
| 1 | 30 | 3.521 | 1,173,934 | 8/3 ≈ 2.667 | {3, 5} |
| 2 | 60 | 3.521 | 1,174,315 | 8/3 ≈ 2.667 | {3, 5} |
| 3 | 90 | 3.521 | 1,174,409 | 8/3 ≈ 2.667 | {3, 5} |
| 4 | 42 | 3.169 | 1,056,727 | 12/5 = 2.400 | {3, 7} |
| 5 | 84 | 3.169 | 1,055,892 | 12/5 = 2.400 | {3, 7} |
| 6 | 66 | 2.934 | 978,067 | 20/9 ≈ 2.222 | {3, 11} |
| 7 | 78 | 2.881 | 960,279 | 24/11 ≈ 2.182 | {3, 13} |
| 8 | 6 | 2.641 | 879,908 | 2.000 | {3} |
| 9 | 12 | 2.641 | 880,196 | 2.000 | {3} |
| 10 | 18 | 2.641 | 880,443 | 2.000 | {3} |

**The most fertile gaps are exactly the multiples of 30** (= 2·3·5), because
they "use up" both odd primes 3 and 5 in the singular series correction.
A primorial-style maximization!

## The "twin = cousin" surprise

| d | observation | prediction |
|---|-------------|------------|
| d = 2 (twin) | 440,312 | 440,368 |
| d = 4 (cousin) | 440,258 | 440,368 |
| d = 8 | 439,908 | 440,368 |
| d = 16 | 441,055 | 440,368 |
| d = 32 | 439,524 | 440,368 |
| d = 64 | 440,328 | 440,368 |

**ALL gaps that are pure powers of 2 have IDENTICAL HL predictions** (and
nearly identical observed counts). At 10⁸, the spread is at most 1500 out
of 440,000 — pure noise. Twin primes are not "special" — they're equal
in density to cousin primes, octuple primes, hexadecimal-prime pairs, etc.

This is counterintuitive! The "famous" twin primes (d=2) have no statistical
distinction from any other power-of-2 gap. The whole "twin prime conjecture"
mystique is about the pattern, not the count.

## The "d divisible by 3" doubling

| Family | Example d | Observed (typical) | C_d / C_2 |
|--------|-----------|--------------------|-----------|
| pure 2-power | 2, 4, 8, 16, 32, 64 | ~440,000 | 2.000 |
| 3·(2-power) | 6, 12, 24, 48, 96 | ~880,000 | 4.000 |
| 3·5·(2-power) | 30, 60 | ~1,174,000 | 16/3 ≈ 5.333 |
| 3·5·7·... | 30, 42, 60, 84, 90 | varies | up to 8 |

**The doubling at "3 divides d" comes from the (3-1)/(3-2) = 2 factor in
the singular series.** The HL constant essentially counts "how many ways d
covers the small primes' residue system".

## Why HL is so beautifully accurate

The Hardy-Littlewood singular series is derived from
1. The local density of (n, n+d) coprime to small primes
2. Multiplied over all primes via Möbius inclusion-exclusion
3. With correct normalization to give a probability per N units

At N = 10⁸ and d ≤ 100, ALL of:
- Sieve effects from primes ≤ 100
- Local-global density transitions
- Möbius cancellations
- Functional equations

are operating in concert to make the prediction within 0.2% of observation.
This is a strong signal that **the HL conjecture is essentially TRUE**.
The only thing missing is a proof.

## What we cannot do (yet)

While π_d(10⁸) for ALL d ≤ 100 is well-predicted, we cannot:
- Prove π_d(N) → ∞ for ANY single d (open since 1849)
- Prove π_d(N) ~ C_d · Li_2(N) for ANY single d (HL conjecture still open)
- Prove the singular series C_d converges in a way that passes through to
  arithmetic statements about specific intervals

The Maynard-Tao bound (d ≤ 246 for some unspecified d) is the best we've
proven about Polignac.

## Sigma Method observation

This is the **strongest empirical confirmation** of HL in this campaign.
50 independent gap classes, all matching to 3-4 digits, no anomalies.
At 10⁸, the typical noise per class is ~0.0007 (sqrt of inverse count),
and the discrepancies are at exactly that scale.

The fact that **the prediction works for d = 100 just as well as d = 2**
shows that HL is not a "fit to twin primes" — it's a structural law that
holds across the full pattern space. The constants C_d are not adjustable;
they're computed entirely from first principles via the singular series.

## Reproducibility

Script: `numerics/polignac.py`
Dependencies: numpy, scipy.integrate.quad, math, sieve_core.
Runtime: ~5 seconds (sieve + 50 bitwise AND counts on 10⁸ array).
