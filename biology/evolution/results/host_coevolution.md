# Host-Side Coevolution with the Persistent-Organism Set

> Synthesis note. The persistent-organism framework has so far
> focused on the organism side — per-organism phylogeny, persistence
> mechanisms, disease associations. The host side is the
> complementary picture: human immune-system genes that show
> measurable signatures of long-term selection by the very
> organisms on this list. This note pulls together scattered
> mentions across attempts 002–010 into a unified picture.
>
> **VERIFICATION STATUS:** structural claims (categories of
> coevolution, specific gene–organism pairings named below) are
> drawn from the per-organism attempts. Five of those attempts
> have had audit passes; 5 are still at trained-prior level.
> Specific effect sizes and PMIDs require audit-loop verification.
>
> Companion: `results/persistence_mechanisms_taxonomy.md`;
> attempts 001–010.

---

## The claim

**A measurable fraction of human adaptive + innate immune gene
diversity has been shaped by selection from the persistent-organism
set.** Specifically:

- **HLA polymorphism** — driven disproportionately by persistent
  viruses (EBV, HCMV, HIV) that establish chronic antigen exposure
- **KIR / NK-cell receptor diversity** — driven largely by HCMV
  counter-immunology
- **TRIM5α, APOBEC3G, BST-2, SAMHD1, MX1, and other intrinsic
  restriction factors** — show positive-selection signatures
  consistent with retroviral + persistent viral exposure
- **HERVs (human endogenous retroviruses) — 8%+ of the human
  genome** — the terminal state of class-5 (integration with
  germline transmission) persistence
- **Cytokine pathway polymorphisms** — IL-1β, IL-6, TNF variants
  affect disease-progression given persistent-organism infection
- **Innate-immunity receptors** — TLR2, TLR4, NOD1/2 variants
  modulate response to bacterial + fungal persistent organisms
- **Blood group antigens** — ABO, Lewis antigens are bacterial-
  adhesion ligands; frequency distributions are partly selected by
  bacterial pathogens

The argument here is not "every immune polymorphism is
persistent-organism driven" — that would be false, and other
forces (acute zoonoses, parasitic infections outside the list,
non-immune selection) matter too. The argument is that **the
persistent-organism set is a major co-driver alongside these other
forces, and specific signatures can be mapped to specific organisms.**

---

## HLA polymorphism — class I + class II

The MHC / HLA locus is the most polymorphic region of the human
genome. Evolutionary forces maintaining this polymorphism are
debated; persistent-virus infection is one of the strongest.

**Class I (HLA-A, B, C):**

- Presents intracellular peptides to CD8+ T cells
- Extremely polymorphic (>20,000 alleles at HLA-B)
- Rare-allele advantage: carriers of rare HLA alleles present
  peptides that common viral strains can't easily escape → higher
  fitness in virus-exposed populations

**Examples of HLA class I signatures per organism on the list:**

| Organism | HLA class I signal |
|----------|--------------------|
| HIV | HLA-B*57, B*27 (protective against progression); HLA-B*35 (faster progression) |
| HCMV | HLA-A*02 associated with CMV-specific CTL control; UL40-HLA-E recognition shapes NK response |
| EBV | HLA-A*02 associated with CTL control; HLA class I presentation of EBNA-1 affects latency dynamics |
| HPV | HLA class I impacts clearance vs progression to cancer |

**Class II (HLA-DR, DQ, DP):**

- Presents extracellular / vesicular peptides to CD4+ T cells
- Also very polymorphic
- Often autoimmune-disease-associated

**Examples per organism:**

| Organism | HLA class II signal |
|----------|---------------------|
| EBV | **HLA-DR15 (DRB1*15:01)** is the primary MS susceptibility allele; synergizes with EBV infection (Bjornevik 2022 causal + HLA-DR15 as risk modulator) |
| P. gingivalis | **HLA-DRB1 "shared epitope"** is the primary RA susceptibility; PPAD citrullination → anti-CCP → RA requires shared-epitope HLA |
| HPV | HLA-DR / DQ variants influence persistence vs clearance |
| HCMV | HLA class II presentation affects viral control |
| H. pylori | HLA-DQ variants modulate gastric cancer risk given infection |
| T1DM (via CVB) | HLA-DR3 + HLA-DR4 are the primary T1DM susceptibility alleles; interact with CVB infection per the DiViD framework |

