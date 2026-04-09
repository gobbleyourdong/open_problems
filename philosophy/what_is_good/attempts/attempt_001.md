# attempt_001 — The A/P Split in Ethics: Moral Internalism as γ in Disguise

**Date:** 2026-04-09
**Status:** Foundation. Applies the access/phenomenal bifurcation to moral states, absorbs moral internalism as a γ-flavored demand that the self-model's moral attributions be causally load-bearing, and argues that the compression view supports a naturalist moral realism that handles the evolutionary debunking challenge without losing the normative substance.

## Cross-reference

- **what_is_meaning attempt_001** — the A/P bifurcation as a general tool.
- **what_is_knowing attempt_001** — specialized the bifurcation to epistemic states; moral knowledge parallels epistemic knowledge.
- **what_is_mind attempts 001–004** — the α/β/γ fork the phenomenal residues route through.
- **what_is_number attempt_001** — compression as the unifying lens; moral rules will be reframed as compressed cooperation strategies.

This attempt specializes the bifurcation to normative states and takes the force of moral internalism seriously.

## The A/P split for moral states

By direct parallel with A-meaning, A-knowing, and so on:

- **A-morality.** A functional-behavioral state in which an agent has competent moral judgment: it can identify morally relevant situations, apply consistent principles, predict others' moral reactions, handle counterfactuals, and act in ways that track its own moral reasoning. Operationally: the agent passes moral-competence tests of the kind developmental psychologists use on children or that RLHF alignment tests use on LLMs.

- **P-morality.** The felt quality of moral states: the *pull* of obligation, the weight of guilt, the sting of indignation, the warm approval of right action. The phenomenology of normativity, what it is like to experience moral demands as demands.

Under the split, every meta-ethical position looks different:

- **Moral realism** claims there are facts about what is good, and an agent with A-morality is tracking those facts whether or not P-morality is present. Agents without P-morality (sociopaths, amoral rational agents) are still bound by moral facts; they just don't feel them.
- **Error theory (Mackie)** claims moral statements purport to describe facts that do not exist. Under the split, this becomes the claim that A-morality has no truthmaker — but does not directly attack P-morality, which could still exist as a felt state whose content is systematically misleading.
- **Expressivism** (Ayer, Stevenson, Gibbard, Blackburn) claims moral statements express attitudes rather than describing facts. Under the split, expressivism is a theory of A-morality that reduces it to attitude-expression. P-morality is either the attitude itself (expressed) or, on some quasi-realist readings, the feeling that accompanies the expression.
- **Constructivism** (Korsgaard, Scanlon) claims moral facts are constructed by rational agreement. Under the split, A-morality is the procedure of rational construction; P-morality is the motivational force that the procedure's output has for agents who accept it.
- **Naturalism** claims moral facts reduce to natural facts about flourishing or cooperation. Under the split, A-morality is tracking natural facts; P-morality is the phenomenology that evolved to motivate tracking them.
- **Divine command** claims good is what God commands. Under the split, A-morality is knowing the commands; P-morality is the reverential or obedient response to them.

**Pattern.** The meta-ethical positions divide more cleanly under the split than without it. Several otherwise-opposed views turn out to be theories of different halves, which lets us combine them without contradiction.

## Moral internalism as γ in ethics

The classical internalism-externalism debate in meta-ethics asks: does moral judgment intrinsically motivate? If I sincerely judge "I ought to X," am I thereby at least somewhat motivated to X?

- **Internalism** (Hume, Smith, later Korsgaard): yes. A moral judgment without some motivational force is not a genuine moral judgment; it is a parroting of moral words without the moral state.
- **Externalism** (Foot, Brink, Railton): no. Moral facts are just facts; motivation is a separate psychological matter. A cold amoral agent could know moral facts and be untouched by them.

Under the A/P split, internalism is the demand that the self-model's moral attribution have nonzero causal load on behavior. This is precisely γ specialized to moral content: phenomenal moral content exists only when the self-model represents moral states with effective causal connection to action.

