#!/usr/bin/env python3
"""
brain_k_flow.py — K-information flow rate in the human brain.

The quantum_K_change.py script established:
- Unitary evolution: K-change = 0 (no new information, just rotation)
- Quantum measurement/decoherence: K-change = -log2(P(outcome)) bits per event

The brain is a decoherence machine: neural activity converts quantum uncertainty
into classical K-information at a measurable rate.

This script computes:
1. Estimated decoherence events per second in the brain
2. K-information flow rate (bits/second)
3. Landauer energy cost of this K-flow
4. Compare to actual brain power consumption (20W)
5. Compare to sensory channel capacities (vision, hearing, etc.)

The key connection to gap.md R3: "physical change vs phenomenal flow."
If phenomenal change = K-information update at the neural decoherence timescale,
then the rate of experienced events should be ~the rate of K-information updates.

Numerical track, what_is_change — 2026-04-09
"""

import math, json, os

k_B  = 1.380649e-23  # J/K
hbar = 1.054571817e-34  # J·s
c    = 2.998e8  # m/s
eV   = 1.602e-19  # J

T_brain = 310.0  # K

# ── Neural K-information estimates ───────────────────────────────────────────

# 1. Neuron firing
neurons = 8.6e10          # ~86 billion neurons in brain
firing_rate = 10.0        # average Hz (some neurons fire at 1, others at 100)
bits_per_firing = 1.0     # 1 bit: fire or not fire (simplest model)
k_flow_neurons = neurons * firing_rate * bits_per_firing  # bits/second

# 2. Synaptic transmission
synapses = 1.5e14         # ~150 trillion synapses
synapse_rate = 10.0       # Hz average (follows neuron firing)
bits_per_synapse = 1.0    # 1 bit: release or not release
k_flow_synapses = synapses * synapse_rate * bits_per_synapse  # bits/second

# 3. Ion channel decoherence
# Each ion channel decision is a quantum event (Na+, K+ channel open/close)
# Each neuron has ~10^9 ion channels
ion_channels_per_neuron = 1e9
decoherence_rate_per_channel = 1e3  # Hz (channel gating timescale ~1ms)
active_neurons = neurons * 0.01    # ~1% active at any time
k_flow_ion_channels = active_neurons * ion_channels_per_neuron * decoherence_rate_per_channel * 1.0  # bits/s

# 4. Protein conformational changes
# ATP hydrolysis, protein folding, signaling
proteins_per_cell = 1e9
protein_rate = 1e3        # Hz conformational changes
cells_brain = 1.4e11      # neurons + glia
k_flow_proteins = cells_brain * proteins_per_cell * protein_rate * 1.0  # bits/s

# ── Landauer energy costs ─────────────────────────────────────────────────────
landauer_per_bit = k_B * T_brain * math.log(2)  # J per bit erased

def landauer_power(k_bits_per_s):
    return k_bits_per_s * landauer_per_bit  # watts

brain_power_actual = 20.0  # W (typical brain metabolic power)

# ── Sensory channel capacities ────────────────────────────────────────────────
# (bits per second entering the brain from each sense)
sensory_channels = {
    "visual_retina_total":    1.5e9,     # ~1.5 Gbps from both retinas (raw photoreceptor)
    "visual_optic_nerve":     2.0e7,     # ~20 Mbps through optic nerve (after compression)
    "auditory":               3.0e6,     # ~3 Mbps (cochlea)
    "tactile":                1.0e6,     # ~1 Mbps (skin receptors)
    "olfactory":              3.0e5,     # ~300 kbps (olfactory neurons)
    "gustatory":              1.0e4,     # ~10 kbps (taste receptors)
    "proprioceptive":         1.0e6,     # ~1 Mbps (muscle spindles)
    "vestibular":             1.0e5,     # ~100 kbps
}
total_sensory_inflow = sum(sensory_channels.values())

# Conscious awareness bandwidth (estimated from psychophysics)
conscious_bandwidth = 50.0    # bits/second (what we can consciously process)
subconscious_processing = 1.1e7  # bits/second (subconscious integration)

# ── Temporal scale of "now" ───────────────────────────────────────────────────
# "The perceived present" (psychological present, specious present): ~3 seconds
# This is the window over which events feel simultaneous
specious_present = 3.0  # seconds
k_per_specious_present_conscious = conscious_bandwidth * specious_present
k_per_specious_present_subconscious = subconscious_processing * specious_present
k_per_specious_present_neural = k_flow_neurons * specious_present

# ── Main output ───────────────────────────────────────────────────────────────

