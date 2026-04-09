# BSD — Paper Arsenal

> Built: 2026-04-07 | theory track Phase 1

## Tier 1: The Solved Cases (Rank 0 and 1)

### 1.1 Gross-Zagier (1986)
- **Gross, Zagier**. "Heegner points and derivatives of L-series." Inventiones 84.
  - L'(E/K, 1) = c · ĥ(y_K) — THE formula connecting L-derivatives to heights
  - Generalized: Yuan-Zhang-Zhang (2013)

### 1.2 Kolyvagin's Euler System (1990)
- **Kolyvagin**. "Euler systems." Grothendieck Festschrift.
  - y_K non-torsion → rank(E(K)) = 1, Ш finite
  - Bounds |Ш| divides [E(K) : Z·y_K]²

### 1.3 Kato's Euler System (2004)
- **Kato**. "p-adic Hodge theory and values of zeta functions of modular forms."
  - L(E,1) ≠ 0 → rank = 0 (independent of Heegner points)
  - One divisibility of Iwasawa main conjecture

### 1.4 Modularity
- **Wiles** (1995), **BCDT** (2001). Every E/Q is modular.
  - Essential: gives analytic continuation of L(E,s)

## Tier 2: The Framework (Iwasawa Theory)

### 2.1 Skinner-Urban Main Conjecture (2014)
- **Skinner, Urban**. Inventiones 195.
  - Full Iwasawa MC for good ordinary primes (under technical conditions)
  - Implies p-part of BSD for rank 0/1

### 2.2 Jetchev-Skinner-Wan (2017)
- p-part of BSD formula for rank 1 at good ordinary p ≥ 3
  - Combined with GZ+K: FULL BSD formula at all but finitely many primes

### 2.3 Skinner Converse (2014)
- If rank = 0 and Ш[p^∞] finite → analytic rank = 0 (converse direction)

## Tier 3: Average Rank / Statistics

### 3.1 Bhargava-Shankar (2010-2015)
- Average rank ≤ 0.885. Average 2-Selmer = 3.
- Method: geometry of numbers on representation spaces

### 3.2 Bhargava-Skinner-Zhang (2014)
- ≥ 66.48% of E/Q satisfy BSD (statistically)

### 3.3 Smith (2022)
- 2^∞-Selmer distribution matches Cohen-Lenstra for 100% of quadratic twists

### 3.4 Koymans-Smith (2024)
- Positive density of quadratic twists with r_an = 0 (and r_an = 1), for every E/Q

## Tier 4: The Frontier (Rank ≥ 2 Attempts)

### 4.1 Darmon-Rotger Diagonal Cycles
- Higher-dimensional generalizations of Heegner points
- Gross-Zagier formulas for triple products, but still rank 1

### 4.2 Loeffler-Zerbes Euler Systems (2020-2024)
- Euler systems from GSp(4), GU(2,1), automorphic forms
- Still rank-1 Euler systems (one cohomology class, not two)
- arXiv: multiple papers 2020-2024

### 4.3 Castella-Grossi-Lee-Skinner (2022)
- p-converse to GZ+K in Eisenstein case

## The Obstruction Table

| Approach | Reaches | Blocked by |
|----------|---------|------------|
| Heegner + GZ + Kolyvagin | rank 0, 1 | ONE point only |
| Kato | rank 0 | One divisibility |
| Iwasawa MC | rank 0, 1 (p-parts) | Higher derivatives of p-adic L |
| Bhargava-Shankar | 66.48% statistically | Individual rank ≥ 2 curves |
| Loeffler-Zerbes | New Bloch-Kato cases | Still rank-1 Euler systems |
| Computational | Verified to conductor 500K | Circular for rank ≥ 2 Ш |

## THE WALL

**No second-order Gross-Zagier formula exists.**

Rank 0-1: L'(E/K,1) = height(Heegner point). ONE derivative, ONE point.
Rank ≥ 2: Need L''(E,1) = ??? (two independent points). NOTHING.

Every approach that works for rank 1 is structurally limited to
producing ONE algebraic object. For rank ≥ 2: need TWO. Nobody has them.
