---
file_id: "[550]"
table_title: "Compressor Attack, Release, and Ratio Presets by Stem"
governing_standard: "Dynamic Range Processing Master Reference"
archetype: "F"
---

# [550] Exact ms and ratio settings for DX Peak, DX Leveler, MX Glue, FX Smash

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Dynamic Range Processing Master Reference`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Compressor Attack, Release, and Ratio Presets by Stem`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Target Stem | Compressor Type | Attack Time (ms) | Release Time (ms) | Ratio | Knee | Makeup Gain Target |
|---|---|---|---|---|---|---|
| Dialogue Peak Tamer | VCA / Digital Peak | 1.0 – 5.0 ms | 40 – 80 ms | 4:1 | Soft (4dB) | Catch transients, -3dB max |
| Dialogue Leveler | Opto / LA-2A Style | 10 – 20 ms | 200 – 500 ms | 2.5:1 | Smooth | Smooth RMS, -4dB average |
| Dialogue Bus Glue | Variable-Mu | 30 ms | Auto / 100 ms | 2:1 | Soft | Cohesion, -1.5dB to -2dB |
| Music Ducking Trigger | Sidechain VCA | 15 – 30 ms | 250 – 400 ms | 3:1 | Medium | Attenuate MX -4dB to -6dB |
| SFX Transient Punch | FET / 1176 Style | 0.5 – 1.0 ms | 50 – 100 ms | 8:1 | Hard | Punch control on gunshots, hits |
| Mix Master Bus Limiter | True Peak Brickwall | 0.1 ms | Auto / 100 ms | $\infty:1$ | Hard | True Peak ceiling -1.0 dBTP |

## 3. Deterministic Mathematical Formulation
Gain reduction formula: $GR(x) = \begin{cases} 0 & x \le T \\ -\frac{x - T}{R} & x > T \end{cases}$ in dB.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Always enable lookahead (minimum 1.5ms) on master bus brickwall limiters to eliminate inter-sample overshoot.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
