# Birch and Swinnerton-Dyer — Gap Assessment

## Phase: 0 → 1 (Paper Arsenal in progress)

## The Problem

For an elliptic curve E/Q:

**Weak BSD**: rank(E(Q)) = ord_{s=1} L(E, s)

**Full BSD**: The leading coefficient of L(E,s) at s=1 is:
  lim_{s→1} L(E,s)/(s-1)^r = (Ω_E · Reg_E · |Ш(E)| · ∏ c_p) / |E(Q)_tors|²

where r = rank, Ω = real period, Reg = regulator, Ш = Tate-Shafarevich group,
c_p = Tamagawa numbers, E(Q)_tors = torsion subgroup.

## What's Known

### Rank 0: PROVED
If L(E,1) ≠ 0, then rank(E(Q)) = 0 and Ш is finite.
- Kolyvagin (1990): Euler systems prove finiteness of Ш
- Kato (2004): alternative proof via his Euler system
- Gross-Zagier + Kolyvagin: if L(E,1) ≠ 0, Heegner point is torsion → rank = 0

### Rank 1: PROVED
If L(E,1) = 0 and L'(E,1) ≠ 0, then rank(E(Q)) = 1 and Ш is finite.
- Gross-Zagier (1986): L'(E,1) = c · ĥ(P_K) where P_K is a Heegner point
  and ĥ is the Néron-Tate height. So L'(E,1) ≠ 0 ⟺ P_K has infinite order.
- Kolyvagin (1990): P_K infinite order → rank exactly 1 and Ш finite.

### Rank ≥ 2: COMPLETELY OPEN
If ord_{s=1} L(E,s) ≥ 2: NOTHING is known.
- Can't produce rational points (no Heegner point analog)
- Can't bound the rank from above
- Can't prove Ш is finite

### Average Rank
- Bhargava-Shankar (2010-2015): average rank of E/Q is ≤ 1.5 (unconditional)
- With Goldfeld conjecture: average analytic rank ~ 1/2
- This means MOST curves have rank 0 or 1 (where BSD is known)
- But individual curves of rank ≥ 2 are intractable

### Parity
- Root number w(E) = ±1 determines the parity of ord_{s=1} L(E,s)
- Parity conjecture: rank(E) ≡ ord_{s=1} L(E,s) mod 2
- Proved in many cases (Dokchitser-Dokchitser, Nekovář)

### Iwasawa Theory
- Main conjecture for GL₂: relates Selmer groups to p-adic L-functions
- Skinner-Urban (2014): proved the main conjecture for many cases
- Implications for BSD: gives p-part of |Ш| in some cases

## The Structural Gap

```
rank 0: SOLVED (Euler systems)
rank 1: SOLVED (Heegner points + Euler systems)
rank 2: ??????????????????
rank 3: ??????????????????
         ↑
    THE WALL: no construction of rational points for rank ≥ 2
```

### Why Rank ≥ 2 Is Hard

**Heegner points work for rank 1** because:
1. There's ONE special point P_K (constructed from CM theory)
2. Gross-Zagier relates L'(E,1) to the height of P_K
3. Kolyvagin's Euler system bounds the rank using P_K

**For rank ≥ 2**: you'd need TWO or more independent points.
No known construction produces them. The CM/Heegner method gives
at most one independent point per imaginary quadratic field K.

**The fundamental obstacle**: we don't know how to CONSTRUCT rational
points on elliptic curves of high rank. We can find them by search
(e.g., Elkies found curves of rank 28+) but can't prove they exist
from L-function data.

## Route Map (Initial)

### Route 1: Higher Heegner Points / Derived Functors
Generalize Heegner points to produce more than one independent point.
- Darmon (2004): "Rational points on modular elliptic curves" — Stark-Heegner
  points (conjectural, over real quadratic fields)
- Higher-dimensional cycles on Kuga-Sato varieties
- Derived Euler systems (Loeffler-Zerbes)

### Route 2: Iwasawa Theory
The Iwasawa main conjecture relates p-Selmer groups to p-adic L-functions.
If proved in sufficient generality → BSD for specific curves.
- Skinner-Urban: proved for many ordinary primes
- Wan (2014+): results for supersingular primes
- Castella-Hsieh: higher-rank Iwasawa theory

### Route 3: Automorphic / Langlands
BSD is a special case of the Bloch-Kato conjecture for motives.
The Langlands program provides the framework.
- Functoriality: relates L(E,s) to automorphic L-functions
- Potential automorphy: Taylor et al.
- The full Langlands program would imply BSD (eventually)

### Route 4: Computational Certification
- LMFDB: millions of curves with computed ranks and L-values
- Verify BSD for specific curves to build an "iron fortress"
- Cremona: all curves of conductor ≤ 500000 classified

### Route 5: New Ideas
- Zhang (2014): Gross-Zagier for higher weight modular forms
- Arithmetic Gan-Gross-Prasad conjecture
- Diagonal cycles (Darmon-Rotger)

## Status
- [ ] Paper arsenal built
- [ ] Routes ranked
- [ ] Lean definitions started
- [ ] Computational targets identified
- [ ] Phase 1 begun
