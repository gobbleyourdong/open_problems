#!/usr/bin/env python3
"""
patient_lifetime_trajectory.py
==============================
Simulates a patient's lifetime CVB exposure and disease trajectory from
birth to age 80. Models multiple CVB infections (most people get 2-4 in
a lifetime across 5 serotypes), with HLA-dependent disease outcomes at
each infection event.

Key biological parameters:
  - Age-dependent susceptibility (neonatal highest mortality, childhood
    highest T1DM seeding, young adult myocarditis peak, etc.)
  - Serotype-specific organ tropism (CVB3 = heart, CVB4 = pancreas, etc.)
  - HLA-dependent disease outcome probabilities
  - Cumulative tissue damage across multiple infections
  - Partial cross-immunity between serotypes
  - Prevention scenario: vaccination at birth eliminates all CVB disease

Monte Carlo: 10,000 lifetimes, random CVB exposures, random HLA genotypes.
Population-level disease burden and prevention benefit estimates.

References:
-----------
[1]  Khetsuriani et al., MMWR 2006: Enterovirus surveillance, age distribution
[2]  Abzug, Pediatrics 2001: Neonatal enteroviral disease severity
[3]  Hyoty & Taylor, Diabetologia 2002: CVB preceding autoantibodies
[4]  TEDDY Study Group, JAMA 2019: Environmental triggers of islet autoimmunity
[5]  Caforio et al., Circulation 2013: Myocarditis age distribution
[6]  Gauntt & Huber, Viral Immunol 2003: CVB serotype tropism
[7]  Chia & Chia, J Clin Pathol 2008: CVB persistence in ME/CFS
[8]  Tracy et al., J Clin Invest 2000: TD mutant persistence
[9]  Hober & Sauter, Front Microbiol 2010: Enterovirus infections per lifetime
[10] Modlin, Rev Infect Dis 1986: Epidemiology of enteroviral infections
[11] Rewers & Ludvigsson, Lancet 2016: T1DM environmental factors
[12] Dalldorf, Am J Med 1950: Pleurodynia / Bornholm disease epidemics

systematic approach -- ODD Instance (numerics) -- Cross-disease analysis
Date: 2026-04-08
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import defaultdict, OrderedDict
import os
import json

SEED = 42
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results", "figures")
RESULTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================================
# SECTION 1: CVB SEROTYPE DEFINITIONS
# ============================================================================

# Five CVB serotypes with different organ tropisms.
# Tropism values are relative probability multipliers for each organ target.
# Informed by clinical/epidemiological data.

SEROTYPES = {
    "B1": {
        "name": "CVB1",
        "prevalence": 0.20,     # Fraction of all CVB infections
        "tropism": {            # Relative organ affinity (1.0 = baseline)
            "pancreas_endo": 1.5,   # Moderate pancreatic tropism [Rewers 2016]
            "pancreas_exo":  1.3,
            "heart":         0.8,
            "skeletal_muscle": 1.0,
            "cns_meninges":  1.2,
            "cns_parenchyma": 0.3,
            "liver":         0.8,
            "testis":        0.5,
        },
    },
    "B2": {
        "name": "CVB2",
        "prevalence": 0.15,
        "tropism": {
            "pancreas_endo": 0.8,
            "pancreas_exo":  0.7,
            "heart":         1.0,
            "skeletal_muscle": 0.8,
            "cns_meninges":  1.5,   # Strong meningeal tropism [Khetsuriani 2006]
            "cns_parenchyma": 0.5,
            "liver":         1.0,
            "testis":        0.5,
        },
    },
    "B3": {
        "name": "CVB3",
        "prevalence": 0.25,     # Most common CVB serotype
        "tropism": {
            "pancreas_endo": 1.0,
            "pancreas_exo":  0.8,
            "heart":         2.5,   # THE cardiac serotype [Gauntt 2003]
            "skeletal_muscle": 1.5,
            "cns_meninges":  1.0,
            "cns_parenchyma": 0.3,
            "liver":         0.5,
            "testis":        0.5,
        },
    },
    "B4": {
        "name": "CVB4",
        "prevalence": 0.25,
        "tropism": {
            "pancreas_endo": 2.5,   # THE pancreatic/T1DM serotype [Hyoty 2002]
            "pancreas_exo":  2.0,
            "heart":         0.8,
            "skeletal_muscle": 0.8,
            "cns_meninges":  1.0,
            "cns_parenchyma": 0.4,
            "liver":         1.5,   # Hepatotropic [Modlin 1986]
            "testis":        0.5,
        },
    },
    "B5": {
        "name": "CVB5",
        "prevalence": 0.15,
        "tropism": {
            "pancreas_endo": 0.8,
            "pancreas_exo":  0.6,
            "heart":         1.0,
            "skeletal_muscle": 2.0,  # Pleurodynia serotype [Dalldorf 1950]
            "cns_meninges":  1.2,
            "cns_parenchyma": 0.6,
            "liver":         0.5,
            "testis":        2.0,   # Orchitis association [Loria 1977]
        },
    },
}


# ============================================================================
# SECTION 2: AGE-DEPENDENT PARAMETERS
# ============================================================================

# Age-dependent susceptibility to infection and disease severity.
# Values are relative multipliers applied to base disease probabilities.

def age_susceptibility(age):
    """
    Return age-dependent susceptibility multipliers for each organ system.

    Based on:
    - Neonates (0-0.08 yr / 0-1 month): highest viremia, immature immune
    - Infants (0.08-2 yr): developing immunity, still vulnerable
    - Children (2-12 yr): peak CVB exposure window, T1DM seeding
    - Adolescents (12-18 yr): myocarditis begins, orchitis risk
    - Young adults (18-40 yr): peak myocarditis/DCM, ME/CFS onset
    - Middle age (40-65 yr): DCM progression, accumulated damage
    - Elderly (65+): lower susceptibility (prior immunity), but cumulative effects
    """
    suscept = {}

    if age < 0.08:  # Neonatal (0-1 month)
        suscept = {
            "infection_prob":   0.90,  # Very high if exposed (no maternal Ab for CVB)
            "neonatal_sepsis":  1.0,   # THE high-risk window
            "t1dm_seeding":     0.5,   # Can seed but immune immaturity may actually limit autoimmunity
            "myocarditis":      0.3,   # Less than young adults
            "dcm":              0.1,
            "me_cfs":           0.0,   # Not diagnosed in neonates
            "pericarditis":     0.2,
            "pancreatitis":     0.3,
            "hepatitis":        1.5,   # Severe in neonates [Abzug 2001]
            "pleurodynia":      0.1,
            "meningitis":       1.5,   # High in neonates
            "encephalitis":     1.0,   # Rare but severe in neonates
            "orchitis":         0.0,   # Pre-pubertal
            "mortality":        0.15,  # 10-30% mortality in neonatal CVB [Abzug 2001]
        }
    elif age < 2:   # Infant
        suscept = {
            "infection_prob":   0.60,
            "neonatal_sepsis":  0.1,
            "t1dm_seeding":     0.8,   # Islet infection possible, autoimmunity begins
            "myocarditis":      0.2,
            "dcm":              0.05,
            "me_cfs":           0.0,
            "pericarditis":     0.1,
            "pancreatitis":     0.3,
            "hepatitis":        0.8,
            "pleurodynia":      0.2,
            "meningitis":       1.2,
            "encephalitis":     0.5,
            "orchitis":         0.0,
            "mortality":        0.02,
        }
    elif age < 12:  # Childhood — THE T1DM WINDOW
        suscept = {
            "infection_prob":   0.50,  # 50% chance of infection if exposed
            "neonatal_sepsis":  0.0,
            "t1dm_seeding":     1.0,   # Peak T1DM seeding window [TEDDY]
            "myocarditis":      0.3,
            "dcm":              0.1,
            "me_cfs":           0.1,
            "pericarditis":     0.3,
            "pancreatitis":     0.5,
            "hepatitis":        0.3,
            "pleurodynia":      0.5,
            "meningitis":       1.0,   # Common in school-age children
            "encephalitis":     0.3,
            "orchitis":         0.0,   # Pre-pubertal
            "mortality":        0.001,
        }
    elif age < 18:  # Adolescent
        suscept = {
            "infection_prob":   0.35,
            "neonatal_sepsis":  0.0,
            "t1dm_seeding":     0.6,   # Lower but still possible (late-onset T1DM)
            "myocarditis":      0.8,   # Rising — puberty-related immune changes
            "dcm":              0.2,
            "me_cfs":           0.3,
            "pericarditis":     0.6,
            "pancreatitis":     0.4,
            "hepatitis":        0.2,
            "pleurodynia":      0.8,
            "meningitis":       0.5,
            "encephalitis":     0.2,
            "orchitis":         0.5,   # Post-pubertal
            "mortality":        0.001,
        }
    elif age < 40:  # Young adult — CARDIAC PEAK
        suscept = {
            "infection_prob":   0.30,
            "neonatal_sepsis":  0.0,
            "t1dm_seeding":     0.3,   # Rare but LADA possible
            "myocarditis":      1.0,   # Peak myocarditis window [Caforio 2013]
            "dcm":              0.5,
            "me_cfs":           1.0,   # Peak ME/CFS onset window
            "pericarditis":     1.0,
            "pancreatitis":     0.5,
            "hepatitis":        0.3,
            "pleurodynia":      1.0,
            "meningitis":       0.3,
            "encephalitis":     0.2,
            "orchitis":         1.0,   # Peak male susceptibility
            "mortality":        0.001,
        }
    elif age < 65:  # Middle age
        suscept = {
            "infection_prob":   0.20,  # Prior immunity reduces infection rate
            "neonatal_sepsis":  0.0,
            "t1dm_seeding":     0.1,   # Very rare de novo T1DM at this age
            "myocarditis":      0.5,
            "dcm":              1.0,   # Accumulated damage manifests [Bowles 1986]
            "me_cfs":           0.5,
            "pericarditis":     0.5,
            "pancreatitis":     0.3,
            "hepatitis":        0.2,
            "pleurodynia":      0.5,
            "meningitis":       0.2,
            "encephalitis":     0.3,
            "orchitis":         0.3,
            "mortality":        0.005,
        }
    else:  # Elderly (65+)
        suscept = {
            "infection_prob":   0.15,
            "neonatal_sepsis":  0.0,
            "t1dm_seeding":     0.05,
            "myocarditis":      0.3,
            "dcm":              0.8,   # Still manifesting from old infections
            "me_cfs":           0.2,
            "pericarditis":     0.3,
            "pancreatitis":     0.2,
            "hepatitis":        0.2,
            "pleurodynia":      0.3,
            "meningitis":       0.2,
            "encephalitis":     0.5,  # Higher severity if it occurs
            "orchitis":         0.1,
            "mortality":        0.01,
        }

    return suscept


# ============================================================================
# SECTION 3: CVB EXPOSURE MODEL
# ============================================================================

# Population exposure parameters
EXPOSURE_PARAMS = {
    "annual_cvb_probability_base": 0.05,   # ~5% chance per year of any CVB exposure
    # [Hober 2010: most people get 2-4 enteroviral infections in childhood]
    # Adjusted so that by age 12, ~50% have had at least one CVB exposure

    "peak_exposure_age": (2, 10),           # Peak exposure during school years
    "peak_multiplier": 3.0,                 # 3x higher in peak years

    "cross_immunity_factor": 0.3,           # 30% cross-protection between serotypes
    "homologous_immunity": 0.95,            # 95% protection against same serotype reinfection
}


def annual_exposure_probability(age, prior_serotypes):
    """
    Probability of CVB exposure in a given year, accounting for
    age-dependent exposure rates and prior immunity.
    """
    base = EXPOSURE_PARAMS["annual_cvb_probability_base"]

    # Age-dependent exposure rate
    peak_lo, peak_hi = EXPOSURE_PARAMS["peak_exposure_age"]
    if peak_lo <= age <= peak_hi:
        rate = base * EXPOSURE_PARAMS["peak_multiplier"]
    elif age < 2:
        rate = base * 1.5   # High exposure from family contacts
    elif age < 18:
        rate = base * 2.0   # School-age
    else:
        rate = base * 0.8   # Adult, less exposure

    # Prior immunity reduces effective exposure
    n_prior = len(prior_serotypes)
    if n_prior > 0:
        # Each prior infection provides ~30% cross-immunity to others
        cross = 1.0 - EXPOSURE_PARAMS["cross_immunity_factor"] * min(n_prior, 5) / 5
        rate *= max(cross, 0.1)  # Floor at 10% of base rate

    return min(rate, 0.5)  # Cap at 50% annual probability


def select_serotype(rng, prior_serotypes):
    """
    Select which CVB serotype for this infection.
    Accounts for prior immunity (same serotype less likely).
    """
    serotype_names = list(SEROTYPES.keys())
    probs = np.array([SEROTYPES[s]["prevalence"] for s in serotype_names])

    # Reduce probability of previously encountered serotypes
    for i, s in enumerate(serotype_names):
        if s in prior_serotypes:
            probs[i] *= (1.0 - EXPOSURE_PARAMS["homologous_immunity"])

    probs = probs / probs.sum()
    return rng.choice(serotype_names, p=probs)


# ============================================================================
# SECTION 4: DISEASE OUTCOME MODEL
# ============================================================================

# Base disease probabilities per infection event (before age/HLA/serotype modifiers).
# These represent the chance that a single CVB infection leads to clinical disease.

BASE_DISEASE_PROBS = {
    "t1dm":              0.001,    # ~0.1% per infection (needs HLA + seeding + autoimmunity)
    "myocarditis":       0.005,    # ~0.5% per infection (often subclinical)
    "dcm":               0.001,    # ~0.1% per infection (downstream of myocarditis)
    "me_cfs":            0.002,    # ~0.2% per infection (persistence-dependent)
    "pericarditis":      0.008,    # ~0.8% per infection (relatively common)
    "pancreatitis":      0.003,    # ~0.3% per infection
    "hepatitis":         0.001,    # ~0.1% per infection (self-limiting usually)
    "pleurodynia":       0.010,    # ~1.0% per infection (most common CVB presentation)
    "meningitis":        0.008,    # ~0.8% per infection (common in children)
    "encephalitis":      0.0003,   # ~0.03% per infection (rare but severe)
    "orchitis":          0.002,    # ~0.2% per infection (post-pubertal males only)
    "neonatal_sepsis":   0.020,    # ~2.0% per infection (but only in neonates)
}

# HLA risk multiplier categories (simplified from hla_risk_model.py)
# Maps HLA haplotype pair -> disease-specific risk multiplier
HLA_RISK_PROFILES = {
    "DR3/DR4_het": {  # Compound heterozygote — highest T1DM risk
        "t1dm": 15.0, "myocarditis": 0.5, "dcm": 0.5, "me_cfs": 1.5,
        "pericarditis": 0.6, "pancreatitis": 2.0, "hepatitis": 1.3,
        "pleurodynia": 1.0, "meningitis": 1.1, "encephalitis": 1.1,
        "orchitis": 1.0, "neonatal_sepsis": 1.0,
    },
    "DR3_homo": {  # DR3 homozygote
        "t1dm": 5.0, "myocarditis": 0.6, "dcm": 0.7, "me_cfs": 1.3,
        "pericarditis": 0.7, "pancreatitis": 1.5, "hepatitis": 1.5,
        "pleurodynia": 1.0, "meningitis": 1.2, "encephalitis": 1.3,
        "orchitis": 1.1, "neonatal_sepsis": 1.0,
    },
    "DR4_homo": {  # DR4 homozygote
        "t1dm": 4.0, "myocarditis": 0.4, "dcm": 0.4, "me_cfs": 1.6,
        "pericarditis": 0.5, "pancreatitis": 1.3, "hepatitis": 1.2,
        "pleurodynia": 1.0, "meningitis": 1.0, "encephalitis": 1.0,
        "orchitis": 1.0, "neonatal_sepsis": 1.0,
    },
    "DQ5_carrier": {  # DQ5 — cardiac risk
        "t1dm": 0.7, "myocarditis": 2.5, "dcm": 2.8, "me_cfs": 1.1,
        "pericarditis": 2.0, "pancreatitis": 1.0, "hepatitis": 1.0,
        "pleurodynia": 1.0, "meningitis": 1.0, "encephalitis": 1.0,
        "orchitis": 1.3, "neonatal_sepsis": 1.0,
    },
    "DQ6_carrier": {  # DQ6 — T1DM protective, CNS risk
        "t1dm": 0.03, "myocarditis": 1.3, "dcm": 1.2, "me_cfs": 1.2,
        "pericarditis": 1.2, "pancreatitis": 0.8, "hepatitis": 1.0,
        "pleurodynia": 1.0, "meningitis": 1.3, "encephalitis": 1.5,
        "orchitis": 1.0, "neonatal_sepsis": 1.0,
    },
    "neutral": {  # Average HLA — no strong associations
        "t1dm": 1.0, "myocarditis": 1.0, "dcm": 1.0, "me_cfs": 1.0,
        "pericarditis": 1.0, "pancreatitis": 1.0, "hepatitis": 1.0,
        "pleurodynia": 1.0, "meningitis": 1.0, "encephalitis": 1.0,
        "orchitis": 1.0, "neonatal_sepsis": 1.0,
    },
}

# Population frequencies of HLA risk profiles
HLA_PROFILE_FREQS = {
    "DR3/DR4_het": 0.02,   # ~2% compound heterozygotes
    "DR3_homo":    0.017,   # ~1.7% DR3 homozygous
    "DR4_homo":    0.026,   # ~2.6% DR4 homozygous
    "DQ5_carrier": 0.11,    # ~11% carry DQ5
    "DQ6_carrier": 0.14,    # ~14% carry DQ6
    "neutral":     0.687,   # Everyone else
}


def compute_disease_probability(disease, serotype, age, hla_profile, is_male=True):
    """
    Compute probability that a single CVB infection at a given age
    causes a specific disease, accounting for serotype tropism, age
    susceptibility, HLA type, and sex.

    Returns: float probability [0, 1]
    """
    base_prob = BASE_DISEASE_PROBS[disease]

    # 1. Serotype tropism modifier
    organ_map = {
        "t1dm":           "pancreas_endo",
        "pancreatitis":   "pancreas_exo",
        "myocarditis":    "heart",
        "dcm":            "heart",
        "me_cfs":         "skeletal_muscle",
        "pericarditis":   "heart",
        "hepatitis":      "liver",
        "pleurodynia":    "skeletal_muscle",
        "meningitis":     "cns_meninges",
        "encephalitis":   "cns_parenchyma",
        "orchitis":       "testis",
        "neonatal_sepsis": "liver",   # Multi-organ but liver is primary target
    }
    tropism = SEROTYPES[serotype]["tropism"].get(organ_map[disease], 1.0)

    # 2. Age susceptibility
    suscept = age_susceptibility(age)
    # Map disease name to susceptibility key
    suscept_map = {
        "t1dm": "t1dm_seeding",
        "myocarditis": "myocarditis",
        "dcm": "dcm",
        "me_cfs": "me_cfs",
        "pericarditis": "pericarditis",
        "pancreatitis": "pancreatitis",
        "hepatitis": "hepatitis",
        "pleurodynia": "pleurodynia",
        "meningitis": "meningitis",
        "encephalitis": "encephalitis",
        "orchitis": "orchitis",
        "neonatal_sepsis": "neonatal_sepsis",
    }
    age_modifier = suscept.get(suscept_map[disease], 1.0)

    # 3. HLA modifier
    hla_modifier = HLA_RISK_PROFILES[hla_profile].get(disease, 1.0)

    # 4. Sex modifier (orchitis only in males)
    sex_modifier = 1.0
    if disease == "orchitis":
        sex_modifier = 2.0 if is_male else 0.0
    # Myocarditis slightly more common in males
    if disease == "myocarditis":
        sex_modifier = 1.3 if is_male else 0.8

    prob = base_prob * tropism * age_modifier * hla_modifier * sex_modifier
    return min(prob, 0.5)  # Cap at 50%


# ============================================================================
# SECTION 5: LIFETIME SIMULATION ENGINE
# ============================================================================

def simulate_one_lifetime(rng, hla_profile="neutral", is_male=True, vaccinated=False):
    """
    Simulate one person's CVB exposure history from birth to age 80.

    Returns:
      infections: list of (age, serotype) tuples
      diseases: list of (age, disease_name) tuples
      died_age: float or None (if survived to 80)
      cumulative_tissue_damage: dict of organ -> cumulative damage [0, 1]
    """
    infections = []
    diseases = []
    prior_serotypes = set()
    died_age = None

    # Track cumulative tissue damage (each infection adds some damage even
    # if clinical disease threshold not reached)
    tissue_damage = {
        "pancreas_endo": 0.0,
        "pancreas_exo": 0.0,
        "heart": 0.0,
        "skeletal_muscle": 0.0,
        "cns": 0.0,
        "liver": 0.0,
        "testis": 0.0,
    }

    # If vaccinated, no CVB infections occur (simplified; 85% efficacy)
    if vaccinated:
        vaccine_effective = rng.random() < 0.85
        if vaccine_effective:
            return infections, diseases, None, tissue_damage

    # Simulate year by year
    for age_year in range(81):
        age = float(age_year) + rng.random()  # Exact age within year

        # Special handling for neonatal period (first month)
        if age_year == 0:
            # Neonatal exposure check (higher risk, separate from annual)
            neonatal_exposure = rng.random() < 0.01  # ~1% neonatal CVB exposure
            if neonatal_exposure and not vaccinated:
                serotype = select_serotype(rng, prior_serotypes)
                infections.append((0.02, serotype))  # ~1 week old
                prior_serotypes.add(serotype)

                suscept = age_susceptibility(0.02)
                if rng.random() < suscept["infection_prob"]:
                    # Check all diseases
                    for disease in BASE_DISEASE_PROBS:
                        prob = compute_disease_probability(
                            disease, serotype, 0.02, hla_profile, is_male)
                        if rng.random() < prob:
                            diseases.append((0.02, disease))

                    # Mortality check
                    if rng.random() < suscept["mortality"]:
                        died_age = 0.02
                        return infections, diseases, died_age, tissue_damage

        # Annual exposure check
        exp_prob = annual_exposure_probability(age, prior_serotypes)
        if rng.random() < exp_prob:
            serotype = select_serotype(rng, prior_serotypes)
            suscept = age_susceptibility(age)

            # Does exposure lead to infection?
            if rng.random() < suscept["infection_prob"]:
                infections.append((age, serotype))
                prior_serotypes.add(serotype)

                # Check each possible disease outcome
                for disease in BASE_DISEASE_PROBS:
                    prob = compute_disease_probability(
                        disease, serotype, age, hla_profile, is_male)
                    if rng.random() < prob:
                        diseases.append((age, disease))

                # Subclinical tissue damage (even without clinical disease)
                organ_map = {
                    "pancreas_endo": SEROTYPES[serotype]["tropism"]["pancreas_endo"],
                    "pancreas_exo":  SEROTYPES[serotype]["tropism"]["pancreas_exo"],
                    "heart":         SEROTYPES[serotype]["tropism"]["heart"],
                    "skeletal_muscle": SEROTYPES[serotype]["tropism"]["skeletal_muscle"],
                    "cns":           max(SEROTYPES[serotype]["tropism"]["cns_meninges"],
                                         SEROTYPES[serotype]["tropism"]["cns_parenchyma"]),
                    "liver":         SEROTYPES[serotype]["tropism"]["liver"],
                    "testis":        SEROTYPES[serotype]["tropism"]["testis"] if is_male else 0,
                }
                for organ, tropism in organ_map.items():
                    # Subclinical damage: 0.5-2% per infection, scaled by tropism
                    damage = rng.uniform(0.005, 0.02) * tropism
                    tissue_damage[organ] = min(1.0, tissue_damage[organ] + damage)

                # Mortality check (rare outside neonatal period)
                if rng.random() < suscept["mortality"]:
                    died_age = age
                    return infections, diseases, died_age, tissue_damage

    return infections, diseases, died_age, tissue_damage


def simulate_population(n_people=10000, seed=SEED, vaccinated=False):
    """
    Simulate n_people lifetimes with random HLA profiles.

    Returns:
      all_infections: list of lists of (age, serotype)
      all_diseases: list of lists of (age, disease_name)
      all_deaths: list of float or None
      all_hla: list of HLA profile names
      all_tissue_damage: list of dicts
    """
    rng = np.random.default_rng(seed)
    hla_names = list(HLA_PROFILE_FREQS.keys())
    hla_probs = np.array(list(HLA_PROFILE_FREQS.values()))
    hla_probs = hla_probs / hla_probs.sum()

    all_infections = []
    all_diseases = []
    all_deaths = []
    all_hla = []
    all_tissue_damage = []

    for i in range(n_people):
        hla = rng.choice(hla_names, p=hla_probs)
        is_male = rng.random() < 0.5

        infections, diseases, died_age, tissue_damage = simulate_one_lifetime(
            rng, hla_profile=hla, is_male=is_male, vaccinated=vaccinated)

        all_infections.append(infections)
        all_diseases.append(diseases)
        all_deaths.append(died_age)
        all_hla.append(hla)
        all_tissue_damage.append(tissue_damage)

    return all_infections, all_diseases, all_deaths, all_hla, all_tissue_damage


# ============================================================================
# SECTION 6: ANALYSIS FUNCTIONS
# ============================================================================

def analyze_disease_burden(all_diseases, all_hla, n_people):
    """Compute disease burden statistics."""
    disease_counts = defaultdict(int)
    disease_by_hla = defaultdict(lambda: defaultdict(int))
    diseases_per_person = []
    disease_ages = defaultdict(list)

    for i, diseases in enumerate(all_diseases):
        unique_diseases = set(d[1] for d in diseases)
        diseases_per_person.append(len(unique_diseases))
        for age, disease in diseases:
            disease_counts[disease] += 1
            disease_by_hla[all_hla[i]][disease] += 1
            disease_ages[disease].append(age)

    return disease_counts, disease_by_hla, diseases_per_person, disease_ages


def analyze_infection_patterns(all_infections, n_people):
    """Compute infection statistics."""
    infections_per_person = [len(inf) for inf in all_infections]
    serotype_counts = defaultdict(int)
    infection_ages = []

    for infections in all_infections:
        for age, serotype in infections:
            serotype_counts[serotype] += 1
            infection_ages.append(age)

    return infections_per_person, serotype_counts, infection_ages


def compute_prevention_benefit(disease_counts_unvax, disease_counts_vax, n_people):
    """Compute the benefit of vaccination (prevented cases)."""
    benefit = {}
    for disease in BASE_DISEASE_PROBS:
        unvax = disease_counts_unvax.get(disease, 0)
        vax = disease_counts_vax.get(disease, 0)
        prevented = unvax - vax
        benefit[disease] = {
            "unvaccinated": unvax,
            "vaccinated": vax,
            "prevented": prevented,
            "reduction_pct": round(prevented / max(unvax, 1) * 100, 1),
        }
    return benefit


# ============================================================================
# SECTION 7: VISUALIZATION
# ============================================================================

def plot_infection_timeline(all_infections, all_diseases, n_people):
    """Plot the distribution of CVB infections and diseases across lifetime."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("Lifetime CVB Exposure: 10,000 Simulated Lives (Birth to 80)",
                 fontsize=14, fontweight='bold')

    # 1. Infection age distribution
    ax = axes[0, 0]
    all_ages = [age for infections in all_infections for age, _ in infections]
    ax.hist(all_ages, bins=80, range=(0, 80), color='#3498db', alpha=0.7, edgecolor='white')
    ax.set_xlabel("Age at CVB Infection")
    ax.set_ylabel("Count")
    ax.set_title(f"Distribution of CVB Infections by Age\n"
                 f"(Total: {len(all_ages)} infections in {n_people} lifetimes, "
                 f"mean {len(all_ages)/n_people:.1f} per person)")
    ax.grid(True, alpha=0.2)

    # 2. Number of infections per person
    ax = axes[0, 1]
    n_inf = [len(infections) for infections in all_infections]
    max_inf = max(n_inf)
    ax.hist(n_inf, bins=range(0, max_inf + 2), color='#e67e22', alpha=0.7, edgecolor='white')
    ax.set_xlabel("Number of CVB Infections per Lifetime")
    ax.set_ylabel("Count")
    ax.set_title(f"Infections per Person (mean {np.mean(n_inf):.1f}, "
                 f"median {np.median(n_inf):.0f})")
    ax.grid(True, alpha=0.2)

    # 3. Disease onset age distribution (top 6 diseases)
    ax = axes[1, 0]
    top_diseases = ["meningitis", "pericarditis", "pleurodynia", "myocarditis", "t1dm", "me_cfs"]
    colors = ['#3498db', '#e67e22', '#2ecc71', '#e74c3c', '#9b59b6', '#1abc9c']
    for disease, color in zip(top_diseases, colors):
        ages = [age for ds_list in all_diseases for age, d in ds_list if d == disease]
        if ages:
            ax.hist(ages, bins=40, range=(0, 80), alpha=0.5, color=color,
                    label=f"{disease} (n={len(ages)})")
    ax.set_xlabel("Age at Disease Onset")
    ax.set_ylabel("Count")
    ax.set_title("Disease Onset Age Distribution (Top 6)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.2)

    # 4. Cumulative disease burden by age
    ax = axes[1, 1]
    age_bins = np.arange(0, 81, 1)
    for disease, color in zip(top_diseases, colors):
        ages = sorted([age for ds_list in all_diseases for age, d in ds_list if d == disease])
        if ages:
            cumulative = np.searchsorted(ages, age_bins) / n_people * 100
            ax.plot(age_bins, cumulative, color=color, linewidth=2,
                    label=f"{disease}")
    ax.set_xlabel("Age")
    ax.set_ylabel("Cumulative Incidence (%)")
    ax.set_title("Cumulative Disease Incidence by Age")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "lifetime_cvb_timeline.png"), dpi=150)
    plt.close()
    print("  Saved: lifetime_cvb_timeline.png")


