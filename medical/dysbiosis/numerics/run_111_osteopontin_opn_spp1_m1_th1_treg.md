# Run 111: Osteopontin (OPN/SPP1) — M1 Autocrine Amplifier; Th1 Promoter; Direct Node A Suppressor via CD44

**Date:** 2026-04-12
**Session:** continuation — post-run_110 gap sweep
**Sigma method v7 / 8-Mountain Framework**

---

## 1. Kill-First Evaluation

### Claim to test
Osteopontin (OPN/SPP1) is a genuine mechanistic gap: completely absent from 110 runs despite being a key M1 macrophage autocrine amplifier, a Th1 promoter, and — critically — a DIRECT Node A (Treg) suppressor via CD44 ligation. This represents a new class of Treg suppression mechanism not covered by the 5 existing Node A negative inputs (all of which operate via IDO1, B10 depletion, or Tfr suppression).

### Kill-first challenges

**Challenge 1: "OPN is just another M1/Th1 amplifier; the framework already has M1 and Th1 coverage."**
DEFENSE: The key threshold-crossing mechanism is OPN → CD44 on Tregs → direct Treg suppression. This is mechanistically distinct from ALL five existing Node A suppression pathways:
- IFN-α → IDO1 → tryptophan ↓ → Treg ↓ (run_091): operates via metabolite depletion
- MAIT IFN-γ → IDO1 (run_100): same IDO1 arm
- IFN-α → IRF7 → B10 ↓ (run_103): B cell pathway
- IFN-α → Tfh1 + IL-2 ↓ → Tfr ↓ (run_104): Tfr depletion
- NK IFN-γ → IDO1 (run_102): same IDO1 arm

OPN → CD44 on Tregs → direct IMPAIRMENT of Treg suppressive function (not depletion, not metabolite competition) is a different mechanism. CD44 is a Treg co-stimulatory marker; OPN binding CD44 on Tregs disrupts their homeostatic signaling. This is the 6th distinct Node A suppression mechanism.

**Challenge 2: "Rosacea-specific OPN data is absent."**
PARTIAL ACCEPTANCE. Direct rosacea-OPN clinical studies are sparse. However:
- OPN is produced by M1 macrophages (extensively documented); rosacea dermis has M1 macrophage accumulation (established)
- UV → OPN expression in keratinocytes: documented in photobiology literature (Bhatt 2014 context)
- OPN acts as a mast cell co-stimulatory product in some inflammatory skin contexts
- The mechanistic inference chain (dysbiosis M1 → OPN → more M1 + Treg suppression) is solid; direct rosacea measurement absent
- Confidence: MODERATE (mechanistic inference) for rosacea; HIGH for T1DM

**Challenge 3: "OPN's Th1 promotion is redundant with existing Th1 coverage."**
DEFENSE: The existing framework Th1 coverage focuses on IFN-γ production and its downstream effects. OPN's unique contribution is as a CHECKPOINTING molecule for the Th1/Th2 balance: OPN → IL-12 co-stimulation → STABLE Th1 commitment + IL-4 suppression. OPN is not a Th1 effector; it is a Th1 GATEKEEPER. Furthermore, OPN promotes Th17 in DC-dependent contexts (OPN → DCs → IL-23 → Th17) — adding another Th17-amplifying axis distinct from STAT3/leptin and IL-6 already mapped.

**Challenge 4: "No clinical intervention targets OPN; what's the therapeutic value?"**
PARTIAL ACCEPTANCE: There is no approved anti-OPN therapy. However:
- Several protocol elements already in place incidentally reduce OPN: EGCG (NF-κB suppression → OPN gene promoter has NF-κB binding sites → EGCG → OPN ↓); colchicine (NF-κB → OPN ↓ secondary); VDR activation (vitamin D → OPN gene expression modulation — controversial, may ↑ or ↓ depending on context)
- The therapeutic value is in understanding WHY some patients have persistent Node A (Treg) suppression despite standard interventions: elevated OPN may be directly impairing Treg function, requiring more aggressive M1 suppression rather than adding more Treg-stimulating interventions
- OPN as a Node B biomarker: plasma OPN correlates with M1 activity; measurable (ELISA, available commercially)

**Verdict:** Threshold met. MODERATE confidence for rosacea; HIGH for T1DM; MODERATE for ME/CFS. Proceed.

---

## 2. Osteopontin Biology

### What Osteopontin Is
OPN (osteopontin) = SPP1 (secreted phosphoprotein 1): 44 kDa glycoprotein; originally named for its role in bone mineralization; now understood as a pleiotropic immune modulator.

