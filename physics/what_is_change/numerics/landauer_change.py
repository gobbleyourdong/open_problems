#!/usr/bin/env python3
"""
landauer_change.py — Thermodynamic cost of K-information change (Landauer's principle).

Context: zeno_and_change.py defined K-change as K(S2|S1) and computed it for several
transitions. gap.md R1 asks which theory of causation is best supported by the compression
view. R3 asks about physical change vs phenomenal flow.

Key connection: Landauer's principle says erasing 1 bit costs k_B T ln(2) joules.
If change = K-information update = K(S2|S1) new bits written + old bits erased, then
CHANGE HAS A THERMODYNAMIC COST. This connects K-change to the S-information thermodynamics
from what_is_time.

For each physical process modelled here, we compute:
  E_change = K_bits × k_B × T × ln(2)      [Landauer cost, joules]

at three temperatures:
  T_body = 310 K    (biological processes)
  T_room = 298 K    (chemistry / lab scale)
  T_cmb  = 2.725 K  (cosmological change)

And for the black hole: at its own Hawking temperature.

Usage:
    cd ~/open_problems/physics/what_is_change
    python3 numerics/landauer_change.py

Numerical track, what_is_change — 2026-04-09
"""

import math, json, os

# ── Physical constants ────────────────────────────────────────────────────────

k_B       = 1.380649e-23    # J/K   Boltzmann constant
G         = 6.674e-11       # m³/(kg·s²)
hbar      = 1.054571817e-34  # J·s
c         = 2.998e8          # m/s
m_proton  = 1.673e-27        # kg
ln2       = math.log(2)

T_body    = 310.0   # K — body temperature
T_room    = 298.0   # K — room temperature
T_cmb     = 2.725   # K — cosmic microwave background

# ── Landauer cost ─────────────────────────────────────────────────────────────

def landauer_J(bits: float, T: float) -> float:
    """Energy cost (joules) of erasing `bits` at temperature T."""
    return bits * k_B * T * ln2

def landauer_eV(bits: float, T: float) -> float:
    eV = 1.602176634e-19  # J
    return landauer_J(bits, T) / eV

# ── Process 1: Neuron firing ──────────────────────────────────────────────────

def neuron_firing():
    """
    A single neuron crosses its threshold: binary state change (sub-threshold →
    action potential). Modelled as 1 bit of K-change (threshold crossed or not).

    Real neurons: ~10^9 ions move during an action potential, but the DECISION
    (whether to fire) is 1 bit of information. The physical cost is much larger
    because of the ion-channel mechanism; here we compute the MINIMUM
    information-theoretic cost (Landauer floor).

    Biological energy of one action potential: ~2×10^-12 J (measured).
    Landauer floor at T=310 K for 1 bit: many orders of magnitude lower.
    The gap = thermodynamic slack = inefficiency of biological implementation.
    """
    bits = 1.0  # 1 bit: fire or not fire
    E_body = landauer_J(bits, T_body)
    E_measured = 2e-12  # J, empirical (ATP hydrolysis per action potential)
    slack = E_measured / E_body

    return {
        "process": "neuron_firing",
        "description": "Binary threshold crossing: fire or not fire",
        "K_bits": bits,
        "T_body_K": T_body,
        "E_landauer_body_J": E_body,
        "E_landauer_body_eV": landauer_eV(bits, T_body),
        "E_biological_measured_J": E_measured,
        "thermodynamic_slack_factor": slack,
        "note": (
            "Landauer floor is ~{:.2e} J. Biological implementation costs ~{:.2e} J "
            "— a factor of {:.2e} above minimum. The slack is structural: ion-channel "
            "specificity, reversal-potential gradients, pump reset costs.".format(
                E_body, E_measured, slack)
        ),
    }

# ── Process 2: DNA base-pair mutation ────────────────────────────────────────

