# Numerics Run 067 — HMGB1 → RAGE Convergence: Single DAMP, Dual Receptor, Amplified NF-κB
## HMGB1 as a TLR4 + RAGE Dual-Receptor Agonist Post-Pyroptosis | 2026-04-12

> Run_048 documented HMGB1 as a TLR4 DAMP released from pyroptotic keratinocytes.
> Run_060 documented AGE-RAGE-NF-κB as an independent pathway (T1DM collagen AGEs → RAGE →
> DIAPH1/Rac1/NADPH oxidase → NF-κB).
>
> These two analyses were conducted independently. However, HMGB1 — the DAMP released during
> keratinocyte pyroptosis — is ALSO a direct RAGE ligand with an affinity comparable to AGEs.
> This convergence means that a single pyroptotic event (Loop 2 caspase-1 activation)
> simultaneously generates a DAMP that:
> 1. Activates TLR4 → MyD88 → NF-κB (already documented in run_048)
> 2. Activates RAGE → DIAPH1/Rac1 → NF-κB (same downstream pathway as AGE-RAGE; run_060)
>
> The two receptor signals from the same DAMP are ADDITIVE (different upstream receptors
> converging on the same IKKβ/NF-κB node) and produce a stronger, more sustained NF-κB
> response than either receptor alone — this is the "HMGB1 amplifier" effect that makes
> Loop 2 pyroptosis self-amplifying beyond just the TLR4 arm.

---

## HMGB1 Biology: Dual Receptor Binding

**HMGB1 (High Mobility Group Box 1 protein):**
HMGB1 is a nuclear chromatin-binding protein that serves as a damage-associated molecular
pattern (DAMP) when released from dying cells:

```
Normal (non-pyroptotic) state:
    HMGB1 → nuclear localization (LANA nuclear retention sequence)
    → bound to DNA → assists transcription factor assembly

Pyroptotic state (caspase-1 → gasdermin D pores → cell lysis):
    HMGB1 passively released through gasdermin D plasma membrane pores
    → extracellular HMGB1 → DAMP signal
    → Also: sub-lytic NLRP3 activation → active HMGB1 secretion via
      JAK/STAT1-dependent mechanism (Bonaldi 2003; HMGB1 acetylation
      prevents nuclear retention → secreted from activated macrophages)
```

**HMGB1 extracellular forms and receptor binding:**
```
HMGB1 exists in three redox forms extracellularly:

1. All-thiol HMGB1 (fully reduced): CXCL12 binding → CXCR4 → chemotaxis (migration)
2. Disulfide HMGB1 (partially oxidized: C23-C45 disulfide): TLR4 binding → NF-κB (run_048)
3. Oxidized HMGB1 (fully oxidized; all three Cys sulfonylated): RAGE binding → NF-κB
```

**Critical insight: the same HMGB1 released from pyroptotic keratinocyte undergoes sequential
redox modification in the inflamed dermis:**
```
Pyroptotic keratinocyte → HMGB1 released (mixed redox forms)
    ↓
Acute phase (minute → hours): All-thiol HMGB1 → CXCL12/CXCR4 → macrophage/neutrophil chemotaxis
    ↓
Hours: Disulfide HMGB1 → TLR4/MD-2 → NF-κB (run_048; the established mechanism)
    ↓
Hours-days: Oxidized HMGB1 + ROS from ongoing inflammation → RAGE binding → NF-κB
    (RAGE ligand generation is temporally extended — as long as inflammation produces ROS,
     HMGB1 is continuously oxidized to the RAGE-binding form)
```

**The pyroptotic event thus generates a TEMPORALLY EXTENDED NF-κB signal:**
- Immediate: CXCL12/CXCR4 chemotaxis (hours)
- Sustained: TLR4 → NF-κB (hours to 1-2 days)
- Extended: RAGE → NF-κB (persists days, driven by ongoing ROS oxidizing HMGB1)

---

## HMGB1 → RAGE: The Mechanistic Bridge

**HMGB1 → RAGE signaling:**
```
Oxidized HMGB1 → RAGE (receptor for advanced glycation end-products)
    Note: RAGE is named for AGE binding but is a MULTI-LIGAND RECEPTOR:
    - AGEs (run_060): T1DM collagen glycation products
    - HMGB1 (this run): pyroptotic DAMP
    - S100A8/S100A9 (calprotectin): inflammatory alarmin
    - Amyloid-β: Alzheimer's context
    ↓
RAGE → cytoplasmic tail → DIAPH1 (Diaphanous-1) → Rac1/CDC42 activation
    → Rac1 → NADPH oxidase (NOX2) complex assembly → O2•- (superoxide) production
    → Superoxide → IKKβ activation (cysteine oxidation → IKKβ → IκBα phosphorylation)
    → NF-κB (p65/p50) nuclear translocation
    → Identical downstream pathway as AGE-driven RAGE signaling (run_060)
```

