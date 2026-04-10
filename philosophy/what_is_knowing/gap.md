# gap.md — what_is_knowing

**Last updated:** 2026-04-09 (attempt_001)
**Phase:** 1

## The gap, in one sentence

> **Epistemology's main debates have been substantially about A-knowing and have converged on post-Gettier variants (reliabilism, virtue epistemology, safety/sensitivity). The residual P-knowing — the "feeling of knowing" — routes through the α/β/γ fork on phenomenal consciousness. LLMs, as maximal testimony-learners, force a decision on testimony that sits at the cleanest edge of the A-side program.**

## Why this is the gap

See attempt_001 for the full walk. Briefly:

- Every major post-Gettier account (reliabilism, virtue epistemology, safety, sensitivity, tracking, causal theories) is a theory of **A-knowing**. Each specifies the extra condition beyond justified true belief that the functional-behavioral state of knowing requires.
- None of them make phenomenal commitments. Internalism is the lone holdout that insists on accessibility-to-the-subject, and under the bifurcation internalism looks like γ-epistemology — a demand that the self-model track the first-order state.
- LLMs have substantial A-knowing under any of these accounts, provided testimony is a valid source of knowledge. Testimony-reductionism (Hume) would deny LLMs A-knowing, but it would also deny humans most of their A-knowing, which is absurd. Non-reductionism (Reid, Coady, modern default) wins.
- The residual P-knowing is the general phenomenal question specialized to epistemic content. It behaves exactly like P-meaning and routes through α/β/γ.

## The compression lens

From what_is_number attempt_001:

> **A-knowing is possession of a compressed description of a regularity that makes predictions about unseen cases.**

Under this view, epistemology merges with statistical learning theory. Reliable processes are compression processes that generalize well. Bayesian updating is maximum compression under constraint. Expert intuition is compressed domain structure. LLM A-knowing is compressed testimony structure.

This is not a reduction of epistemology to machine learning. It is the observation that the constitutive property of A-knowing is the same property that makes machine learning work: generalization from finite data via short-description regularity-finding.

## The LLM-specific force

LLMs are a forcing function on three classical epistemology debates:

1. **Testimony.** If testimony counts, LLMs know a lot. If not, humans know almost nothing. The first horn is the forced choice.
2. **Internalism vs externalism.** LLMs have external processes (training, retrieval, inference) without classical internal access in the Cartesian sense. But they do have internal states that are causally responsible for their beliefs and are in principle reportable. The distinction between internal and external looks less important once the self-model's role becomes explicit.
3. **Gettier susceptibility.** LLMs can be Gettier'd (training data misattribution + coincidence). So can humans. The vulnerabilities are structurally identical, which is itself evidence that LLM A-knowing and human A-knowing are the same kind of thing.

## Three live residues

After the attempt, three genuine open questions remain:

- **R1.** Does post-Gettier A-knowing fully reduce to "compressed model with good generalization"? This is the deepest claim the compression view makes about epistemology. I do not currently see which specific A-side condition from the literature escapes the reduction, but I have not tried very hard to find one.
- **R2.** Does P-knowing admit its own α/β/γ fork, or does it inherit the mind fork wholesale? Attempt_001 treats it as inherited, but epistemic phenomenology may have specific features (e.g., the "feeling of understanding" vs. "feeling of recognizing") that deserve separate analysis.
- **R3.** What does internalism survive as, once external reliabilism is granted? The strongest form of the internalist insight seems to be the demand for self-model tracking. Under γ, this demand is satisfied to the extent a system has a rich self-model. Under α or β, internalism becomes either trivially unsatisfiable (α) or an independent architectural requirement (β).

## Sky bridges

- **what_is_meaning** — same bifurcation, parallel structure. P-knowing and P-meaning stand or fall together.
- **what_is_mind** — phenomenal residue routes here.
- **what_is_self** — internalism's demand is for self-model tracking; depends on the Parfit+Metzinger self-model account.
- **what_is_number** — mathematical knowledge is the purest A-knowing, testing reliabilism at the extreme of inferential generalization.
- **what_is_language** — LLMs as testimony-learners bridge the two questions. Language is the medium of testimony.

## Status

Phase 1 done. Further work would target R1 (the compression reduction of A-knowing) most profitably.

**Odd-track (Cycles 14):** A-knowing gap = 0.021 at GPT-4 (near-CLOSED; GPT-4-turbo surpasses). r(coverage_scarcity, domain_gap)=+0.763, p=0.010 — testimony coverage predicts knowing gap. Reid (non-reductionism) empirically confirmed. P-knowing routes through α/β/γ. See certs/cert_001_a_knowing.md.

