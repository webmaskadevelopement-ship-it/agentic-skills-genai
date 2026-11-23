---
file_id: "[551]"
table_title: "Reverb RT60 Decay and Pre-Delay Reference by Acoustic Environment"
governing_standard: "ISO 3382-1 Architectural Acoustics"
archetype: "F"
---

# [551] RT60 (0.2s Closet to 4.5s Cathedral) and Pre-Delay (5ms to 65ms) matrices

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `ISO 3382-1 Architectural Acoustics`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Reverb RT60 Decay and Pre-Delay Reference by Acoustic Environment`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Acoustic Environment | RT60 Decay (Seconds) | Pre-Delay (ms) | Early Reflections Level | Damping Freq (Hz) |
|---|---|---|---|---|
| Small Vocal Booth / Closet | 0.15 – 0.25 s | 2 – 5 ms | -18 dBFS | 4.5 kHz |
| Domestic Living Room | 0.40 – 0.65 s | 8 – 15 ms | -12 dBFS | 3.5 kHz |
| Corporate Office / Studio | 0.50 – 0.80 s | 12 – 20 ms | -14 dBFS | 4.0 kHz |
| Concrete Garage / Warehouse | 1.80 – 2.50 s | 25 – 45 ms | -6 dBFS | 1.8 kHz |
| Cathedral / Large Stone Hall | 3.50 – 5.50 s | 45 – 75 ms | -3 dBFS | 1.2 kHz |
| Exterior City Alleyway | 0.80 – 1.40 s (discrete slaps) | 35 – 60 ms | -8 dBFS | 2.2 kHz |

## 3. Deterministic Mathematical Formulation
Sabine Formula: $RT_{60} = \frac{0.161 \cdot V}{\sum (S_i \cdot \alpha_i)}$ where $V$ is volume ($m^3$) and $\alpha$ is absorption.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: High frequencies roll off faster in natural air; dampen reverb above 4 kHz to prevent dialogue masking.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
