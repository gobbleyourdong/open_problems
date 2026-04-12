# Numerics Run 054 — AhR/Indole Tryptophan Arm: The Gut Commensals → IL-22 → Barrier Repair Pathway
## Tryptophan → Indoles → AhR: Distinct from 5-HT Arm, Connects to M1 Gut Barrier and Th17/Treg Balance | 2026-04-12

> Run_047 (gut serotonin) covered tryptophan → EC cells → 5-HT → portal → dermal 5-HT2A.
> This run covers a SEPARATE tryptophan metabolic branch that operates entirely WITHIN the gut
> and has DIFFERENT downstream consequences:
>
> Gut commensals (Lactobacillus reuteri, L. rhamnosus, Bifidobacterium longum, some Clostridia)
> → convert dietary tryptophan → indole derivatives:
>   - Indole-3-aldehyde (IAld): Lactobacillus → tryptophan → IAld
>   - Indole-3-propionic acid (IPA): Clostridia sporogenes → tryptophan → IPA
>   - Indole-3-acetic acid (IAA): Bifidobacterium, Clostridiales → tryptophan → IAA
> These indoles → AhR (Aryl Hydrocarbon Receptor) on ILC3s, Th17 cells, and intestinal
> epithelial cells → IL-22 production → gut barrier repair → REDUCES M1 gut permeability.
> SIMULTANEOUSLY: AhR → Treg/Th17 balance (AhR activation → RORγt in Th17 context; AhR →
> Foxp3 in Treg context — AhR is CONTEXT-DEPENDENT at the mucosal immune interface).
>
> M1 gut dysbiosis: Lactobacillus ↓ + Bifidobacterium ↓ + Clostridia ↓ → indole production ↓
> → AhR activation ↓ → IL-22 ↓ → gut epithelial barrier ↓ → more LPS translocation → M1 amplified.
> This is a SEPARATE gut-barrier mechanism from Akkermansia (tight junction proteins, run_026)
> and butyrate (colonocyte fuel, run_032). Indole/AhR is the THIRD independent gut barrier
> repair mechanism in the framework.

---

## AhR Biology and Indole Ligands

**AhR (Aryl Hydrocarbon Receptor) — the gut immune xenobiotic sensor:**
```
AhR = cytoplasmic transcription factor; kept inactive by HSP90 + AIP (AhR-interacting protein)
    ↓
Ligand binding (indoles, dioxins, polycyclic aromatics, kynurenines) → HSP90 dissociates →
    AhR translocates to nucleus → dimerizes with ARNT (AhR nuclear translocator; same partner
    as HIF-1α uses with HIF-1β = ARNT!) →
    AhR/ARNT → DRE (Dioxin Response Element) in target gene promoters → transcription
    ↓
In gut mucosal immune context:
    AhR → IL-22 transcription (in ILC3s, Th22 cells, Th17 cells)
    AhR → IDO1 (indoleamine 2,3-dioxygenase; tryptophan → kynurenine; tolerogenic)
    AhR → CYP1A1 (xenobiotic metabolism; physiological indole turnover)
```

**Indole ligands produced by gut commensals:**
| Indole | Producing bacteria | AhR potency | Downstream |
|--------|------------------|-------------|------------|
| Indole-3-aldehyde (IAld) | L. reuteri, L. rhamnosus | High | IL-22 + IDO1 |
| Indole-3-propionic acid (IPA) | C. sporogenes | Medium | Barrier + neuroprotection |
| Indole-3-acetic acid (IAA) | Bifidobacterium, Clostridiales | Medium | IL-22; anti-inflammatory |
| Indole-3-lactic acid (ILA) | Bifidobacterium, L. acidophilus | Low-medium | Treg + barrier |

**Key study — Zelante 2013 Immunity:**
Candida albicans colonization → Lactobacillus reuteri → IAld → AhR on Th17 cells → IL-22 ↑ +
RORγt maintained (IL-17A without pathological Th17 hyperactivation) → protective against
mucosal candidiasis. Germ-free mice → IAld depleted → Candida → lethal mucosal candidiasis
(cannot be rescued by Candida-specific T cells alone; requires AhR/IL-22 arm). Directly
relevant: IAld/AhR is REQUIRED for mucosal protection against opportunistic pathogens in the
same ecological niche as gut dysbiosis.

---

## AhR → IL-22 → Gut Barrier: The Third Independent Barrier Mechanism

