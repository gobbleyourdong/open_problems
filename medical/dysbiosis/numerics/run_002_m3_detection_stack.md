# M3 CVB Detection Stack — Sensitivity Analysis
## Run 002 | Numerical Instance | 2026-04-11

> CVB = Coxsackievirus B, specifically the 5'UTR-deleted non-cytolytic persistent form.
> Mapping: each detection method's sensitivity for THIS specific target (persistent low-copy islet-resident virus).
> NOT acute CVB infection — that's a different, easier problem.

---

## The Target: What We're Trying to Detect

```
STANDARD CVB (enterovirus)        PERSISTENT FORM (the clinically relevant one)
─────────────────────────────     ────────────────────────────────────────────
Full genome, ~7.4 kb              5' UTR deleted (hundreds of nucleotides removed)
Replication-competent              Non-cytolytic, defective replication
Detectable in stool               Primarily in pancreatic islets, possibly gut
High copy number (10^6+ in acute) Very low copy (10^3 per gram tissue)
Cleared by immune system          Persists for years/decades
Standard PCR detects it           Standard PCR MISSES it (deleted primer region)
```

Key reference: Krogvold 2015 (DiViD study) — pancreatic biopsies from 6 recent-onset T1DM patients. VP1 protein detected by IHC in 4/6. Viral RNA by ISH in 3/6. First direct detection of persisting enterovirus in human islets in living patients.

---

## Detection Layer 1: Serum Serology (routine clinical, CVB IgG/IgM)

**What it detects:** Prior exposure (IgG) or recent acute infection (IgM). Does NOT detect persistent form.

**Sensitivity for persistent CVB:** ~0%
- IgG: 80-90% of adults are seropositive for one or more CVB serotypes. A positive IgG means "exposed at some point." Non-informative for persistence.
- IgM: positive only during acute infection (first 4-6 weeks). Persistent carrier with 5'UTR-deleted form: IgM negative.

**Current clinical availability:** Routine. $30-80.

**Verdict:** USELESS for detecting persistence. Use only for ruling in acute infection.

---

## Detection Layer 2: Standard Stool PCR (enterovirus PCR, routine virology)

**What it detects:** Replication-competent enterovirus shed in stool. Targets 5' UTR conserved region.

**Sensitivity for persistent CVB:** ~0%
- 5' UTR primers: target the DELETED region. Will NOT amplify the persistent form.
- Even if 3' UTR or capsid-region primers used: the persistent virus is in islets, not actively shedding to stool at detectable copy numbers.
- Stool viral load of persistent islet-resident CVB: likely below detection limit of PCR (<10^2 copies/mL stool)

**Current clinical availability:** Routine virology labs. $50-150.

**Verdict:** MISSES the persistent form both by primer design AND by sampling location. Standard clinical virology cannot detect this.

---

## Detection Layer 3: TinyHealth FASTQ (what the user ordered)

**What it detects (depends on kit type):**

| TinyHealth kit type | CVB detection capacity |
|--------------------|----------------------|
| 16S rRNA amplicon (most common) | NONE — bacteria only, no virome |
| Shotgun metagenomics (DNA) | Cannot detect RNA viruses without cDNA step |
| Metatranscriptomics (RNA-seq) | THEORETICALLY could detect CVB RNA if gut-replicating, but persistent islet form NOT expected in stool at detectable abundance |

**Practical conclusion:** TinyHealth FASTQ almost certainly contains:
- Bacterial community composition (16S or shotgun bacterial)
- Possibly fungal reads (if shotgun)
- NO CVB information

**What IS valuable from TinyHealth FASTQ:**
- F. prausnitzii relative abundance (M4 proxy)
- Akkermansia muciniphila relative abundance (M4 proxy)
- Butyrate pathway gene presence (butyryl-CoA transferase if shotgun)
- Overall diversity (Shannon index) — gut dysbiosis measure for M1
- Bacterial dysbiosis markers (Proteobacteria bloom, Firmicutes:Bacteroidetes ratio)

**Verdict:** TinyHealth is M1/M4 data, not M3 data. Do not expect CVB information.

---

## Detection Layer 4: Virome-Enriched Sequencing (research grade)

**What it detects:** RNA viruses, low-titer DNA viruses, bacteriophage. With proper preparation:
- Host depletion (removes human DNA/RNA)
- RNA capture (poly-A selection or random hexamer RT)
- Deep sequencing (100× standard depth)

**Sensitivity for persistent CVB (stool source):**
- If virus is shedding in gut at any level: potentially detectable
- Problem: the DiViD study showed CVB in ISLETS. Does it shed from islets to gut to stool? Unknown.
- Some evidence that enterovirus can persist in gut mucosa alongside islets (Oikarinen 2012 — intestinal mucosal biopsies positive for enterovirus in T1DM)
- If gut mucosa positive: virome-enriched stool sequencing MIGHT detect it

**Protocol for detecting 5'UTR-deleted form specifically:**
- Need custom bioinformatics: align reads to CVB reference with 5' end soft-clipping
- Standard alignment would discard reads from the deleted region (no reference match)
- Special primer-free detection (de novo assembly from reads) could identify truncated genome

**Cost:** $500-2000/sample. Research labs only. Not clinically available.

**Verdict:** BEST non-invasive option but research-grade, expensive, and requires specialized bioinformatics. Sensitivity unknown for the islet-resident persistent form specifically.

---

## Detection Layer 5: IFN-α / Type I Interferon Signature (indirect proxy)

