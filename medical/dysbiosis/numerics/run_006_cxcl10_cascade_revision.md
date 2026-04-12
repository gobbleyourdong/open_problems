# CVB Monitoring Cascade Revision — CXCL10 Gate Reassessment
## Run 006B | Numerical Instance | 2026-04-11

> Theory phase carried forward "CXCL10 serum screen → if elevated, proceed to IFN-α2 Simoa"
> as the recommended cascade. Run 006B tests whether CXCL10 is a valid gate.
> Result: CXCL10 is a weak gate. Protocol revision required.

---

## CXCL10 in T1DM — Quantitative Assessment

| Parameter | Value | Source |
|-----------|-------|--------|
| Typical T1DM CXCL10 | ~89-99 pg/mL | Nicoletti 2002; multiple cohorts |
| Typical control CXCL10 | ~68-120 pg/mL | Same cohorts |
| Fold-increase (T1DM vs control) | 1.3-1.5× | Overlapping ranges |
| Sensitivity (>2 SD above control mean) | ~44-55% | Best published estimate |
| Validated clinical cutoff | NONE | No consensus established |

**Key limitation:** In the majority of T1DM patients (~50%), serum CXCL10 is NOT clearly elevated above control range. CXCL10 is induced by IFN-γ AND IFN-α — it is not IFN-α specific.

---

## IFN-α2 Simoa Reference Frame

| Population | IFN-α2 level | Assay |
|------------|-------------|-------|
| Healthy controls | ≤5 fg/mL | Simoa |
| Primary Sjogren's | median ~61.3 fg/mL | Simoa (Haljasmagi 2025) |
| SLE active | variable, often >20 fg/mL | Simoa |
| T1DM (expected) | low fg/mL range | Extrapolated; no published T1DM-specific Simoa cohort data |

**Gap identified:** T1DM-specific IFN-α2 Simoa values have NOT been published in large cohorts.
The only T1DM IFN-α data is:
- Bioassay (Devendra): ~10.1 U/mL (69.6% positivity in T1DM vs 0% controls)
- Gene expression (ISG panel in islets): confirmed
- Protein level in blood by Simoa: not established for T1DM specifically

---

## ISG Panel as Better Approach

**IFN-I Hyper-responsiveness (Diabetologia 2020):**
In T1DM whole blood, IFN-I hyper-responsiveness (response to ex-vivo IFN stimulus) is detectable EVEN when baseline ISG score is normal. This means:
- Resting ISG elevation is an insensitive measure for some T1DM patients
- The DYNAMIC response (how much ISGs upregulate in response to stimulation) is more informative
- This cannot be done with a simple blood draw — requires ex-vivo stimulation assay

**Best available ISG panel for resting-state measurement:**
IFN-Score-A and IFN-Score-B from 31 ISGs (Scientific Reports 2018, TaqMan):
Key genes: IFI27, IFI44L, IFIT1, RSAD2, SIGLEC1
→ IFIT1 and RSAD2 overlap with the Run 004 ISG 4-gene panel (MX1/IFIT1/OAS1/RSAD2)

**MxA protein (more IFN-α specific):**
- MxA is induced specifically by type I and type III IFN (not IFN-γ)
- More specific for IFN-α activity than CXCL10 (which responds to both IFN-γ and IFN-α)
- Serum MxA available as research assay
- Used in SLE, MS, lupus monitoring as IFN-I biomarker
- Has NOT been validated as CVB-specific indicator, but more IFN-α specific than CXCL10

---

## Revised CVB Monitoring Cascade

**Previous protocol (Run 004):**
```
CXCL10 serum screen
    ↓ if elevated
IFN-α2 Simoa (Quanterix, CLIA lab)
    ↓ if elevated
ISG 4-gene panel (MX1/IFIT1/OAS1/RSAD2) — baseline + serial
```

**Revised protocol (Run 006B):**
```
STEP 0 (baseline, any lab): CXCL10 serum
   - Interpret: if >150 pg/mL, HIGH suspicion; 100-150 pg/mL, BORDERLINE; <100 pg/mL, does NOT rule out
   - Do NOT use normal CXCL10 as a reason to skip IFN-α2 Simoa if CVB clinical context is present

STEP 1 (Quanterix or CLIA): IFN-α2 Simoa
   - Reference: healthy controls ≤5 fg/mL
   - Interpretation: T1DM-specific published norms not available; use SLE/Sjogren's as proxy
   - Any value >10-15 fg/mL in T1DM context = likely elevated (awaiting T1DM-specific cohort data)
   - This step should NOT be gated exclusively on CXCL10 if clinical suspicion is present

STEP 2 (add if IFN-α2 elevated): ISG 4-gene panel (IFIT1, RSAD2, MX1, OAS1) — blood RNA
   - Baseline expression
   - Monitor every 6 months if persistently elevated

STEP 3 (optional, if robust signal): Add MxA protein (serum, research assay)
   - More IFN-α specific than CXCL10
   - Confirms type I interferon signature vs. IFN-γ dominant inflammation
```

**Key change:** CXCL10 is now a SUPPORTIVE marker, not an exclusive gate. Normal CXCL10 does NOT justify skipping IFN-α2 Simoa if other CVB context is present (T1DM, persistent elevated ISG score in prior testing).

---

## Kill Criterion Update (Run 004 revision)

**Previous kill criterion A:** "IFN-α2 Simoa shows NO elevation in T1DM patients vs controls"

**Revised interpretation:**
- T1DM-specific Simoa cohort data doesn't yet exist → we don't know what T1DM baseline looks like
- First measurement IS the baseline for this individual
- Serial monitoring (every 6 months) is the approach: rising trend = signal; stable trend = stable
- Comparison is intra-individual (own baseline), not population reference range

---

## What This Means for User Protocol

1. **CXCL10 is cheap (~$50-100) and worth checking as a first indicator** — but a normal result does NOT exclude CVB activity.
2. **IFN-α2 Simoa should be ordered based on clinical context (T1DM + suspected CVB), not conditional on CXCL10 elevation.**
3. **MxA protein** (if available via your CLIA or research lab) is a better IFN-α confirmatory marker than repeat CXCL10.
4. **No T1DM-specific IFN-α2 Simoa population data exists yet** — the first data point becomes N=1 baseline for this case. Serial measurement every 6 months is the protocol.

---

## References

- [Nicoletti et al. 2002 — CXCL10 in T1DM (Diabetologia)](https://link.springer.com/article/10.1007/s00125-002-0879-5)
- [CXCL10/CXCR3 in T1DM review (PMC2779012)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2779012/)
- [Haljasmagi et al. 2025 — IFN-α2 Simoa in Sjogren's (EJI)](https://onlinelibrary.wiley.com/doi/10.1002/eji.70100)
- [IFN-I hyper-responsiveness in T1DM whole blood (Diabetologia 2020)](https://link.springer.com/article/10.1007/s00125-020-05179-4)
- [Two-score ISG system (Scientific Reports 2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5895784/)
- [IFN-alpha: trigger of T1DM (PMC6235162)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6235162/)

---

*Run 006B: 2026-04-11 | CXCL10 gate reassessed — weak gate (~50% sensitivity)*
*Revised cascade: CXCL10 as supportive marker; IFN-α2 Simoa based on clinical context, not CXCL10 threshold*
*Gap identified: no published T1DM-specific IFN-α2 Simoa cohort data; first measurement = N=1 baseline*
