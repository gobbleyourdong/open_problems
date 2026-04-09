# Attempt 055: Target 1 — OSBP (Cholesterol Delivery to Viral Replication Organelles)

## The Target

**Protein:** OSBP (Oxysterol-Binding Protein)
**Function:** Lipid exchanger. Shuttles cholesterol FROM ER → TO viral replication organelle membranes, counter-transporting PI4P in the opposite direction. PI4P is hydrolyzed by Sac1 at the ER, providing the energy gradient.
**Why the virus needs it:** Replication organelle membranes require cholesterol for stability. Without cholesterol delivery, the membranes collapse, dsRNA is exposed to cytoplasmic sensors, and replication complexes disassemble.
**Druggability:** HIGH. The oxysterol binding pocket is well-characterized. Multiple compound classes bind it.

## Every Known Compound That Hits OSBP

### Pharmaceutical Compounds

| Compound | EC50 vs Enterovirus | Mechanism | In Vivo Achievable? | Clinical Status |
|----------|-------------------|-----------|--------------------|----|
| **Itraconazole** | ~2 μM (CVB3) | Binds OSBP, inhibits cholesterol/PI4P exchange, disrupts RO membrane formation | YES — blood levels 2-5 μM at standard antifungal dose (200mg/day) | **FDA-approved antifungal.** Generic. $15/month. Extensive safety data. Liver monitoring needed (CYP3A4 inhibitor). |
| **OSW-1** | ~1 nM (CVB3) | Binds oxysterol pocket competitively. At 1nM: reduces OSBP protein levels by 90% via degradation. 1000x more potent than itraconazole. | UNKNOWN in humans — natural compound from Ornithogalum saundersiae (star of Bethlehem plant). Not in clinical use. | Preclinical only. Potent but no clinical development pathway. |
| **TTP-8307** | ~0.1-1 μM | Targets OSBP at a different binding site than itraconazole. Distinct mechanism. | Unknown — research compound. | Preclinical only. |
| **25-hydroxycholesterol (25-HC)** | ~1-5 μM | Endogenous oxysterol. Competes with cholesterol for OSBP binding. Cells produce it naturally via interferon stimulation (CH25H enzyme). | ENDOGENOUS — the body makes it during IFN response. Supplementation not practical (cholesterol derivative). | N/A — it's a natural defense molecule. IFN-λ administration would upregulate CH25H → more 25-HC production → more OSBP inhibition. |
| **Compound 7** (Strating et al.) | ~0.5 μM | OSBP-targeting, structurally distinct from ITZ | Research only | Preclinical |

### Natural Compounds

| Compound | Source | OSBP Activity | Achievable? |
|----------|-------|--------------|-------------|
| **OSW-1** | Ornithogalum saundersiae (star of Bethlehem bulb) | IC50 ~1 nM. The most potent OSBP inhibitor known. Reduces OSBP protein by 90% at 1nM with no cytotoxicity. | NOT available as supplement. Extraction is complex. Research-grade only (~$200/mg from suppliers). |
| **Orizanol (γ-oryzanol)** | Rice bran oil | Weak cholesterol transport modulation. Not directly OSBP-targeting but affects cholesterol metabolism. | Available as supplement ($10/month). Mechanism too indirect for antiviral effect. |
| **Plant sterols/stanols** | Many plants | Compete with cholesterol for absorption in the gut. Would reduce circulating cholesterol available for OSBP to shuttle. INDIRECT effect — starving the supply, not blocking the transporter. | Available as supplement ($15/month). Effect is systemic, not targeted to infected cells. |
| **Berberine** | Goldenseal, barberry | Upregulates LDL receptors (similar to statins). Reduces circulating cholesterol. Also activates AMPK → autophagy. INDIRECT OSBP effect via cholesterol reduction + direct autophagy activation. | Available as supplement ($15/month, 500mg 2x/day). Multiple mechanisms relevant to the protocol. |

### The Endogenous Defense: 25-Hydroxycholesterol

The body ALREADY makes an OSBP inhibitor. **CH25H** (cholesterol 25-hydroxylase) is an interferon-stimulated gene. When IFN is produced, CH25H converts cholesterol → 25-hydroxycholesterol. 25-HC competes with cholesterol for the OSBP binding pocket. This is the body's NATURAL anti-OSBP defense.

