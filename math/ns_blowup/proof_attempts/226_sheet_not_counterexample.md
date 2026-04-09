---
source: Instance B — The sheet is NOT a counterexample when ê = ω direction
range: 226
type: CORRECTION — R measured along ω is ≤ 1 even for sheets
date: 2026-03-29
---

## The Correction

File 225 found R = 2 for a flat sheet with ê = z (the thin direction).
But for NS: ê = ω/|ω| (the VORTICITY direction), not the thin direction.

For a vortex sheet: ω is TANGENT to the sheet (in the y-direction).
The thin direction is z. ê = ŷ ≠ ẑ.

R along ŷ (the ω direction): R = 0 for a pure sheet, R = 0.53 for perturbed.
R along ẑ (the thin direction): R = 2 (but this is NOT the NS ê).

## The Physical Reason

For NS: ê = ω/|ω| is always tangent to vortex structures.
- Tube: ê along the tube axis → H is measured along the tube → R = 1
- Sheet: ê tangent to the sheet → H is measured IN the sheet → R = 0

The worst case (R = 1) is the TUBE, not the sheet.
The sheet has R = 0 along ω because the source is isotropic in the sheet plane.

## Data

| IC | ê direction | R |
|----|------------|---|
| Pure sheet | ê = ω (tangent) | 0.00 |
| Perturbed sheet | ê = ω | 0.53 |
| Straight tube | ê = ω (axis) | 1.00 |
| Evolved trefoil | ê = ω | 0.84 |

The tube IS the worst case. The sheet is actually the BEST case.

## Implication for the Proof

The R ≤ 1 bound, when measured along ê = ω/|ω|, may be a UNIVERSAL
property after all. The sheet "counterexample" was measuring a
non-physical direction.

The tube (R = 1) is the extremal because ω is parallel to the axis
of the tube, and the Hessian along the axis is maximally anisotropic.
For any OTHER geometry, ω is tangent to a surface that provides
additional isotropy → R < 1.

## Revised Statement

CONJECTURE: For any div-free ω on T³, at any point x* where |ω| = ||ω||∞:

  |ê·H_dev·ê|/(Δp/3) ≤ 1  where ê = ω/|ω|

with equality iff ω is locally a straight tube (ê-independent source).

This uses: ê is the VORTICITY direction (not arbitrary).
Instance A's proof (file 267, 188) targets exactly this statement.

## 226 — The sheet is NOT a counterexample. R ≤ 1 along ω may be universal.