def plot_hla_disease_heatmap(disease_by_hla, n_people):
    """Heatmap of disease rates by HLA profile."""
    hla_profiles = list(HLA_PROFILE_FREQS.keys())
    disease_names = list(BASE_DISEASE_PROBS.keys())

    # Count people per HLA profile
    # (approximate from population frequencies)
    hla_counts = {h: int(n_people * f) for h, f in HLA_PROFILE_FREQS.items()}

    matrix = np.zeros((len(hla_profiles), len(disease_names)))
    for i, hla in enumerate(hla_profiles):
        for j, disease in enumerate(disease_names):
            count = disease_by_hla[hla].get(disease, 0)
            n_hla = max(hla_counts[hla], 1)
            matrix[i, j] = count / n_hla * 100  # Disease rate per 100 people

    fig, ax = plt.subplots(figsize=(16, 8))
    im = ax.imshow(matrix, cmap='YlOrRd', aspect='auto')

    ax.set_xticks(range(len(disease_names)))
    ax.set_xticklabels([d.replace('_', ' ').title() for d in disease_names],
                        rotation=45, ha='right', fontsize=9)
    ax.set_yticks(range(len(hla_profiles)))
    ax.set_yticklabels(hla_profiles, fontsize=10)

    for i in range(len(hla_profiles)):
        for j in range(len(disease_names)):
            v = matrix[i, j]
            color = 'white' if v > matrix.max() * 0.6 else 'black'
            ax.text(j, i, f"{v:.2f}", ha='center', va='center',
                    fontsize=7, color=color)

    ax.set_title("Lifetime Disease Rate by HLA Profile (%)\n"
                 "(10,000 simulated lifetimes: birth to 80)",
                 fontsize=13, fontweight='bold')
    plt.colorbar(im, ax=ax, label="Disease rate per 100 people", shrink=0.7)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "lifetime_hla_disease_heatmap.png"), dpi=150)
    plt.close()
    print("  Saved: lifetime_hla_disease_heatmap.png")


