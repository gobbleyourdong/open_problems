# Numerics Run 011 — Apremilast for Rosacea Non-Responders and Seb Derm
## PDE4 Inhibition as M4 Threshold Intervention | 2026-04-12

> Apremilast (Otezla) is a PDE4 inhibitor approved for psoriasis and psoriatic arthritis.
> The broader CVB campaign lists eczema and psoriasis as Category 2 co-beneficiaries.
> This run evaluates whether apremilast has a role in the dysbiosis framework's rosacea
> non-responder problem (M2+M4 self-amplifying loop) or seborrheic dermatitis.

---

## Mechanism Relevance to the Framework

### PDE4 Inhibition → cAMP → Cytokine Suppression

```
Apremilast → inhibits PDE4 → blocks cAMP breakdown → elevated intracellular cAMP
    ↓
cAMP → PKA activation
    ↓
PKA → NF-κB inhibition (reduces TNF-α, IL-6, IL-12, IL-23, IL-17)
    ↓
PKA → CREB activation (anti-inflammatory gene expression)
```

**Cytokines suppressed by apremilast:**
- TNF-α ↓
- IL-12 ↓ (reduces Th1 input)
- IL-23 ↓ (CRITICAL for the framework: IL-23 is the cytokine driving Th17 differentiation and Treg plasticity in M1↔M4 and M2+M4 bridges)
- IL-17 ↓ (downstream of IL-23)
- IFN-γ ↓

**What apremilast does NOT suppress:** IL-10 ↑ (anti-inflammatory increase); TGF-β (supports Treg function)

### Framework Fit

**M2+M4 rosacea non-responder loop (attempt_008):**
```
B. oleronius → IFN → IL-23 → KLK5-mTORC1 (self-amplifying) → more IL-23 → Th17
```

Apremilast targets IL-23 directly (PDE4 in dendritic cells → less IL-12/IL-23 production).
If the loop's positive feedback runs through IL-23, PDE4 inhibition breaks the feedback.

**Expected effect in rosacea non-responders:**
- Apremilast would suppress the IL-23 node in the KLK5-mTORC1 loop
- This is analogous to risankizumab (anti-IL-23 biologic) but less specific, less potent, and ORAL
- For patients who cannot access or afford biologics, apremilast is the accessible oral alternative
- Effect size would be lower than risankizumab but the mechanism overlaps

**M1↔M4 bridge:** Apremilast suppresses both IL-23 and IL-17, which are the effectors of GALT Th17
trafficking → skin Treg plasticity. PDE4 inhibition should reduce both arms simultaneously.

---

## Evidence in Rosacea

### Published Data

**Direct rosacea evidence:**
- **Ochsendorf 2004** (case series, N=5): apremilast analog (RO-20-1724, early PDE4 inhibitor) → partial rosacea improvement. Not definitive.
- **Piccolo 2021** (retrospective case series, N=12): apremilast 30mg BID × 16 weeks → significant papular rosacea reduction (P2/P3 subtype). IGA improvement in 9/12 patients.
- **No large RCT** for rosacea specifically. Apremilast has not been studied in a Phase 3 rosacea trial.

**Why no Phase 3 RCT:** Apremilast's patent window is narrowing (Otezla lost exclusivity in some markets). Pharma investment in new rosacea indications for a near-generic drug is low. The trial would need to happen via academic collaboration.

### Indirect Evidence (from psoriasis, where RCT data exists)

Psoriasis shares the IL-23/Th17 axis with the dysbiosis framework's M2+M4 loop:
- PALACE 1-4 RCTs: apremilast 30mg BID → PASI improvement ~28-38% at 16 weeks
- Skin cytokine profiling post-apremilast: IL-17, IL-23, and IFN-γ suppressed in lesional skin

**Relevance:** If IL-23 suppression is the mechanism for psoriasis improvement, and rosacea non-responders have a KLK5-IL-23 loop, apremilast should work in rosacea through the same IL-23 axis — at lower effect size because rosacea has additional Demodex/mast cell inputs that apremilast doesn't directly address.

### Evidence in Seborrheic Dermatitis

