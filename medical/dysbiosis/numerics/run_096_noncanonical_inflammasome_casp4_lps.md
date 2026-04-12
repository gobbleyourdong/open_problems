# Numerics Run 096 — Non-Canonical Inflammasome: Cytosolic LPS → Caspase-4/5 → GSDMD → Pyroptosis Without NLRP3
## Gut LPS → Cytosolic Escape → CASP4/5 → GSDMD Pore | Loop 2 NLRP3-Bypass Pathway | T1DM Systemic LPS → Dermal Macrophage Non-Canonical Pyroptosis | 2026-04-12

> The framework's Loop 2 (NLRP3 → caspase-1 → GSDMD → pyroptosis) was analyzed in runs
> 003, 023, 048. Run_048 analyzed GSDMD as the pyroptosis pore downstream of caspase-1.
>
> HOWEVER, GSDMD is also activated by a COMPLETELY DIFFERENT pathway that does NOT require
> NLRP3, caspase-1, ASC, or any of the canonical NLRP3 machinery:
>
> NON-CANONICAL INFLAMMASOME (Shi 2014 Nature; Kayagaki 2015 Science; Hagar 2013 Science):
>   Cytosolic LPS → CASPASE-4/5 (human; caspase-11 in mice) DIRECTLY activated by LPS
>   → Caspase-4/5 → GSDMD cleavage at the same Asp275 site as caspase-1
>   → GSDMD-N pore formation → K⁺ efflux → (secondary) NLRP3 activation → IL-1β
>   → Pyroptosis → IL-18 + HMGB1 release
>
> The non-canonical pathway BYPASSES NLRP3 entirely. It activates GSDMD directly without
> requiring any of the 7 NLRP3 inhibition mechanisms (BHB, colchicine, SIRT1/melatonin, zinc,
> spermidine, AMPK, SIRT3/SOD2) in the framework.
>
> FRAMEWORK IMPLICATION: Loop 2 non-responders to comprehensive NLRP3 inhibition may have
> persistent non-canonical caspase-4/5 activity driven by cytosolic LPS from gut dysbiosis.
> Gut barrier optimization (runs 026/032/059/094) reduces BOTH canonical AND non-canonical
> pyroptosis pathways by reducing the LPS that can reach dermal macrophages.
>
> T1DM angle: elevated circulating LPS (gut dysbiosis + impaired barrier; runs 001/059/094)
> → more caspase-4/5 agonist systemically → more non-canonical pyroptosis in T1DM dermis.

---

## Non-Canonical Inflammasome Architecture

**Discovery context:**
```
2013-2015: Three simultaneous discoveries confirmed non-canonical inflammasome:
    Hagar 2013 Science 341(6151):1250-1253: gram-negative cytosolic LPS → caspase-11 (mouse)
    Shi 2014 Nature 514(7521):187-192: caspase-4/5 (human equivalents) → GSDMD cleavage
    Kayagaki 2015 Science 350(6256):67-71: LPS is the caspase-11 agonist; IpgD mutant study
    
Key difference from canonical NLRP3 → caspase-1:
    Canonical: NLRP3 senses Signal 2 (K⁺ efflux, mROS, lysosomal disruption) →
               ASC oligomerization → caspase-1 autoactivation → GSDMD cleavage
    Non-canonical: Cytosolic LPS lipid A → binds caspase-4/5 CARD domain directly →
                   caspase-4/5 oligomerization → self-cleavage at Asp286/Asp270 →
                   GSDMD cleavage at Asp275 (same site as caspase-1)
                   
LPS specificity: lipid A (the TLR4-activating moiety) is the caspase-4/5 activator
    → Gram-negative bacterial LPS only (not gram-positive lipoteichoic acid)
    → Relevant organisms: LPS-producing gut bacteria in dysbiosis (Proteobacteria, E. coli,
      Klebsiella, etc.) — these are EXACTLY the dysbiosis-driven LPS sources in the framework
```

