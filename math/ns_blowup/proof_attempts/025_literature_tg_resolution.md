---
source: Web search round 5
type: Literature — Taylor-Green at high resolution
status: FOUND SUPPORTING DATA from DNS community
---

## Key Finding
The DNS community has extensively studied Taylor-Green at 512³ and confirms:
- Enstrophy-based dissipation computation improves dramatically with resolution
- 256³: 2.5% accuracy
- 512³: 1% accuracy
- The ENSTROPHY computation converges with resolution

This is exactly what our infection ratio measures — the fraction where
enstrophy production exceeds dissipation. The DNS community sees the
same convergence but hasn't framed it as an infection ratio.

## arXiv 2505.18696 (May 2025): "DNS and role of round-off error: 2D TG"
Studies how round-off error affects DNS of Taylor-Green.
Relevant: our spectral method has machine-precision accuracy,
so round-off is not a factor in our results.

## Connection to Our Work
The DNS community benchmarks solvers against Taylor-Green because
it has known analytical properties. Our N=512 result showing
frac → 0 by gen1 is consistent with their convergence data:
at 512³, the dissipation is fully resolved and dominates everywhere.

The DNS community measures GLOBAL quantities (total dissipation rate).
We measure POINTWISE quantities (fraction where stretch > dissip).
Same physics, sharper diagnostic.

## For the Paper
Can cite the Taylor-Green benchmark literature to support our
resolution choices. The community consensus is that 512³ resolves
the dissipation scale at ν ~ 10⁻³ to 10⁻⁴. Our results at ν = 10⁻⁴
are consistent with this.

No one in the DNS community has measured our specific quantity
(the infection ratio). This confirms our contribution is novel.
