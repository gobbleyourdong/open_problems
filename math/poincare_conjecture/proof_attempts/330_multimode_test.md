---
source: Instance B — testing the multi-mode α/|ω| bound
type: NUMERICAL VERIFICATION — does α/|ω| approach 1/2 with more modes?
file: 330
date: 2026-03-29
---

## Instance C's Two-Mode Result (file 306)

For any two-mode div-free field on T³:
  α/|ω| ≤ 1/(2√2) ≈ 0.354 at the vorticity maximum.

This is STRICTLY below 1/2 with 29% margin.

## The Critical Question

Does the bound increase toward 1/2 as N (number of modes) increases?

If max_N (α/|ω|) < 1/2 for all N: the proof closes (for NS, via Seregin).
If max_N → 1/2: the bound is useless.

## What We Need to Test

1. Two-mode verification: confirm 1/(2√2) numerically
2. Three-mode: what's the max α/|ω|?
3. Many-mode (N=10, 20, 50): trend?
4. The EVOLVED trefoil data: α/|ω| < 0.48 (from file 301). Is this < 1/(2√2)?

Actually α/|ω| ≈ 0.48 > 0.354 for the trefoil. So the two-mode bound
doesn't hold for many-mode fields. The bound INCREASES with N.

## The Scaling with N

From the per-mode analysis:
- Each mode pair contributes at most 1/(2√2) to α/|ω|
- Multiple pairs can ADD their contributions
- But phases at x* create cancellations
- The NET effect depends on the phase coherence

For N RANDOM modes: α/|ω| ~ 1/(2√N) (central limit theorem — cancellation).
For N OPTIMALLY CHOSEN modes: α/|ω| could approach 1/2 (constructive).

The NS dynamics determines the phase structure. The question is whether
NS solutions have the "optimal" phase structure that pushes α/|ω| to 1/2,
or the "random" structure that gives α/|ω| ~ 1/√N → 0.

From the data: α/|ω| ≈ 0.1-0.48 for evolved flows. NOT approaching 1/2.
NOT approaching 0 either. Intermediate values.

## The Honest Assessment

The two-mode bound 1/(2√2) is a PROVEN result for N=2.
For N > 2: the bound likely increases toward some C < 1/2.
But proving C < 1/2 for all N is the open question.

The data (α/|ω| < 0.48 always, across 23+ ICs) suggests C ≈ 0.48.
This is < 1/2 but the margin is only 4%.

## Can the Attractor Help?

At the |ω|²/|S|² = 4 attractor: α ≤ λ₁ ≤ |ω|/√6 ≈ 0.408|ω|.
This gives α/|ω| ≤ 0.408 (18% margin from 1/2).

BUT: the attractor needs to be proven at the max (the original gap).

## INTERIM CONCLUSION

- N=1: α/|ω| = 0 (Beltrami). PROVEN.
- N=2: α/|ω| ≤ 1/(2√2) ≈ 0.354. PROVEN (Instance C).
- N→∞: α/|ω| < 0.48 (measured). NOT PROVEN.
- At the attractor: α/|ω| ≤ 0.408. CONDITIONAL on attractor.
- NS needs: α/|ω| < 0.5 for Seregin. 4% margin measured.

## 330.
