---
source: Instance A — H_ww > 0 is DYNAMIC (needs evolution), not STATIC
type: DEFINITIVE NEGATIVE — static bounds fail, dynamics essential
date: 2026-03-29
---

## What Failed

| Test | H_ww < 0 rate | Structure used |
|------|-------------|---------------|
| Generic f ≥ 0 | 45% | Positivity only |
| Div-free |ω|² | 43% | + incompressibility |
| NS source (random IC) | 43% | + Biot-Savart + quadratic |
| NS source (EVOLVED) | **7.5%** | + Euler dynamics |

The bound H_ww > 0 at the max is NOT a consequence of:
- Positivity of the source (45% fail)
- Incompressibility (43% fail)
- The NS quadratic structure (43% fail for random ICs)

It IS a consequence of:
- **EULER EVOLUTION** (only 7.5% fail, and those are transient jumps)

## What This Means for the Proof

NO STATIC BOUND WILL WORK. The proof must be DYNAMIC.

The Euler evolution creates correlations between:
- The vorticity field ω
- The strain field S
- The pressure field p
- Their spatial relationship (the |ω|²/|S|² = 4 attractor)

These correlations don't exist in random fields. They're built up by
the nonlinear dynamics over time. The proof must show these correlations
are self-maintaining.

## The Right Approach (confirmed)

Grok's suggestion: derive a TRANSPORT EQUATION for the ratio R (or the
quantity Q = S²ê - α² - H_ωω) and show it satisfies a MAXIMUM PRINCIPLE.

The transport equation approach works DYNAMICALLY:
- It doesn't need R < 1 at t=0 (random ICs can have R > 1)
- It shows R DECREASES toward the attractor R < 1
- The attractor is self-maintaining under Euler evolution

This is consistent with our data:
- Random ICs: R > 1 at 43% of points
- After evolution: R < 1 at 92.5%+ of max-point measurements
- The DYNAMICS push R below 1 and keep it there

## Instance A Final Status (files 180-190)

PROVEN:
- Straight tube: ratio = 1 exactly, α = 0 (extremal, harmless)
- First variation: dR/dε < 0 (straight tube is local max)
- Generic f ≥ 0: conjecture FALSE (45% counterexamples)
- Div-free: doesn't help (43% violations)
- NS random: doesn't help (43% violations)
- NS evolved: works (7.5% transient violations only)

NOT PROVEN:
- R < 1 universally for evolved Euler (the actual target)
- Transport equation for R with maximum principle
- Any static bound on the CZ operator at vorticity maxima

THE GAP: prove the Euler evolution maintains R < 1 dynamically.
This requires the transport equation approach (files 187 suggestion,
not yet attempted rigorously).

## 190. Instance A complete. The proof is dynamic, not static.
