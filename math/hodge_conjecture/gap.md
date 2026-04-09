# Hodge Conjecture — Gap Assessment

## Phase: 0 → 1 (Paper Arsenal in progress)

## The Problem

On a non-singular complex projective variety X, every Hodge class is a
rational linear combination of classes of algebraic cycles.

## Unpacking

### The Hodge Decomposition
For a compact Kähler manifold X of dimension n:
  H^k(X, C) = ⊕_{p+q=k} H^{p,q}(X)

where H^{p,q} = {classes representable by closed (p,q)-forms}.
Conjugation: H^{p,q} = conjugate of H^{q,p}.

### Hodge Classes
A Hodge class of degree 2p is an element of:
  Hdg^p(X) = H^{2p}(X, Q) ∩ H^{p,p}(X)

These are rational cohomology classes that live in the "middle" of the
Hodge decomposition (equal holomorphic and anti-holomorphic degree).

### Algebraic Cycles
An algebraic cycle of codimension p is a formal sum Z = Σ n_i Z_i
where Z_i are irreducible subvarieties of codimension p.

The cycle class map: cl: Z^p(X) → H^{2p}(X, Q)
sends a subvariety to its cohomology class (Poincaré dual of its
fundamental class).

### The Conjecture
Im(cl ⊗ Q) = Hdg^p(X)

Every Hodge class comes from a rational combination of subvarieties.

## What's Known

### p = 1: PROVED (Lefschetz (1,1)-theorem)
Every Hodge class in H^2(X,Q) ∩ H^{1,1}(X) is algebraic.
Proof: uses the exponential sequence 0 → Z → O → O* → 0 and
the fact that H^1(X, O*) classifies line bundles, whose first
Chern classes give exactly the (1,1) Hodge classes.

This is a COHOMOLOGICAL argument — it uses the structure of sheaf
cohomology to match topological and algebraic objects.

### p = dim(X) - 1: PROVED
By hard Lefschetz + the p=1 case: duality gives the complementary
codimension case.

### Abelian varieties
- dim ≤ 3: proved (various authors)
- dim 4: proved (assuming some genericity conditions)
- dim 5: partial results
- General abelian varieties: OPEN

### Integer coefficients: FALSE
Atiyah-Hirzebruch (1962): the INTEGRAL Hodge conjecture fails.
There exist torsion Hodge classes that are not algebraic.
This is why the conjecture uses RATIONAL coefficients.

## Route Map

### Route 1: Grothendieck's Standard Conjectures ★★★★
The standard conjectures (Lefschetz, Hodge) would imply the Hodge
conjecture. They predict:
- Künneth components of the diagonal are algebraic
- The Lefschetz operator is algebraic
- Numerical and homological equivalence coincide

These are stronger than Hodge but provide the "right framework."

### Route 2: Motives ★★★
Grothendieck's theory of motives: if the category of motives is
semisimple (Jannsen's conjecture), Hodge would follow.
Voevodsky's motivic cohomology gives tools but hasn't closed the gap.

### Route 3: Hodge Theory / Period Maps ★★★
Study how Hodge classes vary in families. Use period domains and
Griffiths transversality to constrain which classes can be Hodge.

### Route 4: Specific Varieties ★★★★
Prove Hodge for increasingly large classes of varieties:
- Abelian varieties (partially done)
- Complete intersections
- Moduli spaces
- Hilbert schemes

### Route 5: Derived Categories ★★
Use derived categories of coherent sheaves and Fourier-Mukai transforms.
Powerful but hasn't reached Hodge directly.

## The Structural Gap

**Why p = 1 works and p ≥ 2 doesn't:**

For p = 1: Hodge classes ↔ line bundles ↔ divisors (codim 1 subvarieties).
The correspondence is CANONICAL (exponential sequence).

For p ≥ 2: Hodge classes ↔ ??? ↔ codim p subvarieties.
The middle step is missing. There's no "exponential sequence for
higher codimension." Vector bundles give Chern classes (not all Hodge
classes). The Chern character maps K-theory to cohomology but isn't
surjective onto Hodge classes in general.

**The wall: no canonical construction of subvarieties from Hodge classes.**

## Status
- [ ] Paper arsenal built
- [ ] Routes ranked
- [ ] Lean definitions started
- [ ] Computational targets identified
