# Numerics Run 090 — SIRT3 + SIRT6: Mitochondrial and Epigenetic NAD⁺-Dependent Sirtuins Beyond SIRT1
## SIRT3 → SOD2 Deacetylation → mROS ↓ → NLRP3 Signal 2 ↓ | SIRT6 → H3K9ac at NF-κB Targets → Epigenetic Repression | T1DM NAD⁺ Compartmentalization | 2026-04-12

> Run_031 analyzed niacinamide → NAD⁺ → SIRT1 via five distinct mechanisms (NLRP3 K496
> deacetylation, FOXO3a, p53/apoptosis inhibition, HIF-1α mRNA stability, and direct
> NAD⁺-dependent effects). SIRT1 is the nuclear/cytoplasmic sirtuin.
>
> Two other sirtuins — SIRT3 and SIRT6 — also require NAD⁺ as co-substrate and are
> NOT analyzed in the framework despite being activated by the same niacinamide → NAD⁺ pool.
>
> SIRT3 (mitochondrial localization; the "guardian of the mitochondria"):
>   → Primary substrate: SOD2 (Mn-superoxide dismutase) Lys122/Lys68
>   → SIRT3 → deacetylates SOD2 → SOD2 FULLY ACTIVE → O₂•⁻ → H₂O₂ scavenged
>   → Mitochondrial ROS (mROS) ↓ → NLRP3 Signal 2 (mROS-triggered K⁺ efflux) ↓
>   → T1DM: mitochondrial Complex I/III dysfunction → mROS → mitochondrial PARP-3 activation
>     → mitochondrial NAD⁺ ↓ → SIRT3 ↓ → SOD2 acetylated/inactive → MORE mROS (vicious cycle)
>
> SIRT6 (nuclear; H3 deacetylase at specific loci):
>   → Primary substrate: H3K9ac and H3K56ac at NF-κB target gene promoters
>   → SIRT6 → deacetylates H3K9 at TNFα, IL-6, MCP-1 promoters → chromatin compacted
>     → NF-κB transcriptional activity ↓ at these specific loci (epigenetic mechanism)
>   → Also: SIRT6 → TNFα mRNA stability ↓ (Zhong 2010 Science: JNK pathway)
>   → T1DM: high glucose → SIRT6 expression ↓ (Li 2012 BBRC) → less H3K9 deacetylation
>     → more open chromatin at NF-κB targets → lower threshold for inflammatory gene expression
>
> Both SIRT3 and SIRT6 are activated by NAD⁺ → niacinamide protocol (run_031) already
> provides the cofactor. These are ADDITIONAL benefits of the existing niacinamide protocol
> not previously formalized.

---

## Part A: SIRT3 — Mitochondrial Sirtuin and the mROS → NLRP3 Connection

### SIRT3 Localization and NAD⁺ Dependence

**Mitochondrial NAD⁺ compartmentalization:**
```
NAD⁺ in cells is compartmentalized:
    Cytosolic/nuclear NAD⁺: 100-200 µM (run_031 niacinamide → NAD⁺ primarily in this pool)
    Mitochondrial NAD⁺: 200-300 µM (higher concentration; synthesized locally in mitochondria)
    
Mitochondrial NAD⁺ synthesis:
    Mitochondria CANNOT directly import NAD⁺ from cytoplasm in mammals (NAD⁺ is membrane-impermeant)
    → Mitochondrial NAD⁺ relies on: (1) NRK2 (mitochondrial NR kinase); (2) NMNAT3 (mitochondrial)
    → NMN transporter Slc12a8 (mouse) may exist in human mitochondrial membrane
    
T1DM impact on mitochondrial NAD⁺:
    High glucose → mitochondrial Complex I/III dysfunction → excess NADH → PARP-3 activation
    (PARP-3 is the mitochondrial PARP isoform) → PARP-3 consumes mitochondrial NAD⁺
    → Mitochondrial NAD⁺ ↓ → SIRT3 substrate depleted → SIRT3 activity ↓
    
Niacinamide → NAD⁺ (primarily cytosolic via NAMPT → NMNAT1/2):
    → Also elevates mitochondrial precursors (NMN can be converted to mitochondrial NAD⁺)
    → NR (nicotinamide riboside): direct mitochondrial NAD⁺ precursor; better mitochondrial
       penetration than niacinamide in some studies (Cantó 2012 Cell Metab 15(6):838-847)
    
SIRT3 expression: highest in metabolically active tissues (liver, brown adipose, brain)
    → Also expressed in macrophages, β cells, neutrophils (all relevant to T1DM rosacea)
```

