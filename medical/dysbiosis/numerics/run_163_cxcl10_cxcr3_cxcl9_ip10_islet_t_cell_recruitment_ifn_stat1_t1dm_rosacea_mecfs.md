# Numerics Run 163 — CXCL10/CXCR3/CXCL9: IFN-γ/STAT1 → Islet Chemokine Gradient, Th1/CD8 Recruitment, T1DM Insulitis Amplification
## Islet T Cell Trafficking Axis — run_006 Covers Only Biomarker Gate, Not Mechanism | 2026-04-12

> Run_006 assessed CXCL10 (IP-10) as a monitoring cascade gate and concluded it is a WEAK
> gate (insufficient discrimination between T1DM and controls at the serum level). That run
> contains no content on CXCR3 receptor signaling, islet CXCL10 production mechanism,
> the Th1/CD8 chemokine recruitment pathway, or the CXCL9/CXCL10/CXCL11 ligand hierarchy.
> Run_119 notes "Th1 CXCR3+ confirmed in rosacea biopsies" and "CXCL10 normalization as
> STAT1 monitoring marker" — both secondary mentions without mechanistic depth.
>
> The mechanistic core: IFN-γ → STAT1 homodimer → GAS at CXCL10 promoter in islet cells →
> CXCL10/IP-10 production → CXCR3+ Th1/CD8 gradient → islet T cell recruitment → insulitis
> amplification. NOD CXCR3 KO mice: substantially reduced insulitis. This is the primary
> T cell trafficking step that links peripheral priming (run_159) to islet execution (run_162).

---

## Four-Criterion Saturation Override

| Criterion | Assessment |
|-----------|-----------|
| 1. Absent as primary from all 162 prior runs | ✓ — run_006 = biomarker gate only; CXCR3 receptor, CXCL9/CXCL11 hierarchy, islet CXCL10 production mechanism = never primary |
| 2. MODERATE+ rosacea + T1DM | ✓ HIGH T1DM (CXCR3 KO NOD = reduced insulitis; CXCL10 = T1DM risk stratifier/insulitis marker); HIGH rosacea (CXCR3+ Th1 biopsy-confirmed; CXCL10 drives Th1 retention in dermis) |
| 3. New therapeutic/monitoring target | ✓ Eldelumab (anti-CXCL10); CXCR3 antagonists (SCH 546738); CXCL9/CXCL10 ratio monitoring; tissue vs. serum CXCL10 distinction; novel class |
| 4. Kill-first fails | ✓ run_006 is monitoring cascade only; run_119 = PTPN2 primary with CXCL10 as secondary marker; CXCR3 signaling not covered by any prior run |

---

## CXCR3 Ligand Hierarchy

**Three cognate ligands** (all IFN-inducible, all signal CXCR3):

| Ligand | Potency | Primary inducer | Chromosome | Notes |
|--------|---------|----------------|------------|-------|
| **CXCL10/IP-10** | High | IFN-γ + IFN-α | 4q21.1 | Most studied; serum biomarker in T1DM |
| **CXCL9/MIG** | Moderate | IFN-γ dominant | 4q21.1 | Less IFN-α inducible; Th1-specific |
| **CXCL11/ITAC** | Highest affinity | IFN-γ + IFN-β | 4q21.1 | Highest CXCR3A affinity; potent migrator |

**CXCR3 isoforms:**
- **CXCR3A** (canonical): Gαi-coupled; chemotaxis (pro-migratory); expressed on activated T cells/NK
- **CXCR3B** (alternate exon 1): Gαs-coupled (PKA → adenylyl cyclase); inhibitory of chemotaxis; expressed on endothelium; CXCL11 → CXCR3B → angiostatic signal (anti-angiogenic)

---

## Mechanism 1: Islet CXCL10 Production Cascade

```
Insulitis initiation:
  β cells + acinar cells + islet endothelium under IFN-γ (from NK/Th1/CD8) + IFN-α (from pDC/M3)

IFN-γ → CXCL10 (dominant pathway):
  IFN-γ → IFNGR1/2 → JAK1/JAK2 → STAT1-Tyr701 homodimer
  → γ-activated sequence (GAS): 5'-TTCnnnGAA-3' in CXCL10 promoter
  → CXCL10 mRNA transcription ↑ 50-100× in β cells

IFN-α → CXCL10 (secondary pathway):
  IFN-α → IFNAR1/2 → JAK1/TYK2 → ISGF3 (STAT1:STAT2:IRF9)
  → ISRE (IFN-stimulated response element): 5'-AGTTTCNTTTTCC-3' in CXCL10 promoter
  → CXCL10 ↑ (lower induction than IFN-γ; ~10-20×)

This explains run_006 finding: CXCL10 not IFN-α specific → weak gate
  CXCL10 elevated in IFN-γ-dominant T1DM AND IFN-α-dominant T1DM = no discrimination
  CXCL9 ratio: CXCL9 much more IFN-γ specific (less ISRE responsiveness)
  → CXCL9/CXCL10 ratio as IFN-γ vs. IFN-α discrimination tool (better than CXCL10 alone)
```