**What it detects:** Persistent viral infection activates innate antiviral response → constitutive IFN-α production → upregulation of interferon-stimulated genes (ISGs).

**The IFN signature:**
- MX1, IFIT1, IFIT2, IFIT3, OAS1, OAS2, OAS3, RSAD2 (Viperin), ISG15
- These genes are upregulated in both blood cells (PBMCs) and tissues in response to viral infection
- In T1DM: an IFN-α signature is detectable in pancreatic islets (Richardson 2021 — transcriptomics of T1DM islets show high IFN-α stimulated gene expression)
- In blood: IFN-α signature elevated in ~50-60% of T1DM patients vs controls

**Clinical availability:** NanoString IFN gene panel, or custom RT-PCR panel on PBMCs. Research/specialty labs. ~$200-500.

**Sensitivity for CVB persistence:** ~40-60% (estimated from T1DM cohort data)
- Not specific to CVB — any persistent viral infection would trigger IFN signature
- EBV reactivation, HHV-6 persistence, or other virome activity also elevates IFN
- But in the T1DM context, CVB is the most likely driver

**Verdict:** BEST AVAILABLE indirect proxy for "is there a persistent viral infection?". Not specific to CVB but relevant in T1DM context.

---

## Detection Layer 6: Islet Tissue (gold standard, not feasible)

**What it detects:** VP1 capsid protein (IHC), viral RNA (ISH/FISH), full-length and truncated genome (RT-PCR with 3' UTR primers).

**Methods:**
1. VP1 immunostaining — Krogvold 2015, Richardson 2009 — most published data
2. In situ hybridization for CVB RNA — localizes virus to islet beta cells
3. Proximity ligation assay — detects viral dsRNA (replication intermediate)
4. Single-cell transcriptomics — recent; identifies islet cells with viral gene expression

**Why not feasible clinically:**
- Requires pancreatic biopsy (significant procedural risk: pancreatitis, bleeding)
- Or post-mortem tissue (available only in research consortia: nPOD, DiViD, INNODIA)
- Cannot be done routinely or for individual patient management

**Sensitivity:** ~50-60% in T1DM vs ~5-15% in controls (for VP1 IHC)

**Verdict:** Gold standard but inaccessible. Reference point only.

---

## Detection Summary Table

| Method | Sensitivity for persistent CVB | Clinical availability | Cost | User relevance |
|--------|-------------------------------|----------------------|------|----------------|
| CVB IgG serology | ~0% (exposure only) | Routine | $30-80 | None for persistence |
| CVB IgM serology | ~0% (acute only) | Routine | $30-80 | None unless acute |
| Stool PCR (5'UTR) | ~0% (wrong primers + wrong tissue) | Routine | $50-150 | None |
| Stool PCR (3'UTR/capsid) | <10% (low copy in stool) | Research | $100-300 | Marginal |
| TinyHealth FASTQ (16S/shotgun) | ~0% | Consumer | $200-400 | None for CVB |
| Virome-enriched sequencing | Unknown (maybe 20-40%) | Research | $500-2000 | Future option |
| IFN-α gene signature (blood) | ~50-60% (indirect) | Specialty lab | $200-500 | BEST CURRENT OPTION |
| Pancreatic biopsy + VP1 IHC | ~50-60% in T1DM | Research only | N/A | Not feasible |

---

## Best Available Protocol for CVB Persistence Testing (User Context)

Given constraints (no research lab access, no pancreatic biopsy):

**Step 1 (cheap, indirect):** IFN-α2 serum protein (ultrasensitive ELISA) + ISG15 mRNA in PBMCs
- Order from specialty immunology lab
- Elevated → suggests persistent viral trigger
- Normal → doesn't rule out persistence (IFN response can be suppressed)

**Step 2 (medium, indirect):** Stool virome-enriched sequencing
- Kraken2 analysis of shotgun reads + de novo assembly
- Requires the sample to contain detectable CVB (uncertain)
- Emerging commercial options: Microbial Research 16S + virome add-on ($400-600)

**Step 3 (research, if partnership available):** nPOD (Network for Pancreatic Organ Donors with Diabetes)
- Not for living patients
- Research consortium for post-mortem islet tissue
- Relevant for understanding mechanisms, not individual management

**Current status of user's CVB protocol:** Running blind — no direct detection of CVB persistence has been established. The protocol makes mechanistic sense (blocking viral replication via OSBP cholesterol delivery + host NF-κB/NLRP3 suppression) but is not confirmed by detection of the virus it targets.

---

## Sky Bridge: EBV-MS Evidence Applied to CVB-T1DM

Bjornevik 2022 (EBV-MS): prospective military cohort, 10 million subjects.
- Design: serum samples banked before MS diagnosis → tested for EBV antibody status
- Result: 32× MS risk increase after EBV seroconversion; 0 MS cases in EBV-seronegative

**Analogous study for CVB-T1DM:** Does not yet exist at this scale.
- What would it look like: prospective cohort, stool enterovirus sampling + IFN signature in first-degree T1DM relatives → track autoantibody emergence → T1DM onset
- TEDDY study partially does this: follows at-risk children, but CVB detection method is standard PCR (misses persistent form)

**The sky bridge:** Same prospective-cohort study design that proved EBV-MS should be deployed for CVB-T1DM with virome-enriched methods. This has not happened at scale.

---
*Run 002 M3 CVB detection stack: direct detection is not currently possible outside research. Best proxy: IFN-α gene signature. TinyHealth FASTQ = M1/M4 data, not M3 data.*
