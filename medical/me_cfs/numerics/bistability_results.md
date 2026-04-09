# REQ-011: ME/CFS Bistability Phase Portrait — Initial Results

## Date: 2026-04-09

## Result: Model framework built, bistability NOT YET achieved

### What was built
- 6-variable ODE system (V, I, N, M, A, F) from `models/vicious_cycle.md`
- Steady state finder via fsolve from 108 initial conditions
- Trajectory simulator via RK45
- Phase portrait flow analysis (V vs N plane)

### Current result
With estimated parameters:
- **Only 1 steady state found: HEALTHY** (V → 0, N → 1, M → 1)
- All trajectories (disease IC, healthy IC, threshold IC) converge to recovery
- The viral clearance rate exceeds replication at all tested viral loads

### Why bistability wasn't found
The current parameters make NK + autophagy clearance too strong relative
to viral replication. For bistability, need:
1. **Stronger positive feedback**: k_exhaust should increase more steeply
   with V (NK collapses at high viral load)
2. **Threshold effect**: below critical NK level, virus escapes control
3. **Slower NK restoration**: k_restore should be smaller (weeks, not days)

### What the theory track needs to provide
- Literature-derived parameter VALUES (not just qualitative signs):
  - k_replicate: CVB TD mutant replication rate in muscle tissue
  - k_clear: NK cell killing rate per NK cell per virus (from in vitro)
  - k_exhaust: NK exhaustion rate from chronic stimulation (Koss 2015?)
  - k_restore: NK restoration time with sleep + selenium + zinc
- The RATIO k_replicate / (k_clear × N_baseline) determines whether
  bistability exists. Need this ratio > 1 for disease persistence.

### Script location
`me_cfs/numerics/bistability_portrait.py`
Runtime: < 1 second. Dependencies: numpy, scipy.

### Next steps
1. Parameter calibration from published PK/PD data
2. Re-run with calibrated parameters to find bistability
3. Once bistable: map the basin boundary (the "tipping point")
4. Test interventions: which parameter changes push across the boundary?
