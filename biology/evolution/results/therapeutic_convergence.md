# Therapeutic Convergence Across Persistent-Organism Classes

> Synthesis note. The persistent-organism set's disease portfolio is
> unified enough that **single drugs work across multiple diseases
> via shared mechanisms**. This note catalogs the cross-organism
> repurposing patterns that emerged across attempts 002–010, and
> argues they are direct clinical evidence for the framework's
> utility: a small pharmacopoeia covers a large fraction of chronic
> persistent-organism disease.
>
> **VERIFICATION STATUS:** structural claims drawn from per-organism
> attempts (audit-corrected through batch 5). Specific dosing, trial
> evidence, and mechanism citations are at operator-call confidence
> pending further audit passes.
>
> Companions: `persistence_mechanisms_taxonomy.md`, `host_coevolution.md`,
> per-organism attempts 001–010.

---

## The pattern

Across the 10 organisms + 7 classes, certain drugs appear
repeatedly as primary or adjunct therapy. Their cross-class
efficacy comes from **shared host mechanisms** downstream of
organism-specific insults — specifically:

- MMP-9 inhibition (tissue-destruction control)
- NF-κB inhibition (general anti-inflammation)
- NLRP3 inflammasome suppression (inflammatory-cascade brake)
- IL-6 / IL-17 / IL-23 axis modulation (Th17 / chronic
  inflammation)
- B-cell depletion (adaptive-immune reservoir emptying)

Each maps to a host gene / pathway that attempt host-coevolution
(`results/host_coevolution.md`) identified as a shared substrate
across persistent-organism disease. The convergence is not
coincidence — it is the predictable consequence of these diseases
sharing inflammatory machinery.

---

## The doxycycline 40 mg case — cleanest cross-class convergence

**Doxycycline at sub-antimicrobial dose (40 mg modified-release,
brand name Oracea) works at a dose below antibacterial MIC but
retains multiple host-directed anti-inflammatory effects:**

- **Matrix metalloproteinase (MMP-9) inhibition** — reduces
  tissue destruction
- **ROS inhibition in neutrophils** — reduces bystander tissue
  damage
- **Protein kinase C inhibition** — reduces inflammatory
  signaling
- **Reduced VEGF / angiogenic signaling** — reduces
  telangiectasia
- **No antibacterial pressure at this dose** — does not drive
  resistance

**Clinical uses spanning the persistent-organism framework:**

| Disease | Class | Dose | Role | Source |
|---------|-------|------|------|--------|
| **Papulopustular rosacea** | 7 (Demodex) | 40 mg/day | FDA-approved (Oracea, 2006) | `medical/blepharitis/attempt_006` |
| **Ocular rosacea** | 7 | 40 mg/day × 3 mo | Off-label; widely used | `medical/blepharitis/attempt_006` |
| **Demodex blepharitis** (chronic inflammation) | 7 | 40 mg/day | Adjunct post-acaricide | same |
| **Periodontitis** (adjunct to SRP) | 6 (P. gingivalis) | 20–40 mg/day | FDA-approved (Periostat, 1998) | `biology/evolution/attempt_008` |
| **Meibomian gland dysfunction** | (ecosystem) | 40 mg/day | Dry-eye specialist use | `medical/blepharitis/attempt_006` |

**Same drug, same mechanism (MMP-9 inhibition), four disease
contexts across classes 6 and 7.** This is the single clearest
therapeutic-convergence pattern in the repo. It spans:
- A Gram-negative anaerobic bacterium (P. gingivalis)
- An arthropod (Demodex)
- A fungal ecosystem component (Malassezia in seb blepharitis)
- A Gram-positive bacterial ecosystem component (C. acnes in
  rosacea)

Across these, the **common downstream inflammatory substrate**
(MMP-9 activation, neutrophil ROS, tissue destruction) is what the
drug targets. The upstream organism biology is different; the drug
doesn't care.

**Implication:** patients with periodontitis + rosacea + blepharitis
(a common clinical trio — see `medical/blepharitis/results/cross_directory_drift.md`)
can be treated with a single sub-antimicrobial doxycycline regimen
that addresses all three simultaneously.

---

