# attempt_001 — Persistence as an Evolutionary Strategy

> Cross-cutting analysis before per-virus attempts. Establishes what
> "persistence" means as an evolutionary trait and what selection
> conditions produce it. Sets up the comparative framework that
> attempts 002–005 (per-virus) will populate.

---

## Two fundamentally different viral life histories

Most human viral infections are **acute-and-cleared**: rapid
replication, high peak titer, strong immune response, clearance within
days to weeks, with lifelong immune memory. Examples: influenza,
rhinovirus, norovirus, measles, rotavirus.

A minority establish **persistent infection**: continued viral presence
(replicating or latent) for months to decades, often lifelong. Examples:
EBV, HCMV, HHV-6, HSV, VZV, HBV, HCV, HIV, HPV, and the edge case of
CVB (acutely cleared in most, persistent in a subset).

These are not two points on a spectrum but two distinct evolutionary
strategies. Acute viruses maximize per-infection transmission intensity
and tolerate short infectious windows. Persistent viruses trade peak
transmission for duration, accepting lower instantaneous R0 in exchange
for decades of sporadic transmission opportunities.

The two strategies impose different constraints:

| Trait | Acute / cleared | Persistent |
|-------|-----------------|------------|
| Peak viral load | High (need fast spread before clearance) | Low to moderate (sustained over time) |
| Antigenic constancy | High (one infection, one immune response) | Often requires antigen minimization or variation |
| Host cell damage | Tolerable — host can recover or die | Must minimize — long-term relationship |
| Genome complexity | Often minimal (small RNA virus) | Often larger (encodes latency machinery) |
| Host range | Can be wide (epidemic species-jumps) | Typically narrow (species-specific adaptation) |
| Transmission mode | Often aerosol / fecal-oral (short contact) | Often bodily-fluid / mucosal / vertical (prolonged contact) |
| Evolutionary rate | High (rapid antigenic drift, e.g. flu) | Often lower (latent periods have no replication) |

## What selection conditions favor persistence

Persistence is not trivially better than clearance. A persistent virus
must solve a harder problem (immune evasion over decades) for benefits
that only pay off over long timescales. Selection favors persistence
when:

1. **Host population is small and scattered.** High R0 acute strategies
   require dense susceptible populations. In bands of 50–150 hominins
   over thousands of generations, persistence lets a virus wait for new
   susceptible hosts (infants, immigrants) rather than burn through a
   small population and go extinct locally. This is the "measles-needs-
   millions" population-threshold argument in reverse: measles-like
   strategies failed before agriculture allowed large settlements.

2. **Host lifespan is long.** A virus with a 60-year host has a long
   transmission window if it can stay in the host. A short-lived host
   (rodent, most mammals) favors acute strategies because long
   persistence yields diminishing returns per host.

3. **Transmission is low-frequency / low-intensity.** Sexual and
   salivary transmission are inherently rarer than aerosol; a virus
   depending on those routes benefits from being present for years
   rather than weeks.

4. **Immune tolerance is achievable.** Some niches (B cells for EBV,
   basal epithelium for HPV, myeloid for HCMV) are sites where the virus
   can minimize antigen exposure. Viruses without access to such niches
   cannot persist regardless of selection.

5. **Vertical transmission is possible.** A virus transmissible to
   offspring (HCMV placental, HIV perinatal, HHV-6 chromosomal
   integration) guarantees continuation even if horizontal transmission
   fails temporarily.

Hominin populations check all five conditions. This is consistent with
the observation that humans carry multiple persistent virus families;
most mammals do too, each set shaped by that species' ecology.

## The four latency / persistence mechanisms in humans

Across the persistent human viruses, four broad solutions to "stay here
without provoking clearance" have evolved:

### 1. True latency (transcriptional silencing with episomal maintenance)

The virus genome enters a quiescent state with minimal-to-zero gene
expression. Most prominent in **herpesviruses** (EBV, HCMV, HSV-1/2,
VZV, HHV-6/7, KSHV).