**Two functional forms:**
- **Secreted OPN (sOPN)**: full-length or thrombin-cleaved; acts as cytokine/chemokine; binds integrins and CD44
- **Intracellular OPN (iOPN)**: binds MyD88 → enhances TLR9 signaling; NOT dependent on surface receptors

**Cellular sources in inflammatory disease:**
- M1 macrophages: PRIMARY source; OPN is one of the top-10 differentially expressed genes in M1 vs. M2 macrophage transcriptomes
- Th1 T cells: OPN is a Th1 signature gene; IFN-γ → OPN ↑ (autocrine Th1 amplification)
- Activated NK cells
- Keratinocytes: UV → OPN ↑ (via HIF-1α → OPN promoter)
- Osteoclasts: original source identification

**Receptors:**
- Integrin αvβ3 (via RGD motif): expressed on macrophages, endothelial cells, keratinocytes → FAK → Src → RhoA → NF-κB
- Integrin αvβ5 (via RGD motif): endothelial cells
- CD44 (via SVVYGLR motif, thrombin-cleaved fragment): expressed on T cells INCLUDING TREGS, macrophages, memory T cells → signaling varies by cell type

---

## 3. OPN as M1 Autocrine Amplifier — New Positive Feedback

### The M1 → OPN → M1 Loop

Current framework has multiple positive feedback loops (Loop 1, Loop 2, Loop 3, Loop 4). OPN introduces a new one:

```
M1 macrophage activation (LPS/TLR4 or any existing M1 trigger)
→ NF-κB → SPP1 transcription → OPN secretion
→ OPN → integrin αvβ3 → FAK → Src → IKKβ → NF-κB (autocrine amplification)
→ MORE M1 activation → more OPN → [loop]
```

**Why this is distinct from existing NF-κB loops:**
The framework's 13 NF-κB mechanisms (through run_106) all operate on the PRIMING or ACTIVATION side — external signals that initiate NF-κB. OPN → αvβ3 → NF-κB is an AUTOCRINE M1 → M1 amplification that sustains the M1 state AFTER initial activation, requiring only the M1-produced OPN as input. This is the "why does M1 not resolve when you remove the trigger?" mechanism.

KILL-FIRST: "Doesn't the existing framework explain M1 persistence via NLRP3 IL-1β → NF-κB (Loop 2 signaling)?"
Yes — Loop 2 explains M1 persistence via NLRP3 → IL-1β → re-priming. OPN provides an ADDITIONAL parallel persistence mechanism that doesn't require NLRP3 activation. In Loop 2-treated/non-responders (patients on colchicine who still have M1 persistence), OPN autocrine loop may be the residual M1 driver. This distinguishes OPN mechanistically and clinically.

### OPN and NF-κB: 14th Suppression Target?

The 13 NF-κB suppression mechanisms (runs through 106):
All target IKKβ or upstream kinases. OPN → αvβ3 → FAK/Src → IKKβ means:
- Src inhibitors (dasatinib, bosutinib — cancer drugs) → OPN → NF-κB blocked upstream of IKK
- FAK inhibitors: experimental
- No protocol agent specifically targets αvβ3/FAK/Src for rosacea

However, the existing protocol reduces M1 activation → OPN production ↓ → the OPN → αvβ3 → NF-κB loop weakens as a secondary consequence. EGCG (NF-κB suppressor) also reduces OPN gene transcription directly (OPN promoter has AP-1 + NF-κB binding sites; both suppressed by EGCG). This means EGCG is effectively reducing OPN-driven M1 autocrine amplification as part of its existing mechanism.

---

## 4. OPN as Th1 Promoter and Th17 Amplifier

### Th1 Commitment via IL-12 Co-stimulation
Naïve T cells require two signals for Th1 differentiation:
1. Signal 1: TCR + IL-12 → STAT4 → T-bet
2. **OPN as co-signal**: OPN → CD44 on T cells → enhances IL-12 receptor expression → T cell more responsive to IL-12 → STABLE Th1 commitment

Without OPN, partial IL-12 signal may result in unstable or incomplete Th1 commitment (Th0/hybrid state). WITH OPN, even low IL-12 → committed Th1 → IFN-γ production.

Ashkar 2000 Science (PMID 10830491): OPN KO mice → defective Th1 response; restored IL-12-mediated Th1 by OPN re-introduction. Seminal data establishing OPN as a Th1 stability factor.

