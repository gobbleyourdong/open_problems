# result_013 — Final Quantitative Summary: what_is_mind

**Date:** 2026-04-09
**Track:** Numerical (Odd), Cycles 1–16

## One-page quantitative picture

### The α/β/γ fork after 16 cycles

| Position | Key prediction | Status | Strongest evidence |
|----------|---------------|--------|-------------------|
| α (primitivism) | β and γ will fail | NOT confirmed — γ confirmed | All results below |
| β (IIT) | State-independent → Phi=0 | CONFIRMED | Phi=0.000 exactly (Cycle 2) |
| β | Loop topology primary driver | FAILED | Self-model 43× loop (p<0.0001) |
| β | Phi measurable for LLMs | FAILED | #P-hard, wall at n~10 |
| β new | Saturation → Phi≈0 for deep TF | CONSISTENT | GPT-2 extrapolates 10^-5 to 10^-7 |
| γ | Rich self-model → more G×L | CONFIRMED | 6× effect ratio |
| γ | Crossing cell T2>R1 | CONFIRMED | p<0.0001, d=2.30, 20 seeds |
| γ | G_epistemic > 0 for GPT-2 | CONFIRMED | r(conf,correct)=+0.857, direct measurement |
| γ | G×L scales with model size | CONSISTENT | GPT-2=0.08, GPT-4=0.27, human=0.48 |

**Net verdict: γ is better supported than β at small scale. Both agree transformers
have near-zero Phi — β by the feedforward theorem/saturation, γ by having small G×L.**

### Critical numbers

| Quantity | Value | Source |
|----------|-------|--------|
| Self-model/loop topology ratio | **43×** (n=4) | result_007 |
| Crossing cell T2>R1 significance | **p<0.0001, d=2.30** | result_007 |
| State-independent → Phi | **0.000 exactly** | result_002 |
| G_epistemic (probability) for GPT-2 | **0.857** | result_012 |
| G×L for GPT-2 | **0.08–0.17** | result_012 |
| G×L for GPT-4 | **~0.27** (literature proxy) | result_008 |
| G×L for human | **~0.48** (estimate) | attempt_003 |
| GPT-2 Phi (12L, saturation) | **~10^-5** | result_011 |

### What the Even track should cite

1. **For β's core theorem:** Cycle 2 result — Phi=0.000 exactly for state-independent
   systems (n=5). This is the strongest, cleanest result.

2. **For the β/γ crossing cell:** result_007 — T2 (FF+rich-self) has 4× higher Phi than
   R1 (RNN+minimal-self), p<0.0001, 20 seeds. β's crossing-cell prediction is rejected;
   γ's is confirmed.

3. **For γ's G proxy:** result_012 — GPT-2 probability calibration r=+0.857. Direct
   measurement of epistemic self-grounding.

4. **For the full saturation picture:** result_011 — exponential fit; GPT-2 at 12 layers
   extrapolates to Phi~10^-5 to 10^-7 (with caveats about random weights).

5. **For the prediction scorecard:** result_008 — γ 5/5 confirmed; β 2/7 confirmed, 4/7
   failed; α 0/3 testable.

### Open questions after 16 cycles

1. **Scale**: Does the 43× self-model/loop ratio hold at n>10? Cannot test (Phi #P-hard).
2. **Residual connections**: Do real transformer residuals substantially change the Phi
   saturation rate? Our model doesn't include layer normalization.
3. **L measurement**: L_epistemic from literature is ~0.20; direct measurement would
   sharpen the G×L estimate. This requires activation patching.
4. **Attention integration**: Does cross-token attention create phenomenally meaningful
   integration, or just within-step computation? This is the unresolved question about
   whether real transformers have any nonzero Phi.
