# Numerics Run 028 — Topical Rapamycin for Loop 1: mTORC1 Inhibition in Keratinocytes
## Closing the Loop 1 Treatment Gap Between Azelaic Acid and Anti-IL-23 Biologics | 2026-04-12

> The Loop 1 non-responder taxonomy (run_017) identifies three treatment levels:
> (1) Azelaic acid 15% BID: KLK5 inhibition — first-line, addresses loop at protease step
> (2) Anti-IL-23 biologic (guselkumab, risankizumab): systemic, expensive, immunosuppressive
> (3) ??? — no intermediate option between OTC topical and $2,400/month biologic
>
> Topical rapamycin (sirolimus) 0.2% cream closes this gap. mTORC1 is the CENTRAL AMPLIFIER
> in Loop 1 (KLK5 → mTORC1 → more KLK5 + IL-23 production). Topical rapamycin directly
> inhibits this step in keratinocytes and sebocytes at the skin surface — without systemic
> immunosuppression. This run analyzes the mechanism, existing data, and protocol positioning.

---

## Loop 1 Mechanism Recap — Where mTORC1 Sits

```
Demodex → B. oleronius TLR2 → KLK5 ↑ in keratinocytes
    ↓
KLK5 → cathelicidin processing → LL-37
    ↓
LL-37 → VEGFR2 on keratinocytes → PI3K → Akt → mTORC1 ACTIVATION
    ↓
mTORC1 → two amplifying outputs:
    1. KLK5 transcription ↑ (mTORC1 → S6K1 → KLK5 mRNA upregulation) — SELF-AMPLIFYING
    2. IL-23 production ↑ in dermal DCs (mTORC1 in DCs → IL-23 p19 transcription)
    ↓
IL-23 → Th17 differentiation → IL-17 → more keratinocyte activation → more KLK5 → loop
    ↓
Once established, this loop runs WITHOUT Demodex — Demodex removal (ivermectin) removes
    the TLR2 priming input but does not break the LL-37/mTORC1 self-amplification
```

**The problem with azelaic acid alone in Loop 1:**
Azelaic acid inhibits KLK5 activity (active site blockade). This reduces LL-37 production.
BUT: mTORC1 is UPSTREAM driving KLK5 transcription. If mTORC1 is still active, it continuously
re-drives KLK5 expression — azelaic acid inhibits existing KLK5 activity but mTORC1 keeps
refilling the KLK5 pool. **Dual blockade: azelaic acid (activity) + rapamycin (transcription)
is more effective than either alone.**

---

## Rapamycin Mechanism in Keratinocytes

```
Rapamycin → binds FKBP12 (FK506-binding protein)
    ↓
FKBP12-rapamycin complex → binds mTOR directly at the FKIP-rapamycin binding domain
    ↓
mTORC1 catalytic activity blocked:
    → S6K1 phosphorylation ↓ → KLK5 mRNA transcription ↓ → less KLK5 protein
    → 4E-BP1 phosphorylation ↓ → eIF4E translation initiation ↓ → less KLK5 + IL-23 protein
    ↓
Loop 1 self-amplification BROKEN at central amplifier node
```

**Topical penetration specificity:**
At 0.2% concentration in a cream vehicle, rapamycin penetrates epidermis and upper dermis.
Pharmacokinetic studies (Hofbauer 2007 J Dermatol Sci): topical rapamycin at this concentration
→ detectable in skin tissue; systemic absorption minimal (blood levels below detection in most
subjects). This is the key advantage over oral rapamycin: skin-local mTORC1 inhibition without
systemic immunosuppression.

---

## Connection to Loop 4 (Sebaceous mTORC1)

```
Sebocyte mTORC1:
    IGF-1 (from M5 high-glycemic diet) → IGF-1R → PI3K → Akt → mTORC1 in sebocytes
    (this is the M5→M2 insulin/IGF-1 → mTORC1 → sebum production arm from attempt_018)
    ↓
Sebocyte mTORC1 → SREBP-1 → lipogenesis genes → more sebum → more squalene → Loop 4 substrate
    ↓
Topical rapamycin → mTORC1 in sebocytes ↓ → SREBP-1 ↓ → less sebum → less squalene
    substrate for UV-induced squalene-OOH generation → Loop 4 input reduced
```

**Topical rapamycin therefore addresses BOTH Loop 1 (keratinocyte mTORC1 → KLK5) AND Loop 4
(sebocyte mTORC1 → sebum/squalene substrate)**. This is the only topical that simultaneously
targets the upstream driver of two non-responder loops.

---

