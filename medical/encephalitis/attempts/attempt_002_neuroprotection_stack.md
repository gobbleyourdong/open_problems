# Attempt 002: Neuroprotection Stack — Saving Neurons During CVB Encephalitis

## The Problem Restated
Attempt 001 focused on killing the virus urgently. But neurons die from TWO sources:
1. Direct viral cytolysis (virus kills the neuron)
2. Bystander damage from neuroinflammation (activated microglia kill neighboring neurons)

In many CNS infections, bystander damage exceeds direct viral damage. The immune response to the infection kills more neurons than the infection itself.

## The Neuroprotection Stack

### Layer 1: Anti-excitotoxicity
Dying neurons release glutamate → excitotoxic cascade in neighbors → more death.

| Agent | Mechanism | Status |
|-------|-----------|--------|
| **Memantine** | NMDA receptor antagonist → blocks excitotoxic Ca²⁺ influx | FDA-approved (Alzheimer's), well-tolerated, IV formulation exists |
| **Magnesium sulfate** | Natural NMDA channel blocker (Mg²⁺ sits in channel pore) | Cheap, IV, used in eclampsia — well-characterized in acute settings |
| **Ketamine** (low-dose) | NMDA antagonist + anti-inflammatory | ICU setting, sedative properties actually useful in encephalitis |

### Layer 2: Anti-microglial activation
Microglia are brain-resident macrophages. Once activated, they produce TNF-α, IL-1β, ROS → bystander neuronal death.

| Agent | Mechanism | Status |
|-------|-----------|--------|
| **Minocycline** | Directly inhibits microglial activation (independent of antibiotic activity) | FDA-approved, crosses BBB, neuroprotective in multiple models |
| **BHB (exogenous ketones)** | NLRP3 suppression in microglia → reduced IL-1β | Already in protocol; IV ketone ester or sodium BHB |
| **Ibudilast** | PDE4/PDE10 inhibitor → cAMP ↑ → microglial deactivation | Approved in Japan for cerebrovascular disease; used in MS trials |

### Layer 3: Mitochondrial protection
Neuronal mitochondria are damaged by inflammatory ROS → energy failure → cell death.

| Agent | Mechanism | Status |
|-------|-----------|--------|
| **CoQ10 (ubiquinol)** | Electron carrier in complex III, antioxidant | Oral/NG tube, 400mg/day |
| **N-acetylcysteine (NAC)** | Glutathione precursor → ROS scavenging | IV available, used in acetaminophen OD, well-characterized |
| **Edaravone** | Free radical scavenger | Approved in Japan/US for ALS, IV formulation |

### Layer 4: Blood-brain barrier protection
Preventing further viral entry and reducing immune cell infiltration.

| Agent | Mechanism | Status |
|-------|-----------|--------|
| **Dexamethasone** | Reduces BBB permeability, anti-edema | Already in attempt 001; short course (5-7 days) |
| **Statins** | Pleiotropic BBB-stabilizing effects | Cheap, oral, some neuroprotective data in stroke |

## The Complete Acute Encephalitis Protocol (Attempt 001 + 002 Combined)

```
HOUR 0-6 (Antiviral + Neuroprotection simultaneously):
  ANTIVIRAL:
    IVIG 1g/kg IV
    Fluoxetine 20mg via NG
    Pocapavir (compassionate use)
  
  NEUROPROTECTION:
    MgSO₄ 4g IV bolus then 1-2g/hr (NMDA block + neuroprotection)
    Minocycline 200mg IV then 100mg q12h (microglial suppression)
    NAC 150mg/kg IV over 1hr then 50mg/kg over 4hr (ROS scavenging)
    Dexamethasone 10mg IV (BBB protection, anti-edema)
  
  SUPPORTIVE:
    Levetiracetam 1g IV (seizure prophylaxis)
    ICU admission, ICP monitoring if GCS <12

DAY 1-7 (Sustain + Monitor):
    Continue all antiviral agents
    Continue MgSO₄ (taper after 72hr based on clinical response)
    Continue minocycline 100mg q12h
    BHB: ketone ester 25g TID or IV sodium BHB (NLRP3 + neuroprotection)
    CoQ10 400mg via NG (mitochondrial support)
    NAC continue at 70mg/kg/day
    Serial MRI: day 3, day 7 (track edema, necrosis, new lesions)
    Continuous EEG

DAY 7-28 (Recovery transition):
    Taper dexamethasone
    Continue minocycline (2 weeks total)
    Continue fluoxetine (6 months)
    Transition to oral: BHB, CoQ10, NAC, omega-3
    Begin neurorehabilitation when stable
    MRI at day 14, day 28

MONTH 1-6 (Chronic neuroprotection):
    Fluoxetine 20mg daily (antiviral + neuroprotective SSRI effects)
    BHB via ketogenic diet or exogenous ketones
    CoQ10 400mg daily
    Omega-3 3g EPA/DHA daily (DHA is structural in neuronal membranes)
    Vitamin D 5000 IU daily
    Monitor: neurocognitive testing monthly, MRI at 3 and 6 months
```

## The Key Insight: Minocycline

Minocycline is a tetracycline antibiotic that happens to have potent anti-microglial properties unrelated to its antibiotic action. It:
- Crosses BBB efficiently
- Inhibits microglial activation and proliferation
- Reduces TNF-α, IL-1β, NO production by microglia
- Protects neurons in models of stroke, TBI, MS, Parkinson's
- Is cheap ($15/month generic), oral, well-tolerated
- Has NO antiviral activity → doesn't interfere with immune clearance of CVB

**Minocycline is the "colchicine of the brain" — an anti-inflammatory that suppresses the damage-causing pathway without suppressing the virus-clearing pathway.**

## Status: NEUROPROTECTION PROTOCOL — combines antiviral (attempt 001) with neuroprotective stack