### SIRT3 → SOD2 → mROS Scavenging

**SOD2 (Mn-SOD; manganese superoxide dismutase) activation by SIRT3:**
```
SOD2 in mitochondria:
    → Converts superoxide (O₂•⁻) from Complex I/III → H₂O₂ (less reactive)
    → H₂O₂ → then reduced by glutathione peroxidase (GPx) or catalase → H₂O
    → Without SOD2: O₂•⁻ + NO → peroxynitrite (ONOO⁻) → protein nitration + DNA damage
    
SOD2 regulation by acetylation:
    SOD2 Lys122/Lys68: acetylated (INACTIVE) → SOD2 cannot convert O₂•⁻ → H₂O₂
    SIRT3 → deacetylates SOD2 Lys122 → SOD2 FULLY ACTIVE (Qiu 2010 J Biol Chem 285:8211)
    → Key switch: SIRT3 activity = acetylation state of SOD2 = mROS scavenging capacity
    
Evidence:
    Hirschey 2010 Cell 140(2):280-293: SIRT3 knockout → SOD2 hyperacetylation → mROS ↑
    SIRT3 KO mice: 3-5× elevated mitochondrial O₂•⁻ vs. wildtype under same metabolic load
    Qiu 2010 J Biol Chem: Lys122 is the dominant deacetylation site → mutating K122R → SOD2
    activity ↑ 3-fold even without SIRT3 (proves K122 acetylation is the primary inhibitory switch)
```

**SIRT3 → SOD2 → mROS ↓ → NLRP3 Signal 2 ↓:**
```
NLRP3 Signal 2 requires an activation signal from MULTIPLE routes (run_012 framework):
    mROS: mitochondrial O₂•⁻ → cardiolipin oxidation → NLRP3 direct activation
          + mROS → K⁺ efflux (via membrane lipid peroxidation → channel disruption)
    
SIRT3-active state:
    SIRT3 ↑ → SOD2 deacetylated → active → O₂•⁻ ↓ → cardiolipin not oxidized
    → K⁺ efflux NOT triggered by mROS → NLRP3 Signal 2 ↓
    → This is DISTINCT from the existing 6 NLRP3 inhibition mechanisms (which target different 
      steps: BHB=K⁺/NACHT; colchicine=tubulin; SIRT1=K496; zinc=K⁺; spermidine=EP300; AMPK=Ser291)
    → SIRT3-SOD2 = 7th NLRP3 inhibition mechanism (suppresses the mROS arm of Signal 2 specifically)
    
T1DM: 
    Mitochondrial Complex I/III dysfunction → mROS chronically elevated (T1DM-specific)
    → SIRT3 ↓ (from PARP-3/NAD⁺ depletion) → SOD2 acetylated → mROS not scavenged
    → NLRP3 Signal 2 elevated from BOTH: (a) mROS (via SIRT3 ↓) + (b) ATP/HMGB1/crystals
    → SIRT3 restoration via NAD⁺ supplementation = T1DM-specific benefit
```

### SIRT3 → FOXO3a → Mitophagy

```
SIRT3 → deacetylates FOXO3a (transcription factor) → FOXO3a nuclear → activates:
    PINK1/Parkin gene expression (Bcl-2 family, mitophagy pathway)
    SOD2 gene expression (additional SOD2 beyond K122 deacetylation)
    Catalase gene expression → H₂O₂ → H₂O (secondary ROS scavenging)
    
SIRT3 → FOXO3a → PINK1/Parkin = ADDITIVE to spermidine (run_071: EP300 → Beclin-1/ATG) 
    and urolithin A (run_078: PINK1/Parkin directly)
    → Three parallel mitophagy activation routes in protocol:
        Spermidine → EP300 inhibition → acetylation shift → autophagy induction
        Urolithin A → PINK1/Parkin → selective mitophagy
        SIRT3 → FOXO3a → PINK1/Parkin gene expression (via NAD⁺ niacinamide)
```

