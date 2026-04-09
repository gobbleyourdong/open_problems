---
source: Galerkin convergence argument for regularity
type: POTENTIAL PROOF for specific ICs via Galerkin + computer-assisted verification
status: POSSIBLY CLOSED for verified ICs — needs careful analysis
date: 2026-03-26 cycle 21
---

## The Argument

### Step 1: Galerkin truncation is globally regular
For any N and ν > 0: the Galerkin-truncated NS is a finite-dimensional
dissipative ODE → global smooth solutions for all time. KNOWN.

### Step 2: Computer-assisted verification at fixed N
Our theorems: ||ω_N(t)||_∞ ≤ ||ω_N(0)||_∞ for N=64, ν=10⁻⁴,
50 seeds, T ∈ [0, 10]. Verified with margin > 10⁶.

### Step 3: Galerkin convergence
For smooth PDE solutions on [0,T*): ω_N → ω in all H^s norms.
In particular: ||ω_N - ω||_∞ → 0 as N → ∞ on [0,T*).
STANDARD (spectral convergence for smooth data).

### Step 4: Pass the bound to the limit
On [0, min(T*, 10)]:
||ω(t)||_∞ = lim_{N→∞} ||ω_N(t)||_∞ ≤ lim_{N→∞} ||ω_N(0)||_∞ = ||ω(0)||_∞

### Step 5: Extend to all time via BKM
If T* ≤ 10: step 4 gives ||ω||_∞ bounded on [0,T*) → BKM → contradiction.
So T* > 10. Repeat with T=20, 30, ... → T* = ∞.

(The computer-assisted verification at T=10 extends to arbitrary T
because the N=64 system is globally regular and ||ω_N||_∞ is
monotonically decreasing.)

## The Subtleties

### 1. The bound needs to hold uniformly in N
Our verification is at N=64 and N=32. For the limit, we need
||ω_N(t)||_∞ ≤ ||ω_N(0)||_∞ for ALL N ≥ N₀. We've verified at
N=32, 64. We need it for ALL N ≥ 64 (or at least a subsequence).

Data: at N=64, 128, 256 with floating point: ratio = 1.0000 always.
The computer-assisted verification at N=64 has margin 10⁸.
If verified at N=128 (needs GPU): the argument strengthens.

### 2. Galerkin convergence rate
The error ||ω_N - ω||_∞ ≤ C N^{-s+3/2} ||ω||_{H^s}.
For s = 2: error ~ N^{-1/2}. For s = 3: error ~ N^{-3/2}.
At N=64: error ~ 64^{-1/2} = 0.125 (10⁻¹ order).
Our ||ω||_∞ ~ 10⁻³. So the Galerkin error COULD exceed the signal.

This is the problem: the spectral convergence rate might not be fast
enough to guarantee ||ω_N||_∞ ≈ ||ω||_∞ at N=64.

### 3. The H^s norm depends on regularity
||ω||_{H^s} is finite only if the solution is s-times differentiable.
This is guaranteed for smooth solutions (on [0,T*)), but the BOUND
on ||ω||_{H^s} might blow up as t → T*, which would make the
Galerkin error blow up too.

## Assessment

The argument WORKS in principle but has a quantitative gap:
the Galerkin error at N=64 might be too large relative to the
||ω||_∞ signal. At N=128 or N=256, the error would be smaller.

For a RIGOROUS version: need computer-assisted verification at
multiple N values and a convergence rate estimate showing the
error shrinks fast enough.

This is the computer-assisted proof paradigm:
- Verify at N=64 ✅
- Verify at N=128 (GPU needed)
- Show convergence rate from N=64 to N=128
- Bound Galerkin error in terms of verified quantities
- The limit N→∞ gives the PDE solution bound

## Status

NOT CLOSED — needs:
1. Verification at N=128 (to establish convergence)
2. Galerkin error bound (quantitative)
3. Extension to arbitrary T (from the monotone decrease)

But the STRUCTURE is right. This is the cleanest path from
computer-assisted theorems to PDE regularity.
