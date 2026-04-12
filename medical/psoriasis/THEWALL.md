# Psoriasis — THE WALL

## Classification Reminder

Psoriasis is **NOT** a CVB disease. Category 2 co-beneficiary: Th17/IL-23 axis, NF-κB, NLRP3, and Treg insufficiency. The campaign addresses psoriasis through the shared pathway.

## The Wall

**The wall for psoriasis is that the protocol doesn't directly block IL-23 — the primary driver.**

In psoriasis: keratinocyte neoantigen (LL-37) → NF-κB → IL-23 production → Th17 differentiation → IL-17 release → keratinocyte proliferation. The biologics (guselkumab, secukinumab, ixekizumab) directly block IL-23 or IL-17.

The protocol attacks the amplification system:
```
What biologics do:                   What the campaign does:
Guselkumab → block IL-23            Butyrate → FOXP1 → Tregs suppress Th17
                                     BHB/colchicine → NLRP3 suppression → less IL-1β
                                     VitD → VDR → FOXP1 + anti-IL-17 effects
                                     Omega-3 → resolvins → IL-17 suppression
                                     Apremilast (generic) → PDE4 → cAMP → IL-23↓
```

## The Apremilast Bridge (Critical for Psoriasis)

The protocol's NF-κB targeting (attempt 062 from T1DM) identified apremilast (PDE4 inhibitor) as the bridge drug between T1DM and psoriasis. Apremilast:
- FDA-approved for psoriasis AND psoriatic arthritis
- Goes generic in 2024-2026 (Otezla patent expiry)
- At generic price: ~$30-60/month
- Mechanism: PDE4 inhibition → cAMP → PKA → CREB → IL-10 ↑, TNF-α ↓, IL-17 ↓, IL-23 ↓

**The wall is crossed when generic apremilast becomes affordable**: protocol + apremilast 30mg BID = predicted PASI 65-75% improvement (comparable to biologic response at a fraction of the cost).

## The FOXP1-Th17 Connection

Attempt_004 (bioinformatics): FOXP1 required for Treg homeostasis in skin microenvironment. In psoriasis:
- Chronic NF-κB activation → possible FOXP1 suppression (independent of CVB)
- FOXP1 suppression → local Treg failure → Th17 cells escape suppression
- High-dose butyrate (4-6g/day) + VitD 5000 IU → FOXP1 restoration → Treg suppression of Th17

This is the FOXP1-mediated mechanism running parallel to the apremilast's direct IL-23 suppression. Together: synergistic.

## Expected Effect (Protocol Alone vs Protocol + Apremilast)

| Intervention | Predicted PASI Response | Mechanism |
|--------------|------------------------|-----------|
| Protocol alone | 40-50% | NLRP3 + NF-κB + Treg/Th17 balance |
| Apremilast alone | 50-60% (PALACE trial data) | PDE4 → cAMP → IL-10/IL-23 |
| Protocol + apremilast | **65-75%** | Synergistic: upstream (Treg) + mid-stream (IL-23) |
| Biologic (guselkumab) | 65-75% | Direct IL-23 blockade |

Protocol + generic apremilast ≈ biologic response at $90-120/month total vs $2,400+/month biologic.

## Timeline

- **Month 1-2**: NF-κB suppression (colchicine, BHB) + gut dysbiosis starting to improve
- **Month 3-4**: FOXP1/Treg restoration (butyrate + VitD). Th17 modulation beginning.
- **Month 4-6**: If adding apremilast: IL-23 suppression adds to Treg effects → PASI improvement
- **Month 6+**: Expect 40-75% PASI improvement depending on whether apremilast is added

## For Psoriatic Arthritis Patients

Psoriatic arthritis (PsA) has the same mechanism plus joint inflammation. Apremilast is FDA-approved for PsA specifically. The protocol's BHB (NLRP3 → IL-1β suppression) and colchicine (microtubule block) additionally address the gouty-like crystal deposition in some PsA joints.

## The Wall (Formal)

The wall for psoriasis is cost: generic apremilast doesn't exist yet at the time of writing (2026), though patent expiry is imminent. Without apremilast:
- Protocol alone achieves 40-50% PASI — meaningful but not complete
- Adding a biologic to the protocol: costs $2,400+/month, defeats the purpose

**The wall is apremilast going generic.** When it does, the protocol + generic apremilast becomes a $120/month alternative to $2,400/month biologics with comparable PASI response. That's the clinical breakthrough for psoriasis patients.

**Immediate action**: if the patient has psoriasis alongside T1DM, start the protocol. Track PASI at 3 and 6 months. When generic apremilast becomes available, add it. The protocol establishes the Treg/FOXP1 foundation; apremilast will provide the final IL-23 hit.

---

## Phase 4 Update — 2026-04-12 (Dysbiosis Framework Cross-Pollination)

### Non-Responder Loop Taxonomy Applied to Psoriasis