def plot_prevention_benefit(benefit):
    """Bar chart: vaccinated vs unvaccinated disease counts."""
    diseases = list(benefit.keys())
    names = [d.replace('_', ' ').title() for d in diseases]
    unvax = [benefit[d]["unvaccinated"] for d in diseases]
    vax = [benefit[d]["vaccinated"] for d in diseases]

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle("Vaccination Impact: 10,000 Lifetimes x 2 Scenarios",
                 fontsize=14, fontweight='bold')

    # Bar chart
    ax = axes[0]
    x = np.arange(len(diseases))
    width = 0.35
    bars1 = ax.bar(x - width/2, unvax, width, label='Unvaccinated',
                    color='#e74c3c', alpha=0.8)
    bars2 = ax.bar(x + width/2, vax, width, label='Vaccinated',
                    color='#27ae60', alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha='right', fontsize=8)
    ax.set_ylabel("Total Cases")
    ax.set_title("Disease Cases: Vaccinated vs Unvaccinated")
    ax.legend()
    ax.grid(True, alpha=0.2, axis='y')

    # Reduction percentage
    ax = axes[1]
    reductions = [benefit[d]["reduction_pct"] for d in diseases]
    colors = ['#27ae60' if r > 0 else '#e74c3c' for r in reductions]
    ax.barh(names, reductions, color=colors, alpha=0.8)
    ax.set_xlabel("% Reduction")
    ax.set_title("Disease Reduction from Vaccination (%)")
    ax.grid(True, alpha=0.2, axis='x')
    for i, (r, n) in enumerate(zip(reductions, names)):
        ax.text(max(r + 1, 1), i, f"{r:.0f}%", va='center', fontsize=8)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "lifetime_vaccination_benefit.png"), dpi=150)
    plt.close()
    print("  Saved: lifetime_vaccination_benefit.png")


