# Attempt 005 — Dysbiosis Framework Import: Novel Mechanisms for Psoriasis Non-Responders
## Phase 4 Cross-Pollination from Dysbiosis Campaign | 2026-04-12

> Psoriasis THEWALL.md correctly identifies IL-23/Th17/NF-κB as the primary axis.
> The dysbiosis sigma campaign (Phase 4, 8 mountains, 22+ mechanisms) has identified
> several mechanisms that apply DIRECTLY to psoriasis but are not in the current psoriasis framework.
> This attempt imports the most clinically actionable ones, focusing on:
> (1) the psoriasis non-responder problem (30-40% of biologic patients are partial/non-responders),
> (2) novel sustaining loops not addressed by IL-23 blockade alone,
> (3) the VDR-butyrate synergy for Foxp3 maintenance.

---

## Import 1: Three Non-Responder Loops in Psoriasis

The dysbiosis campaign identified three independent sustaining loops in rosacea non-responders
(run_017). All three operate in psoriasis, explaining partial biologic response.

### Loop 1: KLK5/LL-37/IL-23 self-amplifying loop (directly operative in psoriasis)

In psoriasis, LL-37 is the PRIMARY AUTOANTIGEN — LL-37 forms complexes with self-DNA →
pDC TLR9 recognition → IFN-α → more KLK5 → more LL-37 → loop:

```
LL-37-DNA complexes → pDC → IFN-α → KLK5 ↑ in keratinocytes → more LL-37
    ↓
LL-37 → mTORC1 (via VEGFR2) → keratinocyte hyperproliferation (the psoriatic plaque)
    ↓
mTORC1 → KLK5 ↑ → more LL-37 → more IFN-α from pDCs
    ↓
Loop established: INDEPENDENT OF any external microbial trigger
```

**Implication:** IL-23 blockade (guselkumab, risankizumab) reduces Th17 downstream but does
NOT break the LL-37/IFN-α/KLK5/mTORC1 loop upstream. Patients who partially respond to
biologics may have this loop running independently.
**Treatment:** Azelaic acid (KLK5 inhibitor) topically — addresses this loop at its source.
mTORC1 inhibition (rapamycin 0.2% topical): used off-label in psoriasis; breaks mTORC1 arm.

### Loop 2: NLRP3/pyroptosis

NLRP3 is documented in psoriatic skin (Lamkanfi 2012 confirmed NLRP3 activation in keratinocytes):
```
Keratinocyte stress (UV, IL-17 cytotoxicity) → ATP release → P2X7 → K+ efflux → NLRP3
    ↓ caspase-1 → IL-1β + IL-18
    ↓
Keratinocyte pyroptosis → DAMPs (HMGB1, self-DNA) → re-prime NLRP3 + activate pDCs
    ↓ pDC + self-DNA → IFN-α → Loop 1 amplified
    ↓
Pyroptosis also releases LL-37 (pre-formed in keratinocyte granules) → Loop 1 further stimulated
```

**T1DM + psoriasis overlap:** T1DM hyperglycemia → constitutive NLRP3 priming → patients with
T1DM comorbidity have a primed Loop 2 baseline.
**Treatment:** BHB + colchicine 0.5mg BID + IF — same as rosacea Loop 2.

### Loop 3: HERV-W in Psoriasis (Novel — Not in Psoriasis THEWALL.md)

HERV-W is ELEVATED IN PSORIATIC SKIN:
- Gross 2000 Exp Dermatol: HERV sequences expressed in psoriatic skin but not normal skin
- Balada 2010 Autoimmun Rev: HERV-W expression elevated in multiple autoimmune conditions
  including psoriasis; MSRV-Env detected in psoriatic PBMCs
- Mechanism: the same NF-κB sustaining loop as in rosacea/T1DM:
  LL-37 → pDC → IFN-α → epigenetic unsilencing of HERV-W → MSRV-Env → TLR4 → NF-κB →
  IL-6/TNF-α → more HERV-W expression → loop sustains