**The persistent-organism list collectively drives a meaningful
fraction of HLA polymorphism** via chronic antigen exposure + rare-
allele advantage + specific organism-HLA coevolution. This is more
than acute infections produce because acute infections clear before
HLA variants matter much for outcomes; chronic infections allow
decades for HLA-specific selection to act.

---

## KIR / NK-cell receptor diversity — HCMV driver

From attempt_005 (HCMV): **HCMV is the strongest single driver of
NK-cell receptor evolution in humans.**

**KIR (killer immunoglobulin-like receptor) family:**
- Gene family on chromosome 19q13.4
- Encodes activating and inhibitory NK receptors that bind HLA
  class I ligands
- Extreme haplotype diversity (haplotype A vs B; specific KIR
  gene content varies across individuals)
- Specific KIRs recognize HCMV-modified HLA patterns
- Certain KIR/HLA combinations correlate with HCMV control vs poor
  control

**"Memory-like" NK cells** — a concept largely discovered through
HCMV studies — show that NK cells retain memory of HCMV exposure,
an observation that overturns the old dogma that only T/B cells
have immunological memory. This is a strong coevolutionary
signature that HCMV has been shaping NK biology for long enough to
produce novel immunological mechanisms.

Without HCMV, human KIR diversity would likely be substantially
lower.

---

## Intrinsic antiviral restriction factors

A category of cellular proteins that directly restrict viral
replication. Several show positive-selection signatures consistent
with millions of years of retroviral + persistent-viral exposure:

| Factor | Target | Evidence of positive selection |
|--------|--------|---------------------------------|
| **TRIM5α** | Retroviral capsid | Strong primate-specific positive selection; human TRIM5α distinct from chimp/gorilla |
| **APOBEC3G** | Retroviral reverse transcription | Strong positive selection in primates |
| **BST-2 / tetherin** | Retroviral budding | Positive selection; HIV Vpu antagonizes it |
| **SAMHD1** | dNTP hydrolysis (blocks reverse transcription) | Positive selection; HIV Vpx antagonizes it |
| **MX1 (MxA)** | Influenza, VSV | Interferon-induced; evolves under pressure |
| **SERINC5** | HIV infectivity (by Nef-dependent mechanism) | Positive selection |
| **GBP proteins** | Intracellular pathogens | Positive selection |

**These genes are the "molecular trench warfare" of long-term
human-virus interaction.** Their positive-selection signatures are
among the strongest in the human genome — comparable to selection
on immune-system receptors. The persistent viruses on the framework
list (HCMV, EBV, HPV) don't directly select these factors at the
same intensity as retroviruses did, but they contribute to the
chronic intracellular-pathogen pressure that keeps these restriction
factors under positive selection.

---

## HERVs — the terminal state of class-5 persistence

**Human endogenous retroviruses (HERVs) compose ~8% of the human
genome.** They are the ultimate signature of virus-host coevolution:
former exogenous retroviruses that integrated germline, lost
replication competence, and now persist as host genome content.

**HERVs relate to the persistent-organism framework in two ways:**

1. **HERVs are the end-state trajectory of class 5 (integration
   with germline transmission).** ciHHV-6 (attempt_006) is currently
   at the mid-state of this trajectory. Given enough evolutionary
   time, could ciHHV-6 become a HERV-like endogenous herpes virus?
   Theoretically possible but currently hypothetical.

2. **Some HERVs remain partially expressible and have been
   co-opted for host functions.** Syncytin-1 (from HERV-W) is
   required for placental syncytiotrophoblast formation.
   HERV-W envelope and HERV-K proteins have been implicated in
   autoimmune diseases — MS in particular (HERV-W-Env as a
   potential player; temelimab / GNbAC1 trialed against HERV-W-Env
   in MS patients).

HERVs are thus both:
- Residue of ancient persistent-organism battles (their origin)
- Active players in current biology (their co-opted functions +
  possible disease contributions)

---

## Cytokine pathway polymorphisms

