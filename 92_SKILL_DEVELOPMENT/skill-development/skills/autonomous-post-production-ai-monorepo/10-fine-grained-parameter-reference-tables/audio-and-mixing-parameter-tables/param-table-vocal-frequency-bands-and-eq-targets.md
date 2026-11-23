---
file_id: "[549]"
table_title: "Vocal Frequency Bands and EQ Corrective Targets"
governing_standard: "Acoustic Voice Formant Standards"
archetype: "F"
---

# [549] Plosive (<100Hz), Mud (250Hz), Box (500Hz), Presence (3kHz), Sibilance (7kHz)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Acoustic Voice Formant Standards`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Vocal Frequency Bands and EQ Corrective Targets`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Frequency Band | Center Hz | Bandwidth (Q) | Acoustic Description | Action Threshold & Target |
|---|---|---|---|---|
| Sub-Bass / Rumble | < 80 Hz | High Pass 18dB/oct | Handling noise, air con rumble | Cut: High-pass filter at 80 Hz |
| Plosives (P-Pops) | 90 – 140 Hz | 2.5 Q | Breath bursts hitting diaphragm | Dynamic notch attenuation -6dB |
| Chest Resonance / Body | 180 – 250 Hz | 1.4 Q | Warm vocal weight | Trim -1.5dB if boomy, boost if thin |
| Boxiness / Hollow Room | 400 – 600 Hz | 2.0 Q | Untreated room box reflection | Cut -2.0dB to -4.0dB |
| Nasal Resonance | 800 – 1200 Hz | 3.0 Q | Nasal speaker formant build-up | Narrow notch -2.5dB |
| Speech Intelligibility | 2.5 kHz – 4 kHz | 1.2 Q | Consonant clarity and presence | Subtle wide bell boost +1.5dB |
| Sibilance (Esses) | 5.5 kHz – 8 kHz | De-Esser | Harsh piercing vocal friction | De-esser threshold -24dB, max -4dB reduction |
| Air / Openness | > 12 kHz | High Shelf | Modern breath sheen | High shelf boost +1.0dB (if signal is low noise) |

## 3. Deterministic Mathematical Formulation
Parametric filter transfer function: $H(s) = \frac{s^2 + (A/Q)s + 1}{s^2 + (1/(A \cdot Q))s + 1}$ where $A = 10^{\Delta G / 40}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Never apply static boosts to sibilant bands (5–8 kHz); use dynamic EQ or dedicated de-essers.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
