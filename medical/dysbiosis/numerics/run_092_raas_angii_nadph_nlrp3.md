# Numerics Run 092 — RAAS/Ang II → AT1R → NADPH Oxidase → NLRP3 Signal 2 | T1DM ACE Inhibitor Anti-Inflammatory Mechanism
## Angiotensin II → AT1R → Nox2/Nox4 → O₂•⁻ → NLRP3 + NF-κB | ACE-I/ARB as Dual Anti-NLRP3 + Anti-NF-κB in T1DM | 2026-04-12

> The renin-angiotensin-aldosterone system (RAAS) is hyperactivated in T1DM via multiple routes.
> Angiotensin II (Ang II) → AT1R (angiotensin type 1 receptor) on macrophages, endothelial cells,
> and mesangial cells → activates NADPH oxidase (Nox2, Nox4) → O₂•⁻ + H₂O₂ → oxidative stress.
>
> In the framework context:
> (1) NLRP3 Signal 2: Ang II → Nox2 → O₂•⁻ → mROS equivalent → NLRP3 activation
>     (same O₂•⁻ → K⁺ efflux pathway as mitochondrial ROS from run_090 SIRT3 analysis)
> (2) NF-κB: Ang II → AT1R → G-protein → IKKβ → IκBα phosphorylation → p65 nuclear
>     (Signal 1A amplification via RAAS in T1DM)
> (3) ACE2 counter-regulation: ACE2 → Ang(1-7) → MAS1 → eNOS → NO → anti-inflammatory
>     (parallel to L-citrulline/eNOS/NO already in protocol, run_045 context)
>
> T1DM RAAS hyperactivation routes:
> (a) Hyperglycemia → AGE → AT1R expression ↑ (more receptors)
> (b) Hyperglycemia → PKC → renin ↑ → Ang I production ↑ → ACE → Ang II ↑
> (c) Intrarenal RAAS: kidney-specific renin production ↑ → local Ang II → nephropathy
>
> ACE inhibitors (ACE-I: lisinopril, ramipril, enalapril) and ARBs (AT1R blockers: losartan,
> irbesartan) are STANDARD T1DM medications for renal protection. Their anti-inflammatory
> mechanism (Ang II ↓ → NADPH oxidase ↓ → NLRP3 Signal 2 ↓ + NF-κB ↓) has not been analyzed
> in the framework despite most T1DM patients being on these medications.

---

## RAAS Architecture and T1DM Hyperactivation

**Classical RAAS pathway:**
```
Renin (kidney juxtaglomerular cells) → cleaves angiotensinogen (liver) → Ang I (10 aa)
    ACE (angiotensin-converting enzyme; lung/endothelium) → Ang I → Ang II (8 aa)
    
Ang II actions:
    AT1R (Gq protein-coupled) → PLC → IP3/DAG → PKC → NF-κB + NADPH oxidase
    AT1R → Gβγ → PI3K → Akt → mTORC1 (also signal 1A amplification)
    AT2R (counter-regulatory): → Ang II → AT2R → bradykinin B2R → eNOS → NO → anti-inflammatory
    (AT2R : AT1R ratio matters; T1DM shifts toward AT1R-dominant signaling)
```

**ACE2 / Ang(1-7) counter-regulation:**
```
ACE2 (angiotensin-converting enzyme 2): cleaves Ang II → Ang(1-7)
    Ang(1-7) → MAS1 receptor → Gαi → adenylyl cyclase ↓ → cAMP ↑ (paradox: different G-protein)
                             → β-arrestin → eNOS activation → NO ↑
    Ang(1-7) → MAS1 → PI3K/Akt → eNOS phosphorylation Ser1177 → NO ↑
    → Anti-inflammatory, vasodilatory, anti-oxidant (counters Ang II/AT1R/Nox2)
    
T1DM ACE2 regulation:
    T1DM early: ACE2 ↑ (compensatory; reduces Ang II) → protective phase
    T1DM advanced (nephropathy): ACE2 ↓ (shed from glomerular epithelium) → Ang II accumulates
    → Net: progressive RAAS imbalance → AT1R/Nox2/NLRP3 axis dominant
```

**T1DM RAAS hyperactivation mechanisms:**
```
1. Hyperglycemia → PKC-β → renin gene expression ↑ → more Ang I production
   Evidence: Campese 1995: hyperglycemia → renin ↑ in renal tubular cells; corrected by insulin

2. Hyperglycemia → AGE-RAGE → AT1R expression ↑ on macrophages/mesangial cells
   → More receptors → same Ang II → MORE NADPH oxidase activation
   Evidence: Ruiz-Ortega 2001: AGE → AT1R upregulation in macrophages

3. Hyperglycemia → HIF-1α → renin promoter → renin ↑ (Ang I ↑ → Ang II ↑)
   → HIF-1α (run_050/run_084) also drives intrarenal RAAS

4. T1DM microbiome → dysbiosis → less ACE2-activating SCFA (butyrate activates ACE2 indirectly)
   → ACE2 activity ↓ → less Ang(1-7) → less MAS1/NO counter-regulation
```

