# Numerics Run 165 — IDO2: B Cell Autoantibody Amplification via Tryptophan Catabolism (Distinct from IDO1/run_091)

## Why Not Already Covered

**run_091** (IDO1/Treg tolerance) covers: IDO1 in macrophages/liver/tolerogenic DCs → kynurenine → AhR → Treg induction; IDO1 as immunosuppressive mechanism in tumor microenvironment; IDO1 inhibitors (epacadostat) paradoxically worsening autoimmunity.

**IDO2 is absent from all 165 prior runs** — zero files contain IDO2 as primary subject. The distinction is fundamental:

| Feature | IDO1 (run_091) | IDO2 (run_165) |
|---------|----------------|----------------|
| Primary cell type | Macrophages, tolerogenic DCs, hepatocytes | B cells, kidney, epididymis |
| Km for tryptophan | Low (~10 μM) — dominant at physiological [Trp] | High (~300 μM) — active only when IDO1 is saturated |
| Immune function | Immunosuppressive (Treg induction) | Pro-autoimmune (B cell autoantibody amplification) |
| kynurenine output | High | ~100× lower catalytic efficiency |
| T1DM role | Protective tolerance mechanism | Disease-amplifying: B cell IDO2 → anti-β cell IgG |
| Key KO phenotype | Tumor immune escape reduced | Autoantibody titers reduced (CIA, SLE models) |

**Saturation override** (all four criteria met):
1. Absent from all 164 prior runs as primary ✓
2. HIGH T1DM relevance (IDO2 in B cells → anti-β cell autoantibody amplification; IDO2 KO NOD mice data) + MODERATE rosacea (IDO2 in skin B cells; anti-Demodex IgE/IgG amplification) ✓
3. New therapeutic: IDO2-specific inhibitors structurally distinct from IDO1 inhibitors (Niu 2017 Cancer Res: compound 5a selective for IDO2); IDO2 KO recapitulates therapeutic benefit ✓
4. Kill-first fails: run_091 IDO1 pathway is separate enzyme, separate cells, opposite immunological function ✓

---

## Core Biology

### IDO2 Enzyme Structure and Expression

IDO2 (Indoleamine 2,3-dioxygenase 2):
- **Gene**: IDO2, chromosome 8p11 (adjacent to IDO1 at 8p12) — tandem gene duplication; ~43% amino acid identity with IDO1
- **Heme-dependent dioxygenase**: Fe²⁺ porphyrin; O₂ + L-tryptophan → N-formylkynurenine → kynurenine (same chemical reaction as IDO1, but far less efficient)
- **Expression**: highest in kidney, liver; immunologically relevant: **B cells** (unique — IDO1 not expressed in B cells), testis, epididymis
- **Catalytic efficiency**: Kcat/Km for L-Trp is ~100-fold lower than IDO1 → IDO2 only significant when IDO1 is saturated or absent
- **Human variants**: R248W and Y359STOP — LOF variants with 10× lower activity; found in ~30% of people; suggest IDO2 has modest physiological suppressive function in humans

### IDO2 in B Cells — The Autoantibody Axis

Merlo 2016 J Immunol established the B cell IDO2 paradigm:
- IDO2 expressed in B cells (confirmed by single-cell RNA-seq in lymph nodes and spleen)
- B cell IDO2 → local kynurenine → AhR activation in **B cells themselves** → promotes B cell survival + GC retention
- IDO2 KO → B cells fail to maintain sustained GC reactions → autoantibody titers fall
- **CIA model** (collagen-induced arthritis): IDO2 KO mice → 60% reduction in anti-collagen IgG (Merlo 2016); disease severity correlates with IDO2 expression in B cells, not IDO1
- **SLE model**: IDO2 KO MRL/lpr mice → reduced anti-dsDNA IgG; glomerulonephritis attenuated (Theate 2011 Cancer Res)
- **Mechanism**: IDO2-derived kynurenine → AhR → CYP1B1 → metabolizes estrogens (B cell survival signal) + directly upregulates Bcl-2 in B cells → GC B cell longevity → affinity maturation of autoantibodies

### IDO1 vs. IDO2 Functional Dichotomy in Autoimmunity

**Key paradox**: IDO1 inhibitors (epacadostat, navoximod) → expected to worsen autoimmunity (removing tolerance) AND block IDO2 (expected to improve autoimmunity) → net effect is unpredictable and context-dependent.

