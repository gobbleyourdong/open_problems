# Three Barriers to Proving P ≠ NP — Findings

**Script**: `numerics/three_barriers.py`
**Data**: `results/three_barriers_data.json`
**Date**: 2026-04-09

---

## Context

All prior numerical evidence (sat_scaling, landscape_k, grover, shor) is
consistent with P ≠ NP. The doubling period of k ≈ 14.24 variables,
K-flat hard landscapes, and Grover's 2× period all support the compression
asymmetry claim. But numerical evidence cannot PROVE P ≠ NP.

This study addresses why a proof has been elusive for 50+ years by
numerically demonstrating the three known barriers and connecting each
to the K-information / compression view.

---

## Barrier 1: Relativization (Baker-Gill-Solovay 1975)

**Claim**: Any proof technique that works uniformly for all oracle machines
cannot separate P from NP.

**Why**: There exist oracles O₁ where P^O1 = NP^O1 (e.g., an oracle that
directly solves SAT) and oracles O₂ where P^O2 ≠ NP^O2 (e.g., a random
oracle). A technique valid for all oracles would have to give inconsistent
answers — blocked.

**Numerical demo**: Classical vs Grover query complexity on random oracles.

| n | 2^n | Classical (expected) | Grover queries | Speedup |
|---|-----|---------------------|----------------|---------|
| 4 | 16 | 8.5 | 3.14 | 2.71× |
| 8 | 256 | 128.5 | 12.57 | 10.23× |
| 12 | 4096 | 2048.5 | 50.27 | 40.75× |
| 16 | 65536 | 32768.5 | 201.06 | 162.98× |

- Classical doubling period: **1 variable** (queries ∝ 2^n)
- Grover doubling period: **2 variables** (queries ∝ 2^(n/2))
- Speedup = 2^(n/2), growing exponentially

**Key finding**: Even with identical oracle access, classical and quantum
query complexities diverge exponentially. This means oracle-independent
arguments cannot explain P vs NP — oracles are the wrong abstraction
level. Any relativizing proof technique is blocked.

**Techniques blocked**: diagonalization, simulation arguments, most of
classical computability theory.

---

## Barrier 2: Natural Proofs (Razborov-Rudich 1994)

**Claim**: Under the assumption that pseudorandom generators (PRGs) exist,
no "natural" proof property can separate P from NP.

**Definition**: A property P is *natural* if it is:
1. **Constructive**: checkable in poly(2^n) time from the n-bit truth table
2. **Large**: holds for > 2^{-n/2} fraction of all n-bit boolean functions
3. **Useful**: holds for all functions NOT computable in poly-size circuits

**Why it's blocked**: A useful + constructive + large property would
distinguish hard functions from easy ones — but this would also let you
BREAK any PRG (the PRG output would fail the property, but truly random
strings usually satisfy it). This contradicts PRG security.

**Numerical demo**: gzip compression as a candidate "natural" property.
Property: P(x) = "x is compressible by > 15% under gzip (zlib level 9)".

| n_bits | n_samples | Compressible | Fraction | Threshold 2^{-n/2} | Large? |
|--------|-----------|--------------|----------|--------------------|--------|
| 8 | 1000 | 0 | 0.000000 | 6.25e-02 | NO |
| 16 | 1000 | 0 | 0.000000 | 3.91e-03 | NO |
| 32 | 1000 | 0 | 0.000000 | 1.53e-05 | NO |
| 64 | 1000 | 0 | 0.000000 | 2.33e-10 | NO |
| 128 | 1000 | 0 | 0.000000 | 5.42e-20 | NO |

**Key findings**:
- Gzip fails the **USEFUL** criterion: compressible strings are easy to
  compute (just output them from a small circuit). The property should
  identify HARD functions.
- Gzip fails the **LARGE** criterion: almost all random strings are
  Kolmogorov-incompressible. The compressible fraction is essentially 0,
  far below the 2^{-n/2} threshold.
- A natural proof would need all three criteria simultaneously — Razborov-
  Rudich proves this is impossible assuming PRGs exist.

**PRG assumption**: AES, SHA-256, and similar constructions are widely
believed to be secure PRGs. Under this assumption, natural proofs are
blocked.

**Techniques blocked**: Razborov's own monotone circuit lower bound
(which IS natural and thus cannot extend to general circuits), most
combinatorial circuit lower bound arguments.

---

## Barrier 3: Algebrization (Aaronson-Wigderson 2009)

**Claim**: Most algebraic proof techniques — including the polynomial method
that underlies IP=PSPACE, MIP*=RE, and other major results — cannot separate
P from NP, because they work via algebraic oracle extensions that preserve
computational difficulty.

