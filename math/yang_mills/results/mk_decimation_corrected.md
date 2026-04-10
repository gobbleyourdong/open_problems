# MK Decimation — Tomboulis (5.15) Test CORRECTED

**Date:** 2026-04-10
**Script:** `numerics/mk_decimation.py`
**Track:** Numerical

## Bug in Diagnostic

The script reports "NO ✗" at every β, but this is a COMPARISON BUG:
the criterion `all(r > 1.0)` uses STRICT inequality, while the ratio
flows to exactly 1.0000 at steps 1-5 (the trivial fixed point).

**Corrected criterion:** `all(r ≥ 1.0)` → ALL β values pass.

## Corrected Results

Z/Z+ ratio under MK decimation for SU(2) in d=4:

| β | Step 0 | Step 1 | Steps 2-5 | Z/Z+ ≥ 1? |
|---|--------|--------|-----------|------------|
| 0.5 | 1.004 | 1.000 | 1.000 | **YES** |
| 1.0 | 1.053 | 1.000 | 1.000 | **YES** |
| 2.0 | 1.549 | 1.000 | 1.000 | **YES** |
| 2.3 | 1.796 | 1.000 | 1.000 | **YES** |
| 3.0 | 2.308 | 1.000 | 1.000 | **YES** |
| 4.0 | 2.474 | 1.001 | 1.000 | **YES** |
| 6.0 | 2.153 | 1.024 | 1.000 | **YES** |
| 8.0 | 2.030 | 1.134 | 1.000 | **YES** |

**Z/Z+ ≥ 1 at every step, every β.** Tomboulis (5.15) is preserved
under MK decimation at all tested couplings.

## Physical Interpretation

The ratio Z/Z+ measures the CENTER SYMMETRY cost:
- Z/Z+ > 1: the non-twisted sector is energetically favorable → CONFINEMENT
- Z/Z+ = 1: center symmetry is unbroken → trivial (or deconfined)
- Z/Z+ < 1: would indicate center symmetry BREAKING → deconfinement

MK decimation flows ALL couplings to the STRONG coupling fixed point
(c_j → 0 for j > 0), where Z/Z+ → 1 from above. The flow never
crosses Z/Z+ = 1 from above — confinement is preserved throughout.

## Comparison: U(1) Should BREAK at Weak Coupling

For U(1) in d=4 (which HAS a phase transition at β_c ≈ 1.01):
MK decimation also shows Z/Z+ ≥ 1 at all steps. This means MK
is NOT sensitive enough to detect the U(1) phase transition.

**MK is an APPROXIMATION** — it doesn't detect deconfinement transitions
because it coarse-grains too aggressively. The U(1) failure shows that
Z/Z+ ≥ 1 under MK is NECESSARY but NOT SUFFICIENT for confinement.

## For the Proof Route

Tomboulis (5.15) says: Z ≥ Z+ on the EXACT lattice (not under MK).
MK preserving Z/Z+ ≥ 1 is CONSISTENT with (5.15) but doesn't PROVE it.
The MK test is a sanity check, not a rigorous bound.

For a rigorous proof: need Z/Z+ ≥ 1 on the FULL lattice, not just
under the MK approximation. This requires either:
- Direct computation on small lattices (Phase 2.1)
- The plaquette positive correlation route (primary alive route)
- Extension of the cluster expansion to intermediate β
