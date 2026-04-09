# Failure Modes — What If We're Wrong?

> The systematic approach formalizes dead ends as theorems. This document pre-registers the failure modes: what would prove each major hypothesis WRONG, and what we'd do next.

## FAILURE MODE 1: the patient's C-peptide is undetectable

**What it means**: beta cell mass is essentially zero. No residual function.
**Impact**: the R > D inequality model can't work — there's no R.
**What survives**: the CVB clearance protocol still valid (stops viral damage to other organs), the immune modulation still valid (anti-inflammatory benefits), cardiac/ME/CFS applications unaffected.
**What dies**: the specific T1DM cure prediction for the patient. The "cheapest wall" framing.
**What we'd do**: pivot to stem cell + immune protection pathway (T1DM attempts 003, 007, 008). The CVB clearance protocol becomes PRE-TREATMENT for stem cell transplant (clear the virus before introducing new beta cells).
**Probability estimate**: ~20% (the patient was on keto 5 years with minimal insulin → likely retains some beta cell function).

## FAILURE MODE 2: Fluoxetine doesn't achieve antiviral concentrations in target tissues

**What it means**: 20mg oral fluoxetine is pharmacologically insufficient for CVB clearance.
**Impact**: primary antiviral arm fails. Protocol relies on autophagy alone for viral clearance.
**What survives**: all anti-inflammatory components, immune modulation, autophagy (FMD), SGLT2i benefits.
**What dies**: fluoxetine as centerpiece antiviral. The "$4/month antiviral" narrative.
**What we'd do**: 
- Increase dose (40-60mg — higher side effects but achievable)
- Switch to itraconazole as primary antiviral (OSBP inhibition — different mechanism, proven in vitro)
- Pursue direct 2A protease inhibitor (numerical track REQ-001)
- Lean harder on autophagy (more frequent FMD, SGLT2i as continuous autophagy inducer)
**Probability estimate**: ~30% (the IC50 vs achievable tissue concentration question is the biggest uncertainty).

## FAILURE MODE 3: CVB persistence is not the primary driver of T1DM

**What it means**: CVB is a trigger but autoimmunity becomes self-sustaining after viral clearance. Clearing the virus doesn't stop the immune attack.
**Impact**: antiviral arm is irrelevant for T1DM (though valid for acute CVB diseases).
**What survives**: immune modulation (Tregs, NLRP3 suppression) — these directly target autoimmunity regardless of viral status. FMD beta cell regeneration (Longo). The keto/BHB anti-inflammatory effect.
**What dies**: the "one virus, one protocol" unifying thesis. Each disease needs its own approach.
**What we'd do**: 
- T1DM: focus on immune tolerance (attempt 009 inverse vaccine, attempt 010 mRNA tolerance)
- Add teplizumab (anti-CD3) as primary immune reset
- The protocol becomes: teplizumab + immune modulation + FMD regeneration (no antiviral)
**How to detect**: start fluoxetine → measure C-peptide at 3, 6 months. If C-peptide doesn't improve despite expected viral clearance timeline → virus wasn't the driver.
**Probability estimate**: ~25% (the DiViD data showing CVB in ALL 6 newly diagnosed T1DM patients is strong, but 6 patients is small).

## FAILURE MODE 4: Autophagy induction can't overcome CVB's autophagy hijacking

