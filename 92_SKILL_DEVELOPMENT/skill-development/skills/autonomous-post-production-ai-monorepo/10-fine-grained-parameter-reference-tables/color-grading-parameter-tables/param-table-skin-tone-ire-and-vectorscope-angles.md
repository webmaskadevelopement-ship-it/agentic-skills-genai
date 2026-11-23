---
file_id: "[541]"
table_title: "Skin Tone IRE and Vectorscope Placement Across Fitzpatrick Scale"
governing_standard: "SMPTE RP 2093 / Fitzpatrick Dermatology Phototyping"
archetype: "F"
---

# [541] Fitzpatrick Scale I–VI IRE exposure ranges and vectorscope saturation bounds

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `SMPTE RP 2093 / Fitzpatrick Dermatology Phototyping`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Skin Tone IRE and Vectorscope Placement Across Fitzpatrick Scale`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Fitzpatrick Skin Type | Luminance Target (IRE in Rec.709) | 10-Bit Code Value | Vectorscope Angle (Skin Tone Line) | Saturation Range |
|---|---|---|---|---|
| Type I (Very Fair / Pale) | 65 – 72 IRE | 633 – 695 CV | 123° ± 2° | 25% – 32% |
| Type II (Fair / Light) | 60 – 68 IRE | 590 – 660 CV | 123° ± 2° | 28% – 35% |
| Type III (Medium / Olive) | 55 – 63 IRE | 546 – 616 CV | 123° ± 2° | 30% – 38% |
| Type IV (Moderate Brown) | 48 – 56 IRE | 484 – 554 CV | 123° ± 2° | 32% – 40% |
| Type V (Dark Brown) | 40 – 48 IRE | 414 – 484 CV | 123° ± 2° | 30% – 42% |
| Type VI (Deeply Pigmented) | 32 – 42 IRE | 344 – 432 CV | 123° ± 2° | 28% – 40% |

## 3. Deterministic Mathematical Formulation
Skin Line Vectorscope Axis: $Q = 0.587 R - 0.274 G - 0.313 B$. The angle of blood perfusion under melanin is mathematically invariant at $123^\circ$ regardless of skin type.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Melanin modifies luminance level (IRE) and total saturation, but NOT vectorscope hue angle.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