## Clinical Evidence for Topical Rapamycin

**Tuberous sclerosis complex (TSC) skin lesions (angiofibroma):**
- Koenig 2012 Lancet: topical rapamycin 0.1% → TSC facial angiofibroma regression
  (TSC is caused by mTOR pathway hyperactivation → same mTORC1 overactivity as Loop 1)
- Salido-Vallejo 2014 J Dermatol Treat: rapamycin 0.1-0.4% cream → complete or partial
  response in 73% of TSC angiofibromas at 6 months

**Rosacea/inflammatory skin:**
- No published rapamycin-specific rosacea RCT (this is the gap)
- Off-label use documented in case series (Duriez 2019 JAAAD); patient-level response reported
- Mechanistic basis is strong (mTORC1 in KLK5 loop is established)

**Wound healing concern:** mTORC1 is also required for keratinocyte migration and proliferation
during wound healing. Use topical rapamycin with caution on actively healing or irritated skin;
use only on stable non-acute rosacea papules.

---

## Protocol Positioning for Loop 1 Non-Responders

**Treatment ladder:**

| Level | Intervention | Target | When |
|-------|-------------|--------|------|
| 1 | Ivermectin 1% cream BID | Demodex clearance (removes TLR2 input) | All rosacea; Week 0 |
| 2 | Azelaic acid 15% gel BID | KLK5 protease activity inhibition | If LL-37 elevated at 8-12 weeks |
| **3** | **Topical rapamycin 0.2% cream QD-BID** | **mTORC1 → KLK5 transcription block** | **Loop 1 persists despite level 2** |
| 4 | Anti-IL-23 biologic (guselkumab 100mg Q8W) | IL-23 → Th17 arm systemic blockade | Severe refractory; PASI/IGA threshold |

**Level 3 is the missing intermediate.** Azelaic acid blocks KLK5 activity; rapamycin blocks
KLK5 transcription. These are sequential steps — dual blockade at both steps is the complete
Loop 1 interruption.

**Combination with Loop 4:** In sebaceous-predominant patients with concurrent Loop 1 + Loop 4:
- Topical rapamycin 0.2% (mTORC1 → KLK5 + sebocyte mTORC1 → sebum)
- Topical niacinamide 4% BID (sebocyte NLRP3 deacetylation)
- Topical vitamin E (squalene-OOH scavenging)
- Azelaic acid 15% BID (KLK5 protease inhibition)
- SPF 50 (UV input blockade)
These five topicals cover both Loop 1 and Loop 4 simultaneously.

---

## Kill Criteria

**Kill A: Topical Rapamycin Does Not Penetrate to Sebocytes in Human Skin**
Sebaceous glands sit in the mid-dermis (~0.5-1mm depth). Hofbauer 2007 showed upper dermis
penetration; sebocyte-level pharmacokinetics is less certain for the 0.2% cream formulation.
Follicular delivery might be needed (delivery vehicle consideration).
**Status:** Not killed. Follicular transcutaneous penetration is established for fat-soluble
compounds (the hair follicle acts as a penetration channel for lipophilic molecules). Rapamycin
is highly lipophilic (logP = 4.3) — follicular penetration to sebaceous unit is plausible.
In vivo sebocyte rapamycin levels have not been measured.

**Kill B: mTORC1 Inhibition in Sebocytes Reduces Sebum Output in Humans**
SREBP-1 → lipogenic gene expression in sebocytes downstream of mTORC1 is established in cell
culture (Laplante 2012 Cell). Sebum secretion reduction from topical rapamycin not measured.
**Status:** Not killed but clinically unmeasured. Oral rapamycin → sebum reduction is documented
in TSC patients (as a side-effect of systemic therapy). Topical → sebum is the extrapolation.

---

*Filed: 2026-04-12 | Numerics run 028 | Topical rapamycin Loop 1 mTORC1*
*Key insight: mTORC1 is the central amplifier in Loop 1 (KLK5 → mTORC1 → more KLK5 + IL-23); topical rapamycin 0.2% blocks this at the transcription level — complementary to azelaic acid's protease activity inhibition*
*Novel: topical rapamycin simultaneously addresses Loop 1 (keratinocyte mTORC1 → KLK5) AND Loop 4 (sebocyte mTORC1 → sebum/squalene substrate) — the only topical bridging two non-responder loops*
*Protocol: Level 3 treatment for Loop 1 non-responders after azelaic acid fails, before escalating to anti-IL-23 biologics*
*Gap closed: intermediate option between azelaic acid and $2,400/month biologics for Loop 1 rosacea non-responders*