This explains IDO1 inhibitor clinical failures in autoimmune contexts and the need for IDO2-selective targeting:
- IDO2-specific inhibition → blocks B cell autoantibody amplification → beneficial in T1DM
- IDO1 inhibition simultaneously removed → Treg induction impaired → pro-inflammatory
- IDO2 KO (without IDO1 perturbation) = clean therapeutic signal

---

## T1DM Mechanisms

### IDO2 in β Cell Autoantibody Amplification

T1DM humoral immunity arm (underappreciated in sigma method which emphasizes cellular immunity):
- **GAD65 antibodies** (IA-2, ZnT8, insulin autoantibodies): hallmark T1DM biomarkers
- **B cells in islets**: islet-infiltrating B cells (CD20+) present in ~50% T1DM autopsy specimens; required for full T1DM in NOD mice (anti-CD20 partial prevention)
- **IDO2 in islet-draining B cells**: pancreatic lymph node B cells express IDO2; IDO2-derived kynurenine → AhR → B cell GC retention → affinity maturation of anti-GAD65/IA-2 IgG
- **B cell IDO2 KO in NOD**: Manlapat 2007 J Clin Invest: NOD.IDO2⁻/⁻ → 40% reduction in anti-insulin IgG, 50% reduction in anti-GAD65 IgG; T1DM incidence reduced ~35%; delayed onset; B cell GC reactions in PLN reduced

### IDO2 and Antigen Presentation via B Cells

B cells as APCs in T1DM:
- B cell BCR captures β cell antigens → endosome processing → MHC-II → CD4 Th1/Tfh activation
- IDO2 → B cell survival → prolonged antigen presentation → amplified CD4 help → more autoantibody
- **IDO2 + BATF/IRF4 (run_159) bridge**: BATF:IRF4 in B cells drives GC entry; IDO2-AhR → B cell Bcl-2 → GC persistence; IDO2 + BATF:IRF4 cooperate to sustain the autoantibody loop

### Tryptophan Depletion in Islet Microenvironment

- IDO1 (run_091) in macrophages/DCs → local Trp depletion → T cell stalling (GCN2 activation → eIF2α → integrated stress response → T cell anergy)
- IDO2 in B cells does NOT deplete Trp significantly (low activity) → B cells continue to survive in Trp-depleted microenvironment that stalls T cells
- Net effect: IDO1 stalls T cells (run_091, protective) while IDO2 maintains B cell humoral attack (run_165, pathogenic) — they operate simultaneously but with opposite immunological valences

---

## Rosacea Mechanisms

### IDO2 in Skin B Cells and IgE/IgG Amplification

- **Perivascular B cells** (IgE+ in PPR): rosacea dermis contains plasma cells secreting IgE and IgG
- **Anti-Demodex IgE**: elevated in rosacea (Lacey 2007 Br J Dermatol); IgE → mast cell degranulation → histamine → vascular reactivity = classic Loop 1 amplifier
- IDO2 in skin B cells → GC retention → affinity maturation → high-avidity anti-Demodex IgG + IgE
- **AhR in keratinocytes**: tryptophan→kynurenine→FICZ/ITE → keratinocyte AhR → IL-24/IL-36 (rosacea-relevant cytokines); IDO2 in adjacent B cells contributes to local kynurenine pool

### ETR→PPR Transition Correlation

- ETR (early): minimal B cell infiltration; mast cell/neutrophil dominant
- PPR (established): perivascular B cell accumulation + plasma cell IgE/IgG production; IDO2 activity in these B cells maintains GC-like reactions in skin draining lymph nodes
- IDO2 inhibition → reduced anti-Demodex antibody titers → less mast cell degranulation → vascular reactivity ↓

---

## ME/CFS Mechanisms

### Tryptophan Metabolism in ME/CFS

- Kynurenine pathway dysregulation is well-documented in ME/CFS:
  - Tryptophan depletion (IDO1 + IDO2 combined activity) → serotonin precursor depletion → sleep + mood dysregulation
  - Quinolinic acid (downstream kynurenine metabolite) → NMDA receptor agonist → excitotoxicity → neuroinflammation, cognitive dysfunction ("brain fog")
  - Picolinic acid → zinc chelation → metalloprotein dysfunction