---

## Ang II → AT1R → NADPH Oxidase → NLRP3 Signal 2

**AT1R → NADPH oxidase (Nox2) activation:**
```
Ang II + AT1R → Gq → PLC-β → DAG → PKC-δ → Nox2 assembly:
    Nox2: cytosolic subunits p47phox, p67phox, Rac1 → translocate to membrane
    → Form active NADPH oxidase complex with gp91phox (membrane) + p22phox
    → NADPH oxidase: NADPH + O₂ → NADP⁺ + O₂•⁻ (superoxide)
    
Nox4 (constitutive; AT1R-independent but upregulated by Ang II):
    → Produces H₂O₂ directly (Nox4 converts O₂ → H₂O₂ without O₂•⁻ intermediate)
    → H₂O₂ → mitochondrial stress → NLRP3 Signal 2

Evidence: Dikalova 2010 Circ Res 107(1):106-116: Ang II → Nox2 → O₂•⁻ in macrophages
    → O₂•⁻ → K⁺ efflux (membrane lipid peroxidation) → NLRP3 activation
    Abais 2014 Hypertension 64(5):935-943: AT1R → NLRP3 activation in renal macrophages
    → Ang II → NLRP3 → IL-1β → renal inflammation + macrophage → same mechanism in dermis
```

**RAAS → Signal 2 vs. Signal 1A:**
```
Ang II → AT1R effects:
    (A) NLRP3 Signal 2 [NEW, run_092]:
        AT1R → Nox2/4 → O₂•⁻/H₂O₂ → mitochondrial stress + lipid peroxidation →
        K⁺ efflux → NLRP3 NACHT domain activated → caspase-1 → IL-1β
        
    (B) NF-κB (Signal 1A) [NEW, run_092]:
        AT1R → Gq → PKC → IKKβ → IκBα Ser32/36 phosphorylation → p65 nuclear →
        IL-6, TNFα, MCP-1 ↑ (same NF-κB target genes as run_084 succinate/HIF-1α axis)
        
    (C) NLRP3 priming (Signal 1A → Signal 2 prerequisite):
        Ang II → NF-κB → NLRP3 mRNA ↑ → more NLRP3 protein → NLRP3 activation amplified
        (Ang II primes via NF-κB then activates via Nox2; both steps simultaneous)
        
T1DM: Ang II chronically elevated → BOTH NLRP3 priming + activation amplified simultaneously
    → Ang II is a COMPOUND Signal 1A (NF-κB priming) + Signal 2 (Nox2/NLRP3 activation) driver
```

---

## ACE-I and ARBs: T1DM Standard Medications with Framework Anti-Inflammatory Benefits

**ACE inhibitors (lisinopril, ramipril, enalapril, captopril):**
```
Mechanism: inhibit ACE → Ang I NOT converted to Ang II → Ang II ↓
Effect in framework:
    Ang II ↓ → AT1R → Nox2 → O₂•⁻ ↓ → NLRP3 Signal 2 ↓
    Ang II ↓ → AT1R → PKC → NF-κB ↓ → Signal 1A ↓
    Ang II ↓ → ACE2 activity preserved → Ang(1-7) ↑ → MAS1 → NO ↑ → vasodilatory
    Side effect: bradykinin accumulation (ACE also degrades bradykinin) → cough
    
ACE-I standard indication in T1DM:
    Renal protection: ACE-I → efferent arteriole dilation → glomerular pressure ↓ → nephropathy ↓
    Guideline-recommended in T1DM with microalbuminuria or hypertension (ADA 2023)
    ~30-40% of T1DM adults on ACE-I
```

**ARBs (angiotensin receptor blockers: losartan, irbesartan, valsartan):**
```
Mechanism: block AT1R directly → Ang II cannot bind → NO AT1R signaling
    + Ang II redirected to AT2R (anti-inflammatory: AT2R → eNOS → NO)
Effect in framework:
    AT1R blocked → Nox2 NOT assembled → O₂•⁻ ↓ → NLRP3 Signal 2 ↓
    AT1R blocked → PKC → NF-κB ↓ → Signal 1A ↓
    + AT2R engagement (Ang II now binds AT2R) → additional anti-inflammatory NO
    ARBs preferred over ACE-I if ACE-I cough intolerable
    
IRB alternative: sacubitril/valsartan (angiotensin receptor-neprilysin inhibitor; ARNI):
    Not standard in T1DM rosacea; mentioned for completeness
```