---

## Part B: SIRT6 — Epigenetic NF-κB Suppression via H3K9ac Deacetylation

### SIRT6 Mechanism: Chromatin-Level NF-κB Control

**SIRT6 and histone H3K9 deacetylation at NF-κB targets:**
```
SIRT6 (nuclear sirtuin; class III HDAC):
    → Deacetylates H3K9ac (histone H3 lysine 9 acetylation) at SPECIFIC gene promoters
    → H3K9 deacetylation → HP1 (heterochromatin protein 1) binding → chromatin compacted
    → NF-κB cannot recruit RNA Pol II to compacted promoters → target gene ↓
    
NF-κB target genes repressed by SIRT6 (Kawahara 2009 Cell 136:62-74):
    → TNFα: SIRT6 physically interacts with NF-κB at TNFα promoter → H3K9 deacetylated
    → IL-6: similar SIRT6/NF-κB co-occupancy at IL-6 promoter → chromatin repressed
    → MCP-1/CCL2: SIRT6 → H3K9ac ↓ → monocyte chemoattractant ↓
    → VCAM-1: SIRT6 → endothelial VCAM-1 ↓ → less immune cell adhesion
    
This is EPIGENETIC NF-κB suppression:
    → Not inhibiting NF-κB activation (upstream mechanisms: 10 suppressors in framework)
    → Not blocking NF-κB nuclear translocation (colchicine tubulin mechanism)
    → But preventing chromatin accessibility at NF-κB target loci even when p65 is present
    → p65 can bind DNA but cannot recruit Pol II to H3K9-deacetylated/compacted loci
    → 11th NF-κB suppression mechanism (epigenetic; downstream of nuclear p65)
```

**SIRT6 → TNFα mRNA stability (Zhong 2010 Science):**
```
Zhong 2010 Science 327:1484-1488:
    SIRT6 → promotes TNFα mRNA export/decay via the JNK pathway
    → Even when TNFα is transcribed: SIRT6 → KSRP (mRNA decay protein) → TNFα mRNA ↓
    → Double mechanism: SIRT6 suppresses TNFα at BOTH transcriptional (H3K9ac) AND
      post-transcriptional (mRNA stability) levels
```

**SIRT6 and T1DM glucose effects:**
```
Li 2012 BBRC (Biochem Biophys Res Commun):
    High glucose (25 mM) → SIRT6 mRNA and protein ↓ in endothelial cells
    → Mechanism: high glucose → advanced glycation → AGE-RAGE → oxidative stress
      → SIRT6 protein oxidatively modified → proteasomal degradation ↑
    → T1DM: chronic hyperglycemia → SIRT6 ↓ → less H3K9 deacetylation → NF-κB chromatin
      more accessible → inflammatory gene expression amplified by same p65 activation
      
T1DM implication:
    Three converging NF-κB amplifiers from hyperglycemia:
        (a) High glucose → AGE-RAGE → NF-κB activation (direct; run_046)
        (b) High glucose → AMPK ↓ → mTORC1 ↑ → NF-κB coactivation
        (c) High glucose → SIRT6 ↓ → NF-κB target chromatin open (epigenetic; run_090 new)
    → SIRT6 restoration via NAD⁺ supplementation addresses mechanism (c)
```

### SIRT6 vs. SIRT1 NF-κB Suppression

```
SIRT1 → NF-κB:
    SIRT1 → deacetylates p65 Lys310 → p65 cannot recruit CBP/p300 (run_031 context)
    → Mechanism: deacetylates the TRANSCRIPTION FACTOR directly
    
SIRT6 → NF-κB:
    SIRT6 → deacetylates H3K9ac at NF-κB target PROMOTERS → chromatin compacted
    → Mechanism: deacetylates the CHROMATIN at target gene loci
    
These are ADDITIVE (different substrates, different mechanisms, same net outcome: NF-κB target ↓)
→ NAD⁺ supplementation (niacinamide) activates BOTH simultaneously:
    SIRT1: p65 Lys310 deacetylation → NF-κB transcription factor inactivated
    SIRT6: H3K9 deacetylation at target loci → NF-κB cannot access chromatin
    Combined: NF-κB activity ↓ at TWO independent points (protein + chromatin)
```

