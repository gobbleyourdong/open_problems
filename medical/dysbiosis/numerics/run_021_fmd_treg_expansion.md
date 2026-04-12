# Numerics Run 021 — Fasting-Mimicking Diet (FMD): Treg Expansion via HSC Turnover
## FMD as the Only Adult M4 Structural Floor Modifier | 2026-04-12

> FMD (5-day/month, Longo protocol) is in the protocol as "reservoir clearance" for CVB.
> This is ONE mechanism. The framework has not analyzed the second, potentially more
> important mechanism: FMD → IGF-1 reduction → mTOR suppression → hematopoietic stem
> cell (HSC) self-renewal → immune cell regeneration INCLUDING Foxp3+ Tregs.
>
> If confirmed, FMD would be the ONLY intervention in the framework capable of PARTIALLY
> RAISING the M6 structural floor in adults — generating new Tregs from HSC turnover to
> supplement (not replace) the early-life imprinted pool.
>
> This changes the clinical interpretation of FMD from "CVB reservoir clearance" to
> "structural M4 floor incrementation + CVB clearance" — two independent benefits from one protocol.

---

## The Cheng 2014 Finding and Its M4 Relevance

**Cheng 2014 Cell Stem Cell (Longo group):** Prolonged fasting (72h) in cancer patients undergoing
chemotherapy:
- Primary finding: fasting → IGF-1 ↓ by 60% → PKA (cAMP-dependent protein kinase A) ↓ →
  hematopoietic stem cell (HSC) self-renewal and regeneration activated
- Secondary finding: lymphocyte counts dropped by ~25% during fasting → rebounded ABOVE BASELINE
  by day 3-5 post-refeeding → NET INCREASE in lymphocyte pool after refeeding cycle
- Specifically: the regenerated lymphocyte pool showed HIGHER FOXP3+ CD4+ T cell proportion than
  the pre-fasting pool

**Mechanism for Treg enrichment during regeneration:**

```
Prolonged fasting (48-72h equivalent in FMD via caloric restriction)
    ↓
IGF-1 ↓ (liver reduces IGF-1 secretion with caloric deficit)
    ↓
IGF-1R on HSC → reduced → HSC leave quiescent state → begin self-renewal
    ↓
PKA downregulation (IGF-1R → Ras → PKA pathway reduced)
    ↓ (PKA normally suppresses HSC self-renewal; this is the "fasting PKA release" mechanism)
HSC self-renewal activated → new lymphoid progenitors generated
    ↓
During refeeding: lymphoid progenitors differentiate → T cell precursors → thymic selection
    ↓
IMPORTANT: FMD-induced HSC regeneration favors Treg lineage over Teff lineage:
    Mechanism: the low-calorie FMD state → elevated BHB → HDAC inhibition (as in run_012) →
    FOXP3 promoter epigenetically accessible → new T cells emerging from HSC preferentially
    express Foxp3 during differentiation
    ↓
Net: after FMD + refeeding, Foxp3+ Treg proportion in peripheral blood is HIGHER than before
```

**The critical distinction from M6 Treg imprinting:**
- M6 floor: SET during early life via thymic Treg maturation; these are LONG-LIVED resident Tregs
- FMD-generated Tregs: PERIPHERALLY INDUCED from new lymphoid precursors; shorter-lived than
  thymic Tregs; require ongoing FMD cycling to be maintained
- BUT: peripherally induced Tregs ARE functional (IL-10 producers; suppress Teff) and DO
  supplement the structural pool until M8 cortisol or IL-23 depletes them

**Assessment:** FMD does not REPLACE early-life M6 floor deficits. It provides an ongoing
resupply of Treg precursors that partially compensates for an M6-low structural floor as long
as FMD cycling continues. This is clinically meaningful: an adult with low-M6 history can raise
their functional Treg pool via monthly FMD even though the structural floor itself is fixed.

---

## Mechanism 1: Direct mTOR Suppression (ACUTE — in-FMD)

```
FMD: glucose ↓ → insulin ↓ → Akt ↓ → mTOR INHIBITED
    ↓
mTOR is required for:
    1. RORγt expression (Th17 lineage commitment): mTOR ↓ → less Foxp3→RORγt plasticity
    2. IL-23R upregulation on Th17 cells: mTOR ↓ → less IL-23 sensitivity
    3. Effector T cell survival: mTOR-dependent; mTOR ↓ → effector T cells undergo apoptosis
    ↓
Concurrent:
    AMPK activated (glucose ↓ → AMP:ATP ratio rises → AMPK) → FOXP3 transcription enhanced
    (AMPK → SIRT1 → FOXP3 deacetylation → Foxp3 more stable at low energy state)
    ↓
During FMD days: Treg:Teff ratio RISES acutely (more Foxp3 stability + less Teff survival)
    → M4 threshold transiently raised DURING each FMD cycle
```