## Ivermectin — pan-class antiparasitic + unexpected antiviral

**Ivermectin has three separate mechanism-of-action categories:**

1. **GABA-gated Cl⁻ channel agonist in invertebrates** — paralyzes
   arthropods / nematodes; safe in mammals (no cross-reactive
   receptor)
2. **Importin α/β-1 nuclear-transport inhibitor** — blocks p65
   nuclear translocation (NF-κB signaling suppressed) — similar
   mechanism class to colchicine's p65-block
3. **Unknown additional mechanisms** — several anti-inflammatory
   effects not fully characterized

**Cross-class clinical uses:**

| Use | Class | Formulation | Dose |
|-----|-------|-------------|------|
| **Facial Demodex / rosacea** | 7 | Topical 1% cream (Soolantra, FDA 2014) | Daily |
| **Demodex blepharitis** | 7 | Off-label topical periocular | Daily |
| **Scabies** (Sarcoptes) | 7 | Oral 200 μg/kg × 1–2 | Dose-limited |
| **Onchocerciasis, lymphatic filariasis, strongyloidiasis** | 7 | Oral mass drug administration | Weight-based |
| **Severe demodicosis / refractory rosacea** | 7 | Oral off-label | 200 μg/kg × 1–2 |
| **Refractory Demodex blepharitis** | 7 | Oral off-label | same |

**Also shows in-vitro / in-vivo activity against:**
- Coxsackievirus (Benkahla 2018 CV-B4 in vitro and mouse model; fluoxetine is a stronger-effect analog)
- HIV, SARS-CoV-2, Zika (nuclear-transport inhibition; clinical efficacy limited)
- Various other viruses (via importin mechanism)

**Framework interpretation:** ivermectin is a **class-7
workhorse** (most direct utility against eukaryotic ectoparasites)
with **class-1 antiviral spillover activity** via the
importin mechanism. It is not a strong antiviral clinically at
topical ocular doses, but the NF-κB suppression contributes to
anti-inflammatory effect in rosacea.

---

## Metronidazole — class 6 + class 7 bridge

**Metronidazole mechanism:**
1. **Anaerobic bacterial killing** — requires reducing conditions
   to activate; toxic to Gram-neg + Gram-pos anaerobes
2. **Weak direct anti-Demodex activity**
3. **Host anti-inflammatory effects** (at any dose): neutrophil
   ROS suppression, reduced pro-inflammatory cytokine production

**Clinical uses:**

| Use | Class | Role |
|-----|-------|------|
| **Rosacea (topical MetroGel)** | 7 + 6 | First-line; primary anti-inflammatory |
| **Demodex blepharitis (topical, off-label)** | 7 | Weak direct + anti-inflammatory |
| **Periodontal therapy** | 6 | Systemic + metronidazole + amoxicillin standard |
| **H. pylori eradication** | 6 | Part of triple/quadruple therapy |
| **Bacterial vaginosis** | 6 | First-line |
| **Clostridioides difficile** | 6 | Secondary (vancomycin is first-line now) |

**Metronidazole is the clearest bridge between class-7 disease
(Demodex rosacea) and class-6 disease (periodontitis, H. pylori).**
Like doxycycline 40 mg, it's used for reasons both of organism
targeting and host anti-inflammation — but at antibacterial doses,
so resistance + microbiome side effects apply (unlike sub-
antimicrobial doxy).

---

## NLRP3 inflammasome suppressors — across many classes

The NLRP3 inflammasome (Demodex run_046, T1DM dysbiosis mechanism,
P. gingivalis pathway) sits downstream of many persistent-organism
insults. Drugs targeting it have broad cross-class applications:

**Colchicine:**
- Mechanism: microtubule disruption → IKK complex formation
  blocked (upstream NF-κB)
- Uses: gout (crystalline inflammasome), familial Mediterranean
  fever, pericarditis (CVB-class 2), Behçet's disease, coronary
  disease (COLCOT trial showed post-MI CVD benefit), Demodex
  rosacea (off-label inflammation control)

**β-hydroxybutyrate (BHB):**
- Mechanism: direct NLRP3 inhibition + HDAC inhibition
- Uses: ketogenic diet benefits for autoimmune / neurologic
  disease (T1DM protocol in dysbiosis framework cites this);
  not a licensed drug but widely used supplementally

