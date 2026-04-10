# Skewes / Littlewood — Li(x) > π(x) Bias and the Famous Asymptotic Surprise

## Date: 2026-04-08

## The result

**Li(x) > π(x) for all x ≤ 10⁸** (verified directly), in agreement with
**Gauss's 1849 conjecture**. **Yet Littlewood proved (1914) the inequality
reverses infinitely often** — the first crossing is estimated at
**x ≈ 1.397 × 10³¹⁶** (Bays-Hudson 2000).

This is **the most famous example of asymptotic surprise** in mathematics:
empirical evidence to 10²⁵ shows one thing, theory proves the opposite
happens. Both are right; the "transition" just happens at an unreachable scale.

## Verification at x ≤ 10⁸

| x | π(x) | Li(x) | Li − π | (Li−π)/√x |
|---|------|-------|--------|-----------|
| 10² | 25 | 30.13 | +5.13 | +0.513 |
| 10³ | 168 | 177.61 | +9.61 | +0.304 |
| 10⁴ | 1,229 | 1,246.14 | +17.14 | +0.171 |
| 10⁵ | 9,592 | 9,629.81 | +37.81 | +0.120 |
| 10⁶ | 78,498 | 78,627.55 | +129.55 | +0.130 |
| 10⁷ | 664,579 | 664,918.41 | +339.41 | +0.107 |
| **10⁸** | **5,761,455** | **5,762,209.38** | **+754.38** | **+0.075** |

**Li(x) exceeds π(x) by ~754 at x = 10⁸**, a relative discrepancy of
**0.013%** that has persisted at every checkpoint since x = 4. The
normalized deficit (Li − π)/√x is bounded around 0.1-0.5 — well within
the RH bound O(log x) ≈ 18.

### Bays-Hudson world record (2000)

Bays and Hudson computed π(x) at 100 strategic checkpoints using Meissel-Lehmer
combinatorial methods, **verifying Li(x) > π(x) for all x ≤ 10²⁵**. This is
the maximum scale at which the inequality has been directly verified.

**Yet we KNOW it must reverse before x ≈ 1.397 × 10³¹⁶** — the gap between
"verified" and "must reverse" is 291 orders of magnitude.

## Why Li(x) > π(x): the explicit formula breakdown

Riemann's explicit formula (via Möbius inversion of J(x)) gives:
```
π(x) = Li(x) - (1/2) Li(√x) - (1/3) Li(³√x) - (1/5) Li(⁵√x) + ...
            - Σ_ρ Li(x^ρ)  + small corrections
```
where the sum is over nontrivial ζ-zeros ρ.

**The (1/2) Li(√x) term is the systematic bias source:**
- It is positive for x > 4
- It SUBTRACTS from Li(x) to give π(x)
- So π(x) is systematically LESS than Li(x) by about Li(√x)/2

### Numerical decomposition

| x | Li − π (observed) | Li(√x)/2 (leading bias) | ratio |
|---|-------------------|-------------------------|-------|
| 10⁴ | 17.14 | 15.06 | 1.14 |
| 10⁵ | 37.81 | 35.58 | 1.06 |
| 10⁶ | 129.55 | 88.80 | 1.46 |
| 10⁷ | 339.41 | 231.48 | 1.47 |
| 10⁸ | 754.38 | 623.07 | 1.21 |

**The (1/2) Li(√x) term explains 70-95% of the observed deficit.** The
remainder comes from:
1. Higher-order Möbius terms: Li(³√x), Li(⁵√x), etc. (small contribution)
2. The zero sum Σ Li(x^ρ): OSCILLATING contribution that fluctuates
3. The constant correction term -log 2

Cross-reference: the same explicit formula is verified to ~3-digit
precision at x = 10⁶ in `explicit_formula_verified.md` using 200 zeros.
That cert captures the "97% of Li-deficit" via the zero sum.

## Littlewood's theorem (1914)

> **Theorem (Littlewood 1914)**: π(x) − Li(x) changes sign infinitely often.
> Specifically, it is positive infinitely often AND negative infinitely often.

The proof goes through Riemann's explicit formula:
```
π(x) - Li(x) ≈ - (1/2) Li(√x) - Σ_ρ Li(x^ρ) + O(small)
```

The sum Σ Li(x^ρ) is **oscillating** with no consistent sign. As x grows
through specific values, the phases of x^ρ for various ρ can align to make
this sum extremely large in magnitude (positive or negative). When it
becomes large enough to exceed (1/2) Li(√x), the total
"π(x) − Li(x)" can flip sign.

Littlewood used a clever "Diophantine approximation" argument: pick x
to make many phases simultaneously favorable. The ARGUMENT shows the
existence of such x, but gives **no estimate** on its location.

### Why the bound is so astronomical