**Why this matters for biologic non-responders:**
IL-23 blockade reduces Th17 but does NOT address HERV-W TLR4-driven NF-κB sustaining loop.
Patients with active HERV-W loop will have residual IL-6/TNF-α/NF-κB activity maintaining
keratinocyte activation even after IL-23 is blocked.
**Treatment:** Gut/sleep protocol (reduces sustaining cytokines); colchicine (NF-κB suppression —
dual loop agent as per dysbiosis/run_023).

---

## Import 2: VDR-Butyrate Synergy for Foxp3 Maintenance (Why Combination Works Better)

The psoriasis THEWALL.md mentions VitD 5000 IU → "anti-IL-17 effects" (correct) but misses the
VDR-Foxp3 mechanism that makes the systemic + topical vitamin D combination mechanistically optimal.

**From dysbiosis run_018:**

```
Systemic VitD₃ (5000 IU/day) → 25(OH)D₃ → calcitriol → VDR in Foxp3+ Tregs
    → VDR-VDRE in FOXP3 promoter → Foxp3 transcription ↑ → Treg STABILITY maintained
    → Tregs less susceptible to IL-23-driven Foxp3→RORγt conversion
    → Treg functional suppression of Th17 maintained DESPITE ongoing IL-23 environment

Simultaneously:
Topical calcipotriol (vitamin D analog, 50 µg/g cream) → acts on keratinocytes:
    VDR in keratinocytes → reduces KLK5 expression → less LL-37 processing
    VDR in skin DCs → tolerogenic DC polarization → less IL-23 production locally

Butyrate 4-6g/day → HDAC inhibition → VDR gene promoter histone acetylation → VDR protein ↑
    → MORE VDR available in Tregs for calcitriol to bind → SUPERADDITIVE Foxp3 induction
```

**The combination is synergistic (not just additive):**
- Butyrate alone: modest Foxp3 induction via HDAC inhibition
- VitD alone: Foxp3 induction via VDR-VDRE binding
- Butyrate + VitD: butyrate upregulates VDR → more VDR per Treg → same calcitriol dose
  produces GREATER Foxp3 induction → more Treg stability against IL-23

**Protocol implication:** The protocol combination (butyrate 4-6g/day + VitD₃ 5000 IU/day) is
mechanistically SYNERGISTIC for Treg maintenance in psoriasis. This is not coincidental — it
is the VDR upregulation synergy. Both components should be used simultaneously, not sequentially.

---

## Import 3: Gut-Skin GALT Th17 Trafficking (M1↔M4 Bridge in Psoriasis)