Specific cytokine gene variants affect persistent-organism disease
outcomes:

| Polymorphism | Persistent-organism context |
|--------------|------------------------------|
| **IL-1B -31T/C, -511C/T** | El-Omar 2000 Nature PMID 10746728 — IL-1β polymorphisms + H. pylori → increased gastric cancer risk (verified in audit) |
| **IL-1RN (IL-1 receptor antagonist)** | Same H. pylori axis |
| **IL-6 -174G/C** | Chronic inflammation modulator; affects several persistent-organism disease outcomes |
| **TNF -308A/G** | Sepsis + chronic inflammation; H. pylori cancer risk |
| **TLR2 variants** | Modulate Demodex/B. oleronius response; rosacea severity |
| **TLR4 Asp299Gly** | Modulate LPS response; various infections |
| **NOD2 variants** | Crohn's disease (linked to gut microbiome); P. gingivalis recognition |
| **IL-23R, IL-17** | Chronic inflammation axis; rosacea + periodontal + IBD links |
| **NLRP3 variants** | Autoinflammatory syndromes; Demodex/CVB rosacea connections |

These polymorphisms exist at meaningful frequencies, consistent
with balancing selection — common variants have disease tradeoffs
(lower response = less immunopathology but worse clearance; higher
response = better clearance but more autoimmune risk).

---

## Innate-immunity receptor polymorphisms

**TLR2 / TLR4 — Gram-pos / Gram-neg recognition:**
- TLR2 variants affect Demodex/B. oleronius/Malassezia responses
- TLR4 variants (Asp299Gly) affect LPS response to H. pylori,
  P. gingivalis
- Distribution of TLR variants across populations correlates with
  regional bacterial burden

**CLEC7A (Dectin-1) — fungal beta-glucan recognition:**
- Recognizes Candida, Malassezia
- Deficiency causes mucocutaneous candidiasis
- Variants affect Malassezia-associated disease severity

**NOD1/NOD2 — peptidoglycan recognition:**
- Intracellular sensors
- NOD2 variants linked to Crohn's disease via altered gut microbiome
  interactions
- Response to P. gingivalis and H. pylori

**NLRP3 — inflammasome sensor:**
- Activated by diverse stimuli including bacterial products and
  host DAMPs
- Variants cause autoinflammatory syndromes (CAPS)
- Central to Demodex/B. oleronius rosacea mechanism (attempt_009
  cross-link to dysbiosis run_046)

---

## Blood group antigens as bacterial-adhesion modulators

ABO and Lewis blood group antigens are expressed on mucus-layer
surfaces and serve as **adhesion ligands for persistent bacteria**:

- **H. pylori BabA** adhesin binds Lewis-b antigen; different
  strains have different Lewis-binding specificities
- **Norovirus** also uses secretor/Lewis antigens for host-cell
  binding (relevant to acute infections)
- **ABO frequency distribution across populations** correlates
  with regional bacterial pathogen pressure — argued as partial
  explanation for ABO polymorphism maintenance

The ABO / Lewis system is thus partly shaped by persistent
bacterial pathogens.

---

## The composite picture

Pulling it together:

**Each of the 10 organisms on the persistent-organism list has
contributed to human immune gene diversity**, via different
mechanisms:

| Organism | Primary host-gene coevolution signal |
|----------|---------------------------------------|
| CVB | HLA-DR3/DR4 (T1DM susceptibility); IFIH1 (MDA5) variants |
| EBV | HLA-DR15 (MS); HLA-A/B CTL; B-cell biology |
| HPV | HLA class I + II clearance variants |
| HCMV | KIR haplotype diversity; HLA-E/UL40 axis; TRIM coevolution |
| HHV-6 | Partial; ciHHV-6 as inherited locus |
| H. pylori | HLA-DQ + IL-1B + Lewis antigens |
| P. gingivalis | HLA-DRB1 shared epitope; IL-1β; PADI4 |
| Demodex | TLR2 + cathelicidin (KLK5/LL-37) system |
| Malassezia | Dectin-1 (CLEC7A); TLR2; keratinocyte biology |
| C. acnes | TLR2; IL-8 pathway; strain-specific |