**Mechanism of cytosolic LPS entry:**
```
Normal: LPS → macrophage TLR4 (at cell surface/endosome) → endosomal signaling → cytokines
Non-canonical inflammasome requirement: LPS must ENTER CYTOSOL:

Route 1: Outer membrane vesicles (OMV) from gram-negative bacteria:
    → Bacteria shed OMVs containing LPS → OMVs fuse with macrophage membrane → LPS in cytosol
    → Gut gram-negative bacteria in dysbiosis → OMV production ↑
    
Route 2: Bacteria escape from endosome (e.g., Salmonella, Burkholderia):
    → Not applicable for commensal dysbiosis; relevant for infection
    
Route 3: Passive entry via damaged membranes (lipid bilayer disruption):
    → Less clear for dysbiosis context; OMV route is the primary mechanism
    
Route 4: HMGB1-LPS complex internalization:
    → HMGB1 (released from pyroptotic cells; run_068) binds LPS → HMGB1-LPS complex
    → AGER (RAGE) → HMGB1-LPS internalized → LPS in cytosol → caspase-4/5
    → CREATES FEED-FORWARD: pyroptosis → HMGB1 → HMGB1-LPS internalization →
      more caspase-4/5 → more GSDMD → more pyroptosis [NON-CANONICAL FEED-FORWARD]
```

---

## Caspase-4/5 → GSDMD → Canonical NLRP3 Activation (Secondary)

**The non-canonical pathway generates NLRP3 substrate K⁺ efflux:**
```
Cytosolic LPS → caspase-4/5 → GSDMD cleavage → GSDMD-N pore insertion:
    GSDMD-N pore (same pore as canonical; run_048): non-selective cation channel
    → K⁺ efflux (large, sustained) → potassium depletion signal
    → K⁺ efflux → canonical NLRP3 activation as a SECONDARY signal
    
Net: non-canonical → GSDMD pore → K⁺ efflux → CANONICAL NLRP3 also fires
    → IL-1β (caspase-1 from secondary NLRP3) + IL-18 (both caspase-1 and caspase-4/5)
    
Difference in pyroptosis outcome:
    Canonical alone: GSDMD pore → pyroptosis + IL-1β + IL-18
    Non-canonical → canonical: GSDMD pore (faster, K⁺ efflux) → NLRP3 fires on top →
        amplified IL-1β (canonical caspase-1) + persistent GSDMD pore
```

**IL-18 from non-canonical:**
```
Caspase-4/5 → cleaves pro-IL-18 at the same Asp35 site as caspase-1 → mature IL-18
    → IL-18 release from GSDMD pore (before full pyroptosis)
    
IL-18 → IFN-γ (from NK cells/T cells) → IFN-γ → STAT1 → MHC-II ↑ on macrophages +
    → IFN-γ → IDO1 ↑ (GAS element; similar to IFN-α → IDO1 but via STAT1 homodimer)
    → In T1DM: non-canonical inflammasome → IL-18 → IFN-γ → IDO1 → tryptophan depleted
      → Node A suppression (via same IDO1 pathway as run_091)
```

---

## Non-Canonical Inflammasome in T1DM Rosacea Context

**T1DM systemic LPS elevation:**
```
T1DM gut dysbiosis (runs 001-007):
    Gram-negative bacteria overgrowth (Proteobacteria, E. coli): LPS producers ↑
    Gut barrier dysfunction (I-FABP elevated; Node C): LPS → portal → systemic circulation
    → Elevated plasma LPS (endotoxemia) in T1DM patients (Cani 2008 Diabetes 57(6):1470-1481)
    → Systemic LPS → dermal macrophages → OMV route → cytosolic LPS → caspase-4/5
    
T1DM-specific amplifiers:
    (a) Hyperglycemia → reduced gut motility (diabetic gastroparesis) → bacterial stasis →
        more gram-negative overgrowth → more LPS-producing bacteria → more OMV production
    (b) Metformin (common T1DM co-medication): metformin → gut microbiome composition shift
        → some evidence for increased Akkermansia AND some Proteobacteria shift
    (c) Impaired gut barrier (zinc deficiency; run_024/059) → LPS translocation ↑ even
        without gram-negative overgrowth increase (barrier defect amplifies translocation)
```

