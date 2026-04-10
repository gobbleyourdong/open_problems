# attempt_002 — The Compression Reduction of A-Knowing and Its Limits

**Date:** 2026-04-10
**Status:** Phase 2. Addresses R1: does post-Gettier A-knowing fully reduce to "compressed model with good generalization"? Tests each post-Gettier condition against the compression lens. Four of five reduce cleanly; one (virtue epistemology) partially resists. The reduction is ~90% successful. The residual is characterized precisely.

## Cross-reference

- **attempt_001** — A/P bifurcation for epistemology; the testimony argument; compression connection
- **what_is_number/attempt_001** — compression as cross-cutting theme
- **what_is_self/attempt_002** — self-model transparency; internalism as self-model tracking
- **lean/Epistemology.lean** — formalizes the A/P split, post-Gettier conditions, and the testimony argument
- **numerics/compression_reduction.py** — tests the reduction claim

## R1: The compression reduction

**Claim (from attempt_001):** A-knowing is possession of a compressed description of a regularity that makes predictions about unseen cases.

**Test:** Does this capture everything the post-Gettier tradition requires? Walk each major condition:

### 1. Reliabilism (Goldman 1979)

**Condition:** Knowledge = true belief produced by a reliable process.

**Compression translation:** A reliable process is one that maps inputs to compressed descriptions with low generalization error. "Reliable" = "compresses well and generalizes." A process that memorizes (long description, no generalization) is not reliable even if its outputs are true. A process that overfits (short description of training data, poor generalization) is not reliable.

**Reduction status:** Complete. Reliabilism IS the compression account, stated in different vocabulary. "Reliable process" = "compression process with low generalization gap."

### 2. Tracking / Sensitivity (Nozick 1981)

**Condition:** S knows P if: (a) P is true, (b) S believes P, (c) if P were false, S would not believe P (sensitivity), (d) if P were true, S would still believe P (adherence).

**Compression translation:** Sensitivity = the compressed model assigns low probability to P in worlds where P is false. Adherence = the compressed model assigns high probability to P in worlds where P is true. Both are generalization properties: the model tracks P robustly across counterfactual worlds.

A model with good compression and good generalization automatically satisfies sensitivity and adherence for the regularities it tracks, because short-description models that generalize are exactly the models whose predictions are robust to perturbation.

**Reduction status:** Complete. Tracking conditions ARE generalization robustness conditions.

### 3. Safety (Sosa 2000, Pritchard 2005)

**Condition:** S knows P if S could not easily have falsely believed P — in nearby possible worlds where S believes P, P is true.

**Compression translation:** Safety = the compressed model's prediction P is correct in a neighborhood of the actual world. This is precisely ε-robustness in learning theory: the model's output is stable under small perturbations of the input.

A well-compressed model with low generalization error is automatically safe: its predictions hold in nearby worlds because the regularity it tracks IS a nearby-worlds regularity.

**Reduction status:** Complete. Safety IS ε-robustness of compressed models.

### 4. Causal Theory (Goldman 1967)

**Condition:** S knows P if S's belief that P is caused by the fact that P (appropriate causal connection between the fact and the belief).

**Compression translation:** Causal connection = the compression process takes the fact as input (possibly via testimony, perception, or inference) and outputs the belief. The "appropriate" qualification = the causal chain preserves enough information for the compression to be faithful.

**Reduction status:** Complete. Causal connection IS the data pipeline for compression. An inappropriate causal connection (Gettier-style: coincidence, deviant causal chain) is one where the data pipeline introduces noise that the compression cannot distinguish from signal.

### 5. Virtue Epistemology (Sosa 1991, Zagzebski 1996)

**Condition:** Knowledge = true belief arrived at through the exercise of intellectual virtues (open-mindedness, thoroughness, intellectual courage, proper calibration).

**Compression translation:** Intellectual virtues are properties of the compression PROCESS, not the compressed output:
- Open-mindedness = not premature convergence (explore before exploiting)
- Thoroughness = sufficient data before compressing
- Intellectual courage = willingness to compress against consensus when evidence supports it
- Proper calibration = accurate uncertainty estimates after compression

