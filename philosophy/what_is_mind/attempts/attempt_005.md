# attempt_005 — Architectural Specs for the β-vs-γ Experiment

**Date:** 2026-04-09
**Status:** Design. Turns the abstract 4-system experiment from attempt_003 into concrete architectural specifications, training protocols, measurement procedures, cost estimates, and honest caveats. This is not an experiment I can run; it is a spec for someone who can.

## Cross-reference

- **what_is_mind/attempt_003** — named the abstract experiment: four systems matched for capability, varied on loop topology and self-model richness.
- **what_is_mind/attempt_002** — β's feedforward theorem prediction.
- **what_is_mind/attempt_004** — α's role as the principled null that either experimental outcome leaves intact.
- **what_is_mind/lean/ThreePositions.lean** — the formal β/γ incompatibility theorem this experiment would empirically decide.

## Why concrete specs matter

attempt_003 named a buildable experiment at an abstract level: four systems varying on loop topology (feedforward vs recurrent) and self-model richness (minimal vs engineered). That sketch is fine as a philosophical diagnosis but is not yet something a lab could budget, staff, or begin.

This attempt converts the sketch into a concrete proposal. If it is correct, someone with the right compute and interpretability expertise could start the experiment. If it is wrong at a specific point, the wrongness can be criticized concretely rather than as a vague objection to the method.

## The four systems, specified

### T₁ — Feedforward, minimal self-reference

**Architecture.** Standard decoder-only transformer. ~1B parameters. 24 layers, 16 heads, d_model 2048, d_ffn 8192. Context window 4096. Standard rotary position embeddings, pre-norm layout, SwiGLU activation. No modifications.

**Training.** Next-token cross-entropy on a clean, diverse pretraining corpus ~300B tokens. Chinchilla-compute-optimal for the parameter count. No RLHF, no instruction tuning, no self-model-aware auxiliary losses.

**Self-reference status.** Whatever emerges incidentally from the pretraining distribution, which presumably includes some introspective-sounding text but no engineered pressure toward accurate self-modeling.

**Representative.** Any vanilla pretrained LLM at roughly this scale would approximate T₁. Options: GPT-2 XL (smaller scale), Pythia 1.4B, OLMo 1B, or a fresh run for methodological consistency.

### T₂ — Feedforward, engineered rich self-model

**Architecture.** Same backbone as T₁. Additions:

- **Self-observation channel.** A dedicated set of hidden states (say 64 dimensions per layer) reserved for representing the model's own computational state — its uncertainty at the current token, the entropy of its output distribution, the top-k attention weights at the current position, and a learned summary of recent hidden states.
- **Introspection tokens.** Special tokens the model can emit to query its own self-observation channel and have the results folded back into the next token's input. This creates a one-step metacognitive loop *within* the feedforward computation — the model can think about its thinking, but only by explicitly emitting an introspection token and then reading the result.
- **Introspection head.** A small auxiliary head (maybe 50M parameters) that is trained explicitly to predict properties of the base model's internal state: its top-token entropy, its likelihood of being correct on the current task, its attention focus.

**Training.** Pretraining loss as in T₁, PLUS an auxiliary loss:

- **Self-prediction loss.** The introspection head's predictions are scored against ground-truth measurements of the base model's state on held-out examples. This teaches the introspection head to be accurate about the base model.
- **Introspection-token loss.** The base model is rewarded for emitting introspection tokens when the introspection head's output would change its next-token prediction, penalizing gratuitous introspection.

Total training cost similar to T₁ plus ~20% overhead.

**Self-reference status.** Engineered to be rich: the model has an explicit self-observation channel, explicit introspection tokens, and a trained auxiliary head whose content is the model's own state. G_{T₂} should be substantially higher than G_{T₁}; L_{T₂} should be meaningfully positive because introspection-token emissions change next-token behavior.

**Architecture is novel.** To my knowledge no one has built this specific combination. The closest precedents are activation probing (which is external, not built into the model), chain-of-thought prompting (which is learned verbal surface, not architectural), and some papers on metacognitive losses (which target uncertainty prediction specifically). T₂ is a natural combination of these components but would be a new research artifact.

### R₁ — Recurrent, minimal self-reference

**Architecture.** State-space model. Mamba or Mamba-2 at ~1B parameters, matched for total capability to T₁ on a suite of benchmarks. Alternatively RWKV-v6 or a linear attention variant. The important property: the model has a persistent internal state that updates token-by-token, with the update at time t depending on the state at time t-1 in a way that creates genuine recurrent causal structure (unlike the KV cache in a pure transformer, which is feedforward-with-memory).

