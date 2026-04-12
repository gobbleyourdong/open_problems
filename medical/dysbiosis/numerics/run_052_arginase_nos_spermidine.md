# Numerics Run 052 — Arginase/NOS Competition and the Spermidine Precursor Feedback
## NF-κB → Arginase → Dual Consequence: Less NO + Spermidine Precursor Accumulation | 2026-04-12

> The framework contains two arginine-dependent mechanisms that have never been connected:
> (1) Endothelial NO synthesis via eNOS (L-arginine → NO + citrulline; NO provides
>     vasodilatory anti-inflammatory tone in dermal vasculature + NF-κB suppression via
>     S-nitrosylation of IKKβ Cys179)
> (2) Spermidine biosynthesis via the polyamine pathway (L-arginine → ornithine via arginase →
>     ornithine decarboxylase → putrescine → spermidine synthase → spermidine)
> These two pathways COMPETE for the same substrate (L-arginine), and this competition is
> REGULATED BY NF-κB:
> - NF-κB → arginase-1 (ARG1) transcription ↑ (a well-documented NF-κB target gene;
>   macrophage M1→M2 transition involves arginase-1 induction by NF-κB-dependent factors)
> - Arginase-1 ↑ → L-arginine depleted → eNOS substrate limited → NO ↓
>   AND simultaneously: arginase → ornithine ↑ → spermidine precursor ↑
> This creates a STATE-DEPENDENT consequence of NF-κB activation:
>   Acute NF-κB: arginase ↑ → NO ↓ (less anti-inflammatory vasodilation; pro-inflammatory)
>   BUT: ornithine ↑ → spermidine ↑ → mitophagy (run_041) → NLRP3 Signal 2 ↓ (counter-inflammatory)
> The net effect depends on relative enzyme kinetics and substrate availability.

---

## L-Arginine Substrate Competition: eNOS vs. Arginase

**eNOS (endothelial NO synthase) pathway:**
```
L-arginine + O2 + NADPH → [eNOS] → NO + L-citrulline
    ↓
NO:
    (1) Vascular smooth muscle → sGC → cGMP → Ca2+-MLCK → vasodilation
    (2) IKKβ Cys179 S-nitrosylation → IKKβ enzymatic activity blocked → NF-κB suppressed
    (3) Mitochondrial respiratory chain → complex I NO inhibition at physiological [NO]
        → mild metabolic braking → less ROS from electron transport
    ↓
eNOS NO = anti-inflammatory: vasodilation + NF-κB suppression + ROS reduction
```

**Arginase pathway (polyamine route):**
```
L-arginine + H2O → [arginase-1 or arginase-2] → L-ornithine + urea
    ↓
L-ornithine → [ODC (ornithine decarboxylase)] → putrescine
    → [spermidine synthase] → spermidine
    → [spermine synthase] → spermine
    ↓
Spermidine → run_041: EP300 inhibition → Beclin-1 deacetylation → autophagy/mitophagy
    → mtROS + mtDNA + cardiolipin removed → NLRP3 Signal 2 sources eliminated
```

**Km competition:**
- eNOS Km for L-arginine: ~150 µM
- Arginase-1 Km for L-arginine: ~2-20 mM (much higher Km, but Vmax orders of magnitude higher)
- At physiological intracellular L-arginine (~100-150 µM): eNOS has substrate affinity advantage
  → NORMALLY eNOS dominates
- When arginase-1 massively induced (NF-κB activation → arginase ↑): despite higher Km,
  the high Vmax means arginase rapidly depletes L-arginine BELOW eNOS Km
  → eNOS becomes substrate-limited → NO production ↓ even though eNOS protein is present
- This is the "arginine paradox": supplemental L-arginine restores eNOS NO production even
  though baseline L-arginine should be sufficient — because arginase competition depletes local pool

---

## NF-κB → Arginase-1: The Transcriptional Mechanism

**NF-κB → arginase-1 (ARG1):**
```
LPS → TLR4 → NF-κB (p65/p50) → ARG1 promoter (NF-κB binding site at -1.4 kb confirmed;
    El Kasmi 2008 Nat Immunol: NF-κB DIRECT transcriptional inducer of arginase-1 in
    macrophages via IL-4Rα-independent pathway)
    ↓
Arginase-1 protein ↑ → L-arginine → ornithine → less L-arginine for eNOS
    ↓
Inflammatory microenvironment → NO ↓ → LESS NF-κB IKKβ S-nitrosylation → NF-κB MORE active
    per unit TLR4 signal (positive feedback: NF-κB → arginase → less NO → less NF-κB
    suppression → more NF-κB → more arginase)
```

**M1 gut dysbiosis → NF-κB → arginase → NO deficit in T1DM rosacea:**
- M1: LPS → TLR4 → NF-κB → arginase-1 ↑ in macrophages + endothelium
- T1DM: hyperglycemia → PKC → eNOS uncoupling (PKC-βII → phospho-eNOS Thr495 = INHIBITORY
  phosphorylation; hyperglycemia increases this; uncoupled eNOS produces superoxide not NO)
