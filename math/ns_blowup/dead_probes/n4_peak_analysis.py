"""
numerical track Cycle 9 — N=4 Peak Analysis

The N=4 peak configuration (worst S²ê/|ω|² across all N):

  c(4) = 0.3615936452
  k-vectors: [-1,0,0], [-1,1,1], [1,0,1], [1,1,1]
  K² shells: 1, 3, 2, 3 (mixed)

Wavevector geometry:
  cos∠(k0,k1) = 1/√3 ≈ 0.577
  cos∠(k0,k2) = -1/√2 ≈ -0.707
  cos∠(k0,k3) = -1/√3 ≈ -0.577
  cos∠(k1,k2) = 0     (orthogonal!)
  cos∠(k1,k3) = 1/3
  cos∠(k2,k3) = √(2/3) ≈ 0.817

NOT a clean geometric configuration like N=3 (all orthogonal).
The value 0.3616 doesn't match simple fractions (closest: 13/36 = 0.361).
Likely an algebraic number determined by the wavevector Gram matrix.

COMPLETE c(N) SEQUENCE (proven/computed):
  c(2) = 1/4        = 0.2500  (proven, tight)
  c(3) = 1/3        = 0.3333  (proven in Lean, tight)
  c(4) = 0.3616     (computed, GLOBAL PEAK)
  c(5) = 0.3332     (computed)
  c(6) = 0.3161     (computed)
  c(7) = 0.2960     (computed)
  c(8) = 0.2802     (computed)
  c(10) = 0.2522    (computed)
  c(13) = 0.1696    (computed)

ALL < 0.75. Peak at N=4 with 52% margin.
Found via exhaustive scan of all C(26,4)=14950 quadruples + DE refinement.
"""