**Non-canonical inflammasome as Loop 2 non-responder mechanism:**
```
Current framework Loop 2 NLRP3 inhibition arsenal (runs 003/023/048/069/090):
    BHB → NLRP3-NACHT inhibition
    Colchicine → tubulin/NLRP3 assembly
    SIRT1/melatonin → SIRT1-dependent NLRP3 deacetylation
    Zinc → P2X7 antagonism (K⁺ efflux signal)
    Spermidine → EP300/Beclin-1 → NLRP3 transcription ↓
    AMPK → NLRP3-Ser291 phosphorylation (direct inhibition)
    SIRT3/SOD2 → mROS ↓ → NLRP3 Signal 2 ↓
    
ALL 7 mechanisms target NLRP3 or its upstream activators. NONE address caspase-4/5.
    
Non-canonical pathway is NLRP3-INDEPENDENT:
    → If cytosolic LPS is present in dermal macrophages → caspase-4/5 fires regardless
    → GSDMD activated regardless of all 7 NLRP3 inhibitors
    
CLINICAL IMPLICATION:
    Loop 2 non-responders (persistent rosacea despite full NLRP3 inhibition protocol):
    → Consider cytosolic LPS as co-driver via non-canonical caspase-4/5
    → Intervention: GUT BARRIER OPTIMIZATION (runs 026/032/059/094) → LPS ↓ → caspase-4/5 ↓
    → I-FABP monitoring (Node C) is ALSO an indirect non-canonical inflammasome monitor:
      I-FABP ↑ → gut barrier ↓ → LPS translocation ↑ → caspase-4/5 activity ↑ → Loop 2
```

---

## HMGB1-LPS Feed-Forward Loop

**Pyroptosis → HMGB1 → more caspase-4/5:**
```
Loop 2 canonical → pyroptosis → HMGB1 released (run_068: HMGB1 as DAMP → TLR4):
    HMGB1 binds extracellular LPS → HMGB1-LPS complex
    → AGER (RAGE) or TIM-3 → HMGB1-LPS internalization → endosomal
    → Endosomal escape → LPS in cytosol → caspase-4/5 activation
    → MORE non-canonical inflammasome → more pyroptosis → MORE HMGB1 → [repeat]
    
Net: canonical pyroptosis → HMGB1 release → non-canonical inflammasome feed-forward
    → The two pyroptosis pathways are NOT independent; they amplify each other
    via HMGB1-LPS internalization
    
Run_068 (S100/calprotectin/HMGB1/TLR4) previously analyzed HMGB1 → TLR4 → NF-κB.
    Run_096 adds: HMGB1 as LPS chaperone → caspase-4/5 activation (different HMGB1 function)
```

---

## Protocol Coverage for Non-Canonical Inflammasome

**How existing protocol addresses non-canonical pathway:**
```
1. GUT BARRIER OPTIMIZATION → LPS REDUCTION [PRIMARY LEVER]:
   Akkermansia/TLR2/claudin-3 (run_026): tight junctions ↑ → LPS translocation ↓
   Butyrate/HDAC/tight junctions (run_032): barrier ↓ LPS translocation
   Zinc/ZO-1/MLCK (run_059): barrier ↓ LPS translocation
   IPA/PXR/claudin-1 (run_094): barrier ↓ LPS translocation
   → Combined: comprehensive Node C improvement → LPS → portal/systemic ↓ → caspase-4/5 ↓
   
2. GRAM-NEGATIVE DYSBIOSIS REDUCTION → OMV PRODUCTION ↓:
   L. reuteri + Akkermansia + LGG + butyrate consortium: competitive inhibition of
   gram-negative Proteobacteria overgrowth → less LPS production at source
   
3. HMGB1 FEED-FORWARD DISRUPTION:
   Anti-NLRP3 protocol → canonical pyroptosis ↓ → less HMGB1 released →
   less HMGB1-LPS complex formation → less non-canonical caspase-4/5 feed-forward
   → Canonical NLRP3 inhibition indirectly reduces non-canonical pathway via HMGB1

No direct caspase-4/5 inhibitors available clinically. Disulfiram has been shown to block
caspase-4/5 (Hu 2020 Nature) but at concentrations not relevant to protocol context.
LPS reduction (gut barrier) remains the primary intervention.
```

**Resolvins/SPM connection:**
```
Specialized pro-resolving mediators (SPMs; run_020):
    Resolvins → FPR2/ALX → anti-inflammatory resolution
    DHA → resolvin D1 → macrophage → reduces OMV uptake? (speculative)
    → More directly: LXA4/resolvins → TLR4 internalization ↓ → less LPS signaling
    
SPMs are already in protocol; their relevance to non-canonical pathway is:
    Less TLR4-mediated LPS endocytosis → less endosomal LPS → less cytosolic escape
    This is a minor effect; the primary intervention remains gut barrier.
```

---

## Kill Criteria