def dna_mutation():
    """
    A single base-pair mutation: one of {A,T,G,C} → another.
    Each base encodes log2(4) = 2 bits. A mutation changes 2 bits of K-content.

    Landauer cost = 2 bits × k_B T ln(2) at T=310 K (body temperature).

    Actual cost of DNA replication (polymerase per bp): ~50 k_B T.
    This is the chemical energy including fidelity enforcement (proofreading).
    The minimum (Landauer) is 2 k_B T ln(2) ≈ 3 k_B T for two bits.
    """
    bits = math.log2(4)   # 2 bits — 4 possible bases, 1 position changed
    E_body = landauer_J(bits, T_body)
    E_polymerase = 50 * k_B * T_body  # ~50 k_B T per base pair (measured)
    slack = E_polymerase / E_body

    return {
        "process": "dna_base_pair_mutation",
        "description": "Single nucleotide substitution: 2 bits of K-change",
        "K_bits": bits,
        "T_body_K": T_body,
        "E_landauer_body_J": E_body,
        "E_landauer_body_eV": landauer_eV(bits, T_body),
        "E_polymerase_J": E_polymerase,
        "thermodynamic_slack_factor": slack,
        "note": (
            "2 bits (4 bases) at T=310K costs >= {:.2e} J. "
            "Polymerase uses ~{:.2e} J per bp including error-correction. "
            "Slack factor {:.1f}x — proofreading imposes ~25x overhead above Landauer.".format(
                E_body, E_polymerase, slack)
        ),
    }

# ── Process 3: Photon absorption (quantum state change) ──────────────────────

def photon_absorption():
    """
    A two-level atom absorbs a photon: |ground> → |excited>.
    This is a 1-qubit state flip, which classically encodes log2(2) = 1 bit.

    The photon energy: E_photon = h*nu (e.g., visible light: ~2 eV at 500 nm).
    The Landauer MINIMUM for 1-bit change at T=298 K:
      E_L = k_B × 298 × ln(2) ≈ 2.84e-21 J ≈ 0.018 eV

    The actual photon energy (500 nm visible): ~4e-19 J ≈ 2.5 eV.
    Ratio: photon energy / Landauer cost ≈ 140.

    The excess energy (2.5 eV vs 0.018 eV) goes into:
    - Vibrational modes of the atom/molecule
    - Internal conversion (heat)
    - Fluorescence emission
    The 1 bit of WHICH-state information is the K-change;
    the rest is S-entropy increase (heat).
    """
    bits = 1.0   # 1 classical bit from a 2-level system
    wavelength_nm = 500.0
    h_planck = 2 * math.pi * hbar  # J·s
    E_photon = h_planck * c / (wavelength_nm * 1e-9)  # J
    E_landauer_room = landauer_J(bits, T_room)
    slack = E_photon / E_landauer_room

    return {
        "process": "photon_absorption_500nm",
        "description": "Two-level atom absorbs visible photon: 1 qubit = 1 bit K-change",
        "K_bits": bits,
        "wavelength_nm": wavelength_nm,
        "T_room_K": T_room,
        "E_photon_J": E_photon,
        "E_photon_eV": E_photon / 1.602176634e-19,
        "E_landauer_room_J": E_landauer_room,
        "E_landauer_room_eV": landauer_eV(bits, T_room),
        "thermodynamic_slack_factor": slack,
        "note": (
            "Photon at 500nm carries {:.3f} eV. Landauer floor for 1 bit at T=298K: "
            "{:.4f} eV. Slack factor: {:.0f}x. The excess energy is dissipated as "
            "heat (S-entropy), not K-change. Only ~{:.1f}% of photon energy encodes "
            "the state transition; the rest is thermodynamic waste.".format(
                E_photon / 1.602176634e-19,
                landauer_eV(bits, T_room),
                slack,
                100.0 / slack)
        ),
    }

# ── Process 4: Macroscopic object moving 1 mm ────────────────────────────────

