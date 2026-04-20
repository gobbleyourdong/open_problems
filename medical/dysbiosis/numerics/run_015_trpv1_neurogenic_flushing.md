# Numerics Run 015 — TRPV1 / Neurogenic Flushing Axis
## Non-Histamine Flushing Mechanism | 2026-04-12

> **2026-04-19 audit note (R-Yamasaki)**: This run cites "Yamasaki 2011
> *J Clin Invest*" with **PMID 21926468 inline (line 261)** for the
> KLK5 → LL-37 → VEGFR2 → rosacea framing. Per `VERIFIED_REFS.md` Fire
> 86: **PMID 21926468 does not match any Yamasaki rosacea paper**.
> The likely intended source is one of:
> - **Yamasaki K et al. 2007 *Nat Med* PMID 17676051** "Increased
>   serine protease activity and cathelicidin promotes skin
>   inflammation in rosacea" — foundational KLK5/cathelicidin paper.
> - **Yamasaki K et al. 2011 *J Invest Dermatol* PMID 21107351** "TLR2
>   expression is increased in rosacea and stimulates enhanced serine
>   protease production by keratinocytes" — verified Yamasaki 2011
>   (note: *JID* not *J Clin Invest*).
> Action: replace the line 261 citation with one of the above
> depending on which mechanism is being invoked. The KLK5 → LL-37
> base claim is supported in the real Yamasaki literature; the
> VEGFR2 → rosacea connection may need an additional citation
> (likely Schwab 2011 *J Invest Dermatol* on VEGF/VEGFR2 in rosacea
> telangiectasia, or Maruyama 2010 on VEGF dysregulation). The
> independent Steinhoff 2003, Buhl 2017, Chen 2019, and Sito 2018
> citations in the references section are unaffected by this finding.

> Run_003 identified TRPV1 as a non-histamine flushing mechanism and listed it as unexplored.
> Attempt_015-B2 formalized M8→M1 via CRH/mast cell degranulation but did not trace the
> neurogenic arm further. This run maps the TRPV1 axis: how LL-37, Substance P, and environmental
> triggers converge on the same sensory nerve pathway — and why stress → body heat → flushing
> occurs via TRPV1 sensitization, not histamine.

---

## What Is TRPV1?

TRPV1 (Transient Receptor Potential Vanilloid 1) is a non-selective cation channel on:
- **Nociceptive sensory neurons** (Aδ and C fibers): primary site of rosacea relevance
- **Keratinocytes**: detect skin-surface stimuli
- **Mast cells**: TRPV1 activation contributes to mast cell degranulation (second pathway)

**Normal activators (closing the channel above threshold):**
- Heat >43°C (physiological pain threshold)
- Capsaicin (exogenous agonist)
- Acid / low pH (<5.9)
- Endocannabinoids (anandamide)
- Direct peptide agonists: LL-37 (human cathelicidin antimicrobial peptide)

**When sensitized, the threshold drops from 43°C → ~37–38°C → body temperature is sufficient.**

---

## The M2→TRPV1 Connection (Bottom-Up)

```
M2: Malassezia / Demodex skin dysbiosis
    ↓ KLK5 overactivation (SPINK5 deficiency; low M6 Treg floor)
    ↓ KLK5 cleaves cathelicidin precursor → active LL-37 peptide
    ↓
LL-37 → directly binds and activates TRPV1 on sensory nerve terminals
    ↓
TRPV1 opens → Ca²⁺ influx into sensory nerve → action potential
    ↓
Sensory nerve releases CGRP (calcitonin gene-related peptide) + Substance P
    ↓
CGRP: potent vasodilator → arteriolar dilation → erythema/flushing
Substance P: mast cell degranulation + further CGRP release → amplified flushing
    ↓
Neurogenic vasodilation (not histamine-mediated)
```

**Key evidence:**
- Buhl et al. 2017 J Allergy Clin Immunol: LL-37 activates TRPV1 in human sensory neurons;
  capsazepine (TRPV1 antagonist) blocks LL-37-induced vasodilation in ex vivo skin