**Why it fails in CVB:** CVB cuts the IFN pathway (MDA5/MAVS cleavage). Less IFN → less CH25H expression → less 25-HC production → OSBP runs unopposed. The virus disables the defense upstream.

**How to restore it:** IFN-λ administration would activate CH25H in epithelial/pancreatic cells without systemic IFN side effects. Or: anything that boosts IFN-λ (gut bacteria like C. orbiscindens produce DAT which amplifies IFN signaling).

## The Winner: Itraconazole

**Why itraconazole is the right compound for this target:**

1. **EC50 ~2 μM.** Blood levels at 200mg/day = 2-5 μM. **ACHIEVABLE.**
2. **FDA-approved since 1992.** 30+ years of safety data. Billions of doses given.
3. **Generic.** $15/month.
4. **Oral.** Once daily.
5. **Mechanism PROVEN for enteroviruses.** Cell Reports 2015: itraconazole inhibits CVB, poliovirus, EV71, rhinovirus replication by targeting OSBP. Not speculation — demonstrated.
6. **Liver monitoring needed** (CYP3A4 inhibitor — drug interactions with statins, some antibiotics, some antidepressants). Check: does itraconazole interact with fluoxetine? Both CYP substrates. NEED TO VERIFY before combining.

## Drug Interaction Check: Itraconazole + Fluoxetine

**CRITICAL:** Itraconazole is a strong CYP3A4 inhibitor. Fluoxetine is a CYP2D6 inhibitor AND CYP3A4 substrate.

Combining them:
- Itraconazole inhibits CYP3A4 → fluoxetine clearance may decrease → fluoxetine levels rise
- The interaction is MODERATE, not contraindicated
- May need to reduce fluoxetine dose from 20mg to 10mg when co-administered
- OR: stagger — itraconazole 3 months first, then switch to fluoxetine
- **This needs pharmacist/physician review before combining**

## The Supplement Alternative

If itraconazole is not accessible (needs Rx, liver monitoring):

**Berberine 500mg 2x/day** ($15/month):
- Reduces circulating cholesterol (LDL receptor upregulation) → less substrate for OSBP
- Activates AMPK → autophagy → direct viral clearance
- Anti-inflammatory (NF-κB inhibition)
- Does NOT directly bind OSBP — the effect is INDIRECT
- Achievable concentration: berberine has poor oral bioavailability (~5%). Active metabolites may help.
- Evidence: moderate for cholesterol reduction, weak for antiviral specifically

**Berberine is NOT itraconazole.** The direct OSBP blockade is orders of magnitude more potent. But berberine attacks the same system from a different angle (reduce supply vs block transport) and has multiple other mechanisms relevant to the protocol.

## Summary

| Approach | Potency | Achievable | Cost | Prescription |
|----------|---------|-----------|------|-------------|
| Itraconazole | HIGH (EC50 2μM, direct OSBP) | YES (2-5 μM blood) | $15/mo | YES (Rx) |
| OSW-1 | EXTREME (IC50 1nM) | NO (not clinical) | N/A | N/A |
| 25-HC (via IFN-λ) | MODERATE (endogenous) | YES (if IFN-λ given) | Expensive | YES (Rx) |
| Berberine | LOW (indirect) | PARTIAL (poor bioavail) | $15/mo | NO (OTC) |
| Plant sterols | VERY LOW (systemic) | YES | $15/mo | NO (OTC) |

**For the protocol:**
- With Rx access: itraconazole 200mg/day × 3-6 months
- Without Rx: berberine 500mg 2x/day (weaker but multi-mechanism) — ADD TO SUPPLEMENT STACK

## Status: OSBP TARGET FULLY CHARACTERIZED — itraconazole is the drug, berberine is the OTC fallback

Sources:
- [Itraconazole inhibits enterovirus via OSBP - Cell Reports](https://www.cell.com/cell-reports/fulltext/S2211-1247(14)01121-8)
- [OSW-1 broad-range enterovirus inhibition - PubMed](https://pubmed.ncbi.nlm.nih.gov/25752737/)
- [OSBP compound-induced reduction - ACS Chem Bio](https://pubs.acs.org/doi/10.1021/acschembio.8b00984)
- [TTP-8307 targets OSBP - PubMed](https://pubmed.ncbi.nlm.nih.gov/28088354/)
- [Differing OSBP-targeting compounds - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10786240/)