**IL-1β-targeted biologics (canakinumab, anakinra):**
- Mechanism: block IL-1β signaling (downstream of inflammasome)
- Uses: CAPS (inflammasome-mutation syndromes), atherosclerosis
  (CANTOS trial showed major CVD benefit from IL-1β blockade),
  autoinflammatory disease broadly, hidradenitis suppurativa

**MCC950 (investigational):**
- Mechanism: direct NLRP3 inhibition
- Preclinical promise; trials in multiple indications

**Framework interpretation:** the NLRP3 pathway is a **class-
neutral inflammation hub**. Drugs that suppress it benefit
diseases across classes (rosacea, periodontitis, T1DM,
atherosclerosis, etc.). This matches the host-coevolution
observation that NLRP3 variants are repeatedly named across
persistent-organism disease associations.

---

## Anti-IL-6 / anti-TNF / anti-IL-17 biologics — shared
inflammatory substrate

The biologic era has produced drugs that target specific cytokines,
and these drugs consistently show efficacy across multiple
persistent-organism-driven chronic diseases:

| Drug class | Target | Diseases (across persistent-organism framework) |
|------------|--------|-------------------------------------------------|
| **Anti-TNF-α** (infliximab, adalimumab, etanercept) | TNF-α | RA (P. gingivalis), IBD (gut dysbiosis), psoriasis (C. acnes + Malassezia), uveitis |
| **Anti-IL-6R** (tocilizumab) | IL-6 signaling | RA, giant cell arteritis, CAR-T cytokine release |
| **Anti-IL-17A** (secukinumab, ixekizumab) | IL-17A | Psoriasis, ankylosing spondylitis, axial spondyloarthritis |
| **Anti-IL-23** (ustekinumab, risankizumab, guselkumab) | IL-23 + IL-12 (ustekinumab only) | Psoriasis, IBD, psoriatic arthritis |
| **Anti-IL-4/13** (dupilumab) | IL-4Rα | Atopic dermatitis (Malassezia contribution), asthma |

**The striking observation:** each of these biologics shows
efficacy across 3–5 diseases that previously looked unrelated.
From the persistent-organism framework view, they're not unrelated
— they share host cytokine circuits driven by different organism-
specific triggers.

**Modern inflammation therapy is converging on the shared
substrate**, which is precisely what the framework predicts
should happen.

---

## Anti-CD20 biologics — EBV-reservoir targeting

**Rituximab, ocrelizumab, ofatumumab** deplete CD20+ B cells.

**Original indication** was lymphoma. **Later uses** expanded to
autoimmune disease where B cells drive pathology:

- **MS** — ocrelizumab FDA-approved 2017 for relapsing + primary
  progressive MS. Very high efficacy.
- **RA** — rituximab (when TNF inhibitors fail)
- **Neuromyelitis optica spectrum disorder**
- **ANCA-associated vasculitis**

**Reframing via EBV causation:** since Bjornevik 2022 established
EBV as a causal driver of MS, the anti-CD20 efficacy in MS is
reinterpretable as **depleting the EBV reservoir**. Memory B cells
carrying EBV episomes are among the targets of CD20+ depletion.
The mechanism-level unification: **anti-CD20 for MS = targeted
persistent-organism-reservoir therapy**.

This reframing extends: anti-CD20 efficacy in Sjögren's, lupus,
and other B-cell autoimmune diseases may be partly targeting EBV
reservoirs, since EBV is implicated in each.

---

## Omega-3 fatty acids — cross-class anti-inflammatory

**Mechanism:**
- Competes with arachidonic acid for COX/LOX → reduced pro-
  inflammatory PGs/LTs; increased anti-inflammatory resolvins +
  protectins
- Incorporated into membrane phospholipids
- Modulates Th17/Treg balance

**Uses across persistent-organism framework:**

| Use | Relevance |
|-----|-----------|
| Dry eye / MGD | Incorporated into meibum, improves quality (Malassezia + Demodex + C. acnes ecosystem) |
| Rheumatoid arthritis | Reduced joint inflammation |
| Cardiovascular disease | Reduced plaque burden (debated in recent trials) |
| Psoriasis | Moderate reduction in severity |
| IBD (maintenance) | Moderate effect |