Key features:
- Episomal circular DNA in the host nucleus (not integrated)
- Expression of a few critical "latency genes" (EBNA-1 for EBV;
  LANA for KSHV) that maintain the episome during cell division
- Repression of lytic-cycle genes via chromatin modification
- Periodic reactivation triggered by host stress, immunosuppression,
  or cell differentiation

### 2. Chromosomal integration (covert residence)

The viral genome physically integrates into the host chromosome.

Key examples:
- **HHV-6A and HHV-6B** — chromosomally-integrated HHV-6 (ciHHV-6) is
  present in ~1% of the human population. Integrates at telomeric
  regions. Can reactivate and can be transmitted vertically via
  germline.
- **HIV** — integrates into the host genome; latent reservoir in
  resting CD4+ T cells is the barrier to cure.
- **HPV** — integrates in many cases of malignant progression (especially
  high-risk types in cervical cancer); episomal in benign/low-grade
  lesions.
- **HBV** — often integrates partial sequences even when episomal cccDNA
  also persists.

Integration is a deeper form of persistence — the virus becomes part
of the host genome, inherited by daughter cells.

### 3. Slow-replicating chronic infection (continuous low-level output)

The virus continues replicating at low levels indefinitely without a
true latent state.

Key examples:
- **HCV** — continuous hepatocyte infection until treated with
  direct-acting antivirals
- **HIV** (pre-cART) — continuous replication in CD4 T cells; latency
  is only for memory-cell reservoir
- **HBV** — mixed; cccDNA is long-lived episomal, plus low-level
  replication
- **CVB persistent** — truncated 5'-UTR-deleted variants replicate
  inefficiently but continuously in pancreas, heart (suggested; less
  established than for EBV/HPV)

### 4. Antigenic variation (hide in plain sight)

The virus continuously varies surface antigens to stay ahead of the
immune response.

Key examples:
- **HIV** — env gene hypervariability
- **HCV** — E1/E2 hypervariable regions
- Less dominant in herpesviruses, which favor strategies 1–2

These four mechanisms are not mutually exclusive. HPV uses both
episomal persistence AND integration in different disease stages.
HIV uses both chronic active replication AND latent reservoir.

## Disease as incidental to virus fitness