**This means RAGE is activated by BOTH the structural legacy of T1DM (AGEs) AND the acute
pyroptotic DAMP (HMGB1) — different temporal scales, same downstream NF-κB pathway.**

---

## The Additive Signal: TLR4 + RAGE from Single HMGB1 Release

**Why additive signaling produces sustained NF-κB:**
```
TLR4 → MyD88 → IRAK4 → TRAF6 → TAK1 → IKKβ
RAGE → DIAPH1 → Rac1 → NADPH oxidase → ROS → IKKβ

Both converge on IKKβ via different upstream mechanisms:
TLR4 activates IKKβ via TRAF6/TAK1 (protein-protein kinase cascade; fast; 15-30 min)
RAGE activates IKKβ via ROS (redox-sensitive cysteine oxidation; slower; 30-90 min; sustained)

Together:
    Phase 1 (15-60 min): TLR4 arm → rapid IKKβ → NF-κB spike
    Phase 2 (30 min - 24h): RAGE arm → sustained ROS → IKKβ → NF-κB plateau
    Result: prolonged bimodal NF-κB activation well beyond what TLR4 alone produces
```

**In T1DM rosacea: HMGB1 hits BOTH receptors at elevated baseline:**
```
T1DM collagen AGEs → RAGE constitutively active (partial basal signaling; run_060)
    → RAGE already pre-loaded (sensitized to additional RAGE ligands)
    ↓
Loop 2 pyroptosis → HMGB1 released → oxidized HMGB1 → RAGE (same receptor)
    → RAGE has TWO simultaneous ligands (AGE from collagen + HMGB1 from DAMP)
    → RAGE signaling output = AGE signal + HMGB1 signal (additive)
    ↓
SIMULTANEOUSLY: HMGB1 → TLR4 (disulfide form) → NF-κB (second independent arm)
    ↓
Result: HMGB1 pyroptotic DAMP → TLR4 NF-κB + RAGE NF-κB simultaneously
    → Total NF-κB output >> either receptor alone
    → NLRP3 Signal 1A maximally elevated → lower threshold for next Signal 2
    → Self-amplifying: this NF-κB output → more NLRP3 → more pyroptosis → more HMGB1
```

---

## Loop 2 Self-Amplification: Complete Mechanism

**Loop 2 (NLRP3/pyroptosis) with HMGB1 dual-receptor now fully specified:**
```
Signal 1 (priming): NF-κB → NLRP3 ↑ [Signal 1A]
                    IFN-α/ISGF3 → NLRP3 ISRE ↑ [Signal 1B; M3]
                    HIF-1α → NLRP3 HRE ↑ [Signal 1C; OSA]
    ↓
Signal 2 (activation): LPS/DAMPs → NLRP3 conformational change + ASC recruitment → caspase-1
    ↓
Caspase-1 → IL-1β + IL-18 cleavage → secreted (NLRP3 output)
Caspase-1 → Gasdermin D N-terminal → plasma membrane pores
    → Pores: HMGB1 passively released + K+ efflux (NLRP3 perpetuation signal)
    → Cell lysis: HMGB1 + cellular contents → extracellular
    ↓
HMGB1 → [Disulfide form] TLR4 → TRAF6/TAK1 → IKKβ → NF-κB (Signal 1A ↑)
HMGB1 → [Oxidized form] RAGE → DIAPH1/Rac1 → NADPH oxidase → ROS → IKKβ → NF-κB (↑↑)
AGEs (pre-existing T1DM collagen) → RAGE → additive DIAPH1/Rac1 → NF-κB (↑↑↑)
    ↓
NF-κB ↑ → new NLRP3 transcription → even more NLRP3 available
    → next Signal 2 trigger → amplified Loop 2 response
    → LOOP: pyroptosis → HMGB1 → dual receptor → NF-κB ↑ → more NLRP3 → more pyroptosis
```

**The HMGB1 → RAGE arm is the reason Loop 2 does not self-extinguish after a single
pyroptotic event in T1DM patients.** Non-T1DM: HMGB1 → TLR4 (single receptor); NF-κB
resolves within 24-48h as HMGB1 is cleared. T1DM: HMGB1 → TLR4 + RAGE (dual receptor);
RAGE arm sustained by ongoing ROS oxidation of ambient HMGB1; Loop 2 does not resolve until
HMGB1 is fully cleared AND ROS generation ceases — which in T1DM (ongoing mitochondrial
uncoupling, AGE-RAGE NADPH oxidase, HIF-1α from OSA) may not happen between triggers.

