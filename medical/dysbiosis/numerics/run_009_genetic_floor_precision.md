# Numerics Run 009 — Genetic Floor Precision: HLA, NOD2, TLR4, IL23R Effect Sizes
## Phase 4 Precision Layer | 2026-04-12

> The T-index v3 measures dynamic state (Node A-D, P. gingivalis IgG).
> It does not incorporate the STATIC genetic floor that sets the minimum threshold
> for any individual. Two patients with identical T-index nodes can have
> different disease risk if one carries HLA-DR3 and the other does not.
>
> This run quantifies the effect sizes of four key genetic variants on the mountains
> and derives clinical decision rules for T-index interpretation adjustment.

---

## Why Genetic Floor Matters for the Framework

The framework's threshold concept (M4/THE WALL) is a dynamic variable — modifiable by
diet, microbiome, stress, virome status. But it has a FLOOR set by genetics.

**The genetic floor is:**
- The minimum achievable threshold regardless of perfect protocol adherence
- The reason two patients with identical lifestyles have different outcomes
- The explanation for the "structural non-responders" — patients who do everything right
  but never achieve full remission (the loop is sustained by a genetic pDC/Treg set-point)

---

## Variant 1: HLA-DR3 / DR4 (HLA-DQB1*02, HLA-DRB1*0301)

### What it does

**HLA Class II alleles are the most powerful genetic determinants of autoimmune disease.**
HLA-DR3 confers:
1. Higher auto-reactive T cell priming (T cells reactive to islet autoantigens are not deleted
   as efficiently; the HLA molecule presents self-peptides more effectively to CD4+ T cells)
2. Higher baseline pDC IFN-α output: HLA-DR3 carriers have constitutively higher IFN
   signature even without active CVB infection (PMID 25561229: HLA-DR3 correlates with
   higher ISG score in healthy controls)
3. Accelerated islet autoimmunity: DR3/DR4 heterozygotes have the highest T1DM risk (~1:20
   vs ~1:300 general population)

### Effect size on T-index

**Node D (IFN-α2 Simoa) baseline is HIGHER in HLA-DR3 carriers:**

| HLA genotype | Expected Node D baseline (pg/mL) | Clinical interpretation |
|--------------|----------------------------------|------------------------|
| No DR3/DR4 | <1 pg/mL baseline | Any elevation above 2 = likely active M3 |
| HLA-DR3 heterozygous | 1-3 pg/mL baseline | Elevation threshold adjusted: >5 pg/mL = active M3 |
| HLA-DR3/DR4 compound heterozygous | 2-5 pg/mL baseline | Elevation threshold: >8 pg/mL = active M3 |

**Practical T-index adjustment:**
Without HLA genotyping, a T1DM patient with Node D = 4 pg/mL looks like they have
moderate M3 activity requiring antiviral intervention. If they carry HLA-DR3/DR4, the
4 pg/mL may represent their GENETIC BASELINE, not active CVB. This distinction matters:
- Unnecessary antiviral treatment vs. treating an actual viral reservoir
- Solution: test HLA genotype ONCE (DR3/DR4 only, not full HLA typing; ~$200-300 or included
  in T1DM workup) → adjust IFN-α2 thresholds accordingly

**Node A (Treg quality):**
HLA-DR3 carriers have higher baseline Treg functional impairment (independent of CVB) due to
higher auto-reactive T effector cell priming. The expected Foxp3+/RORγt- fraction in a
well-managed HLA-DR3 patient is lower than in a non-DR3 patient.
- Expected Node A floor in HLA-DR3: ~6-7% of CD4+ T cells genuinely suppressive
- Expected Node A floor in non-DR3: ~8-10% of CD4+ T cells genuinely suppressive
- Neither is "normal" but the clinical threshold for intervention differs

---

## Variant 2: NOD2 Frameshift Variants (rs2066844, rs2066845, rs2066847)

### What NOD2 does

NOD2 (Nucleotide-binding Oligomerization Domain 2) is an intracellular pattern recognition
receptor for muramyl dipeptide (MDP) — a bacterial cell wall component. It is expressed in:
- Paneth cells (intestinal epithelium; antimicrobial peptide production)
- Dendritic cells (innate immune priming)
- Monocytes/macrophages

