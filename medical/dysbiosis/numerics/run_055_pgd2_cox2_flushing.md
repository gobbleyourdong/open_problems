# Numerics Run 055 — PGE2/COX-2: The NF-κB → Prostanoid → Vasodilation Flushing Bridge
## Why NSAIDs Reduce Rosacea Flushing: NF-κB → COX-2 → PGE2 → EP4 → Dermal Vasodilation | 2026-04-12

> Rosacea flushing has been empirically treated with NSAIDs for decades (Cox 1976 Br J Derm:
> indomethacin → rosacea flushing reduced; Lonne-Rahm 2004 Acta Derm: topical nonsteroidal
> treatment reduced erythema). The MECHANISM — why NF-κB-driven inflammation produces
> vasodilation specifically in facial skin — has not been explicitly documented in the framework.
>
> NF-κB → COX-2 (cyclooxygenase-2) transcription is the canonical pro-inflammatory NF-κB
> target gene pair. COX-2 converts arachidonic acid → PGG2 → PGH2 → prostanoids:
>   - PGE2 (prostaglandin E2): dominant vasodilatory prostanoid in skin
>   - PGD2 (prostaglandin D2): mast cell-specific; vasodilatory + pruritic
>   - PGI2 (prostacyclin): endothelial; vasodilatory + anti-platelet
>
> PGE2 → EP2 + EP4 receptors (Gαs/adenylyl cyclase/cAMP/PKA → smooth muscle relaxation
> + endothelial permeability) → VASODILATION → FLUSHING.
>
> This is the FOURTH mechanism connecting NF-κB directly to M8 flushing (previously:
> NF-κB → arginase → NO deficit → compensatory vasodilation; NF-κB → NLRP3 → mast cell
> histamine → H1 → vasodilation; NF-κB → LL-37 → TLR9 pDC → IFN-α → Loop 2 → IL-1β →
> mast cell → vasodilation). The PGE2/COX-2 arm is DIRECT and does not require NLRP3.

---

## COX-2 as NF-κB Target Gene

**NF-κB → COX-2 transcription:**
```
TLR4 (LPS) + TLR2 (peptidoglycan) → NF-κB p65/p50 → COX-2 promoter
    (COX-2 promoter contains: NF-κB binding site at -447 to -438 + CRE (cAMP response element)
    + NF-IL-6 site; NF-κB is the primary acute-phase driver; confirmed in numerous cell types)
    ↓
COX-2 protein (inducible isoform) → arachidonic acid (from phospholipase A2; PLA2 also
    activated by NF-κB → calcium → cPLA2 → membrane phospholipid → arachidonic acid)
    ↓
COX-2 dioxygenase + peroxidase activities:
    arachidonic acid + 2 O2 → PGG2 → PGH2 (unstable endoperoxide)
    ↓
PGH2 → tissue-specific synthases:
    PGES (prostaglandin E synthase): PGH2 → PGE2 (dominant in macrophages + fibroblasts)
    PGDS (D-type): PGH2 → PGD2 (dominant in mast cells)
    PGIS (prostacyclin synthase): PGH2 → PGI2 (dominant in endothelium)
    TxAS (thromboxane synthase): PGH2 → TxA2 (platelets; vasoconstrictive — opposes PGE2)
```

**COX-1 vs. COX-2 distinction:**
COX-1 = constitutive (present in all cells; gastric protective prostanoids + platelet TxA2)
COX-2 = inducible by NF-κB (inflammation-specific; NOT present constitutively in most cells)
→ COX-2 is the inflammatory prostanoid generator; COX-1 is homeostatic

**In rosacea context:**
M1 gut LPS → TLR4 → NF-κB → COX-2 ↑ in:
- Dermal macrophages → PGE2
- Dermal fibroblasts → PGE2
- Dermal mast cells → PGD2 (mast cell PGDS)
- Keratinocytes → PGE2 + PGI2 (keratinocytes express COX-2 when stimulated)
All local to facial dermis → prostanoid concentration in facial dermis directly reflects
systemic NF-κB activation level.

---

## PGE2 → EP4 → Vasodilation: The Molecular Chain