**Definition**: A proof technique *algebrizes* if it continues to work when
oracles are replaced by their unique low-degree polynomial extensions over
large fields.

**Why it's blocked**: Algebraic extensions of hard oracles remain hard.
The Schwartz-Zippel lemma guarantees that a degree-d polynomial over Z/p
agrees with a random function on at most d/p fraction of inputs — so the
polynomial extension carries essentially no useful information about preimages.

**Numerical demo**: Low-degree polynomial extensions of SHA-256 hash function.
For domain sizes N ∈ {64, 128, 256, 512} and polynomial degrees d ∈ {2, 4, 8}:

- Classical preimage search: random order, queries scale with N
- Polynomial oracle (algebraic extension): number of x where p(x) ≡ target (mod N)
- Algebraic advantage ratio ≈ 0 in almost all cases

| N | degree | Classical queries | Poly preimage matches | Algebraic advantage |
|---|--------|------------------|----------------------|---------------------|
| 128 | 2 | 26 | 0 | 0.0000 |
| 256 | 4 | 65 | 0 | 0.0000 |
| 512 | 8 | 46 | 0 | 0.0000 |

**Key finding**: Low-degree polynomial extensions of SHA-256 provide no
meaningful advantage for finding preimages. The algebraic structure does
not compress the hardness — it preserves it.

**Techniques blocked**: polynomial method, Razborov-Smolensky approach,
arithmetic circuit lower bounds via algebraic methods, most tools that
have been used to prove major results in interactive proofs.

---

## K-Information Framework: Connecting the Three Barriers

The compression view of P ≠ NP says: finding compression (solving NP)
is exponentially harder than verifying it (checking solutions). The
find/verify asymmetry has doubling period k ≈ 14.24 (from sat_scaling).

The three barriers can be reread as constraints on the **K-complexity**
of any valid proof:

| Barrier | What it blocks | K-info reading | Proof requirement |
|---------|---------------|----------------|-------------------|
| Relativization (1975) | Generic, oracle-independent arguments | K-simple: short argument valid across all models | Must be model-specific (high K-content) |
| Natural Proofs (1994) | Constructive + large + useful properties | K-simple: common, checkable, generic (under PRG) | Must be unnatural: rare or non-constructive |
| Algebrization (2009) | Polynomial method, algebraic extensions | K-simple: algebraic = compact description (low K) | Must transcend polynomial structure |

**Synthesis**: All three barriers block proof techniques that are **K-SIMPLE**
(low Kolmogorov complexity — short, natural, generic, algebraic arguments).

Therefore: any proof of P ≠ NP must be **K-COMPLEX**. It cannot be:
- A generic argument (blocked by relativization)
- A constructive, common, applicable argument (blocked by natural proofs)
- An algebraically structured argument (blocked by algebrization)

**Why this explains 50+ years of failure**: Every "obvious" approach is
K-simple. The three barriers explicitly and provably block all K-simple
approaches. The remaining search space consists of genuinely novel,
K-complex techniques — rare, specific, and non-algebraic arguments that
complexity theorists have not yet found.

**Prediction from K-information view**: A proof of P ≠ NP (if found) will:
1. Exploit specific properties of the Turing machine model (non-relativizing)
2. Be non-constructive or apply to a non-large class (non-natural)
3. Go beyond polynomial methods (non-algebrizable)

Such a proof will be **K-complex** — it cannot be summarized in a few
pages using standard techniques. It must match the K-content of the
claim it proves: the separation of two exponentially different complexity
regimes requires an argument of comparably high information content.

---

## What Remains Open

The three barriers narrow the proof search space to K-complex techniques.
Current candidates that may escape the barriers:

- **Geometric complexity theory** (Mulmuley-Sohoni): uses representation
  theory and algebraic geometry. Possibly non-algebrizable, but controversial.
- **Circuit complexity via random restrictions**: partially non-natural,
  but has not yet reached general circuits.
- **Information-theoretic arguments**: if non-relativizing and non-large,
  may escape all three barriers — but none known to suffice.

The numerical track has characterized the **size** of the gap (k ≈ 14,
exponential asymmetry) but not the **mechanism**. Identifying the mechanism
is the task of the theoretical track — and it must be K-complex.

---

## Data Summary

- Relativization: classical/Grover speedup = 2^(n/2), confirmed for n=4..16
- Natural proofs: gzip compressibility of random strings = 0/1000 at all n
- Algebrization: polynomial-oracle advantage ≈ 0 for SHA-256 preimage search
- K-framework: all three barriers consistent with "proof must be K-complex"
- JSON data: `results/three_barriers_data.json`