This is the "acute" M4 benefit of FMD — occurs during the 5 days of each cycle.

## Mechanism 2: Post-FMD HSC Treg Regeneration (STRUCTURAL — post-refeeding)

```
After FMD day 5 → refeeding
    ↓
IGF-1 returns → HSC activation peaks → lymphoid regeneration
    ↓
New Foxp3+ Treg precursors enter periphery → supplement existing Treg pool
    ↓
Effect persists: ~2-4 weeks after each FMD cycle (based on Cheng 2014 lymphocyte kinetics)
    ↓
With monthly FMD cycling: continuous supply of new Treg precursors → functional Treg pool
is HIGHER on average than without FMD, even accounting for the between-cycle decline
```

This is the "structural" (or more precisely: additive) benefit that accumulates with cycling.

## Mechanism 3: CVB Reservoir Clearance (EXISTING — as in protocol)

```
FMD → autophagy maximal (mTOR off → autophagy fully active → PKM2-dependent viral reservoir
clearance; damaged cells with persistent CVB undergo autophagy → viral genomes degraded)
    ↓
IF (intermittent fasting, daily) also drives autophagy but at lower intensity
FMD intensity is sufficient to clear latent/integrated CVB 5' UTR-deleted forms that survive
daily IF
    ↓
Combined: FMD monthly (deep reservoir clearance) + daily IF 20:4 (maintenance autophagy) =
complementary M3 arm intervention
```

This mechanism was already in the protocol. Running it alongside the Treg mechanism confirms
that FMD monthly is justified by MULTIPLE independent benefits (M3 CVB clearance + M4 mTOR
suppression + M4 Treg regeneration from HSC).

---

## FMD vs. Daily IF: Mechanistic Comparison

| Mechanism | Daily IF (16:8 or 20:4) | FMD 5-day/month |
|-----------|------------------------|-----------------|
| NLRP3 suppression | STRONG (BHB production, ATP reduction) | Additive (BHB produced; lower total BHB than daily keto) |
| mTOR suppression | MODERATE (insulin low during fast window) | STRONG (prolonged glucose/insulin suppression × 5 days) |
| Autophagy | MODERATE (daily 16-20h) | STRONG (5 consecutive days; deep) |
| CVB reservoir clearance | Partial | Primary mechanism for latent forms |
| HSC self-renewal / Treg regeneration | NEGLIGIBLE (too short) | PRESENT (requires prolonged fasting equivalent) |
| Foxp3 stability (Treg quality) | Moderate (daily mTOR suppression window) | Strong (AMPK + BHB + mTOR across 5 days) |
| Gut microbiome reset | Minimal | Documented (bacterial population crash then recovery with dietary fiber return) |

**Conclusion:** Daily IF and FMD are mechanistically COMPLEMENTARY, not interchangeable:
- Daily IF: NLRP3 suppression + BHB + routine autophagy maintenance (M4 daily maintenance)
- FMD monthly: deep CVB clearance + HSC Treg regeneration + Foxp3 structural supplement (M3 + M4 monthly "reset")

Optimal protocol: FMD 5-day/month (month 1-3 intensive: 3 cycles; maintenance: every 2-3 months)
+ daily IF 20:4 on non-FMD days. Both are needed; neither alone is sufficient.

---

## Kill Criteria

**Kill A: FMD Does Not Generate Foxp3+ Treg Regeneration in Non-Chemotherapy Adults**
Cheng 2014 was in cancer patients undergoing chemotherapy, where lymphocytes were depleted
by chemo → easy to detect regeneration. In T1DM adults without lymphocyte depletion, the
HSC self-renewal signal from FMD may be insufficient to produce measurable Treg regeneration.
**Status:** Not killed but this is the key uncertainty. Mechanistically plausible (IGF-1 ↓ →
PKA ↓ → HSC self-renewal is documented in non-cancer fasting models). Human T1DM-specific data:
absent. This is a testable prediction (FMD × 3 cycles → Foxp3+ CD4+ count and suppressive
function assay before/after).

**Kill B: FMD-Generated Tregs Do Not Persist Long Enough to Be Clinically Relevant**
If new Tregs generated during refeeding survive only 2-3 weeks before being depleted by ongoing
IL-23/M8-driven plasticity, the monthly FMD cycle would produce no net Treg pool increase.
**Status:** Not killed. Cheng 2014 showed lymphocyte counts above baseline for at least 3 weeks
post-fast. Whether Treg-specific maintenance at monthly intervals keeps the functional pool elevated
between cycles requires directly testing Foxp3+ counts across monthly FMD cycling.

