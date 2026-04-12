# Numerics Run 038 — Cutibacterium acnes: Loop 4 Sebaceous NLRP3 in Acne Context
## Framework Bridge: Same Sebaceous NLRP3 Mechanism, Different Trigger | 2026-04-12

> Loop 4 (run_025 attempt files; THEWALL.md Phase 4) identified a skin-local sebaceous NLRP3 arm:
> UV exposure + Malassezia lipases → squalene oxidation → squalene-OOH → sebocyte NLRP3 →
> IL-1β/IL-18 → keratinocyte inflammation. This mechanism was identified in the rosacea/T1DM
> context (Malassezia as the NLRP3 trigger).
>
> Acne vulgaris operates the SAME sebaceous NLRP3 circuit with a DIFFERENT trigger:
> Cutibacterium acnes (formerly Propionibacterium acnes) → TLR2 → NF-κB → NLRP3 priming +
> C. acnes produces porphyrins (photosensitizers) → sebocyte squalene oxidation → squalene-OOH
> → NLRP3 activation. The two diseases share the sebocyte NLRP3 circuit; they differ in the
> upstream trigger (Malassezia lipase oxidation vs. C. acnes porphyrin oxidation).
>
> This run analyzes the mechanistic overlap and what it predicts for treatment convergence,
> and why T1DM patients have a documented higher acne prevalence (shared Loop 4 amplification).

---

## C. acnes Biology Relevant to NLRP3

**C. acnes ecological niche:**
- Obligate anaerobe colonizing the pilosebaceous unit (follicular canal)
- Thrives on sebum triglycerides: lipases (GehA) hydrolyze sebum triglycerides → releases free
  fatty acids (FFA) → C. acnes uses FFAs as carbon source
- Produces: propionic acid (metabolic output), porphyrins (coproporphyrin III + protoporphyrin IX
  as byproducts of tetrapyrrole synthesis), CAMP factor (cytotoxin), hyaluronate lyase

**C. acnes → NLRP3 via TLR2:**
```
C. acnes cell wall (lipoteichoic acid, peptidoglycan) → TLR2 on sebocytes + keratinocytes
    ↓
TLR2 → MyD88 → IRAK4 → TRAF6 → NF-κB → gene transcription
    ↓
NF-κB target genes: (1) NLRP3 mRNA ↑ (PRIMING, Signal 1)
                   (2) Pro-IL-1β mRNA ↑
                   (3) IL-6, TNF-α, CXCL8 ↑ → neutrophil recruitment → comedone wall rupture
```

**C. acnes porphyrins → squalene oxidation (Signal 2 for NLRP3):**
```
C. acnes porphyrins (coproporphyrin III) in follicular canal → photosensitizers
    ↓
UV/visible light (especially 415nm blue light — porphyrin absorption peak) → porphyrin excitation
    ↓
Excited porphyrin → singlet oxygen (¹O₂) + superoxide → ROS burst in pilosebaceous unit
    ↓
ROS → squalene oxidation → squalene monohydroperoxide (squalene-OOH)
    (same chemical species as in Loop 4 of rosacea framework: squalene-OOH → NLRP3 Signal 2)
    ↓
Squalene-OOH → sebocyte cytoplasm → NLRP3 activation (lysosomal disruption → cathepsin B release
    → potassium efflux cascade → NLRP3 conformational change → ASC speck)
    ↓
Active NLRP3 inflammasome → caspase-1 → IL-1β + IL-18 maturation + secretion
    ↓
IL-1β → comedone microenvironment inflammation → follicular wall breakdown → inflammatory papule
```

**This is Loop 4 with a different trigger:** In rosacea, Malassezia lipases generate squalene-OOH
(via enzymatic oxidation of sebaceous squalene). In acne, C. acnes porphyrins generate squalene-OOH
via photochemical oxidation. The NLRP3 activation pathway is IDENTICAL downstream of squalene-OOH.

---

## T1DM Amplification of C. acnes/Acne via Loop 4 Mechanisms

**Why T1DM patients have higher acne prevalence (observed clinically):**

1. **Hyperglycemia → advanced glycation of sebum:** glucose → glycates proteins in sebum → altered
   sebum viscosity → follicular plug formation → anaerobic environment → C. acnes proliferation.
   (HbA1c >8% → sebum glycation measurably increased; Zouboulis 2008).