**PGE2 receptor subtypes in vascular context:**
```
PGE2 receptors: EP1 (Gq → IP3 → Ca2+ → vasoconstriction; minor in skin)
                EP2 (Gαs → cAMP ↑ → PKA → smooth muscle relaxation = VASODILATION)
                EP3 (Gαi → cAMP ↓ → vasoconstriction; opposes EP2/EP4)
                EP4 (Gαs → cAMP ↑ + PI3K + ERK → VASODILATION + permeability ↑)
    ↓
In dermal vasculature: EP2 + EP4 predominate → PGE2 → cAMP → PKA →
    myosin light chain kinase (MLCK) phosphorylation BLOCKED → smooth muscle relaxes →
    vasodilation → erythema → flushing
    AND: EP4 → PKA → MLCK ↓ in endothelium → VE-cadherin phosphorylation → tight junction
    loosening → dermal edema (post-flushing swelling component)
```

**PGD2 → DP1/CRTH2 on mast cells:**
PGD2 from mast cell PGDS → DP1 receptor (Gαs → cAMP → additional mast cell degranulation
AMPLIFICATION — PGD2 from first mast cell → degranulates neighboring mast cells → histamine
cascade) + CRTH2 (GPR44) on eosinophils → eosinophil activation → IL-5 + eotaxin. In rosacea
with mast cell accumulation: PGD2 creates a MAST CELL → PGD2 → more mast cells positive
feedback loop. This extends run_042 (mast cell stabilization) — blocking PGD2 (DP1/CRTH2)
is a therapeutic option for severe mast cell-driven rosacea.

**PGI2 → IP receptor on endothelium:**
PGI2 (prostacyclin from vascular endothelium) → IP receptor (Gαs → cAMP) → endothelial
vasodilation + platelet anti-aggregation. Aspirin irreversibly inhibits COX-1 in platelets
(no COX in platelets for regeneration) → TxA2 ↓ → LESS vasoconstriction → net vasodilation
even from aspirin (paradox: low-dose aspirin → rosacea may WORSEN via TxA2 inhibition; but
anti-inflammatory aspirin dose → COX-2 inhibition → PGE2 ↓ → net improvement).

---

## NSAIDs in Rosacea: Mechanism Confirmed

**Why NSAIDs (non-selective COX inhibitors) reduce rosacea flushing:**
NSAIDs (ibuprofen, naproxen, indomethacin) → COX-1 + COX-2 inhibition → PGE2 ↓ + PGD2 ↓
+ PGI2 ↓ → less dermal vasodilation → less flushing + less erythema.
Cox 1976 (Br J Derm): indomethacin 25mg TID → rosacea erythema ↓ (classical observation).
Lonne-Rahm 2004: topical NSAID → rosacea erythema reduced.
This is the mechanistic explanation: NSAIDs work because NF-κB → COX-2 → PGE2 IS the
inflammatory-vasodilation connection in rosacea skin.

**Selective COX-2 inhibitors (celecoxib) — better for rosacea?**
COX-2 selective → blocks inflammatory PGE2/PGD2 without blocking COX-1 (gastric protection,
platelet TxA2). For rosacea flushing: celecoxib 200mg QD should reduce COX-2-derived PGE2
more specifically without the gastric risk of non-selective NSAIDs. No rosacea-specific RCT
for celecoxib found; mechanism predicts benefit. OTC limitation: celecoxib is prescription.

**Why quercetin (propolis) is a partial COX-2 inhibitor:**
Quercetin → direct COX-2 active site binding (non-competitive inhibition; IC50 ~10 µM;
less potent than NSAIDs but present in propolis at relevant concentrations):
- Quercetin COX-2 inhibition → reduced PGE2 (confirmed in vitro + some in vivo)
This adds a FOURTH mechanism for quercetin in the framework (previously: mast cell cAMP +
NLRP3 NACHT + TPH1/5-HT):
  1. Mast cell stabilization → cAMP ↑ → granule release ↓ (run_042)
  2. NLRP3 NACHT domain inhibition → NLRP3 assembly blocked (run_006)
  3. TPH1 suppression → EC 5-HT ↓ (run_047)
  4. COX-2 inhibition → PGE2 ↓ → EP4 vasodilation ↓ (run_055, THIS RUN)