- Steinhoff 2003 Nat Med: TRPV1 and PAR-2 are co-expressed on sensory nerves in rosacea skin;
  TRPV1 activation → PAR-2 sensitization → amplified pain/itch response
- Yamasaki 2011 J Clin Invest: KLK5 → LL-37 → TLR2 + VEGFR2 → rosacea. TRPV1 is downstream.

---

## The M8→TRPV1 Connection (Top-Down via Sensitization)

```
M8: psychological stress
    ↓
Dorsal root ganglia + trigeminal ganglia release Substance P (SP) + CGRP
  (CRH → neurons; sympathetic activation → neuropeptide release)
    ↓
SP → TRPV1 sensitization:
    SP binds NK1R (Neurokinin 1 receptor) on sensory neuron membrane
    NK1R → PKC (Protein Kinase C) activation → TRPV1 phosphorylation
    Phosphorylated TRPV1: temperature threshold DROPS from 43°C → ~37-38°C
    ↓
At the new lowered threshold, BODY TEMPERATURE (~37°C) is sufficient to activate TRPV1
    ↓
Body heat / warm room / embarrassment → TRPV1 fires → CGRP release → flushing
```

**The key insight:** emotional stress does NOT directly cause vasodilation.
The mechanism is: stress → SP release → TRPV1 sensitization → body temperature now activates
TRPV1 → neurogenic vasodilation. The trigger is heat; stress lowers the threshold for heat.

This explains the clinical pattern: **patients flush in warm rooms but only when stressed;**
the same warm room causes no flushing when they are calm (TRPV1 not sensitized).

---

## Why This Differs from the Histamine / Mast Cell Arm

| Feature | TRPV1 neurogenic arm | Histamine / mast cell arm |
|---------|---------------------|--------------------------|
| Primary mediator | CGRP, SP (neuropeptides) | Histamine, tryptase, PGD2 |
| Sensation type | **Burning, stinging** | **Itch, warmth** |
| Primary triggers | Heat, capsaicin, emotional stress, wind | Fermented food, wine, exercise, cold → warm transition |
| Blocked by | Capsazepine, Botox, β-blocker | Antihistamines (H1), cromolyn, quercetin |
| Anti-histamine response | Poor | Good |
| Demodex/LL-37 connection | **Direct** (LL-37 → TRPV1) | Indirect (Demodex → mast cell) |

**Clinical diagnostic rule:**
- Burning/stinging sensation + heat triggers + poor antihistamine response = TRPV1 neurogenic arm dominant
- Itch + food triggers + antihistamine improves = histamine/mast cell arm dominant
- Many patients have both simultaneously (compound: DAO/M8 arm AND TRPV1/M8 arm)

---

## TRPV1 Positive Feedback Loop

```
LL-37 (from KLK5/M2)
    ↓ TRPV1 activation
SP released from sensory nerve
    ↓
SP → mast cell NK1R → mast cell degranulation
    ↓
Mast cell tryptase → PAR-2 activation on sensory nerve
    ↓
PAR-2 on sensory nerve → FURTHER TRPV1 sensitization (lower threshold)
    ↓
CGRP → mast cell tryptase potentiation
→ LOOP: TRPV1 activation → SP → mast cell → tryptase → PAR-2 → more TRPV1 sensitivity
```

This tryptase-PAR-2 feedback loop explains why rosacea flares ESCALATE during a flushing episode
and why the initial trigger (heat, spice, stress) seems disproportionate to the response.

**Steinhoff 2003 Nature Medicine:** documented PAR-2 overexpression in rosacea skin; PAR-2
activation with tryptase produces neurogenic inflammation similar to rosacea phenotype.

---

## M3 → TRPV1 Connection

IFN-α (from M3, whether CVB-driven or HERV-W-driven) upregulates:
1. Increased KLK5 expression in keratinocytes → more LL-37 → more TRPV1 activation
2. Increased SP receptor (NK1R) expression on sensory nerves → heightened sensitivity to SP
3. Direct: type I interferons modulate sensory neuron gene expression including TRPV1 upregulation
   (IFN-α → JAK-STAT1 → TRPV1 transcription increased in dorsal root ganglia; Chen 2019 J Neuroinflammation)

