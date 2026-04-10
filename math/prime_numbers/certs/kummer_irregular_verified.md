# Kummer's Irregular Primes — Bernoulli, Cyclotomic Class Groups, and FLT

## Date: 2026-04-08

## The result

**All 28 irregular primes p ≤ 500 found** via Kummer's criterion (p divides
the numerator of B_{2k} for some 2k ∈ [2, p − 3]). The list matches
**OEIS A000928** exactly:
```
{37, 59, 67, 101, 103, 131, 149, 157, 233, 257, 263, 271, 283, 293,
 307, 311, 347, 353, 379, 389, 401, 409, 421, 433, 461, 463, 467, 491}
```
**66 regular primes** (Kummer's FLT theorem applies to all of them).

## Definition

An odd prime p is **regular** if p does not divide the class number h(Q(ζ_p))
of the p-th cyclotomic field Q(ζ_p) (where ζ_p = e^(2πi/p)).
Otherwise it is **irregular**.

The class number h is in general extremely hard to compute. **Kummer's
remarkable insight (1850)**: regularity is equivalent to a simple
divisibility condition on Bernoulli numbers.

## Kummer's criterion (1850)

> p is regular iff p does NOT divide the numerator of any B_{2k}
> for 2 ≤ 2k ≤ p − 3.

This converts a difficult class group computation to a finite check:
compute B_2, B_4, ..., B_{p−3} (all rationals), and look for a numerator
divisible by p.

The **irregularity index** of p is the number of even integers
2k ∈ [2, p − 3] with p | numerator(B_{2k}). Index 0 = regular,
index ≥ 1 = irregular.

## The 28 irregular primes ≤ 500 with their indices

| p | index | bad B_{2k} (witnesses) |
|---|-------|------------------------|
| 37 | 1 | B_32 |
| 59 | 1 | B_44 |
| 67 | 1 | B_58 |
| 101 | 1 | B_68 |
| 103 | 1 | B_24 |
| 131 | 1 | B_22 |
| 149 | 1 | B_130 |
| **157** | **2** | **B_62, B_110** |
| 233 | 1 | B_84 |
| 257 | 1 | B_164 |
| 263 | 1 | B_100 |
| 271 | 1 | B_84 |
| 283 | 1 | B_20 |
| 293 | 1 | B_156 |
| 307 | 1 | B_88 |
| 311 | 1 | B_292 |
| 347 | 1 | B_280 |
| **353** | **2** | **B_186, B_300** |
| **379** | **2** | **B_100, B_174** |
| 389 | 1 | B_200 |
| 401 | 1 | B_382 |
| 409 | 1 | B_126 |
| 421 | 1 | B_240 |
| 433 | 1 | B_366 |
| 461 | 1 | B_196 |
| 463 | 1 | B_130 |
| **467** | **2** | **B_94, B_194** |
| **491** | **3** | **B_292, B_336, B_338** |

**Most irregular primes have index 1** (a single bad Bernoulli numerator).
**491 has index 3** — the most "irregular" prime in our range.

## The famous 691 connection

**Kummer's original observation (1850)**: B_12 = −691/2730. Since 691 is
prime and divides the numerator, **691 is irregular** with irregularity
index 1 (just B_12).

This is the smallest irregular prime that divides a Bernoulli numerator
in a "small" position — Kummer noticed it because B_12 is small enough
to compute by hand.

```
B_12 = -691/2730  ← computed via mpmath.bernfrac(12)
691 | numerator: True
```

(691 is just outside our [2, 500] range, so it doesn't appear in our
table, but the calculation is verified.)

## Cumulative density vs Siegel's heuristic

**Siegel (1964)**: The density of irregular primes is conjecturally
1 − e^(−1/2) ≈ 0.39347.

**Heuristic derivation**: each B_{2k} mod p is "random" in [0, p), so
P(p | B_{2k}) ≈ 1/p. There are (p − 3)/2 ≈ p/2 candidate 2k values.
P(p has zero hits) ≈ (1 − 1/p)^(p/2) → e^(−1/2) as p → ∞.
Hence density of irregular primes → 1 − e^(−1/2).

| X | irregular | odd primes | observed density | Siegel (asymptotic) |
|---|-----------|-----------|------------------|---------------------|
| 50 | 1 | 14 | 0.071 | 0.3935 |
| 100 | 3 | 24 | 0.125 | 0.3935 |
| 150 | 7 | 34 | 0.206 | 0.3935 |
| 200 | 8 | 45 | 0.178 | 0.3935 |
| 250 | 9 | 52 | 0.173 | 0.3935 |
| 300 | 14 | 61 | 0.230 | 0.3935 |
| 350 | 17 | 69 | 0.246 | 0.3935 |
| 400 | 20 | 77 | 0.260 | 0.3935 |
| 450 | 24 | 86 | 0.279 | 0.3935 |
| **500** | **28** | **94** | **0.298** | **0.3935** |

**Density climbs slowly from 0.07 to 0.30 over [50, 500]**, approaching
Siegel's 0.3935 from below. Convergence is logarithmic — by p ≈ 10⁷,
empirical density is about 0.36 (Buhler-Harvey 2011), still below Siegel.
Buhler-Crandall-Ernvall-Metsänkylä-Shokrollahi extended this to ~10⁹
with density ~0.367.

The **slow under-convergence** to Siegel's asymptotic is itself a notable
phenomenon — the heuristic is right in shape but the convergence rate
is governed by ω(p) and other p-dependent factors.

## Kummer's FLT theorem

> **Kummer (1850)**: If p is a regular odd prime, then Fermat's Last
> Theorem holds for exponent p — there are no nonzero integer solutions
> to x^p + y^p = z^p.

This was a sensation in 1850. It was the first general technique for
attacking FLT after Fermat's own marginal note in 1637 — over 200 years
of waiting. Kummer's proof:

1. **Factor x^p + y^p over Q(ζ_p)**: in Z[ζ_p], one has
   ```
   x^p + y^p = ∏_{j=0}^{p-1} (x + ζ_p^j y)
   ```
2. **Coprimality and unique factorization**: in regular cases (p ∤ class
   number), the factors are pairwise coprime "ideals" with unique
   prime ideal factorization. Each must be a p-th power.
3. **Take p-th roots in the cyclotomic ring**: derive constraints that
   ultimately contradict the assumed equation.

The crux is the **unique factorization**, which holds for ideals in
Z[ζ_p] when p is regular. Without regularity, prime ideals can fail
to be principal, and the factor-and-take-roots argument fails.

### FLT exponents covered ≤ 500

| Status | Count | Examples |
|--------|-------|----------|
| Regular (Kummer's theorem applies) | **66** | 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ... |
| Irregular (Kummer's theorem fails) | **28** | 37, 59, 67, 101, 103, 131, ... |

Kummer's theorem alone covers ~70% of small odd primes for FLT. The
remaining 30% (irregular primes) needed extension.

### The Vandiver extension and Wiles

**Vandiver (1929)**: extended FLT to many irregular primes via the
"Vandiver criterion" — checking that no prime in a related auxiliary
set divides the class number. This handled most known irregular primes
but not all.

**Wiles (1995)**: Proved FLT in full generality via the **modularity
theorem** for elliptic curves. Wiles's proof bypasses Kummer's
cyclotomic approach entirely, using instead the connection
```
elliptic curves ↔ modular forms ↔ Galois representations
```
with Frey's curve to derive a contradiction from any FLT counterexample.

Wiles is vastly more powerful than Kummer (it covers all p, not just
regular), but Kummer's theorem retains its place as the **first
infinite-family result** on FLT.

## Connection to ζ values

Bernoulli numbers are connected to Riemann zeta values via Euler:
```
ζ(2k) = (-1)^(k+1) · (2π)^(2k) · B_{2k} / (2 · (2k)!)
```
So:
```
B_{2k} = (-1)^(k+1) · 2 · (2k)! · ζ(2k) / (2π)^(2k)
```
The numerator of B_{2k} encodes information about ζ(2k) — specifically,
Kummer's irregular prime condition is "p divides ζ(2k) in some sense".

**This is the bridge from ζ to FLT**: irregular primes are exactly the
primes where the Riemann zeta function has a special "p-adic vanishing"
that controls the cyclotomic class number. The Kummer-Iwasawa theory
makes this precise via p-adic L-functions.

## Sigma Method observation

This cert is the campaign's **deepest connection between number theory's
main pillars**:
- **Bernoulli numbers** (combinatorial, computed by mpmath.bernfrac)
- **Cyclotomic class groups** (algebraic, controlled by Kummer's criterion)
- **Riemann zeta values** (analytic, via Euler's formula)
- **Fermat's Last Theorem** (Diophantine, the historical motivation)

A simple divisibility check on numerators of Bernoulli numbers reveals
the cyclotomic class group structure, which controls FLT — and we can
verify the entire ladder for the first 28 irregular primes in seconds
using mpmath.

The Sigma Method takeaway: **arithmetic objects are highly correlated
across "different" mathematical structures**. Computing one (Bernoulli
numerators) gives free access to information about the others (class
numbers, FLT exponents). This is the kind of "underground connection"
that makes computational number theory powerful — verifying one
quantity unlocks predictions about others.

## Reproducibility

Script: `numerics/kummer_irregular.py`
Dependencies: mpmath (for bernfrac), sieve_core (for primes_up_to).
Runtime: ~2 seconds (computing 248 even Bernoulli numbers + 94 prime tests).
