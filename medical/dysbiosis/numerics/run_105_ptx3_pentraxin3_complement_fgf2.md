# run_105 — PTX3 (Pentraxin-3): Tissue-Local Complement Initiation; FGF-2/Angiogenesis; IL-1β Feedback Loop; T1DM SNP and Endothelial Damage

**Date:** 2026-04-12
**Status:** Complete
**Iteration:** 105
**Mountain:** M4 (innate immune threshold) — tissue-local pattern recognition; M2 (skin angiogenesis arm)
**Cross-connection:** Complement/run_101 (local C1q→C3a/C5a); Loop 2/run_083 (NLRP3→IL-1β→PTX3 feedback); UV/alarmin/run_099 (mast cell TNF-α→PTX3); T1DM (Chiarini 2010 SNP; microalbuminuria); ME/CFS (endothelial PTX3)

---

## 1. Kill-First Evaluation

**Gap claim**: PTX3 (pentraxin-3, TSG-14) is completely absent from all 104 prior runs. Run_101 covers complement activation, but covers circulating complement components and systemic/UV-driven generation. PTX3 is a tissue-local pattern recognition molecule produced by mast cells, macrophages, DCs, endothelial cells, and fibroblasts — not primarily hepatocytes (unlike CRP).

**Kill pressure applied:**

**Challenge 1**: Run_101 already covers complement activation comprehensively (C3a/C5a, Signal 1E, UV mechanism, C4A null). What does PTX3 add that is not derivative?

**Defense**: Three genuinely new elements not in run_101:
(a) **LOCAL production source**: PTX3 is produced IN SITU by skin-resident mast cells, dermal macrophages, and endothelial cells — it activates classical complement locally before systemic complement arrives. Run_101 covers circulating C3/C5 cleavage; PTX3 covers the cell-produced INITIATOR of the classical pathway operating at millimolar distances from the inflammatory focus.
(b) **FGF-2 sequestration**: PTX3 binds FGF-2 (basic FGF, fibroblast growth factor 2) with nanomolar affinity — completely absent from framework. In rosacea, FGF-2-driven neovascularization produces telangiectasias. PTX3 → FGF-2 sequestration → paradoxical anti-angiogenic effect is the ONLY FGF-2 axis in the entire framework.
(c) **IL-1β → PTX3 → C1q positive feedback loop**: IL-1β (NLRP3 product) → PTX3 ↑ in endothelial cells/fibroblasts → PTX3 → C1q → classical complement → C5a (run_101 Signal 1E substrate) → NLRP3 priming. This creates a new Loop 2 amplification arc not identified in any prior run.

**Challenge 2**: Rosacea-specific PTX3 evidence?

**Defense**: Direct rosacea PTX3 data is limited. However: (a) C3d complement deposits in rosacea skin (Chiller 2002 Arch Dermatol, already in run_101) are consistent with local complement activation via PTX3/C1q; (b) mast cells and activated macrophages — both established rosacea cell types — are the primary tissue PTX3 producers; (c) FGF-2 is documented elevated in rosacea skin (Gomaa 2007 Int J Dermatol: FGF-2 elevated in ETR/PPR vs. controls), providing direct relevance for the FGF-2/angiogenesis connection; (d) T1DM evidence is strong enough to include the mechanism regardless of rosacea direct data gap.

**Challenge 3**: Is PTX3's paradoxical complement-regulatory role (sometimes anti-inflammatory) a confound?

**Defense**: The paradox is important and mechanistically informative — not a confound. PTX3 competes with CRP at C1q binding (Deban 2010 Nat Immunol). When PTX3 is in large excess relative to CRP, it can REDUCE complement activation (competitive inhibition). When PTX3 is in moderate amounts alongside CRP (the typical case in active rosacea/T1DM), both cooperate at C1q → additive complement activation. The regulatory arm is relevant for interpretation of PTX3 as a therapeutic target (pro-inflammatory to modulate, not simply anti-inflammatory to preserve).