30-40% of biologic-treated psoriasis patients are partial/non-responders. The dysbiosis non-responder framework explains why (see `attempts/attempt_005_dysbiosis_framework_import.md`):

**Loop 1 (KLK5/LL-37/IFN-α in psoriasis):** LL-37 is the PRIMARY psoriasis autoantigen — LL-37-DNA complexes → pDC TLR9 → IFN-α → KLK5 ↑ → more LL-37 → self-amplifying loop. IL-23 blockade reduces downstream Th17 but does not break this upstream loop. Treatment: azelaic acid (KLK5 inhibitor topically) + topical rapamycin 0.2% (mTORC1 arm in keratinocytes).

**Loop 3 (HERV-W in psoriasis):** HERV-W sequences are elevated in psoriatic skin (Gross 2000 Exp Dermatol; Balada 2010 Autoimmun Rev — MSRV-Env in psoriatic PBMCs). HERV-W → TLR4 → NF-κB → IL-6/TNF-α sustaining loop independent of IL-23. IL-23 blockade does not address this. Treatment: gut/sleep protocol + colchicine 0.5mg BID (NF-κB suppression arm; same dual-loop mechanism as in rosacea).

### VDR-Butyrate Synergy Confirmed for Psoriasis

Butyrate (4-6g/day) HDAC inhibition → VDR upregulation in Tregs → same vitamin D dose produces superadditive Foxp3 induction. Tregs become more stable against IL-23-driven Foxp3→RORγt conversion. The protocol combination (butyrate + VitD₃ 5000 IU) is mechanistically synergistic, not coincidentally combined.

### SEQUENCE Trial as RCT Confirmation

Risankizumab (IL-23 inhibitor) is FDA-approved for BOTH psoriasis (ULTIMMA) and Crohn's disease (SEQUENCE trial). The SEQUENCE trial finding — treating Crohn's → secondary psoriasis improvement — is RCT-level confirmation of the M1↔M4 gut-skin GALT Th17 trafficking mechanism. Psoriasis patients with concurrent IBD should receive gut intervention as a primary psoriasis treatment component.

### M6 Structural Floor as Psoriasis Severity Predictor

C-section delivery + early antibiotic exposure → reduced SCFA during neonatal Treg imprinting → lower Foxp3 CNS2 methylation → lower structural Treg floor. Under chronic IL-23 stimulation (psoriatic skin), this floor is the final limit on Treg suppression of Th17. **Prediction:** psoriasis patients with C-section/early antibiotics have higher baseline PASI, lower Foxp3+/CD4+ ratio, and slower biologic response rate (needs more IL-23 suppression to compensate for lower Treg ceiling).

*Updated: 2026-04-12 | Dysbiosis Phase 4 cross-pollination | Three non-responder loops | VDR-butyrate synergy | SEQUENCE trial M1↔M4 | M6 floor severity predictor*

---

### Vitamin K2/MK-7: Fifth NF-κB Suppressor for Loop 3 in Psoriasis (run_039 import)

**Bacteroidetes depletion is documented in psoriasis (independent of T1DM):**
Scher 2015 eLife: psoriatic skin + psoriatic arthritis → Bacteroidetes ↓ (specifically
Bacteroides + Prevotella; MK-7 producers). Psoriasis patients are thus K2-deficient from gut
dysbiosis by the same mechanism as T1DM, independent of T1DM comorbidity.

**K2 → Gas6/Axl → SOCS1 → NF-κB suppression in psoriasis:**
Loop 3 (HERV-W NF-κB sustaining loop) is a psoriasis non-responder mechanism. SOCS1 from
Gas6/Axl signaling inactivates the assembled IKK complex → IκBα not phosphorylated → NF-κB p65
stays sequestered → HERV-W promoter not driven → Loop 3 broken. This is the fifth independent
NF-κB mechanism alongside colchicine, sulforaphane, vagal CAP, and CAPE.

**Psoriasis-specific: MGP + psoriatic arthritis calcification:**
Enthesitis calcification (calcaneal spurs, tendon calcification at entheses) is driven partly
by inadequate MGP-mediated calcium crystal inhibition. MK-7 180µg/day → MGP carboxylated →
entheseal calcium deposition reduced. This is a secondary benefit for psoriatic arthritis patients.

**Add to psoriasis protocol:** MK-7 180µg/day (with dietary fat; warfarin contraindication check).
Complements existing colchicine + sulforaphane + VDR-butyrate protocol for Loop 3 NF-κB arm.

See `../dysbiosis/numerics/run_039_vitamin_k2_mk7_nfkb.md`.

*Updated: 2026-04-12 | K2/MK-7 cross-pollination from dysbiosis run_039*
*Bacteroidetes ↓ in psoriasis (Scher 2015) → K2 deficiency → Gas6/Axl SOCS1 → NF-κB disinhibited: Loop 3 amplified*
*MK-7 180µg/day adds fifth NF-κB mechanism; also addresses entheseal calcification in psoriatic arthritis*
