---
file_id: "[534]"
table_title: "Dissolve and Fade Duration Frames by Narrative Transition"
governing_standard: "SMPTE Post-Production Transition Standards"
archetype: "F"
---

# [534] Soft cut (4f), Standard dissolve (24f), Slow passage of time (72f)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `SMPTE Post-Production Transition Standards`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Dissolve and Fade Duration Frames by Narrative Transition`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Transition Type | Duration Frames (24fps) | Duration (ms) | Energy Curve | Narrative Meaning |
|---|---|---|---|---|
| Flash Dissolve / Soft Cut | 4 – 8 frames | 166ms – 333ms | Linear | Soften jump cut without visible dissolve |
| Short Cross Dissolve | 12 – 16 frames | 500ms – 666ms | Equal Power (3dB) | Fluid scene flow / subtle change |
| Standard Scene Dissolve | 24 – 36 frames | 1000ms – 1500ms | Cosine / S-Curve | Clear passage of time / location change |
| Extended Montage Blend | 48 – 72 frames | 2000ms – 3000ms | S-Curve | Memory, dream sequence, montage |
| Fade to Black | 24 – 48 frames | 1000ms – 2000ms | Exponential Dip | Act break, conclusion, loss of consciousness |
| Fade from Black | 16 – 32 frames | 666ms – 1333ms | Logarithmic Rise | Beginning of act / awakening |

## 3. Deterministic Mathematical Formulation
Equal power audio crossfade: $G_A(t) = \cos(t \cdot \frac{\pi}{2})$, $G_B(t) = \sin(t \cdot \frac{\pi}{2})$ where $t \in [0, 1]$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Video dissolves across high-contrast luminance edges must be computed in linear light to avoid dark banding.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