def run():
    print("=" * 65)
    print("K-Information Flow Rate in the Human Brain")
    print("=" * 65)

    print(f"\nLandauer energy per bit at T={T_brain}K: {landauer_per_bit:.4e} J")

    print(f"\n── K-flow estimates (bits/second) ──")
    estimates = [
        ("Neuron firing", k_flow_neurons),
        ("Synaptic transmission", k_flow_synapses),
        ("Ion channel decoherence", k_flow_ion_channels),
        ("Protein conformational", k_flow_proteins),
    ]
    for name, rate in estimates:
        power = landauer_power(rate)
        slack = brain_power_actual / power if power > 0 else float('inf')
        print(f"  {name:<30}: {rate:.2e} bits/s → {power:.2e} W ({slack:.2e}× slack)")

    print(f"\n  Actual brain power:  {brain_power_actual:.1f} W")

    print(f"\n── Sensory channel inflow (bits/second) ──")
    for sense, rate in sorted(sensory_channels.items(), key=lambda x: -x[1]):
        print(f"  {sense:<30}: {rate:.2e} bits/s")
    print(f"  Total sensory inflow: {total_sensory_inflow:.2e} bits/s")
    print(f"  Conscious bandwidth:  {conscious_bandwidth:.0f} bits/s")
    print(f"  Compression ratio (sensory→conscious): {total_sensory_inflow/conscious_bandwidth:.2e}:1")

    print(f"\n── K-information in the 'specious present' (t={specious_present}s window) ──")
    print(f"  Conscious:    {k_per_specious_present_conscious:.1f} bits (50 b/s × 3s)")
    print(f"  Subconscious: {k_per_specious_present_subconscious:.2e} bits")
    print(f"  Neural total: {k_per_specious_present_neural:.2e} bits")
    print(f"  Sensory:      {total_sensory_inflow * specious_present:.2e} bits")

    print(f"\n── The bottleneck: conscious experience filters ~50 bits/s from 10^9 bits/s ──")
    print(f"  Ratio: {total_sensory_inflow/conscious_bandwidth:.2e}:1 compression from retina to awareness")
    print(f"  K-information view: the brain is a massive K-compressor")
    print(f"    Input: {total_sensory_inflow:.2e} bits/s (raw sensory)")
    print(f"    Output: {conscious_bandwidth:.0f} bits/s (conscious experience)")
    print(f"    Compression: {total_sensory_inflow/conscious_bandwidth:.2e}:1")
    print()
    print(f"  The 'phenomenal flow of time' (gap.md R3) may correspond to the")
    print(f"  ~50 bits/s of K-information entering conscious experience.")
    print(f"  Each 'moment' in the specious present contains ~150 bits of conscious K.")
    print()
    print(f"  Compare to Landauer floor for conscious bandwidth:")
    power_conscious = landauer_power(conscious_bandwidth)
    print(f"  Landauer cost for 50 bits/s: {power_conscious:.4e} W")
    print(f"  Actual brain power: 20 W")
    print(f"  Slack: {brain_power_actual / power_conscious:.2e}×")
    print(f"  The brain is {brain_power_actual/power_conscious:.2e}× above the Landauer minimum")
    print(f"  for conscious K-processing — immense waste by K standards,")
    print(f"  but efficient by biological standards (ATP hydrolysis overhead).")

    print(f"\n── Connection to time's arrow ──")
    print(f"  Each decoherence event in the brain is a K-change event (1+ bits).")
    print(f"  Neural timescale: ~1ms (neuron firing) = 10^3 Hz per neuron")
    print(f"  Decoherence timescale: ~10^-13 s (warm wet biological quantum decoherence)")
    print(f"  The 'phenomenal present' (~3s) integrates:")
    print(f"    - ~{neurons * firing_rate * specious_present:.2e} neuron firings")
    print(f"    - ~{k_per_specious_present_neural:.2e} bits of neural K-update")
    print(f"    - ~{conscious_bandwidth * specious_present:.0f} bits of conscious K-update")
    print()
    print(f"  The 'experienced present' is defined by a K-integration window:")
    print(f"  the brain integrates K-updates over ~3 seconds into a coherent 'now'.")
    print(f"  This is the temporal equivalent of a compression pass: 3s of K-flow")
    print(f"  is integrated into one moment of phenomenal experience.")

    # Save
    os.makedirs("results", exist_ok=True)
    manifest = {
        "T_brain_K": T_brain,
        "landauer_per_bit_J": landauer_per_bit,
        "k_flow_rates_bits_per_s": dict(estimates),
        "brain_power_actual_W": brain_power_actual,
        "sensory_channels": sensory_channels,
        "total_sensory_inflow_bits_per_s": total_sensory_inflow,
        "conscious_bandwidth_bits_per_s": conscious_bandwidth,
        "specious_present_s": specious_present,
        "conscious_compression_ratio": total_sensory_inflow / conscious_bandwidth,
        "landauer_cost_conscious_W": landauer_power(conscious_bandwidth),
        "slack_conscious": brain_power_actual / landauer_power(conscious_bandwidth),
    }
    with open("results/brain_k_flow_data.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest → results/brain_k_flow_data.json")

if __name__ == "__main__":
    run()