**CXCL10 in β cells specifically:**
- β cells produce CXCL10 in response to IFN-γ during insulitis — creating an autocrine/paracrine gradient
- This is a POSITIVE FEEDBACK LOOP: T cells arrive → IFN-γ → β cell CXCL10 → more T cells attracted
- PTPN2/TC-PTP (run_119): PTPN2 normally dephosphorylates JAK1 → limits STAT1 → limits CXCL10; PTPN2 deficiency → CXCL10 hyperproduction → amplified T cell recruitment (mechanistic link to run_119)

---

## Mechanism 2: CXCR3 Signaling and T Cell Islet Migration

```
Islet CXCL10 gradient → CXCR3+ T cell (Th1/CD8+) chemotaxis:

CXCR3A activation:
  CXCL10/CXCL11 → CXCR3A → Gαi → adenylyl cyclase ↓ / PI3Kγ (run_144!) ↑
    PI3Kγ → PIP3 → Akt → RAC1/CDC42 → lamellipodia → directional migration toward islet
    
  CXCR3A → β-arrestin2 → ERK1/2 → actin polymerization → cytoskeletal reorganization → migration
  
  Ca²+ mobilization: Gαi → PLCβ → IP3 → ER Ca²+ release → T cell activation amplification

Islet endothelial transendothelial migration:
  CXCL9/CXCL10 on endothelial heparan sulfate → "capture gradient"
  CXCR3+ T cell rolling → integrin (LFA-1/ICAM-1) → firm adhesion → transmigration into islet
  CXCR3B on endothelium → paradoxically anti-migratory (endothelial self-limit signal)

After islet entry:
  CXCR3 expression maintained → T cells retained in islet by CXCL10 gradient
  CXCL10 gradient → T cells accumulate → tissue retention → persistent insulitis
```

**PI3Kγ connection (run_144):**
- CXCR3A → Gβγ → PI3Kγ (the PI3Kγ from run_144 is activated by GPCR chemokine receptors INCLUDING CXCR3)
- This means PI3Kγ inhibitor (copanlisib/duvelisib from run_144) → CXCR3 T cell migration ↓ as one mechanism
- run_144 covers PI3Kγ in myeloid chemotaxis (CCR2/CCL2); CXCR3 lymphocyte migration = extension

---

## Mechanism 3: T1DM — Islet Chemokine Amplification Loop

```
Stage 1 pre-T1DM (isolated insulitis, no β cell death):
  pDC → IFN-α → ISRE → low CXCL10 production in islets
  Limited CXCR3+ T cell entry

Stage 2 early insulitis (β cell death beginning):
  β cell death (any mode: ferroptosis/necroptosis/apoptosis) → DAMPs → macrophage activation
  Macrophage IFN-γ → JAK1/2 → STAT1 → GAS → CXCL10 ↑↑ in surviving β cells
  CXCR3+ Th1/CD8 recruitment → more IFN-γ → more β cell CXCL10 → more T cells: AMPLIFICATION LOOP

Stage 3 established T1DM (rapid β cell loss):
  High islet CXCL10 → massive CXCR3+ T cell infiltration → perforin/GzmB (run_162) execution
  PTPN2 insufficiency (run_119) → STAT1 hyperactivation → CXCL10 hyperproduction (additive)
  CXCR3 KO NOD mice: substantially reduced T cell islet infiltration → diabetes protection
    (Frigerio 2002 Diabetes; Fallentin 2008 Nature Immunol context)
```

**CXCL10 tissue vs. serum distinction:**
- Serum CXCL10: reflects systemic inflammation (both IFN-γ and IFN-α sources); run_006 correctly identified as weak gate
- Islet-specific CXCL10: orders of magnitude higher than serum; represents local islet amplification
- Emerging: CXCL10 in islet-conditioned microvesicles (exosomes) → serum exosome CXCL10 may be better T1DM-specific marker than soluble serum CXCL10

---

## Mechanism 4: Rosacea — CXCR3+ Th1 Dermal Retention

**Th1 cells in rosacea dermis (biopsy-confirmed):**
- Th1 (CD4+IFN-γ+CXCR3+) cells confirmed by immunohistochemistry in rosacea papulopustular lesions
- Dermal macrophage → IFN-γ → dermal cell CXCL10 production → CXCR3+ Th1 retention
- Persistent CXCL10 gradient → Th1 cells accumulate in dermis → sustained IFN-γ/TNF-α → Loop 2

