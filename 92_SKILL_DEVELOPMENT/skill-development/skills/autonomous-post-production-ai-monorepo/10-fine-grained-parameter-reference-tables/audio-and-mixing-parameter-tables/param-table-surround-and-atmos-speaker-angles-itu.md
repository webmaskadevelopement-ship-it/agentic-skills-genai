---
file_id: "[554]"
table_title: "Surround and Atmos Speaker Angles (ITU-R BS.2051)"
governing_standard: "ITU-R BS.2051-2 / Dolby Atmos Authoring Guidelines"
archetype: "F"
---

# [554] ITU-R BS.2051 speaker azimuth and elevation angles for 5.1, 7.1, 7.1.4

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `ITU-R BS.2051-2 / Dolby Atmos Authoring Guidelines`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Surround and Atmos Speaker Angles (ITU-R BS.2051)`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Speaker Channel | Abbreviation | Azimuth Angle (°) | Elevation Angle (°) | Distance Scalar |
|---|---|---|---|---|
| Center | C | 0° | 0° | 1.00 (Anchor) |
| Left | L | -30° (-22° to -30°) | 0° | 1.00 |
| Right | R | +30° (+22° to +30°) | 0° | 1.00 |
| Left Surround | Ls | -110° (-90° to -110°) | 0° | 1.00 |
| Right Surround | Rs | +110° (+90° to +110°) | 0° | 1.00 |
| Left Back Surround | Lb | -140° (-135° to -150°) | 0° | 1.00 |
| Right Back Surround | Rb | +140° (+135° to +150°) | 0° | 1.00 |
| Low Frequency Effects | LFE | Subwoofer Floor | Floor | Bandpass 20–120 Hz (+10dB in monitor) |
| Top Front Left (Atmos) | Ltf | -45° | +45° | 1.00 |
| Top Front Right (Atmos) | Rtf | +45° | +45° | 1.00 |
| Top Rear Left (Atmos) | Ltr | -135° | +45° | 1.00 |
| Top Rear Right (Atmos) | Rtr | +135° | +45° | 1.00 |

## 3. Deterministic Mathematical Formulation
Vector Base Amplitude Panning (VBAP): $\vec{p} = l_1 \vec{c_1} + l_2 \vec{c_2} + l_3 \vec{c_3}$. Gain normalization: $\sqrt{\sum l_i^2} = 1$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Center channel carries anchor speech; surround channels must be decorrelated to prevent comb filtering.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