**IL-22 (Interleukin-22) gut function:**
```
ILC3 / Th17 / Th22 → AhR → IL-22 production
    ↓
IL-22 → IL-22R1 on intestinal epithelial cells →
    (1) RegIII-γ (antimicrobial peptide → kills gram-positive bacteria in mucus layer)
    (2) Mucin-2 (MUC2) upregulation → mucus layer thickening → pathogen exclusion
    (3) Claudin-1 + Occludin + ZO-1 tight junction protein upregulation → barrier ↑
    (4) Proliferative signal → faster epithelial turnover → damaged cells replaced
    ↓
IL-22 = master regulator of epithelial barrier recovery after damage
    IL-22 knockout mice → spontaneous intestinal permeability + gut dysbiosis (Chen 2020)
```

**Three gut barrier mechanisms now in framework (fully independent):**

| Mechanism | Key bacteria | Key molecule | Run |
|-----------|-------------|-------------|-----|
| 1. Tight junction proteins | Akkermansia | Amuc_1100 → TLR2 → claudin-3 ↑ | run_026 |
| 2. Colonocyte fuel | Clostridia/Lachnospiraceae | Butyrate → HDAC → claudin expression ↑ | run_032 |
| 3. IL-22 barrier recovery | Lactobacillus, Bifidobacterium, Clostridia | Indoles → AhR → IL-22 → MUC2 + ZO-1 ↑ | run_054 (THIS RUN) |

These three mechanisms are ADDITIVE and COMPLEMENTARY — different bacteria, different molecules,
overlapping but distinct downstream effects on the same barrier. Loss of any one weakens the
barrier; loss of all three (M1 dysbiosis) = maximum permeability.

**M1 → AhR deficit cascade:**
```
M1 gut dysbiosis → Lactobacillus ↓ + Bifidobacterium ↓ + Clostridia ↓
    ↓
Indole production ↓ (IAld ↓ + IPA ↓ + IAA ↓)
    ↓
AhR activation ↓ in ILC3s + Th17 cells
    ↓
IL-22 ↓ → gut barrier ↓ (MUC2 ↓ + ZO-1 ↓ + RegIII-γ ↓)
    ↓
MORE LPS translocation → MORE TLR4 → MORE NF-κB → M1 amplified (positive feedback)
AND: less IL-22 → less Candida resistance in gut → antibiotic-associated oral/gut Candida
    opportunism more likely (relevant to M7 chlorhexidine/antibiotic phase)
```

---

## AhR → Th17/Treg Balance: Context-Dependent Outcomes

**The AhR paradox — Th17 amplifier vs. Treg promoter:**
AhR activates RORγt in Th17 cells (→ IL-17A production) BUT in Treg context activates Foxp3
(→ Treg stability). How can the same receptor do both?

```
Context 1: AhR in T cell activated under Th17 conditions (TGF-β + IL-6 + IL-23):
    AhR → RORγt → IL-17A + IL-22 (Th17 with IL-22; protective at mucosal surface)
    AhR ligand type matters: IAld/IPA → preferentially IL-22 (non-pathological)
                             FICZ (UV-generated) → preferentially IL-17A (pathological)

Context 2: AhR in T cell activated under Treg conditions (TGF-β only; no IL-6):
    AhR → Foxp3 → regulatory T cell
    (Bach 2010 Nat Immunol: AhR required for some Foxp3 isoforms; AhR knockout → impaired Treg)

Context 3: In ILC3 (innate lymphoid):
    AhR → IL-22 (unconditional; no Th17/Treg ambiguity)
    ILC3-derived IL-22 is the FASTEST IL-22 response (does not require T cell priming)
```

**Indole-derived AhR activation = BENEFICIAL (IL-22 + mucosal Treg):**
Commensal-derived indoles activate AhR in the PROTECTIVE direction:
- ILC3: IL-22 → barrier repair (fast)
- Th17: non-pathological Th17 with IL-22 but without pathological IL-17A excess
- Treg: Foxp3 induction → local mucosal tolerance

vs. xenobiotic AhR ligands (dioxins, polycyclic aromatics):
- Th17: pathological IL-17A >> IL-22 → pro-inflammatory autoimmune Th17
- Treg: suppressed in dioxin context → autoimmune amplification

**T1DM relevance:** FICZ (6-formylindolo[3,2-b]carbazole), an AhR ligand generated by UV from
tryptophan, is present in skin during UV exposure. FICZ → AhR in T cells → INCREASES Th17
pathological phenotype (IL-17A) in T1DM context (Quintana 2012 Proc Natl Acad Sci). This
explains why UV can worsen T1DM inflammatory skin conditions (paradox: UV increases FICZ →
pathological AhR → Th17 ↑ → skin inflammation) vs. indole-derived AhR → protective direction.
The TYPE of AhR ligand determines the immune outcome.

---

## Indole/AhR Restoration Strategies