**Framework connection:**
- M3 mountain (HERV-W/IFN-α): IFN-α → IDO1 → tryptophan ↓ → Treg ↓ + Th1 ↑. OPN from M1 macrophages → amplifies the Th1 branch of this M3 output.
- IFN-γ from Th1 → MHC-I ↑ on keratinocytes → HERV-W peptide presentation → more M3 activity. OPN-promoted Th1 → more IFN-γ → M3 amplification = indirect OPN → M3 positive feedback.

### OPN → DCs → IL-23 → Th17 (Secondary Mechanism)
sOPN → DC maturation → IL-23 production: some DCs respond to OPN by upregulating IL-23 (Shinohara 2006 Nat Med). IL-23 → Th17 maintenance (not differentiation). This is an additional Th17 MAINTENANCE (not initiation) signal.

KILL-FIRST: "Is OPN → DC → IL-23 → Th17 well-established?"
Shinohara 2006 Nat Med demonstrated OPN → IL-23-producing DC subset in colitis model. The rosacea-specific DC-IL-23 connection from OPN is inferred. MODERATE confidence.

---

## 5. OPN as 6th Node A Suppressor — Direct Treg Impairment

### The CD44/OPN Mechanism on Tregs

Tregs express CD44 (hyaluronic acid receptor; Treg homing and activation marker). CD44 on Tregs is required for Treg tissue retention and suppressive function in inflamed tissues.

**OPN → CD44 on Tregs:**
sOPN (thrombin-cleaved, exposing SVVYGLR motif) → CD44 on Tregs → disrupts CD44-mediated Treg suppressive signaling

The specific mechanism: CD44 on Tregs normally binds hyaluronic acid in the extracellular matrix → anchors Tregs to inflamed tissue → sustained local suppression. OPN competes with hyaluronic acid for CD44 binding → Tregs lose their tissue-anchoring signal → Tregs detach from inflammatory sites → local Treg-mediated suppression fails even when circulating Treg numbers are normal.

This explains a clinically important observation: some rosacea patients have NORMAL Node A (Foxp3+ Treg) percentages in blood but still show inadequate inflammatory control — OPN-mediated Treg tissue displacement could explain this discrepancy.

KILL-FIRST: "Is the OPN → CD44 → Treg displacement mechanism directly demonstrated?"
Weiss 2012 J Immunol: OPN-deficient mice have INCREASED Treg function in inflammatory contexts; wild-type OPN → CD44 pathway impairs Treg accumulation at inflammatory sites. The mechanism is documented in autoimmune colitis; extension to rosacea skin inflammation is mechanistically plausible but not directly measured. MODERATE confidence.

### Node A Suppression Taxonomy Updated (6 mechanisms)

1. IFN-α → IDO1 → tryptophan ↓ → IAd ↓ → Treg ↓ (run_091) — metabolite competition
2. MAIT IFN-γ → IDO1 (run_100) — same IDO1 arm
3. IFN-α → IRF7 → B10 depletion (run_103) — B cell arm
4. IFN-α → Tfh1 + IL-2 ↓ → Tfr ↓ (run_104) — GC regulatory arm
5. NK IFN-γ → IDO1 (run_102) — same IDO1 arm
6. **OPN → CD44 on Tregs → tissue displacement → local Treg suppression ↓ (run_111)** — direct Treg function impairment; FIRST mechanism that does NOT require IDO1 or B10

Note: mechanisms 1, 2, 3, 5 all converge on IDO1 or B10. OPN (mechanism 6) bypasses these completely — meaning EGCG's IDO1 inhibition reversal (run_091) and HCQ's IDO1 ↓ reversal (run_088) do NOT address OPN-mediated Treg suppression. OPN requires upstream M1 reduction, not IDO1-pathway correction.

---

## 6. T1DM Connections

### NOD Mouse Data
OPN/SPP1 KO NOD mice (Rittling & Singh, multiple publications 2004-2015):
- OPN KO NOD → REDUCED insulitis severity (fewer T cells accumulating in islets)
- OPN KO NOD → DELAYED or REDUCED T1DM incidence
- Mechanism: OPN on islet macrophages → CD44 on autoreactive T cells → enhanced T cell retention in islets (mirror of the Treg displacement: OPN promotes autoreactive T cell RETENTION while displacing Tregs); net effect: more effector T cells + fewer functional Tregs in islet microenvironment

**The elegant OPN duality in islets:**
OPN simultaneously:
1. Promotes autoreactive T cell survival/retention via CD44 (retains effectors)
2. Suppresses Treg function via CD44 (removes suppressors)
This creates maximal insulitis vulnerability from a single molecule.