def macro_object_move():
    """
    A macroscopic object (1g mass) moves 1 mm at T=298 K.

    The K-information content of the new position (vs old):
    - Thermal position uncertainty at 298 K: δx ~ sqrt(k_B T / k_spring)
      For a free particle in a box, use de Broglie thermal wavelength:
      λ_th = h / sqrt(2π m k_B T)  (thermal de Broglie wavelength)

    - For m = 1g, T = 298K: λ_th is absurdly small (< 10^-30 m).
    - The number of distinguishable positions in 1 mm:
      N_pos = 1e-3 m / λ_th
    - K_bits = log2(N_pos) — the bits needed to specify which 1mm-slot we're in.

    This gives the MAXIMUM K-bits for specifying position to thermal precision.
    But any real measurement has a much coarser resolution.
    We use two cases:
      (a) Thermal precision: λ_th (theoretically minimal)
      (b) Measurement precision: 1 micrometer (realistic lab measurement)
    """
    h_planck = 2 * math.pi * hbar
    m_obj = 1e-3       # 1 gram in kg
    dx    = 1e-3       # 1 mm displacement in metres
    T     = T_room

    # Thermal de Broglie wavelength
    lambda_th = h_planck / math.sqrt(2 * math.pi * m_obj * k_B * T)

    # (a) Thermal precision
    N_thermal = dx / lambda_th
    bits_thermal = math.log2(N_thermal)

    # (b) Measurement precision: 1 micrometer
    dx_meas = 1e-6   # 1 micron
    N_meas = dx / dx_meas
    bits_meas = math.log2(N_meas)

    E_L_thermal = landauer_J(bits_thermal, T)
    E_L_meas    = landauer_J(bits_meas, T)

    return {
        "process": "macro_object_move_1mm",
        "description": "1g object moves 1mm — K-bits from position distinguishability",
        "mass_kg": m_obj,
        "displacement_m": dx,
        "T_room_K": T,
        "thermal_deBroglie_m": lambda_th,
        "K_bits_thermal_precision": bits_thermal,
        "K_bits_measurement_precision_1um": bits_meas,
        "E_landauer_thermal_J": E_L_thermal,
        "E_landauer_measurement_J": E_L_meas,
        "note": (
            "Thermal de Broglie wavelength for 1g at 298K: {:.2e} m. "
            "K-bits to thermal precision: {:.1f} bits ({:.2e} J at Landauer). "
            "K-bits at 1-micron measurement: {:.1f} bits ({:.2e} J). "
            "Macroscopic motion requires enormous K-information at thermal precision, "
            "but only ~10 bits at realistic measurement precision.".format(
                lambda_th, bits_thermal, E_L_thermal, bits_meas, E_L_meas)
        ),
    }

# ── Process 5: Black hole absorbs a proton ────────────────────────────────────