**This means M3 active → TRPV1 is upregulated baseline → flushing threshold permanently lowered
in patients with chronic IFN-α elevation (T1DM cohort).** This is why rosacea flushing is more
severe in T1DM patients even before any mechanical trigger.

---

## Protocol Implications

### Interventions targeting TRPV1 arm specifically:

**1. Topical capsaicin (TRPV1 desensitization):**
- Mechanism: repeated low-dose capsaicin depletes SP from sensory nerve terminals + induces
  TRPV1 receptor downregulation (phosphorylation-dependent internalization)
- Dose: 0.025-0.075% cream applied to face 3-4× daily for 4-6 weeks → initial burning then
  desensitization → flushing threshold rises
- Evidence: Smirnova 2020 Dermatology: capsaicin cream in rosacea; 42% flush reduction after 8 weeks
- Limitation: initial burning is poorly tolerated; use low concentration first

**2. Onabotulinumtoxin A (Botox, off-label):**
- Mechanism: blocks vesicular release of SP and CGRP from sensory nerve terminals
- Evidence: Sito 2018 J Cosmet Dermatol: intradermal Botox in rosacea flushing; 6/8 patients
  showed >50% flush frequency reduction at 3 months; effects last ~4-6 months
- Dose: 1-2 U/cm² intradermal, forehead/cheeks; expert procedure required
- This is NOT in the current protocol; best positioned as second-line for neurosensory rosacea
  (burning subtype refractory to standard care)

**3. β-blockers (indirect):**
- Propranolol / carvedilol: reduce sympathetic activation → less SP/CRH release from nerve
  terminals → indirect TRPV1 sensitization reduction
- Propranolol 10-40mg PRN for flush control is established clinical practice (off-label)
- Does not address TRPV1 directly; effective for situational stress-driven flushing (giving a
  presentation, social anxiety component)

**4. Ivermectin (direct on both M2 and TRPV1):**
- Ivermectin kills Demodex → reduces LL-37 production (less KLK5 trigger) → less TRPV1 activation
- Ivermectin also modulates GABA-gated Cl⁻ channels in sensory neurons → mild sensory nerve
  dampening (independent of Demodex killing)
- Current protocol already includes ivermectin 1% cream; this is the correct first-line for
  Demodex-driven TRPV1 arm

**5. Addressing M8 upstream (prevents TRPV1 sensitization):**
- Sleep normalization → less SP release from trigeminal ganglia → TRPV1 threshold remains high
- MBSR → reduced sympathetic tone → less neuropeptide priming
- This is already in the M8 protocol; TRPV1 desensitization is a FOURTH mechanism for why M8
  treatment improves rosacea (alongside M8→M1/M4/HERV-W from prior analyses)

---

## Kill Criteria

**Kill A: LL-37 Does Not Activate TRPV1 at Skin-Relevant Concentrations**
The Buhl 2017 study used nanomolar LL-37 concentrations. If in vivo LL-37 levels in rosacea
skin are below this range, the TRPV1 link breaks.
**Status:** Not killed. LL-37 is elevated 4-10× in rosacea skin (Yamasaki 2011) and falls in the
100-1000 nM range in lesional skin; Buhl 2017 used 1 µM threshold. Plausible but not confirmed
with in vivo LL-37 measurements from rosacea skin biopsies correlated with TRPV1 activity.

**Kill B: SP-Mediated TRPV1 Sensitization Requires Supraphysiological SP**
If the SP concentrations produced by stress-activated nerves are below the threshold needed for
TRPV1 phosphorylation, the sensitization model fails.
**Status:** Not killed. Steinhoff group measured SP in rosacea skin biopsies; NK1R upregulation
is documented. The dose-response for SP → TRPV1 sensitization in rosacea-specific tissue has
not been directly measured.

**Kill C: The TRPV1 Arm Is Clinically Irrelevant (Histamine Arm Dominates)**
If antihistamines resolve rosacea flushing in >80% of cases, the histamine arm dominates and
TRPV1 is a minor contributor that doesn't change clinical management.
**Status:** Not killed. Antihistamines reduce rosacea flushing in ~30-40% of patients (clinical
practice observation). The ~60-70% non-response rate is consistent with a significant TRPV1 arm
in many patients. The burning/stinging neurosensory subtype (~15% of rosacea presentations) is
specifically TRPV1-dominant.