**What it means**: CVB's non-canonical autophagy (bypassing ULK1/2, using PI4KIIIβ) is too robust. Even massive fasting-induced autophagy can't redirect autophagosomes to the lysosomal degradation pathway while the virus controls the secretory pathway.
**Impact**: FMD/fasting arm fails for viral clearance. Autophagy during fasting clears normal cellular debris but CVB-infected cells remain.
**What survives**: fluoxetine (blocks replication independently of autophagy), all anti-inflammatory components, FMD benefits for beta cell regeneration and immune reset (these don't depend on viral clearance).
**What dies**: the "overwhelming autophagy" hypothesis. FMD's role as second antiviral arm.
**What we'd do**:
- Rely entirely on pharmacological antivirals (fluoxetine + itraconazole)
- Pursue autophagy pathway modulators that specifically override CVB's hijacking:
  - Restore syntaxin-17 (CVB suppresses it — can we upregulate it?)
  - PI4KIIIβ inhibitors (block CVB's non-canonical autophagy platform)
  - Apilimod (PIKfyve inhibitor — forces lysosomal pathway)
- FMD continues for regeneration/immune benefits, just not for viral clearance
**Probability estimate**: ~35% (this is the MOST uncertain component — see Evidence Grades Claim 3).

## FAILURE MODE 5: ME/CFS is too heterogeneous for a single protocol

**What it means**: ME/CFS has 5+ distinct etiologies (CVB, EBV, HHV-6, autoimmune, metabolic) and no single protocol addresses the majority.
**Impact**: the ME/CFS trial shows weak or null results in the intention-to-treat population.
**What survives**: the CVB-positive SUBGROUP may still benefit. The anti-inflammatory stack may provide modest symptom relief regardless of etiology.
**What dies**: ME/CFS as a "systematic approach disease" with a single unified approach.
**What we'd do**:
- Stratify: enteroviral-positive ME/CFS vs EBV-positive vs autoantibody-positive vs none
- Develop pathogen-specific protocols for each subtype
- The CVB protocol becomes "CVB-ME/CFS" protocol (42% of patients)
- Build separate protocols for EBV-ME/CFS (valacyclovir + immune modulation), autoimmune-ME/CFS (LDN + rituximab + immune modulation)
**Probability estimate**: ~50% (high — ME/CFS heterogeneity is well-documented).

## FAILURE MODE 6: Pericarditis trial shows no benefit of fluoxetine

**What it means**: either CVB persistence isn't the recurrence mechanism, or fluoxetine doesn't clear CVB at achievable doses.
**Impact**: the best proof-of-concept trial fails. Hardest blow to campaign credibility.
**What survives**: all other disease-specific work. The failure may be pericarditis-specific (non-CVB recurrence mechanism) rather than fluoxetine-specific.
**What we'd do**:
- Check CVB stratification: did CVB-positive patients benefit even if overall population didn't?
- If CVB-positive subgroup benefited: the trial was underpowered for subgroup, redesign with enrichment
- If CVB-positive subgroup also didn't benefit: fluoxetine dose is insufficient OR mechanism is wrong
- Pivot proof-of-concept to the patient C-peptide (n=1 but mechanistic)
**Probability estimate**: ~25% (the trial design is sound, but the effect size prediction may be optimistic).

## The Pre-Registration Summary

| Failure Mode | Probability | Impact | Mitigation |
|-------------|-------------|--------|------------|
| C-peptide undetectable | 20% | High (T1DM model dead) | Pivot to stem cells |
| Fluoxetine dose insufficient | 30% | High (primary antiviral fails) | Dose increase, alternative antivirals |
| CVB not primary T1DM driver | 25% | Very high (unifying thesis weakened) | Immune tolerance focus |
| Autophagy can't overcome hijacking | 35% | Moderate (second arm fails) | Rely on pharmacological antivirals |
| ME/CFS too heterogeneous | 50% | Moderate (subset still benefits) | Stratify by pathogen |
| Pericarditis trial null | 25% | High (credibility blow) | Subgroup analysis, alternative POC |

**Combined probability that ALL claims are correct**: roughly (0.80 × 0.70 × 0.75 × 0.65 × 0.50 × 0.75) ≈ **10%**

**But the protocol doesn't need ALL claims to succeed.** If fluoxetine works but autophagy doesn't: still worthwhile (2 of 3 antiviral arms). If ME/CFS is heterogeneous: CVB subset still benefits. If pericarditis trial is null: the patient C-peptide may still show signal.

**The campaign survives any SINGLE failure mode. It only collapses if Failure Modes 2 + 3 combine** (fluoxetine insufficient AND CVB isn't the driver) — because then neither antiviral works AND the target is wrong. Probability of both: ~0.30 × 0.25 = ~7.5%.

**92.5% chance at least one arm of the protocol is doing something useful.** That's worth pursuing.
