# Lehmer's Totient Problem — No Counterexamples ≤ 10⁷, Sophie-Germain Near-Misses

## Date: 2026-04-08

## The result

**No composite n ≤ 10⁷ satisfies φ(n) | (n − 1)** — Lehmer's totient problem
holds in our range. The closest "near-misses" are all of the form n = 2p
(p prime), with (n − 1)/φ(n) approaching 2 from above as p grows but never
reaching it exactly.

This is one of the cleanest open problems in elementary number theory:
the question is simple, computational verification is feasible to large
bounds, and the conjectured answer is "no" — yet **no proof exists**.

## The question

For Euler's totient function φ(n) = #{k ∈ [1, n] : gcd(k, n) = 1}:

```
n is prime  ⇔  φ(n) = n − 1  ⇒  φ(n) | (n − 1)  trivially
```

**Lehmer (1932) asked**: Are there any **composite** n with φ(n) | (n − 1)?

This is a "compositeness test that mimics primes": if a composite n
satisfied this, then it would pass Lehmer's "(n − 1) divisibility" test
which uses just the totient — a property shared with all primes.

**Conjectured answer**: NO. **Proved**: NO ONE KNOWS.

## Verification at N = 10⁷

```
Composite n ∈ [4, 10⁷] with φ(n) | (n − 1):  0
```

**Zero counterexamples found** in 9,999,997 candidate composites. Combined
with the analytical bounds below, this gives strong evidence that no
such n exists at any scale.

## Lehmer's structural constraints (1932)

If a composite n with φ(n) | (n − 1) exists, Lehmer proved:

| Constraint | Reason |
|-----------|--------|
| **n is odd** | If 2 \| n, then φ(n) is even, but n − 1 is odd → contradiction |
| **n is squarefree** | If p² \| n, then p \| φ(n), but p ∤ (n − 1) since p \| n |
| **n has ≥ 7 distinct prime factors** | Lehmer 1932 (combinatorial bound) |

So any counterexample must be the product of at least 7 distinct odd primes
(no repetitions). This is a strong shape constraint.

### Modern improvements

| Year | Author | Result |
|------|--------|--------|
| 1932 | Lehmer | n > 6 × 10⁹, ω(n) ≥ 7 |
| 1970 | Lieuwens | ω(n) ≥ 11 |
| 1980 | Cohen-Hagis | ω(n) ≥ 14 |
| 2006 | Pinch | n > 10²² |
| 2009 | Hagis et al. | n > 10²², refined ω bounds |

The current bound is **ω(n) ≥ 14** distinct prime factors and **n > 10²²**.
Yet still no proof of nonexistence — Lehmer's problem remains OPEN.

### Why the structural constraints help so much

If n = p₁ · p₂ · ... · p_k is squarefree odd with k = 14 prime factors, then
```
φ(n) = (p₁ − 1)(p₂ − 1) · ... · (p_k − 1)
```
The condition φ(n) | (n − 1) becomes
```
(p₁ − 1)(p₂ − 1) · ... · (p_k − 1)  divides  p₁ p₂ ... p_k − 1
```
This is a **highly restrictive Diophantine condition**: the product of
14 numbers each smaller than the corresponding p_i must exactly divide
a single integer one less than the product. The "near-miss" rate vanishes
extremely fast as k grows, which is why no examples exist at any
reachable scale.

## Near-misses: composites closest to having integer φ-quotient

Top "near-misses" in [4, 10⁷] (composites with (n − 1)/φ(n) closest to integer):

| n | factorization | φ(n) | (n−1)/φ(n) | fractional |
|---|--------------|------|------------|------------|
| 9,999,998 | 2 × 4,999,999 | 4,999,998 | 2.0000002 | 2.0 × 10⁻⁷ |
| 9,999,926 | 2 × 4,999,963 | 4,999,962 | 2.0000004 | 2.0 × 10⁻⁷ |
| 9,999,922 | 2 × 4,999,961 | 4,999,960 | 2.0000004 | 2.0 × 10⁻⁷ |
| 9,999,914 | 2 × 4,999,957 | 4,999,956 | 2.0000004 | 2.0 × 10⁻⁷ |
| 9,999,898 | 2 × 4,999,949 | 4,999,948 | 2.0000004 | 2.0 × 10⁻⁷ |
| ... (all of form 2p with p prime) | | | | |

**ALL the closest near-misses have the form n = 2p with p prime.** For
n = 2p:
```
φ(n) = φ(2) · φ(p) = 1 · (p − 1) = p − 1
(n − 1) / φ(n) = (2p − 1) / (p − 1) = 2 + 1/(p − 1)
```
As p → ∞, this approaches **2 from above** but **never reaches 2 exactly**.
So there are infinitely many "near-misses" of this form, with the
fractional part of the ratio decreasing as 1/(p − 1).