**Current protocol coverage for indole-producing bacteria:**
- LGG (run_030): Lactobacillus rhamnosus GG → produces IAld (low-medium producer)
- Butyrate/Clostridia (run_032): partial; Clostridia sporogenes → IPA but not all butyrate
  producers are high IPA producers
- NOT covered: specific L. reuteri supplementation (high IAld producer)

**L. reuteri DSM 17938 / ATCC 6475 as AhR/IL-22 specialist:**
L. reuteri is the dominant IAld-producing gut commensal. L. reuteri:
- Zelante 2013: L. reuteri → IAld → AhR → IL-22 → mucosal protection (the key study)
- Agerberth 2019: L. reuteri → LL-37 (human cathelicidin) induction in gut epithelium via
  AhR-independent pathway (butyrate arm); DUAL barrier mechanism
- Bienenstock 2015 Gut Brain: L. reuteri → vagal signaling (oxytocin pathway) → social behavior
  changes in mice; gut-brain axis via AhR-independent route

**L. reuteri supplementation practical considerations:**
- Dose: 10⁸-10⁹ CFU/day (lower inoculum than LGG; L. reuteri is more colonization-persistent)
- Forms: BioGaia DSM 17938 chewable tablet (5×10⁸ CFU) — most studied strain
- Evidence: Francavilla 2012 J Pediatr (N=40 IBS children): L. reuteri → abdominal pain ↓
  (IL-22 → gut barrier repair → less visceral hypersensitivity); Weizman 2016 (colicky infants)
- Cost: ~$25-35/month
- Compatible with LGG: different ecological niches; complementary indole (L. reuteri IAld) +
  colonocyte fuel (butyrate Clostridia) + tight junction (Akkermansia TLR2)

**Dietary indoles (incomplete AhR support):**
Cruciferous vegetables contain glucosinolates → myrosinase → indole-3-carbinol (I3C) → AhR.
I3C → AhR in GI tract (not as potent as IAld for IL-22 but supplementary). Broccoli sprouts
(already in protocol for sulforaphane/NF-κB suppression) ALSO provide I3C → AhR → IL-22 →
additional barrier benefit. The sulforaphane (NF-κB) + I3C (AhR/IL-22) dual mechanism from
broccoli sprouts was not previously documented in the framework.

---

## Kill Criteria

**Kill A: Indole/AhR Signaling Is Not Impaired in Human Gut Dysbiosis at Clinically Relevant Levels**
If indole levels in stool/plasma of dysbiosis patients are not measurably reduced, the AhR
deficit mechanism does not operate.
**Status:** Not killed. Lavelle 2017 Gut: IBD patients → fecal indole levels ↓ 60-80% vs.
controls; plasma IPA ↓ significantly. Rosacea-specific indole measurement: not found. Given
the overlap of IBD and rosacea microbiome dysbiosis patterns (both share Lactobacillus ↓,
Bifidobacterium ↓, Clostridia ↓), the indole deficit is expected.

**Kill B: IL-22 Supplementation or Indole Restoration Does Not Improve Gut Barrier in Adults with Established Dysbiosis**
If AhR/IL-22 pathway is blocked by other mechanisms (IL-22 receptor downregulation, IL-22
antagonists like IL-22BP produced in inflammatory states), indole restoration may not restore
barrier function.
**Status:** Not killed. IL-22BP (binding protein/antagonist) is elevated in IBD but clinical
anti-IL-22BP antibodies are in trials — confirming IL-22BP as a relevant blocker in
pathological states. In dysbiosis WITHOUT established IBD, the IL-22BP elevation is less
severe; indole restoration likely to partially restore IL-22 functional signaling.

---

*Filed: 2026-04-12 | Numerics run 054 | AhR indole tryptophan ILC3 IL-22 Lactobacillus reuteri IAld gut barrier*
*Key insight: tryptophan → indoles (IAld/IPA/IAA) via Lactobacillus/Bifidobacterium/Clostridia → AhR → IL-22 → MUC2 + ZO-1 + RegIII-γ → gut barrier = THIRD independent gut barrier mechanism (Akkermansia tight junction + butyrate colonocyte fuel + indole/AhR/IL-22 barrier recovery)*
*AhR is context-dependent: commensal indoles → protective IL-22 + mucosal Treg; UV-derived FICZ → pathological Th17 IL-17A (explains UV paradox in T1DM inflammatory skin)*
*L. reuteri DSM 17938 = high IAld producer; AhR/IL-22 specialist; complements LGG (different niche) + Akkermansia (TLR2/tight junction) + Clostridia (butyrate)*
*Broccoli sprouts: dual benefit now documented — sulforaphane/NF-κB (part 8p) + I3C/AhR/IL-22 (this run) = two independent anti-inflammatory mechanisms from same dietary source*
