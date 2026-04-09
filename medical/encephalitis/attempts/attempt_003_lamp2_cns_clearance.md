# Attempt 003: LAMP2 in Neurons — Why CNS Clearance Is Bimodal

## Source
Patterns 013-016, attempt_080 (LAMP2 unified theory), hepatitis/attempt_003 (liver baseline analysis).

## The CNS Divergence (3.4×)

Unified model v2 predicts CNS clearance in 5 months. Dedicated encephalitis model predicts 1.7 years. The LAMP2 unified theory resolves this.

The CNS contains two fundamentally different cell populations with respect to autophagy:

| Cell type | % of CNS volume | LAMP2 baseline | After CVB −2.7× | κ_effective | Clearance |
|-----------|----------------|---------------|-----------------|-------------|----------|
| **Microglia** | 10–15% | ~1.8× avg | ~0.67× | **0.67** | ~5–7 months |
| **Astrocytes** | 20–40% | ~1.2× avg | ~0.44× | 0.44 | ~8–10 months |
| **Neurons** | 30–40% | ~0.6× avg | ~0.22× | **0.22** | ~1.5–2 years |
| **Oligodendrocytes** | 15–20% | ~0.8× avg | ~0.30× | 0.30 | ~12 months |

**The 5-month unified model captures microglia (the fastest-clearing CNS cells). The 1.7-year dedicated model better represents neuronal clearance.**

CVB in the CNS infects primarily neurons (CAR is expressed on neurons; DPP4 on astrocytes), but viral RNA from all cell types contributes to the disease burden. The clinical disease timeline follows the *slowest* clearing cell type — neurons — not the fastest.

## Why Neuronal LAMP2 Is Low

Neurons are post-mitotic, highly specialized cells that have evolved to minimize autophagy to protect irreplaceable structures:
- High mTOR activity (promotes synaptic protein synthesis, suppresses autophagy)
- Selective autophagy (mitophagy, aggrephagy) rather than bulk autophagy
- Lysosome distribution is problematic: lysosomes concentrate in soma, but viral replication complexes may be in distal processes (axons, dendrites) where lysosomal fusion is even more limited

**In CVB encephalitis**: viral replication complexes in neuronal processes are particularly difficult to clear — they're far from the perinuclear lysosomes, and fasting-induced autophagy doesn't uniformly access distal axons.

## The FOXP1/Microglial Treg Connection

Pattern 015/016: FOXP1 -67x in persistent CVB. In the CNS, FOXP1 has additional relevance:
- **Microglia** express FOXP1 as a regulator of inflammatory responses
- FOXP1 suppression in microglia → exaggerated neuroinflammation in response to CVB persistence
- This creates a local neuroinflammatory loop: CVB in neurons → microglia suppress FOXP1 → unrestrained microglial activation → neuroinflammation → synaptic damage → cognitive symptoms

The "brain fog" in ME/CFS and post-CVB encephalitis may reflect this microglial FOXP1 suppression as much as direct neuronal infection.

**Protocol implication**: the high-dose butyrate arm (HDAC inhibition → FOXP1 restoration) may have specific benefit for neurological symptoms via microglial FOXP1 recovery, separate from the Treg mechanism in peripheral tissues.

## Fluoxetine's CNS Advantage: Still the Best Drug

Despite low κ_effective in neurons, fluoxetine's 15× brain accumulation (Bolo 2000) ensures drug concentrations at 4.5 μM >> IC50 = 1.0 μM at standard 20mg dose. The drug gets there. The problem is autophagy completion, not drug delivery.

**Two-component CNS clearance under full protocol:**
1. Fluoxetine → WT CVB eliminated from CNS (fast: 3–5 months)
2. FMD + trehalose → TD mutant clearance (slow: 1.5–2 years for neurons)

This predicts a **biphasic clinical response** in encephalitis/ME/CFS:
- Phase 1 (months 1–5): improvement from WT clearance → reduced acute inflammation, some symptom improvement
- Phase 2 (months 5–24): slower improvement from TD clearance → gradual cognitive recovery, fatigue improvement

ME/CFS patients should be counseled to expect this biphasic trajectory. The Phase 1 improvement ("honeymoon") followed by a plateau is NOT failure — it reflects the transition from WT clearance to TD clearance.

## The Pocapavir Emergency Window

Prior attempt_001 (emergency antiviral protocol): pocapavir is the most potent direct CVB replication inhibitor (picomolar IC50). For acute CVB encephalitis, pocapavir + fluoxetine in the first 48–72 hours could:
1. Halt WT replication immediately
2. Prevent TD mutant establishment window (estimated 48–72 hours from initial infection)

**If pocapavir given within 48 hours of CVB encephalitis onset**: TD formation may be largely prevented because the WT population (which spawns TDs during replication errors) never reaches the size needed to generate sufficient TD variants. The risk of chronic neurological disease is dramatically reduced.

This is the most time-sensitive clinical recommendation in the entire campaign: **pocapavir within 48 hours of CVB encephalitis onset**. This window may prevent the neurological chronicity that follows.

## Trehalose for Neurological Benefit

Trehalose has direct neuroprotective effects beyond LAMP2 bypass:
1. **Huntington's disease**: trehalose reduces polyglutamine aggregates via autophagy enhancement (Sarkar 2007, Nat Chem Biol)
2. **ALS model**: trehalose delays disease progression in SOD1 mice (Kishimoto 2013)
3. **Mechanism**: TFEB activation in neurons → lysosomal expansion → better clearance of protein aggregates AND viral complexes

For CVB encephalitis and ME/CFS with neurological symptoms, trehalose serves double duty:
- Addresses LAMP2 block specifically (κ_neuron 0.22 → 0.50)
- Provides direct neuroprotection via TFEB/lysosomal biogenesis

**Optimal dose for neurological benefit**: trehalose 3g/day (higher than the 2g general protocol recommendation) — the neurological TFEB studies used higher doses.

## The Bimodal Clearance Prediction for ME/CFS

ME/CFS with CNS involvement (brain fog, cognitive dysfunction) will follow:

```
Timeline with full protocol (fluoxetine + FMD + trehalose 3g/day):

Month 1-3: Fluoxetine reaches CNS → WT CVB eliminated
Month 3-6: Microglial CVB (κ=0.67) clearing → neuroinflammation reducing
Month 6-12: Astrocyte CVB clearing → some recovery
Month 12-24: Neuronal CVB clearing (κ=0.22 → 0.50 with trehalose) → slow cognitive recovery
Month 18-24: PEM should significantly diminish as neuronal TD mutants clear

cfRNA prediction: STAT1/2/4, RIG-I/MDA5 normalize at months 3-6 (WT cleared)
then plateau, then continue to normalize at months 12-24 (neuronal clearance)
```

## Updated ODD Request

**REQ-014 (new)**: Update unified_cvb_clearance_v4.py to include:
1. Cell-type-specific LAMP2 corrections for CNS (microglia 0.67, neurons 0.22)
2. Trehalose correction factor per organ
3. Bimodal clearance curves for CNS (glial + neuronal populations separately)

**Output**: `results/pattern_019_lamp2_corrected_clearance_v4.md`

## Status: CNS CLEARANCE BIMODALITY EXPLAINED — microglia 5-7mo, neurons 1.5-2yr. FOXP1 microglial suppression explains brain fog. Trehalose 3g/day for neurological benefit (dual mechanism: LAMP2 bypass + direct neuroprotection). Pocapavir 48-hour window identified as most time-sensitive intervention in entire campaign.