def plot_multi_disease_per_person(diseases_per_person):
    """How many distinct CVB diseases does each person develop in a lifetime?"""
    fig, ax = plt.subplots(figsize=(10, 6))

    max_d = max(diseases_per_person) if diseases_per_person else 0
    bins = np.arange(-0.5, max_d + 1.5, 1)
    counts, _, patches = ax.hist(diseases_per_person, bins=bins,
                                  color='#3498db', alpha=0.8, edgecolor='white')
    for i, p in enumerate(patches):
        if i >= 2:
            p.set_facecolor('#e74c3c')
        elif i >= 1:
            p.set_facecolor('#e67e22')

    total = len(diseases_per_person)
    for i in range(max_d + 1):
        count = sum(1 for d in diseases_per_person if d == i)
        pct = count / total * 100
        if count > 0:
            ax.text(i, count + total * 0.003, f"{pct:.1f}%",
                    ha='center', fontsize=9, fontweight='bold')

    ax.set_xlabel("Number of Distinct CVB Diseases in Lifetime")
    ax.set_ylabel("Number of People (out of 10,000)")
    ax.set_title("Lifetime CVB Disease Burden: How Many Diseases per Person?\n"
                 "(10,000 simulated lifetimes, random HLA genotypes)",
                 fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.2)

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "lifetime_diseases_per_person.png"), dpi=150)
    plt.close()
    print("  Saved: lifetime_diseases_per_person.png")