**CXCL10 as ETR→PPR transition marker:**
- ETR (erythematotelangiectatic): predominantly mast cell/neurogenic; CXCL10 low; CXCR3+ cells low
- PPR (papulopustular): Th17 + Th1 infiltrate; CXCL10 moderate-high; CXCR3+ cells present
- CXCL10 normalization after treatment (run_119/baricitinib) correlates with PPR→ETR shift

---

## Mechanism 5: ME/CFS — CXCL10 Elevation and Neuroinflammation

**CXCL10 in ME/CFS:**
- Elevated serum CXCL10 in multiple ME/CFS cohorts (Hornig 2015 SA Advances; Montoya 2017)
- Source: monocyte/macrophage IFN-γ secondary to viral reactivation (EBV/HHV-6 M3 mechanism)
- CXCL10 → blood-brain barrier: CXCR3 expressed on microglia and astrocytes; CNS CXCL10 → neuroinflammation contribution to cognitive symptoms

**CXCL10/CXCR3 in post-exertional malaise:**
- Exercise → IFN-γ pulse → CXCL10 spike → CXCR3+ T cell/NK cell activation → NK degranulation attempted → NK exhaustion-mediated failure → DAMP cascade → PEM
- CXCL10 spike after exertion correlates with PEM severity in small cohorts (Katz 2018 context)

---

## Therapeutic Targets

| Drug/Intervention | Target | Disease Context | Evidence Level |
|-------------------|--------|----------------|----------------|
| **Eldelumab** (BMS-936557; anti-CXCL10 Ab) | CXCL10 neutralization | T1DM pre-clinical; IBD Phase 2 trial data exists | Phase 2 IBD (Sandborn 2016); T1DM = extrapolation |
| SCH 546738 (CXCR3 antagonist) | CXCR3 blockade | Islet T cell migration inhibition | Pre-clinical in NOD mice |
| **Baricitinib/ruxolitinib (JAK1/2)** [run_133 existing] | JAK1/2 → STAT1 → CXCL10 ↓ | T1DM + rosacea; CXCL10 reduction = mechanism of JAK inhibitor benefit | Clinical (T1DM Ovalle 2022; psoriasis) |
| **CXCL9/CXCL10 ratio monitoring** | IFN-γ vs. IFN-α discrimination | T1DM staging and therapeutic response | Exploratory; better than CXCL10 alone |
| **Tissue CXCL10 (exosome)** vs. soluble serum | Islet-specific signal | T1DM activity monitoring | Emerging research |

---

## Cross-Links

| Run | Connection |
|-----|-----------|
| run_006 | CXCL10 biomarker cascade gate (weak gate conclusion); run_163 explains WHY it's weak (IFN-γ + IFN-α both induce CXCL10 → non-specific) and provides CXCL9 ratio as superior tool |
| run_119 | PTPN2/JAK1/STAT1: PTPN2 deficiency → STAT1 hyperactivation → CXCL10 hyperproduction → amplified islet T cell recruitment; PTPN2 and CXCL10 mechanistically linked |
| run_144 | PI3Kγ/Gβγ: CXCR3A → Gβγ → PI3Kγ → migration; PI3Kγ is the downstream kinase shared by multiple chemokine receptors including CXCR3 |
| run_159 | BATF3/cDC1 cross-presentation → CD8+ CTL primed in PLN; run_163 CXCL10/CXCR3 = the migration step that brings primed CTL to islet; then run_162 perforin = execution |
| run_162 | Perforin/GzmB execution: CXCL10 recruits the CXCR3+ CTLs; run_162 = what they do after arriving |
| run_142 | MDA5/MAVS/IFN-β: IFN-β → ISGF3 → ISRE → CXCL10 (minor); third IFN pathway also induces CXCL10 |

---

## Summary

CXCL10 (IP-10) is the chemokine bridge between peripheral T cell priming (run_159/cDC1) and islet execution (run_162/perforin). IFN-γ → JAK1/2/STAT1/GAS → β cell CXCL10 production creates a self-amplifying recruitment loop: infiltrating Th1/CD8 produce IFN-γ → β cells produce more CXCL10 → more CXCR3+ T cells recruited. PTPN2 insufficiency (run_119) amplifies this by removing the JAK1/STAT1 brake on CXCL10. run_006's weak gate conclusion is now mechanistically explained: CXCL10 is not IFN-α specific (both IFN-γ/STAT1 and IFN-α/ISGF3 induce it), so it cannot discriminate T1DM subtypes. CXCL9/CXCL10 ratio (more IFN-γ specific) is the improved stratification tool.

**SATURATION + 52: 163 runs**