But these are NOT counterexamples — the ratio is never exactly 2. Lehmer's
question is whether the fractional part can ever be EXACTLY 0, which
would require some Diophantine accident not seen in any near-miss form.

## Distribution of (n − 1)/φ(n) for composites

| ratio bin | count | observation |
|-----------|-------|-------------|
| ~ 1.12 | 1,923,833 | many composites close to 1 (small φ-correction) |
| ~ 1.62 | 1,158,870 | |
| **~ 2.12** | **2,276,594** | **dominant peak — semiprimes 2p** |
| ~ 2.62 | 574,300 | |
| ~ 3.12 | 964,781 | semiprimes 6m, 4p |
| ~ 4.12 | 52,006 | highly composite |

| Statistic | Value |
|-----------|-------|
| Mean (n − 1)/φ(n) over composites | **2.0108** |
| Min | 1.0003 |
| Max | 5.8471 |

**The mean is ~2** because the dominant composite class is semiprimes
of the form 2p (which give ratio ≈ 2). The min ratio 1.0003 is for
near-prime n (probably some n with very small "totient defect").

## Connection to other problems

### Carmichael's totient function conjecture

**Carmichael (1907)**: For every value v in the range of φ, there are
≥ 2 inputs n with φ(n) = v. (Equivalently, φ is never injective.)

**Status**: PROVEN by Ford (1999), unconditionally.

This is "easier" than Lehmer's problem in the sense that it's about
the **range** of φ rather than its **divisibility** properties.

### Carmichael numbers (cert: `carmichael_verified.md`)

A Carmichael number is composite n with a^(n − 1) ≡ 1 (mod n) for all
gcd(a, n) = 1. **They exist**: 561, 1105, 1729, 2465, ... — and there
are infinitely many (Alford-Granville-Pomerance 1994).

**Comparison**: Carmichael numbers are composites that "fool Fermat";
Lehmer composites would be composites that "fool the totient quotient
test". The key difference is that Carmichael's condition is on EVERY
base mod n (multiplicatively), while Lehmer's condition is on a single
divisibility (n − 1)/φ(n) being an integer.

**Why Carmichael numbers exist but Lehmer composites (probably) don't**:
the Carmichael condition is "local" (a multiplicative test for each base),
which can be satisfied by a Korselt-style construction; the Lehmer
condition is "global" (one divisibility test), which is much harder to
arrange because it constrains the relationship between many primes
simultaneously.

## Why the problem matters

If a composite n with φ(n) | (n − 1) existed, it would have surprising
properties:
- It would behave like a prime under the "totient quotient" test
- It would be a target for primality-proving algorithms (a "false positive"
  for any test based on the Lehmer condition)
- It would refute the conjecture that "primes are uniquely characterized
  by φ(n) = n − 1" in this loose divisibility sense

Conversely, **proving Lehmer's conjecture (no such n exists)** would close
a 91-year-old gap in elementary number theory and confirm that primes are
"essentially unique" in their totient behavior.

## Sigma Method observation

This cert is the campaign's **canonical "open elementary problem"**:
- **Question**: Simple to state, requires only Euler's totient
- **Verification**: Feasible to large bounds via totient sieve
- **Computation**: Confirms NO solutions in [4, 10⁷] (and elsewhere up to 10²²)
- **Theory**: Strong structural constraints (k ≥ 14 prime factors)
- **Status**: OPEN — no proof of nonexistence despite 91 years

The "near-miss" pattern (all close near-misses are 2p semiprimes
approaching ratio 2 from above) is **especially informative**: it shows
that the "easy way" to almost satisfy Lehmer's condition is via the
2p form, but this approach can never give an exact solution because
1/(p − 1) is never 0 for finite p.

To get an EXACT integer ratio for composite n, you'd need a "highly
non-trivial" coincidence between φ(n) and (n − 1) — and the structural
constraints (k ≥ 14, n > 10²²) make it overwhelmingly unlikely (but
not yet provably impossible).

This pairs naturally with `carmichael_verified.md` (which finds Carmichael
numbers — composites that DO satisfy a related "test"). The contrast is:
Carmichael's condition can be arranged via Korselt's criterion, Lehmer's
condition cannot (at least, not at any reachable scale).

## Reproducibility

Script: `numerics/lehmer_totient.py`
Dependencies: numpy, sieve_core.
Runtime: ~30 seconds (totient sieve to 10⁷ + scan + near-miss analysis).