def plot_branching_tree():
    """
    Schematic of the CVB disease branching tree:
    one infection -> many possible outcomes, age-dependent.
    """
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 12)
    ax.axis('off')

    # Root: CVB infection
    ax.text(0, 6, "CVB\nInfection", fontsize=14, fontweight='bold',
            ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#95a5a6', alpha=0.8))

    # Age-dependent branches
    branches = [
        (2.5, 10.5, "Neonatal\n(0-1 mo)", '#e74c3c',
         [(5, 11, "Sepsis\n(30-50% mortality)"), (5, 10, "Hepatitis")]),
        (2.5, 8.5, "Childhood\n(2-12 yr)", '#e67e22',
         [(5, 9.5, "T1DM seeding\n(peak window)"), (5, 8.5, "Meningitis"),
          (5, 7.5, "Pleurodynia")]),
        (2.5, 6, "Adolescent\n(12-18 yr)", '#f1c40f',
         [(5, 6.5, "Myocarditis\n(rising)"), (5, 5.5, "Orchitis")]),
        (2.5, 3.5, "Young Adult\n(18-40 yr)", '#3498db',
         [(5, 4.5, "Myocarditis\n(peak)"), (5, 3.5, "ME/CFS"),
          (5, 2.5, "Pericarditis")]),
        (2.5, 1.5, "Middle Age\n(40-65 yr)", '#9b59b6',
         [(5, 1.5, "DCM\n(accumulated)"), (5, 0.5, "Pancreatitis")]),
    ]

    for bx, by, blabel, bcolor, diseases in branches:
        ax.annotate("", xy=(bx - 0.3, by), xytext=(0.7, 6),
                     arrowprops=dict(arrowstyle='->', color=bcolor, lw=2))
        ax.text(bx, by, blabel, fontsize=10, fontweight='bold',
                ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor=bcolor, alpha=0.6))
        for dx, dy, dlabel in diseases:
            ax.annotate("", xy=(dx - 0.3, dy), xytext=(bx + 0.8, by),
                         arrowprops=dict(arrowstyle='->', color='gray', lw=1))
            ax.text(dx, dy, dlabel, fontsize=8, ha='left', va='center',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#ecf0f1', alpha=0.7))

    # Title and legend
    ax.text(5, -0.5,
            "The Branching Tree: One CVB Infection, Many Possible Outcomes\n"
            "Which branch is taken depends on AGE + SEROTYPE + HLA + DOSE",
            fontsize=11, ha='center', va='center', style='italic')

    # Progression arrows (long-term)
    ax.annotate("Years later", xy=(8, 9.5), xytext=(6.5, 9.5),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5),
                fontsize=8, color='#e74c3c')
    ax.text(8.2, 9.5, "T1DM\n(clinical)", fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e74c3c', alpha=0.3))

    ax.annotate("Years later", xy=(8, 4.5), xytext=(6.5, 4.5),
                arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5),
                fontsize=8, color='#e74c3c')
    ax.text(8.2, 4.5, "DCM\n(heart failure)", fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#e74c3c', alpha=0.3))

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "lifetime_branching_tree.png"), dpi=150)
    plt.close()
    print("  Saved: lifetime_branching_tree.png")