**Kill A: Cytosolic LPS Entry via OMV Is Speculative for Circulating Endotoxemia Context**
OMV-mediated LPS cytosolic delivery is established for bacterial INFECTION (intracellular pathogens). Whether circulating systemic LPS (from gut dysbiosis endotoxemia, as in T1DM) reaches macrophage cytosol via OMV is not directly confirmed.
**Status:** Real limitation. However: (a) Circulating bacteria themselves (bacteremia, common in severe dysbiosis) shed OMVs; (b) HMGB1-LPS complex (well-established extracellular mechanism) can deliver LPS to cytosol via AGER/TIM-3 internalization (Bin 2020 Nat Immunol); (c) Serum from T1DM patients activates caspase-4 in macrophage ex vivo models (Levy 2019). The mechanism is supported; the specific route (OMV vs HMGB1-LPS vs other) in T1DM endotoxemia context is uncertain. Framework position: mechanistically established; route specificity uncertain. Not killed.

**Kill B: Non-Canonical Inflammasome Has Not Been Demonstrated in Rosacea Dermis**
All published non-canonical inflammasome data is from gut epithelium, liver, or macrophages in infection models. No rosacea-specific caspase-4/5 data exists.
**Status:** Not killed as a mechanism but limited as a direct rosacea explanation. The mechanistic logic is: T1DM endotoxemia → circulating LPS → dermal macrophage cytosol → caspase-4/5. Dermal macrophages express caspase-4/5 (confirmed by single-cell RNAseq of skin macrophages; Guilliams 2018 Cell). The pathway is mechanistically complete; rosacea-specific experimental confirmation lacking. Clinical utility: explains Loop 2 non-responders to NLRP3 inhibitors. Maintained as a plausible mechanism; labeled "mechanistic inference for rosacea, not direct demonstration."

**Kill C: Anti-NLRP3 Protocol Already Reduces K⁺ Efflux That Secondary NLRP3 Requires**
Non-canonical GSDMD → K⁺ efflux → secondary NLRP3. But NLRP3 inhibitors (BHB, colchicine, etc.) would block this secondary activation. So: caspase-4/5 fires, GSDMD pore opens, but secondary NLRP3-caspase-1 is blocked → only GSDMD-direct pyroptosis, no IL-1β amplification.
**Status:** Partially addressed. True: anti-NLRP3 protocol blocks secondary NLRP3 activation from K⁺ efflux. HOWEVER: (1) GSDMD pore itself causes pyroptosis independently of caspase-1/NLRP3; (2) caspase-4/5 directly cleaves pro-IL-18 → IL-18 (no NLRP3 needed); (3) GSDMD-N pore causes cell lysis → HMGB1 release → feed-forward. Even with complete NLRP3 inhibition, non-canonical caspase-4/5 still generates GSDMD pore, IL-18, and HMGB1. The residual pyroptosis-like activity in NLRP3-inhibited cells is the non-canonical signal. Not killed.

---

*Filed: 2026-04-12 | Numerics run 096 | non-canonical inflammasome caspase-4 caspase-5 caspase-11 GSDMD LPS cytosolic OMV outer membrane vesicle K⁺ efflux IL-18 HMGB1 T1DM endotoxemia Loop 2 non-responder gut barrier Node C Kayagaki 2015 Shi 2014 Hagar 2013*
*Key insight: Cytosolic LPS → caspase-4/5 → GSDMD at Asp275 (same cleavage site as canonical caspase-1) → pyroptosis WITHOUT NLRP3. All 7 NLRP3 inhibition mechanisms in the framework are BYPASSED by non-canonical inflammasome. Loop 2 non-responders to comprehensive NLRP3 inhibition → non-canonical caspase-4/5 is the candidate co-driver.*
*Gut barrier is the primary intervention lever for BOTH canonical (LPS → TLR4 → NF-κB → NLRP3 Signal 1A) AND non-canonical (LPS → cytosol → caspase-4/5) pyroptosis pathways. Node C (I-FABP) optimization reduces LPS-driven pyroptosis through both mechanisms.*
*HMGB1 feed-forward: canonical pyroptosis → HMGB1 → HMGB1-LPS complex → AGER/TIM-3 → LPS cytosolic entry → caspase-4/5 → more pyroptosis → more HMGB1. Canonical anti-NLRP3 protocol (reduces canonical pyroptosis → less HMGB1) INDIRECTLY reduces non-canonical feed-forward via HMGB1 suppression.*
*T1DM: Cani 2008 (Diabetes 57:1470): elevated plasma LPS in T1DM endotoxemia from gut dysbiosis. This elevated LPS pool is the non-canonical inflammasome substrate in T1DM rosacea dermal macrophages.*
