---
source: Peak curvature argument WRONG — μ_par << μ_perp but H_ωω > 0 anyway
type: NEGATIVE RESULT — the mechanism is NOT local peak curvature
date: 2026-03-29
---

## Data

At the max of |ω| for the trefoil:
  μ_par / μ_perp ≈ 0.01-0.13 (parallel curvature is 10-100× smaller)
  μ_par even NEGATIVE at some times

Yet: H_ωω > 0 at 80% of measurements (Q < 0 at 80%).

## What This Means

The H_ωω > 0 does NOT come from the z-curvature of the |ω|² peak.
The peak is nearly FLAT along ω (a tube is elongated along its axis).
The local peak contribution to H_zz is actually NEGATIVE (from μ_par << μ_perp).

H_ωω > 0 comes from the FAR-FIELD pressure — the contribution of
DISTANT parts of the vorticity field to the Hessian at x*.

The far-field overwhelms the (negative) local contribution by a
large margin (~4000 units to overcome the local -4000).

## The Mechanism Is Non-Local

H_ωω > 0 is a NON-LOCAL property of the evolved Euler flow.
It cannot be proven by LOCAL analysis at x* (the peak curvature
gives the wrong sign).

The non-local contribution: from the Fourier cancellation (file 171),
the 98% cancellation between shells creates a net positive H_ωω
that exceeds the negative local contribution.

## Score: 197 proof files, 14 dead approaches

| # | Approach | Status |
|---|----------|--------|
| ... | (files 1-179, see file 170) | 12 dead |
| 13 | Kelvin + core width | Dead |
| 14 | Peaked source (local) | **Dead** (μ_par << μ_perp) |
| | **Q < 0 attractor (dynamic)** | **ALIVE but unproven** |

## The Honest State

After 197 files and 14 failed analytical approaches:

The ONLY surviving proof route is the DYNAMIC one:
"The Euler evolution creates and maintains Q < 0 at vorticity maxima."

This is confirmed by numerics (100% post-transient compliance,
all ICs, all resolutions, all times). But every attempt to prove
it analytically has failed because H_ωω > 0 is a NON-LOCAL,
DYNAMIC property that can't be captured by:
- Static CZ bounds (file 189)
- Positivity arguments (file 189)
- Div-free structure (file 190)
- Peak curvature (this file)
- Eigenvalue bounds (file 194)

The proof requires understanding HOW the Euler dynamics create
the non-local pressure correlations that make H_ωω > 0.
This is the deepest level of the Millennium Prize problem.

## 197.