Omega-3 is not a high-efficacy single-disease drug, but its
modest cross-class utility is consistent with it acting on the
shared inflammatory substrate.

---

## The framework prediction — "treat the substrate, not each organism"

Pulling this together:

**Persistent-organism diseases share a downstream inflammatory
substrate. Treatment targeting the substrate works across
diseases. Treatment targeting a specific organism works only for
that disease.**

This has practical consequences:

1. **Cross-specialty opportunities**: a rheumatologist prescribing
   doxycycline 40 mg for RA, a dermatologist for rosacea, a
   dentist for periodontitis are all using the same drug for the
   same host mechanism against organism-diverse triggers. Sharing
   this insight across specialties would accelerate awareness and
   use.
2. **Biomarker-driven therapy**: identifying the specific
   inflammatory axis in a patient (Th17-dominant? NLRP3-active?
   TNF-high?) could guide treatment selection more precisely than
   disease-specific guidelines.
3. **Combination therapy logic**: pairing an organism-specific
   clearance agent (acaricide, antiviral, antibiotic) with a
   substrate-targeting anti-inflammatory is the **two-phase
   therapeutic architecture** defined in
   `medical/persistent_organisms/PROBLEM.md`. This synthesis
   shows that phase 2 is often the same drug across diseases.
4. **Drug-discovery priority**: developing better MMP-9 / NLRP3 /
   IL-6 targeting agents has disproportionately high cross-class
   return. A new NLRP3 inhibitor that beats MCC950 could benefit
   rosacea + periodontitis + T1DM + atherosclerosis + CAPS +
   gout simultaneously.

---

## Open questions

1. **Are there cross-class drug candidates currently in
   development?** Scan of phase 2/3 inflammation-pathway drugs
   would likely identify several.
2. **What is the real clinical overlap in patients?** If
   periodontitis + rosacea + RA comorbidity is common, sub-
   antimicrobial doxycycline should already be helping — is it
   prescribed that way? Mostly not, per specialty-silo patterns.
3. **Does treating one persistent-organism disease improve others
   in the same patient?** Occasionally reported anecdotally
   (treating rosacea with ivermectin improving concurrent
   demodicosis + blepharitis). Systematic study would be
   valuable.
4. **Is there a theoretical upper bound to cross-class therapeutic
   convergence?** Maybe — the more specific a therapeutic target
   (organism-specific clearance), the less cross-class utility. At
   the substrate level (MMP-9, NLRP3), maximum cross-class.
   Biologics sit in between.
5. **Will the framework's predictions be validated by
   forthcoming cross-disease trials?** Several IL-6/IL-17/IL-23
   biologics are being tested in diseases that would be predicted
   to respond under this framework.

---

## Status of biology/evolution/ synthesis work

From attempt_010 + taxonomy + host-coevolution closeouts:

1. ✅ 7-class taxonomy — `persistence_mechanisms_taxonomy.md`
2. ✅ Host-side coevolution — `host_coevolution.md`
3. ✅ **Therapeutic convergence (this note)**
4. ⏳ Modernity trajectory analysis — H. pylori ↓ vs P. gingivalis /
   Demodex ↑ under Western diet + sanitation pressures
5. ⏳ Class-boundary cases — M. tuberculosis, Toxoplasma,
   Trypanosoma as framework extensions
6. ⏳ `attempts/attempt_001_persistence_as_strategy.md` update to
   reference the 7-class taxonomy

Half the recommended synthesis work is now done. The remaining
items are more speculative (trajectory analysis) or boundary-
testing (extending to non-listed organisms).

---

*Filed: 2026-04-15 | biology/evolution/results/therapeutic_convergence.md*
*Companions: persistence_mechanisms_taxonomy.md, host_coevolution.md, attempts 002–010*
*Key empirical grounding: doxycycline 40 mg (Oracea, Periostat), ivermectin (Soolantra + oral), metronidazole, colchicine, anti-CD20 in MS (ocrelizumab)*