- Combined: arginase competition + eNOS uncoupling → severe NO deficit in T1DM dysbiosis
- Consequence in rosacea: NO ↓ → less vasodilatory anti-inflammatory tone → lower threshold for
  reactive flushing (same trigger → more vasomotor response); less NF-κB IKKβ suppression →
  chronic NF-κB activation sustained by NO deficit alone

---

## The Spermidine Counter-Signal: Ornithine → Anti-Inflammatory Feedback

**The unexpected anti-inflammatory consequence of arginase activation:**
```
NF-κB → arginase ↑ → L-arginine → ornithine ↑
    ↓
Ornithine → ODC → putrescine → spermidine synthase → spermidine
    ↓
Spermidine → EP300 acetyltransferase inhibition → Beclin-1 deacetylated → autophagy
    + mitophagy (PINK1/Parkin recruited to depolarized mitochondria)
    → mtROS scavenged + mtDNA removed + cardiolipin oxidation prevented
    → NLRP3 Signal 2 sources (run_041) diminished
    ↓
NET COUNTER: inflammation → arginase → spermidine → mitophagy → NLRP3 Signal 2 ↓
    (DELAYED negative feedback on NLRP3 activation)
```

**Why is this a DELAYED counter-signal?**
Arginase → ornithine is fast (minutes). ODC → putrescine → spermidine requires hours (enzyme
induction, sequential reactions). Mitophagy requires 12-24 hours (autophagosome formation,
lysosomal fusion, cargo degradation). So:
- ACUTE NF-κB → arginase → NO ↓ (IMMEDIATE: pro-inflammatory, less IKKβ suppression)
- DELAYED arginase → spermidine → mitophagy → NLRP3 ↓ (12-24h: negative feedback)

This predicts a BIPHASIC inflammatory response in high-arginase states:
- Phase 1 (hours): elevated NF-κB activity from NO deficit → peak inflammation
- Phase 2 (12-24h): spermidine-driven mitophagy → NLRP3 Signal 2 reduced → inflammation dampened
This temporal pattern matches clinical observations of rosacea flare cycles (peak at hours after
trigger, gradual spontaneous resolution over 24-48 hours even without treatment).

---

## eNOS Uncoupling in T1DM: Amplifying the Arginase Effect

**T1DM-specific eNOS uncoupling:**
```
Hyperglycemia → PKC-βII activation → eNOS Thr495 phosphorylation
    (Thr495 = inhibitory phosphorylation site; phospho-Thr495 → eNOS uncoupled →
    eNOS uses O2 without making NO → superoxide (O2•-) produced instead)
    ↓
Uncoupled eNOS: NOT NO but O2•- → peroxynitrite (ONOO-) if NO present nearby
    → NLRP3 Signal 2 (oxidative peroxynitrite → carbonyl stress → NLRP3 activation)
    → the enzyme that should produce anti-inflammatory NO is instead producing NLRP3 Signal 2
    ↓
T1DM: hyperglycemia → eNOS uncoupling + arginase ↑ from M1 NF-κB → double eNOS suppression:
    (1) Less substrate (L-arginine depleted by arginase competition)
    (2) Uncoupled enzyme (Thr495 phosphorylation)
    → Maximum NO deficit + MAXIMUM NLRP3 Signal 2 contribution from uncoupled eNOS
```

**BH4 cofactor: the third eNOS regulation point:**
eNOS requires BH4 (tetrahydrobiopterin) for coupled (NO-producing) activity. Oxidative stress
→ BH4 → BH2 (dihydrobiopterin) → eNOS further uncoupled. In T1DM with oxidative stress:
BH4 ↓ → additional eNOS uncoupling beyond PKC phosphorylation. The arginase-BH4-PKC triple
eNOS suppression in T1DM dysbiosis explains why eNOS-dependent vasodilation is severely impaired.

---

## Framework Integration: Where This Connects

**Arginase/NO/spermidine bridges these framework elements:**

1. **Loop 3 (HERV-W NF-κB self-sustaining) + NO deficit:**
   HERV-W → NF-κB → arginase → less NO → less IKKβ S-nitrosylation → NF-κB MORE ACTIVE →
   HERV-W NF-κB loop is AMPLIFIED by the NO deficit it creates. Arginase explains why the
   NF-κB loop is self-sustaining beyond HERV-W transcription alone.

2. **Spermidine supplementation (run_041) → partial arginase bypass:**
   Exogenous spermidine (wheat germ, mushrooms or supplement) provides the downstream product
   of the arginase pathway DIRECTLY → bypasses the arginase → ornithine → putrescine steps →
   EP300 inhibition achieved without requiring substrate arginase flux. This is why dietary
   spermidine supplementation is relevant even when endogenous spermidine synthesis is occurring:
   the endogenous pathway is rate-limited by L-arginine availability (depleted by arginase
   competition at high flux).