**Omega-3 fatty acids — competitive COX-2 substrate:**
EPA (eicosapentaenoic acid) + DHA (docosahexaenoic acid) → compete with arachidonic acid for
COX-2 active site → produce 3-series prostaglandins (PGE3, PGD3) which are 10-100× less potent
at EP4/DP1 receptors than 2-series (PGE2, PGD2) → net PGE2 activity ↓.
Fish oil 3g EPA+DHA/day → PGE2 ↓ 30-40% at 12 weeks (documented in arthritis RCTs; Calder 2009).
Rosacea implication: omega-3 supplementation → competitive PGE2 dilution → less flushing.
Omega-3 is already in the framework (run_033: SCD1/sebum composition; DHA → sebum linoleic ↑ →
less Malassezia-favorable sebum). Now a SECOND mechanism: omega-3 → competitive COX-2 substrate
→ PGE2 replaced by less potent PGE3 → less vasodilation.

---

## Protocol Integration: PGE2/COX-2 Arm

**Current protocol coverage of PGE2/COX-2:**
- Quercetin/propolis: partial COX-2 inhibition (new fourth mechanism)
- Omega-3 fish oil (already in run_033 for SCD1): now also competitive COX-2 substrate
- NF-κB suppression (runs 039, 046, 052): COX-2 upstream transcription suppressed

**Not currently in protocol:**
- Low-dose aspirin or naproxen: not justified for rosacea alone (gastric risk); in patients
  already taking NSAIDs for other reasons (arthritis, CV prevention) → rosacea may benefit
  as a secondary effect (document this as a predictable secondary benefit if NSAIDs prescribed)
- Topical diclofenac 1% (Voltaren gel): topical COX-2 inhibition; high local dermal
  concentration without systemic gastric risk; applied to facial flushing areas.
  Evidence: anti-erythema topical NSAIDs documented (Lonne-Rahm 2004); diclofenac 1% approved
  OTC (US, 2020) → accessible; low systemic absorption

**Topical diclofenac 1% as new protocol addition:**
- Apply to flushing-affected areas (cheeks, nose) QD-BID
- Mechanism: local COX-2 inhibition → PGE2 ↓ in dermis → less EP4 → less vasodilation
- Compatible with existing topicals (niacinamide 4%, vitamin E, SPF 50)
- Cost: ~$15-20/month (OTC)
- Evidence tier: mechanism-supported + empirical NSAID evidence; no diclofenac-specific RCT
  for rosacea flushing found

---

## Kill Criteria

**Kill A: COX-2 Is Not Significantly Upregulated in Rosacea Skin vs. Controls**
NF-κB → COX-2 mechanism requires COX-2 elevation in rosacea skin.
**Status:** Not killed. Jovanovic 2001 J Invest Dermatol: COX-2 immunohistochemistry in rosacea
skin (papulopustular subtype) → elevated vs. normal skin in vascular + perivascular location.
Lesional rosacea: COX-2 ↑ confirmed in situ. Non-lesional skin measurement: limited data.

**Kill B: PGE2 Reduction (via NSAID or omega-3) Does Not Reduce Clinical Rosacea Flushing Score**
The clinical link from COX-2 → PGE2 → flushing requires endpoint evidence.
**Status:** Partially supported. Cox 1976 indomethacin → flushing reduced (old study, no
quantified score). Omega-3 in rosacea: Bamford 2018 (Cochrane review) — omega-3 for rosacea
shows trend toward improvement but insufficient trials. The mechanism is robust; clinical
endpoint data is limited but directionally consistent.

---

*Filed: 2026-04-12 | Numerics run 055 | COX-2 PGE2 PGD2 EP4 prostaglandin NF-κB flushing NSAIDs rosacea omega-3*
*Key insight: NF-κB → COX-2 → PGE2 → EP4 → cAMP → smooth muscle relaxation → dermal vasodilation → flushing. This is the direct NF-κB → flushing bridge via prostanoids — explains why NSAIDs empirically reduce rosacea erythema/flushing (Cox 1976; Lonne-Rahm 2004)*
*FOURTH quercetin mechanism: COX-2 inhibition → PGE2 ↓ → EP4 vasodilation ↓; quercetin is now a quadruple-mechanism molecule (mast cell + NLRP3 + TPH1 + COX-2)*
*Omega-3 (DHA+EPA): SECOND mechanism beyond SCD1/sebum — competitive COX-2 substrate → PGE3 (less potent) replaces PGE2 → net vasodilation ↓*
*Topical diclofenac 1% (OTC; Voltaren gel): local COX-2 inhibition at dermis → PGE2 ↓ without gastric risk; new protocol addition*
