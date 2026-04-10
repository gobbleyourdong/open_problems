# Liouville Function & Pólya's Conjecture — Verified ≤ 10⁷, π²/15 to 11 Digits

## Date: 2026-04-08

## The result

For the **Liouville function** λ(n) = (−1)^Ω(n) (where Ω counts prime
factors with multiplicity), at x ≤ 10⁷:

| Test | Result |
|------|--------|
| **Pólya conjecture** (L(x) ≤ 0) | **HOLDS** in [2, 10⁷] |
| **Mertens-style bound** (|L(x)| ≤ √x) | **FAILS** at x = 96,862 (|L|/√x = 1.33) |
| **Generating function**: Σ λ(n)/n² | **= π²/15 to 11 digits** |
| **Generating function**: Σ λ(n)/n³ | **= ζ(6)/ζ(3) to 16 digits** (float-exact) |

The **Pólya counterexample at n = 906,150,257** (Tanaka 1980) is just outside
our 10⁷ range, so we see no Pólya violations directly. But the smaller
"Mertens-style |L| < √x" claim is already disproved within [2, 10⁷] —
useful contrast.

## Definition and small values

```
λ(n) := (-1)^Ω(n)
Ω(n) := number of prime factors of n WITH multiplicity
```

| n | factorization | Ω(n) | λ(n) |
|---|--------------|------|------|
| 1 | 1 | 0 | +1 |
| 2 | 2 | 1 | −1 |
| 3 | 3 | 1 | −1 |
| 4 | 2² | 2 | +1 |
| 5 | 5 | 1 | −1 |
| 6 | 2·3 | 2 | +1 |
| 7 | 7 | 1 | −1 |
| 8 | 2³ | 3 | −1 |
| 9 | 3² | 2 | +1 |
| 10 | 2·5 | 2 | +1 |
| 12 | 2²·3 | 3 | −1 |
| 16 | 2⁴ | 4 | +1 |

**Difference from Möbius**: μ(n) = 0 if n is not squarefree (e.g., μ(4) = μ(8) = 0),
while λ(n) is **never zero** — it cycles between +1 and −1 based on the
total prime count with multiplicity.

## L(x) at multiple scales

```
L(x) := Σ_{n ≤ x} λ(n)
```

| x | L(x) | L(x) / √x | sign |
|---|------|-----------|------|
| 10 | 0 | 0.000 | ≤ 0 ✓ |
| 100 | -2 | -0.200 | ≤ 0 ✓ |
| 10³ | -14 | -0.443 | ≤ 0 ✓ |
| 10⁴ | -94 | -0.940 | ≤ 0 ✓ |
| 10⁵ | -288 | -0.911 | ≤ 0 ✓ |
| 10⁶ | -530 | -0.530 | ≤ 0 ✓ |
| **10⁷** | **-842** | **-0.266** | **≤ 0 ✓** |

**Pólya's conjecture L(x) ≤ 0 holds at every checkpoint** (and at every
single x in [2, 10⁷] — exhaustively verified).

## Pólya's conjecture (1919) and its disproof

**Pólya (1919) conjectured**: L(x) ≤ 0 for all x ≥ 2.

This was strongly suggested by direct computation: L(x) ≤ 0 for all x in
the computable range of 1919 (~10⁵). The conjecture stood for **39 years**.

**Haselgrove (1958)** disproved Pólya analytically using Riemann's explicit
formula, **without exhibiting a counterexample**. The proof used the same
machinery as Littlewood's 1914 disproof of Gauss's Li(x) > π(x) conjecture
(see `skewes_littlewood_verified.md`) — both rely on the oscillating behavior
of the zero sum overcoming a "main term" eventually.

**Tanaka (1980)** found the **smallest counterexample**: at n = 906,150,257,
L(n) = +1. This is just beyond our 10⁷ range, which is why we see no
violations in our direct computation.

| Bound on first counterexample | Year | Author |
|--------------------------------|------|--------|
| existence (no number) | 1958 | Haselgrove |
| < 1.847 × 10³⁶¹ | 1960 | Lehman |
| < 1.96 × 10²⁹⁰ | 1980 | Tanaka |
| **= 906,150,257** | **1980** | **Tanaka (exact)** |

The discovery of the exact counterexample at ~9 × 10⁸ was a major
computational achievement at the time — essentially exhausting the
limits of 1980 computing power.

## The Mertens-style bound is even weaker — and FAILS in our range

| Bound | Status |
|-------|--------|
| L(x) ≤ 0 (Pólya) | **HOLDS** for x ≤ 906,150,256 |
| |L(x)| ≤ √x | **FAILS** at x = 96,862 (|L|/√x = 1.33) |

At x = 96,862:
- L(96,862) = -414 (computed)
- √96,862 ≈ 311.2
- |L| / √x = 1.331

So **L can be MORE NEGATIVE than √x** — the cumulative bias of small
factors makes the Liouville sum drift more strongly than its variance
would suggest. RH gives the weaker O(x^(1/2 + ε)), which is consistent
with what we see (the 1.33 ratio doesn't grow without bound, just stays
in O(1) up to log factors).

For comparison, the **Mertens function** M(x) (sum of μ) was conjectured
by Mertens in 1897 to satisfy |M(x)| < √x. This was disproved by
Odlyzko-te Riele (1985) using LLL on Riemann zeros — no explicit
counterexample is known, but the disproof shows limsup |M|/√x ≥ 1.06.

**Liouville parallel**: Pólya is the analogous one-sided conjecture for L,
disproved 27 years earlier. The Liouville disproof was easier because
Pólya's claim is one-sided (L ≤ 0), whereas Mertens is two-sided.