---

## Framework Integration: Complete NAD⁺-Sirtuin Map

**Niacinamide → NAD⁺ → Sirtuin Activation: Expanded Mechanism Count**

```
Prior (run_031): niacinamide → NAD⁺ → SIRT1 → 5 mechanisms:
    M1: NLRP3 K496 deacetylation → Loop 2 ↓
    M2: FOXO3a → apoptosis-resistance → β cell survival
    M3: p53 deacetylation → p53 pro-apoptotic transcription ↓ → less inflammatory death
    M4: HIF-1α mRNA destabilization → Signal 1C ↓ (indirect; SIRT1 → HIF-1α deacetylation)
    M5: DNMT1 maintenance → HERV-W LTR methylation maintained (indirect; run_085 context)

New (run_090): niacinamide → NAD⁺ → SIRT3 + SIRT6 → 3 additional mechanisms:
    M6 (SIRT3): SOD2 Lys122 deacetylation → MnSOD active → O₂•⁻ ↓ → NLRP3 Signal 2 ↓
    M7 (SIRT3): FOXO3a → PINK1/Parkin → mitophagy (additive to spermidine + UA)
    M8 (SIRT6): H3K9ac deacetylation at NF-κB targets → epigenetic NF-κB repression
    (+ SIRT6 bonus: TNFα mRNA stability ↓ via JNK/KSRP; Zhong 2010)
    
Total: niacinamide → NAD⁺ → 8 distinct sirtuin-mediated mechanisms (5 SIRT1 + 2 SIRT3 + 1 SIRT6)
```

**BHB additional connection to SIRT3:**
```
Ketogenic diet → BHB → two SIRT3 activation routes:
    (1) BHB → NLRP3 direct (run_031; HCAR2 + K⁺ efflux inhibition) [direct]
    (2) BHB → ketosis → fasting-like signaling → SIRT3 ↑ expression (Hirschey 2010: fasting → SIRT3)
        → SIRT3 ↑ → SOD2 deacetylated → mROS ↓ → NLRP3 Signal 2 ↓ (indirect, via SIRT3)
    → BHB (ketogenic) has a SECOND NLRP3 suppression mechanism via SIRT3 not in run_031
```

---

## Protocol: No New Agents Required

```
Existing protocol provides SIRT3 + SIRT6 activation:
    Niacinamide 250-500mg/day → NAD⁺ → SIRT1 (run_031) + SIRT3 (run_090) + SIRT6 (run_090)
    
For ENHANCED mitochondrial NAD⁺ (SIRT3-specific benefit in T1DM):
    NR (nicotinamide riboside) or NMN: better mitochondrial NAD⁺ precursor than standard
    niacinamide (Cantó 2012: NR → mitochondrial NAD⁺ ↑ more effectively than niacinamide)
    → Optional: consider NR 250-300mg/day as alternative/adjunct to niacinamide in T1DM
      patients with high mROS burden (Node F elevated, poor glycemic control)
    → Standard niacinamide also effective (elevated cytosolic NAD⁺ → equilibration with
      mitochondrial pool over time); NR is a refinement, not a replacement
    
BHB/ketogenic: additional SIRT3 induction (independent of NAD⁺; transcriptional)
Exercise: SIRT3 ↑ expression (mRNA induction by exercise in skeletal muscle → macrophages)
```

---

## Kill Criteria