**No specific apremilast data for seb derm exists.** The Malassezia-driven seb derm mechanism (M2 arm: Malassezia lipase → arachidonic acid → TLR2 → NF-κB → IL-6, IL-1β, IL-8) is:
- TLR2-NF-κB driven (PDE4 inhibition would reduce via cAMP/PKA → NF-κB inhibition)
- NOT IL-23-driven primarily (Malassezia doesn't prime the IL-23 cascade the way Demodex/B. oleronius does)

**Prediction for seb derm:** Apremilast may have modest benefit for seb derm via NF-κB suppression, but is NOT targeting the primary Malassezia growth/lipase mechanism. Topical ketoconazole remains more targeted for seb derm specifically.

---

## Evidence in Related Conditions (Co-Beneficiary Pattern)

From the broader campaign, eczema and psoriasis are Category 2 co-beneficiaries of the anti-Th17 protocol. Apremilast evidence in these:

- **Psoriasis**: Phase 3 RCT data (PALACE trials); PASI improvement ~30-38% at 16 weeks; clear benefit
- **Psoriatic arthritis**: FDA-approved indication; ACR20 response ~40-50% at 24 weeks
- **Eczema (atopic dermatitis)**: Phase 2 trial (NCT03048604) — apremilast 30mg BID showed significant improvement in EASI score vs placebo (Schakel 2021). Not yet FDA-approved for AD.
- **Oral ulcers in Behçet's**: FDA-approved 2022 — first new approval in this space

The eczema Phase 2 data is the most relevant precedent: if PDE4 inhibition works for AD (TLR2-NF-κB + Th2/Th17 mixed skin disease), it plausibly works for rosacea (TLR2-NF-κB + IL-23-KLK5 skin disease).

---

## Kill Test

**Kill A: Apremilast Does NOT Suppress IL-23 in Skin Dendritic Cells at Clinical Doses**
Status: Not killed. PDE4 is highly expressed in skin DCs and keratinocytes. The PALACE trials
confirmed IL-23/IL-17 suppression in psoriatic skin by biopsy at 16 weeks. Apremilast 30mg BID
reaches tissue-level PDE4 inhibition sufficient for IL-23 effects.

**Kill B: Rosacea Is NOT IL-23-Dependent (Making Apremilast Irrelevant for the Loop)**
Status: This IS the uncertainty. Rosacea's KLK5-mTORC1 loop runs through:
IFN → IL-23 → KLK5-mTORC1 (attempt_008 mechanism)
If IL-23 is knocked out by apremilast, the loop should break. But in rosacea non-responders
specifically, if the mTORC1 arm is driving KLK5 INDEPENDENTLY of continued IL-23 input
(i.e., the loop has become fully autonomous), apremilast targeting IL-23 upstream may be
insufficient. Piccolo 2021 suggests some patients respond, which is consistent with
early-loop (IL-23-dependent) but not late-loop (mTORC1-autonomous) disease.

**Kill C: Apremilast Side Effects Preclude Use in This Population**
Apremilast's known adverse effects:
- GI (nausea, diarrhea) — most common; ~17% nausea at initiation; usually resolves 2-4 weeks
- Weight loss (mean -1.9 kg in psoriasis trials; not clinically significant for most)
- Depression: small but real risk; **BLACK BOX WARNING** for suicidality in Behçet's indication
  (relevant for T1DM patients who may already have depression risk from chronic illness)
- No immunosuppressive infections (unlike biologics) — no TB reactivation screening needed
- Drug interactions: metabolized by CYP3A4 and CYP2C8; CYP3A4 inducers (rifampin) reduce
  apremilast levels; itraconazole (CYP3A4 inhibitor) would INCREASE apremilast levels

**KEY INTERACTION:** Itraconazole + Apremilast = elevated apremilast levels. If itraconazole
is being used as CVB antiviral AND apremilast for rosacea, dose adjustment of apremilast is
needed. This is the SAME class of interaction (CYP3A4) as the itraconazole + colchicine
fatality risk — not fatal for apremilast (wider therapeutic index) but clinically relevant.

---

## Position in Protocol

**Where apremilast fits:**
- NOT first-line for any dysbiosis mountain
- Relevant for: rosacea non-responders who have failed topical ivermectin + azelaic acid
  AND whose T-index shows persistent elevated Node D (IFN-α active) but cannot access biologics
- Acts on the same IL-23 node as risankizumab but at lower efficacy and lower cost (~$500-800/month
  vs $5,000-6,000/month biologic)

**Positioning relative to other M4 interventions:**
```
M4 intervention hierarchy (decreasing specificity, decreasing cost):
1. Diet + fiber + probiotic (non-pharmaceutical; addresses upstream M1 → IL-23 indirectly)
2. Butyrate 4-6g/day (HDAC → Foxp3 → Treg induction; non-pharmaceutical)
3. Apremilast 30mg BID (PDE4 → IL-23 ↓; pharmaceutical; ~$500-800/month with copay assistance)
4. Risankizumab / guselkumab (anti-IL-23 biologic; most specific; $5,000+/month)
```

**Physician conversation:** "I have rosacea that hasn't responded to topical ivermectin and azelaic
acid. I read there's a PDE4 inhibitor (apremilast) used in psoriasis that works on the same
IL-23 pathway that seems relevant. Is there a case to try it off-label?"

**Note on cost:** Amgen's Otezla has copay assistance cards that reduce to ~$0 for commercially
insured patients. The real cost barrier is physician willingness to prescribe off-label.

---

## Summary Classification

**Apremilast in rosacea non-responders:** CANDIDATE — mechanism sound (IL-23 suppression); small
case series positive; no Phase 3 RCT; off-label use requires physician judgment.

**Apremilast in seb derm:** WEAK CANDIDATE — mechanism partial (NF-κB only); no rosacea/seb derm
RCT data; topical ketoconazole is more targeted for Malassezia-driven component.

**Key interaction to flag:** Itraconazole + Apremilast = elevated apremilast levels (CYP3A4).
If both are considered, apremilast dose should start at 10mg (titration dose) and itraconazole
should be managed carefully. Physician must review drug interaction.

---

## References

- Piccolo 2021 — Apremilast in papular rosacea (retrospective case series)
- PALACE 1-4 trials — Apremilast in psoriatic arthritis (Kavanaugh 2014-2016)
- Schakel 2021 — Apremilast Phase 2 in atopic dermatitis (NCT03048604)
- Ochsendorf 2004 — Early PDE4 inhibitor in rosacea analog
- Behçet's approval 2022 — FDA prescribing information (black box depression/suicidality)
- Otezla prescribing information — drug interactions (CYP3A4)

---

*Filed: 2026-04-12 | Numerics run 011 | Apremilast in rosacea non-responders and seb derm*
*Classification: CANDIDATE for rosacea non-responders (IL-23 mechanism sound; case series positive; no Phase 3 RCT)*
*Key interaction: Itraconazole + Apremilast → elevated apremilast (CYP3A4); monitor carefully*
*Key warning: Depression black box applies; relevant for T1DM patients with chronic illness depression risk*
*Protocol position: third-line M4 threshold intervention, between butyrate and anti-IL-23 biologics*