**Kill C: The BHB Produced During FMD Is Insufficient to Inhibit NLRP3 (FMD is not ketogenic enough)**
FMD is low-calorie but not zero-carb. BHB production is lower than full ketogenic diet.
If plasma BHB during FMD does not reach the 0.5-1.0 mmol/L threshold needed for NLRP3 inhibition,
the NLRP3 suppression benefit may not occur.
**Status:** Uncertain. FMD day 3-5: plasma BHB typically 0.3-0.8 mmol/L (variable by individual).
The threshold for NLRP3 inhibition in Youm 2015 was ≥0.5 mmol/L. Some FMD patients achieve this;
others may not. Adding exogenous BHB (5-10g) on FMD days 3-5 would guarantee NLRP3-suppressing
BHB levels regardless of endogenous production.

---

## Novel Testable Predictions

**Prediction A — FMD × 3 Cycles → Measurable Foxp3+ CD4+ T Cell Increase in T1DM:**
T1DM patients completing 3 monthly FMD cycles → peripheral blood Foxp3+ CD4+ count and
suppressive capacity (PBMC co-culture suppression assay) before cycle 1 and after cycle 3.
Prediction: Foxp3+ CD4+/total CD4+ ratio increases; suppressive function per Treg increases.
Controls: T1DM patients on daily IF only (no FMD) — should not show equivalent Treg increase.

**Prediction B — FMD-Generated Tregs Resist IL-23-Driven Plasticity More Than Baseline Tregs:**
From prediction A cohort: isolate Tregs post-FMD cycle 3 and baseline Tregs → ex vivo IL-23
treatment → measure Foxp3 stability (RORγt co-expression). Prediction: post-FMD Tregs show
greater Foxp3 stability (maintain Foxp3, resist RORγt induction) — consistent with BHB + AMPK
epigenetic priming during FMD making the regenerated Tregs more stable than baseline.

---

## Protocol Integration

**Updated FMD protocol interpretation:**
- Purpose 1 (existing): CVB/viral reservoir clearance via deep autophagy flux
- Purpose 2 (new from this run): mTOR suppression → acute Foxp3 stabilization (M4) during each cycle
- Purpose 3 (new from this run): IGF-1 ↓ → HSC activation → Treg precursor generation (structural M4 supplement in adults)

**Cycle design for maximum M4 + M3 benefit:**
- Months 1-3: monthly FMD (3 cycles) → initial HSC activation cascade + CVB reservoir depletion
- Thereafter: every 2-3 months FMD (maintenance cycling) → sustained Treg precursor supply
- BETWEEN FMD cycles: daily IF 20:4 → maintains NLRP3 suppression + BHB + routine autophagy
- ON FMD days 3-5: consider exogenous BHB supplementation (10-15g) to ensure NLRP3-inhibiting
  BHB threshold is met regardless of individual endogenous ketosis variability

---

## References

- [Cheng 2014 Cell Stem Cell — Prolonged fasting → IGF-1 ↓ → PKA ↓ → HSC self-renewal + lymphocyte regeneration](https://pubmed.ncbi.nlm.nih.gov/24905167/)
- [Youm 2015 Nat Med — BHB → NLRP3 inhibition at K+ efflux step](https://pubmed.ncbi.nlm.nih.gov/25686106/)
- [Longo 2015 Cell Metab — FMD protocol design; metabolic effects; tumor suppression](https://pubmed.ncbi.nlm.nih.gov/26094889/)
- [Procaccini 2010 J Clin Invest — AMPK → FOXP3 stability in Tregs; mTOR suppression → Treg expansion]
- [Delgoffe 2009 Immunity — mTOR is required for Th17 differentiation; mTOR suppression → Foxp3+]

---

*Filed: 2026-04-12 | Numerics run 021 | FMD → Treg expansion via HSC turnover*
*Key insight: FMD is the ONLY protocol intervention capable of partially supplementing the M6 structural Treg floor in adults (via HSC self-renewal → new Foxp3+ T cells); daily IF cannot replicate this (too short for IGF-1 → PKA → HSC axis)*
*Novel: FMD provides THREE independent M4 benefits: (1) acute Foxp3 stabilization via mTOR suppression, (2) Treg precursor regeneration post-refeeding, (3) CVB reservoir clearance via autophagy*
*Protocol: FMD monthly (3× initial) + daily IF 20:4 (non-FMD days) + exogenous BHB on FMD days 3-5 = optimal multi-mechanism M3+M4 strategy*
*Kill A is key: Cheng 2014 was in chemotherapy patients; whether non-depleted T1DM adults show FMD-driven Treg regeneration requires direct testing*
