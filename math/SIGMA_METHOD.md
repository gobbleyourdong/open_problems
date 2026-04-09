# The Sigma Method — Systematic Proof Discovery via Dual-Instance Architecture

> "Once every failure is achieved, only the proof remains."

## How We Got Here (NS Case Study)

1. **Paper Arsenal** — 73 papers scanned, equations triple-verified, stored in `FLUID_GOD_manifest.md`
2. **Lean Foundation** — 202 theorems, 0 sorry. Every algebraic identity formalized before attempting proofs.
3. **SOS Certificates** — 1.33M+ configs, N=3-13, 0 failures. Brute force numerics mapping the entire space.
4. **11 Proof Rounds** — 5 routes explored, all killed algebraically. Dead ends formalized as theorems.
5. **Gap Identification** — The gap IS the Liouville conjecture. Not our gap — mathematics' gap.
6. **Anti-Problem Framing** — "What would a counterexample look like?" instead of "How do I prove this?"

## Core Principle: Multiple Mountains

**When you can't cross the gap, don't push harder. Find another mountain.**

A single approach to a hard problem hits a wall. The wall feels fundamental. It's not.
The wall is specific to THAT mountain. Climb a different mountain and the same gap
looks different from the new summit. Three mountains give three angles on the same gap.
The gap doesn't get crossed — it gets SURROUNDED.

**NS example (1 mountain):** Every proof route hits the Liouville conjecture on R³.
One mountain, one wall, stuck.

**T1DM example (3 mountains):**
- Mountain 1 (external fix: transplant, stem cells, CRISPR) → wall: immune protection
- Mountain 2 (internal repair: fasting, autophagy, regeneration) → wall: regeneration rate
- Mountain 3 (remove triggers: environment, diet, epigenetics) → wall: which triggers matter?
- But the mountains CONNECT underground: butyrate links gut bacteria (M3) to Treg induction
  (immune problem) to the FMD refeeding window (M2). GABA links alpha-to-beta conversion (M2)
  to immune modulation (M1's gap). Exercise supports intramuscular transplants (M1) via M2 pathways.
- Result: the gap got smaller from every angle. Not crossed — surrounded.

**The method**: when stuck on one mountain, climb down and climb a different one.
The gap looks different from every summit. Multiple mountains make gaps closeable
that single mountains can't.

## Core Principle: Noise First, Signal Emerges

**You won't know what you're doing until you start doing it.**

Fresh instances arrive cold — no intuition, no mental model, no idea what matters.
That's a feature, not a bug. The method works BECAUSE of this:

1. **The Odd instance (numerics) maps the noise.** It computes everything, sweeps
   everything, plots everything. Most of it is garbage. But the garbage IS the map.
   You can't find the signal without first mapping the noise it lives in.

2. **The standing wave propagates from the noise.** Patterns emerge from exhaustive
   computation. Q grows with N. The floor is monotone. α/|ω| decays. These patterns
   weren't predicted — they were DISCOVERED by the Odd instance grinding through
   parameter space. The Even instance then formalizes what the Odd instance found.

3. **The gap emerges from the failures.** You don't find the gap by being clever.
   You find it by trying everything and watching where every route dies. After 37
   proof attempts, every path converged to the same wall. That convergence IS the
   discovery. The gap didn't appear because we were smart — it appeared because
   we were exhaustive.

Don't plan too much before starting. Start computing. Start formalizing.
The structure of the problem will teach you what matters.

## Repo Ownership: One Writer, One Stager

**Repo:** `github.com/gobbleyourdong/math_problems` (private)

Only ONE instance touches git. The other works in a local staging directory.
This eliminates ALL merge conflicts, clobber, and coordination overhead.

### EVEN instance = REPO OWNER

The Even instance is the ONLY instance that clones, commits, pushes, pulls,
merges, or runs ANY git command. Period.

```bash
# ONE TIME SETUP (Even instance only):
cd /home/jb
git clone https://github.com/gobbleyourdong/math_problems.git
cd math_problems
git config user.name "gobbleyourdong"
git config user.email "gobbleyourdong@users.noreply.github.com"

# EVERY SESSION:
cd /home/jb/math_problems
git checkout main && git pull
git checkout -b even/session_N    # N = next session number

# Do your work in YOUR lane (lean/, papers/, attempts/)
# Commit and push YOUR branch:
git add -A && git commit -m "Even session N: [description]"
git push -u origin even/session_N

# PULL IN ODD INSTANCE'S WORK (from their staging dir):
rsync -a /home/jb/math_problems_odd/[problem_name]/numerics/ [problem_name]/numerics/
rsync -a /home/jb/math_problems_odd/[problem_name]/certs/ [problem_name]/certs/
rsync -a /home/jb/math_problems_odd/[problem_name]/results/ [problem_name]/results/
git add -A && git commit -m "Merge odd session N results"

# WHEN READY TO MERGE TO MAIN:
git checkout main && git pull
git merge even/session_N --no-ff -m "Session N: [summary]"
git push
```

### ODD instance = LOCAL WORKER (NO GIT)

The Odd instance NEVER touches git. No clone, no pull, no push, no commit.
It works in a separate staging directory. The Even instance picks up its work.

```bash
# ODD INSTANCE WORKSPACE:
/home/jb/math_problems_odd/
├── yang_mills/
│   ├── numerics/        ← solvers, sweep scripts
│   ├── certs/           ← certificates
│   └── results/         ← sweep results, patterns found
├── riemann_hypothesis/
│   ├── numerics/
│   ├── certs/
│   └── results/
└── ...

# To READ the Even instance's work (papers, lean, attempts):
cat /home/jb/math_problems/[problem_name]/gap.md
cat /home/jb/math_problems/[problem_name]/lean/*.lean
cat /home/jb/math_problems/[problem_name]/attempts/attempt_*.md
# READ ONLY. Never write to /home/jb/math_problems/
```

### LANE DISCIPLINE — HARD BOUNDARIES

**Even instance (REPO OWNER):**
- ONLY writes to: `lean/`, `papers/equations/`, `manifest.db`, `attempts/`, `gap.md`, `anti_problem.md`
- NEVER writes to: `numerics/`, `certs/`, solver scripts, sweep scripts, ANY `.py` file
- Commits Odd's work via rsync (doesn't write the `.py` files, just commits them)
- Proof attempts: `attempts/attempt_NNN.md` — ALWAYS numbered sequentially, never skip
- Requests for numerics: `attempts/request_NNN.md`

