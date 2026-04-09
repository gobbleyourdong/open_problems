# Attempt 020: Mountain 2 Deep Dive — Harmine and Beta Cell Proliferation

## The Rate Problem

Mountain 2's wall: human beta cells replicate at ~0.5-1% per year in adults. Even if FMD activates Ngn3+ progenitors, the RATE of new beta cell generation may be too slow to outpace the autoimmune attack.

Mouse beta cells replicate 10-20x faster than human beta cells. This is why mouse FMD data may overestimate human results.

**We need a beta cell mitogen — something that accelerates the replication.**

## Harmine: The DYRK1A Inhibitor

**The finding** (Wang et al., Nature Medicine, 2015; Wang et al., Cell Metabolism, 2019):

Harmine, a natural beta-carboline alkaloid found in Banisteriopsis caapi (ayahuasca vine) and Peganum harmala (Syrian rue), induces human beta cell proliferation at rates of **3-8% per day** in vitro. This is 1000x the normal adult rate.

### Mechanism
- Harmine inhibits **DYRK1A** (dual-specificity tyrosine-regulated kinase 1A)
- DYRK1A normally phosphorylates NFAT transcription factors, keeping them in the cytoplasm (inactive)
- When DYRK1A is inhibited: NFAT translocates to the nucleus → activates cell cycle genes → beta cell enters S-phase → divides
- DYRK1A is on chromosome 21 — this is why Down syndrome (trisomy 21, extra DYRK1A copy) has reduced beta cell mass and increased diabetes risk. The connection validates the target.

### Key Results
- **In vitro**: 3-8% human beta cell proliferation per day (verified across multiple labs)
- **In vivo (mice)**: harmine increases human beta cell mass in transplanted human islets
- **Synergy with GLP-1**: harmine + GLP-1 agonist (exendin-4) → 5-8% proliferation (additive/synergistic)
- **Synergy with TGF-β inhibition**: harmine + LY364947 → up to 18% proliferation in some studies
- **Beta cell specificity**: harmine preferentially drives beta cell (not alpha or ductal cell) proliferation when combined with GLP-1 signaling

### Problems
1. **Selectivity**: Harmine also inhibits MAO-A (monoamine oxidase A) → psychoactive effects at systemic doses. This is why it's in ayahuasca. Can't give it systemically at effective doses.
2. **Cancer risk**: Driving cell proliferation always carries oncogenic risk. NFAT activation is implicated in some cancers. Need long-term safety data.
3. **Next-gen DYRK1A inhibitors**: More selective compounds (GNF4877, CC-401, INDY) are in development. DYRK1A-selective without MAO-A inhibition. None in clinical trials for T1DM yet.

## How Harmine Fits Mountain 2

The FMD cycle:
1. **Fast**: autophagy clears damaged cells, activates Ngn3+ progenitors
2. **Refeed**: mTOR reactivation drives progenitor differentiation → new beta cells
3. **GAP**: the new beta cells appear but replicate slowly (0.5-1%/yr)

Add harmine (or next-gen DYRK1A inhibitor) DURING the refeeding phase:
1. **Fast**: autophagy + clearance (same as before)
2. **Refeed + DYRK1A inhibitor**: progenitors differentiate AND existing/new beta cells PROLIFERATE at 3-8%/day
3. **Result**: beta cell mass rebuilds 100-1000x faster than FMD alone

The timing matters: DYRK1A inhibitor during REFEEDING only (not during fasting). During fasting, you want autophagy (clearance). During refeeding, you want proliferation (rebuilding). The oscillation is the key.

## Convergence with Mountain 1

If you combine:
- Mountain 2 regeneration (FMD + Ngn3+ progenitors)
- Harmine/DYRK1A inhibitor (proliferation boost)
- Semaglutide (GLP-1 synergy with harmine + beta cell protection)

You might not need Mountain 1 (external cells) at all. The body regenerates its own cells, and the mitogen accelerates the process to clinically meaningful rates.

## The Updated Protocol (Stage 2 Enhancement)

**Months 2-8 (revised):**
- Monthly 5-day FMD cycle
- During refeeding (days 6-12): DYRK1A inhibitor (next-gen, not harmine — avoid MAO-A)
- Semaglutide continuous (GLP-1 synergy)
- Low-dose IL-2 during refeeding (Treg expansion to protect new cells)
- Teplizumab at study start (immune suppression window)

If the DYRK1A inhibitor achieves even 1% per day during the 7-day refeeding window, that's 7% per cycle × 6 cycles = ~50% beta cell mass increase over 6 months. Combined with FMD-driven Ngn3+ neogenesis, this could restore insulin independence.

## The Gap

No selective DYRK1A inhibitor is in clinical trials for T1DM. The target is validated (harmine works spectacularly in vitro), the mechanism is understood (NFAT nuclear translocation), and next-gen compounds exist (GNF4877, INDY). The gap: **pharma hasn't prioritized this because beta cell proliferation alone doesn't solve the immune problem.** But combined with Mountain 2 (immune reset) and Mountain 3 (environmental cleanup), it could be the rate accelerator that makes regeneration viable.

## Status: TARGET VALIDATED — next-gen DYRK1A inhibitors exist but no T1DM trial
