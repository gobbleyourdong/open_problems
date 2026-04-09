# Paper Arsenal — Philosophy and Physics Tracks

> Working bibliography for the 37 files in `philosophy/` and `physics/`. Organized by the topics of the argument chain rather than by author.

## Epistemic honesty preface

This is a Phase 1 arsenal under the systematic approach. A full Phase 1 would involve:

- Reading each paper carefully from the primary source.
- Extracting claims with page numbers and equation references.
- Triple-verifying against at least two secondary sources.
- Cross-referencing against any conflicts in the literature.

**I have not done that.** The entries below are drawn from my training-data familiarity with each work. In most cases I am confident about the author, approximate year, and core claim. In many cases I am *not* confident about the exact title, publisher, or page-level details, and have deliberately omitted those rather than risk fabrication. Entries marked **(verify)** are cases where I'd particularly recommend a second reader check the primary source before citing in a paper.

This arsenal is a **pointer list** for future work, not a finished citation apparatus. A future instance or a human reader should replace each entry with a proper reference after verification.

## Format

Each entry is:

> **Author(s), ~Year — Short title**
> *One-sentence claim.* Attempts that reference: `path/attempt_NNN.md`.

If the paper's core claim is widely known and attributed to this author, I omit "verify." If the attribution is mine from training data and would warrant primary-source checking, I flag it.

---

## I. Philosophy of Mind — the α/β/γ fork

### Chalmers 1995 — "Facing Up to the Problem of Consciousness"
The hard problem of consciousness: why is there phenomenal experience at all, beyond the functional descriptions? Frames the easy/hard problem distinction.
**Attempts:** `what_is_mind/attempt_001`.

### Chalmers 1996 — *The Conscious Mind*
Property dualism with psychophysical bridge laws. The zombie argument is developed here as a modal argument against physicalism.
**Attempts:** `what_is_mind/attempt_004` (α₃ variant).