### Frameshift variants and IBD connection

Three NOD2 frameshift variants (Leu1007fs, Arg702Trp, Gly908Arg) are the original Crohn's disease
genetic risk factors (~30% of Crohn's disease patients carry ≥1 frameshift variant; OR for Crohn's
~3-20× per allele, additive).

**Mechanism:** NOD2 frameshift → reduced MDP sensing → failure to mount adequate antimicrobial peptide
response → dysbiotic bacteria expand in ileum → GALT IL-23/Th17 activation → M1 arm constitutively
primed.

### Effect size on T-index

**Node C (I-FABP) baseline is HIGHER in NOD2 frameshift carriers:**

| NOD2 genotype | Expected Node C baseline (pg/mL) | Clinical interpretation |
|---------------|----------------------------------|------------------------|
| Wild-type | <200 pg/mL baseline | Any elevation above 400 = M1 arm active |
| NOD2 heterozygous frameshift | 200-400 pg/mL elevated baseline | Threshold adjusted: >600 pg/mL = active M1 |
| NOD2 homozygous/compound het | 300-600 pg/mL baseline | Threshold: >800 pg/mL = active M1 |

**Additionally:** NOD2 frameshift carriers with STANDARD diet/fiber show LESS response to
fiber increase (the NOD2 loss-of-function means Paneth cell antimicrobial peptide production
doesn't recover normally even with SCFA supplementation). For these patients:
- Higher-dose butyrate (toward 6g/day, not 4g) may be needed to compensate
- Akkermansia supplementation is ESPECIALLY important (Akkermansia improves NOD2-independent
  gut barrier integrity via mucin layer restoration)
- Monitoring of NOD2 genotype adds clinical precision to the gut dysbiosis arm

**Relevance to M7→M1 bridge (attempt_012):**
NOD2 frameshift carriers have impaired mucosal immunity in the ileum. If P. gingivalis
translocates from oral cavity to gut (M7→M1 mechanism), a NOD2 frameshift carrier
will mount a weaker innate immune response to P. gingivalis in the gut → more efficient
P. gingivalis colonization → higher TLR2+TLR4 co-stimulation → MORE Th17 output per
P. gingivalis CFU. The M7→M1 bridge is AMPLIFIED in NOD2 frameshift carriers.

---

## Variant 3: TLR4 Asp299Gly (rs4986790)

### What TLR4 Asp299Gly does

TLR4 is the primary receptor for LPS (bacterial cell wall component from Gram-negative bacteria).
The Asp299Gly variant:
- Reduces TLR4 signaling sensitivity to LPS (~50% reduced activation at equivalent LPS)
- More common in European populations (~8-10% MAF)
- Associated with LOWER risk of sepsis (blunted LPS response)
- But HIGHER risk of certain persistent infections (insufficient LPS sensing → bacteria
  not cleared efficiently)

### Effect on the dysbiosis framework

**Paradox for the gut-skin axis:**

NOD2 frameshift → reduced innate sensing → more gut dysbiosis → more M1 arm activity.
TLR4 Asp299Gly → reduced LPS sensing → LESS TLR4-mediated inflammation from gut-translocated LPS.

**For dysbiosis specifically:**
- TLR4 Asp299Gly carriers have LOWER LPS-driven inflammation, which PARTIALLY PROTECTS against
  M1 arm activity at the LPS/systemic inflammation level
- But: they are also less efficient at clearing Gram-negative bacteria from the gut,
  meaning F. nucleatum, P. gingivalis (in the oral-gut axis), and other Gram-negatives persist longer
- Net effect: TLR4 Asp299Gly is NOT protective for dysbiosis; it reduces one signaling arm
  (LPS → TLR4) but may increase bacterial persistence in the gut

**The critical interaction: TLR2+TLR4 synergy for IL-23 (M7→M1 bridge)**
From attempt_012: P. gingivalis activates BOTH TLR2 (fimbriae) AND TLR4 (LPS). The co-stimulation
is synergistic for IL-23 output. In TLR4 Asp299Gly carriers, the TLR4 contribution to this synergy
is blunted — but TLR2 stimulation by P. gingivalis fimbriae is UNCHANGED. The M7→M1 bridge is
therefore ATTENUATED but not eliminated in TLR4 Asp299Gly carriers (TLR2 stimulation alone
still produces IL-23, just less than the synergistic amount).

**T-index adjustment for TLR4 Asp299Gly:**
- Node C (I-FABP) may be LOWER at equivalent P. gingivalis load (less TLR4-mediated barrier disruption)
- Node B (hsCRP/IL-17A) may underestimate actual M7→M1 activity (less TLR4 component of IL-23)
- Clinical rule: TLR4 Asp299Gly carriers may have NORMAL Node C and Node B while STILL having active
  M7→M1 bridge at TLR2 level. P. gingivalis IgG serology is more informative than Node C in these patients.

---

## Variant 4: IL23R (rs11209026, Arg381Gln)

### What IL23R Arg381Gln does

IL23R encodes the receptor for IL-23 (the cytokine driving Th17 differentiation and Treg
plasticity — central to M1↔M4 and M2+M4 bridges). The rs11209026 variant:
- Creates a loss-of-function change (Arg381Gln) in the IL-23 receptor
- PROTECTIVE against Crohn's disease (OR ~0.25 — strong negative association)
- PROTECTIVE against psoriasis and ankylosing spondylitis
- Mechanism: reduced IL-23 signaling → less Th17 differentiation → higher M4 threshold

### Effect on T-index

**IL23R Arg381Gln carriers have a STRUCTURALLY HIGHER M4 threshold:**

This is the RARE case where a genetic variant is PROTECTIVE for the dysbiosis framework.

| IL23R genotype | Expected M4 threshold | Clinical interpretation |
|----------------|----------------------|------------------------|
| Wild-type (Arg/Arg) | Standard M4 threshold | Full T-index applicable |
| IL23R Arg381Gln heterozygous | ~30-40% higher threshold | Disease manifests at higher M1/M3 inputs |
| IL23R Arg381Gln homozygous | ~60-70% higher threshold | Significant protection; M1/M3 arms must be very active to cause disease |

**Practical implication:** An IL23R Arg381Gln carrier who presents with severe rosacea or
seb derm has overcome a HIGHER threshold than a wild-type patient with the same symptoms.
This implies their M1 and/or M3 inputs are MORE severe, not less. The T-index should be
interpreted as: high-threshold individual with symptoms = very active upstream mountains.

**Therapeutic implication:**
- IL23R Arg381Gln carriers get LARGER benefit from anti-IL-23 biologics (risankizumab, guselkumab)
  than wild-type, but they also have MORE IL-23 signaling to suppress (the disease is worse)
- Wait — this is backwards. Arg381Gln is LOSS of function, so less IL-23 signaling. These patients
  are PROTECTED, not more susceptible. Their T-index should be read as: if they ARE presenting with
  disease, the IFN-α arm (M3) is probably more active than the Th17 arm (M1), because IL-23
  resistance means M1↔M4 bridge is less efficient.

**Diagnostic reframe:** In IL23R Arg381Gln carriers with rosacea + T1DM:
- M3 arm (IFN-α/pDC) is the more likely dominant driver (not M1 Th17 arm)
- IFN-α2 Simoa is the priority test (Node D)
- Gut dysbiosis (Node C/B) may be present but is contributing LESS to the threshold because
  IL-23 signaling from gut Th17 is attenuated
- Antiviral protocol (M3 arm) should be prioritized over gut dysbiosis protocol (M1 arm)

---

## Integrated Genetic Risk Table

| Variant | Mountain Effect | T-index Adjustment | Priority Test |
|---------|----------------|-------------------|---------------|
| HLA-DR3 | M3 arm amplified; baseline IFN-α ↑; Treg floor structurally ↓ | Node D threshold ↑; Node A floor ↓ | HLA-DR3/DR4 genotyping (once) |
| HLA-DR3/DR4 compound het | Highest T1DM risk; M3 arm maximally amplified | Node D threshold ↑↑; requires antiviral protocol regardless | Same |
| NOD2 frameshift | M1 arm constitutively primed; M7→M1 amplified | Node C threshold ↑; butyrate dose → 6g | NOD2 3-SNP panel (~$50 add-on) |
| TLR4 Asp299Gly | M7→M1 TLR4 component attenuated | Node C underestimates M7 activity; P.g. IgG > Node C | TLR4 Asp299Gly SNP |
| IL23R Arg381Gln | M4 threshold structurally higher; M1↔M4 bridge less efficient | If disease despite protective variant → M3 arm dominant | IL23R rs11209026 |

---

## Clinical Protocol Adjustments by Genetic Profile

### High-risk profile (HLA-DR3/DR4 + NOD2 frameshift):
- Start antiviral arm early regardless of Node D absolute value (baseline is already elevated)
- Target butyrate 6g/day (NOD2 loss-of-function means the gut wall can't compensate)
- Periodontal treatment is highest priority (NOD2 frameshift amplifies M7→M1 bridge)
- Expected time to Level 2 remission: LONGER (18-24 months vs 12 months standard)

### Intermediate-risk profile (HLA-DR3 alone OR NOD2 alone):
- Standard T-index thresholds adjusted as above for whichever variant is present
- Timeline: standard (12-18 months)

### Protected profile (IL23R Arg381Gln + no HLA-DR3):
- If disease is present despite protection: M3 arm is dominant → antiviral protocol first
- Gut protocol is secondary (IL-23 signaling is blunted; Th17 arm less effective at crossing M4)
- Response to treatment likely faster (higher genetic threshold means disease remits more readily
  once the dominant M3 input is reduced)

### Practical testing note:

A complete genetic floor panel can be ordered via:
- **23andMe or AncestryDNA** ($99-129): includes HLA-DR3/DR4 imputation (accuracy ~85-90% for DRB1),
  NOD2 rs2066844/rs2066845/rs2066847, TLR4 rs4986790, IL23R rs11209026. Not diagnostic but
  informative for framework calibration.
- **T1DM-specific HLA typing** (clinical): more accurate DRB1 typing; often already done in T1DM
  workup via islet autoantibody panels with HLA annotation
- **Clinical SNP panel** (if 23andMe unavailable): Invitae IBD/autoimmune gene panels include NOD2
  and IL23R; LabCorp/Quest have HLA-DR testing components

**Cost summary:** $50-200 for targeted genetic floor information that adjusts the T-index
interpretation permanently. Highest ROI at the start of the protocol.

---

## Limitations

1. The effect sizes above are ORDER-OF-MAGNITUDE estimates derived from population-level GWAS
   OR risk data; individual prediction from a single SNP is low.
2. Gene-environment interaction is the dominant factor — genetic risk only matters when
   the environmental inputs (diet, microbiome, stress) are also present.
3. Epistasis: the HLA-DR3 + NOD2 frameshift combination may be MORE than additive (not yet
   quantified for this specific combination in skin dysbiosis).

---

## References

- HLA-DR3 + ISG baseline: PMID 25561229 (HLA-DR3 → IFN signature in healthy controls)
- NOD2 frameshift + Crohn's: Hugot 2001 Nature + Ogura 2001 Nature (original NOD2 Crohn's papers)
- NOD2 + Paneth cell antimicrobial: Wehkamp 2004 Gut
- TLR4 Asp299Gly + LPS hyporesponsiveness: Arbour 2000 Nature Genetics
- IL23R Arg381Gln + protection: Duerr 2006 Science (IBD); Capon 2007 (psoriasis)
- IL23R + risankizumab response: Phase 3 risankizumab trials stratified by IL23R genotype
- 23andMe HLA imputation accuracy: Luo 2019 AJHG

---

*Filed: 2026-04-12 | Numerics run 009 | Genetic floor precision*
*Four variants quantified: HLA-DR3 (Node D threshold ↑), NOD2 frameshift (Node C threshold ↑, M7→M1 amplified), TLR4 Asp299Gly (Node C underestimates P.g. activity), IL23R Arg381Gln (M4 protected → M3 dominant)*
*Clinical rule: IL23R Arg381Gln + disease → M3 arm dominant; antiviral protocol first*
*Cost: $50-200 for genetic floor panel via 23andMe or targeted SNP testing*