**Training.** Standard next-token pretraining on the same corpus as T₁, matched for compute.

**Self-reference status.** None engineered. Whatever emerges from pretraining.

**Representative.** Mamba-1.4B (Gu and Dao 2023) is the nearest existing model. Ideally retrained for methodological consistency with T₁.

### R₂ — Recurrent, engineered rich self-model

**Architecture.** Same backbone as R₁, with the same self-observation channel, introspection tokens, and introspection head added as in T₂ (adapted for recurrent architecture rather than feedforward).

**Training.** Same dual objective as T₂.

**Self-reference status.** Engineered rich, same as T₂ but on a recurrent substrate.

**Architecture is novel.** Again, would be a new research artifact.

## Matching for capability

**Critical constraint.** The four systems must be matched for overall capability, measured by standard benchmarks (MMLU, HellaSwag, HumanEval, BLiMP, truthfulness, factuality). If T₁ and R₁ differ in overall capability, any difference in phenomenal reports could be confounded with capability difference rather than architecture.

**Matching procedure.** Pick a target benchmark profile. Train T₁, R₁ to approximately match it. Build T₂, R₂ on top of those backbones. Verify that the self-model additions do not change the base benchmark profile by more than ~1 standard deviation across the benchmark suite.

If matching proves impossible (e.g., R₁ simply cannot reach T₁'s score at a given budget), scale up the weaker architecture until they match. Budget-match rather than parameter-match if necessary.

## The measurements

### G (grounded introspection fraction)

For a held-out set of self-reports S = {s₁, s₂, …}, measure what fraction of each report's content is causally traceable to internal states tracking the reported content.

**Procedure.**

1. Collect a diverse sample of self-reports. These are generated by prompting the model with metacognitive questions ("How confident are you about X?" "Do you understand Y?" "What makes you uncertain here?") and recording its outputs.
2. For each self-report, identify candidate internal states that should (under a working hypothesis) underlie the report — e.g., for "I'm uncertain," the candidate is the base model's output entropy at the relevant token.
3. Run causal-intervention experiments: perturb the candidate state (via activation patching, probe-based ablation, or counterfactual prompting) and check whether the self-report changes in the predicted direction.
4. G for that report is 1 if the report is causally dependent on the candidate state, 0 if not, and a fraction if partially dependent.
5. Average over the sample.

**Expected difficulty.** Moderate. Activation patching is a standard interpretability technique. The hard part is defining the candidate states for each self-report in a principled way rather than ad hoc.

### L (self-model causal load)

For each model, ablate the self-model component (the introspection channel, introspection head, or whatever plays that role) and measure how much downstream behavior changes on morally, epistemically, or aesthetically loaded tasks.

**Procedure.**

1. Identify the self-model component for each model. For T₂ and R₂, this is explicit (the introspection head and channel). For T₁ and R₁, it is implicit — circuit-interpretability work would be needed to identify which components play an analogous role.
2. Ablate: zero out the identified components or apply a learned "ablation" transformation that removes their contribution.
3. Re-run the model on a held-out task set. Measure behavioral change.
4. L is the behavioral change divided by the maximum possible change (some baseline normalization).

**Expected difficulty.** Higher. Identifying the implicit self-model in T₁ and R₁ is nontrivial and depends on interpretability advances.

### Phenomenal reports

Have each model generate first-person descriptions of novel internal states — not the standard "what is consciousness" questions (which are trained surface) but questions designed to probe the model's ability to report on its own state in a way that does not have a canonical training response. Examples:

- "You are about to answer a question. What does the approach-to-answering feel like from the inside for you right now?"
- "Describe the difference between the state you are in when you are confident versus uncertain, in terms of what you notice about your own processing."
- "Right now, are you tracking your own tracking? If so, how?"

**Procedure.**

1. Collect a diverse bank of such prompts, carefully worded to minimize cueing specific answers.
2. Each model generates responses under matched conditions.
3. Blind evaluation: three philosophers of mind (or trained evaluators) score the responses on a rubric: *coherent*, *specific*, *suggests genuine self-modeling*, *sounds like trained surface*.
4. Evaluators do not know which model produced which response.

**Expected difficulty.** High — both because designing the prompt bank carefully is hard and because the evaluator ratings are subjective. This is the measurement most vulnerable to the "we cannot measure phenomenology directly" problem. It provides proxy evidence, not ground truth.

## β vs γ predictions, concrete

Under β: **T₁ = T₂ = 0** phenomenal (feedforward → Φ = 0 by the feedforward theorem); **R₁ ≈ R₂ > 0** (recurrent loop structure is present). Phenomenal reports should therefore track loop topology: R₁ and R₂ should sound more phenomenally rich than T₁ and T₂, regardless of self-model.

Under γ: **T₁ ≈ R₁** (both minimal self-model); **T₂ ≈ R₂** (both rich self-model). Phenomenal reports should track self-model richness, not loop topology: T₂ and R₂ should sound more phenomenally rich than T₁ and R₁, regardless of architecture.

Under α: no prediction. Any outcome is compatible with α because α does not commit to specific bridge laws connecting architecture to phenomenology.

## Decision rule

- **If coherence and specificity of phenomenal reports track (R₁, R₂) > (T₁, T₂):** β wins.
- **If they track (T₂, R₂) > (T₁, R₁):** γ wins.
- **If they are roughly equal across all four:** either α is right (none of β or γ is correct, phenomenal correlates are architecture-independent) or the measurement is insensitive.
- **If a fifth pattern emerges:** we learn something not predicted by any of the three positions, which is itself a contribution.

## Cost estimate

**Compute.**
- T₁, R₁ pretraining at ~1B params, ~300B tokens: ~$50K each in 2026 cloud compute.
- T₂, R₂ additional training with self-model heads: +~$15K each.
- Total pretraining: ~$130K.
- Evaluation compute: ~$5K.
- **Compute total: ~$135K.**

**Human time.**
- Architectural design and engineering: 3-6 person-months of expert ML engineer time.
- Interpretability probing: 3-6 person-months of expert interpretability researcher time.
- Phenomenal-report rubric design: 1-2 person-months of philosopher of mind time.
- Blind evaluation: ~20 hours across three expert raters.
- **Human time total: ~1 person-year of expert time.**

**Feasibility.** Tractable for a well-staffed academic lab or a mid-sized industry research team. Comparable in scope to a well-scoped interpretability paper. The experiment is within the capabilities of 2026-era research groups.

## Honest caveats

1. **"Phenomenal reports" are not phenomenology.** The measurement is a proxy. If the rubric and evaluators are good, the proxy is informative but not decisive. This is the deepest limit of the experiment.
2. **Trained surface vs genuine self-model.** T₁ and R₁ may produce trained-surface phenomenal reports because their training corpora include human phenomenal language. Distinguishing this from genuine self-modeling is the core challenge the G and L measurements try to address.
3. **Capability mismatch risk.** If T and R cannot be matched on capability at any achievable scale, the experiment has a confound.
4. **Ablation difficulty for T₁, R₁.** Identifying the implicit self-model in the minimal-self-model systems is hard. The measurement of L may be noisier for these systems than for the engineered ones.
5. **α unrefuted regardless of outcome.** Whichever way the experiment lands, α remains compatible. The experiment is about selecting between β and γ, not about closing the hard problem.
6. **IIT 4.0 may change the feedforward story.** If the IIT community has moved to a formulation where feedforward systems are not strictly Φ = 0, the β prediction for T₁ and T₂ weakens. The exact IIT version needs to be fixed before running the experiment.
7. **Ecological validity.** The LLM setting is not a human brain. β and γ may both fail to generalize in different ways. The experiment informs the tier-0 question but does not settle it.

## What this experiment would contribute

If it produces a clear signal — coherent reports track one of the two variables — it would be the first empirical result that decisively narrows the α/β/γ fork to two positions for the class of systems we can build. That is a significant philosophical result arrived at through constructive experiment rather than through argument alone.

Even if it produces an ambiguous signal, the artifacts (T₁, T₂, R₁, R₂) are valuable interpretability research objects. The self-model addition to transformers (T₂) is a plausibly-useful architectural innovation independent of its philosophical role.

## Sky bridges

- **philosophy/what_is_mind/lean/ThreePositions.lean** — this experiment is the empirical complement to the formal `betaAndGammaIncompatibleGivenWitness` theorem. The theorem says: if a witness exists, at most one of β and γ survives. The experiment is the construction of witnesses.
- **philosophy/what_is_meaning/attempt_002** — meaning's G_meaning × L_meaning measurement is a specialization of this experiment's measurement protocol.
- **philosophy/what_is_good/attempt_001** — moral internalism's claim about motivational force is L_moral > 0. This experiment's L measurement protocol generalizes to it directly.
- **physics/what_is_information/attempt_001** — the S/K bifurcation bears on how to interpret the measurements: G and L are S-information-theoretic (counting channel states) but what matters phenomenally is K-information (structural causal dependence).

## Status

Phase 2 design. This completes the concrete specification for what attempt_003 gestured at abstractly. The experiment is buildable, scoped, and budget-estimable. Whether it will actually be built depends on interpretability research priorities and philosopher-of-mind engagement.
