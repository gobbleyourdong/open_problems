# attempt_008 — Porphyromonas gingivalis: The Keystone Pathogen and the Most Diverse Remote-Disease Portfolio

> Second non-viral entry in the persistent-organism evolution series.
> *P. gingivalis* is an anaerobic Gram-negative bacterium colonizing
> the subgingival periodontal pocket. Its disease portfolio extends
> far beyond the oral cavity: it has the broadest set of documented
> remote-disease associations of any persistent organism on the list
> (periodontitis → rheumatoid arthritis → Alzheimer's association →
> atherosclerosis → adverse pregnancy outcomes → pancreatic cancer
> association).
>
> **VERIFICATION STATUS:** generated from trained priors; structural
> claims high-confidence; specific numeric figures (prevalence,
> Alzheimer's association strength from Dominy 2019 verified in
> batch 2 audit, strain diversity details) flagged for further
> audit.
>
> Cross-cutting: attempt_001. Previous: attempts 002–006 (viral),
> attempt_007 (H. pylori first bacterial).

---

## Phylogenetic placement

**Domain:** Bacteria
**Phylum:** Bacteroidota (formerly Bacteroidetes)
**Class:** Bacteroidia
**Order:** Bacteroidales
**Family:** Porphyromonadaceae
**Genus:** *Porphyromonas*
**Species:** *Porphyromonas gingivalis*

The genus *Porphyromonas* was reclassified from *Bacteroides* in 1988
based on phylogenetic divergence. Other *Porphyromonas* species
infect non-human animals (dogs, cats, rodents) — species-boundaries
within the genus are less strict than in *Helicobacter*, but
*P. gingivalis* has a dominant human-oral ecological niche.

**Sister species of clinical relevance:**
- *P. asaccharolytica* — human oral commensal; occasional pathogen
- *P. endodontalis* — root canal infections
- *P. gulae* — canine oral; closely related, some cross-species
  reports

**Coevolution:** less well-characterized than H. pylori's phylo-
geography, but P. gingivalis is clearly a long-term human commensal.
Ancient DNA recovery from dental calculus in archaeological specimens
has identified P. gingivalis sequences in skeletal remains from
multiple time periods and populations.

## The ecological niche — the subgingival pocket

**P. gingivalis requires:**
1. **Anaerobic environment** — strict obligate anaerobe; oxygen is
   toxic
2. **Protein-rich substrate** — grows on amino acids; no
   carbohydrate utilization
3. **Neutral to slightly alkaline pH** — unlike gastric-adapted H.
   pylori
4. **Host heme source** — requires iron/heme; gets it from
   gingival crevicular fluid

The **subgingival periodontal pocket** meets all four: oxygen is
excluded by the biofilm overlying the tooth root; gingival exudate
provides protein and heme; pH is near-neutral. A healthy gingival
crevice (< 3 mm pocket depth) has limited P. gingivalis; a diseased
pocket (>4 mm) creates a large anaerobic niche where it thrives.

**This is a depth-dependent niche** — P. gingivalis abundance
increases as pocket depth increases, creating a positive feedback
loop: pocket deepening supports P. gingivalis, which drives
inflammation, which deepens the pocket further.

## The keystone pathogen hypothesis

**Hajishengallis G, Darveau RP, Curtis MA. "The keystone-pathogen
hypothesis." Nat Rev Microbiol 2012 Oct;10(10):717–725. PMID 22941505.**
[Journal correction per 2026-04-15 audit: earlier write-up cited Nat
Rev Immunology, which is wrong — the paper is in Nat Rev Microbiology.]

This paper framed P. gingivalis as a **keystone pathogen** — an organism that, at low abundance,
disproportionately restructures the oral microbiome toward
dysbiosis. The model:

```
Healthy subgingival microbiome (low P. gingivalis + balanced flora)
    ↓
Small rise in P. gingivalis abundance
    ↓
P. gingivalis manipulates complement (via gingipain cleavage of C5)
    ↓
Disrupted innate immune response — reduced killing of other
    subgingival bacteria
    ↓
Dysbiosis: overgrowth of other periodontal pathogens (red complex:
    Treponema denticola, Tannerella forsythia; orange complex members)
    ↓
Inflammation, tissue destruction, pocket deepening
    ↓
Further P. gingivalis expansion + additional dysbiosis
```

Critically: **P. gingivalis in monoculture causes little disease in
animal models**. The pathogenesis requires the community context.
This makes it distinct from classical "one pathogen, one disease"
frameworks.