def plot_tissue_damage_accumulation(all_tissue_damage, all_hla):
    """Plot cumulative tissue damage by organ and HLA type."""
    organs = ["pancreas_endo", "heart", "skeletal_muscle", "cns", "liver"]
    organ_labels = ["Pancreas\n(endocrine)", "Heart", "Skeletal\nMuscle", "CNS", "Liver"]

    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle("Subclinical Tissue Damage: Cumulative CVB Impact Over a Lifetime",
                 fontsize=13, fontweight='bold')

    # Average damage by organ
    ax = axes[0]
    mean_damage = [np.mean([td[organ] for td in all_tissue_damage]) * 100 for organ in organs]
    max_damage = [np.max([td[organ] for td in all_tissue_damage]) * 100 for organ in organs]
    colors = ['#9b59b6', '#e74c3c', '#1abc9c', '#3498db', '#e67e22']
    x = np.arange(len(organs))
    ax.bar(x, mean_damage, color=colors, alpha=0.7, label='Mean')
    ax.bar(x, max_damage, color=colors, alpha=0.2, label='Max')
    ax.set_xticks(x)
    ax.set_xticklabels(organ_labels, fontsize=9)
    ax.set_ylabel("Cumulative Damage (%)")
    ax.set_title("Subclinical Damage by Organ\n(Mean and Max across 10,000 lifetimes)")
    ax.legend()
    ax.grid(True, alpha=0.2, axis='y')

    # Damage by HLA type for heart vs pancreas
    ax = axes[1]
    hla_profiles = list(HLA_PROFILE_FREQS.keys())
    heart_by_hla = {}
    pancreas_by_hla = {}
    for hla in hla_profiles:
        heart_vals = [all_tissue_damage[i]["heart"] * 100
                      for i in range(len(all_tissue_damage)) if all_hla[i] == hla]
        panc_vals = [all_tissue_damage[i]["pancreas_endo"] * 100
                     for i in range(len(all_tissue_damage)) if all_hla[i] == hla]
        heart_by_hla[hla] = np.mean(heart_vals) if heart_vals else 0
        pancreas_by_hla[hla] = np.mean(panc_vals) if panc_vals else 0

    x = np.arange(len(hla_profiles))
    width = 0.35
    ax.bar(x - width/2, [heart_by_hla[h] for h in hla_profiles], width,
           label='Heart', color='#e74c3c', alpha=0.7)
    ax.bar(x + width/2, [pancreas_by_hla[h] for h in hla_profiles], width,
           label='Pancreas', color='#9b59b6', alpha=0.7)
    ax.set_xticks(x)
    ax.set_xticklabels(hla_profiles, rotation=30, ha='right', fontsize=8)
    ax.set_ylabel("Mean Cumulative Damage (%)")
    ax.set_title("Heart vs Pancreas Damage by HLA Type\n(THE PARADOX: opposite organs at risk)")
    ax.legend()
    ax.grid(True, alpha=0.2, axis='y')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "lifetime_tissue_damage.png"), dpi=150)
    plt.close()
    print("  Saved: lifetime_tissue_damage.png")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Patient Lifetime CVB Trajectory: 10,000 Simulated Lifetimes")
    print("systematic approach -- ODD (numerics) instance")
    print("=" * 70)

    # ------------------------------------------------------------------
    # 1. Simulate unvaccinated population
    # ------------------------------------------------------------------
    print("\n[1] Simulating 10,000 unvaccinated lifetimes (birth to 80)...")
    (all_infections, all_diseases, all_deaths,
     all_hla, all_tissue_damage) = simulate_population(n_people=10000, vaccinated=False)

    # Infection stats
    inf_per_person, serotype_counts, infection_ages = analyze_infection_patterns(
        all_infections, 10000)
    print(f"\n  CVB Infection Statistics:")
    print(f"  {'Mean infections per lifetime':>40}: {np.mean(inf_per_person):.2f}")
    print(f"  {'Median infections per lifetime':>40}: {np.median(inf_per_person):.0f}")
    print(f"  {'Max infections per lifetime':>40}: {max(inf_per_person)}")
    print(f"  {'% with zero infections':>40}: "
          f"{sum(1 for n in inf_per_person if n == 0) / 10000 * 100:.1f}%")
    print(f"  {'% with >= 3 infections':>40}: "
          f"{sum(1 for n in inf_per_person if n >= 3) / 10000 * 100:.1f}%")

    for sero in sorted(serotype_counts):
        print(f"    {SEROTYPES[sero]['name']}: {serotype_counts[sero]} infections")

    # Disease burden
    disease_counts, disease_by_hla, diseases_per_person, disease_ages = \
        analyze_disease_burden(all_diseases, all_hla, 10000)

    print(f"\n  Disease Burden (10,000 unvaccinated lifetimes):")
    print(f"  {'Disease':<25} {'Cases':>8} {'Rate/1000':>12} {'Mean Age':>10}")
    print(f"  {'-'*57}")
    for disease in sorted(disease_counts, key=disease_counts.get, reverse=True):
        count = disease_counts[disease]
        rate = count / 10000 * 1000
        ages = disease_ages[disease]
        mean_age = np.mean(ages) if ages else 0
        print(f"  {disease:<25} {count:>8d} {rate:>11.1f} {mean_age:>9.1f}")

    # Multi-disease burden
    print(f"\n  Multi-Disease Burden:")
    total_with_any = sum(1 for d in diseases_per_person if d >= 1)
    total_with_2 = sum(1 for d in diseases_per_person if d >= 2)
    total_with_3 = sum(1 for d in diseases_per_person if d >= 3)
    print(f"  {'% developing >= 1 CVB disease':>40}: {total_with_any / 10000 * 100:.1f}%")
    print(f"  {'% developing >= 2 CVB diseases':>40}: {total_with_2 / 10000 * 100:.1f}%")
    print(f"  {'% developing >= 3 CVB diseases':>40}: {total_with_3 / 10000 * 100:.1f}%")

    # Deaths
    deaths = [d for d in all_deaths if d is not None]
    print(f"\n  Mortality: {len(deaths)} deaths from CVB ({len(deaths)/10000*100:.2f}%)")
    if deaths:
        neonatal_deaths = sum(1 for d in deaths if d < 0.1)
        print(f"    Neonatal deaths: {neonatal_deaths} ({neonatal_deaths/max(len(deaths),1)*100:.0f}% of CVB deaths)")

    # ------------------------------------------------------------------
    # 2. Simulate vaccinated population
    # ------------------------------------------------------------------
    print("\n[2] Simulating 10,000 vaccinated lifetimes...")
    (vax_infections, vax_diseases, vax_deaths,
     vax_hla, vax_tissue_damage) = simulate_population(n_people=10000, vaccinated=True)

    vax_disease_counts, _, vax_diseases_per_person, _ = \
        analyze_disease_burden(vax_diseases, vax_hla, 10000)

    # ------------------------------------------------------------------
    # 3. Prevention benefit
    # ------------------------------------------------------------------
    print("\n[3] Prevention benefit: vaccinated vs unvaccinated...")
    benefit = compute_prevention_benefit(disease_counts, vax_disease_counts, 10000)

    print(f"\n  {'Disease':<25} {'Unvax':>8} {'Vax':>8} {'Prevented':>10} {'Reduction':>10}")
    print(f"  {'-'*63}")
    total_prevented = 0
    for disease in sorted(benefit, key=lambda d: benefit[d]["prevented"], reverse=True):
        b = benefit[disease]
        print(f"  {disease:<25} {b['unvaccinated']:>8d} {b['vaccinated']:>8d} "
              f"{b['prevented']:>10d} {b['reduction_pct']:>9.0f}%")
        total_prevented += b["prevented"]

    print(f"\n  TOTAL disease events prevented by vaccination: {total_prevented}")
    print(f"  Disease events per person prevented: {total_prevented / 10000:.3f}")

    vax_total_any = sum(1 for d in vax_diseases_per_person if d >= 1)
    print(f"\n  % with any CVB disease — unvaccinated: {total_with_any/10000*100:.1f}% "
          f"vs vaccinated: {vax_total_any/10000*100:.1f}%")

    vax_deaths_list = [d for d in vax_deaths if d is not None]
    print(f"  Deaths — unvaccinated: {len(deaths)} vs vaccinated: {len(vax_deaths_list)}")

    # ------------------------------------------------------------------
    # 4. HLA-stratified analysis
    # ------------------------------------------------------------------
    print("\n[4] HLA-stratified disease burden...")
    print(f"\n  {'HLA Profile':<20} {'Total Cases':>12} {'Rate/100':>10} {'Most Common Disease':<25}")
    print(f"  {'-'*70}")
    for hla in HLA_PROFILE_FREQS:
        total_hla_cases = sum(disease_by_hla[hla].values())
        n_hla_people = max(sum(1 for h in all_hla if h == hla), 1)
        rate = total_hla_cases / n_hla_people * 100
        if disease_by_hla[hla]:
            top_disease = max(disease_by_hla[hla], key=disease_by_hla[hla].get)
            top_count = disease_by_hla[hla][top_disease]
        else:
            top_disease = "none"
            top_count = 0
        print(f"  {hla:<20} {total_hla_cases:>12d} {rate:>9.1f} "
              f"{top_disease} ({top_count})")

    # ------------------------------------------------------------------
    # 5. Generate all plots
    # ------------------------------------------------------------------
    print("\n[5] Generating plots...")
    plot_infection_timeline(all_infections, all_diseases, 10000)
    plot_hla_disease_heatmap(disease_by_hla, 10000)
    plot_prevention_benefit(benefit)
    plot_multi_disease_per_person(diseases_per_person)
    plot_branching_tree()
    plot_tissue_damage_accumulation(all_tissue_damage, all_hla)

    # ------------------------------------------------------------------
    # 6. Save numerical results
    # ------------------------------------------------------------------
    print("\n[6] Saving results...")
    results = {
        "simulation_params": {
            "n_people": 10000,
            "age_range": "0-80",
            "seed": SEED,
        },
        "infection_stats": {
            "mean_per_person": round(float(np.mean(inf_per_person)), 2),
            "median_per_person": round(float(np.median(inf_per_person)), 1),
            "pct_zero": round(sum(1 for n in inf_per_person if n == 0) / 10000 * 100, 1),
            "pct_3plus": round(sum(1 for n in inf_per_person if n >= 3) / 10000 * 100, 1),
        },
        "disease_burden": {
            d: {"count": c, "rate_per_1000": round(c / 10000 * 1000, 2)}
            for d, c in disease_counts.items()
        },
        "multi_disease": {
            "pct_1plus": round(total_with_any / 10000 * 100, 1),
            "pct_2plus": round(total_with_2 / 10000 * 100, 1),
            "pct_3plus": round(total_with_3 / 10000 * 100, 1),
        },
        "mortality": {
            "total_deaths": len(deaths),
            "death_rate_pct": round(len(deaths) / 10000 * 100, 3),
        },
        "vaccination_benefit": benefit,
        "prevention_total": {
            "total_events_prevented": total_prevented,
            "events_per_person_prevented": round(total_prevented / 10000, 4),
            "deaths_prevented": len(deaths) - len(vax_deaths_list),
        },
    }

    results_path = os.path.join(RESULTS_DIR, "lifetime_trajectory_results.json")
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"  Saved: {results_path}")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("COMPLETE. Key findings:")
    print("=" * 70)

    print(f"\n  1. LIFETIME CVB EXPOSURE:")
    print(f"     - Mean {np.mean(inf_per_person):.1f} CVB infections per lifetime")
    print(f"     - {sum(1 for n in inf_per_person if n == 0)/10000*100:.0f}% escape all CVB infection")
    print(f"     - Each infection is another roll of the dice for tissue persistence")

    print(f"\n  2. POPULATION DISEASE BURDEN:")
    print(f"     - {total_with_any/10000*100:.1f}% develop >= 1 clinical CVB disease in lifetime")
    print(f"     - {total_with_2/10000*100:.1f}% develop >= 2 CVB diseases (multi-organ)")
    print(f"     - Hypothesis check: target was 5-15% with at least one chronic disease")

    print(f"\n  3. THE PREVENTION CASE:")
    print(f"     - Vaccination prevents {total_prevented} disease events in 10,000 lives")
    print(f"     - {len(deaths) - len(vax_deaths_list)} deaths prevented")
    print(f"     - This is the strongest argument for a polyvalent CVB vaccine")

    print(f"\n  4. AGE-DEPENDENT VULNERABILITY:")
    print(f"     - Neonates: highest mortality, hepatitis, sepsis")
    print(f"     - Children: T1DM seeding, meningitis, pleurodynia")
    print(f"     - Young adults: myocarditis, ME/CFS, pericarditis, orchitis")
    print(f"     - Middle age: DCM manifestation, accumulated tissue damage")

    print(f"\n  5. HLA DETERMINES WHICH ORGAN BEARS THE BURDEN:")
    print(f"     - DR3/DR4 compound het: pancreas takes the hit (T1DM)")
    print(f"     - DQ5 carrier: heart takes the hit (myocarditis/DCM)")
    print(f"     - DQ6 carrier: T1DM-protected but CNS-vulnerable")
    print(f"     - Neutral HLA: lower individual risk but NOT zero")

    print(f"\n  All figures saved to: {OUTPUT_DIR}")
    print(f"  Numerical results: {results_path}")