**Challenge 4**: T1DM PTX3 evidence — is it biomarker-only or mechanistic?

**Defense**: Chiarini 2010 Autoimmunity demonstrates a PTX3 promoter SNP (rs3816527) associated with T1DM susceptibility — this is a genetic mechanistic claim, not merely a biomarker correlation. PTX3 is produced by activated islet macrophages during insulitis (consistent with M1 macrophage production), creating local complement activation in the islet microenvironment. Additionally, PTX3 correlates with microalbuminuria (early renal/endothelial damage marker in T1DM), suggesting PTX3-driven endothelial complement activation contributes to vascular complications.

**Verdict**: Run_105 earns execution:
1. FGF-2/angiogenesis = first FGF-2 coverage in framework (genuine new territory)
2. LOCAL (non-hepatic) complement initiation = mechanistically distinct from run_101
3. IL-1β → PTX3 → C1q → C5a = new Loop 2 positive feedback loop
4. T1DM: PTX3 SNP susceptibility (Chiarini 2010) + islet macrophage production
5. Paradoxical complement-regulatory role adds therapeutic nuance

---

## 2. PTX3 Structure and Local Production

### PTX3 vs. Short Pentraxins (CRP/SAP)

Pentraxins divide into two structural families:

| Feature | CRP / SAP (short) | PTX3 (long) |
|---|---|---|
| Subunit structure | 5-mer ring (pentameric) | 8-mer (octameric; disulfide-linked) |
| Primary production site | Hepatocytes (acute phase response) | Macrophages, DCs, mast cells, endothelial, fibroblasts |
| Induction | IL-6/IL-1β → hepatic APR | TNF-α, IL-1β, TLR4/NF-κB in LOCAL tissues |
| C1q affinity | High (CRP) | High (distinct binding site) |
| FGF-2 binding | None | High affinity (Kd ~1 nM) |
| Half-life | ~19h (CRP) | ~12-16h (shorter; faster turnover) |
| Reflects | Systemic inflammation | LOCAL tissue inflammation |

**Implication for framework**: In rosacea skin, serum CRP may be normal (systemic inflammation is not always elevated) while local PTX3 from mast cells and dermal macrophages can be elevated at the tissue level. PTX3 is the innate humoral mediator that bridges tissue-local cell activation to the classical complement pathway.

### PTX3-Producing Cell Types Relevant to Framework

```
Mast cells (dermal/gut) ─ TNF-α autocrine + MRGPRX2/NK1R activation → PTX3 ↑
Dermal macrophages ─────── TLR4/LPS + IL-1β → NF-κB → PTX3 transcription
Endothelial cells ────────── IL-1β + TNF-α → PTX3 (constitutive low-level; induced ×10-100)
DCs (dermal) ──────────────── TLR3/TLR4/TLR7 → PTX3 ↑
Fibroblasts ──────────────── IL-1β + TNF-α → PTX3 (dermal fibroblast production)
```

Islet macrophages in T1DM: activated by dysbiosis-derived LPS (Cani 2008 endotoxemia context, run_096) → TLR4 → NF-κB → PTX3 in islet microenvironment → local classical complement activation → C3a/C5a → islet macrophage NLRP3 priming (Signal 1E amplification locally).

---

## 3. PTX3 → C1q → Classical Complement: Local Arc

### Mechanism

```
PTX3 (from mast cells/macrophages in dermis) →
  Binds C1q (collagen-like domain; distinct site from CRP/IgG) →
  C1q conformational change →
  C1r serine protease activation →
  C1s → cleaves C4 → C4b + C4a
  C1s → cleaves C2 → C2a fragment
  C4b2a = C3 convertase →
  C3 → C3a (anaphylatoxin, mast cell activation) + C3b (opsonin)
  C3b → C5 convertase (C4b2a3b) →
  C5 → C5a (Signal 1E substrate per run_101) + C5b → MAC
```