---

## Convergence Map: RAGE as Multi-Ligand NF-κB Amplifier

**RAGE ligands in the dysbiosis/T1DM framework:**

| RAGE Ligand | Source | Temporal profile |
|-------------|--------|-----------------|
| AGEs (pentosidine, CML, crossline) | T1DM collagen glycation | Chronic, constitutive; increases over decades |
| HMGB1 (oxidized form) | Pyroptotic keratinocytes | Episodic; post-Loop 2 events |
| S100A8/A9 (calprotectin) | Activated macrophages | Episodic; co-secreted with IL-1β |

**All three RAGE ligands can be simultaneously present in T1DM dermis:**
AGE constitutive (chronic T1DM) + HMGB1 (from current flare) + S100A8/A9 (from macrophage
activation) = maximal RAGE engagement → DIAPH1/Rac1/NADPH oxidase → maximal ROS → sustained
NF-κB → NLRP3 constitutive priming.

**Protocol implication: targeting RAGE itself (not just its ligands) is the highest-leverage
anti-NF-κB intervention in T1DM rosacea patients with high SAF (Node F Red):**
- Current protocol targets individual RAGE ligands: AGEs (carnosine/benfotiamine), HMGB1
  reduction (NLRP3 prevention → less pyroptosis → less HMGB1 release)
- RAGE itself can be targeted by: MK-7/Gas6/Axl/SOCS1 pathway (run_039) which reduces RAGE
  expression (Axl/TAM signaling → RAGE transcription ↓); calcitriol/VDR (run_056) → RAGE
  mRNA ↓ (Kang 2011)

---

## Kill Criteria

**Kill A: HMGB1 Oxidation to RAGE-Binding Form Does Not Occur at Physiological ROS Levels in Dermis**
The three-form HMGB1 redox model is established (Venereau 2012 J Exp Med). The question is
whether dermal ROS levels in rosacea are sufficient to drive significant HMGB1 oxidation to
the RAGE-binding form (requires full sulfonylation of C106).
**Status:** Not killed. T1DM dermis has elevated ROS from three sources: AGE-RAGE/NADPH oxidase
(run_060), HIF-1α/reoxygenation from OSA (run_050), and eNOS uncoupling (run_052). The oxidative
environment is above what is required for HMGB1 → oxidized form. Venereau 2012 shows C106
oxidation occurs in chronically inflamed tissue; T1DM dermis qualifies.

**Kill B: HMGB1 → RAGE Does Not Add Meaningful NF-κB Beyond TLR4 Alone (Redundant Pathway)**
If TLR4 already produces saturating NF-κB activation from HMGB1, adding RAGE provides no
additional signal (NF-κB response is already maximal from TLR4 arm alone).
**Status:** Not killed. The NF-κB response is not saturating in vivo — it is graded and
regulated by IκBα resynthesis and A20 negative feedback. RAGE → NADPH oxidase → ROS → IKKβ
is a qualitatively DIFFERENT activation mechanism (redox-sensitive) from TLR4 → TRAF6/TAK1
(kinase cascade) — they converge on IKKβ via different cysteine residues and are not mutually
inhibitory. The temporal extension (RAGE sustained vs. TLR4 acute) is the key additive feature.

---

*Filed: 2026-04-12 | Numerics run 067 | HMGB1 RAGE TLR4 dual receptor convergence pyroptosis NF-κB self-amplifying*
*Key insight: HMGB1 from pyroptotic keratinocytes activates BOTH TLR4 (disulfide form; fast; acute NF-κB) AND RAGE (oxidized form; slow; sustained NF-κB via Rac1/NADPH oxidase). In T1DM: RAGE pre-loaded with AGEs → additional HMGB1 ligand → additive DIAPH1/Rac1 → maximal NF-κB.*
*Loop 2 self-amplification mechanism complete: pyroptosis → HMGB1 → TLR4 + RAGE → NF-κB ↑ → NLRP3 ↑ → pyroptosis → [repeat]. T1DM does not extinguish this loop between triggers due to constitutive ROS oxidizing ambient HMGB1.*
*Three simultaneous RAGE ligands in T1DM dermis: AGEs (chronic) + HMGB1 (post-flare) + S100A8/A9 (macrophage) → maximal RAGE engagement.*
*RAGE expression itself targeted by MK-7/Gas6/Axl (run_039) and calcitriol/VDR (run_056) — highest-leverage points in RAGE convergence.*
