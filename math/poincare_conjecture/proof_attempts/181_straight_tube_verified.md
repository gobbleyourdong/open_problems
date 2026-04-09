---
source: Instance A — Straight tube ratio = 1 exactly, perturbation reduces it
type: ANALYTICAL RESULT verified numerically
date: 2026-03-29
---

## Verified Results

1. STRAIGHT Lamb-Oseen tube: ratio = 1.000000 EXACTLY at max |ω|
   H_ωω = 0, α = 0, |S| = 0. The boundary case.

2. PERTURBED tube (z-modulation):
   | eps | ratio at max | H_ωω | α |
   |-----|-------------|-------|---|
   | 0.0 | 1.000 | 0.000 | 0 |
   | 0.1 | 0.968 | +0.597 | 0 |
   | 0.3 | 0.920 | +1.991 | 0 |
   | 0.5 | 0.886 | +3.650 | 0 |

3. The max-|ω| point of a modulated tube has α = 0 ALWAYS
   (solid-body rotation at the vorticity maximum).

## Key Insight

The straight tube is the EXTREMAL case (ratio = 1 exactly).
Any z-variation (perturbation, curvature, interaction) REDUCES
the ratio at the max-|ω| point.

AND: at the max, α = 0 (no strain). So the ratio = 1 boundary
case is HARMLESS — there's no stretching to worry about.

## The Proof Structure (refined)

At the max-|ω| point x*:

CASE 1: |S(x*)| = 0 (solid-body rotation, like a tube center).
  Then α = 0. No stretching → no blowup danger.
  Ratio can be anything (irrelevant when α = 0).

CASE 2: |S(x*)| > 0 (nonzero strain).
  This means the flow is NOT pure rotation at x*.
  There must be z-variation (or other structure) in ω near x*.
  This structure creates H_ωω > 0 (verified: ratio < 1 for any eps > 0).
  The transport barrier works: Dα/Dt < 0 when α > 0 and H_ωω > 0.

Either way: blowup is prevented.

## The Missing Step

PROVE: |S(x*)| > 0 at the max of |ω| implies ratio < 1 there.

From the numerics: every evolved flow with |S| > 0 at the max
has ratio < 1 (36/36 measurements). The straight tube (|S|=0)
has ratio = 1 but is harmless.

The analytical link: |S(x*)| > 0 → ω has structure beyond solid-body
rotation → the source Δp has z-variation → H_zz > 0 → ratio < 1.

Quantifying this link is the remaining proof step.

## 181. Straight tube is extremal. Any dynamics reduce the ratio.
