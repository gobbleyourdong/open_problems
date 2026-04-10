# Mersenne Primes & Perfect Numbers — 15 Mersennes Found via Lucas-Lehmer

## Date: 2026-04-08

## The result

All **15 Mersenne primes M_p = 2^p − 1 with prime p ≤ 1500** found via the
Lucas-Lehmer test, in agreement with OEIS A000043.

For each, the corresponding **perfect number** N = 2^(p−1) · M_p is verified
to satisfy σ(N) = 2N (the Euclid-Euler theorem). The first 6 are checked
by direct sum of divisors; the larger ones are verified algebraically via
the multiplicative formula σ(N) = (2^p − 1)(M_p + 1) = M_p · 2^p = 2N.

## The 15 Mersenne primes (p ≤ 1500)

| # | p | M_p digits | M_p (or compact) |
|---|---|-----------|------------------|
| 1 | 2 | 1 | 3 |
| 2 | 3 | 1 | 7 |
| 3 | 5 | 2 | 31 |
| 4 | 7 | 3 | 127 |
| 5 | 13 | 4 | 8,191 |
| 6 | 17 | 6 | 131,071 |
| 7 | 19 | 6 | 524,287 |
| 8 | 31 | 10 | 2,147,483,647 |
| 9 | 61 | 19 | 2,305,843,009,213,693,951 |
| 10 | 89 | 27 | 61897001…49562111 |
| 11 | 107 | 33 | 16225927…10288127 |
| 12 | 127 | 39 | 17014118…84105727 |
| 13 | 521 | 157 | 68647976…15057151 |
| 14 | 607 | 183 | 53113799…31728127 |
| 15 | 1279 | 386 | 10407932…68729087 |

The list matches OEIS A000043 (Mersenne exponents) exactly. Total runtime
on a single CPU: about 30 seconds for all 15 (Lucas-Lehmer is very fast
even for 386-digit M_1279).

## The Lucas-Lehmer test

For prime p > 2, M_p = 2^p − 1 is prime if and only if S_{p−2} ≡ 0 (mod M_p),
where S_0 = 4 and S_{i+1} = S_i² − 2.

**Why it's so efficient**:
- Each squaring mod M_p uses bit-shifts since M_p = 2^p − 1 (no division needed)
- Total work is O(p) modular squarings of p-bit numbers → O(p · M(p)) where M is multiplication
- For p ~ 10⁶ this is about 10¹² bit operations, completable in hours
- For p ~ 10⁸ (the current frontier) it takes about a year on consumer hardware

This is why **the largest known prime is always a Mersenne prime**: no other
known primality test is anywhere near as fast for numbers of similar size.
The current record is M_82589933 (2018, GIMPS) with ~24.8 million digits.

## Euclid-Euler theorem verification

| p | M_p | Perfect N = 2^(p−1)·M_p | σ(N) | σ(N) − 2N |
|---|-----|-------------------------|------|-----------|
| 2 | 3 | 6 | 12 | 0 |
| 3 | 7 | 28 | 56 | 0 |
| 5 | 31 | 496 | 992 | 0 |
| 7 | 127 | 8,128 | 16,256 | 0 |
| 13 | 8,191 | 33,550,336 | 67,100,672 | 0 |
| 17 | 131,071 | 8,589,869,056 | 17,179,738,112 | 0 |

All by direct sum-of-divisors computation. Every perfect number is
**exactly twice itself** in σ-value.

### Algebraic proof of Euclid's direction

For N = 2^(p−1) · M_p with M_p = 2^p − 1 prime:
```
σ(N) = σ(2^(p−1)) · σ(M_p)              (σ multiplicative since gcd = 1)
     = (2^p − 1) · (M_p + 1)             (geometric sum + M_p prime)
     = M_p · 2^p
     = 2 · 2^(p−1) · M_p
     = 2N    Q.E.D.
```

Euler's converse (every even perfect number has this form) is harder. The
key fact: if N is even and perfect, write N = 2^a · m with m odd, a ≥ 1.
Then σ(N) = 2N gives σ(2^a) σ(m) = 2^(a+1) m, i.e., (2^(a+1) − 1) σ(m) = 2^(a+1) m.
Since 2^(a+1) − 1 is odd, it divides m. Setting m = (2^(a+1) − 1) k forces
σ(m) = 2^(a+1) k, which (with care) implies k = 1 and m = 2^(a+1) − 1 prime.

**No odd perfect number is known.** If one exists, it must be > 10^1500
(Ochem-Rao 2012). It is conjectured none exist.