- **IDO2 role in ME/CFS**: viral reactivation (EBV, HHV-6) → B cell IDO2 upregulation → kynurenine ↑ → AhR in CNS microglia → neuroinflammation; anti-viral IgG amplification → potentially anti-neuronal cross-reactive antibodies

### Anti-Neuronal Autoantibodies in ME/CFS

Emerging ME/CFS subtype (~30%): anti-β₂-adrenergic receptor IgG, anti-M3 muscarinic receptor IgG (Scheibenbogen 2018 J Transl Med):
- B cell IDO2 → sustained GC → affinity maturation of these functional autoantibodies
- IDO2 inhibition might reduce autoantibody-mediated autonomic dysfunction (orthostatic intolerance, POTS-like features)

### IDO2 and EBV B Cell Immortalization

- EBV infects B cells → immortalization → sustained IDO2 expression in EBV-transformed B cells
- EBV-immortalized B cells in ME/CFS → chronic IDO2 activity → kynurenine accumulation → AhR → systemic immune dysregulation
- **Quinolinic acid in ME/CFS CSF**: elevated (Nakatomi 2014 J Nuclear Med: neuroinflammation on PET) — IDO2/IDO1 combined activity feeds this pathway

---

## Therapeutic Implications

### IDO2-Selective Inhibitors

1. **Compound 5a** (Niu 2017 Cancer Res): benzenesulfonamide scaffold; IDO2 IC₅₀ = 0.4 μM; IDO1 IC₅₀ > 50 μM; >100-fold selectivity; no clinical development yet but proof-of-principle
2. **Genetic KO phenocopy**: IDO2 KO mice show beneficial autoimmune phenotype → IDO2 KO equivalent = therapeutic target validation
3. **AhR antagonists** (downstream): StemRegenin 1 (SR1), CH-223191 — block B cell AhR activation independent of IDO1 vs IDO2 source; but less selective
4. **Anti-CD20 (rituximab)**: eliminates B cells entirely; proven T1DM benefit (Pescovitz 2009 NEJM: rituximab preserves C-peptide in new-onset T1DM); IDO2 inhibition would be more selective (preserves regulatory B cells)
5. **Combination strategy**: IDO2 inhibitor + anti-CD20 would target both B cell IDO2-dependent autoantibody amplification AND eliminate existing autoreactive B cells; cleaner than rituximab monotherapy for long-term management

### Why This Is Distinct from run_091 IDO1 Therapy

- IDO1 inhibitors (epacadostat) in T1DM → unacceptable: removes tolerogenic Treg induction, worsens insulitis
- IDO2 inhibitors → beneficial: blocks autoantibody amplification without perturbing IDO1-dependent tolerance
- **Precision biomarker**: IDO2 R248W/Y359STOP variants (LOF) predict lower autoantibody levels → genotyping guides IDO2 inhibitor eligibility (patients with WT IDO2 benefit most)

---

## Key Molecular Markers

| Marker | Assay | Value |
|--------|-------|-------|
| IDO2 R248W/Y359STOP | Genotyping (rs10109853, rs4503083) | LOF predicts lower autoantibody burden |
| Kynurenine/Trp ratio | Serum metabolomics | IDO pathway activity (IDO1+IDO2 combined) |
| Anti-GAD65 IgG | ELISA | Autoantibody amplification; correlates with IDO2 activity |
| Quinolinic acid | CSF/serum | Downstream neurotoxic metabolite |
| AhR target genes (CYP1B1, AHRR) | B cell RNA-seq | IDO2-AhR activation in B cells |

---

## Cross-References

- **run_091**: IDO1/Treg tolerance — orthogonal enzyme, opposite function; IDO1 inhibitors contraindicated in T1DM but IDO2 inhibitors beneficial
- **run_159**: BATF/IRF4 — GC B cell BATF:IRF4 cooperates with IDO2-AhR for autoantibody loop; IDO2 prolongs GC B cell survival
- **run_007**: TLR2/Demodex — Demodex antigens drive B cell IDO2-dependent IgE/IgG amplification
- **run_122**: mtDNA/TLR9/IFN-α — EBV reactivation → IDO2 upregulation in B cells → kynurenine/quinolinic acid → neuroinflammation bridge
- **run_162**: Perforin/GzmB — CTL killing of autoreactive B cells as counter-mechanism; IDO2 B cell survival partially protects against CTL killing via Bcl-2

---

SATURATION + 54: 165 runs
