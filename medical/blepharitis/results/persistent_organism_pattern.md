# Persistent-Organism Pattern — Synthesis from the Blepharitis Directory

> Short cross-directory synthesis note, not a new top-level framework.
> Captures an intellectual thread the operator raised during the
> construction of `medical/blepharitis/`: a small number of persistent
> organisms drive a surprising fraction of chronic human disease, and
> the blepharitis work is a concrete instance of the broader pattern.
>
> Scope of this note: observation + what the pattern predicts + where
> it breaks. A dedicated `medical/persistent_organisms/` directory
> would be the natural next step if the operator wants to formalize;
> this note deliberately stays small.

---

## The observation

Across the chronic-disease work in this repo (and the public
literature), a small recurring list of organisms shows up as
upstream drivers:

| Organism | Persistence niche | Associated chronic conditions |
|----------|-------------------|-------------------------------|
| **Coxsackievirus B (CVB)** | Pancreas, heart, muscle | T1DM, myocarditis, DCM, pericarditis, pancreatitis, pleurodynia, some ME/CFS |
| **Demodex folliculorum / brevis** | Hair follicle, meibomian gland | Rosacea, anterior blepharitis, MGD, chalazion, POD, demodicosis |
| ***Porphyromonas gingivalis*** | Periodontal pocket | Periodontitis, rheumatoid arthritis, Alzheimer's, atherosclerosis, preterm birth |
| **Epstein-Barr virus (EBV)** | B cells | MS (Bjornevik 2022 causal), several lymphomas, post-viral fatigue, autoimmunity |
| ***Helicobacter pylori*** | Gastric mucosa | Gastric ulcer, gastric cancer, MALT lymphoma |
| **HPV (high-risk types)** | Epithelium | Cervical, oropharyngeal, anal cancers |
| ***Malassezia* + *Cutibacterium acnes*** | Sebaceous sites | Seb-derm, acne, dandruff, Malassezia folliculitis |
| **Composite gut dysbiosis** | Colon, small bowel | IBD, T1DM initiation, metabolic syndrome |
| **HHV-6, CMV** *(weaker evidence)* | Lymphocytes | ME/CFS, transplant complications, some neurological |

Three to ten, depending on how strict you are about "established causal."

## What the pattern predicts

The structure that repeats:

```
persistent organism + tolerance breakdown
    ↓
chronic low-grade innate-immune activation
    ↓
downstream tissue-specific pathology (often at a site distant from
the organism's niche)
    ↓
self-sustaining inflammatory loop that outlives the organism's
presence (KLK5/LL-37 in rosacea; NLRP3 in T1DM; IgG2a + citrullination
in P. gingivalis → RA)
```

If this is the right abstraction, then:

1. **Treatment collapses to two phases.** (i) Reduce organism burden
   with targeted agent (acaricide / antiviral / antibacterial /
   antifungal). (ii) Layer anti-inflammatory management to quench
   the self-sustaining loop the organism initiated. This is exactly
   the structure of `attempt_006_chronic_inflammation_after_clearance.md`
   generalized to any of the ~8 organisms.

2. **Disease-specific guidelines are the wrong abstraction level.**
   Instead of "rosacea protocol + blepharitis protocol + chalazion
   protocol," one "Demodex-driven lid-face complex" protocol covers
   all three. Same pattern applies across organism-defined disease
   clusters.

3. **Cross-organism synergy matters.** The lid margin (attempt_008)
   hosts Demodex + Malassezia + Staph + Cutibacterium + *B. oleronius*
   simultaneously. Broad-spectrum TTO addresses all five at once,
   which is why it works across phenotypes. This generalizes: at any
   sebaceous-rich site, treatment strategies that cover the ecosystem
   outperform single-organism approaches.

4. **Latency matters.** CVB acute infection is mostly self-limiting;
   it's the *persistent* form (5'-UTR-deleted, replication-stalled) that
   drives T1DM. H. pylori acute infection is largely silent; 30-year
   persistence drives cancer. EBV primary infection is mono; 40-year
   latency drives MS risk. The "persistent" qualifier is load-bearing —
   transient infections of the same organisms don't generate the same
   disease burden.

## Concrete instance: the lid margin (from this directory)

5 persistent organisms at one anatomic site:

- Demodex folliculorum (lash follicle)
- Demodex brevis (meibomian gland)
- Malassezia spp. (sebaceous/meibum lipid layer)
- Staphylococcus spp. (lid-margin skin)
- *Bacillus oleronius* (endosymbiont inside Demodex)

Each contributes to chronic blepharitis / MGD / chalazion / rosacea
in different balances. TTO + hypochlorous + doxycycline + omega-3
covers the five-organism ecosystem; that's why mixed-phenotype patients
respond to protocols that don't strictly target their dominant
organism.

**This is a 1:1 instance of the broader pattern.** The lid margin
maps to *"localized site hosting multiple persistent organisms + host
inflammatory response."* Other sites with parallel structure:

- Oral cavity / gingiva → *P. gingivalis* + other red-complex anaerobes
  + Candida + HSV-1 latency
- Gut → composite dysbiosis + *H. pylori* (upper) + C. difficile
  (post-antibiotic)