## Lenstra-Pomerance-Wagstaff heuristic

Wagstaff (1983) extended a heuristic of Gillies/Lenstra: assume each
M_p = 2^p − 1 is "random" with respect to primality, accounting only for
the constraint that small primes can't divide M_p (they have order
dividing p in the multiplicative group). The result:
```
M(X) := #{p prime, p ≤ X : M_p prime} ~ (e^γ / log 2) · log X
```
where γ ≈ 0.5772 is Euler's constant. The leading constant is
**(e^γ / log 2) ≈ 2.5695**.

### Comparison

| X | observed M(X) | LPW prediction | ratio |
|---|---------------|----------------|-------|
| 10 | 4 | 5.92 | 0.676 |
| 30 | 7 | 8.74 | 0.801 |
| 100 | 10 | 11.83 | 0.845 |
| 300 | 12 | 14.66 | 0.819 |
| 1,000 | 14 | 17.75 | 0.789 |
| 1,500 | 15 | 18.79 | 0.798 |

**Ratio sits around 0.8** — LPW slightly over-predicts at this scale. This
is consistent with both:
1. Heuristic nature of the asymptotic (errors are O(1/log X) at finite X)
2. Known irregularity in the Mersenne distribution

### Density per log-range (LPW says ≈ 2.57 per unit of log)

| range | count | rate per log range |
|-------|-------|---------------------|
| [2, 30] | 7 | **2.585** |
| [31, 100] | 3 | 2.562 |
| [101, 300] | 2 | 1.837 |
| [301, 1000] | 2 | 1.666 |
| [1001, 1500] | 1 | 2.472 |

**The first two bins match LPW within 1%**. The middle bins have a
"drought" — between p = 127 and p = 521, there are no Mersenne primes
across about 400 prime exponents. This is the famous **Mersenne gap**.
By [1001, 1500] the rate recovers.

## Why Mersenne primes thin out so much

A naive heuristic: if M_p is "random", the chance it's prime should be
1/log M_p = 1/(p log 2). Sum over p ≤ X:
```
#{p ≤ X : M_p prime} ≈ Σ_{p ≤ X} 1/(p log 2)
                    ≈ (1/log 2) · log log X    (Mertens 1874)
```
This gives the **wrong** asymptotic — too slow. The LPW correction
adds the factor `e^γ` that arises from the constraint analysis: small
primes are forbidden as divisors, increasing the effective primality
probability of M_p.

The constant `e^γ / log 2 ≈ 2.57` reflects:
- `1/log 2` from the heuristic primality probability
- `e^γ` from the Mertens-Meissel correction summed over small prime
  divisors blocked by Fermat's little theorem

## Connection to amicable pairs and aliquot sequences

A perfect number n satisfies σ(n) = 2n, equivalently s(n) = n where
s(n) = σ(n) − n is the **proper-divisor sum**. Generalizations:
- **Amicable pair**: s(a) = b, s(b) = a (Pythagoras knew (220, 284))
- **Sociable cycle**: s(s(...s(n)...)) = n after k steps, k > 2
- **Aliquot sequence**: iterated s; conjectured to terminate or cycle

Both perfect numbers (1-cycles) and amicable pairs (2-cycles) are extremely
rare. The first 6 perfect numbers are 6, 28, 496, 8128, 33550336, 8589869056.
The largest known is the perfect number from M_82589933, with ~50 million digits.

## Sigma Method observation

This cert is the **most "elementary" proof of an unproved conjecture**:
- The Lucas-Lehmer test is **fully proved** (Lucas 1878, Lehmer 1930)
- The Euclid-Euler theorem is **fully proved** (Euclid forward, Euler converse)
- The list of 15 Mersenne primes ≤ p = 1500 is **rigorously verified**
- The LPW prediction is a **heuristic**, not a theorem

The pattern: rigorous tests (Lucas-Lehmer) + exhaustive search (1500 primes)
+ a probabilistic model (LPW) gives a complete picture of **what we know
empirically** about Mersenne primes, plus the heuristic for what we can't
prove (infinitude of Mersenne primes is OPEN).

**Sigma Method takeaway**: when a conjecture is hard to prove (infinitely
many Mersenne primes? infinitely many perfect numbers? odd perfects?), the
combination of (a) rigorous algorithm + (b) computational evidence + (c)
heuristic model gives the most complete picture obtainable.

## Reproducibility

Script: `numerics/mersenne_perfect.py`
Dependencies: math, sieve_core (for prime list ≤ 1500).
Runtime: ~30 seconds total (dominated by LL test for p = 1279).