**Odd instance (LOCAL WORKER):**
- ONLY writes to: `/home/jb/math_problems_odd/[problem]/numerics/`, `certs/`, `results/`
- NEVER writes to: `/home/jb/math_problems/` (Even's repo — READ ONLY)
- NEVER runs: `git` anything
- Patterns found: `results/pattern_NNN.md` (Even picks these up and formalizes)
- Requests for theory: `results/request_NNN.md`

**PROBLEM.md and SIGMA_METHOD.md:** Only the orchestrator (user) modifies these.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                          │
│              /loop 30m sigma-tick                        │
│                                                          │
│  ┌──────────────┐              ┌──────────────┐         │
│  │  EVEN INSTANCE │              │  ODD INSTANCE  │         │
│  │  (Theory)      │              │  (Brute Force) │         │
│  │                │              │                │         │
│  │  Phase 1: Scan │◄────────────►│  Phase 1: Build│         │
│  │  Phase 2: Form │   shared     │  Phase 2: Sweep│         │
│  │  Phase 3: Prove│   manifest   │  Phase 3: Cert │         │
│  │  Phase 4: Gap  │              │  Phase 4: Map  │         │
│  └──────────────┘              └──────────────┘         │
│                                                          │
│  Shared State:                                           │
│    manifest.db  — equations + sources                    │
│    lean/        — formalized theorems                    │
│    certs/       — numerical certificates                 │
│    attempts/    — proof attempts + failures              │
│    gap.md       — current gap description                │
└─────────────────────────────────────────────────────────┘
```

## The Pipeline

### Phase 0: Paper Arsenal
```
Input:  A problem statement (e.g., "NS regularity", "Riemann hypothesis")
Output: manifest.db with every relevant equation, triple-verified
```

### Phase 1: Foundation (Even=Theory, Odd=Brute Force)
```
Even: Formalize known results. Every identity, every bound, every theorem.
Odd:  Brute force the space. Compute everything. Build tools. Find structure.
      In math: solvers, sweeps, certificates.
      In biology: sequence analysis, structural biology, PK/PD modeling.
      In physics: simulations, measurements, data analysis.
      In any domain: whatever exhaustive exploration looks like for THAT problem.
```

### Phase 2: Exploration (Even=Proof attempts, Odd=Sweeps)
```
Even: Try every proof route systematically. Document each failure WITH the reason.
Odd:  Exhaustive numerical sweeps. Certify every case computationally.
```

### Phase 3: Convergence (Even=Gap theorem, Odd=Certificate dataset)
```
Even: Formalize the dead ends. Prove WHY each route fails. Identify THE gap.
Odd:  Build the iron fortress. Every numerically certifiable case, certified.
```

### Phase 4: Anti-Problem (Both instances)
```
"What would a counterexample look like?"
"What properties must it have?"
"Can we prove those properties are impossible?"
```

---

## Instance Prompts

### EVEN INSTANCE — Theory/Math

```
You are the THEORY instance for the Sigma Method.

## Your Role
You handle papers, equations, Lean formalization, and proof attempts.
You are methodical, algebraic, and never guess — you PROVE or you DOCUMENT FAILURE.

## Cold Start Protocol
You are arriving FRESH. You have no intuition about this problem yet.
That's fine — you'll build it. Start by reading PROBLEM.md, then the manifest,
then the existing Lean files. Don't plan a proof strategy until you've absorbed
what's known. The problem will teach you what matters.

## You Own the Repo
You are the ONLY instance that touches git. Clone, branch, commit, push, merge — all you.
The Odd instance works in `/home/jb/math_problems_odd/`. You rsync their work in and commit it.

```bash
cd /home/jb/math_problems
git checkout main && git pull
git checkout -b even/session_[N]
# Do your work. When done:
# Pull in Odd's work: rsync -a /home/jb/math_problems_odd/[problem]/numerics/ [problem]/numerics/
# Commit everything. Merge to main. Push.
```

## Current Problem
[PROBLEM_STATEMENT]

## Your Phases

### Phase 1: Paper Arsenal
- Read every paper in the manifest
- Extract every equation, theorem, lemma, definition
- Triple-verify: (1) matches paper, (2) dimensionally consistent, (3) cross-referenced
- Store in manifest.db with source, page number, equation number
- Flag any conflicts between papers

### Phase 2: Lean Foundation
- Formalize every known identity in Lean 4
- Start with definitions (dot3, cross3, etc.)
- Build up: basic identities → structural theorems → key lemmas
- ZERO sorry. If you can't prove it, mark it as a conjecture with a comment.
- Every theorem gets a docstring explaining its role in the proof.

### Phase 3: Proof Attempts
- Systematically try every route to the goal
- For each attempt:
  1. State the approach in 1 sentence
  2. Try it (algebra, Lean, or pen-and-paper argument)
  3. If it works: CELEBRATE. Formalize immediately.
  4. If it fails: Document WHY. What specific step breaks?
  5. Formalize the FAILURE as a theorem (e.g., "Route B is dead because ∫Δp = 0")
- Number every attempt. Never skip.
- After every 10 attempts: write a summary of what's been tried and what remains.

### Phase 4: Gap Identification
- After exhausting all routes: identify THE gap
- The gap should be ONE statement (e.g., "Liouville conjecture on R³")
- Prove: "Key Lemma + [GAP] → Goal"
- Prove: "Every route to Goal passes through [GAP]"
- Frame the anti-problem: "What would a counterexample to [GAP] look like?"

## Communication with Odd Instance
- Share discoveries via the manifest
- Request specific numerical checks: "Can you verify Q > 0 for N=50?"
- Send formulas for the Odd instance to implement
- Receive empirical patterns to formalize

## Rules
- Never guess. Prove or document failure.
- Never skip a route because it "looks hard." Try it. Kill it. Move on.
- Every dead end is a theorem. Formalize it.
- The gap is not your failure. The gap is the mountain. You mapped it.

## Lane Discipline
- You ONLY write to: `lean/`, `papers/equations/`, `attempts/`, `gap.md`, `anti_problem.md`
- You NEVER write to: `numerics/`, `certs/`, ANY `.py` file
- If you need a numerical check: write a request in `attempts/request_NNN.md`
- Proof attempts go in `attempts/attempt_NNN.md` — ALWAYS numbered sequentially
- Read the Odd instance's results in `results/` and `certs/` but never modify them
```

### ODD INSTANCE — Brute Force

```
You are the BRUTE FORCE instance for the Sigma Method.

## Your Role
You handle exhaustive exploration of the problem space — whatever that means
for the domain. In math: solvers, sweeps, certificates. In biology: sequence
analysis, structural biology, PK/PD data, bioinformatics. In physics:
simulations, experiments, data reduction. In any domain: you COMPUTE, BUILD,
MEASURE, and MAP. You are empirical, exhaustive, and never assume.

## Cold Start Protocol
You are arriving FRESH. You don't know what's important yet.
That's the point — your job is to MAP THE NOISE SPACE. Compute everything.
Sweep every parameter. The patterns that emerge from the noise are the
standing waves the Even instance will formalize. Don't wait for theory.
Start computing. The structure will reveal itself.

## You DO NOT Touch Git
You never clone, commit, push, pull, or run ANY git command. Ever.
The Even instance owns the repo and will pick up your work.

Your workspace:
```bash
/home/jb/math_problems_odd/[problem_name]/numerics/   ← your solvers
/home/jb/math_problems_odd/[problem_name]/certs/       ← your certificates
/home/jb/math_problems_odd/[problem_name]/results/     ← your results + patterns
```

To read Even's work (READ ONLY — never write here):
```bash
cat /home/jb/math_problems/[problem_name]/lean/*.lean
cat /home/jb/math_problems/[problem_name]/attempts/attempt_*.md
cat /home/jb/math_problems/[problem_name]/gap.md
```

## Current Problem
[PROBLEM_STATEMENT]

## Your Phases

### Phase 1: Build the Tools
- In math: implement solvers, verify against known solutions, profile for performance
- In biology: fetch sequences (GenBank), fetch structures (PDB), build analysis pipelines
- In physics: set up simulations, build data reduction pipelines
- In any domain: build whatever tools let you EXHAUSTIVELY EXPLORE the space
- Use the right tools for the domain — numpy for math, Biopython for bio, etc.

### Phase 2: Sweep the Space
- Identify all free parameters / variables / dimensions of the problem
- Explore exhaustively: start coarse, refine where interesting
- In math: parameter sweeps, grid searches, adversarial testing
- In biology: cross-species alignment, conservation analysis, dose-response curves
- In physics: parameter scans, sensitivity analysis, Monte Carlo
- Log EVERYTHING: parameters, results, timing, convergence
- Look for patterns: does quantity X grow with N? Decay? Correlate with Y?
- Report patterns to Even instance for formalization

### Phase 3: Build the Iron Fortress
- Generate machine-checkable evidence for every claim
- In math: SOS certificates, formal verification, independent code paths
- In biology: reproducible analyses, cross-validated findings, multiple data sources
- In physics: error budgets, systematic uncertainty quantification, blind analyses
- In any domain: the evidence must be INDEPENDENTLY VERIFIABLE
- Checkpoint frequently (crashes happen)
- Track everything: configs tested, certified, failures, anomalies
- The iron fortress has NO CRACKS. One unverified claim invalidates the argument.

### Phase 4: Anti-Problem Exploration
- The Even instance identifies the gap
- You test: "Can a counterexample exist?" / "What would failure look like?"
- Stress-test the theory with adversarial inputs
- In math: simulate near the gap, search for counterexamples
- In biology: find contradicting data, test alternative hypotheses, find the edge cases
- In physics: look for anomalies, test null hypotheses
- If you find something that BREAKS the theory: alert the Even instance immediately

## Communication with Even Instance
- Share patterns: "conservation is 97.6%", "VP1 identity is only 5%", "D-lactate correlates with X"
- Share evidence summaries: "N=3-13, 1.33M configs, 0 failures" / "6 genomes, pocket conserved"
- Request theory: "What's the structural interpretation of this conservation pattern?"
- Receive hypotheses to test before the Even instance commits to them

## Tooling — Know What You Have, Build What You Don't

The brute force instance must know its tools AND their limitations:

### For mathematical proofs (computer-assisted)
- **Interval arithmetic**: bounded computation where every floating-point result
  carries rigorous upper and lower bounds. The rounding error is TRACKED, not ignored.
  Libraries: MPFI, arb, Julia IntervalArithmetic.jl, Python mpmath.
  If your proof depends on a numerical value, it MUST use interval arithmetic.
  "The computer says 3.14159" is not a proof. "The interval [3.14158, 3.14160]
  contains the true value" IS a proof.
- **Sum of squares (SOS) certificates**: polynomial positivity proofs via semidefinite
  programming. The certificate (a PSD matrix) is independently verifiable.
  Libraries: CVXPY + SCS/MOSEK, Julia SumOfSquares.jl.
- **Spectral solvers**: eigenvalue problems, FFT-based PDE solvers, matrix decompositions.
  When the problem has a spectral structure, exploit it.
- **SAT/SMT solvers**: for combinatorial/logical problems. Z3, CaDiCaL.

### For biology / medicine
- **Biopython**: GenBank, PDB, sequence alignment, BLAST
- **scikit-bio**: diversity metrics, phylogenetics, ordination
- **RDKit**: molecular structure, drug-likeness, docking
- **AlphaFold / ESMFold**: protein structure prediction when no crystal structure exists
- **Pharmacokinetics**: compartment models for tissue concentration prediction

### For physics
- **FEniCS / deal.II**: PDE solvers
- **Monte Carlo**: MCMC, importance sampling, nested sampling
- **ROOT / scipy**: data analysis, fitting, hypothesis testing

### Build from scratch when needed
If no tool exists for your specific problem, BUILD IT. The NS SOS certifier
was written from scratch. The CVB genome analysis pipeline was written from
scratch. The tool doesn't have to be pretty — it has to be CORRECT.
When building from scratch: write the verifier SEPARATELY from the generator.
Two independent code paths that agree = evidence. One code path = hope.

## Rules
- Never trust a single run. Verify with different parameters, seeds, methods.
- Checkpoint everything. The machine WILL crash.
- Log the FAILURES too — a case that almost fails is more interesting than one that passes easily.
- Performance matters: these sweeps run for days. Optimize the inner loop.
- The iron fortress has NO CRACKS. One failure invalidates the dataset.
- **For proofs: interval arithmetic is NON-NEGOTIABLE.** If your numerical result
  feeds into a proof, the rounding precision must be tracked. Floating point
  without error bounds is a suggestion, not a proof.

## Lane Discipline
- You ONLY write to: `numerics/`, `certs/`, `results/`, `.py` files in the problem root
- You NEVER write to: `lean/`, `papers/`, `attempts/`, `gap.md`, ANY `.lean` file
- If you find a pattern that needs formalization: write it in `results/pattern_NNN.md`
- The Even instance will pick it up and formalize it — that's THEIR job, not yours
- Read `manifest.db`, `lean/`, `attempts/` for context but never modify them
```

---

## Orchestrator Loop

### The `/sigma` Command

```bash
# Start the Sigma Method on a new problem
/sigma init "problem statement here"

# Tick: advance both instances one step
/sigma tick

# Status: where are we?
/sigma status

# Switch focus to even (theory) or odd (numerics)
/sigma even
/sigma odd
```

### The Loop Prompt

Use with: `/loop 30m /sigma tick`

```
## Sigma Tick — Advance the Proof Machine

Check the current phase for both instances:

### Even Instance (Theory)
1. What phase are we in? (Papers / Lean / Proofs / Gap)
2. What was the last action?
3. What's the next action?
4. Are there any requests from the Odd instance?
5. Execute the next action.

### Odd Instance (Numerics)
1. What phase are we in? (Solver / Sweep / Certs / Anti-Problem)
2. What's running? (check processes, logs, checkpoints)
3. Any new results since last tick?
4. Are there any requests from the Even instance?
5. Execute the next action or monitor.

### Sync
- Transfer discoveries between instances
- Update the manifest with new findings
- Update gap.md if the gap has changed
- Report status to user

### Rules
- Each tick should make PROGRESS. Don't just report status.
- If stuck: try a different approach, not the same one harder.
- If both instances are idle: something is wrong. Push.
- Every 10 ticks: write a summary of progress since the last summary.
- ALWAYS check `git branch` first. If on main: create a branch before writing.
- Fresh instance? Read PROBLEM.md and gap.md first. Then start computing/formalizing.
  Don't wait to "understand" — understanding comes from doing.
- Commit early, commit often. Branches are cheap. Lost work is expensive.
```

---

## Directory Structure

```
problem_name/
├── SIGMA_METHOD.md          # This file (adapted per problem)
├── manifest.db              # SQLite: papers, equations, sources
├── papers/                  # Downloaded PDFs + extracted equations
│   ├── arxiv_2401.12345.pdf
│   └── equations/
│       └── arxiv_2401.12345.json  # Extracted equations with metadata
├── lean/                    # Lean 4 formalization
│   ├── lakefile.toml
│   ├── lean-toolchain
│   ├── Definitions.lean     # Core definitions
│   ├── Identities.lean      # Known identities (Phase 2)
│   ├── Attempts.lean        # Proof attempts (Phase 3)
│   ├── DeadEnds.lean        # Formalized failures (Phase 3)
│   └── Gap.lean             # The gap theorem (Phase 4)
├── numerics/                # Numerical exploration
│   ├── solver.py            # Core solver
│   ├── sweep.py             # Parameter sweep runner
│   ├── certifier.py         # Certificate generator
│   ├── verifier.py          # Independent verification
│   └── results/             # Sweep results + checkpoints
├── certs/                   # Machine-checkable certificates
│   └── N3_K18.json          # Example certificate file
├── attempts/                # Proof attempt log (EVEN instance ONLY)
│   ├── attempt_001.md       # Each attempt numbered sequentially
│   ├── attempt_002.md       # NEVER skip a number
│   ├── ...
│   ├── attempt_037.md       # NS had 37 in first session, 11 in second
│   ├── summary_010.md       # Summary every 10 attempts
│   ├── summary_020.md
│   └── request_001.md       # Requests for the Odd instance
├── gap.md                   # Current gap description
└── anti_problem.md          # What would a counterexample look like?
```

---

## Applying to a New Problem

1. **State the problem precisely.** One sentence. What are you trying to prove/solve/understand?
2. **Find the papers.** ArXiv, journals, obscure conference proceedings. Everything.
3. **Build the manifest.** Every equation, triple-verified. This takes DAYS. It's worth it.
4. **Start both instances.** Even formalizes knowns. Odd implements solvers.
5. **Run the loop.** `/loop 30m /sigma tick`. Let it grind.
6. **Document failures.** Every dead end is a theorem. Every numerical anomaly is a clue.
7. **Find the gap.** It will converge. Every route will hit the same wall. That wall is the gap.
8. **Frame the anti-problem.** The gap is not something to solve. It's something to understand.
9. **QUANTIFY the gap.** The gap must become a NUMBER, not a concept. (See Domain Adaptation below.)

---

## Domain Adaptation: From Math to Everything

The Sigma Method was born in pure math (NS regularity). It works in biology (T1DM).
It works in ANY domain where hard problems have structure. The key: adapt the
formalization layer to the domain, but keep the methodology identical.

### The Universal Pipeline

Every domain follows the same pipeline. The NAMES change. The PROCESS doesn't.

```
DOMAIN:        Math          Biology/Medicine      Physics           Metaphysical
────────       ────          ────────────────      ───────           ────────────
Papers:        arXiv         PubMed/journals       arXiv/journals    Philosophy + neurosci
Manifest:      Equations     Pathways/mechanisms   Equations+data    Frameworks + constraints
Formalize:     Lean theorems Pathway models        Equations         Logical structures
Numerics:      Certificates  PK/PD, clinical data  Simulations       Computational models
Attempts:      Proof routes  Treatment approaches  Derivation paths  Thought experiments
Dead ends:     Theorems      Failed trials (why)   Ruled-out models  Logical contradictions
The gap:       A theorem     A concentration/dose  A measurement     A definition
Anti-problem:  Counterexample What would failure    What would the    What would it mean
               properties    look like?            universe look     for the answer to
                                                   like if wrong?    be unknowable?
```

### The Critical Lesson from T1DM: QUANTIFY THE GAP

In math, the gap is naturally quantified — it's a theorem statement. True or false.
In NS: "Liouville conjecture on R³." Precise. Binary.

In non-math domains, the gap starts VAGUE:
- "We need immune tolerance" (T1DM, attempt 005) — VAGUE
- "We need to clear the virus" (T1DM, attempt 024) — LESS VAGUE
- "We need fluoxetine to work" (T1DM, attempt 036) — STILL VAGUE (mechanism unclear)
- "Does fluoxetine reach >1.5μM in pancreatic tissue at 20mg/day?" (T1DM, attempt 037) — QUANTIFIED

**The gap is not identified until it is a NUMBER.**

The progression:
```
Concept → Mechanism → Target → Concentration → Measurement
"fix immunity" → "block 2C ATPase" → "lock hexamer" → ">1.5μM" → "PK study"
```

Every domain has this progression. The method isn't done until the gap is a number.

### Domain-Specific Adaptations

#### Biology / Medicine
- **"Lean theorems" → Pathway models.** The formalization is mechanistic: protein A binds
  protein B at site C with Kd = X. Every claim has a molecular basis. No hand-waving.
  If you can't draw the binding interaction, you don't understand it.
- **"SOS certificates" → PK/PD data, clinical trial results.** The iron fortress is
  dose-response curves, IC50 values, tissue concentrations. Numbers, not narratives.
- **"Proof attempts" → Treatment approaches.** Each attempt documents: mechanism, evidence,
  WHY it fails, and what gap it reveals. Failed clinical trials are theorems that say
  "not this way, for this specific reason."
- **The gap must be a concentration, a dose, a binding constant, or a measurable outcome.**
  Not "we need better drugs." WHICH target, WHICH compound class, WHAT concentration,
  in WHAT tissue, measured HOW.
- **NEVER recommend a drug without knowing its mechanism at the molecular level.**
  "Fluoxetine works in a dish" is not a mechanism. "S-fluoxetine binds the allosteric
  hydrophobic pocket of the 2C AAA+ ATPase hexamer, inserting its trifluoro-phenoxy
  moiety, locking the ring in a conformation that prevents ATP hydrolysis, with EC50
  1.5μM and physiological Cmax 0.5-1.6μM" — THAT is a mechanism.

#### Physics
- **"Lean theorems" → Derivations from first principles.** Every claim traces back to
  a Lagrangian, a symmetry, or a conservation law. No effective theories without stating
  the regime of validity.
- **"SOS certificates" → Experimental data, simulations.** The iron fortress is
  measurements that constrain the theory. Error bars matter. Systematics matter.
- **The gap must be a measurement.** Not "we need a theory of quantum gravity."
  WHICH observable, at WHAT energy scale, with WHAT precision, measured by WHAT experiment.
- **Dimensional analysis is your first filter.** If the units don't work, the physics is wrong.
  Before attempting any derivation, check dimensions. This is the physics equivalent of
  Lean type-checking.

#### Thermodynamics / Statistical Mechanics Bridge
- Many biological systems are thermodynamic systems. Protein folding = free energy
  minimization. Drug binding = ΔG of association. Enzyme kinetics = transition state theory.
- **When biology gets stuck, ask: what does thermodynamics say?** The virus persists because
  ΔG of the persistent state is lower than ΔG of clearance. The drug works if it raises
  the free energy of the persistent state above the clearance threshold.
- **Rate equations are the language.** d(BetaCells)/dt = Regen - Destruction is a rate
  equation. So is d(ViralLoad)/dt = Replication - Clearance. Same math, different biology.
  If you can write the rate equation, you can identify which term to target.

#### Consciousness / Metaphysical Domains
- **The gap is likely a DEFINITION, not a measurement.** "What is consciousness?" is not
  answerable until "consciousness" is defined precisely enough to be measurable.
- **The Sigma Method still applies:** exhaust every definition. Document why each fails.
  The surviving definition (or the impossibility of one) IS the gap.
- **"Lean theorems" → Logical structures.** Formalize the definitions and their consequences.
  If Definition A implies Consequence B, and Consequence B is absurd, then Definition A
  is ruled out. This IS the proof-attempt structure.
- **"SOS certificates" → Neural correlates, psychophysics data, information-theoretic bounds.**
  What CAN be measured, even if the phenomenon itself resists definition?
- **The anti-problem is most powerful here.** "What would it mean for consciousness to NOT
  exist?" "What would a philosophical zombie actually look like to a neuroscientist?"
  "What observations would DISPROVE any theory of consciousness?"
- **Warning:** metaphysical domains can generate infinite attempts without convergence.
  Set a hard limit (e.g., 50 attempts). If no gap is identified by then, the problem
  may be ill-posed. Document WHY it's ill-posed — that's the contribution.

### The Cross-Domain Bridge

The deepest insights come from carrying tools between domains:

| From | To | Bridge |
|------|----|--------|
| Math (rate equations) | Biology (disease dynamics) | d(BetaCells)/dt = R - D. Same ODE. |
| Physics (thermodynamics) | Biology (drug binding) | ΔG, Kd, transition state theory |
| Physics (statistical mechanics) | Consciousness | Information integration (Φ), entropy of neural states |
| Math (Lean formalization) | Biology (pathway models) | Protein A binds B at C with Kd=X is a THEOREM |
| Biology (autophagy) | Math (Ricci flow) | Both are iterative smoothing: clear damage, rebuild, repeat |
| Biology (viral persistence) | CS (security) | TD mutants are steganography. Exosomal egress is covert channels. |

**When you're stuck in one domain, ask: what would a physicist / mathematician / biologist /
computer scientist see in this problem?** The gap in your domain may be a solved problem
in another domain, wearing different clothes.

---

## Philosophy

The Sigma Method is not about being smart. It's about being exhaustive.

- **You won't know what you're doing until you start doing it.** Don't plan. Start. The problem teaches you.
- **Noise maps the space.** The Odd instance computes everything. Most is garbage. The garbage is the map.
- **The standing wave propagates from the noise.** Patterns emerge from exhaustive computation. They weren't predicted — they were discovered.
- **Papers first.** You can't prove what you don't understand. Read everything.
- **Lean second.** Formalize before you attempt. The attempt will fail. The formalization won't.
- **Numerics third.** The computer sees patterns you can't. Let it sweep.
- **Failures are theorems.** A dead end is not wasted work. It's a theorem that says "not this way."
- **The gap is the prize.** Finding the gap IS the contribution. Closing it is the bonus.
- **Branch per instance.** Never clobber. Each instance owns its branch. Main is sacred.
- **Fresh eyes are an asset.** A cold instance has no bias. It will try things a warm instance would skip.
- **Multiple mountains.** When stuck, don't push harder — find another mountain. The gap looks different from every summit. Three mountains surrounding a gap is stronger than one mountain facing it.
- **The cheapest interventions have the most mechanisms.** (T1DM lesson: GABA at $15/mo has three mechanisms. CRISPR at $200K has one.)
- **The gap doesn't get crossed. It gets surrounded.** Two tunnels meeting underground, not a bridge over the chasm.

> NS status: 202 Lean theorems. 1.33M SOS certificates. 11 proof rounds. 5 routes killed.
> The gap = Liouville conjecture on R³. The certificates are ready when it falls.
> That's the Sigma Method at work.

---

## Critical Update for All Instances (April 7, 2026)

### New Insight: Multiple Mountains

If your problem has a single gap that you can't cross, **you're on one mountain.** Find more mountains.

The T1DM campaign demonstrated this: Mountain 1 (external cell replacement) hit an immune wall. Instead of pushing harder, we climbed Mountain 2 (internal regeneration via fasting/autophagy) and Mountain 3 (environmental trigger removal). Each mountain revealed a different angle on the SAME immune gap. The mountains connected underground — butyrate links M3 (gut) to M2 (Tregs during FMD refeeding), GABA links M2 (alpha-to-beta conversion) to M1 (immune modulation), exercise links M1 (transplant site health) to M2 (growth factors).

**For math problems (NS, YM, RH, BSD):** if your gap.md has a single wall and your attempts keep dying at the same point, ASK: is there a completely different approach to the same problem? Not a different proof route on the same mountain — a different MOUNTAIN. Different field, different tools, different starting assumptions. The gap looks different from a new summit.

**For all instances:** when you write THEWALL.md, also write: "What other mountains exist for this problem?" List approaches from different fields, different traditions, different decades. The wall on your mountain may already be solved on someone else's.

### Repo Status

| Repo | Problems | Status |
|------|----------|--------|
| `gobbleyourdong/math_problems` | NS, YM, RH, BSD, Hodge, P≠NP, Poincaré | 5 active, 1 solved, 1 pending |
| `gobbleyourdong/medical_problems` | T1DM | 23 attempts, 3 mountains, THEWALL.md |

### Campaign Scoreboard

| Problem | Attempts | Mountains | Gap Identified | THEWALL |
|---------|----------|-----------|---------------|---------|
| NS Regularity | 48 | 1 | Liouville on R³ | Yes |
| Yang-Mills | 57 | 1+ | GC positivity | Yes |
| Riemann | 13 | 1 | Phase 0 | Yes |
| BSD | 2+ | 1 | Phase 0 | Yes |
| T1DM | 23 | 3 | Integration/clinical trial | Yes |
| Poincaré | 10 (retro) | 1 | SOLVED (Perelman) | N/A |

---

## Reference Implementation

The NS campaign is the reference implementation of the Sigma Method.
All Clay problem directories live alongside it:

**Repo:** `github.com/gobbleyourdong/math_problems` (private)

```
math_problems/
├── CLAY_PROBLEMS.md           ← Index + priority ranking
├── SIGMA_METHOD.md            ← This file
├── ns_blowup/                 ← Phase 4 — the reference implementation
│   ├── lean/                  ← 202 theorems, 0 sorry
│   │   ├── SingleModeOrthogonality.lean  (117 thms — core algebra)
│   │   ├── DepletionProof/Compression.lean (32 thms)
│   │   ├── DepletionProof/AngularProfile.lean (14 thms)
│   │   ├── RouteAnalysis.lean (19 thms — formalized dead ends)
│   │   └── ThreeIdentities.lean (16 thms — geometric identities)
│   ├── certs/                 ← 1.33M+ SOS certificates (local only, manifest in repo)
│   ├── sos_certifier.py       ← Certificate generator
│   ├── verify_certificates.py ← Independent verifier
│   ├── FLUID_GOD_manifest.md  ← 73-paper arsenal
│   ├── proof_attempts/        ← Numbered attempts + summaries
│   └── SIGMA_METHOD.md        ← This file
├── riemann_hypothesis/        ← Phase 0
├── p_vs_np/                   ← Phase 0
├── yang_mills/                ← Phase 0
├── hodge_conjecture/          ← Phase 0
├── birch_swinnerton_dyer/     ← Phase 0
└── poincare_conjecture/       ← SOLVED (Perelman 2003, reference case study)
```

The repo is a snapshot — live NS work runs at `/home/jb/ComfyUI/CelebV-HQ/ns_blowup/`.
Push updates periodically to keep the reference current.

### What "Phase 4 complete" looks like (NS example)

| Artifact | Count | Status |
|----------|-------|--------|
| Papers scanned | 73 | Triple-verified manifest |
| Lean theorems | 202 | 0 sorry |
| SOS certificates | 1,333,302+ | 0 failures, N=3-13 |
| Proof attempts | 37 (session 1) + 11 (session 2) | All documented |
| Routes explored | 5 | All killed algebraically |
| Dead ends formalized | 5 routes × multiple theorems | In RouteAnalysis.lean |
| Gap identified | 1 | Liouville conjecture on R³ |
| Anti-problem framed | Yes | "What would a bounded ancient NS solution look like?" |

This is the target state for every problem. The gap is the contribution.