## Gingipains — the core virulence arsenal

*P. gingivalis* encodes three cysteine proteases called **gingipains**:

- **RgpA** and **RgpB** — arginine-specific gingipains (Arg-gingipain)
- **Kgp** — lysine-specific gingipain (Lys-gingipain)

Gingipains do many things, including:
- Cleave host complement components (C3, C5) — immune evasion
- Degrade cytokines and cytokine receptors — immune modulation
- Degrade collagen, fibronectin, laminin — tissue destruction
- Process bacterial surface proteins — biogenesis
- Degrade host signaling proteins
- Activate the kallikrein-kinin system — pain, inflammation
- Process bacterial adhesins — attachment

**Gingipains are the primary target of anti-P. gingivalis
therapeutics.** Cortexyme's COR388 (atuzaginstat, a Kgp inhibitor)
entered phase 2/3 trials for Alzheimer's (see below) on the
hypothesis that gingipain activity in the brain drives
neurodegeneration. Trials have had mixed results (discussed below).

## Disease portfolio

### Primary: Periodontitis

- Chronic inflammatory destruction of periodontium (gingiva,
  periodontal ligament, alveolar bone)
- Adult prevalence: mild-to-moderate in ~40–50% of adults globally;
  severe in ~10%
- Leads to tooth loss if untreated
- Standard management: scaling and root planing, antiseptic rinses,
  in severe cases systemic antibiotics + periodontal surgery

### Secondary remote-disease associations

1. **Rheumatoid arthritis (RA)** — strongest non-oral association.
   Mechanism: P. gingivalis uniquely among bacteria expresses
   **peptidylarginine deiminase (PPAD)**, which citrullinates
   proteins. Citrullinated proteins are the target of
   anti-citrullinated protein antibodies (ACPAs / anti-CCP) — the
   hallmark autoantibody of RA. **P. gingivalis citrullination may
   be a breaking point for tolerance to self-citrullinated proteins,
   triggering RA in susceptible individuals (HLA-DRB1 shared
   epitope carriers).** Mediator: Wegner 2010 *Arthritis Rheum* on
   PPAD; subsequent epidemiology shows association but causation
   remains debated.

2. **Alzheimer's disease (AD)** — Dominy 2019 *Science Advances*
   (PMID 30746447, verified in batch 2 audit) detected P. gingivalis
   DNA and gingipain activity in postmortem AD brains. Animal models
   showed oral P. gingivalis infection → brain invasion → cognitive
   impairment. **COR388/atuzaginstat** (a Kgp inhibitor) was advanced
   to phase 2/3.
   
   **UPDATED status (2026-04-15 audit):** The GAIN trial
   (NCT03823404, n=643, mild-to-moderate AD) **missed co-primary
   endpoints** (ADAS-Cog11, ADCS-ADL) in the overall cohort. A
   pre-specified P. gingivalis-saliva-positive subgroup (n=242)
   showed 57% slowing of cognitive decline at 80 mg BID (p=0.02).
   **FDA placed a full clinical hold on COR388 in 2021.** Cortexyme
   pivoted to successor COR588, and was subsequently rebranded as
   Quince Therapeutics. The clean P. gingivalis → AD clinical win
   did not materialize as hoped, but the subgroup signal keeps the
   mechanism hypothesis alive.
   
   The AD mechanism is debated but biologically plausible — gingipains
   cleave tau and amyloid precursor proteins.

3. **Atherosclerosis and cardiovascular disease** — P. gingivalis
   DNA detected in coronary/carotid atherosclerotic plaques.
   Association studies show modestly elevated CVD risk in periodontal
   patients. Mechanism: chronic systemic inflammation + possible
   direct vascular invasion.

4. **Adverse pregnancy outcomes** — preterm birth, low birth weight
   associated with maternal periodontitis. Mechanism: systemic
   inflammation + possible placental invasion.

5. **Pancreatic cancer** — some association; bacterial signatures
   in pancreatic tumors; causal evidence weak.

6. **Diabetes** — bidirectional relationship: diabetes exacerbates
   periodontitis; periodontitis worsens glycemic control.
   Mechanism: inflammation, AGE pathways.

7. **Non-alcoholic fatty liver disease (NAFLD)** — emerging
   association; mechanism via gut-liver axis and systemic
   inflammation.