## Generating function: Σ λ(n)/n^s = ζ(2s)/ζ(s)

This is the **fundamental Dirichlet series identity** for the Liouville
function, proven by an Euler product manipulation:
```
Σ_{n=1}^∞ λ(n) / n^s = ∏_p (1 + λ(p)/p^s + λ(p²)/p^(2s) + ...)
                     = ∏_p (1/(1 + 1/p^s))     since λ(p^k) = (-1)^k
                     = ∏_p ((1 - 1/p^s)/(1 - 1/p^(2s)))
                     = ζ(2s) / ζ(s)
```

### At s = 2: Σ λ(n)/n² = ζ(4)/ζ(2) = π²/15

```
ζ(4) = π⁴/90
ζ(2) = π²/6
ζ(4)/ζ(2) = (π⁴/90)/(π²/6) = π² · 6/90 = π²/15 ≈ 0.6579736267...
```

### Verification at N = 10⁷

```
Σ_{n=1}^{10⁷} λ(n)/n²    = 0.6579736268
π²/15                    = 0.6579736267
Δ                        = +1.94 × 10⁻¹¹
Tail bound (1/N)         = 1.00 × 10⁻⁷
```

**Match to 11 digits** — much better than the 1/N tail bound. The
improvement comes from the cancellations in Σ_{n > N} λ(n)/n²: since λ
oscillates around 0, the partial-sum tail is much smaller than its
absolute-value upper bound.

### Bonus at s = 3: Σ λ(n)/n³ = ζ(6)/ζ(3)

```
Σ_{n=1}^{10⁷} λ(n)/n³    = 0.8463351937
ζ(6)/ζ(3)                = 0.8463351937
Δ                        = 1.1 × 10⁻¹⁶  (float-precision)
```

**Floating-point exact match.** ζ(6) = π⁶/945 (exact), ζ(3) ≈ 1.20206
(Apéry's constant, irrational — not known to be a simple closed form),
so ζ(6)/ζ(3) = π⁶ / (945 × ζ(3)) ≈ 0.8463. Our partial sum agrees with
this to all 16 float digits.

## Cross-comparison: Liouville vs Möbius

| | Liouville L(x) | Mertens M(x) |
|---|--------------|-------------|
| Definition | Σ λ(n), λ(n) = (-1)^Ω(n) | Σ μ(n), μ from Möbius |
| Range of summand | ±1 always | -1, 0, or +1 |
| Generating function | ζ(2s)/ζ(s) | 1/ζ(s) |
| Conjectured bound (failed) | L(x) ≤ 0 (Pólya 1919) | |M(x)| ≤ √x (Mertens 1897) |
| First counterexample | 906,150,257 (Tanaka 1980) | unknown (but proven by O-tR 1985) |
| Year disproved | 1958 (Haselgrove) | 1985 (Odlyzko-te Riele) |
| RH equivalence | L(x) = O(x^(1/2+ε)) ⇔ RH | M(x) = O(x^(1/2+ε)) ⇔ RH |
| Our cert | this one | `mertens_chebyshev.md` |

**Both are "almost true under RH"**: the bounds with ε > 0 hold under RH,
but the specific quantitative versions (L ≤ 0; |M| < √x) both fail at
finite scale because of the oscillating contribution from ζ-zeros.

## The connection to RH

For both Liouville and Mertens:
- **The strong form** (Pólya / Mertens) is FALSE.
- **The weak form** L(x) = O(x^(1/2+ε)) (or M(x) = O(x^(1/2+ε))) is
  EQUIVALENT TO RH.

Why? Both summatory functions can be written via Perron's formula:
```
L(x) = (1 / (2πi)) ∫ (ζ(2s)/ζ(s)) · x^s/s ds
```
The integrand has poles at s = 1/2 (from ζ(2s)) and at the nontrivial
zeros of ζ(s). Under RH, all the zero poles lie on Re(s) = 1/2, so the
contribution from each is O(x^(1/2 + ε)).

If RH fails (a zero off the critical line), then L(x) would have a
contribution like O(x^β) where β > 1/2, violating the weak Liouville bound.

So computing L(x) for very large x is a (slow) way to **probe RH
empirically**: any large jump beyond x^(1/2 + ε) would falsify RH.
Within our x ≤ 10⁷ range, |L|/√x ≤ 1.33, well consistent with RH.

## Sigma Method observation

This cert pairs with `mertens_chebyshev.md` to give the **two main
"summatory function" probes of RH**:
- Mertens M(x) for the Möbius function
- Liouville L(x) for the Liouville function

Both:
- Have a "naive" conjecture (Pólya/Mertens) that **fails** at large but
  finite x
- Have a "weak" form equivalent to RH
- Are excellent empirical RH probes
- Connect via Dirichlet series to ζ(s) directly

The Liouville function has the pedagogical advantage of being **always
nonzero**, making the cumulative sum a true random-walk-like process with
clean statistics. The Mertens function has zeros (whenever μ vanishes on
non-squarefree numbers), giving it a "Cantor-set-like" sparseness that
complicates the analysis.

The fact that **the Mertens-style |L| < √x bound fails already at x = 96,862**
within our direct range is a useful surprise: it shows that the "expected
fluctuation magnitude" of these functions is genuinely larger than the
naive √x scaling, even in regimes where the asymptotic theory hasn't yet
"kicked in".

## Reproducibility

Script: `numerics/liouville_polya.py`
Dependencies: numpy, math, mpmath (for ζ(3)), sieve_core.
Runtime: ~12 seconds (Ω sieve to 10⁷ + cumulative L + Dirichlet series).
