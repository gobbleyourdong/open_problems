# Numerics Run 079 — PPARγ → RORγt Suppression → Th17 ↓: Independent T Cell Axis
## PPARγ Agonists → RORγt ↓ → Th17 Differentiation ↓ → IL-17A ↓ → Loop 1 Interrupted | 2026-04-12

> Run_077 documented PPARγ → p65 transrepression in macrophages/keratinocytes (NF-κB
> suppression at DNA binding step). That mechanism acts on INNATE immune cells.
>
> PPARγ has a DISTINCT, independent mechanism in ADAPTIVE immune cells: PPARγ agonists
> suppress RORγt (RAR-related Orphan Receptor gamma t), the master transcription factor
> for Th17 cell differentiation. This is not NF-κB suppression — it is T cell lineage
> programming suppression. The two PPARγ mechanisms are:
>   - Run_077: PPARγ → p65 transrepression (macrophage/keratinocyte NF-κB; innate)
>   - This run: PPARγ → RORγt ↓ → Th17 ↓ (T cell differentiation; adaptive)
>
> Therapeutic relevance: T1DM gut dysbiosis → IS (indoxyl sulfate, run_074) → pathological AhR
> → Th17 ↑ → IL-17A → KLK5 transcription (fifth KLK5 input, established). PPARγ agonists
> (from polyphenol protocol: quercetin + resveratrol + EGCG + niacinamide + EPA) → RORγt ↓
> → Th17 suppression → IL-17A ↓ → Loop 1 interrupted at the T cell differentiation step.
> This is an additional layer of Th17 suppression beyond omega-3/GPR120 (run_062).

---

## PPARγ → RORγt: Mechanistic Basis

**RORγt (RORc2 in humans): Th17 master transcription factor:**
```
Naïve CD4+ T cell → IL-6 + TGF-β (in gut: IL-6 + IL-21) → STAT3 activation
    → STAT3 → RORγt (RORC2) expression induction
    → RORγt → Th17 lineage transcriptional program:
        IL-17A, IL-17F, IL-21, IL-22 ↑
        CCR6 ↑ (gut homing receptor)
        IL-10 ↓ (anti-inflammatory)
        Foxp3 ↓ (Treg suppressor)
```

**PPARγ → RORγt suppression (Mukundan 2009 Immunity; Cunard 2002; Nobs 2013):**
```
PPARγ agonist → ligand-bound PPARγ:
    (1) Physical interaction: PPARγ → directly binds RORγt → blocks RORγt DNA binding
        → RORγt cannot occupy RORC response elements → IL-17A promoter not activated
        (Mechanism: competitive nuclear receptor interaction; similar to PPARγ → p65)
    ↓
    (2) Transcriptional competition: PPARγ/RXR → competes with RORγt for shared co-activators
        (SRC-1, SRC-2) → less SRC available for RORγt-dependent transcription
    ↓
Combined: RORγt transcriptional activity ↓ → Th17 differentiation ↓ → IL-17A, IL-17F ↓
```

**Nobs 2013 (J Exp Med 210:2065-2079):** Key paper.
PPARγ conditional knockout in T cells (T-cell specific) → Th17 INCREASE. Confirmation:
PPARγ in T cells normally RESTRAINS Th17 differentiation.
PPARγ agonist (rosiglitazone) → T cell PPARγ activation → Th17 ↓ in vitro and in vivo.
IL-17A and RORγt mRNA both suppressed by PPARγ agonist.

**Mukundan 2009 (Immunity 31:273-285):**
PPARγ in macrophages → Th17 → Th1 balance shifted. PPARγ in T cells specifically: PPARγ
loss → Th17 polarization. Dual compartment: PPARγ in T cells (direct RORγt suppression) +
PPARγ in macrophages (p65 transrepression + reduced IL-6 production → less Th17-driving cytokine).

---

## PPARγ → Th17 ↓: Relationship to Existing Framework Mechanisms

**Th17 suppression mechanisms already in the framework:**
```
1. Omega-3/GPR120 → ERK1/2 inhibition → Th17 polarization ↓ (run_062)
   Mechanism: GPR120 Gαs → ERK1/2 → STAT3 phosphorylation ↓ → less STAT3-driven RORγt
   
2. IS (run_074) → pathological AhR → Th17 ↑ (INVERSE: removing IS restores balance)
   L. reuteri → IS ↓ (incidental) + IAd ↑ (Tregs) → net T cell balance shift toward Tregs

3. PPARγ → RORγt ↓ (this run):
   Mechanism: direct PPARγ/RORγt nuclear receptor interaction → RORγt blocked
   Distinct from omega-3 (GPR120 → ERK → STAT3) and from IS (AhR transcription factor)
```

**Three independent Th17 suppression mechanisms:**

| Mechanism | Target step | Agent |
|-----------|------------|-------|
| Omega-3/GPR120 (run_062) | STAT3 phosphorylation ↓ → less RORγt induction | EPA/DHA 2-4g/day |
| IS reduction (run_074) | Pathological AhR activation ↓ → less AhR-driven Th17 | L. reuteri + dietary fiber |
| **PPARγ → RORγt (this run)** | **RORγt DNA binding blocked → IL-17A promoter ↓** | **Quercetin + resveratrol + EGCG + niacinamide + EPA** |

All three are mechanistically independent → additive Th17 suppression.

---

## T1DM-Specific Th17 Elevation and PPARγ Response