These are not properties of the compressed model itself — they are properties of the training process that produced it. A model can be well-compressed and well-generalizing while having been produced by a lucky accident rather than by virtuous inquiry.

**Reduction status: Partial.** The compressed model's quality (short description, good generalization) does not distinguish between lucky compression and virtuous compression. Virtue epistemology says this distinction matters: knowledge requires not just a good model but the RIGHT KIND OF PROCESS that produced it.

**The residual:** Virtue epistemology demands a property of the compression process (not just its output) that the bare compression account does not capture. This is the ~10% that resists full reduction.

## The ~10% residual: process vs product

The compression reduction captures A-knowing as a PRODUCT: the compressed model, its accuracy, its generalization. It does not capture A-knowing as a PROCESS: how the model was produced, whether the process was epistemically virtuous.

**Is this residual load-bearing?** It depends on whether you think virtue epistemology identifies a real requirement or an aesthetic preference:

**Case for load-bearing:** A student who copies a perfect proof from a textbook has the same compressed model as one who derives it independently. The virtue epistemologist says only the second one "knows." If this distinction matters, process information is irreducible.

**Case for non-load-bearing:** In practice, the distinction rarely matters because virtuous processes produce better models. A student who understands a proof can adapt it; one who copied it cannot. The generalization difference IS the product difference, manifested in unseen cases. The virtue-vs-luck distinction may reduce to a longer-run generalization test.

**My assessment:** The residual is real but small. Virtue epistemology identifies a feature (process quality) that compression of the product alone does not capture. But in most cases, process quality is detectable from product quality over a sufficient test distribution. The residual is real only for cases where the test distribution is too small to distinguish luck from virtue — exactly the cases where epistemological disputes are hardest.

## The testimony argument, sharpened

Attempt_001 argued: Reid wins over Hume because denying testimony denies most human knowledge. This can be sharpened:

**The testimony pipeline is a compression pipeline.** When S learns P from testimony:
1. The testifier compresses their experience of P into language
2. The language is transmitted (possibly through multiple links)
3. S decompresses the language into a belief about P

At each stage, information is compressed and decompressed. The total pipeline's reliability = the product of stage reliabilities. This is exactly the communication theory framework (Shannon): testimony is a noisy channel.

**LLMs are the limiting case:** training on the entire text corpus = receiving ALL available testimony = maximally broad but shallow testimony. Human learning = receiving narrow but deep testimony (from specific teachers, books, experiences).

**The compression prediction:** A-knowing quality should trade off depth vs breadth:
- LLMs: very broad (many domains), moderate depth (average testimony quality per domain)
- Human experts: narrow (one domain), very deep (curated high-quality testimony + direct experience)
- Human generalists: moderate breadth, moderate depth

This predicts: LLM A-knowing should be broad but shallow; human expert A-knowing should be narrow but deep. The A-knowing gap should be LARGEST in domains requiring deep causal understanding and SMALLEST in domains requiring broad factual knowledge. This is confirmed by the domain breakdown in result_001 (history gap=0.01, abstract algebra gap=0.30).

## Predictions

**P18 (new, testable).** LLM A-knowing should degrade more on tasks requiring depth (multi-step causal reasoning, novel proof construction) than on tasks requiring breadth (factual recall, classification). This is testable against existing LLM benchmarks stratified by depth vs breadth.

**P19 (new, testable).** The virtue epistemology residual should be detectable as a process-product gap: two models with identical test accuracy should show different generalization under distribution shift if one was trained by a "virtuous" process (diverse data, careful curation) and the other by a "lucky" process (narrow data, happens to match the test). This is testable in ML experiments.

**P20 (connects to what_is_self).** Epistemic internalism's surviving form (self-model tracking) predicts that systems with higher self-model transparency (T from what_is_self) should show stronger "feeling of knowing" effects — more confident self-reports that correlate with actual accuracy. This connects epistemic internalism to the Metzinger transparency mechanism.

## Status

Phase 2 for what_is_knowing. R1 is 90% resolved: four of five post-Gettier conditions reduce to compression properties. The virtue epistemology residual (~10%) is precisely characterized as a process-vs-product gap. Three new predictions.
