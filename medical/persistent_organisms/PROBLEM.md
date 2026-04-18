# Persistent Organism–Driven Chronic Disease

## Scope

This directory is the medical-side framework for the observation that
a small number of persistent organisms drive a surprising fraction of
chronic human disease. It is the clinical complement to
`biology/evolution/`, which studies the evolutionary biology of the
same organisms.

**Scope:** organism → disease pathway, treatment architecture, clinical
recognition, protocol synthesis. Does NOT cover: evolutionary origins
(biology/evolution/), or disease-specific mechanism at individual-run
level (that stays in the per-disease directories).

## The core claim

A list of ~8 persistent organisms, each capable of chronic low-level
host immune engagement, drives the majority of chronic disease whose
etiology is not purely genetic / metabolic. Each organism produces a
cluster of associated conditions; each responds to a
**two-phase therapeutic architecture**:

1. **Clearance phase**: reduce organism burden with a targeted agent
   (acaricide, antiviral, antibiotic, antifungal).
2. **Adjunct phase**: anti-inflammatory management to quench the
   self-sustaining inflammatory loop the organism initiated but which
   now runs on its own momentum.

This is the pattern observed concretely at the blepharitis lid-margin
(attempts 001–008 of `medical/blepharitis/`, notably attempt_006 on
chronic inflammation after clearance) and generalized in
`medical/blepharitis/results/persistent_organism_pattern.md`.

## The list

| # | Organism | Persistence niche | Key chronic diseases | Clearance agent(s) | Adjunct |
|---|----------|-------------------|----------------------|--------------------|---------|
| 1 | **Coxsackievirus B (CVB)** | Pancreas, heart, muscle | T1DM, myocarditis, DCM, pericarditis, pancreatitis, pleurodynia, some ME/CFS | Fluoxetine (cellular antiviral), BHB, NLRP3 suppressors | Colchicine, ivermectin (NF-κB), metabolic (keto for β-cell rest) |
| 2 | **Demodex folliculorum / brevis** | Hair follicle, meibomian gland | Rosacea, blepharitis, MGD, chalazion, POD | Tea tree oil / T4O, topical + oral ivermectin, lotilaner (ocular), permethrin, sulfur | Doxycycline 40 mg, omega-3, hypochlorous acid |
| 3 | ***Porphyromonas gingivalis*** | Periodontal pocket | Periodontitis, rheumatoid arthritis, Alzheimer's association, atherosclerosis, preterm birth | Professional periodontal therapy, anti-gingipain (COR388/atuzaginstat — GAIN Phase 2/3 **failed primary endpoint 2021**; Cortexyme → Quince pivot; no active clinical program) | Doxycycline, systemic anti-inflammatory, RA-specific DMARDs if needed |
| 4 | **Epstein-Barr virus (EBV)** | B cell latency | MS (Bjornevik 2022 causal), several lymphomas, post-viral fatigue, autoimmunity | Valacyclovir (limited in latent cycle), tenofovir alafenamide (experimental) | Vitamin D, immunomodulation per downstream syndrome |
| 5 | ***Helicobacter pylori*** | Gastric mucosa | Gastric ulcer, gastric cancer, MALT lymphoma | Triple/quadruple antibiotic therapy, bismuth regimens | PPI, mucosal healing |
| 6 | **HPV (high-risk types)** | Basal epithelium | Cervical, oropharyngeal, anal cancers | Vaccination (prophylactic), imiquimod / 5-FU / cryo for lesions | LEEP / conization; no systemic clearance for established disease |
| 7 | ***Malassezia* + *Cutibacterium acnes*** | Sebaceous sites | Seb derm, acne, dandruff, Malassezia folliculitis | Ketoconazole, selenium sulfide, benzoyl peroxide, topical retinoids | Zinc pyrithione, barrier repair |
| 8 | **Composite gut dysbiosis** | Colon, small bowel | IBD, T1DM initiation, metabolic syndrome | Targeted antibiotics (rifaximin for SIBO), FMT (C. diff), dietary pattern | Butyrate / SCFA, L-glutamine, zinc carnosine |
| (wt) | HHV-6, CMV | Lymphocytes | ME/CFS, transplant complications | Limited antiviral efficacy | Symptom-targeted |

Rows 1–8 are primary; HHV-6/CMV are weaker-evidence candidates.

## Phase 0 shape-check

1. **Mechanism known?** Yes for 1–8; organism-disease associations are
   established to varying strengths. See each organism's row for
   evidence tier.
2. **Effective treatments exist?** Clearance agents exist for most;
   efficacy varies. HPV is preventable by vaccine but not
   curable-once-established. CVB has no dedicated antiviral yet
   (fluoxetine repurposed). Adjunct anti-inflammatory is mature across
   most.
3. **Wall crossable by new information?** Partially. Better clearance
   agents for established persistence would materially help. Mechanism
   completeness is not the main gap.
4. **Requires behavioral changes?** **Yes** — for most, the treatment
   is long (6 weeks to 3 months) and adherence-dependent.
5. **Who has tried?** Each disease-specific field individually; the
   cross-organism synthesis is newer and still informal.

**Classification: Mixed mechanism + behavioral wall.** Mechanism is
largely known; execution and adoption are the bottleneck. Same shape
as dysbiosis and blepharitis (see
`medical/dysbiosis/results/phase0_recheck_2026-04-14.md`).

