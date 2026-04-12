# Numerics Run 075 — FXR/TGR5: Secondary Bile Acid Signaling as Lost Anti-Inflammatory Input
## M1 Gut Dysbiosis → Bile Acid Disruption → FXR NF-κB Suppression ↓ + TGR5 GLP-1 ↓ | 2026-04-12

> Gut dysbiosis disrupts secondary bile acid (BA) production. Primary BAs (cholic acid CA;
> chenodeoxycholic acid CDCA) are synthesized in the liver and secreted into the gut. Gut
> bacteria — specifically Clostridiales (Lachnospiraceae, Ruminococcaceae) and Bacteroidetes —
> convert primary BAs to secondary BAs via 7α-dehydroxylation:
>   CA → deoxycholic acid (DCA)
>   CDCA → lithocholic acid (LCA)
>
> Secondary BAs activate two distinct anti-inflammatory receptors not activated by primary BAs:
> 1. FXR (farnesoid X receptor): nuclear receptor → NF-κB suppression (competitive with p65)
> 2. TGR5 (Takeda G protein-coupled Receptor 5): Gαs → cAMP → GLP-1 release from L-cells
>
> In M1 gut dysbiosis: the specific bacteria required for 7α-dehydroxylation (primarily
> Lachnospiraceae/Clostridiales sp.) are depleted → secondary BA pool ↓ → loss of BOTH
> FXR anti-inflammatory signaling AND TGR5/GLP-1 endogenous production.

---

## Primary vs. Secondary Bile Acids: Biosynthesis

**Hepatic primary BA synthesis:**
```
Cholesterol → 7α-hydroxylase (CYP7A1) → 7α-hydroxycholesterol
    → Multiple enzymatic steps → Cholic acid (CA) + Chenodeoxycholic acid (CDCA)
    → Conjugated to glycine or taurine → Glycocholate/Taurocholate → secreted in bile
    → Bile → duodenum → digestion (emulsification)
    → Terminal ileum: 95% reabsorbed (enterohepatic circulation)
    → Colon: 5% reaches bacteria → SECONDARY BA SYNTHESIS
```

**Bacterial secondary BA synthesis (7α-dehydroxylation):**
```
CA → Clostridium scindens (Lachnospiraceae) + other Clostridiales:
    bile salt hydrolase (BSH) + 7α-dehydroxylase (bai operon) → DCA
    ↓
CDCA → same bacterial enzymes → LCA

Secondary BAs:
    DCA (deoxycholic acid): 15-25% of total BA pool in healthy gut
    LCA (lithocholic acid): 3-5% of total BA pool; potent FXR + TGR5 agonist
```

**In M1 gut dysbiosis:**
Clostridium scindens (Lachnospiraceae) and Ruminococcaceae spp. are reduced in dysbiosis
(depleted by antibiotics, Western diet, T1DM-associated microbiome shifts; Ridaura 2013 Science:
lean microbiome has more 7α-dehydroxylating bacteria).
→ Secondary BA pool ↓ significantly → DCA ↓ + LCA ↓ → FXR and TGR5 activation ↓

---

## Mechanism 1: FXR → NF-κB Suppression

**FXR (Farnesoid X Receptor; NR1H4):**
```
Secondary BAs (DCA, LCA, CDCA) → FXR nuclear receptor
    → FXR/RXR heterodimer binds FXR response elements (FREs) in target gene promoters
    ↓
FXR → NF-κB suppression via two mechanisms:

(1) Direct: FXR → SHP (Small Heterodimer Partner) induction
    → SHP → directly binds p65 → prevents p65 DNA binding at κB sites
    (Wang 2008 Hepatology: SHP → p65 interaction → NF-κB target gene ↓ in hepatocytes;
     conserved in macrophages and keratinocytes by structural homology)

(2) Competitive: FXR/RXR competes with NF-κB/p65 for CBP/p300 transcriptional co-activators
    (same mechanism as GLP-1R/CREB competition for CBP; run_073 Mechanism 1)
    → When FXR active: p65 has reduced access to co-activators → NF-κB target gene ↓
```