**T1DM → Th17 elevated by multiple convergent mechanisms:**
```
T1DM gut dysbiosis pathways feeding Th17:
    IS ↑ → pathological AhR → RORγt induction ↑ (run_074)
    Secondary BA ↓ → FXR ↓ → SHP ↓ → less Treg induction (FXR → Treg differentiation, indirect)
    STAT3/leptin ↑ (Signal 1D, run_070) → STAT3 → RORγt induction ↑
    T1DM itself: Treg/Th17 imbalance fundamental to β cell destruction (Bluestone 2010 Sci Transl Med)
    ↓
T1DM: Th17 elevated from at least FOUR convergent inputs
    → IL-17A → KLK5 transcription (fifth KLK5 input) + β cell attack continuation
    → PPARγ → RORγt ↓ provides direct counter-regulation via polyphenol protocol
```

**PPARγ dual mechanism in T1DM:**
```
T cell compartment: PPARγ → RORγt ↓ → Th17 ↓ → IL-17A ↓ → KLK5 ↓ + β cell attack ↓
Macrophage compartment: PPARγ → p65 transrepression → NF-κB ↓ (run_077)
Two independent PPARγ mechanisms, two different cell types, both anti-inflammatory
→ PPARγ agonism is particularly valuable in T1DM context where BOTH T cell + macrophage
  PPARγ pathways are simultaneously suppressed by dysbiosis
```

---

## PPARγ → RORγt in Gut: Connection to Gut Treg/Th17 Balance

**Colonic PPARγ → mucosal Th17/Treg balance:**
```
Colonocyte PPARγ:
    → Fatty acid β-oxidation ↑ → epithelial oxygen consumption ↑ → luminal hypoxia maintained
    → HIF-1α in enterocytes → cryptdins + RegIII → antimicrobial peptide expression
    → Epithelial O2 consumption prevents luminal aerobic bacteria (aerobic dysbiosis)
    → This is the COLONIC EPITHELIAL PPARγ function (Byndloss 2017 Science)
    → Different from T cell PPARγ (RORγt suppression) and macrophage PPARγ (p65 transrepression)

T cell PPARγ in gut lamina propria:
    → Limits lamina propria Th17 response to gut microbiota antigens
    → PPARγ-deficient mice: spontaneous colitis with Th17 expansion in lamina propria
    → T1DM: gut PPARγ function likely reduced (hyperglycemia → AGE → PPARγ oxidation?)
```

---

## Protocol Note

**Same polyphenol cluster, additional mechanism:**
The five polyphenol/lipid agents that activate PPARγ → p65 transrepression (run_077) are
IDENTICAL to those that activate PPARγ → RORγt suppression. No new agents needed.

| PPARγ → p65 transrepression (run_077) | PPARγ → RORγt suppression (this run) |
|--------------------------------------|--------------------------------------|
| Quercetin (full PPARγ agonist at >10 µM) | Same |
| Resveratrol (partial direct PPARγ agonist) | Same |
| EGCG (partial PPARγ agonist) | Same |
| EPA/omega-3 (weak PPARγ ligand) | Same |
| Niacinamide (PGC-1α → PPARγ) | Same |

**Protocol coherence**: the polyphenol cluster delivers THREE PPARγ-mediated benefits:
1. PPARγ → CerS3 → SC ceramide ↑ (run_076; keratinocyte TRANSACTIVATION)
2. PPARγ → p65 transrepression → NF-κB ↓ (run_077; macrophage/keratinocyte innate)
3. PPARγ → RORγt ↓ → Th17 ↓ (this run; T cell adaptive)
All three from the same five dietary polyphenol agents.

---

## Kill Criteria

**Kill A: T Cell PPARγ Concentrations Not Achieved by Dietary Polyphenol PPARγ Partial Agonists**
Nobs 2013 data uses rosiglitazone (full TZD agonist). T cell PPARγ activation by partial
dietary agonists (quercetin, EGCG, resveratrol at achievable plasma concentrations) may be
insufficient for RORγt suppression.
**Status:** Partially concerning (same concern as run_077 Kill A). Applies identically: cumulative
load from five agents may achieve sufficient T cell PPARγ activation. The individual agent
concern is mitigated by combining all five simultaneously. Rosiglitazone/pioglitazone would
achieve reliable RORγt suppression but have the TZD adverse effect profile. The polyphenol
protocol provides partial benefit; the quantitative magnitude in humans on dietary polyphenols
is the uncertainty.

**Kill B: RORγt Suppression Is Not the Mechanism — PPARγ Acts on Th1 Not Th17**
Some studies show PPARγ agonists suppress Th1 (IFN-γ) as well as Th17. If PPARγ's T cell
effect is primarily Th1 suppression rather than Th17, this mechanism is not the one generating
the claimed Loop 1 benefit.
**Status:** Not killed. Nobs 2013 (J Exp Med) is specifically PPARγ → RORγt → Th17 in the
T cell compartment. Both Th1 and Th17 suppression occur — this does not kill the Th17 claim.
For the T1DM rosacea framework, Th17 is the relevant axis (IS → AhR → Th17 → IL-17A → KLK5).
PPARγ suppression of Th1 is an additional anti-inflammatory benefit (not a kill; it's a bonus).

---

*Filed: 2026-04-12 | Numerics run 079 | PPARγ RORγt Th17 T cell adaptive immune polyphenol protocol Loop 1 IL-17A T1DM*
*Key insight: PPARγ → RORγt suppression is the ADAPTIVE immune complement to PPARγ → p65 transrepression (innate). Together: PPARγ agonism suppresses BOTH macrophage NF-κB (run_077) AND T cell Th17 (this run) via two independent mechanisms in different cell types.*
*Three Th17 suppression mechanisms in framework: omega-3/GPR120 (run_062) + IS reduction/L. reuteri (run_074) + PPARγ/RORγt (this run). All three additive.*
*Protocol: same five polyphenol agents as run_077; no new agents. PPARγ cluster (quercetin + resveratrol + EGCG + EPA + niacinamide) delivers three PPARγ-mediated benefits simultaneously.*