**The overlap is striking** — HLA-DRB1, TLR2, IL-1β, NLRP3 are
repeatedly named across organisms. The persistent-organism set has
not produced 10 independent signatures; it has **jointly shaped a
shared immunogenetic substrate** with common hubs.

This is the structural reason why autoimmune diseases often
cluster together in individuals and families: the same HLA and
cytokine variants mediate risk for multiple persistent-organism-
driven chronic diseases simultaneously.

---

## Predictions from the host-side analysis

1. **Individuals with HLA / TLR / NLRP3 variants that increase
   response to persistent organisms should have higher rates of
   multiple chronic diseases.** This matches epidemiology —
   autoimmune / inflammatory disease comorbidity is strongly
   clustered.
2. **Populations with high chronic-pathogen burden should show
   maintained immunogenetic diversity** at the expense of
   autoimmune susceptibility. Fits observed population genetics.
3. **Drugs targeting shared immunogenetic hubs should have
   cross-disease efficacy.** The doxycycline 40 mg MMP-9 mechanism
   (cross-class in the therapeutic-convergence sense) is one
   instance; monoclonals against IL-6, TNF, IL-17, IL-23 are
   another — used across rheumatology, dermatology, gastroenterology
   for what are really parallel expressions of persistent-organism-
   driven inflammation.
4. **As the persistent-organism composition shifts under modern
   conditions** (H. pylori declining, P. gingivalis rising), the
   relevant HLA/immune variants under selection should shift too.
   This is a prediction on decades-to-centuries timescales.

---

## Open questions

1. **What is the total fraction of human immune gene diversity
   attributable to the persistent-organism set vs other forces?**
   Quantitative partitioning is hard; estimates range from 20% to
   >60% for different gene categories.
2. **Do the 7 persistence-mechanism classes produce different
   host-gene signatures?** Hypothesis: class 1 (encoded latency)
   drives HLA class I + CTL diversity most; class 6 (chronic
   colonization) drives cytokine + TLR variants most; class 7
   (ectoparasite) drives skin-specific + TLR2/inflammasome most.
   Partially supported by the table above.
3. **Are HERVs still being generated?** The HERV-K family includes
   recent integrations, potentially within hominin evolution. ciHHV-6
   might be an early-stage HERV-like in progress.
4. **Can we predict which persistent organisms drove which host
   gene variants using phylogenetic signal?** Comparative primate
   genomics is the tool; specific organism-gene linkages are
   being identified.
5. **Do host immune gene variants feedback-modulate persistent-
   organism evolution?** Host HLA escape selection on viral
   epitopes is well-documented for HIV; likely operates for other
   persistent viruses on slower timescales.

---

## Cross-links and companion work

- `attempts/001_persistence_as_strategy.md` — framework foundation
- Per-organism attempts 002–010 — specific organism-gene pairings
- `results/persistence_mechanisms_taxonomy.md` — the 7-class
  taxonomy this note complements
- `medical/persistent_organisms/PROBLEM.md` — clinical-side
  framework
- **Cross-repo link**: the HLA polymorphism discussion intersects
  strongly with `medical/t1dm/`, `medical/dysbiosis/`,
  `medical/blepharitis/` — HLA is a common node across many
  per-disease directories

---

## What's still needed in biology/evolution/

From the closeout of attempt_010 + the taxonomy synthesis, the
outstanding synthesis items are:

1. ✅ 7-class taxonomy (done — `results/persistence_mechanisms_taxonomy.md`)
2. **Host-side coevolution (this note — done)**
3. Therapeutic convergence synthesis — doxycycline 40 mg
   cross-class + other patterns
4. Modernity trajectory analysis — which organisms rising vs
   declining under current conditions
5. Class-boundary cases — M. tuberculosis, Toxoplasma, Trypanosoma
   as framework extensions
6. Attempt_001 update to reference the 7-class taxonomy

Items 3–6 remain; item 2 is now complete with this synthesis.

---

*Filed: 2026-04-15 | biology/evolution/results/host_coevolution.md*
*Companion: persistence_mechanisms_taxonomy.md; attempts 001–010*
*Depends on specific HLA / TLR / KIR / TRIM-family claims; needs audit*