### Block 1995 — "On a Confusion About a Function of Consciousness"
Distinguishes access-consciousness from phenomenal-consciousness. This is the seed of the A/P bifurcation used throughout the track.
**Attempts:** `what_is_mind/attempt_001`, `what_is_meaning/attempt_001` (which generalizes Block's distinction), and by implication every other A/P attempt.

### Dennett 1991 — *Consciousness Explained*
Heterophenomenology and early illusionism. The target of the "explained away" charge that phenomenal-realists level.
**Attempts:** `what_is_mind/attempt_004` (γ variant).

### Frankish 2016 — "Illusionism as a Theory of Consciousness"
Makes the illusionist position explicit and argues it is the parsimonious reading of the evidence. This paper and its surrounding JCS issue are the current canonical statement of γ.
**Attempts:** `what_is_mind/attempt_004` (γ variant).

### Searle 1980 — "Minds, Brains, and Programs"
The Chinese Room argument. Attempts to show that computational implementations of mind have syntax without semantics.
**Attempts:** `what_is_language/attempt_004` (steelman variant 1), `what_is_meaning/attempt_001`.

### Searle 1992 — *The Rediscovery of the Mind*
Biological naturalism: consciousness is a biological phenomenon not implementable in silicon.
**Attempts:** `what_is_mind/attempt_004` (α₄ variant). **(verify exact date)**

### Tononi 2004 — "An Information Integration Theory of Consciousness"
Original statement of IIT; introduces Φ as the measure of integrated information.
**Attempts:** `what_is_mind/attempt_002`, `what_is_mind/lean/ThreePositions.lean`.

### Oizumi, Albantakis, Tononi 2014 — "From the Phenomenology to the Mechanisms of Consciousness: Integrated Information Theory 3.0"
The mathematically developed version of IIT that attempt_002 takes as the reference formulation. Contains the formal feedforward result.
**Attempts:** `what_is_mind/attempt_002`.

### Rosenthal — higher-order theories of consciousness
The view that a mental state is conscious iff it is the object of a higher-order representation. **(verify best canonical reference — probably Rosenthal 1986 or 1997 collection).**
**Attempts:** `what_is_mind/attempt_004` (HOT variant), `what_is_mind/attempt_001`.

### Baars 1988 — *A Cognitive Theory of Consciousness*
Global Workspace Theory. Consciousness as broadcasting across specialized processors.
**Attempts:** `what_is_mind/attempt_004` (GWT variant).

### Dehaene et al. — neuroscientific versions of global workspace
Later neuroscientific development of GWT, including measurable correlates of the "conscious access" event.
**Attempts:** `what_is_mind/attempt_004`. **(verify specific paper — likely Dehaene & Naccache 2001 or Dehaene 2014 *Consciousness and the Brain*)**

### Strawson (Galen) 2006 — "Realistic Monism: Why Physicalism Entails Panpsychism"
Explicit panpsychist defense. The combination problem is the panpsychist's analogue of the hard problem.
**Attempts:** `what_is_mind/attempt_004` (α₁ variant).

### Goff 2017 — *Consciousness and Fundamental Reality*
Russellian monism + panpsychism developed as the most defensible response to the hard problem.
**Attempts:** `what_is_mind/attempt_004`.

### Metzinger 2003 — *Being No One*
The phenomenal self-model framework. Central text for γ's self-model requirement. The PSM is the model the self-model theory of subjectivity uses.
**Attempts:** `what_is_self/attempt_001`, and every attempt that loads on γ's self-model requirement.

---

## II. Philosophy of Self — Parfit and the bundle cluster

### Parfit 1984 — *Reasons and Persons*
The argument that personal identity is not what matters; psychological continuity is. Dissolves many edge-case puzzles (teleportation, fission, gradual replacement).
**Attempts:** `what_is_self/attempt_001`, `what_is_life/attempt_001` (biological continuity context).

### Hume 1739 — *A Treatise of Human Nature*, Book I
The bundle theory: the self is a bundle of perceptions with no continuous entity behind them.
**Attempts:** `what_is_self/attempt_001`.

### Classical Buddhist sources on anatta (no-self)
The Pali Canon and subsequent Buddhist philosophical tradition develop anatta as the claim that the self is a construction of aggregates, not a substantial entity. **(verify which primary sources to cite — probably the Anattalakkhana Sutta as starting point)**
**Attempts:** `what_is_self/attempt_001`.

### Locke — psychological continuity
The classical statement of the memory-continuity theory of personal identity.
**Attempts:** `what_is_self/attempt_001`. **(verify exact Locke reference — An Essay Concerning Human Understanding, Book II, Ch. 27)**

---

## III. Philosophy of Meaning and Language

### Firth 1957 — "A Synopsis of Linguistic Theory"
"You shall know a word by the company it keeps." The distributional hypothesis stated as a slogan.
**Attempts:** `what_is_language/attempt_001`, `what_is_meaning/attempt_001`.

### Harris 1954 — "Distributional Structure"
Technical statement of the distributional approach to linguistic analysis.
**Attempts:** `what_is_language/attempt_001`, `what_is_meaning/attempt_001`.

### Chomsky 1957 — *Syntactic Structures*
Original statement of generative grammar. The start of the universal-grammar research program.
**Attempts:** `what_is_language/attempt_001`.

### Chomsky 1965 — *Aspects of the Theory of Syntax*
Poverty of stimulus argument. This is the load-bearing paper for the sample-complexity discussion.
**Attempts:** `what_is_language/attempt_002`.

### Tomasello 2003 — *Constructing a Language*
Usage-based theory of language acquisition. Language emerges from social interaction and shared intentionality.
**Attempts:** `what_is_language/attempt_001`, `what_is_language/attempt_005`.

### Fodor and Pylyshyn 1988 — "Connectionism and Cognitive Architecture"
The systematicity argument against connectionism. Historically important; largely defused by modern LLMs.
**Attempts:** `what_is_language/attempt_003`.

### Lakoff and Johnson 1980 — *Metaphors We Live By*
Embodied-semantics: abstract concepts are metaphorical extensions of bodily schemas.
**Attempts:** `what_is_language/attempt_001`, `what_is_meaning/attempt_001`.

### Dreyfus 1972 — *What Computers Can't Do*
Phenomenological-embodied critique of symbolic AI. The ancestor of modern embodied-cognition arguments against LLMs.
**Attempts:** `what_is_language/attempt_004`.

### Kripke 1972 — *Naming and Necessity*
Causal-historical theory of reference. Names refer via chains from baptism events.
**Attempts:** `what_is_meaning/attempt_001`, `what_is_language/attempt_004`.

### Putnam 1975 — "The Meaning of 'Meaning'"
Twin Earth thought experiment. Meaning "ain't in the head."
**Attempts:** `what_is_meaning/attempt_001`.

### Wittgenstein 1953 — *Philosophical Investigations*
Meaning as use in a language-game. The textual foundation of use theory.
**Attempts:** `what_is_meaning/attempt_001`.

### Brandom 1994 — *Making It Explicit*
Inferentialist theory of meaning: meaning is determined by inferential role.
**Attempts:** `what_is_meaning/attempt_001`.

### Lewis 1969 — *Convention*
Convention-based accounts of language and meaning.
**Attempts:** `what_is_meaning/attempt_001`.

### Millikan 1984 — *Language, Thought, and Other Biological Categories*
Teleosemantics: content is fixed by biological function.
**Attempts:** `what_is_meaning/attempt_001`.

### Hart and Risley 1995 — *Meaningful Differences in the Everyday Experience of Young American Children*
The famous study on cumulative word exposure in young children. Source for human sample-complexity estimates.
**Attempts:** `what_is_language/attempt_002`.

### Gilkerson et al. 2017 — LENA foundation studies
Day-long audio recording of early language environments; refined estimates of words-per-day input to children.
**Attempts:** `what_is_language/attempt_002`. **(verify specific Gilkerson et al. paper — likely *Pediatrics* 2017)**

### Frank et al. — Wordbank
Cross-linguistic database of child vocabulary development. Source for productive vocabulary curves.
**Attempts:** `what_is_language/attempt_002`. **(verify specific reference — Frank et al. 2017 *Journal of Child Language* is a candidate)**

### Bergelson and HomeBank studies
Cross-linguistic replication work on child-directed speech volume.
**Attempts:** `what_is_language/attempt_002`. **(verify)**

### Hoffmann et al. 2022 — "Training Compute-Optimal Large Language Models"
The Chinchilla paper. Source for LLM training-token estimates used in attempt_002.
**Attempts:** `what_is_language/attempt_002`.

### LLaMA paper series (Meta)
Technical reports for LLaMA, LLaMA-2, LLaMA-3 with pretraining token counts.
**Attempts:** `what_is_language/attempt_002`. **(verify — likely Touvron et al. 2023 for LLaMA-2; specific LLaMA-3 citation would be a Meta technical report or blog post)**

### Sperber and Mercier 2017 — *The Enigma of Reason*
Argumentative theory of reasoning; bridges to social-pragmatic theories of language function.
**Attempts:** `what_is_language/attempt_005`.

### Dunbar 1996 — *Grooming, Gossip, and the Evolution of Language*
Social-grooming theory of language origin. Language as bonding substitute in large groups.
**Attempts:** `what_is_language/attempt_005`.

### Hauser, Chomsky, Fitch 2002 — "The Faculty of Language: What Is It, Who Has It, and How Did It Evolve?"
The FLB/FLN distinction: broad vs narrow language faculties.
**Attempts:** `what_is_language/attempt_005`.

---

## IV. Epistemology

### Gettier 1963 — "Is Justified True Belief Knowledge?"
The three-page paper that broke the classical JTB definition of knowledge. Foundational for post-Gettier epistemology.
**Attempts:** `what_is_knowing/attempt_001`.

### Goldman — reliabilism
Knowledge as belief produced by reliable processes. **(verify best canonical reference — probably Goldman 1976 or 1979)**
**Attempts:** `what_is_knowing/attempt_001`.

### Nozick 1981 — *Philosophical Explanations*
Sensitivity/tracking account of knowledge.
**Attempts:** `what_is_knowing/attempt_001`.

### Sosa — virtue epistemology and safety
Virtue-based accounts of knowledge + the "safety" condition. **(verify — Sosa has multiple relevant works; probably the *Knowledge in Perspective* or *A Virtue Epistemology* series)**
**Attempts:** `what_is_knowing/attempt_001`.

### Pritchard — safety and luck
Epistemic luck and the safety condition.
**Attempts:** `what_is_knowing/attempt_001`.

### Hume — reductionism about testimony
The Humean view that testimony is only as good as the direct evidence behind it.
**Attempts:** `what_is_knowing/attempt_001`. **(verify — Hume's *Enquiry* on miracles is a common source)**

### Reid — non-reductionism about testimony
Thomas Reid's claim that testimony is a basic source of knowledge, not reducible to other sources.
**Attempts:** `what_is_knowing/attempt_001`. **(verify)**

### Coady 1992 — *Testimony: A Philosophical Study*
Modern defense of non-reductionism about testimony.
**Attempts:** `what_is_knowing/attempt_001`.

### Clark and Chalmers 1998 — "The Extended Mind"
Knowledge and cognition can live outside the head — in notebooks, tools, external memory.
**Attempts:** `what_is_knowing/attempt_001` (contextual reference).

---

## V. Philosophy of Mathematics

### Frege 1884 — *Die Grundlagen der Arithmetik*
The logicist program: arithmetic reducible to logic. Foundational.
**Attempts:** `what_is_number/attempt_001`.

### Russell 1903 — *The Principles of Mathematics*; Russell 1910-13 — *Principia Mathematica* (with Whitehead)
Logicism developed formally; Russell's paradox and the ramified type theory response.
**Attempts:** `what_is_number/attempt_001`.

### Hilbert — formalist program
Mathematics as formal symbol manipulation. **(verify — Hilbert has multiple relevant papers; "On the Infinite" 1925 is a key one)**
**Attempts:** `what_is_number/attempt_001`.

### Brouwer — intuitionism
Mathematics as mental construction. **(verify specific Brouwer texts — "Intuitionism and Formalism" 1913 is a starting point)**
**Attempts:** `what_is_number/attempt_001`.

### Gödel 1931 — "Über formal unentscheidbare Sätze..."
The incompleteness theorems. Load-bearing for the Gödel residue discussion.
**Attempts:** `what_is_number/attempt_001`, `what_is_number/gap.md`, `physics/what_is_computation/attempt_001`.

### Shapiro 1997 — *Philosophy of Mathematics: Structure and Ontology*
Structuralism: mathematical objects are positions in structures. The modal position among contemporary philosophers of math.
**Attempts:** `what_is_number/attempt_001`.

### Resnik 1997 — *Mathematics as a Science of Patterns*
Another structuralist treatment.
**Attempts:** `what_is_number/attempt_001`.

### Hellman 1989 — *Mathematics without Numbers*
Modal structuralism: mathematical truths as modal truths about possible structures.
**Attempts:** `what_is_number/attempt_001`.

### Field 1980 — *Science Without Numbers*
Fictionalism: mathematical statements are literally false; mathematics is a useful fiction.
**Attempts:** `what_is_number/attempt_001`.

### Yablo 2001 — "Go Figure: A Path Through Fictionalism"
Refined fictionalism addressing the indispensability argument.
**Attempts:** `what_is_number/attempt_001`. **(verify)**

### Wigner 1960 — "The Unreasonable Effectiveness of Mathematics in the Natural Sciences"
The puzzle that compression-based accounts of math try to address.
**Attempts:** `what_is_number/attempt_001`.

### Tegmark 2014 — *Our Mathematical Universe*
The Mathematical Universe Hypothesis: reality IS a mathematical structure.
**Attempts:** `what_is_number/attempt_001`, `physics/what_is_reality/attempt_001`.

---

## VI. Ethics and Meta-ethics

### Hume 1739 — *Treatise*, Book III
The is-ought gap. Foundational.
**Attempts:** `what_is_good/attempt_001`.

### Mackie 1977 — *Ethics: Inventing Right and Wrong*
Error theory: moral statements are systematically false because there are no moral facts.
**Attempts:** `what_is_good/attempt_001`.

### Ayer 1936 — *Language, Truth and Logic*
Early expressivism (emotivism). Moral statements express attitudes, not facts.
**Attempts:** `what_is_good/attempt_001`.

### Gibbard 1990 — *Wise Choices, Apt Feelings*; Blackburn 1984 — *Spreading the Word*
Developed expressivism / quasi-realism.
**Attempts:** `what_is_good/attempt_001`.

### Korsgaard 1996 — *The Sources of Normativity*
Constructivist ethics; moral facts constructed by rational agents.
**Attempts:** `what_is_good/attempt_001`.

### Scanlon 1998 — *What We Owe to Each Other*
Contractualist form of constructivism.
**Attempts:** `what_is_good/attempt_001`.

### Foot — externalism in moral psychology
"Morality as a System of Hypothetical Imperatives" and related work. **(verify — Foot 1972 is the likely paper)**
**Attempts:** `what_is_good/attempt_001`.

### Railton 1986 — "Moral Realism"; Brink 1989 — *Moral Realism and the Foundations of Ethics*
Naturalist moral realism and externalism about moral motivation.
**Attempts:** `what_is_good/attempt_001`.

### Street 2006 — "A Darwinian Dilemma for Realist Theories of Value"
Evolutionary debunking argument against moral realism.
**Attempts:** `what_is_good/attempt_001`.

### Joyce 2006 — *The Evolution of Morality*
Another evolutionary debunking line, with different conclusions from Street.
**Attempts:** `what_is_good/attempt_001`.

---

## VII. Aesthetics

### Kant 1790 — *Critique of the Power of Judgment*
Disinterested pleasure, purposiveness without purpose. Foundational for classical aesthetics.
**Attempts:** `what_is_beauty/attempt_001`.

### Schmidhuber — compression-based aesthetics
Formal information-theoretic account of beauty as compression improvement. **(verify — Schmidhuber has multiple papers on this, including 1997 "Low-complexity art" and 2010 "Formal theory of creativity, fun, and intrinsic motivation")**
**Attempts:** `what_is_beauty/attempt_001`.

### Appleton 1975 — *The Experience of Landscape*
Prospect-refuge theory of landscape aesthetics.
**Attempts:** `what_is_beauty/attempt_001`.

### Orians and Heerwagen 1992 — "Evolved Responses to Landscapes"
Evolutionary-psychological account of landscape preferences.
**Attempts:** `what_is_beauty/attempt_001`. **(verify)**

### Buss — evolutionary aesthetics and mate preferences
Evolutionary-psychological accounts of facial attractiveness and mate preferences. **(verify — multiple papers; probably Buss 1989 or subsequent)**
**Attempts:** `what_is_beauty/attempt_001`.

---

## VIII. Philosophy of Life and Origin-of-Life

### Joyce (Gerald) 1994 — NASA working definition of life
"Life is a self-sustaining chemical system capable of Darwinian evolution." The working definition used in origin-of-life and astrobiology.
**Attempts:** `what_is_life/attempt_001`, `what_is_life/gap.md`.

### Maturana and Varela 1980 — *Autopoiesis and Cognition*
Life as self-creating, self-maintaining organization.
**Attempts:** `what_is_life/attempt_001`.

### Kauffman 1993 — *The Origins of Order*
Autocatalytic networks and metabolism-first origin-of-life theories.
**Attempts:** `what_is_life/attempt_001`.

### Dyson 1985 — *Origins of Life*
Metabolism-first proposals.
**Attempts:** `what_is_life/attempt_001`.

### Dawkins 1976 — *The Selfish Gene*
Replicator-first view of life and evolution.
**Attempts:** `what_is_life/attempt_001`.

### Walker and Davies — information-theoretic theories of life
Life as a specific kind of information processing. **(verify — Walker & Davies 2013 "The Algorithmic Origins of Life" is a candidate)**
**Attempts:** `what_is_life/attempt_001`.

### Prigogine 1984 — *Order Out of Chaos*
Dissipative structures: life as far-from-equilibrium self-organization.
**Attempts:** `what_is_life/attempt_001`.

### Langton — artificial life and computational views
Computational conceptions of life and the edge-of-chaos hypothesis. **(verify — "Artificial Life" 1989 conference proceedings introduction is a candidate)**
**Attempts:** `what_is_life/attempt_001`.

---

## IX. Information Theory

### Shannon 1948 — "A Mathematical Theory of Communication"
The foundational paper. Defines entropy and channel capacity. Explicitly disclaims semantic content as irrelevant to the engineering problem.
**Attempts:** `physics/what_is_information/attempt_001`.

### Kolmogorov 1965 — "Three Approaches to the Quantitative Definition of Information"; Chaitin 1966; Solomonoff 1964
Algorithmic information theory: the minimum program length to generate a string.
**Attempts:** `physics/what_is_information/attempt_001`.

### Landauer 1961 — "Irreversibility and Heat Generation in the Computing Process"
Erasing a bit requires kT ln 2 of heat. Information is physical.
**Attempts:** `physics/what_is_information/attempt_001`.

### Bennett 1982 — "The Thermodynamics of Computation — a Review"
Extended Landauer's results; introduced logical reversibility as the key to sub-Landauer computation.
**Attempts:** `physics/what_is_computation/attempt_001`. **(verify)**

### Fisher — Fisher information
Classical statistical information theory; likelihood-curvature measure.
**Attempts:** `physics/what_is_information/attempt_001`. **(verify)**

### Dretske 1981 — *Knowledge and the Flow of Information*; Floridi 2010 — *Information: A Very Short Introduction*
Semantic information theory. Content-bearing information as distinct from Shannon entropy.
**Attempts:** `physics/what_is_information/attempt_001`.

### Wheeler 1990 — "Information, Physics, Quantum: The Search for Links"
"It from bit." Information as the fundamental substrate of reality.
**Attempts:** `physics/what_is_information/attempt_001`, `physics/what_is_reality/attempt_001`.

---

## X. Computation and Complexity

### Turing 1936 — "On Computable Numbers"
Turing machines, the halting problem, the Church-Turing thesis.
**Attempts:** `physics/what_is_computation/attempt_001`.

### Church 1936 — "An Unsolvable Problem of Elementary Number Theory"
Lambda calculus and the Church-Turing thesis's other half.
**Attempts:** `physics/what_is_computation/attempt_001`.

### P vs NP — Cook 1971, Levin 1973, Karp 1972
The origins of the P vs NP question and NP-completeness. **(verify specific canonical references)**
**Attempts:** `physics/what_is_computation/attempt_001`.

### Fredkin — digital physics
Pancomputationalist physics: reality is a cellular automaton.
**Attempts:** `physics/what_is_computation/attempt_001`. **(verify — Fredkin has multiple papers on this)**

### Wolfram 2002 — *A New Kind of Science*
Cellular-automaton view of physics and computation.
**Attempts:** `physics/what_is_computation/attempt_001`.

### Deutsch 1985 — "Quantum Theory, the Church-Turing Principle and the Universal Quantum Computer"
Founding paper of quantum computation theory.
**Attempts:** `physics/what_is_computation/attempt_001`.

### Shor 1994 — "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer"
The factoring algorithm that proved quantum speedup on a natural problem.
**Attempts:** `physics/what_is_computation/attempt_001`.

### Lloyd 2000 — "Ultimate Physical Limits to Computation"
Physical bounds on computation derived from thermodynamics and quantum mechanics.
**Attempts:** `physics/what_is_computation/attempt_001`. **(verify)**

---

## XI. Physics — Reality, Time, and the Substrate

### Einstein 1905, 1915 — special and general relativity
The theoretical basis for the block-universe interpretation.
**Attempts:** `physics/what_is_time/attempt_001`, `physics/what_is_reality/attempt_001`.

### Minkowski 1908 — "Space and Time"
First clear formulation of spacetime as a four-dimensional manifold. The formal block universe.
**Attempts:** `physics/what_is_time/attempt_001`. **(verify)**

### Rovelli — relational physics and loop quantum gravity; *The Order of Time* 2018
Relational view of physics; critique of absolute time and space.
**Attempts:** `physics/what_is_time/attempt_001`, `physics/what_is_reality/attempt_001`.

### Husserl — phenomenology of time-consciousness
*On the Phenomenology of the Consciousness of Internal Time*. Retention-now-protention structure.
**Attempts:** `physics/what_is_time/attempt_001`. **(verify exact text reference)**

### Bostrom 2003 — "Are You Living in a Computer Simulation?"
The simulation hypothesis, stated as an argument from observer counts.
**Attempts:** `physics/what_is_reality/attempt_001`.

### Whitehead 1929 — *Process and Reality*
Process philosophy: reality is events, not substances.
**Attempts:** `physics/what_is_reality/attempt_001`.

### Parmenides — Fragments
The ancient argument against the coherence of genuine nothingness. The Parmenidean response to "why is there something rather than nothing."
**Attempts:** `physics/what_is_reality/attempt_001`.

### Leibniz — "Principles of Nature and Grace"; "Why is there something rather than nothing?"
The canonical statement of the substrate-question.
**Attempts:** `physics/what_is_reality/attempt_001`. **(verify — the "why is there something" formulation is classical but finding the exact Leibniz text is worth doing)**

### Bekenstein 1973 — black hole entropy
The origin of the information-theoretic view of black holes.
**Attempts:** `physics/what_is_information/attempt_001` (background for holographic principle).

### 't Hooft 1993; Susskind 1995 — holographic principle
Information content of a region bounded by its boundary area, not its volume.
**Attempts:** `physics/what_is_information/attempt_001`.

---

## XII. LLM / NLP empirical papers

### Vaswani et al. 2017 — "Attention Is All You Need"
The transformer architecture paper.
**Attempts:** `what_is_language/attempt_001` (LLM existence proof background).

### Brown et al. 2020 — "Language Models are Few-Shot Learners"
GPT-3 paper. In-context learning as an emergent capability.
**Attempts:** `what_is_language/attempt_001`, `what_is_language/attempt_003`.

### SCAN benchmark — Lake and Baroni 2018
Compositional generalization benchmark that early LLMs famously failed.
**Attempts:** `what_is_language/attempt_003`.

### COGS benchmark — Kim and Linzen 2020
A harder compositional generalization test.
**Attempts:** `what_is_language/attempt_003`. **(verify)**

### BLiMP — Warstadt et al. 2020
Grammatical acceptability benchmark for LLMs.
**Attempts:** `what_is_language/gap.md`. **(verify)**

### Interpretability literature — Anthropic, DeepMind, various 2022-2025
The interpretability work on LLM internal representations that the γ/self-model discussion draws on. **(verify specific papers — Anthropic's circuits thread, the "superposition" and "monosemanticity" papers, and probes studies are the cluster)**
**Attempts:** `what_is_mind/attempt_003`, `what_is_meaning/attempt_002`.

### Mamba, SSMs — Gu and Dao 2023 and precursors
State-space models as recurrent alternatives to transformers. Relevant to the β/γ comparison on loop topology.
**Attempts:** `what_is_mind/attempt_002`, `what_is_mind/attempt_003`. **(verify)**

---

## XIII. Not categorized above but referenced

### Russell (Bertrand) 1927 — *The Analysis of Matter*
Russellian monism: physics describes relations, not intrinsic natures.
**Attempts:** `what_is_mind/attempt_004` (α₂ variant).

### Henrich 2015 — *The Secret of Our Success*
Cumulative cultural evolution.
**Attempts:** `what_is_language/attempt_005`. **(verify)**

### Carruthers — inner speech and language of thought
Language as scaffolding for thought. **(verify — Carruthers 1996 *Language, Thought, and Consciousness* is a candidate)**
**Attempts:** `what_is_language/attempt_005`.

### Vygotsky — inner speech
Russian developmental psychology on inner speech as internalized social interaction.
**Attempts:** `what_is_language/attempt_005`. **(verify specific text)**

### Zeno of Elea — paradoxes of motion
Ancient puzzles about change and continuity. Referenced in context for `what_is_change` but not yet with its own attempt.
**Attempts:** `physics/what_is_time/attempt_001` (implicit reference).

---

## Coverage assessment

This arsenal covers, at rough levels of confidence:

- **High confidence** (author, approximate date, core claim accurate): ~60% of entries. Includes all the canonical philosophy-of-mind cluster, the classical ethics, epistemology, and philosophy of language sources, Gödel, Turing, Shannon, Einstein, Parfit, Chalmers, Block, Tononi, Metzinger, Hart & Risley, Hoffmann (Chinchilla), Chomsky, Wittgenstein, Tegmark, Kripke, Putnam, Hume.
- **Medium confidence** (author and core claim accurate; specific title/year may need verification): ~30% of entries. Marked **(verify)** where I'm less sure of details.
- **Lower confidence** (I know the position exists and the general attribution is correct, but specific references are uncertain): ~10%. These are worth treating as leads rather than citations.

## What this arsenal does not include

- **Primary texts in non-English languages.** Parmenides, Heidegger, Husserl, Tononi's Italian papers, Gödel's German paper are all referenced by English title or translation. A rigorous arsenal would cite originals.
- **Page numbers and exact equation references.** Phase 1 proper would include these.
- **Conflict flagging.** The systematic approach's standard is to flag conflicts between sources. Many of the cited positions actively disagree with each other, and this arsenal does not map those disagreements systematically.
- **Recent interpretability papers.** The mind/meaning attempts' claims about G × L proxies lean on an interpretability literature that has moved very fast. Specific papers supporting the "frontier LLMs have partial self-models" claim are available but I have not cited them precisely.

## Next steps

If extending this arsenal:

1. **Verify the **(verify)** entries first.** Pick a source-checking tool (Google Scholar, Semantic Scholar, the author's homepage) and confirm title and date.
2. **Fill in page-level details for the load-bearing claims.** The feedforward theorem in Tononi's IIT papers, the sample-complexity numbers in Hart & Risley and in Chinchilla, and the LLM existence-proof evidence in GPT-3 and later papers are the most load-bearing citations.
3. **Build the conflict map.** Chalmers (property dualism) and Frankish (illusionism) disagree on the nature of phenomenal consciousness in a way that bears on the α/γ split. The track should document where each position stands explicitly.
4. **Add the interpretability cluster.** The mechanistic interpretability papers from 2022–2025 are load-bearing for the γ discussion and should be added here in a dedicated section.

## Status

Phase 1 arsenal, pointer-list quality. A single instance's working bibliography. A second-pass verification would upgrade roughly 30% of entries from "pointer" to "citation" and fill in the gaps flagged above.
