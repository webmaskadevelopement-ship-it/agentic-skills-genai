---
file_id: "[544]"
table_title: "HSL Qualifier Six-Vector Hue Centers and Widths"
governing_standard: "Vectorscope Color Grading Six-Vector Segments"
archetype: "F"
---

# [544] Red, Yellow, Green, Cyan, Blue, Magenta exact degree centers and widths

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Vectorscope Color Grading Six-Vector Segments`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `HSL Qualifier Six-Vector Hue Centers and Widths`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Color Vector | Center Hue Angle (°) | Angular Width (°) | Softness Roll-Off (°) | Typical Secondary Use Case |
|---|---|---|---|---|
| Red Vector | 0° (360°) | 30° (345° – 15°) | 15° | Lips, brake lights, warm saturation control |
| Yellow Vector | 60° | 35° (42° – 77°) | 12° | Foliage highlight, golden hour sun warmth |
| Green Vector | 120° | 40° (100° – 140°) | 20° | Lawn, trees, toxic/neon green isolation |
| Cyan Vector | 180° | 30° (165° – 195°) | 15° | Water, sky tint, sci-fi cool tones |
| Blue Vector | 240° | 45° (217° – 262°) | 20° | Deep sky, navy denim, night exteriors |
| Magenta Vector | 300° | 30° (285° – 315°) | 15° | Neon signage, chromatic aberration cleanup |

## 3. Deterministic Mathematical Formulation
Matte qualifier equation: $M_H(\theta) = \text{clamp}\left(\frac{Width/2 + Softness - |\theta - \theta_0|}{Softness}, 0, 1\right)$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Skin tones sit at $123^\circ$ between Yellow ($60^\circ$) and Red ($0^\circ$); isolate skin with center $123^\circ$ and width $24^\circ$.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
