# Evolutionary Characteristics of Persistent Human Organisms

**Scope expanded 2026-04-15** after operator guidance ("organisms"
broader than the original viral-only framing). Directory now covers
persistent bacteria, fungi, arthropods, and boundary-case protozoa
+ intracellular bacteria in addition to the original viral quintet.

## Scope

This directory studies the **evolutionary biology** of organisms
that establish long-term persistence in humans and drive chronic
disease as a downstream consequence. It is the evolution-side
complement to `medical/persistent_organisms/` (clinical-side),
which catalogues disease associations and therapeutic architecture.

**Primary per-organism attempts (10 organisms, 4 kingdoms):**

Viruses (5):
- **Coxsackievirus B (CVB, 6 serotypes)** — picornavirus, ssRNA(+)
- **Epstein-Barr virus (EBV, HHV-4)** — herpesvirus, dsDNA, B-cell latency
- **Human papillomavirus (HPV, >200 types)** — papillomavirus, dsDNA, epithelium
- **Cytomegalovirus (HCMV, HHV-5)** — β-herpesvirus, dsDNA, myeloid latency
- **Human herpesvirus 6A/6B** — β-herpesvirus, dsDNA, chromosomal integration

Bacteria (2):
- ***Helicobacter pylori*** — Gram-negative gastric microaerophile
- ***Porphyromonas gingivalis*** — Gram-negative anaerobic periodontal keystone

Eukaryotes (3):
- ***Demodex folliculorum* + *D. brevis*** — arthropod skin ectoparasites
- ***Malassezia spp.*** — basidiomycete yeast, lipid-dependent
- ***Cutibacterium acnes*** — Gram-positive pilosebaceous, strain-stratified disease
  (bacterial but grouped ecologically with Demodex + Malassezia in sebaceous ecosystem)

**Class-boundary extensions (6 additional organisms, `results/class_boundary_cases.md`):**
- *Mycobacterium tuberculosis* (class 6b intracellular)
- *Mycobacterium leprae* (class 6b + class-7-like bacterial reductive genome)
- *Treponema pallidum* (class 6 + phased quiescence)
- *Toxoplasma gondii* (class 7 eukaryotic + encoded tissue-cyst dormancy)
- *Trypanosoma cruzi* (class 4 + class 7 hybrid)
- *Plasmodium vivax* (class 4 + class-1-like hypnozoite dormancy)

**Secondary future candidates (not yet attempted):**
HSV-1/2, VZV, HBV, HCV, HIV, JCV, Merkel-cell polyomavirus,
*Candida*, *Aspergillus*, additional helminths, Rickettsia,
Chlamydia, Borrelia.

## The central question

**Why did these viruses evolve to persist in human hosts, and what does
persistence mean as an evolutionary strategy?**

This decomposes into sub-questions:

1. **Persistence vs clearance.** Most human viral infections (flu,
   common cold, norovirus) are cleared within days-to-weeks. These are
   the exceptions. What evolutionary pathway produced persistence, and
   why is it stable?
2. **Latency mechanisms as adaptations.** EBV hides in resting B cells.
   HPV parks in the basal epithelium. CVB makes 5'-UTR-deleted replication-
   defective variants. HCMV hides in monocytes. These are distinct
   molecular solutions to the same problem (immune evasion over
   decades). Are they convergent or independently evolved?