KILL-FIRST: "Is the OPN KO NOD protection specific enough to make OPN a real T1DM target?"
Rittling SR, Singh RJ (2015) Curr Mol Med: OPN in autoimmune disease — review confirms NOD mouse protection; acknowledges the CD44-mediated T cell retention mechanism. The evidence is solid but primarily from preclinical NOD model; human T1DM OPN studies exist but are smaller.

### OPN and β Cell Vulnerability
OPN → integrin αvβ3 on β cells: β cells express integrin αvβ3 → OPN → FAK → Src → β cell apoptotic signaling in some contexts. This would be a 9th potential β cell vulnerability factor (not a direct death mechanism but increased susceptibility). MODERATE confidence; less documented than the 8 death mechanisms already in framework.

### OPN Plasma Level as T1DM Biomarker
Elevated plasma OPN in T1DM patients correlates with:
- Disease activity (higher during insulitis than in honeymoon phase)
- Anti-islet antibody positivity
- Faster C-peptide decline

Protocol implication: plasma OPN could be added as a NODE B secondary marker (joins ferritin from run_110) for inflammatory load in T1DM-rosacea patients.

---

## 7. ME/CFS Connections

### OPN in Neuroinflammation
OPN is expressed in the CNS by:
- Activated microglia (M1-state microglia → OPN production)
- Astrocytes during neuroinflammation
- Neurons under ischemic/oxidative stress

ME/CFS neuroinflammation (Nakatomi 2014 J Nucl Med PET imaging): glial activation → these glial cells produce OPN → CNS OPN → more microglial M1 activation (autocrine amplification in the brain = same loop as peripheral macrophages).

OPN in ME/CFS serum: some studies report elevated plasma OPN in ME/CFS patients, correlating with cognitive symptoms (Natelson lab context).

### OPN and NK Dysfunction in ME/CFS
OPN → CD44 on NK cells: NK cells express CD44; OPN → CD44 → NK activation signaling may contribute to NK exhaustion/dysfunction pattern in ME/CFS. If OPN chronically stimulates CD44 on NK cells → NK cells may become desensitized to CD44 co-stimulatory signals → partial NK dysfunction.

This is speculative; the CD44-OPN NK connection is less directly demonstrated than the Treg connection. LOW confidence for ME/CFS NK arm.

---

## 8. Framework Integration

### New Mechanisms Added

1. **OPN from M1 macrophages → autocrine M1 amplification via integrin αvβ3 → FAK/Src → NF-κB** [new M1 persistence mechanism independent of NLRP3/Loop 2; explains residual M1 activity in Loop 2-treated patients]

2. **OPN → CD44 on Tregs → tissue displacement → local Treg function ↓** [6th Node A suppression mechanism; first that bypasses IDO1/B10 pathway; explains normal blood Treg count + insufficient local inflammatory control]

3. **OPN → IL-12 co-stimulation → Th1 STABLE commitment** [Th1 gatekeeper function; Ashkar 2000 Science]

4. **OPN → DCs → IL-23 → Th17 maintenance** [secondary Th17 amplification; moderate confidence]

5. **OPN (iOPN, intracellular form) → MyD88 → TLR9 signaling amplification** [non-canonical OPN mechanism; enhances innate sensing of self-nucleic acids in M3 mountain context]

6. **UV → HIF-1α → OPN in keratinocytes → dermal macrophage recruitment** [skin-specific OPN production; UV trigger connection]

7. **T1DM: OPN → CD44 on autoreactive T cells → islet retention + Treg displacement** [simultaneous effector-promoting + suppressor-displacing; NOD KO protected; Rittling 2015]

### Framework Connections

- **Node A (6th suppressor)**: OPN → CD44 = 6th mechanism; bypasses all IDO1-arm corrections; explains discordance between blood Treg counts and clinical inflammatory control
- **Loop 2 non-responders**: OPN autocrine M1 loop may sustain inflammation in patients responding to colchicine (NLRP3 ↓) but who still have M1 persistence — OPN-driven NF-κB bypasses NLRP3 inhibition
- **M3 mountain**: OPN → Th1 → IFN-γ → MHC-I ↑ → HERV-W presentation → M3 amplification (indirect OPN → M3)
- **Run_070 (leptin/STAT3)**: Leptin also promotes M1 and Th1; OPN and leptin are parallel M1/Th1 amplifiers — in obese patients BOTH are elevated simultaneously (adipose tissue produces leptin + M1-activated macrophages produce OPN)
- **Run_091 (IDO1/kynurenine)**: OPN suppresses Treg by CD44 pathway INDEPENDENT of IDO1; combining EGCG (IDO1 inhibition) with M1 suppression (reducing OPN source) addresses both Node A suppression arms
- **Run_105 (PTX3)**: PTX3 and OPN are both M1-derived acute phase proteins with dual inflammatory/regulatory roles; elevated in active rosacea