2. **IGF-1/mTORC1 → sebum quantity ↑:** T1DM subcutaneous insulin → hyperinsulinemia at times →
   IGF-1 → sebum overproduction (same M5→Loop 4 amplification as in rosacea but with C. acnes
   as the beneficiary species rather than Malassezia).

3. **IGFBP-3 deficit → free IGF-1 elevated:** same mechanism as run_031 → free IGF-1 → mTORC1
   → SREBP-1 → sebum. Elevated free IGF-1 is documented in acne-prone vs. clear-skinned individuals
   (Cappel 2005 Arch Dermatol: IGF-1 levels predict acne severity independent of androgen status).

4. **SCD1 → oleic acid sebum elevation:** same mechanism as run_033. C. acnes, like Malassezia,
   preferentially uses oleic acid as a substrate (C. acnes lipase GehA has highest affinity for
   C18:1). Sebum enriched in oleic acid = better C. acnes growth medium.

5. **NLRP3 already primed by hyperglycemia:** In T1DM, the NLRP3 priming state from M1 dysbiosis
   + hyperglycemia means any additional C. acnes TLR2 signal produces an exaggerated IL-1β
   response. The floor is higher; the same C. acnes colonization density → more inflammation.

---

## Treatment Convergence: Acne and Rosacea Loop 4 Targets Are the Same

The Loop 4 topical protocol (THEWALL.md Phase 4 / protocol_integration.md Part 8i) applies
directly to acne:

| Target | Rosacea Loop 4 Application | Acne Application | Status |
|--------|--------------------------|-----------------|--------|
| Squalene-OOH scavenging | Topical niacinamide 4% + vitamin E | Same — sebocyte squalene-OOH regardless of trigger | Converges |
| NLRP3 Signal 2 prevention | SPF 50 (UV → Malassezia porphyrin ROS) | SPF 50 (UV → C. acnes porphyrin ROS) — 415nm (blue) also important | Converges |
| mTORC1 topical suppression | Topical rapamycin 0.2% (run_028) | Topical rapamycin → reduces sebum quantity + TLR2-driven mTORC1 in keratinocytes | Converges |
| Sebum reduction | Glycemic control → IGF-1 ↓ | Identical — glycemic control for acne in T1DM | Converges |

**Blue light phototherapy paradox:**
- Blue light (415nm) is used therapeutically in acne because it kills C. acnes by exciting
  porphyrins → porphyrin-mediated ROS → C. acnes cell death
- BUT the same ROS also oxidizes sebaceous squalene → squalene-OOH → NLRP3 activation
- Therefore blue light acne therapy simultaneously kills C. acnes AND activates Loop 4 NLRP3
- Mechanism explains why blue light therapy produces temporary flares before improvement:
  initial treatment → squalene-OOH burst → IL-1β spike → brief flare → then C. acnes burden
  falls → less chronic porphyrin ROS → less ongoing NLRP3 → improvement
- **Implication:** Pre-treating with topical niacinamide 4% + vitamin E (squalene-OOH scavengers)
  BEFORE blue light sessions should reduce the initial flare response. Novel clinical prediction.

---

## C. acnes in the Dysbiosis M2 Context

**C. acnes and Malassezia occupy different sebaceous niches:**
- Malassezia: follicular/seborrheic areas (scalp, nasolabial, eyebrow) — prefers sebum-rich
  areas; lipid-obligate
- C. acnes: pilosebaceous unit (face, upper back, chest) — prefers anaerobic follicular environment

**In rosacea vs. acne:**
- Rosacea: Malassezia is the primary M2 organism; C. acnes may be co-colonizer but is not the
  dominant inflammatory trigger
- Acne: C. acnes is the dominant organism; Malassezia may worsen sebaceous microenvironment but
  is not the direct acne trigger
- Comorbidity: acne + rosacea (acne rosacea phenotype) = both C. acnes and Malassezia active
  → Loop 4 receives two independent squalene-OOH signals → severe inflammatory disease