For the oscillation to overcome the (1/2) Li(√x) bias, we need the
phases of x^ρ for ρ = 1/2 + iγ_k to "line up" for many zeros simultaneously.
The number of zeros below height T is N(T) ≈ (T/2π) log T. For x of size
roughly 10³¹⁶, the relevant zeros have γ ~ 728 or so (the "Skewes height").

The required alignment is **probabilistically rare** — the chance that
many independent phases all align is exponentially small in the number
of zeros. But by Diophantine considerations there exist x where it happens,
and Littlewood found the right way to construct them.

## Historical bound progression

| Year | Bound | Author |
|------|-------|--------|
| 1933 | 10^(10^(10^34)) (assuming RH) | Skewes |
| 1955 | 10^(10^(10^963)) (unconditional) | Skewes |
| 1966 | 1.65 × 10^1165 | Lehman |
| 1987 | 6.69 × 10^370 | te Riele |
| 2000 | **1.39822 × 10^316** | **Bays-Hudson** |
| 2010 | 1.39822 × 10^316 (refined) | Saouter-Demichel |
| 2011 | 1.397 × 10^316 (best estimate) | Stoll-Demichel |

**The bound shrunk from 10^(10^(10^34)) to ~10³¹⁶ over 78 years** — a
"compression" of a triple exponential into a single one, made possible
by sharper analytic methods (Lehman's adaptive Diophantine approximation,
te Riele's improvements, Bays-Hudson's modern refinement).

**But the actual first crossing has NEVER been computed.** Even
"1.397 × 10³¹⁶" is an UPPER bound — there could be (and probably is) an
earlier crossing, but it's similarly inaccessible to direct computation.

### Why we'll never know the first crossing exactly

Computing π(x) at x = 10³¹⁶ would require:
- Storing primes up to x: impossible (more memory than atoms in the universe)
- Combinatorial methods (Meissel-Lehmer, Lagarias-Miller-Odlyzko): polynomial
  in x but with degree ~2/3, so cost ~10²¹⁰ operations — impossible
- Analytic methods (Riemann's explicit formula with computed zeros): could
  work in principle but requires ~10³¹⁶ zeros to high precision — impossible

**The first crossing exists as a definite integer, but humanity will likely
never know it.** It's an example of a "specific number" we can prove things
about (its existence, upper bounds) but cannot ever pin down precisely.

## Connection to the Dirichlet/Chebyshev bias (q=3)

In `dirichlet_chebyshev_bias.md`, we saw that for primes mod 3:
- π(x; 3, 2) > π(x; 3, 1) for all x ≤ 10⁷
- First crossing at x ≈ 6.09 × 10¹¹ (Bays-Hudson 1978)

This is **the same phenomenon at smaller scale**:
- A "main bias" (here, more QNR primes than QR primes mod 3)
- An "oscillating sum" over Dirichlet L-function zeros
- A first crossing far beyond any natural verification range

**Skewes/Littlewood is the unrestricted version** (all primes vs Li).
**Chebyshev bias is the modular version** (primes in different residue
classes). Both follow the same explicit-formula machinery.

## What this teaches us

1. **Empirical evidence is not proof.** Verification to 10²⁵ doesn't
   imply truth at 10³¹⁶. In analytic number theory, "asymptotic" can
   mean "after waiting for ages."

2. **Specific numbers can be both well-defined and unreachable.** The
   first crossing is a real integer; its existence is provable; but its
   value is forever unknown.

3. **The explicit formula is the key analytic tool.** Both Littlewood's
   theorem and the bound improvements come from increasingly skilled
   manipulation of Riemann's explicit formula.

4. **Hardy's quote**: When Skewes showed his 1933 bound, Hardy joked
   it was "the largest number which has ever served any definite purpose
   in mathematics." The number has since been "shrunk" enormously, but
   the spirit of the quote remains: **giant numbers can have meaningful
   meaning**.

## Sigma Method observation

This cert is the campaign's **canonical "asymptotic surprise"** — the
empirical evidence is overwhelming and consistent (Li(x) > π(x) at every
checkpoint to 10²⁵), yet the theoretical truth is the opposite (it
reverses infinitely often).

The **Sigma Method counter-lesson**: empirical verification across many
orders of magnitude is NECESSARY but NOT SUFFICIENT for confidence in a
mathematical statement. The Skewes phenomenon shows that 25 orders of
magnitude of agreement can still be wrong about the asymptotic behavior.

The **right epistemology**: empirical agreement + theoretical understanding
of WHY the asymptotic might (or might not) hold. For Li(x) > π(x), we have
the empirical agreement AND the theoretical proof of eventual failure —
both are true facts about the same mathematical object at different scales.

## Reproducibility

Script: `numerics/skewes_littlewood.py`
Dependencies: numpy, mpmath (high-precision Li), math, sieve_core.
Runtime: ~6 seconds (sieve to 10⁸ + cumulative π + Li at multiple scales).