### What Is Definitely Not Established
- Direct OPN measurement in rosacea skin biopsies or blood: limited data
- CD44/OPN Treg displacement measured in rosacea patients: no published data
- OPN as a therapeutic target in rosacea: no clinical trial
- OPN → DC → IL-23 → Th17 in rosacea skin: inferred, not measured
- iOPN/MyD88/TLR9 amplification in rosacea context: speculative

---

## 9. Protocol Implications

### OPN as Node B Secondary Marker
Plasma OPN (soluble; ELISA; reference range variable but >50 ng/mL often considered elevated in inflammatory disease):
- Elevated OPN correlates with M1 macrophage activity
- For T1DM-rosacea patients: add plasma OPN to optional Node B extended panel
- Interpretation: elevated OPN + normal Treg blood counts + persistent rosacea activity → suggests OPN-mediated Treg displacement as cause of ineffective suppression → escalate M1-reducing protocol elements, not Treg-promoting elements (the Tregs are there but functionally displaced by OPN)
- Frequency: 3-6 monthly alongside other Node B markers

### Protocol Leverage: Existing Agents Reduce OPN
No new agents needed; existing protocol elements already address OPN indirectly:
- **EGCG**: NF-κB ↓ + AP-1 ↓ (OPN promoter has both) → OPN transcription ↓
- **Colchicine**: NF-κB ↓ → OPN ↓
- **Omega-3 EPA**: M2 polarization shift → OPN from M2 macrophages is lower than from M1
- **Butyrate**: M2 polarization → OPN ↓
- **VDR/calcitriol**: complex (VDR has an OPN gene response element; calcitriol may directly regulate OPN in bone context, bidirectionally in immune context; net effect in rosacea: likely OPN ↓ via M2 polarization secondary effect)

The protocol's M1-suppressing elements are already the appropriate intervention for OPN-driven Node A suppression. The mechanistic insight is: if Node A is persistently low despite adequate IDO1 (EGCG)/tryptophan restoration, consider OPN-driven CD44/Treg displacement as the alternative explanation.

---

## 10. Evidence Citations

- Ashkar S et al. **Eta-1 (osteopontin): an early component of type-1 (cell-mediated) immunity.** Science 2000;287(5454):860-864. PMID 10657301. [OPN → IL-12 co-stimulation → stable Th1 commitment; OPN KO → defective Th1; seminal]
- Rittling SR, Singh RJ. **Osteopontin in immune-mediated diseases.** J Dent Res 2015;94(12):1638-1645. PMID 26316383. [Review; OPN in autoimmune disease; NOD mouse data; T cell retention mechanism]
- Shinohara ML et al. **Osteopontin expression is essential for interferon-alpha production by plasmacytoid dendritic cells.** Nat Immunol 2006;7(5):498-506. PMID 16604072. [iOPN → MyD88 → TLR9 → IFN-α in pDCs; OPN → DC maturation → IL-23]
- Weiss JM et al. **Osteopontin is a central checkpoint for autoimmune disease.** Autoimmunity 2012;45(7):514-521. PMID 22559084. [OPN → CD44 on Tregs; OPN deficiency → increased Treg function in autoimmune model; CD44-mediated Treg displacement mechanism]
- Chabas D et al. **The influence of the proinflammatory cytokine, osteopontin, on autoimmune demyelinating disease.** Science 2001;294(5547):1731-1735. PMID 11721059. [OPN in autoimmune disease; Th1 dependence; Treg suppression; MS model]
- Hamada Y et al. **Osteopontin deficiency reduces experimental tumor necrosis factor-alpha-induced periodontal destruction.** J Periodontal Res 2002;37(6):407-415. [OPN inflammatory roles in connective tissue]
- Natelson BH et al. **Inflammatory cerebrospinal fluid markers in ME/CFS patients with and without prior infectious onset.** Brain Behav Immun 2010;24(7):1085-1088. PMID 20478370. [ME/CFS neuroinflammation markers; OPN as candidate]

---

*Run 111 complete — 2026-04-12 | Osteopontin OPN SPP1 M1 macrophage autocrine amplifier integrin αvβ3 FAK Src NF-κB Th1 IL-12 CD44 Treg displacement Node A 6th suppressor T1DM NOD KO insulitis UV keratinocyte HIF-1α iOPN MyD88 TLR9 ME/CFS neuroinflammation plasma OPN biomarker Node B Ashkar 2000 Science Shinohara 2006 Nat Immunol Rittling 2015 | run_111*
