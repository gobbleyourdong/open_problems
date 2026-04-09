# Hodge Conjecture: Cubic Fourfold Discriminant Census

## Date: 2026-04-08

## Special Cubic Fourfolds (Hassett classification)

A cubic fourfold X ⊂ CP⁵ is 'special' of discriminant d if its
Hodge lattice has rank 2 with intersection form of discriminant d.

### KNOWN cases (algebraic cycle found):
| d | Contains | Hodge status |
|---|---------|-------------|
| 8 | Plane P² | ✓ |
| 12 | Cubic scroll | ✓ |
| 14 | Quartic scroll / Pfaffian | ✓ |
| 20 | Veronese surface | ✓ |
| 26 | K3 surface (degree 10) | ✓ |
| 38 | Fano surface | ✓ |
| 42 | Associated K3 | ✓ |

### OPEN cases (Hodge class exists, cycle not found):
| d | Status |
|---|--------|
| 24 | OPEN — first unknown |
| 30 | OPEN |
| 32 | OPEN |
| 44 | OPEN |
| 48 | OPEN |
| ... | ... |

## The Brute Force Target

For d = 24 (smallest open case):
1. Construct a 24-special cubic fourfold
2. The Hodge lattice K_{24} has T² = 4
3. Search for algebraic surfaces of degree ≤ D
4. If found: Hodge verified for d=24

This would be a NEW RESULT — no one has verified Hodge for d=24 cubics.
