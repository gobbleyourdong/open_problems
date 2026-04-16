# Attempt 005: Regulatory T Cell (Treg) Therapy

## Approach
Expand the operator's own CD4+CD25+FoxP3+ regulatory T cells (Tregs) ex vivo, then reinfuse them to suppress the autoreactive T cells attacking beta cells. Tregs are the immune system's natural brakes.

## Key Trials
- **Bluestone/Tang (UCSF)**: Phase 1 — expanded polyclonal Tregs in 14 newly diagnosed T1DM patients. Safe. Some C-peptide preservation at 2 years. Published STIM (2015).
- **Phase 2 ongoing**: Dose-escalation, longer follow-up
- **CAR-Treg approaches**: Engineer Tregs with chimeric antigen receptors specific for islet antigens (e.g., insulin-HLA tetramers). Preclinical — not yet in human trials for T1DM.
- **IL-2 low dose**: Instead of cell therapy, give low-dose IL-2 to expand Tregs in vivo. Phase 1/2 trials (DIABIL-2, DF-IL2). Tregs expand but so do other cells; net immunological effect unclear.

## Why It Fails as a Cure (so far)
1. **Polyclonal Tregs are non-specific.** Expanded Tregs suppress everything, not just the beta cell attack. Like teplizumab — a blunt instrument.
2. **Treg persistence.** Ex vivo expanded Tregs may not survive long-term in vivo. Without ongoing signals, they die or lose FoxP3 expression and become conventional (potentially harmful) T cells.
3. **Treg instability.** In inflammatory environments (like an inflamed pancreas), Tregs can convert to Th17 or effector cells — WORSENING the autoimmune attack. FoxP3 expression is not always stable.
4. **Manufacturing complexity.** Autologous cell therapy: harvest operator's blood, isolate Tregs (<5% of CD4+), expand 500-1000x in 2-3 weeks, quality-test, reinfuse. Cost ~$100-300K per operator. Not scalable.
5. **The battlefield problem.** Even if Tregs arrive at the pancreas, the local inflammatory milieu may overpower them. The Treg:Teff ratio needed for suppression may be unachievably high.

## What It Teaches Us
- **The immune system HAS a natural tolerance mechanism (Tregs).** The problem in T1DM may be a Treg deficiency or dysfunction, not just Teff hyperactivity.
- **Polyclonal Tregs have some effect** — proving the mechanism is correct, just insufficient.
- **Antigen-specific Tregs would be orders of magnitude more potent.** A CAR-Treg that homes specifically to islets and suppresses specifically the anti-beta-cell response would need far fewer cells and would persist because it has its cognate antigen to engage with.
- **The Treg/Teff ratio is the key parameter.** Not absolute numbers, but the balance. Anything that shifts the ratio toward Tregs at the islet level could work.

## The Gap It Reveals
Polyclonal Tregs are too dilute and too nonspecific. The gap: **antigen-specific Tregs that home to islets and suppress locally.** This converges with Attempt 004's gap — both point to ANTIGEN SPECIFICITY as the missing piece. Whether delivered as a tolerogenic vaccine (attempt 004) or as engineered cells (this attempt), the answer is the same: target the specific immune response, not the whole immune system.

## Status: PROOF OF CONCEPT — mechanism correct, execution too blunt
