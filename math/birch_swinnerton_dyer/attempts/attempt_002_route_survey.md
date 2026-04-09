# Attempt 002 — Route Survey for BSD

**Date**: 2026-04-07
**Phase**: 0 → 1 (Paper Arsenal)
**Instance**: Even (Theory)

## The Landscape

BSD is unique among Millennium Problems: HALF of it is solved.
Rank 0 and 1 are proved. The wall is rank ≥ 2.

## Route Rankings (by Sigma Method fit)

### 1. Iwasawa Main Conjecture → BSD ★★★★★

**Why #1**: Most complete existing framework. The Iwasawa main conjecture
(proved by Skinner-Urban for many cases) relates Selmer groups to p-adic
L-functions. BSD follows for curves where the main conjecture is known.

**What's proved**: For E/Q with good ordinary reduction at p, and satisfying
certain technical conditions (residual representation irreducible, etc.):
the p-part of BSD holds.

**The gap**: The technical conditions exclude many curves. Extending to ALL
curves requires handling:
- Supersingular primes (Wan, Sprung have partial results)
- Reducible residual representations (Skinner 2014)
- The "full BSD" (not just p-part but the exact formula)

**Sigma Method fit**: HIGH. The framework exists, gaps are SPECIFIC and
QUANTIFIABLE. Each extension (new prime, new curve class) is a concrete theorem.

### 2. Derived Euler Systems ★★★★

**Why #2**: Loeffler-Zerbes (2020s) developed "Euler system machinery" that
systematically produces Euler systems for various motives. This AUTOMATES
part of the Kolyvagin method.

**What's proved**: New Euler systems for Rankin-Selberg convolutions,
symmetric squares, GSp(4). Each gives new cases of BSD.

**The gap**: These still only reach rank 0 and 1 (the Euler system method
has a structural limitation: it produces ONE cohomology class, which bounds
the Selmer group to rank ≤ 1).

**For rank ≥ 2**: Need MULTIPLE Euler system classes. The "higher-rank
Euler system" program (Kakde-Loeffler-Zerbes) is in development but
hasn't produced results for rank ≥ 2 yet.

### 3. Diagonal Cycles / Higher Heegner ★★★

**Why #3**: Darmon-Rotger diagonal cycles on triple products of modular
curves. These generalize Heegner points to higher-dimensional settings.

**Status**: Partial results for specific cases. The Gross-Zagier formula
has been generalized (Zhang, Yuan-Zhang-Zhang) but only for rank 1.

**The gap**: No analog of the Gross-Zagier formula for rank 2+. The
diagonal cycle gives ONE point, not two.

### 4. Computational Certification ★★★★

**Why high**: BSD is the MOST computationally testable Millennium Problem.
The LMFDB has millions of curves with:
- Proven rank (via descent)
- Computed L-values (via modular symbols)
- Verified BSD formula (numerical, to high precision)

**Sigma Method fit**: PERFECT for the Odd instance. Build an iron fortress
of verified BSD instances. Each verified curve is a certificate.

**The limitation**: Verification for individual curves doesn't prove BSD
in general. But the DATA may reveal patterns that suggest a proof.

### 5. Langlands Program ★★

**Why low**: The full Langlands program would imply BSD (as a consequence
of general motivic L-function theory). But Langlands is even HARDER than
BSD. This is the "prove a harder theorem" route.

## The Key Insight

**BSD rank 0 and 1 are proved because we have ONE construction**:
Heegner points. For rank ≥ 2, we need TWO or more independent
constructions. Nobody has them.

The analogy:
| YM | BSD |
|----|-----|
| Strong coupling (proved) | Rank 0-1 (proved) |
| Weak coupling (the gap) | Rank ≥ 2 (the gap) |
| GC bridges the gap | ??? bridges the gap |

For YM: the gradient correlation GC > 0 bridges strong to weak coupling.
For BSD: need a quantity that bridges rank 1 to rank 2.

**Candidate**: The p-adic regulator. If we could relate the p-adic regulator
to the L-function at HIGHER order vanishing, we'd have a "higher Gross-Zagier."

## Decision

**Primary**: Route 1 (Iwasawa main conjecture) — extend to more curves
**Secondary**: Route 2 (derived Euler systems) — systematize the machinery
**Computational**: Route 4 (LMFDB certification) — build iron fortress
**Speculative**: Route 3 (diagonal cycles) — the rank ≥ 2 breakthrough if it comes

## For Odd Instance

1. Download LMFDB data for elliptic curves of rank 0, 1, 2, 3
2. For each curve: verify rank, compute L^{(r)}(E,1), compare to BSD formula
3. For rank 2+: find the Ш(E) from the BSD formula. Is |Ш| always a perfect square?
4. Look for PATTERNS in rank 2+ curves that might suggest a construction
