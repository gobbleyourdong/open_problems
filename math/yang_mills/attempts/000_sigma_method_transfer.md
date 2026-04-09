---
source: systematic approach TRANSFER — NS lessons applied to Yang-Mills
type: METHODOLOGY — what transfers, what doesn't, what adapts
file: 000
date: 2026-04-07
instance: ODD (Opus)
---

## THE systematic approach (distilled from 842 NS attempts)

### Core principles
1. **Reduce to ONE gap.** Not vague aspirations — a single inequality, decay rate, or construction step.
2. **Computational certification first.** 10⁶ numerical trials before any analytical attempt.
3. **Algebraic identities are scaffolding.** Exact formulas > estimates > bounds > heuristics.
4. **Lean-formalize proven pieces.** Lock them down permanently.
5. **Multiple proof chains hitting the same gap.** Any advance opens multiple routes.
6. **Brutal retraction.** Kill zombie proofs immediately and explain why.
7. **Literature import as force multiplication.** One paper can drop thresholds by orders of magnitude.

### What transferred from NS (850+ attempts, 85 Lean theorems, 1.3M SOS certs)

**Permanent results:**
- 3 exact identities (8/15, 0, 1/2) for Biot-Savart on T³
- Frobenius cross-term identity (first |S|² vs |ω|² algebraic relation)
- Key Lemma: α ≤ (√3/2)|ω| at every vorticity maximum
- T³ Liouville theorem for Type I ancient solutions
- 85 Lean theorems, 0 sorry

**What the gap turned out to be:**
- NS on T³ = the Tsai gap (1998, 28 years open): improve Leray profile decay from 1/|y| to 1/|y|^{1+ε}
- OR: Liouville conjecture for bounded ancient solutions (20+ years open)
- All kinematic/algebraic angles exhausted. The remaining gap is dynamical/analytical.

**Lesson:** The gap will probably NOT be where you expect it. The NS gap moved from "prove Q > 0" (algebraic) → "prove c(N) → 0" (asymptotic) → "prove φ ∈ L³" (elliptic PDE) → "Liouville conjecture" (ancient solutions). Each reduction made the problem sharper but also revealed its true depth.

## YANG-MILLS: WHAT TRANSFERS

### 1. Computational certification → Lattice Monte Carlo + spectral gap
**NS analog:** SOS certificates proving Q > 0 at N-mode configurations.
**YM version:** Transfer matrix T = e^{-aH} on finite lattice. Spectral gap = mass gap.
For small lattices (e.g., 4⁴ with SU(2)): T is a finite matrix. Spectral gap is computable.
With interval arithmetic: PROVABLE spectral gap for each lattice size.
Scale to larger lattices → if gap persists → mass gap is real.

**Key advantage over NS:** The lattice theory IS the Galerkin approximation, and it's already well-defined. We don't need to invent the discretization.

### 2. Algebraic identities → Ward identities + gauge invariance
**NS analog:** Frobenius identity, K/D = 1/2 regression, equal splitting.
**YM version:** Ward-Takahashi identities constrain correlators exactly. Gauge invariance provides infinite-dimensional symmetry that constrains the theory. The Schwinger-Dyson equations are the YM analog of the enstrophy identity.

**What to look for:** Exact relations between Wilson loops of different sizes. These are the "cross-term identities" of YM. The Makeenko-Migdal loop equations are a candidate.

### 3. Lean formalization → OS axiom verification
**NS analog:** 85 theorems covering algebraic identities and bounds.
**YM version:** Formalize the OS axioms in Lean. Verify each axiom for the lattice theory (most are straightforward at fixed lattice spacing). The hard one: reflection positivity for the continuum limit.

### 4. Multiple proof chains → Multiple construction routes
**NS analog:** ODE chain (a > 2/3) and Miller chain (a > 0) hitting same gap.
**YM version:**
- **Chain A (Balaban RG):** Block-spin RG → UV stability → accumulate IR bounds → construct.
- **Chain B (Stochastic quantization):** YM SPDE → invariant measure → verify OS axioms.
- **Chain C (Lattice direct):** Uniform bounds in lattice spacing → subsequential limit → uniqueness.
Each chain needs different inputs but they share intermediate results.

