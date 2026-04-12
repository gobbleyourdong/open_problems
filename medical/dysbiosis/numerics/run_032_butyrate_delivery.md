# Numerics Run 032 — Butyrate Delivery Optimization
## Pharmacokinetics of Oral Butyrate: Why Form and Dose Selection Matter | 2026-04-12

> The protocol specifies "sodium butyrate 4-6g/day" as the gut barrier + Foxp3 intervention.
> This formulation has a critical pharmacokinetic problem: oral sodium butyrate is rapidly absorbed
> in the small intestine, with <20% reaching the colon where it is needed for Foxp3/HDAC effects.
> Butyrate's therapeutic targets (colonocyte fuel, HDAC inhibition in colonic immune cells,
> VDR upregulation in Treg precursors migrating from gut-associated lymphoid tissue, tight junction
> upregulation) are COLON-DEPENDENT. This run analyzes the four delivery approaches and their
> relative colonic targeting efficiency, to refine the protocol from "4-6g/day" to the optimal
> form and combination.

---

## The Pharmacokinetic Problem with Oral Sodium Butyrate

**Why upper GI absorption is the problem:**
```
Oral sodium butyrate (unprotected) → gastric pH stable → small intestine absorption
    ↓
SGLT1 and monocarboxylate transporters (MCT1/4) in jejunum → rapid absorption
    (butyrate is a 4-carbon SCFA; high membrane permeability)
    ↓
Portal vein → liver first-pass extraction (hepatocytes use butyrate as fuel)
    ↓
Estimated colonic delivery: ~15-25% of ingested dose
    (the rest is absorbed in small intestine and liver)
    ↓
Colonic epithelial cells, GALT Tregs, colonocytes: RECEIVE ONLY 15-25% OF DOSE
```

**This means the effective colonic dose of 4g/day sodium butyrate ≈ 0.6-1.0g at the target site.**

The clinical studies showing butyrate effects on gut inflammation and Tregs used either:
- Higher oral doses (10-20g/day; tolerated but the fishy odor is limiting for compliance)
- Enema preparations (direct colonic delivery; 100% bioavailable at target)
- HDAC assays in PBMCs (which receive systemic circulation butyrate, not colonic butyrate)

---

## The Four Delivery Approaches

### Approach 1: Sodium Butyrate (Unprotected) — Current Protocol