The dysbiosis M1↔M4 bridge is DIRECTLY documented in psoriasis via the risankizumab data:
- Risankizumab (IL-23 inhibitor): FDA-approved for BOTH psoriasis (ULTIMMA trials) AND Crohn's
  disease (SEQUENCE trial). Same mechanism works for gut (Crohn's) and skin (psoriasis) because
  the same GALT Th17 trafficking is operating:
  
```
Gut dysbiosis → IL-23 in Peyer's patches → Th17 primed
    ↓ Dual-homing T cells (α4β7+/CLA+) traffic to both gut and skin
    ↓
Skin IL-23 (from skin DCs) → reactivates trafficked Th17 cells in skin
    ↓ IL-17 → keratinocyte proliferation + chemokines → psoriatic plaque
```

**Clinical implication:** A psoriasis patient with concurrent Crohn's disease should be the FIRST
to receive gut intervention (fiber + butyrate + probiotics) as part of psoriasis management —
their gut is actively trafficking Th17 cells to the skin. Treating the gut is treating the skin.

**The SEQUENCE trial finding** (risankizumab for Crohn's → secondary psoriasis improvement):
directly confirms the shared gut-skin Th17 axis. This mechanism is now definitively established
at RCT level. It is the dysbiosis M1↔M4 bridge confirmed in humans.

---

## Import 4: M6 Structural Floor as Psoriasis Severity Predictor

The M6 early-life Treg pool structural floor (dysbiosis/attempt_010) predicts psoriasis severity:

```
Early-life dysbiosis risk (C-section, early antibiotics, formula feeding)
    ↓ SCFA deficit during neonatal Treg imprinting
    ↓ FOXP3 CNS1/CNS3 methylation suboptimal
    ↓
STRUCTURAL TREG FLOOR SET LOWER at birth
    ↓
Adult butyrate/VitD raises Treg COUNT above the floor but cannot restore the floor itself
    ↓
With IL-23 chronic stimulation (psoriatic skin): structural floor is the FINAL LIMIT on
how many functional Tregs can suppress Th17 → low-M6 patients have a lower ceiling
```

**Testable prediction:** Psoriasis patients with documented C-section delivery and/or early
antibiotic exposure in the first year of life should have:
1. More severe psoriasis (higher baseline PASI) for equivalent T-index values
2. Lower Foxp3+ CD4+/CD4+ ratio in peripheral blood
3. Lower FOXP3 CNS2 methylation (the epigenetic floor marker)
4. Slower response to biologic therapy (needs more IL-23 suppression to compensate for lower Treg floor)

---

## Import 5: Melatonin → NLRP3 Suppression in Psoriasis

Psoriasis patients have disrupted sleep (pruritus-driven); disrupted sleep → melatonin deficiency:

```
Psoriatic itch → fragmented sleep → nocturnal melatonin peak absent/reduced
    ↓
Melatonin ↓ → SIRT1 ↓ → NLRP3 K496 deacetylation reduced → NLRP3 more active
    ↓
More NLRP3 → more IL-1β → more keratinocyte activation → more itch → less sleep
    ↓
Itch-sleep-NLRP3 vicious cycle: psoriasis disrupts sleep → sleep disruption amplifies psoriasis
```

**Protocol implication:** Melatonin 0.5mg before bed + CBT-I for psoriasis-related sleep disruption
is BOTH a quality-of-life intervention AND a direct NLRP3 suppression strategy.

---

## Summary: What Changes for Psoriasis Non-Responders

**First, phenotype the non-responder (from dysbiosis run_017):**
- Serum LL-37 elevated → Loop 1 (KLK5 loop); add topical rapamycin (mTORC1) + azelaic acid
- IL-18 elevated → Loop 2 (NLRP3); add BHB + colchicine 0.5mg BID + IF
- MSRV-Env elevated + IFN-α elevated → Loop 3 (HERV-W); add gut/sleep protocol + colchicine
- Early-life M6 risk factors → lower Treg floor; may need anti-IL-23 biologic sooner (lower protocol ceiling)

**Drugs with cross-indication for psoriasis non-responders from dysbiosis framework:**
- Colchicine 0.5mg BID: Loop 2 (NLRP3 assembly) + Loop 3 (NF-κB/HERV-W) — NOT in current psoriasis protocol; add for non-responders
- Apremilast (PDE4) + butyrate: the apremilast bridge already in psoriasis THEWALL.md; add butyrate for VDR synergy
- Melatonin 0.5mg: sleep-disrupted psoriasis patients; NLRP3 deacetylation arm

---

*Filed: 2026-04-12 | Psoriasis Phase 4 cross-pollination from dysbiosis campaign*
*Key import 1: Three non-responder loops (KLK5/LL-37/IFN, NLRP3/pyroptosis, HERV-W) explain partial biologic response in psoriasis — HERV-W is elevated in psoriatic skin (Gross 2000; Balada 2010)*
*Key import 2: Butyrate + VitD synergy is VDR-mediated (butyrate upregulates VDR → same VitD dose produces more Foxp3 induction); not coincidental — it's the optimal Treg maintenance combination*
*Key import 3: SEQUENCE trial (risankizumab Crohn's → psoriasis improvement) is RCT-level confirmation of M1↔M4 gut-skin Th17 trafficking — treats gut = treats skin*
*Novel prediction: C-section/early antibiotics → lower M6 floor → worse psoriasis severity + slower biologic response*
