# REQ-006 Results: Autophagy Kinetics — TD Mutant Clearance

**Script**: `me_cfs/numerics/autophagy_kinetics/autophagy_model.py`
**Date**: 2026-04-08

## Key Findings

### 1. Autophagy Activation Kinetics

| Marker | Timeline |
|--------|----------|
| AMPK activation (t½) | 3h after fasting onset |
| ULK1 phosphorylation | +4.5h delay after AMPK |
| LC3-II/I peak | 18h (5-day FMD); 14h (24h fast) |
| mTOR suppression onset | 5h; maximal at 15h |
| Peak LC3-II/I ratio | 4.46 (FMD), 3.98 (24h fast), 1.76 (16:8 TRE) |

### 2. TD Mutant Load at Quarterly Intervals (normalized, 1.0 = baseline)

| Protocol | 3 months | 6 months | 9 months | 12 months |
|----------|----------|----------|----------|-----------|
| No fasting | 0.723 | 0.523 | 0.377 | 0.272 |
| 16:8 TRE (daily) | 0.656 | 0.430 | 0.281 | 0.184 |
| 24h fast (weekly) | 0.679 | 0.461 | 0.311 | 0.211 |
| 5-day FMD (monthly) | 0.679 | 0.460 | 0.314 | 0.214 |

### 3. FMD Frequency Scan: Thresholds for 50% and 90% Reduction

| FMD interval | 12-month load | Outcome |
|-------------|--------------|---------|
| Every 7 days | 0.096 | 90% reduction achieved |
| Every 10 days | 0.130 | 50% reduction achieved |
| Every 14–90 days | 0.16–0.26 | 50% reduction |

**Conclusion**: Weekly 5-day FMD is required for 90% TD mutant reduction in 12 months. Monthly FMD provides only ~78% reduction (0.214 remaining). Daily 16:8 TRE actually outperforms weekly 24h and monthly FMD because it provides sustained mild autophagy activation for 7% more time at above-baseline LC3 levels.

### 4. ME/CFS Energy Safety During Fasting

| ME/CFS severity | Mitochondrial deficit | Safe fasting duration |
|----------------|----------------------|----------------------|
| Mild | 30% | >120h (full 5-day FMD safe) |
| Moderate | 40% | >120h (full 5-day FMD safe) |
| Severe | 50% | ~9.8h (only TRE safe; no 24h fast) |

**Critical finding**: Severe ME/CFS patients (50% mitochondrial deficit) have PEM risk exceeding 20% threshold after only ~10 hours of fasting. For these patients, 16:8 TRE (8h effective fast after overnight) is the only safe autophagy protocol.

### 5. TRE vs FMD Assessment

- **16:8 TRE**: Peak LC3-II/I = 1.76 (mild, 3.5× below FMD peak). Only 50% enhancement above baseline.
- **5-day FMD**: Peak LC3-II/I = 4.46 (9× baseline). Sustained peak autophagy for 3-4 days.
- **Practical implication**: Daily TRE provides better TD clearance than monthly FMD due to time-integrated autophagy flux, despite lower peak intensity.

## Figures Generated

1. `fig1_autophagy_kinetics.png` — AMPK, ULK1, LC3-II/I, mTOR over 120h fast
2. `fig2_td_clearance_protocols.png` — 12-month simulation all protocols
3. `fig3_quarterly_breakdown.png` — Bar chart 3/6/9/12 month endpoints
4. `fig4_fmd_frequency_scan.png` — FMD interval vs 12-month load
5. `fig5_mecfs_pem_safety.png` — ATP and PEM risk by ME/CFS severity

## Protocol Recommendation

For moderate ME/CFS (40% mitochondrial deficit):
- **Primary**: Daily 16:8 TRE (safe, provides 1.76× LC3 peak, 82% load reduction at 12mo)
- **Monthly**: Add one 5-day FMD cycle when energy permits (no PEM risk at 40% deficit)
- **Avoid**: Weekly 24h fast (same clearance as monthly FMD but more energy-depleting per week)