3. **Disease as side-effect.** From the virus's perspective, chronic
   disease (T1DM, MS, cervical cancer, Alzheimer's association) is
   mostly irrelevant — the virus has usually already transmitted before
   disease manifests. Disease is a host-side accident of persistence,
   not a fitness-relevant outcome for the virus. What does this tell
   us about virulence evolution?
4. **Co-evolution with the immune system.** These viruses have been
   with hominins for tens of thousands to millions of years
   (HCMV-primate divergence ~90 Ma; HPV-mammal coevolution ~100+ Ma;
   CVB-enterovirus lineage more recent). What co-evolutionary signatures
   do we see in human genes vs virus genes?
5. **Horizontal vs vertical transmission.** EBV is horizontal
   (salivary); HPV is horizontal (sexual, skin); CVB is horizontal
   (fecal-oral); HCMV is both (placental + salivary + sexual); HHV-6
   is salivary + chromosomal integration can transmit vertically.
   What does transmission mode predict about evolutionary strategy?
6. **Bottlenecks and population diversity.** Modern sequencing reveals
   intra-host viral populations — quasispecies for RNA viruses, clonal
   + mutant for DNA. How does this intra-host diversity relate to
   persistence?
7. **Reservoir species.** Enteroviruses have many animal hosts;
   herpesviruses are largely species-specific; HPVs are strictly
   species-specific. Why the difference?
8. **Selection pressures now.** Vaccination (HPV, increasingly CMV/EBV
   candidates), antivirals (HSV, HCV — cleared; others — partial),
   and changing human behavior (hygiene, sexual practice, population
   density) are applying novel selection. What do we expect over
   decades to centuries?

## Why this lives in `biology/` not `medical/`

The question "why does EBV persist" is biology. The question "what do
we do about EBV-driven MS" is medicine. Both are important; they
inform each other; they are not the same project.

The medical-side framework (consequences, protocols, treatment) lives
in `medical/` across specific-disease directories. The biology-side
framework (origins, mechanisms, co-evolution) lives here. Each side
should cite the other without collapsing categories.

## Phase 0 shape-check

1. **Is there a known mechanism?**
   - Partially. Latency mechanisms are well-characterized for EBV
     (LMP1/EBNA-1, episomal maintenance) and HPV (E6/E7). HCMV latency
     is partly known. CVB persistence (5'-UTR-deleted, truncated
     replicon) is described in cell culture, less in humans.
   - Evolutionary *origins* of these mechanisms are largely unknown —
     phylogeny gives us tree topology but not mechanism-emergence
     narrative.
2. **Do "effective treatments/solutions" exist?**
   - HPV is preventable by vaccine; curative treatment for established
     disease is surgical.
   - HCV is curable (direct-acting antivirals).
   - HIV is controlled but not cured.
   - EBV, HCMV, HHV-6, CVB: no eradicating therapy exists.
   - The biology-side question is about understanding, not treatment.
3. **Can the wall be crossed by new information?**
   - Yes — phylogenetic data is expanding, ancient DNA is beginning to
     recover viral sequences, molecular-clock dating is improving,
     structural biology of viral-host interactions continues.
4. **Does crossing require changes in recurring human action?**
   - No — this is scientific mechanism work, not behavioral.
5. **Who has tried to cross this wall?**
   - Substantial literature since 1960s; accelerating since
     whole-genome sequencing and ancient-DNA methods. Active field.

**Shape classification: MECHANISTIC + HISTORICAL wall.** Standard sigma
pipeline applies. The method can produce gap maps, catalog
well-established results, identify open frontier questions, and
synthesize across virus families — but cannot run wet-lab phylogeny
or ancient-DNA work itself (same caveat as dysbiosis PROBLEM.md).

## Directory structure

**As of 2026-04-15 — scaffold complete, per-organism series + 5 synthesis notes in place:**

```
biology/evolution/
├── PROBLEM.md                     ← this file (scope, updated 2026-04-15)
├── attempts/
│   ├── attempt_001_persistence_as_strategy.md    (cross-cutting framework + 2026-04-15 addendum)
│   ├── attempt_002_cvb_evolution.md
│   ├── attempt_003_ebv_evolution.md              (audit-corrected)
│   ├── attempt_004_hpv_evolution.md
│   ├── attempt_005_hcmv_evolution.md             (audit-corrected with Moderna 2025-10 failure)
│   ├── attempt_006_hhv6_evolution.md             (audit-corrected)
│   ├── attempt_007_helicobacter_pylori_evolution.md  (audit-corrected)
│   ├── attempt_008_porphyromonas_gingivalis_evolution.md  (audit-corrected with COR388 clinical hold)
│   ├── attempt_009_demodex_evolution.md          (audit-corrected Smith 2022 genome + "no anus" refutation)
│   └── attempt_010_malassezia_cutibacterium_evolution.md  (audit-corrected phylotype attribution)
├── results/
│   ├── persistence_mechanisms_taxonomy.md       ← 7-class taxonomy
│   ├── host_coevolution.md                      ← HLA, KIR, HERV, immune polymorphisms
│   ├── therapeutic_convergence.md               ← doxycycline 40mg + cross-class drug patterns
│   ├── modernity_trajectory.md                  ← rising/declining organisms under modern conditions
│   └── class_boundary_cases.md                  ← 6-organism framework extensions
├── papers/                                      ← (empty; verified citations embedded in attempts + synthesis notes per audit batches)
├── numerics/                                    ← (empty; no computational work yet)
└── certs/                                       ← (empty)
```

Audit status: 6 batches, 65 claims examined, ~52% fully verified,
~48% with material corrections. See
`medical/blepharitis/results/claim_audit_2026-04-15.md` for full log.

## Relationship to other work in the repo

- **`medical/blepharitis/results/persistent_organism_pattern.md`** —
  the medical-side synthesis naming the 8 persistent organisms + the
  two-phase treatment architecture (clearance + anti-inflammatory
  adjunct). The biology here asks: why are these 8 the ones that
  persist?
- **`medical/t1dm/`**, **`medical/myocarditis/`**, etc. — disease-specific
  instances downstream of CVB persistence. The biology here asks: why
  does CVB persist rather than clear?
- **`medical/dysbiosis/`** — organism-composite chronic-disease
  framework. Covers non-viral persistence too (Demodex, Malassezia,
  P. gingivalis, gut bacteria). This directory stays scoped to viruses
  per operator guidance.

## First-pass working hypothesis

**Persistence is a successful evolutionary strategy for viruses that
can establish a low-level equilibrium with host immunity that extends
transmission window beyond the acute phase.** The minimum requirements
appear to be:

1. A molecular mechanism for reducing antigen exposure during dormancy
   (latency via minimal gene expression, compartmentalization in
   immune-privileged cells, or antigenic variation)
2. A reactivation trigger that couples to host stressors sufficient to
   resume transmission-competent virion production
3. A host reservoir (cell type or tissue) that does not get
   constitutively cleared
4. Tolerance of long-term intra-host population diversity (quasispecies
   for RNA; episomal + recombination for DNA)

Different viruses found different solutions to the same four
requirements. The study of "how" each solved them is the core work of
this directory.

---

*Filed: 2026-04-15 | biology/evolution/PROBLEM.md | Updated 2026-04-15 (expanded scope)*
*Companion: medical/persistent_organisms/PROBLEM.md (clinical-side, created same date)*
*Scope: all persistent human organisms — viral, bacterial, eukaryotic (fungal, arthropod), + boundary-case protozoa and intracellular bacteria*
*Per-organism attempts 002–010 spanning 10 organisms + 6 boundary extensions in `results/class_boundary_cases.md`*
