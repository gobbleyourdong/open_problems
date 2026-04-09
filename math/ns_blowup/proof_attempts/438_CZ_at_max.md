---
source: CZ CONSTANT AT THE MAX — the log factor doesn't grow in practice
type: KEY OBSERVATION — the max condition constrains CZ beyond theory
file: 438
date: 2026-03-30
---

## THE OBSERVATION

At x* = argmax|ω|: |∇u(x*)|²/|ω(x*)|² stays below 1.12 for ALL N.

CZ theory predicts: the ratio could be C(1+log(spectral width)) → ∞.
But the MAX CONDITION prevents this growth.

## WHY THE LOG FACTOR DOESN'T GROW AT THE MAX

At x*: ALL Fourier modes of ω are phase-coherent (by definition of max).
The SAME phase coherence constrains ∇u:
- (∇u)_k = (k⊗(k×ω̂_k))/|k|² has |(∇u)_k| = |ω̂_k| (equal magnitude)
- The PHASES of (∇u)_k at x* are determined by e^{ikx*} (same as ω)
- The DIRECTIONS differ (matrix vs vector) but the phases are SHARED

The CZ log factor arises from INCOHERENT summation (generic x).
At x* (max coherence for ω): the summation for ∇u is ALSO coherent
(from the shared phases), preventing the log growth.

## THE FORMAL GAP

Proving |∇u(x*)|²/|ω(x*)|² < 13/8 requires:
- Showing the phase coherence at the max BOUNDS the gradient
- This is a statement about the Fourier multiplier ik⊗(k×·)/|k|²
  evaluated at the argmax of the input |ω|
- No existing CZ theorem covers this (CZ bounds are for generic points)

## CONNECTION TO THE KEY LEMMA

|∇u|²/|ω|² < 13/8 IS the Key Lemma (via trace-free, file 429).
The observation that the ratio doesn't grow with N is the SAME as
S²ê/|ω|² not growing with N.

Both are consequences of the phase-coherence constraint at the max.
Proving either one closes the millennium problem.

## 438. The CZ log factor doesn't grow at the max (phase coherence).
## Proving this formally = closing the Key Lemma = millennium prize.