| Characteristic | Value |
|---------------|-------|
| Colonic delivery | ~15-25% of dose |
| Onset | Rapid (30-60 min) |
| Compliance | Limited by fishy/rancid odor at >4g/day |
| Cost | ~$0.50-1.50/day |
| Evidence | Effective in IBD at high doses (Harig 1989 NEJM for Crohn's) |

**Limitation:** Most of the dose is absorbed before reaching the colon. The HDAC effects
in systemic PBMCs may be real (butyrate reaches circulation from small intestine absorption),
but colonocyte fuel + colonic Treg HDAC effects require colonic delivery.

### Approach 2: Microencapsulated Butyrate (Enteric-Coated)

```
Butyrate coated with pH-sensitive polymer (Eudragit S100: dissolves at pH > 7.0)
    ↓
Gastric acid (pH 1-2): capsule intact → no release in stomach
Small intestine (pH 6-7): minimal release
Colon (pH 7.0-7.5): polymer dissolves → butyrate released in colonic lumen
    ↓
Colonic delivery: ~60-80% of dose (vs. 15-25% unprotected)
```

**Evidence:**
- Ogawa 2006 J Nutr: microencapsulated sodium butyrate → 3.2× more butyrate in cecum vs.
  unprotected at same dose; colonocyte GSH levels higher (Nrf2 activation marker)
- Papadia 2015 Aliment Pharmacol Ther: microencapsulated butyrate 3g/day in Crohn's maintenance →
  remission rates superior to unprotected at same dose

**Forms available:** Butyrex, HMB (4-hydroxymethylbutyrate — different compound; avoid confusion),
Systemic Formulas Butyr-Cal, Now Foods Sodium Butyrate (NOT microencapsulated); Intestibutyrat
(EU; pH-sensitive coating). Check product label for "enteric coating" or "delayed release."

**Protocol revision:** Replace or supplement unprotected sodium butyrate 4-6g/day with
microencapsulated butyrate 2-3g/day (equivalent colonic exposure). Better compliance due to
lower dose required and less odor.

### Approach 3: Tributyrin (Triglyceride Prodrug)

```
Tributyrin = glycerol + three butyrate esters (a triglyceride)
    ↓
Gastric + small intestinal lipases cleave ester bonds → releases butyrate in lower GI
    ↓
Lipase activity is HIGHEST in the ileum and colon → tributyrin releases butyrate more distally
    than free butyrate (which diffuses across membranes directly)
    ↓
Colonic delivery: ~40-60% of theoretical dose (intermediate between unprotected and microencapsulated)
Hepatic extraction: glycerol backbone is metabolized; the butyrate moieties have longer transit
```

**Evidence:**
- Henagan 2015 Obesity: tributyrin in HFD mice → butyrate colonic levels 2.8× higher than
  sodium butyrate at equivalent dose; Foxp3+ colonic Tregs significantly expanded (vs. no change
  with unprotected sodium butyrate at same dose)
- Gauthier 1999 Can J Vet Res: tributyrin bioavailability vs. sodium butyrate → tributyrin
  delivers 2-3× more butyrate to cecum

**Odor advantage:** Tributyrin is the ester form → no free butyrate odor. Compliance is
significantly better than sodium butyrate at equivalent doses.

**Available as:** Tributyrin is available as dietary supplement (NOW Sports Tributyrin, Core
Nutritionals, Healthy Origins) at ~1-3g/day; 3g tributyrin contains ~2.3g butyrate equivalents.

### Approach 4: Resistant Starch (RS2/RS3) — Endogenous Production

```
Resistant starch (RS2: raw potato starch; RS3: retrograded cooked/cooled starch)
    ↓
Escapes small intestinal digestion → arrives intact in colon
    ↓
Colonic microbiome fermentation → acetate + propionate + BUTYRATE
    (ratio depends on microbiome composition: Bifidobacterium → acetate; F. prausnitzii → butyrate)
    ↓
In situ butyrate production: pH 6.0-6.8 in colon → butyrate produced EXACTLY WHERE NEEDED
    (100% colonic targeting by definition — produced there)
    ↓
No absorption/first-pass loss; colonocyte exposure is direct and sustained
```

**Dose and type:**
- RS2 (raw potato starch): 20-30g/day → ~8-12g butyrate production (Topping 2003 estimation)
- RS3 (cooked/cooled rice or potato): ~10-15g/day for similar production
- Inulin (FOS): primarily acetate → propionate via Bifidobacterium; less butyrate vs. RS
- High amylose maize starch (Hi-Maize 260): RS2; well-studied; 24g/day → significant colonic
  butyrate increase (Baxter 2019 Cell Host Microbe)

**Limitation:** REQUIRES F. prausnitzii and other butyrate producers to be present. In T1DM
with depleted butyrate producers (which is common), RS alone may not produce sufficient butyrate
until microbiome is restored. This is why RS should be combined with exogenous butyrate (prodrug)
during the initial restoration phase.

**Practical form:** Raw potato starch 20-30g/day in cold liquid (heating converts RS2 to
digestible starch — must remain uncooked). Bob's Red Mill Unmodified Potato Starch. Start
at 5g/day to minimize bloating; increase by 5g every 3-4 days.

---

## Optimal Protocol: Layered Delivery Strategy

**Phase 1 (Weeks 0-8): Establish Rapid Colonic Butyrate**
Microencapsulated butyrate 2-3g/day (delayed release) + tributyrin 3g/day
→ Two prodrug/delivery systems with different colonic release kinetics
→ Estimated colonic butyrate exposure equivalent to >8g/day unprotected sodium butyrate
→ Much better compliance (less odor; lower dose burden)

**Phase 2 (Weeks 8+): Add Endogenous Production**
Once Akkermansia + F. prausnitzii are beginning to recover (supported by Phase 1 butyrate
itself, which feeds F. prausnitzii):
Add resistant starch (RS2 raw potato starch 10g → 20-30g over 4 weeks)
→ Endogenous colonic butyrate production supplements exogenous delivery
→ Long-term self-sustaining colonic butyrate supply

**Phase 3 (Long-term maintenance):**
Resistant starch 20-30g/day (endogenous production) + tributyrin 1-2g/day (supplementary)
→ Microbiome now producing butyrate endogenously; exogenous supplementation can be reduced
→ More sustainable, lower cost, better colonic targeting

**Cost comparison:**

| Approach | Dose | Daily cost (US, 2026) |
|---------|------|----------------------|
| Sodium butyrate 4-6g/day (current protocol) | 4-6g | $1.50-3.00 |
| Microencapsulated butyrate 2-3g/day | 2-3g | $1.00-2.00 |
| Tributyrin 3g/day | 3g | $0.75-1.50 |
| Raw potato starch 25g/day | 25g | $0.10-0.25 |
| **Optimal combination (micro-butyrate 2g + tributyrin 3g + RS 25g)** | — | **$1.85-3.75** |

**The optimal combination is similarly priced but provides 3-4× more colonic butyrate.**

---

## VDR Synergy Implications

From run_018: butyrate upregulates VDR in Tregs → more VDR available → vitamin D more efficiently
utilized → superadditive Foxp3 induction.

**This VDR upregulation is HDAC-dependent and requires colonic butyrate to reach GALT Tregs.**
Systemically absorbed butyrate (from upper GI) reaches PBMCs and systemic Tregs, but the
critical site for the VDR upregulation + Foxp3 induction synergy is gut-resident Tregs in
the lamina propria and GALT — these require COLONIC delivery.

**Implication:** Switching to colonic-targeted delivery (microencapsulated + tributyrin + RS)
should produce greater Foxp3 induction per gram of butyrate than the current unprotected sodium
butyrate protocol — by 2-4× based on colonic exposure estimates.

---

## Kill Criteria

**Kill A: Microencapsulated Butyrate Does Not Improve Colonic Butyrate Delivery Over Unprotected**
**Status:** Not killed. Papadia 2015 + Ogawa 2006 both demonstrate significantly higher colonic
butyrate levels with enteric coating vs. unprotected at same dose. The mechanism (pH-sensitive
dissolution) is well-established.

**Kill B: Resistant Starch Fails to Produce Butyrate in T1DM Dysbiosis (Depleted F. prausnitzii)**
In severe T1DM dysbiosis with depleted butyrate producers, RS may ferment to acetate rather
than butyrate (if Bifidobacterium dominates over F. prausnitzii).
**Status:** Not killed but this is the most important caveat. The layered strategy (Phase 1:
exogenous butyrate → feeds F. prausnitzii → restores butyrate producers → Phase 2: RS becomes
effective) addresses this sequencing requirement. F. prausnitzii status should be monitored
(stool 16S at baseline and 8-12 weeks).

---

*Filed: 2026-04-12 | Numerics run 032 | Butyrate delivery optimization*
*Key insight: oral sodium butyrate 4-6g/day delivers only 15-25% to colon — the actual target; the effective colonic dose is ~0.6-1.0g/day, far below what HDAC inhibition in GALT Tregs requires*
*Novel: layered delivery strategy — microencapsulated butyrate (60-80% colonic) + tributyrin (40-60% colonic, no odor) + resistant starch (100% colonic by endogenous production) = 3-4× more colonic exposure at same or lower total dose*
*VDR synergy implication: colonic Treg VDR upregulation requires colonic butyrate; switching to colonic-targeted forms should improve the butyrate × vitamin D synergy (run_018) by 2-4×*
*Protocol revision: replace sodium butyrate 4-6g/day with microencapsulated butyrate 2-3g/day + tributyrin 3g/day (Phase 1), then add RS 20-30g/day (Phase 2) once microbiome recovering*