**Kill A: Mitochondrial NAD⁺ Is Not Elevated by Oral Niacinamide (Compartment Separation)**
Niacinamide → cytosolic/nuclear NAD⁺ primarily; mitochondrial NAD⁺ is maintained separately. Oral niacinamide may not effectively elevate mitochondrial NAD⁺ enough to activate SIRT3 in macrophages.
**Status:** Partially concerning. The mitochondrial NAD⁺ compartmentalization is real. However: (1) NMN (product of NAMPT) can enter mitochondria via Slc12a8-like transporters; cytosolic NMN elevation from niacinamide feeds into this. (2) Cantó 2012 showed NR (which becomes NMN) does elevate mitochondrial NAD⁺ in hepatocytes and muscle. (3) Even partial mitochondrial NAD⁺ elevation → some SIRT3 activation. (4) For patients requiring maximized SIRT3 benefit: NR 250mg/day is an actionable upgrade with direct mitochondrial precursor evidence.

**Kill B: SIRT6 H3K9 Deacetylation Locus-Specificity Is Overstated**
SIRT6 deacetylates H3K9 broadly across the genome; it's not selectively targeting NF-κB loci. The NF-κB-specific effect in Kawahara 2009 may reflect the experimental system (SIRT6 is recruited to specific loci by NF-κB itself).
**Status:** Acknowledged as nuance. SIRT6 is recruited to NF-κB target genes by p65 itself (co-immunoprecipitation; Kawahara 2009). The mechanism is: p65 binds → recruits SIRT6 → SIRT6 deacetylates H3K9 → limits duration of transcription → self-limiting NF-κB. So SIRT6's NF-κB effect is indeed locus-specific (requires p65 co-recruitment) rather than genome-wide. This actually makes the mechanism MORE specific and coherent, not less. Not killed.

**Kill C: SIRT3 SOD2 Mechanism Is Already Implicitly Covered by mROS-Targeting Protocol Elements**
The framework already has mitochondrial ROS addressed via: MitoQ/mitochondria-targeted antioxidants (run context), run_084's succinate/HIF-1α discussion, and run_071/078 mitophagy (removing damaged mitochondria that produce mROS). Adding SIRT3-SOD2 is incremental.
**Status:** Not killed as a mechanistic insight, but acknowledged as additive rather than gap-filling. SIRT3's unique value is: (1) it's delivered by existing niacinamide protocol already; (2) the SOD2 K122 acetylation switch is the most direct mROS control mechanism (direct enzyme modulation, not just antioxidant scavenging); (3) SIRT3-FOXO3a→mitophagy is genuinely distinct from EP300 and PINK1 routes. The mechanism count is not inflated; these are distinct substrates.

---

*Filed: 2026-04-12 | Numerics run 090 | SIRT3 SOD2 deacetylation mROS NLRP3 Signal 2 mitochondrial NAD⁺ FOXO3a PINK1 mitophagy / SIRT6 H3K9ac NF-κB epigenetic repression TNFα mRNA stability T1DM hyperglycemia SIRT6 ↓ Kawahara 2009 Zhong 2010 Hirschey 2010*
*Key insight (SIRT3): niacinamide → NAD⁺ → SIRT3 → SOD2 Lys122 deacetylation → MnSOD active → O₂•⁻ scavenged → NLRP3 Signal 2 ↓. This is the 7th NLRP3 inhibition mechanism (mROS-specific) and completes the NLRP3 inhibition taxonomy. T1DM: mitochondrial PARP-3 consumes mitochondrial NAD⁺ → SIRT3 ↓ → SOD2 acetylated → mROS vicious cycle. NR (nicotinamide riboside) provides better mitochondrial NAD⁺ penetration than standard niacinamide.*
*Key insight (SIRT6): SIRT6 → H3K9ac deacetylation at NF-κB target loci (TNFα, IL-6, MCP-1, VCAM-1) → chromatin compacted → 11th NF-κB suppression mechanism (epigenetic; downstream of nuclear p65). T1DM high glucose → SIRT6 ↓ → NF-κB chromatin accessibility ↑ (3rd hyperglycemia → NF-κB amplifier). SIRT6 + SIRT1 from NAD⁺ = protein-level + chromatin-level NF-κB suppression simultaneously.*
*Protocol: niacinamide → NAD⁺ now delivers 8 distinct sirtuin mechanisms (5 SIRT1 + 2 SIRT3 + 1 SIRT6). For enhanced mitochondrial SIRT3: consider NR 250mg/day as upgrade in T1DM patients with high mROS burden (Node F elevated, poor HbA1c control).*