**Key point**: PTX3 initiates the classical pathway WITHOUT requiring immunoglobulin. It is a PRR-based complement initiator — innate rather than adaptive. This means PTX3-driven complement activation precedes any IgG response and operates from the first encounter with DAMPs/PAMPs.

**Skin-local loop**: UV → keratinocyte damage → DAMP release → macrophage/mast cell TLR4/TLR2 → PTX3 → C1q → C3a/C5a (local) → complement amplification → C5a → Signal 1E (run_101) → NLRP3 priming. This UV→PTX3→complement arc is distinct from the UV→oxidized lipid→alternative pathway arc in run_101 and the UV→IL-33 arc in run_099 — it is a third independent UV-driven complement initiation route.

**UV now triggers 7 independent inflammatory pathways** (updated from run_102's 6):
1. IL-33 → ST2 → mast cell (seconds; run_099)
2. Complement C3a/C5a via alternative pathway from oxidized keratinocytes (minutes; run_101)
3. **PTX3 → C1q → classical complement (minutes; new — run_105)**
4. TSLP → TSLPR → mast cell ST2 priming (hours; run_099)
5. Keratinocyte NLRP3 → IL-1β + IL-18 (hours; run_083)
6. HERV-W → IFN-α → ISGF3 → Signal 1B (hours-days; run_065)
7. MICA/MICB → NKG2D → γδ T/NK → IL-17/IFN-γ (hours; run_102)

### Paradoxical Complement-Regulatory Arm

When PTX3 binds C1q at its globular head domains, it can COMPETE with IgG-C1q binding (Deban 2010 Nat Immunol). This competitive inhibition is relevant when:
- PTX3 levels are very high (acutely, early in innate phase) → blocks IgG-mediated classical complement → paradoxical anti-inflammatory
- CRP > PTX3 (chronic phase, systemic) → cooperative complement activation

**Clinical implication**: PTX3 has a biphasic complement profile — acute innate (pro-complement via direct C1q activation) and late regulatory (competes with IgG at C1q when IgG-dependent phase begins). In early rosacea flares, PTX3-C1q direct activation; in chronic IgG-driven phase (anti-keratinocyte IgG → C1q from run_064/104), PTX3 partially competes. This does not reduce the net complement burden but explains why PTX3 inhibition alone may have limited therapeutic benefit without also targeting IgG production (Tfh/run_104) or complement activation (colchicine/quercetin).

---

## 4. FGF-2 Sequestration — First FGF-2 Axis in Framework

### FGF-2 in Rosacea

FGF-2 (basic FGF, fibroblast growth factor 2) drives:
- Endothelial cell proliferation → new vessel formation (angiogenesis)
- Telangiectasia / persistent erythema in ETR subtype
- Mast cell activation (FGF-2 receptor FGFR1 on mast cells → degranulation; minor)
- Sebocyte lipogenesis (FGFR1 on sebocytes → fatty acid synthesis; Loop 4 input)

**Direct rosacea evidence**: Gomaa 2007 Int J Dermatol: FGF-2 immunostaining significantly elevated in rosacea papules and telangiectasias vs. normal skin. This is the primary driver of the neovascular phenotype in ETR and the persistent background erythema in all subtypes.

### PTX3 → FGF-2 Sequestration

PTX3 contains a unique N-terminal domain (absent in CRP/SAP) that binds FGF-2 with Kd ~1-5 nM (Garlanda 2005 Immunity; Rusnati 1997 Blood):

```
PTX3 (N-terminal domain) + FGF-2 (heparin-binding domain) →
  High-affinity complex →
  FGF-2 unavailable for FGFR1 binding →
  FGF-2-dependent angiogenesis ↓
  Telangiectasia formation ↓
  Mast cell FGFR1 activation ↓ (minor)
  Sebocyte lipogenesis via FGFR1 ↓ (minor)
```

**Framework implication**: PTX3's anti-angiogenic effect is the ONLY counter-regulatory FGF-2 mechanism identified in the framework. It provides a partial brake on the neovascular phenotype independently of VEGF pathways. Elevated PTX3 in active rosacea (from mast cell/macrophage activation) paradoxically limits FGF-2-driven vessel expansion — a negative feedback that partially self-limits ETR progression.

**Therapeutic implication**: Agents that increase PTX3 expression (or that provide PTX3 mimetics targeting FGF-2) could theoretically reduce telangiectasia. However, given PTX3's complement-activating role, PTX3 elevation is a net harm (complement amplification outweighs FGF-2 reduction). The correct inference is: DO NOT TARGET PTX3 upregulation. Instead, address upstream PTX3 inducers (IL-1β, TNF-α, TLR4/LPS) to reduce PTX3 from an elevated state, accepting that FGF-2 will transiently increase but complement activation decreases — the net benefit of reduced complement outweighs the partial loss of FGF-2 inhibition.

---

## 5. IL-1β → PTX3 → C1q: New Loop 2 Positive Feedback Arc

This is the primary new positive feedback identified in run_105:

```
Loop 2 NLRP3 activation →
  IL-1β (canonical NLRP3 product) →
  Endothelial cells + fibroblasts in dermis →
  NF-κB → PTX3 transcription ↑ (2-4h; Doni 2006 Blood) →
  PTX3 binds C1q →
  Classical complement → C3a + C5a →
  C5a → C5aR1 → ERK → AP-1 → NLRP3 Signal 1E (run_101) ↑ →
  NLRP3 → more IL-1β
```

**Positive feedback loop (Loop 2 → PTX3 arc)**:
- Canonical Loop 2: NLRP3 → GSDMD → pyroptosis → IL-1β → NF-κB → more NLRP3 priming (run_083)
- **New extension**: IL-1β → PTX3 → complement C5a → Signal 1E → NLRP3 priming (operates through complement rather than direct NF-κB; not blocked by NF-κB suppression alone)

**Why this matters for non-responders**: If Signal 1E (C5a→AP-1→NLRP3) is the dominant NLRP3 priming pathway in a given patient (AP-1-driven, bypassing all 11 NF-κB suppressors), and Loop 2 is active, the IL-1β→PTX3→C5a arc provides a self-sustaining amplification that CANNOT be interrupted by NF-κB suppression alone. Colchicine (inhibits IL-1β secretion + NLRP3 assembly) + complement inhibition (quercetin/C1q binding; quercetin inhibits C1q-IgG interaction per run_042) would be needed to break this arc.

**TNF-α parallel induction**: TNF-α (mast cell degranulation product; macrophage product) also induces PTX3 in endothelial cells (synergistic with IL-1β; Doni 2006). This means:
- Loop 1: KLK5 → bradykinin/SP → mast cell → TNF-α → PTX3 → complement arc
- Loop 2: NLRP3 → IL-1β → PTX3 → complement arc
Both non-responder loops now have PTX3 as an amplification node.

---

## 6. T1DM: PTX3 SNP Susceptibility and Islet Endothelial Damage

### Genetic Association

Chiarini 2010 Autoimmunity: PTX3 promoter polymorphism rs3816527 is associated with T1DM susceptibility in Italian pediatric cohort. The SNP creates altered NF-κB binding in the PTX3 promoter → higher inducibility → elevated PTX3 in response to TLR4/IL-1β signals. Higher PTX3 → more local complement activation in islets → more Signal 1E priming → NLRP3 → IL-1β → β cell damage.

**This is the first PTX3 susceptibility variant in any autoimmune/inflammatory disease analyzed in the framework** — it directly connects PTX3 to T1DM pathogenesis via the complement→NLRP3 axis.

### Islet PTX3 Production and Microangiopathy

Activated islet macrophages (during insulitis, M1 polarization driven by dysbiosis-LPS/TLR4; runs 009/096) → PTX3 production in islet microenvironment:

```
Gut dysbiosis → LPS/endotoxemia (Cani 2008) →
  Islet macrophage TLR4 → NF-κB → PTX3 ↑ (local islet production) →
  Islet PTX3 → C1q → classical complement activation in islet vasculature →
  C3a → islet macrophage NLRP3 priming →
  C5a → islet endothelial damage (MAC) →
  Microalbuminuria + islet capillaritis
```

**PTX3-microalbuminuria connection** (Chistiakov 2012 Diabetes Res Clin Pract): PTX3 positively correlates with microalbuminuria in T1DM patients — consistent with PTX3-driven local complement activation in glomerular endothelium (same mechanism operating in kidney as in islets/skin). PTX3 is the mechanistic link between systemic endotoxemia (Cani 2008 endotoxemia, run_096) and endothelial damage leading to microalbuminuria.

**T-index implication**: PTX3 could serve as a more sensitive local-inflammation biomarker than CRP for T1DM patients. High PTX3 with normal CRP = active islet/vascular local inflammation without systemic APR. This is clinically relevant for T1DM rosacea patients showing skin flares without elevated serum CRP.

---

## 7. ME/CFS: Endothelial PTX3 and Vascular Activation

ME/CFS vascular hypothesis (Fluge 2016 PLOS ONE; Loebel 2016 Brain Behav Immun):
- Anti-β2-adrenoreceptor (β2-AR) and anti-muscarinic receptor IgG from Tfh-driven GC (run_104)
- These autoantibodies activate endothelial cells and autonomic nerve endings
- **Activated endothelial cells → PTX3 ↑** (endothelial PTX3 production is constitutive at low level; IL-1β/TNF-α increase it ×100)

```
Tfh/GC (run_104) → anti-β2-AR IgG →
  Endothelial β2-AR activation/desensitization →
  Endothelial activation state → IL-6 + IL-1β release →
  Endothelial PTX3 ↑ →
  Local vascular complement activation →
  C5a → MAC → endothelial microinjury →
  Impaired small vessel regulation → orthostatic intolerance
```

NK dysfunction (most replicated ME/CFS finding; Brenu 2011, run_102) → reduced NK cytotoxicity → uncleared virus-infected/stressed cells → ongoing DAMP release → mast cell TLR/MRGPRX2 activation → PTX3 production.

**ME/CFS cross-connection summary**: PTX3 bridges the anti-β2-AR autoantibody mechanism (Tfh/GC, run_104) to local vascular complement activation → endothelial microinjury → autonomic dysregulation. PTX3 is downstream of the autoantibody effect, not a primary driver, but it amplifies vascular damage through complement.

---

## 8. Integration with Existing Framework

### Updated Pathway Summary

```
Gut dysbiosis (M1) → LPS/endotoxemia → macrophage/endothelial TLR4 → NF-κB → PTX3 ↑
NLRP3/Loop 2 → IL-1β → endothelial/fibroblast → PTX3 ↑
Mast cell degranulation (Loops 1/2, all 5 mast cell routes) → TNF-α → PTX3 ↑
UV → keratinocyte DAMP → dermal macrophage TLR → PTX3 ↑
     ↓
PTX3 → C1q → classical complement → C3a + C5a
     ↓                    ↓
  (C3a → mast cell)   (C5a → Signal 1E → NLRP3 priming)
     ↓
FGF-2 sequestration (anti-angiogenic; partial counter-regulation)
P-selectin binding (neutrophil extravasation modulation)
```

### Quercetin-PTX3 Interaction

Quercetin → C1q/IgG binding inhibition (run_042/064: mechanism 2). This extends to PTX3-C1q activation: quercetin's C1q-binding inhibition would reduce PTX3-initiated classical complement as well, making quercetin's complement mechanism broader than previously described (inhibits BOTH IgG-C1q AND PTX3-C1q initiation). This is a clarification/extension of the existing mechanism, not a new quercetin mechanism number.

### Protocol Adjustment: PTX3 as Node B Extension

Node B currently monitors hsCRP + IL-6 + waist. PTX3 reflects LOCAL tissue inflammation more accurately than CRP in rosacea patients with normal serum CRP but active skin disease. For T1DM rosacea patients:
- If hsCRP normal but persistent skin flares + microalbuminuria rising → consider serum PTX3
- PTX3 >3.4 ng/mL (upper limit of normal in most studies) alongside active rosacea suggests complement-driven loop is active
- Intervention: same Loop 2/complement management — colchicine, quercetin, gut barrier (Node C), NLRP3 management

No new agents required — existing protocol already targets PTX3 upstream inducers (IL-1β via colchicine/NLRP3 management; TLR4/LPS via gut barrier/Node C; TNF-α via NF-κB suppression cascade).

---

## 9. Summary of New Mechanisms

1. **PTX3 → C1q → classical complement (LOCAL)**: tissue-resident mast cells/macrophages produce PTX3 → initiate classical complement locally without IgG or systemic CRP [new LOCAL complement initiation route; extends run_101]
2. **PTX3 → FGF-2 sequestration → angiogenesis ↓**: N-terminal domain sequesters FGF-2 → partial anti-angiogenic brake on ETR telangiectasia [FIRST FGF-2 axis in framework; counter-regulatory]
3. **IL-1β → PTX3 → C5a → Signal 1E → NLRP3**: new Loop 2 positive feedback arc via complement (not NF-κB; not blocked by 11 NF-κB suppressors) [new amplification loop]
4. **TNF-α → PTX3**: mast cell TNF-α (all 5 mast cell routes) → endothelial PTX3 → complement [Loop 1/2 → PTX3 arc]
5. **UV → PTX3 → classical complement**: UV → DAMP → macrophage TLR → PTX3 = 3rd independent UV→complement mechanism [adds to run_101's 2 UV complement routes; total UV paths now 7]
6. **PTX3 SNP rs3816527 → T1DM susceptibility**: altered NF-κB binding → higher PTX3 inducibility → more islet complement → NLRP3 priming [genetic mechanism; Chiarini 2010]
7. **Islet macrophage PTX3 → microalbuminuria**: endotoxemia-driven islet/glomerular PTX3 → local complement → vascular damage → microalbuminuria [mechanistic link Cani 2008 → Chistiakov 2012]
8. **Paradoxical PTX3 complement regulation**: PTX3 competes with IgG at C1q → net anti-complement at very high PTX3 — NOT a therapeutic rationale for PTX3 upregulation (complement activation cost > FGF-2 inhibition benefit) [Deban 2010]

**UV paths count update: 7 independent UV-triggered inflammatory pathways** (was 6 after run_102).

---

## 10. Evidence

- Bottazzi 1997 Immunity — PTX3 first characterization; local mast cell/macrophage production
- Garlanda 2005 Immunity — PTX3 FGF-2 binding; anti-angiogenic; complement activation
- Moalli 2011 J Exp Med — PTX3 C1q binding mechanism; classical complement initiation
- Deban 2010 Nat Immunol — PTX3 competes with CRP at C1q; complement regulatory role
- Doni 2006 Blood — IL-1β + TNF-α → PTX3 transcription in endothelial cells and fibroblasts
- Chiarini 2010 Autoimmunity — PTX3 promoter SNP rs3816527 associated with T1DM susceptibility
- Chistiakov 2012 Diabetes Res Clin Pract — PTX3 elevated in T1DM; correlates with microalbuminuria
- Gomaa 2007 Int J Dermatol — FGF-2 elevated in rosacea ETR/PPR skin lesions
- Chiller 2002 Arch Dermatol — C3d complement deposits in rosacea skin (consistent with local PTX3/C1q)
- Rusnati 1997 Blood — PTX3 N-terminal domain FGF-2 binding affinity characterization