**This portfolio of ~7 remote diseases is the broadest of any
organism on the persistent-organism list.** It reflects P.
gingivalis's ability to reach distant tissues via bacteremia and
its ability to persistently modulate host inflammation.

## Persistence mechanism — class 6 (as H. pylori)

Like H. pylori, P. gingivalis uses **chronic active colonization of
an immune-privileged niche with host-tolerance induction**:

- Not latent — actively replicates in the periodontal pocket
- Not integrated — no host-genome interaction
- Niche physically protected — biofilm + anaerobic sub-gingival
  position
- **Actively induces host tolerance** via:
  - Gingipain cleavage of complement components (reduces classical-
    pathway killing)
  - Modulation of TLR signaling
  - Reduced inflammasome response
  - Hijacking of host immune signals

Class 6 now has two organism instances (H. pylori, P. gingivalis).
The commonality: **Gram-negative anaerobe or microaerophile, niche
in a mucus-protected body cavity, active host-immunity
manipulation + chronic colonization without clearance.**

This strengthens the claim that class 6 is a robust category, not a
one-organism fit.

## Evolutionary trajectory — industrialization and oral disease

Unlike the viral members of the persistent-organism list, P.
gingivalis shows a **dramatically accelerating disease burden** in
the industrial period:

- Skeletal remains from pre-agricultural hunter-gatherers show low
  rates of periodontitis
- Rates rose with the agricultural transition (~10,000 years ago) as
  diet shifted toward grain and higher-carbohydrate loads
- Industrial-era diets (refined sugars, carbohydrate density, low
  fiber) have driven another increase
- **Modern P. gingivalis prevalence and periodontitis burden are at
  historically unprecedented levels**

Why? Diet changes oral pH, plaque composition, and mucus-layer
biology, all of which support P. gingivalis colonization. Tobacco
use further accelerates risk. **The "Western diet" hypothesis of
gut dysbiosis has a parallel in oral dysbiosis**.

This is a case where the persistent-organism framework intersects
with **environmental change as a driver of persistence-disease
outcomes**. H. pylori is declining with sanitation; P. gingivalis is
rising with dietary change. The net trajectory depends on which
force dominates.

## Host genetic modifiers

- **HLA-DRB1 shared epitope** — RA susceptibility allele; required
  for the P. gingivalis citrullination → ACPA → RA pathway in most
  cases
- **PADI4 polymorphism** — modulates host citrullination baseline
- **IL-1β, IL-6 polymorphisms** — inflammatory response genetics
- **ApoE ε4** — Alzheimer's risk; intersects with P. gingivalis
  hypothesis

## Current selection pressures

1. **Dental hygiene (brushing, flossing, dental cleaning)** —
   mechanical removal of biofilm reduces P. gingivalis. Deployed
   at scale in developed countries; prevalence differential between
   high-hygiene and low-hygiene populations is substantial.
2. **Periodontal antibiotics (metronidazole + amoxicillin; local
   minocycline)** — used in severe periodontitis. Resistance rising
   but less problematic than for H. pylori.
3. **Anti-gingipain therapeutics** — COR388/atuzaginstat and
   successors; if clinically successful, would be the first
   targeted P. gingivalis therapy with systemic (AD-level) effects.
4. **Dietary evolution** — ongoing Western-diet penetration is the
   dominant pressure; tobacco decline partially offsets.

## Therapeutic architecture (link to medical/persistent_organisms/)

Two-phase pattern for P. gingivalis:

**Phase 1 (clearance):**
- Professional scaling and root planing (mechanical biofilm
  disruption)
- Local antimicrobials (chlorhexidine rinse, local minocycline)
- Systemic antibiotics (metronidazole + amoxicillin) in severe
  disease
- Future: anti-gingipain therapeutics

**Phase 2 (adjunct anti-inflammatory):**
- Doxycycline sub-antimicrobial dose (20–40 mg) — **same Oracea
  principle that works for rosacea; MMP-9 inhibition protects
  periodontal tissue**
- Periodontal maintenance (3–4 month cleanings)
- Dietary intervention (reduce carbohydrate load, improve vitamin D,
  omega-3)
- Systemic anti-inflammatory for RA / AD / CVD complications per
  specialty management

The blepharitis/rosacea-side doxycycline 40 mg rediscovery and the
periodontal-side doxycycline sub-antimicrobial use are the **same
agent with the same MMP-9 mechanism, applied at two different
sites**. This is a concrete case of cross-organism therapeutic
unification from the persistent-organism framework.