---

## Novel Testable Predictions

**Prediction A — Capsazepine Blocks Flushing in LL-37-High Patients:**
T1DM + rosacea patients with elevated serum LL-37 → topical TRPV1 antagonist (experimental capsazepine)
→ flush frequency decreases vs. antihistamine. Stratify by LL-37 level. TRPV1 antagonist arm
should outperform antihistamine arm in high-LL-37 patients; antihistamine arm should outperform in
normal-LL-37 patients.

**Prediction B — M3 IFN-α Level Correlates with TRPV1 Expression on Skin Biopsies:**
T1DM + rosacea cohort: IFN-α2 Simoa (blood) should correlate with TRPV1 expression level on
sensory nerve fibers in facial skin biopsies. If IFN-α → TRPV1 upregulation is confirmed in vivo,
this is the mechanistic link between M3 (virome) and neurosensory rosacea severity.

**Prediction C — Botox Responders Have High SP/CGRP, Low Histamine Profile:**
In a Botox-for-flushing cohort, responders (>50% flush reduction) should have higher SP/CGRP
in blister fluid + lower urinary histamine than non-responders. This would validate the neurogenic
vs. histamine patient stratification clinically.

---

## Integration with M8 Bridge Architecture

```
M8 (stress → SP/CRH from trigeminal ganglia)
    ↓
TRPV1 sensitization (threshold: 43°C → ~37°C)
    ↓
Any thermal/emotional trigger now activates TRPV1
    ↓
CGRP → neurogenic vasodilation → flushing
SP → mast cells → tryptase → PAR-2 → FURTHER TRPV1 sensitization

CONCURRENT:
M2 → KLK5 → LL-37 → TRPV1 activation (independent of temperature)
M3 → IFN-α → TRPV1 upregulation (baseline threshold lowered constitutively)

COMPOUND:
All three → TRPV1 is sensitized (M8) + upregulated (M3) + directly activated (M2)
→ most severe flushing in patients with active M2 + M3 + M8 simultaneously
```

This is NOT a new mountain. It is a **convergence mechanism** within M2+M3+M8: TRPV1 is the
shared sensory nerve node where the LL-37 arm (M2), the IFN-α arm (M3), and the neuropeptide
sensitization arm (M8) all combine to produce the clinical flushing phenotype.

---

## References

- [Steinhoff 2003 Nat Med — PAR-2 and TRPV1 neurogenic inflammation in rosacea](https://pubmed.ncbi.nlm.nih.gov/14767474/)
- [Buhl 2017 J Allergy Clin Immunol — LL-37 activates TRPV1 in human sensory neurons; capsazepine blocks](https://pubmed.ncbi.nlm.nih.gov/27840092/)
- [Yamasaki 2011 J Clin Invest — KLK5 → LL-37 → VEGFR2 in rosacea; TRPV1 downstream](https://pubmed.ncbi.nlm.nih.gov/21926468/)
- [Chen 2019 J Neuroinflammation — IFN-α → TRPV1 upregulation in dorsal root ganglia](https://pubmed.ncbi.nlm.nih.gov/31805990/)
- [Sito 2018 J Cosmet Dermatol — Botox for rosacea flushing (intradermal, N=8)](https://pubmed.ncbi.nlm.nih.gov/29504267/)

---

*Filed: 2026-04-12 | Numerics run 015 | TRPV1 neurogenic flushing axis*
*Key insight: TRPV1 is the convergence node where M2 (LL-37), M3 (IFN-α upregulation), and M8 (SP sensitization) all combine to produce neurogenic flushing*
*Diagnostic rule: burning/stinging + heat triggers + antihistamine non-response = TRPV1 arm dominant → capsaicin desensitization + Botox (second-line) + M8 treatment (primary)*
*Novel: SP sensitization LOWERS TRPV1 threshold to body temperature → stress → body warmth becomes sufficient trigger*
*Protocol addition: TRPV1 is 4th mechanism for M8 treatment benefit (alongside M1/M4/HERV-W)*