- Pancreatic islet → CVB persistence + any intra-islet commensal
  state (still debated)
- Heart (post-infection) → CVB RNA persistence + subsequent immune
  activation

## Where the pattern breaks

1. **Primary autoimmune without infectious precedent.** True autoimmune
   disease where no organism has been identified — systemic lupus
   erythematosus broadly, some forms of autoimmune hepatitis, some
   vitiligo phenotypes. The "persistent organism" frame suggests
   looking harder; it does not guarantee one will be found.

2. **Genetic and metabolic disease.** Hereditary hemochromatosis,
   cystic fibrosis, Huntington's, familial hypercholesterolemia — these
   are genotype-driven and organism-independent. The frame doesn't
   apply.

3. **Cancer outside the documented oncogenic viruses.** HPV drives
   cervical cancer, EBV drives certain lymphomas, HBV/HCV drive HCC,
   *H. pylori* drives gastric cancer. But most solid tumors
   (pancreatic, prostate, colorectal, most lung) are not
   persistent-organism-driven in the same simple sense.

4. **Co-infection as the norm, not the exception.** Most real patients
   have multiple persistent organisms simultaneously. Attribution of a
   specific syndrome to a specific organism is often statistical, not
   mechanistic. The frame assumes cleaner organism-attribution than
   real populations show.

5. **Host genetic susceptibility modulates penetrance heavily.** HLA
   genotype determines whether CVB exposure produces T1DM (rare) or a
   transient febrile illness (common). The organism is necessary but
   not sufficient; the frame needs a host-response co-axis.

## Therapeutic architecture implied

Per-organism "clearance + adjunct" recipe:

| Organism | Clearance agent(s) | Adjunct |
|----------|--------------------|---------|
| CVB | Fluoxetine (antiviral in cells), BHB / NLRP3 suppressors, potential nucleoside analogs | Anti-inflammatory (colchicine, resolvins, ivermectin NF-κB), metabolic (keto for β-cell rest) |
| Demodex | Tea tree oil / T4O, ivermectin (topical + oral), lotilaner (ocular only), permethrin, sulfur | Doxycycline 40 mg, omega-3, hypochlorous acid |
| *P. gingivalis* | Professional periodontal therapy, local antimicrobials, anti-gingipain (COR388 trialed) | Systemic anti-inflammatory (doxycycline, resolvins), RA-specific DMARDs if RA present |
| EBV | Valacyclovir, valganciclovir (limited efficacy; latent cycle not reachable), tenofovir alafenamide (experimental for MS) | Vitamin D, immunomodulation per downstream syndrome |
| *H. pylori* | Triple/quadruple antibiotic therapy, bismuth regimens | PPI, gastric mucosal healing |
| HPV | Vaccination (Gardasil 9) for prevention; topical imiquimod / 5-FU / cryo for lesions | LEEP / conization for dysplasia; no clearance for established disease |
| Malassezia + C. acnes | Ketoconazole, selenium sulfide, benzoyl peroxide, topical retinoids | Zinc pyrithione, omega-6 modulation |
| Gut dysbiosis | Targeted antibiotics (rifaximin for SIBO), FMT (C. diff specifically), prebiotic / probiotic / dietary pattern | Butyrate, SCFA supplementation, barrier repair (L-glutamine, zinc carnosine) |

Each row has the same two-phase structure: **reduce burden + layer
anti-inflammatory.**

## Implication for the repo

This directory (`medical/blepharitis/`) naturally becomes an instance
of the broader framework. Other instances already in the repo:

- `medical/dysbiosis/` — gut + multi-site dysbiosis instance
- `medical/t1dm/` — CVB + pancreas instance
- `medical/myocarditis/`, `medical/pericarditis/`, etc. — CVB + heart
  instances
- `medical/perioral_dermatitis/` — Demodex + child-skin instance
- `medical/eczema/`, `medical/psoriasis/` — dysbiosis + skin-barrier
  instances

If the operator wants to formalize the framework, the next step is
`medical/persistent_organisms/README.md` pulling the above into one
explicit reference. This note deliberately stops short — it reports the
observation and its concrete instance here, without committing to a
directory-level reorganization.

---

## Honest calibration

The pattern is real but not the whole picture.

- Strong evidence: CVB→T1DM, *P. gingivalis*→periodontitis, EBV→MS,
  HPV→cervical cancer, *H. pylori*→gastric cancer, Demodex→rosacea.
- Moderate evidence: several gut-dysbiosis composite conditions;
  Malassezia→seb-derm; *C. acnes*→acne.
- Speculative: CVB→ME/CFS; *P. gingivalis*→Alzheimer's (Dominy 2019
  contested); HHV-6→specific syndromes.

The frame is a **heuristic for where to look, not a universal theory
of chronic disease.** Specifically: when a chronic condition has
unclear etiology + inflammatory biomarker elevation + site-specific
damage, the frame says "look for a persistent organism at a plausible
niche." Sometimes there is one. Sometimes there isn't and the answer
is elsewhere.

---

*Filed: 2026-04-15 | results/persistent_organism_pattern.md*
*Short synthesis; not a new top-level directory*
*Cross-reference: attempts 001–008 this directory; dysbiosis/run_046 (rosacea mechanism); t1dm/ (CVB instance)*