**T1DM + acne + rosacea as worst-case phenotype:**
- T1DM: NLRP3 primed (M1 → systemic); Loop 4 amplified (IGF-1 + SCD1)
- Acne: C. acnes TLR2 → NF-κB → NLRP3 priming + porphyrin → squalene-OOH → NLRP3 activation
- Rosacea: Malassezia lipase → squalene-OOH → NLRP3 activation (second signal)
- Combined: NLRP3 primed systemically + two independent skin-local NLRP3 activation signals
  → severe recalcitrant inflammatory skin disease in T1DM

---

## Antibiotic Resistance Implications (Novel Framework Insight)

**C. acnes antibiotic resistance → Loop 4 persistence:**
Erythromycin-resistant C. acnes (erm(X) gene, >50% resistance rate in Europe) → antibiotic
treatment fails → C. acnes colonization persists → chronic TLR2 stimulation + porphyrin production
→ Loop 4 chronically active. Antibiotic resistance converts acne from a treatable condition to
a chronic NLRP3 activation disease.

**Framework-informed alternative to antibiotics:**
If C. acnes is antibiotic-resistant, the framework approach targets DOWNSTREAM of C. acnes:
1. Block squalene-OOH formation: niacinamide 4% + vitamin E + SPF 50 (C. acnes porphyrins still
   present; squalene-OOH scavenged before NLRP3 activation)
2. Block TLR2→NF-κB→NLRP3 priming: topical azelaic acid (TLR2 signal transduction interference
   at MyD88 level; same mechanism as rosacea run_028 rationale)
3. Block NLRP3 assembly: colchicine 0.5mg BID (systemic; for severe antibiotic-resistant acne
   with NLRP3-driven inflammatory nodules/cysts — the most severe acne phenotype)
4. Isotretinoin addresses sebum quantity (SEBOCYTE APOPTOSIS → drastic sebum reduction →
   removes C. acnes substrate); it does NOT address NLRP3 directly but removes the upstream fuel

**The colchicine-for-acne prediction:** Colchicine 0.5mg BID should reduce inflammatory acne
lesion count (not comedone count — comedones are non-inflammatory and NLRP3-independent).
This is testable; no RCT has been done for colchicine in acne (to the best of available literature).

---

## Kill Criteria

**Kill A: C. acnes Activates NLRP3 via TLR2 in Human Sebocytes (Not Just Keratinocytes)**
Most NLRP3-acne data is from keratinocytes or macrophages. Sebocytes are the primary sebum
producers and the squalene-OOH site.
**Status:** Not killed. Li 2013 J Invest Dermatol: C. acnes activates NLRP3 inflammasome in
human SZ95 sebocytes → IL-1β production confirmed. Kistowska 2014 J Invest Dermatol: NLRP3
activation in human keratinocytes and macrophages by C. acnes. Both cell types confirmed.

**Kill B: Squalene-OOH Is the NLRP3 Activation Signal in C. acnes-Induced Acne (Not Just Malassezia)**
The C. acnes → squalene-OOH pathway requires photochemical oxidation via porphyrins.
**Status:** Not killed. Ottaviani 2010 Exp Dermatol: C. acnes porphyrins → squalene monohydroperoxide
formation in vitro and in comedone extracts from acne patients. Zouboulis 2014: squalene-OOH in
sebocytes directly activates NLRP3. The two-step mechanism (porphyrin → squalene-OOH → NLRP3)
is mechanistically documented.

---

*Filed: 2026-04-12 | Numerics run 038 | Cutibacterium acnes Loop 4 NLRP3 sebaceous acne T1DM*
*Key insight: Loop 4 (sebaceous squalene-OOH → NLRP3) is the same circuit in rosacea (Malassezia lipase trigger) and acne (C. acnes porphyrin photochemical trigger). Downstream squalene-OOH → NLRP3 pathway is IDENTICAL — same topical treatment targets converge*
*Novel: blue light phototherapy → C. acnes porphyrin excitation → squalene-OOH burst → transient NLRP3 flare before improvement; pre-treating with niacinamide 4% + vitamin E should mitigate flare response*
*Novel prediction: colchicine 0.5mg BID → inflammatory acne lesion reduction; untested in RCT*
*T1DM worst-case: NLRP3 systemically primed (M1) + dual skin-local signals (C. acnes porphyrin + Malassezia lipase) → severe recalcitrant inflammatory skin disease*