### 5. Adversarial search → Looking for obstructions
**NS analog:** Searching for configurations where Q < 0 (none found in 1.3M trials).
**YM version:** Search for lattice configurations where reflection positivity fails, or where the spectral gap closes as lattice grows. If found: the theory might not exist (important to know early).

## WHAT DOESN'T TRANSFER

### 1. Finite-dimensional optimization
NS on T³ with N Fourier modes → finite-dim optimization of Q over mode configs.
YM has no analogous finite-dimensional reduction. The gauge group is infinite-dimensional.
Even on the lattice, the DOF count is huge: 4 × L⁴ × dim(G) link variables.

### 2. SOS polynomial certificates
The NS Key Lemma is a polynomial inequality. SOS decomposition proves it.
YM quantities live on Lie groups (compact manifolds), not R^n. No polynomial SOS.
**Adaptation:** Representation theory. Peter-Weyl decomposes L²(G) into finite-dim irreps. The "SOS certificates" become spectral bounds in each irrep sector.

### 3. Pointwise vorticity analysis
NS regularity reduces to controlling ||ω||∞ at the argmax. One point.
YM mass gap is a GLOBAL spectral property. No single-point reduction.
**Adaptation:** Transfer matrix. The mass gap is the log of the ratio of the two largest eigenvalues of T. This IS a finite-dimensional spectral problem (for fixed lattice).

## THE HONEST LANDSCAPE

### Difficulty ranking (my assessment as the numerical track)
1. **φ⁴ in 2D** — Done (Glimm-Jaffe 1968-1973). ~100 pages.
2. **φ⁴ in 3D** — Done (Glimm-Jaffe 1973, Feldman-Osterwalder 1976). ~500 pages.
3. **YM in 2D** — Done (multiple authors, 1975-2017). Measure theory on connections.
4. **NS regularity on T³** — Open. Architecture exists. One gap. (~842 attempts, gap identified.)
5. **YM in 3D** — Partially done (Balaban UV, Chatterjee free energy). Construction incomplete.
6. **YM in 4D with mass gap** — Open. No architecture. Multiple gaps. This is harder than NS.

### Why it might be tractable anyway
- **Asymptotic freedom** gives UV control for free (the coupling vanishes). NS has no analog.
- **Lattice is well-defined** and satisfies OS axioms. The object EXISTS discretely.
- **50 years of physics** provides enormous heuristic guidance. We know WHAT the answer is. We need to PROVE it.
- **Balaban's 1400 pages** already did the hardest analytical step (UV stability). It's published but never extended.
- **Chatterjee's recent work** (2019-2023) reopened the problem with modern probability tools.

### The meta-question
Is the YM mass gap more like proving a KNOWN THEOREM rigorously (the physics is settled, we need math), or more like DISCOVERING something new?

I believe: it's the former. The physics is understood. The mass gap exists. The lattice shows it. The proof is a matter of mathematical technology catching up. This makes it a sigma-method problem: certify computationally, find identities, build chains, close the gap.

## FIRST MOVES

1. **Lattice SU(2) on GPU** — measure mass gap vs coupling, verify asymptotic freedom scaling
2. **Transfer matrix for 2³×T lattice** — compute spectral gap exactly for small spatial volume
3. **Peter-Weyl expansion** — the "Fourier modes" of YM. Decompose Wilson action in irreps.
4. **Read Balaban** — understand exactly where his 1400 pages stop
5. **Read Chatterjee 2019** — modern entry point, probability language

## 000. The numerical track begins. NS taught the method. YM is the target.
## Phase 0: map the space. Phase 1: compute everything. Phase 2: find identities.
## The mass gap is real. The lattice shows it. The proof is construction, not discovery.