## Why this directory exists

Three reasons the framework deserves its own home rather than being
scattered across per-disease directories:

1. **Cross-organism synergy.** Real patients are polymicrobially
   infected. Lid margin alone hosts 5 of the ~8 organisms
   (Demodex × 2 + Malassezia + Staph + *B. oleronius*). Treatment
   protocols that address one organism and ignore the others
   underperform broad-spectrum combined approaches. A framework
   that treats the 8-organism list as a unit captures this.

2. **Shared therapeutic architecture.** Two-phase
   (clearance + adjunct) is the pattern across all 8. Recognizing this
   collapses disease-specific guidelines into organism-specific
   ones, which is a smaller problem.

3. **Differential diagnosis routes through organism identification.**
   A patient with chronic inflammatory disease of unclear etiology
   benefits from a structured screen: which of the ~8 organisms is
   driving? The disease-specific workup doesn't ask this cleanly.

## Directory structure

```
medical/persistent_organisms/
├── PROBLEM.md                     ← this file
├── README.md                      ← nav + cross-refs to per-organism work
├── attempts/
│   ├── attempt_001_two_phase_architecture.md  ← planned
│   ├── attempt_002_differential_diagnosis.md  ← planned (which organism?)
│   └── ...
├── papers/                        ← key citations per organism
└── results/                       ← syntheses
```

## Relationship to existing per-disease directories

| Organism | Existing disease-specific work |
|----------|-------------------------------|
| CVB | `medical/t1dm/`, `medical/myocarditis/`, `medical/pericarditis/`, `medical/pancreatitis/`, `medical/pleurodynia/`, `medical/me_cfs/` |
| Demodex | `medical/blepharitis/` (2026-04-15 new), `medical/perioral_dermatitis/`, cross-refs in `medical/dysbiosis/numerics/run_046` |
| *P. gingivalis* | None dedicated; mentioned in dysbiosis/protocol_integration.md (M7 oral arm) |
| EBV | None dedicated; relevant to me_cfs, potential future MS directory |
| *H. pylori* | None dedicated |
| HPV | None dedicated |
| Malassezia + *C. acnes* | `medical/eczema/`, `medical/psoriasis/`, `medical/perioral_dermatitis/`, `medical/blepharitis/attempts/attempt_008` |
| Composite gut dysbiosis | `medical/dysbiosis/` (primary home) |

The existing directories are **organism → single-disease** instances.
This directory is the **cross-organism synthesis layer** that pulls
the instances up into a common framework.

## Relationship to `biology/evolution/`

- `biology/evolution/PROBLEM.md` asks: *why did these organisms evolve
  to persist?*
- This directory asks: *given that they persist and cause disease,
  what do we do about it?*

Both sides should reference each other without collapsing. Biology →
mechanism of persistence. Medical → clinical consequence + treatment.

## Work plan (initial)

1. **attempt_001: the two-phase architecture in detail.** How
   clearance + adjunct works across the 8 organisms; what goes wrong
   when either phase is skipped; why the adjunct is often more
   important than the clearance agent after the first few weeks.
2. **attempt_002: differential diagnosis by organism.** When a patient
   presents with unexplained chronic inflammatory disease, how to
   screen for each of the 8; which screens are free (physical exam),
   which are cheap (standard bloodwork), which require specialty
   (IVCM, periodontal probing, upper endoscopy).
3. **attempt_003: the coinfection problem.** Most real patients have
   2+ persistent organisms. How to sequence or combine treatment; when
   one blocks another; the lid-margin precedent as a model.
4. **Per-organism deep-dive attempts** as needed for organisms
   without existing dedicated directories (P. gingivalis, EBV,
   H. pylori, HPV, HHV-6/CMV).

## Status

Directory created 2026-04-15 as the medical-side companion to
biology/evolution/. Initial content: this PROBLEM.md + README
synthesis. Content expansion follows from subsequent /loop iterations
or direct operator instruction.

---

*Filed: 2026-04-15 | medical/persistent_organisms/PROBLEM.md*
*Companion: biology/evolution/ (viral side), medical/blepharitis/results/persistent_organism_pattern.md (original synthesis, now migrated here conceptually)*

---

## 2026-04-18 audit note (R28 from AUDIT_LOG fire 15; cross-confirmed by prior content-audit C23)

**Flagged claim (L41):** "anti-gingipain (COR388 trialed)" implied as an active clearance option for *P. gingivalis*.

**Correction:** COR388 / **atuzaginstat** (Cortexyme) **failed its GAIN trial Phase 2/3 primary endpoint in October 2021** in mild-to-moderate Alzheimer's disease. Cortexyme subsequently paused development, faced FDA clinical hold on safety signals (hepatotoxicity + subsequent questions about efficacy subgroup analyses), and pivoted to Quince Therapeutics with different program focus. **As of 2026, there is no active anti-gingipain clinical program for Alzheimer's or periodontitis**. This was independently identified by (i) my structural audit (R28), and (ii) the prior biology/evolution content audit (C23 at `medical/blepharitis/results/claim_audit_2026-04-15.md`) via different paths — structural vs WebSearch — a clean **cross-audit convergence** documented in the audit synthesis as an example of Three-Source-Triangulation retraction-culture evidence.

**Fix applied:** L41 inline updated to note GAIN failure + Cortexyme → Quince pivot. Original wording preserved above separator per Maps-Include-Noise v6.