**FXR loss in dysbiosis = sustained NF-κB disinhibition:**
Without secondary BAs → FXR inactive → SHP not induced → NF-κB freely uses CBP/p300.
This is a CONSTITUTIVE NF-κB disinhibition from loss of an endogenous signal — similar
architecturally to how adiponectin loss (run_066) removes the AMPK/IKKβ brake.

**FXR in gut epithelium:**
FXR is expressed in ileal enterocytes (highest) + colon epithelium + liver + dermal cells
(lower). The primary anti-inflammatory action of FXR relevant to M1 is:
- Ileal FXR → reduces gut permeability (TJ expression ↑) → less LPS leakage
- Macrophage FXR → reduced pro-inflammatory polarization
- Hepatic FXR → protects against LPS-induced hepatic NF-κB (NASH mechanism; hepatitis relevance)

---

## Mechanism 2: TGR5 → Endogenous GLP-1 Release

**TGR5 (Takeda G Protein-coupled Receptor 5; GPBAR1):**
```
Secondary BAs (LCA >> DCA > CDCA > CA; potency order) → TGR5 (Gαs-coupled GPCR)
    on L-cells (enteroendocrine cells in ileum + colon)
    → Gαs → adenylyl cyclase → cAMP ↑ → PKA → vesicular GLP-1 exocytosis
    → GLP-1 secreted → portal circulation → pancreatic β cells (insulin) + vagal afferents
    ↓
GLP-1 effects relevant to framework:
    → Pancreatic: incretin effect → insulin secretion (T1DM context: limited due to β cell loss)
    → CNS: hypothalamic satiety → appetite ↓ (M8 HPA)
    → GLP-1R on macrophages/keratinocytes → cAMP/PKA → NF-κB ↓ (run_073 = ninth NF-κB suppressor)
    → GLP-1R on vagal afferents → vagal tone ↑ → α7-nAChR → NF-κB ↓ (M8 vagal arm; run_033)
```

**The TGR5 → GLP-1 → GLP-1R chain connects secondary BA production (M1 gut bacteria)
directly to the anti-inflammatory GLP-1R mechanism (run_073):**
```
M1 dysbiosis → secondary BA ↓ → TGR5 → endogenous GLP-1 ↓
    → Less endogenous GLP-1R activation → less cAMP/PKA → NF-κB less suppressed
    → Less endogenous GLP-1 → vagal afferent stimulation ↓ → vagal tone ↓ → M8 arm weakened
```

**This means GLP-1RAs (semaglutide, liraglutide; run_073) are effectively replacing the
endogenous TGR5/GLP-1 signal that M1 gut dysbiosis has depleted.**
GLP-1RA efficacy in T1DM rosacea patients may be partly explained by this: they have lower
endogenous GLP-1 production (TGR5 signal depleted by secondary BA deficit) than healthy
controls, making the exogenous GLP-1RA benefit larger in dysbiotic patients.

---

## Secondary BA Restoration: Protocol

**Primary intervention: gut bacteria that perform 7α-dehydroxylation:**
```
Clostridium scindens (Lachnospiraceae) → key 7α-dehydroxylating organism
    → Not in standard probiotic formulations (difficult to culture; spore-forming)
    → Cannot be directly supplemented with current commercial probiotics
    ↓
Indirect restoration:
    High dietary fiber + prebiotic FOS/inulin → Lachnospiraceae/Ruminococcaceae proliferation
    → These families contain 7α-dehydroxylating organisms
    → Secondary BA pool partially restored over 8-12 weeks
    (David 2014 Nature: dietary fiber → rapid Lachnospiraceae enrichment; within 3-4 days)
```

**UDCA (ursodeoxycholic acid) — a secondary BA for therapeutic use:**
```
UDCA (ursodeoxycholic acid): a secondary BA produced by gut bacteria from CDCA
    → Available as a pharmaceutical (Ursodiol; FDA-approved for primary biliary cholangitis)
    → UDCA → FXR agonist (weaker than LCA/DCA but clinically used)
    → UDCA → TGR5 agonist
    → UDCA 10-15mg/kg/day: used in NASH/PBC; also used off-label in IBD for BA malabsorption
    → For dysbiosis context: UDCA 250-500mg/day (lower than hepatology doses) could
      partially replace the depleted secondary BA pool → FXR + TGR5 activation
    Note: UDCA is OTC in some countries (UK, Germany); prescription in others (US: Ursodiol)
    → Evidence gap: UDCA specifically in rosacea/T1DM is not directly studied; mechanistic
      extrapolation from FXR/TGR5 biology
```