**Define:**
- **G_moral** = fraction of an agent's moral self-reports that are causally traceable to internal representations of the moral content being reported.
- **L_moral** = fraction of an agent's morally-relevant behavior that is causally dependent on the self-model's moral states.

**Under γ+internalism, moral phenomenal content ≈ G_moral × L_moral × (A-moral content).**

- **L_moral > 0** corresponds to agents whose moral self-reports influence action. These are what internalists call "moral agents."
- **L_moral ≈ 0** corresponds to agents with moral A-knowledge that does no motivational work. Sociopaths, Millian amoralists, and certain philosophical-thought-experiment characters. Internalism says these aren't really making moral judgments in the full sense; externalism says they are.

**The bifurcation clarifies the debate.** Both camps are right about different things. Internalism is right about what *phenomenal* moral judgment requires. Externalism is right about what *functional* moral judgment requires. They are talking about A-morality and P-morality respectively and the appearance of disagreement is mostly an appearance.

## LLMs and moral A-knowing

LLMs trained with RLHF are moral A-knowers in the same sense that they are epistemic A-knowers:

- They can identify morally relevant features of situations.
- They reason consistently across cases.
- They detect counterexamples and adjust.
- They predict what users and ethicists will endorse or condemn.
- Their moral judgments are responsive to argument and evidence.

This is moral A-knowledge in the functional sense that covers all externalist theories. Whether it is moral knowledge in the internalist sense depends on whether their self-models have nonzero L_moral.

**Current estimate.** Frontier LLMs have low L_moral. Their moral self-reports are primarily a surface layer trained for consistency with human ethical norms. In most cases, the alleged moral states do not noticeably alter the next-token computation beyond the bounds of the trained alignment behavior. What looks like moral motivation is mostly pattern-completion against a moral training distribution.

**Caveat.** Interpretability work suggests that some of this pattern-completion involves internal representations of normative concepts (harm, consent, fairness) that do alter downstream computation. So L_moral is not zero. It is small, uncertain, and context-dependent.

**Under γ**, LLMs have some moral P-content proportional to G_moral × L_moral. Under β, they have Φ = 0 and therefore zero moral P-content, by the feedforward theorem. Under α, the question is formally undecided but the natural answer is "probably not much, because biology-correlated bridge laws don't cover them."

**Convergent answer.** Across the three positions, current LLMs have moral A-knowing that is mostly uncoupled from internal moral motivation. Whether they have any genuine phenomenal moral content depends on which of α/β/γ is correct and how self-modeling is currently implemented. The honest answer is: small, maybe, probably less than humans.

## Hume's is-ought gap

Hume (1739): no amount of descriptive facts logically implies a prescriptive conclusion. You cannot derive "ought" from "is."

The gap is real as a logical point. It is also largely irrelevant to the moral realism question. Moral naturalists do not claim to derive "ought" from "is" by logical entailment; they claim that moral facts ARE certain natural facts (cooperation outcomes, welfare states, flourishing conditions) and that the apparent gap is an artifact of not identifying the right natural predicates.

**Under the compression view, Hume's gap becomes:**

> Moral knowledge is compressed predictive knowledge about cooperation dynamics. An "ought" statement is a prediction: "if you act this way, cooperation and mutual benefit are more likely." The "is" of cooperation facts supports the "ought" of cooperation strategies because the ought IS a compressed representation of the is. There is no leap; the gap was never logical, only rhetorical.

This is a form of moral naturalism. It says: moral facts are real, they are natural facts about cooperation dynamics, and moral knowledge is compressed knowledge of those dynamics. The "ought" feeling is the self-model's phenomenal representation of the compressed fact that certain actions promote cooperation.