## Predictions from attempt_001 framework

1. **Transmission-mode clustering:** oral-oral, vertical (parent-
   child), horizontal family transmission. ✓
2. **Host-adaptation encoded in genome:** P. gingivalis has
   ~2.3 Mb genome with extensive virulence gene content (gingipains,
   fimbriae, capsular polysaccharide, heme acquisition). ✓
3. **Species-specific:** strong (human-dominant, some close
   relatives in primates); not as absolute as H. pylori but close. ✓
4. **Low mutation rate during persistence:** biofilm-resident
   bacteria have lower effective mutation rates than planktonic
   populations. ✓ in net
5. **Ancient DNA recovery:** yes — P. gingivalis sequences
   recovered from archaeological dental calculus. ✓
6. **No licensed vaccine, no vaccine trials in progress:** vaccine
   development has been attempted but has not reached clinical
   deployment. Pending.

Framework fits. P. gingivalis is a cleaner bacterial instance than
H. pylori on some axes (simpler ecological niche; cleaner
keystone-pathogen biology) and on others parallels H. pylori
closely (host-tolerance induction, ancient coevolution).

## Open questions specific to P. gingivalis

1. **Is the Alzheimer's hypothesis causal or associative?** Dominy
   2019 Sci Adv provided compelling mechanism + detection evidence.
   COR388 trial results have been mixed. A definitive answer needs
   either a clearly positive phase-3 trial or a strong negative
   trial with mechanism-level disconfirmation.
2. **Can targeted gingipain inhibition treat periodontitis + RA +
   AD + atherosclerosis simultaneously?** The multi-disease
   portfolio of P. gingivalis argues yes — and this would be the
   most elegant persistent-organism-framework test case if achieved.
3. **Why does modern diet drive P. gingivalis specifically vs other
   oral pathogens?** Simple fermentable-carbohydrate enhancement?
   pH shift? Biofilm complexity change?
4. **What fraction of RA is P. gingivalis–initiated?** The
   citrullination mechanism is mechanistically clean but
   population-level contribution is debated.
5. **How does oral-gut axis modulate P. gingivalis and its
   remote-disease effects?** Recent research suggests swallowed
   P. gingivalis can colonize gut and affect systemic inflammation
   via different mechanism than oral-cavity-local effects.

## Cross-links to existing repo work

- `medical/persistent_organisms/PROBLEM.md` — P. gingivalis row
  (organism #3)
- `medical/dysbiosis/results/protocol_integration.md` — M7 oral arm
  covers P. gingivalis with existing protocol content
- `medical/dysbiosis/numerics/run_046_demodex_rosacea_nlrp3.md`
  shares the doxycycline / MMP-9 / NF-κB mechanism with the
  periodontal and ocular rosacea sides

The doxycycline 40 mg connection is the single clearest cross-
organism therapeutic overlap in the repo so far.

---

## Structural comparison after 7 attempts

| Organism | Persistence class | Genome | Host | Remote diseases | Unique |
|----------|-------------------|--------|------|-----------------|--------|
| CVB | Mutation (5'-UTR) | 7.4 kb | Humans + pigs | T1DM, DCM, ME/CFS | RNA virus persistent form |
| EBV | Encoded latency | 172 kb | Strict human | MS, lymphomas | Clean MS causation |
| HPV | Lifecycle coupling | 8 kb | Strict human | Cervical/oral cancer | Only vaccine-era test |
| HCMV | Latency + immunology | 235 kb | Strict human | CMV disease, congenital | Biggest genome; NK driver |
| HHV-6 | Integration (germline) | 160 kb | Strict human | MS, DRESS | Only germline-transmitting |
| H. pylori | Chronic + tolerance | 1.7 Mb | Strict human | Ulcer, cancer + protective GERD | Ancient-DNA migration signal |
| **P. gingivalis** | **Chronic + tolerance** | **~2.3 Mb** | **Strict human** | **Periodontitis + RA + AD + CVD + preterm + pancreatic + diabetes** | **Broadest remote-disease portfolio; keystone pathogen** |

---

*Filed: 2026-04-15 | biology/evolution/attempts/attempt_008*
*Companions: attempts 001–007; needs audit pass*
*Next: Demodex (attempt_009) — first arthropod coevolution entry; Malassezia + C. acnes (attempt_010) for fungal + skin-bacterial coverage*