**Dietary ursodeoxycholic acid precursor: ursolic acid (not the same as UDCA):**
Note: Ursolic acid (from apple skin, holy basil, rosemary) is NOT UDCA despite the similar
name. Ursolic acid is a pentacyclic triterpenoid (AMPK activator, mTOR inhibitor) with no
structural relationship to bile acids. Do not confuse.

---

## FXR/TGR5 and T1DM-Specific Disruption

**T1DM additional mechanisms for BA disruption:**
1. Autonomic neuropathy → impaired gallbladder contraction → reduced bile secretion → less
   primary BA in gut → less substrate for secondary BA synthesis (Bytzer 2001: 40% T1DM
   patients have gallbladder dysfunction)
2. Hyperglycemia → CYP7A1 downregulation → reduced primary BA synthesis → smaller total
   BA pool → secondary BA ↓ proportionally
3. Ileal FXR inhibition by IS: indoxyl sulfate (run_074) → OAT-mediated intracellular
   accumulation in ileal enterocytes → ROS → FXR protein oxidation → FXR activity ↓
   (indirect: IS-driven oxidative damage impairs FXR function; Watanabe 2021 Kidney Int)

**The IS-FXR connection is a new cross-run insight:**
IS (run_074) → oxidizes FXR → FXR less responsive to secondary BAs → loss of FXR
anti-inflammatory effect is AMPLIFIED in T1DM patients with elevated IS. The dual problem:
- Secondary BA pool ↓ (less FXR agonist)
- FXR activity ↓ from IS oxidation (less FXR response per unit BA)

---

## Kill Criteria

**Kill A: Secondary BA Pool Reduction in T1DM/Rosacea Patients Is Not Clinically Documented**
Direct measurement of secondary BA pool in T1DM rosacea patients is lacking. The mechanism
is inferred from: (1) T1DM → Lachnospiraceae ↓ (confirmed; Lambeth 2019); (2) Lachnospiraceae
→ secondary BA ↓ (confirmed; Ridaura 2013); but the combination in T1DM rosacea specifically
is not measured.
**Status:** Not killed. Two-step inference is mechanistically sound; both steps are individually
confirmed. Clinical measurement would strengthen the claim but absence of direct T1DM rosacea
data is a data gap, not a mechanism kill.

**Kill B: FXR SHP → p65 Interaction Is Not Demonstrated in Dermal Macrophages**
Wang 2008 is in hepatocytes. Dermal macrophage FXR expression is lower (FXR is mainly a
liver/gut receptor). Dermal FXR-NF-κB inhibition may be minimal compared to gut/liver.
**Status:** Partially concerning for DERMIS specifically. The primary FXR anti-inflammatory
benefit operates at the gut barrier level (ileal FXR → TJ proteins → less LPS leakage) and
hepatic level (less systemic LPS-driven NF-κB). The TGR5 → GLP-1 → systemic mechanism is
not limited to gut — GLP-1 reaches dermal macrophages systemically. The dermal FXR direct
claim is moderated: primary benefit is through gut barrier + TGR5/GLP-1 systemic arms.

---

*Filed: 2026-04-12 | Numerics run 075 | FXR TGR5 secondary bile acid DCA LCA Clostridium scindens Lachnospiraceae UDCA endogenous GLP-1*
*Key insight: M1 dysbiosis → Lachnospiraceae ↓ → secondary BA ↓ (DCA + LCA) → FXR NF-κB suppression ↓ + TGR5 endogenous GLP-1 ↓. The TGR5 → GLP-1 → GLP-1R chain means gut dysbiosis directly reduces endogenous GLP-1 signaling — explaining why GLP-1RAs (run_073) may be particularly effective in dysbiotic T1DM patients.*
*New cross-run insight: IS (run_074) oxidizes FXR protein → FXR activity ↓ even with residual secondary BAs = compounded BA dysfunction from IS.*
*Protocol: dietary fiber → Lachnospiraceae ↑ → secondary BA restoration (primary). UDCA 250-500mg/day as supplemental secondary BA replacement (mechanistic extrapolation; evidence gap noted).*