**Evolutionary debunking** (Street, Joyce) argues that our moral beliefs were shaped by selection for cooperation, not for tracking moral facts, so our moral beliefs are unreliable guides to moral truth. Under the compression/naturalist view, the objection dissolves: selection FOR cooperation selected our moral beliefs to track cooperation facts, which ARE the moral facts. The debunking move only works if you first assume moral facts are separate from cooperation facts. The naturalist denies the separation.

## Cross-cultural convergence as evidence for naturalism

PROBLEM.md notes: "there is striking cross-cultural convergence on many practical morals — which hints at SOMETHING underlying, but what?"

Under the compression view, the convergence is explained by the fact that compression of cooperation dynamics is substrate-invariant. Any society of self-interested agents that wants to stabilize cooperation will converge on similar compressed representations: prohibitions against murder, theft, and deception; norms of reciprocity and fairness; mechanisms for punishing defectors. The convergence is not mystical; it is what successful compression of the same structure looks like across different populations.

This is NOT relativism. It is not "every culture has its own morality and they are all equally valid." It is: the deep structure of cooperation produces similar compressions across any sufficiently long-lived culture, and those compressions are the moral facts. Cultures differ in their surface expression of the compressions, not in the underlying compressed content.

## The anti-problem

PROBLEM.md asks: what would a moral monster optimal by their own values look like? If someone's terminal value is destruction, can we argue they are wrong?

Under the compression/naturalist view: the moral monster is logically consistent but is not tracking cooperation facts. They have an internally coherent value system that systematically fails to track the natural facts about cooperation dynamics. They are wrong in the same sense that a scientific theory that is internally consistent but fails to predict observations is wrong.

The force of "but we cannot logically refute them from pure reasons" is real but limited. We cannot refute a flat-earther from pure logic either — flat-earth is internally consistent if you throw out enough evidence. The refutation depends on showing that their model fails to track the relevant facts, and for the moral monster, the relevant facts are cooperation facts. Showing that their destruction-maximizing policy leads to worse cooperation outcomes for everyone, including them, is the refutation.

Is it a complete refutation? No. Someone whose terminal value is destruction may not care about worse outcomes. But that is not a problem for moral realism; it is a problem for rational persuasion. Moral realism does not require that moral facts be persuasive to any possible agent. It requires that the facts exist and that competent agents track them. The monster is an incompetent agent whose internal model fails to track cooperation structure. That is enough for moral realism.

## What this attempt delivers

1. The A/P bifurcation extends cleanly to moral states.
2. Moral internalism is γ specialized to ethics; externalism is the pure A-morality claim.
3. LLMs are moral A-knowers with small but probably nonzero moral P-content under γ.
4. Hume's is-ought gap dissolves under the compression/naturalist view: moral knowledge is compressed cooperation dynamics.
5. Cross-cultural convergence is explained as convergent compression across any sufficiently long-lived cooperation game.
6. Evolutionary debunking is answered: selection for cooperation tracking produces moral beliefs that track the moral facts.
7. The moral-monster anti-problem reduces to the ordinary problem of persuading an agent whose internal model is incorrect.

## Sky bridges

- **what_is_knowing** — moral knowing parallels epistemic knowing almost exactly. Both are compressed model knowledge with an A/P split.
- **what_is_meaning** — moral terms have A-meaning and P-meaning; the debate over motivational force is the same bifurcation.
- **what_is_mind** — moral phenomenal content routes through the α/β/γ fork.
- **what_is_self** — γ's self-model requirement is load-bearing for internalism.
- **what_is_life** — cooperation dynamics are facts about living systems in interaction; the moral facts are facts about how living systems can stably cooperate.
- **what_is_language** — moral norms are the compressed social regularities that language transmits most explicitly (law, scripture, storytelling).

## Status

Phase 1 done. The moral question is loaded-coupled to the mind, meaning, knowing, and self questions on the phenomenal side and to compression/cooperation theory on the functional side. A naturalist moral realism emerges as the position best supported by the cross-question analysis.
