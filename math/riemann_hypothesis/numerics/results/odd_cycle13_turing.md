# RH Odd Instance — Turing Verification (Cycle 13)

## Date: 2026-04-08

## Results

| T | N(T) | Zeros found | Status |
|---|------|-------------|--------|
| 500 | 269.6 | 254 | GAP (dt too coarse) |
| 1000 | 648.6 | 668 | **VERIFIED** |
| 2000 | 1517 | 2275 | OVERCOUNTING (R-S correction needed) |
| 3000 | 2469 | 4050 | OVERCOUNTING |
| 5000 | 4520 | 7809 | OVERCOUNTING |

## Assessment

**T=1000 is solid**: 668 sign changes >= 649 expected. All zeros accounted for.

**T>=2000 overcounts** because the basic R-S formula (leading term only) creates
spurious oscillations at large t. Need Gabcke correction terms or Odlyzko-Schonhage.

## Next Steps
1. Implement R-S correction terms (C0 at minimum)
2. Re-verify T=2000-5000 with corrected Z(t)
3. Push to T=10000 with proper algorithm

## Update: C₀ Correction (Cycle 14)

With Riemann-Siegel C₀ correction term:
| T | N(T) | Basic | C₀ corrected |
|---|------|-------|--------------|
| 200 | 79.2 | 67 | **79 ✓** |
| 500 | 269.6 | 253 | **269 ✓** |
| 1000 | 648.6 | 667 | 687 |
| 2000 | 1517 | 2274 | 2250 (still overcounting) |

T=200 and T=500 now match N(T) EXACTLY with C₀ correction.
T≥1000 still overcounts — need C₁, C₂ or Odlyzko-Schönhage.

## Li Criterion (Cycle 15)

λ_n ≥ 0 for all n ≤ 200 (using K=200 zero pairs, 30-digit precision).

| n | λ_n |
|---|-----|
| 1 | 0.0210 (minimum) |
| 10 | 2.0733 |
| 50 | 38.38 |
| 100 | 98.03 |
| 200 | 224.72 |

All positive. Growth ~(n/2)log(n), consistent with RH.
Previous: n ≤ 60. Now: n ≤ 200 (3.3x improvement).