For acute viruses, severe disease shortens the transmission window
(dead hosts don't shed). Virulence is under stabilizing or reducing
selection once host death impairs spread.

For persistent viruses, **disease is typically decoupled from
transmission**. HPV transmits before cervical cancer. EBV transmits
during mononucleosis (often subclinical) decades before any MS
manifestation. CVB transmits fecal-orally during acute or asymptomatic
infection, often before T1DM appears. HCMV transmits vaginally /
placentally / salivarily during asymptomatic shedding.

**Consequence:** chronic diseases these viruses cause are largely
*not* under virus-side selection. The virus has already transmitted
before the disease appears; the disease doesn't affect virus fitness.
This explains why chronic disease burden persists despite long
coexistence — it is not a selection target.

This is a critical difference from acute viruses, where virulence and
transmissibility are tightly coupled. It has a clinical corollary:
reducing chronic-disease burden from persistent viruses does not
drive virus evolution toward lower virulence, because virulence is
already irrelevant to virus fitness. Vaccination against HPV-16/18
reduces disease but has not selected for less-oncogenic HPV variants
(yet — it is early in evolutionary time).

## Host-side coevolution

The other side of the relationship: human immune genes show signatures
of adaptation to persistent viruses.

- **HLA polymorphism** — the MHC class I locus is extraordinarily
  polymorphic. A major driver of this polymorphism is selection by
  persistent viruses (especially CMV, EBV, HIV). Heterozygote advantage
  at HLA is maintained by rare-allele advantage against persistent
  viral antigens.
- **KIR–HLA coevolution** — natural killer cell inhibitory receptors
  (KIRs) pair with HLA class I ligands; CMV is a major driver of KIR
  evolution.
- **TRIM5α and other restriction factors** — several primate-specific
  or rapidly-evolving antiviral genes (TRIM5α, APOBEC3G, BST-2/tetherin,
  SAMHD1, MX1) show positive-selection signatures consistent with
  millions of years of retroviral and persistent-viral exposure.
- **HERVs (human endogenous retroviruses)** — the 8%+ of the human
  genome that is retroviral in origin is the ultimate mark of
  coevolution: formerly persistent retroviruses that integrated
  germline, lost infectivity, and now persist as host genome
  components. Some HERVs remain transcribable and have been co-opted
  for host functions (syncytin-1 for placenta).

These signatures tell us that persistent viruses have been present
and actively shaping primate and human evolution for tens of millions
of years. The co-evolutionary timescale is long enough that both
sides have adapted.

## Predictions this framing makes

If persistence-as-strategy is the right frame, we should see:

1. **Persistent viruses should cluster by transmission mode and host
   niche.** Herpesviruses (salivary, sexual, vertical) + papillomaviruses
   (skin, sexual) + hepatitis viruses (blood, sexual) + retroviruses
   (blood, sexual, vertical) — all with low-intensity transmission
   and long host contact. Acute respiratory viruses (influenzas,
   coronaviruses, RSV) — high-intensity brief exposure. The divide
   is empirical.

2. **Persistent viruses should have larger genomes than acute viruses
   of the same family.** Latency machinery costs coding capacity.
   Herpesviruses (120–230 kb dsDNA) are among the largest viral
   genomes known. Compare to picornaviruses (acute clearance default,
   7.5 kb ssRNA).

3. **Persistent viruses should be more species-specific** (narrower
   host range) than acute viruses. Long coevolution tunes the
   virus–host interaction. Prediction holds strongly: human
   herpesviruses are strictly human-restricted; influenza has wide
   zoonotic range.

4. **Persistent viruses should have lower per-site mutation rates
   during latent phases** than acute viruses during replication.
   Latency is non-replicating (or minimally so); no mutation
   accumulation. Prediction holds.

5. **Ancient DNA (aDNA) should yield persistent virus sequences more
   readily than acute virus sequences**, because persistent viruses
   can be present in skeletal material decades after host death (EBV
   in teeth pulp; HHV-6 in bone). aDNA virology confirms this — EBV,
   HBV, smallpox aDNA are being recovered; influenza aDNA is much
   harder.

6. **Vaccination against persistent viruses should produce durable
   immunity** for sterilizing-immunity vaccines (HPV is the canonical
   success), but may fail to eradicate persistence once infection is
   established (EBV and HCMV vaccine efforts struggle with this).
   Prediction holds — HPV prophylactic vaccination has reduced new
   infections sharply but is not therapeutic for established disease.

## What the cross-cutting analysis sets up

Individual attempts for CVB, EBV, HPV, HCMV, HHV-6 will each ask:

- Which of the four persistence mechanisms does this virus use?
- What transmission mode, and what does it predict about the
  strategy?
- What host niche and cell type does latency occupy?
- What is the phylogenetic placement — age, divergence, primate
  coevolution?
- What chronic disease(s) does it drive, and is the disease
  virus-fitness-neutral?
- What selection pressures (vaccination, antivirals, hygiene) is
  it currently under?
- What predictions does the framework make for the next 50–500
  years of viral evolution?

The per-virus attempts will follow in subsequent iterations. This
cross-cutting analysis is the shared backbone.

---

## Gap closed / opened

**Closed (initial scope):**
- What "persistence" means as a distinct evolutionary strategy
- Four mechanism classes cataloged (latency, integration, chronic
  low-level, antigenic variation)
- Selection conditions that favor persistence
- Disease-as-incidental argument for persistent viruses
- Host-side coevolution signatures

**Opened for per-virus attempts:**
- CVB: why does it mostly clear but sometimes persist? (attempt_002)
- EBV: latency mechanism deep dive; MS causation mechanism (attempt_003)
- HPV: type diversity + integration vs episome transition (attempt_004)
- HCMV: myeloid-cell latency + KIR coevolution (attempt_005)
- HHV-6: chromosomal integration biology (attempt_006)

---

## Addendum — Framework Refinement After Per-Organism Series

> Added 2026-04-15 after completion of per-organism attempts 002–010
> and synthesis notes in `results/`. This section records the
> refinements to the initial 4-mechanism framework that emerged
> from examining 10 organisms (viruses, bacteria, arthropod, fungus)
> + 6 boundary cases (MTB, M. leprae, T. pallidum, Toxoplasma,
> T. cruzi, P. vivax).

### The framework is now 7 classes, not 4

Original formulation in this attempt named 4 mechanism classes
(latency, integration, chronic replication, antigenic variation).
The per-organism work established that **3 additional classes are
warranted**:

1. **Encoded latency with programmatic quiescence** — EBV, HCMV,
   HSV, VZV, KSHV
2. **Mutation-driven replication-defective persistent form** — CVB
3. **Lifecycle-differentiation compartmentalization** — HPV (new)
4. **Antigenic variation** — HIV, HCV, protozoa
5. **Chromosomal integration with germline transmission** —
   HHV-6, HERVs
6. **Chronic active colonization + host-tolerance induction** —
   H. pylori, P. gingivalis, C. acnes; subtypes 6a mucosal-luminal
   and 6b intracellular (MTB, M. leprae, T. pallidum)
   (new)
7. **Obligate host-dependent organism with reductive-genome
   signature** — Demodex, Malassezia, M. leprae; across kingdoms
   (new)

The full taxonomy is in `results/persistence_mechanisms_taxonomy.md`
with definitions, organism assignments, predictions, and boundary
cases.

### Revised predictions

Original attempt_001 offered 6 predictions for the viral-focused
framework. The per-organism work refined these:

1. **Transmission-mode + niche clustering predicts persistence** ✓
   Holds across all 16 organisms examined.
2. **Larger genomes for persistent viruses** — **REFORMULATED**.
   The original claim fails for HPV (8 kb) and Demodex (~51 Mb
   nuclear — reductive, not expanded). Corrected claim: **"persistent
   organisms show genome SPECIALIZATION relative to free-living
   relatives — either expansion (viral/bacterial immune-evasion
   machinery) or contraction (eukaryotic/intracellular-bacterial
   host-commitment)"**. Both are signatures of long coevolution.
3. **Species-specificity + long coevolution as prerequisites** ✓
   All 16 organisms show strict or near-strict host specificity.
4. **Low mutation rate during persistence** ✓ Holds.
5. **Ancient DNA recoverability** ✓ Holds — H. pylori is the
   strongest case (used as a human migration marker).
6. **Vaccination prevents but doesn't cure** ✓ HPV + Hepatitis B
   confirm the pattern; Moderna HCMV failure + Cortexyme COR388
   (P. gingivalis-targeted) clinical hold show vaccine/therapeutic
   development is hard.

### Additional framework principles (not in original attempt_001)

From the synthesis work, two principles emerged:

**A. Disease-as-incidental is a near-universal feature.**
For all 16 organisms examined, chronic disease appears after
transmission has already occurred, so disease is evolutionarily
invisible to organism fitness. This has a clinical corollary:
treating chronic disease does not drive rapid evolution toward
reduced virulence, because virulence is already irrelevant to
organism fitness.

**B. Host-coevolution has converged on common hubs.**
HLA-DRB1, TLR2, IL-1β, NLRP3 are repeatedly named across the
persistent-organism set. The shared immunogenetic substrate
explains why autoimmune diseases cluster in individuals + families
(same variants drive risk across multiple persistent-organism-
driven diseases) and why broad anti-inflammatory drugs
(doxycycline 40 mg, anti-TNF, anti-IL-6) work across disease
categories. See `results/host_coevolution.md`.

### Three additional synthesis claims

**C. Therapeutic convergence across classes is real and clinically
useful.** Doxycycline 40 mg MMP-9 inhibition works across classes
6 + 7 (rosacea + blepharitis + periodontitis). Colchicine + IL-1β
inhibition work across classes 1, 2, 6, 7 via NLRP3. Anti-CD20
biologics work via B-cell EBV-reservoir depletion. Cross-
specialty opportunities exist. See `results/therapeutic_convergence.md`.

**D. Modernity is shifting persistent-organism composition away
from luminal-bacterial and toward biofilm/ectoparasite/diet-
dependent.** H. pylori declines with sanitation; P. gingivalis,
Demodex, Malassezia rise with Western diet. Clinical consequence:
21st-century chronic-disease landscape looks like an inflammation
epidemic. See `results/modernity_trajectory.md`.

**E. Classes are not mutually exclusive.** Many real organisms
use 2+ mechanisms in combination (T. cruzi class 4 + class 7;
T. pallidum 6 + 4 + phased; Plasmodium 4 + class-1-like hypnozoite).
Single-class assignment is a simplification; hybrid organisms are
common. See `results/class_boundary_cases.md`.

### Structure of biology/evolution/ as of 2026-04-15

```
biology/evolution/
├── PROBLEM.md                      ← scope
├── attempts/
│   ├── attempt_001_persistence_as_strategy.md    ← this file (cross-cutting framework; now updated with addendum)
│   ├── attempt_002_cvb_evolution.md
│   ├── attempt_003_ebv_evolution.md
│   ├── attempt_004_hpv_evolution.md
│   ├── attempt_005_hcmv_evolution.md
│   ├── attempt_006_hhv6_evolution.md
│   ├── attempt_007_helicobacter_pylori_evolution.md
│   ├── attempt_008_porphyromonas_gingivalis_evolution.md
│   ├── attempt_009_demodex_evolution.md
│   └── attempt_010_malassezia_cutibacterium_evolution.md
├── results/
│   ├── persistence_mechanisms_taxonomy.md      ← 7-class taxonomy
│   ├── host_coevolution.md                     ← HLA, KIR, HERV, immune polymorphisms
│   ├── therapeutic_convergence.md              ← cross-class drug patterns
│   ├── modernity_trajectory.md                 ← rising/declining organisms under modern conditions
│   └── class_boundary_cases.md                 ← MTB, Toxo, Trypano, M. leprae, T. pallidum, P. vivax extensions
├── papers/                                     ← (empty; verified citations embedded in per-organism attempts + synthesis notes)
├── numerics/                                   ← (empty; no computational work yet)
└── certs/                                      ← (empty)
```

All 10 per-organism attempts + 5 synthesis notes form a coherent
framework. Audit passes (6 batches, 65 claims, ~52% fully verified,
~48% with corrections) have improved claim reliability across the
directory. The `medical/persistent_organisms/` directory provides
the clinical-side complement.

### What remains open

1. **Update `PROBLEM.md`** to reflect the expanded scope (original
   was viral-only; now includes bacterial, fungal, arthropod, +
   boundary-case organisms)
2. **Audit-loop continuation** — the audit loop (30m cron) should
   continue hitting remaining claims (Class boundary note has
   specific figures not yet audited)
3. **Cross-organism therapeutic trial synthesis** — would be an
   aggregate analysis of ongoing clinical trials using class-
   unifying drugs (doxycycline 40 mg, NLRP3 inhibitors, IL-6
   biologics) across persistent-organism disease indications.
   Not started.
4. **8th class consideration** — biofilm was considered and
   rejected as a mechanism subclass of class 6 rather than a new
   class. Future persistent-organism candidates may motivate
   revisiting.

---

*Addendum filed: 2026-04-15 | Framework refinements after per-organism series*
*Completes the biology/evolution/ synthesis phase initiated 2026-04-15*

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_001*
*Cross-cutting; depends on biology/evolution/PROBLEM.md*
*Companion: medical/blepharitis/results/persistent_organism_pattern.md (medical-side)*