def black_hole_proton():
    """
    Black hole of mass M absorbs one proton (mass m_p).

    Bekenstein-Hawking entropy:
      S_BH = (k_B * c³ * A) / (4 * G * hbar)
      where A = 16π G² M² / c⁴  (Schwarzschild area)
      So: S_BH = 4π k_B G M² / (hbar c)   [in joules/kelvin]

    In bits: S_bits = S_BH / (k_B ln2)

    Change in bits when proton falls in:
      ΔS_bits = [S_BH(M + m_p) - S_BH(M)] / (k_B ln2)
              = 4π G [(M + m_p)² - M²] / (hbar c ln2)
              = 4π G [2M m_p + m_p²] / (hbar c ln2)
              ≈ 8π G M m_p / (hbar c ln2)   (for m_p << M)

    Hawking temperature: T_H = hbar c³ / (8π G M k_B)

    We use M = 10 solar masses (stellar black hole).
    """
    M_sun = 1.989e30   # kg
    M     = 10 * M_sun  # 10 solar mass black hole

    # Bekenstein-Hawking entropy in bits for mass M
    def bh_entropy_bits(mass):
        S_SI = 4 * math.pi * k_B * G * mass**2 / (hbar * c)
        return S_SI / (k_B * ln2)

    S_before = bh_entropy_bits(M)
    # Float64 cannot represent (M + m_proton)^2 - M^2 directly when M~10^31, m~10^-27
    # (ratio 10^58 >> float64 precision ~10^15).
    # Use exact algebraic identity: (M+m)^2 - M^2 = 2Mm + m^2  (both terms safe).
    delta_S_bits = (4 * math.pi * G * (2 * M * m_proton + m_proton**2)
                    / (hbar * c * ln2))
    S_after = S_before + delta_S_bits

    # Hawking temperature at mass M
    T_hawking = hbar * c**3 / (8 * math.pi * G * M * k_B)

    # Landauer cost at Hawking temperature
    E_landauer_hawking = landauer_J(delta_S_bits, T_hawking)

    # Also at CMB temperature (comparison)
    E_landauer_cmb = landauer_J(delta_S_bits, T_cmb)

    # Proton rest mass energy
    E_proton_mass = m_proton * c**2

    return {
        "process": "black_hole_absorbs_proton",
        "description": "10 solar mass black hole absorbs one proton",
        "M_black_hole_kg": M,
        "M_solar_masses": 10,
        "m_proton_kg": m_proton,
        "S_BH_before_bits": S_before,
        "S_BH_after_bits": S_after,
        "delta_S_bits": delta_S_bits,
        "T_hawking_K": T_hawking,
        "T_cmb_K": T_cmb,
        "E_landauer_at_T_hawking_J": E_landauer_hawking,
        "E_landauer_at_T_cmb_J": E_landauer_cmb,
        "E_proton_rest_mass_J": E_proton_mass,
        "ratio_landauer_hawking_to_proton_mass_energy": (
            E_landauer_hawking / E_proton_mass if E_proton_mass > 0 else 0.0),
        "note": (
            "10 M_sun BH: S_BH = {:.4e} bits. Adding one proton adds {:.4e} bits. "
            "Hawking temperature: {:.4e} K. Landauer cost at T_H: {:.4e} J. "
            "Proton rest-mass energy: {:.4e} J. "
            "Landauer/mc² ratio: {:.4e}. "
            "At T_H, the Landauer cost of the state change is much less than mc².".format(
                S_before, delta_S_bits, T_hawking,
                E_landauer_hawking, E_proton_mass,
                E_landauer_hawking / E_proton_mass if E_proton_mass > 0 else 0.0)
        ),
    }

# ── Cross-scale comparison ────────────────────────────────────────────────────

def cross_scale_comparison(neuron, dna, photon, macro, bh):
    """
    Summarise across scales: K-bits, Landauer cost at each process's natural temperature,
    and energy per bit.
    """
    rows = [
        {
            "process":         "neuron_firing",
            "K_bits":          neuron["K_bits"],
            "T_K":             neuron["T_body_K"],
            "E_landauer_J":    neuron["E_landauer_body_J"],
            "E_actual_J":      neuron["E_biological_measured_J"],
            "scale":           "biological",
        },
        {
            "process":         "dna_mutation",
            "K_bits":          dna["K_bits"],
            "T_K":             dna["T_body_K"],
            "E_landauer_J":    dna["E_landauer_body_J"],
            "E_actual_J":      dna["E_polymerase_J"],
            "scale":           "molecular",
        },
        {
            "process":         "photon_absorption",
            "K_bits":          photon["K_bits"],
            "T_K":             photon["T_room_K"],
            "E_landauer_J":    photon["E_landauer_room_J"],
            "E_actual_J":      photon["E_photon_J"],
            "scale":           "quantum",
        },
        {
            "process":         "macro_move_1mm_measured",
            "K_bits":          macro["K_bits_measurement_precision_1um"],
            "T_K":             macro["T_room_K"],
            "E_landauer_J":    macro["E_landauer_measurement_J"],
            "E_actual_J":      None,
            "scale":           "macroscopic",
        },
        {
            "process":         "black_hole_absorbs_proton",
            "K_bits":          bh["delta_S_bits"],
            "T_K":             bh["T_hawking_K"],
            "E_landauer_J":    bh["E_landauer_at_T_hawking_J"],
            "E_actual_J":      bh["E_proton_rest_mass_J"],
            "scale":           "cosmological",
        },
    ]

    # Sort by K_bits ascending
    rows.sort(key=lambda r: r["K_bits"])
    return rows

# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("=" * 70)
    print("Landauer Change — Thermodynamic Cost of K-Information Updates")
    print("=" * 70)
    print()
    print("Landauer's principle: erasing 1 bit costs k_B T ln(2) joules.")
    print("If change = K(S2|S1) new bits, then change has thermodynamic cost.")
    print(f"  k_B = {k_B:.6e} J/K")
    print(f"  T_body = {T_body} K,  T_room = {T_room} K,  T_cmb = {T_cmb} K")
    print(f"  Landauer unit at T_body: {landauer_J(1.0, T_body):.4e} J/bit")
    print(f"  Landauer unit at T_room: {landauer_J(1.0, T_room):.4e} J/bit")
    print(f"  Landauer unit at T_cmb:  {landauer_J(1.0, T_cmb):.4e} J/bit")
    print()

    # ── Process results ──────────────────────────────────────────────────────
    neuron = neuron_firing()
    dna    = dna_mutation()
    photon = photon_absorption()
    macro  = macro_object_move()
    bh     = black_hole_proton()

    # ── Neuron ───────────────────────────────────────────────────────────────
    print("── 1. Neuron Firing ──")
    print(f"   K-change:          {neuron['K_bits']:.1f} bit  (threshold crossing: fire/no fire)")
    print(f"   Landauer floor:    {neuron['E_landauer_body_J']:.4e} J  at T={T_body} K")
    print(f"   Measured cost:     {neuron['E_biological_measured_J']:.2e} J  (ATP per action potential)")
    print(f"   Slack factor:      {neuron['thermodynamic_slack_factor']:.2e}x above Landauer minimum")
    print(f"   {neuron['note']}")
    print()

    # ── DNA ──────────────────────────────────────────────────────────────────
    print("── 2. DNA Base-Pair Mutation ──")
    print(f"   K-change:          {dna['K_bits']:.4f} bits  (log2(4) bases = 2 bits)")
    print(f"   Landauer floor:    {dna['E_landauer_body_J']:.4e} J  at T={T_body} K")
    print(f"   Polymerase cost:   {dna['E_polymerase_J']:.2e} J  (~50 k_B T per bp)")
    print(f"   Slack factor:      {dna['thermodynamic_slack_factor']:.2f}x above Landauer minimum")
    print(f"   {dna['note']}")
    print()

    # ── Photon ───────────────────────────────────────────────────────────────
    print("── 3. Photon Absorption (500 nm, visible) ──")
    print(f"   K-change:          {photon['K_bits']:.1f} bit  (2-level atom: ground vs excited)")
    print(f"   Photon energy:     {photon['E_photon_eV']:.4f} eV  = {photon['E_photon_J']:.4e} J")
    print(f"   Landauer floor:    {photon['E_landauer_room_eV']:.6f} eV = {photon['E_landauer_room_J']:.4e} J at T={T_room} K")
    print(f"   Slack factor:      {photon['thermodynamic_slack_factor']:.0f}x — photon carries ~{photon['thermodynamic_slack_factor']:.0f}× more energy than the 1-bit update needs")
    print(f"   {photon['note']}")
    print()

    # ── Macro object ─────────────────────────────────────────────────────────
    print("── 4. Macroscopic Object Moving 1 mm ──")
    print(f"   Thermal de Broglie wavelength (1g, {T_room}K): {macro['thermal_deBroglie_m']:.3e} m")
    print(f"   K-bits (thermal precision):    {macro['K_bits_thermal_precision']:.1f} bits")
    print(f"   Landauer (thermal):            {macro['E_landauer_thermal_J']:.3e} J")
    print(f"   K-bits (1 µm measurement):     {macro['K_bits_measurement_precision_1um']:.1f} bits")
    print(f"   Landauer (1 µm):               {macro['E_landauer_measurement_J']:.3e} J")
    print(f"   {macro['note']}")
    print()

    # ── Black hole ───────────────────────────────────────────────────────────
    print("── 5. Black Hole Absorbs One Proton ──")
    print(f"   Black hole mass:     10 M_sun = {bh['M_black_hole_kg']:.3e} kg")
    print(f"   Hawking temperature: {bh['T_hawking_K']:.4e} K  (extremely cold)")
    print(f"   S_BH before:         {bh['S_BH_before_bits']:.6e} bits")
    print(f"   S_BH after:          {bh['S_BH_after_bits']:.6e} bits")
    print(f"   ΔS_BH (K-change):    {bh['delta_S_bits']:.6e} bits")
    print(f"   Landauer at T_H:     {bh['E_landauer_at_T_hawking_J']:.4e} J")
    print(f"   Proton rest mass:    {bh['E_proton_rest_mass_J']:.4e} J  (mc²)")
    print(f"   Landauer / mc²:      {bh['ratio_landauer_hawking_to_proton_mass_energy']:.4e}")
    print(f"   Landauer at T_cmb:   {bh['E_landauer_at_T_cmb_J']:.4e} J  (for reference)")
    print(f"   {bh['note']}")
    print()

    # ── Multi-temperature table ───────────────────────────────────────────────
    print("── Landauer cost per process at three temperatures ──")
    print(f"{'Process':<30} {'K_bits':>12} {'@T_body(J)':>14} {'@T_room(J)':>14} {'@T_cmb(J)':>14}")
    print("─" * 86)

    processes = [
        ("neuron_firing",        neuron["K_bits"]),
        ("dna_mutation",         dna["K_bits"]),
        ("photon_absorption",    photon["K_bits"]),
        ("macro_1mm(1um meas)",  macro["K_bits_measurement_precision_1um"]),
        ("macro_1mm(thermal)",   macro["K_bits_thermal_precision"]),
        ("BH+proton (dS)",       bh["delta_S_bits"]),
    ]

    temp_table = []
    for name, bits in processes:
        E_b = landauer_J(bits, T_body)
        E_r = landauer_J(bits, T_room)
        E_c = landauer_J(bits, T_cmb)
        print(f"{name:<30} {bits:>12.4g} {E_b:>14.4e} {E_r:>14.4e} {E_c:>14.4e}")
        temp_table.append({
            "process": name,
            "K_bits": bits,
            "E_landauer_T_body_J": E_b,
            "E_landauer_T_room_J": E_r,
            "E_landauer_T_cmb_J": E_c,
        })
    print()

    # ── Cross-scale comparison ────────────────────────────────────────────────
    comparison = cross_scale_comparison(neuron, dna, photon, macro, bh)
    print("── Cross-scale comparison (sorted by K-bits) ──")
    print(f"{'Process':<30} {'Scale':<15} {'K_bits':>10} {'E_Landauer(J)':>16} {'E_actual(J)':>14} {'slack':>10}")
    print("─" * 97)
    for row in comparison:
        if row["E_actual_J"] is None or row["E_landauer_J"] == 0:
            slack_str = "N/A"
        else:
            slack_str = f"{row['E_actual_J']/row['E_landauer_J']:.2e}x"
        actual_str = "N/A" if row["E_actual_J"] is None else f"{row['E_actual_J']:.3e}"
        print(f"{row['process']:<30} {row['scale']:<15} {row['K_bits']:>10.4g} "
              f"{row['E_landauer_J']:>16.4e} {actual_str:>14} {slack_str:>10}")
    print()

    # ── Key findings ──────────────────────────────────────────────────────────
    print("── KEY FINDINGS ──")
    print()
    print("1. CHANGE HAS A LANDAUER FLOOR.")
    print("   Every K-information update costs >= k_B T ln(2) per bit.")
    print("   This is the MINIMUM energy dissipated in any real physical change.")
    print("   Real processes (neurons, DNA polymerase, photon absorption) are all")
    print(f"   orders of magnitude above this floor — the smallest slack is the photon")
    print(f"   (~{photon['thermodynamic_slack_factor']:.0f}x), the largest is the neuron (~{neuron['thermodynamic_slack_factor']:.2e}x).")
    print()
    print("2. K-BITS SCALE WITH PHYSICAL COMPLEXITY, NOT SIZE.")
    print("   A neuron firing: 1 bit. A DNA mutation: 2 bits.")
    print("   A photon absorption: 1 bit (2-level system).")
    print(f"   A macroscopic 1g object moving 1mm: {macro['K_bits_thermal_precision']:.0f} bits at thermal precision,")
    print(f"   but only {macro['K_bits_measurement_precision_1um']:.1f} bits at laboratory measurement precision.")
    print(f"   A black hole absorbing a proton: {bh['delta_S_bits']:.4e} bits (Bekenstein entropy jump).")
    print("   K-change is NOT proportional to the physical SIZE of the system —")
    print("   it's proportional to the INFORMATION CONTENT of the state transition.")
    print()
    print("3. THE THERMODYNAMIC SIGNATURE OF CHANGE IS REAL.")
    print("   Landauer's principle is experimentally verified (Bérut et al. 2012).")
    print("   If K-change = physical change, then every change leaves a thermodynamic")
    print("   signature: heat dissipated >= k_B T ln(2) × K(S2|S1) bits.")
    print("   This grounds the claim that 'change is real': real change must dissipate energy.")
    print("   A purely block-universe 'change' (no dissipation) is not K-change.")
    print()
    print("4. BLACK HOLE: INFORMATION PRESERVING AT THE BOUNDARY.")
    bh_bits = bh["delta_S_bits"]
    print(f"   Absorbing one proton adds {bh_bits:.3e} bits to the horizon entropy.")
    print(f"   This is {bh_bits / neuron['K_bits']:.3e}x the information content of a neuron firing.")
    print(f"   Hawking temperature ({bh['T_hawking_K']:.3e} K) is far below T_cmb ({T_cmb} K),")
    print(f"   so the black hole radiates no thermal photons in practice — the bits are")
    print(f"   'frozen' on the horizon. The K-change is real (Bekenstein entropy increases)")
    print(f"   but the Landauer dissipation is deferred until Hawking evaporation.")
    print()
    print("5. CAUSAL CONNECTION (R1 from gap.md).")
    print("   The compression view of change is best supported by INTERVENTIONIST causation.")
    print("   Reason: each K-information update requires an intervention that costs >= k_B T ln(2).")
    print("   If there is no thermodynamic intervention, K(S2|S1) = 0 and there is no change.")
    print("   Regularity theories can't distinguish K-change from K-identity (stopped clock).")
    print("   Interventionism CAN: an intervention IS a bit-erasure event with Landauer cost.")
    print("   Therefore: Landauer = thermodynamic operationalisation of interventionist causation.")
    print()
    print("6. PHENOMENAL FLOW (R3 from gap.md).")
    print("   Physical change = K-information update with thermodynamic cost.")
    print("   Phenomenal flow = the self-model's TRACKING of K-changes in the body/environment.")
    print("   The experience of 'time flowing' is the neural system doing K-updates at ~1 bit")
    print("   per cognitive event, each costing ~10^9 × Landauer (neural overhead).")
    print("   The felt 'rate' of flow tracks the rate of K-changes per unit time:")
    print("   high K-rate → time feels fast; low K-rate (boredom, anaesthesia) → time slows.")
    print()

    # ── Save ──────────────────────────────────────────────────────────────────
    os.makedirs("results", exist_ok=True)

    manifest = {
        "constants": {
            "k_B_J_per_K": k_B,
            "G_m3_per_kg_s2": G,
            "hbar_J_s": hbar,
            "c_m_per_s": c,
            "m_proton_kg": m_proton,
            "T_body_K": T_body,
            "T_room_K": T_room,
            "T_cmb_K": T_cmb,
        },
        "processes": {
            "neuron_firing": neuron,
            "dna_mutation": dna,
            "photon_absorption": photon,
            "macro_object_move": macro,
            "black_hole_proton": bh,
        },
        "temperature_table": temp_table,
        "cross_scale_comparison": comparison,
    }

    with open("results/landauer_data.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Data → results/landauer_data.json")

    return manifest

if __name__ == "__main__":
    run()
