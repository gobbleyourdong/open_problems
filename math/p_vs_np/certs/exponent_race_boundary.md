# P vs NP: The Exponent Race + Boundary Mapping

## Date: 2026-04-09

## The exponent race

For each NP-complete problem, measure the **base c** of the best-known
exponential runtime O(c^n). c = 1 would mean polynomial time (P); c > 1
means exponential (not-in-P unless c → 1 with a better algorithm).

| Problem | Best algo | c (base) | log₂ c | verdict |
|---------|----------|----------|--------|---------|
| **3-SAT α=2.0** | DPLL+UP | **1.044** | 0.063 | **≈ POLY** |
| 3-SAT α=4.27 | DPLL+UP | 1.112 | 0.153 | subexp |
| Subset Sum | brute | 1.373 | 0.458 | exp |
| Subset Sum | meet-in-middle | 1.390 | 0.475 | exp |
| 3-Coloring (dense) | backtrack | 1.459 | 0.545 | exp |
| 3-Coloring (sparse) | backtrack | 1.514 | 0.599 | hard exp |

**Closest to P**: 3-SAT below the phase transition (α = 2.0), c = 1.044.
**Farthest**: 3-Coloring on sparse graphs, c = 1.514.

### What the gap means

To prove **P ≠ NP**: show c > 1 for ALL polynomial-time algorithms on
SOME NP-complete problem.

To prove **P = NP**: find ANY algorithm with c = 1 on ANY NP-complete problem.

The measured c_best = 1.044 at α = 2.0 is tantalizing — it's almost
polynomial. But "almost" is the whole problem: the difference between
c = 1.00 (P) and c = 1.04 (exponential) is the difference between
"tractable" and "impossible at n = 1000".

## The k-SAT boundary mapping

Where exactly does "polynomial" become "exponential" as clause width k
varies? k-SAT is in P for k = 2 (resolution) and NP-complete for k ≥ 3.

| k | n=12 ratio | n=16 ratio | n=20 ratio | scaling |
|---|-----------|-----------|-----------|---------|
| 2.0 | 119 | 1,385 | 23,548 | exponential |
| 2.5 | 103 | 874 | 10,673 | exponential |
| 3.0 | 43 | 619 | 10,177 | exponential |
| 3.5 | 48 | 281 | 2,373 | ~n^7.7 |
| 4.0 | 6 | 23 | 264 | ~n^7.3 |
| 5.0 | 2 | 2 | 20 | polynomial |

**The boundary is NOT sharp at k = 3.** Instead:
- k ≤ 2: true polynomial (2-SAT is in P)
- k = 3-4: high-degree polynomial at small n (~n^7), but accelerates
- k = 2-3: exponential even at small n (this is the "hardest" range!)

The **counterintuitive finding**: k = 2.0 gives HIGHER finder/checker
ratios than k = 3.5 at n ≤ 20. Why? Because at k = 2 with high clause
density, the checker still has to verify many clauses, but the DPLL
solver happens to be inefficient on dense 2-SAT (even though 2-SAT is
in P, the constant factors are large at small n). At large n, k = 2
becomes efficient while k = 3+ stays hard.

## The "boundary number" c(k) — NS analogy

The finder/checker ratio at fixed n = 16, α = 4.0:

```
k=2.0: c(k) = 1284  ████████████████████████████████
k=2.5: c(k) = 1519  ████████████████████████████████
k=3.0: c(k) =  895  █████████████████████████████
k=3.5: c(k) =  270  ████████████████████████
k=4.0: c(k) =   55  █████████████████
k=4.5: c(k) =    9  █████████
k=5.0: c(k) =    4  ██████
```

**c(k) DECREASES as k increases** (at fixed n). This is because larger k
makes instances more constrained → easier to find satisfying assignments
(or prove unsatisfiability) via unit propagation.

### Analogy to Navier-Stokes

The `ns_blowup` campaign measures c(N) = S²ê/|ω|² (a regularity ratio)
which DECREASES with resolution N (consistent with regularity/no blowup).

Here c(k) DECREASES with k, but the MEANING is opposite:
- **NS**: c(N) → 0 means regularity (good behavior)
- **P vs NP**: c(k) → 0 as k increases means easier instances (good behavior)
- Both measure "distance from catastrophe" (blowup / intractability)

The analogy breaks down because the P vs NP question is about the
WORST CASE (does c_best → 1 for the best algorithm?), while NS is about
all initial data. But the measurement methodology — compute c as a function
of a structural parameter and look for monotone trends — is the same
Sigma Method approach.

## Subset Sum: bounded vs unbounded

Subset Sum is **pseudo-polynomial** with DP when the target value is bounded
(O(n · max_val)), but **NP-complete** when values are unbounded.

| n | max_val | DP time | brute time | DP/checker | brute/checker |
|---|---------|---------|------------|-----------|--------------|
| 12 | 100 | 27μs | 7μs | 96 | 27 |
| 12 | 10,000 | 2,615μs | 44μs | 9,774 | 163 |
| 16 | 100 | 22μs | 10μs | 80 | 35 |
| 16 | 10,000 | 11,850μs | 5,421μs | 35,217 | 16,111 |
| 20 | 100 | 17μs | 26μs | 68 | 107 |
| 20 | 10,000 | 15,278μs | 4,802μs | 40,137 | 12,614 |

**At max_val = 100**: DP is fast (pseudo-polynomial ≈ polynomial), brute
force is slow. The gap is modest.

**At max_val = 10,000**: DP is slow (pseudo-polynomial with large constant),
brute force is also slow. Both scale badly.

The NP-completeness of Subset Sum is hidden in the max_val parameter: when
max_val is polynomial in n, the problem is in P (via DP). When max_val is
exponential in n, no poly-time algorithm is known.

## Sigma Method observation

These empirical measurements quantify the P vs NP gap as **numbers**:
- c = 1.044 (closest known to P for any NPC problem)
- c = 1.514 (farthest tested)
- The k-SAT boundary ratio c(k) = 4 at k = 5 to 1519 at k = 2.5

None of these numbers PROVE P ≠ NP (that would require showing c > 1 for
ALL algorithms, not just the ones we tested). But they give a quantitative
picture of "how far from P" our best algorithms are.

The **three barriers** (relativization, natural proofs, algebrization)
explain why we can measure c but can't prove c > 1: any proof technique
that works must be non-relativizing, non-naturalizing, AND
non-algebrizing — a constraint that eliminates essentially all known
proof methods.

## Reproducibility

Scripts: `numerics/exponent_race.py`, `numerics/boundary_mapping.py`
Dependencies: numpy, random, time.
Runtime: ~30 seconds total.