3. **L-arginine supplementation — the paradox and the fix:**
   L-arginine supplementation (2-4g/day) in inflammatory states → provides substrate for
   BOTH eNOS (→ NO restoration) AND arginase (→ ornithine → spermidine ↑). The net benefit:
   - eNOS gets substrate back → NO restored → IKKβ suppression → NF-κB ↓
   - Arginase gets MORE substrate → ornithine ↑ → spermidine ↑ → mitophagy → NLRP3 Signal 2 ↓
   Both consequences of L-arginine supplementation are anti-inflammatory. HOWEVER: in T1DM
   with eNOS uncoupling (Thr495 phosphorylation), L-arginine supplementation → arginase →
   ornithine → spermidine is the MORE reliable benefit (uncoupled eNOS cannot use the extra
   arginine productively for NO; arginase/spermidine route still functional).
   Practical: L-citrulline (2-3g/day; converted to L-arginine in kidney via argininosuccinate
   synthase; avoids hepatic arginase first-pass destruction of oral L-arginine) is preferred
   substrate for eNOS support.

4. **Vagal CAP / NO interaction (run_029):**
   α7-nAChR → JAK2/STAT3 → IKKβ inhibitory phosphorylation (NF-κB suppression via vagal CAP).
   α7-nAChR activation ALSO stimulates eNOS via Ca2+/calmodulin pathway in endothelium →
   vagal tone → NO ↑ additionally suppresses NF-κB via IKKβ S-nitrosylation. The vagal
   mechanism (run_029) has a DUAL NF-κB suppression: JAK2/STAT3 direct + eNOS/NO/S-nitrosylation.
   Vagal withdrawal → BOTH pathways lost simultaneously → explains why vagal tone is the most
   potent single modulator of dermal NF-κB.

---

## Protocol Implications

**L-citrulline as eNOS support:**
- L-citrulline 2g BID (avoids first-pass hepatic arginase cleavage of L-arginine)
- → kidney → L-arginine → eNOS substrate → NO restoration
- Evidence: Morita 2014 J Int Soc Sports Nutr: L-citrulline 3g/day → plasma L-arginine ↑ 100%
  vs. L-arginine 3g/day → plasma L-arginine ↑ only 60% (citrulline more bioavailable)
- Rosacea-specific: no direct RCT; mechanism via IKKβ S-nitrosylation + vasodilation is sound
- Cost: ~$10-15/month
- NOT in current protocol: designate as "mechanistically justified addition; low evidence tier"

**Spermidine supplementation (run_041 synergy):**
Exogenous spermidine (wheat germ 20g/day or supplement) bypasses the rate-limiting arginase →
ornithine steps → provides EP300 inhibition directly → complements L-citrulline (which works
at eNOS end of the L-arginine branch). Together: L-citrulline (→ NO → IKKβ suppression) +
spermidine (→ mitophagy → NLRP3 Signal 2 ↓) = dual arginine pathway coverage.

---

## Kill Criteria

**Kill A: Arginase-1 Is Not Significantly Elevated in Rosacea Skin or Circulating Macrophages vs. Controls**
The mechanism requires arginase-1 induction by NF-κB in the rosacea context.
**Status:** Not killed. Arginase-1 elevation in inflammatory skin conditions (psoriasis: Bruch-
Gerharz 2003; atopic dermatitis) is documented. Rosacea-specific arginase measurement: not
found in literature. Given rosacea NF-κB elevation (LL-37 → NF-κB confirmed), arginase-1
induction is predicted but not directly measured in rosacea. Testable prediction.

**Kill B: L-Citrulline Supplementation Does Not Reduce Rosacea Flushing or Inflammatory Markers**
The NO → IKKβ S-nitrosylation → NF-κB ↓ mechanism predicts L-citrulline should reduce
inflammatory markers and potentially flushing in rosacea patients with confirmed NF-κB
activity (elevated Node B).
**Status:** No rosacea-specific trial found. The arginine paradox (arginase competition → NO deficit
despite adequate total L-arginine) has been demonstrated in cardiovascular disease, heart failure,
and sickle cell disease but not rosacea. Mechanistic prediction remains testable.

---

*Filed: 2026-04-12 | Numerics run 052 | Arginase eNOS NOS NO spermidine ornithine L-arginine L-citrulline NF-κB*
*Key insight: NF-κB → arginase-1 ↑ → L-arginine substrate competition → eNOS NO ↓ (immediate: less IKKβ S-nitrosylation → NF-κB amplified) AND ornithine ↑ → spermidine ↑ → mitophagy (delayed 12-24h: NLRP3 Signal 2 ↓). Biphasic consequence explains flare-resolution cycles.*
*T1DM triple eNOS suppression: arginase competition + PKC-βII Thr495 uncoupling + BH4 oxidation → maximum NO deficit + uncoupled eNOS → superoxide → NLRP3 Signal 2*
*L-citrulline 2g BID: bypasses first-pass hepatic arginase → eNOS substrate → NO → IKKβ Cys179 S-nitrosylation → NF-κB suppressed (seventh NF-κB suppression mechanism)*
*Vagal CAP (run_029) has DUAL NF-κB suppression: JAK2/STAT3 direct + eNOS/NO/S-nitrosylation indirect — explains why vagal tone is the most potent single NF-κB modulator*