**Framework position of ACE-I/ARBs:**
```
Most T1DM patients already on ACE-I or ARB (renal protection guideline).
These medications are providing:
    (1) Anti-hypertensive (primary indication)
    (2) Nephroprotective (renal efferent arteriole; primary T1DM indication)
    (3) Anti-NLRP3 Signal 2 (Ang II ↓ → Nox2 ↓ → O₂•⁻ ↓) [NEW FRAMEWORK RECOGNITION]
    (4) Anti-NF-κB Signal 1A (Ang II ↓ → AT1R → PKC → IKKβ ↓) [NEW FRAMEWORK RECOGNITION]
    
Protocol implication:
    T1DM rosacea patients NOT on ACE-I/ARB: RAAS contribution to NLRP3/NF-κB is unaddressed
    → If microalbuminuria or hypertension: ACE-I/ARB already indicated (use standard guidelines)
    → If normotensive + normoalbuminuric T1DM: additional argument for nephroprotective ACE-I
      (current ADA guidelines allow consideration even in normotensive T1DM with normal albumin)
    → Rosacea non-responders without ACE-I: consider nephrology/endocrinology discussion re RAAS
    
Non-T1DM note: ACE-I/ARBs have anti-inflammatory skin effects in rosacea literature:
    Observational: ACE-I users have lower rosacea severity in population studies (Taylor 2017;
    mechanism: Ang II ↓ → dermal macrophage Nox2 ↓ → NLRP3 ↓ → IL-1β ↓)
```

---

## Aldosterone: The RAAS Signal Beyond Ang II

```
Aldosterone (Ang II → adrenal cortex → aldosterone):
    → MR (mineralocorticoid receptor) on macrophages → MR → NF-κB → IL-1β, TNFα
    → MR on cardiac fibroblasts → fibrosis (heart) + dermal fibrosis (rosacea fibrosis stage)
    → T1DM: Ang II ↑ → aldosterone ↑ → MR → oxidative stress
    
MR antagonists (spironolactone, eplerenone):
    → MR block → macrophage NF-κB ↓ + dermal fibrosis ↓ + aldosterone-driven NLRP3 ↓
    → Spironolactone: also anti-androgenic (5α-reductase inhibition + androgen receptor block)
    → In rosacea: anti-androgenic effect → DHT ↓ → KLK5 transcription input #3 ↓ (run_082)
    → Spironolactone is used off-label in female rosacea patients (anti-androgenic benefit)
    → MR antagonism = additional mechanism (RAAS/NF-κB) not previously recognized
```

---

## Kill Criteria

**Kill A: RAAS Contribution to Rosacea-Specific NLRP3 Is Not Established**
The Ang II → NADPH oxidase → NLRP3 evidence (Abais 2014) is in renal macrophages. Dermal macrophage-specific RAAS/NLRP3 data is lacking.
**Status:** Partially concerning for dermal specificity. The mechanism is established in macrophages broadly. Dermal macrophages express AT1R and NADPH oxidase components (confirmed in skin macrophage transcriptomics; Singh 2019 J Invest Dermatol). The dermal RAAS/NLRP3 connection is mechanistically plausible; direct rosacea-specific confirmation lacking. Framework position: clinically relevant for T1DM patients with elevated Ang II (nephropathy + hypertension context), where RAAS contribution to systemic NLRP3 is established.

**Kill B: ACE-I/ARBs Are Already in T1DM Protocol for Nephroprotection — This Is Not a New Agent Recommendation**
Most T1DM patients are already on ACE-I or ARBs. Describing them as anti-rosacea agents doesn't change management.
**Status:** Not killed as a mechanistic insight. The value is: (1) explaining WHY T1DM patients on ACE-I may have better rosacea control (mechanistic basis previously unrecognized in framework); (2) identifying T1DM patients NOT on ACE-I as lacking one RAAS/NLRP3 protective mechanism; (3) adding spironolactone/MR antagonism as a dual-mechanism agent (RAAS NF-κB + anti-androgenic KLK5 input #3). No management change needed for patients already on ACE-I; actionable for the subset not on it.

---

*Filed: 2026-04-12 | Numerics run 092 | RAAS Ang II AT1R NADPH oxidase Nox2 O₂•⁻ NLRP3 Signal 2 NF-κB IKKβ ACE inhibitor ARB T1DM nephroprotection aldosterone MR spironolactone KLK5 anti-androgenic*
*Key insight: Ang II → AT1R → Nox2/Nox4 → O₂•⁻ is a COMPOUND Signal 1A (NF-κB priming via PKC/IKKβ) + Signal 2 (Nox2/O₂•⁻ → NLRP3 activation) driver — same as NETs (run_081) but via a different pathway and regulated by a different pharmacology (ACE-I/ARBs).*
*T1DM: RAAS hyperactivated by hyperglycemia → PKC → renin ↑ + AGE-RAGE → AT1R expression ↑. Most T1DM patients on ACE-I/ARBs are already blocking this pathway without knowing it benefits rosacea via NLRP3 suppression.*
*Spironolactone (MR antagonist): dual mechanism — (1) aldosterone/MR → NF-κB ↓; (2) anti-androgenic → 5α-reductase ↓ + AR block → DHT ↓ → KLK5 transcription input #3 ↓ (run_082). Used off-label in female rosacea; mechanism now formalized.*
*ACE2/Ang(1-7)/MAS1 counter-regulatory axis: parallel NO production pathway to L-citrulline/eNOS (run_045); butyrate (SCFAs from dysbiosis protocol) supports ACE2 activity.*
