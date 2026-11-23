---
file_id: "[540]"
table_title: "Color Space Primaries and White Point CIE xy Coordinates"
governing_standard: "SMPTE RP 431-2 / ITU-R BT.709 / BT.2020 / SMPTE ST 2065-1 (ACES)"
archetype: "F"
---

# [540] Red/Green/Blue/White CIE xy coordinates for Rec.709, P3, Rec.2020, AP0, AP1

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `SMPTE RP 431-2 / ITU-R BT.709 / BT.2020 / SMPTE ST 2065-1 (ACES)`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Color Space Primaries and White Point CIE xy Coordinates`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Color Space | Red (x, y) | Green (x, y) | Blue (x, y) | White Point (x, y) | Illuminant |
|---|---|---|---|---|---|
| Rec.709 / sRGB | (0.640, 0.330) | (0.300, 0.600) | (0.150, 0.060) | (0.3127, 0.3290) | D65 |
| DCI-P3 | (0.680, 0.320) | (0.265, 0.690) | (0.150, 0.060) | (0.3140, 0.3510) | DCI White |
| P3-D65 (Display P3) | (0.680, 0.320) | (0.265, 0.690) | (0.150, 0.060) | (0.3127, 0.3290) | D65 |
| Rec.2020 / UHDTV | (0.708, 0.292) | (0.170, 0.797) | (0.131, 0.046) | (0.3127, 0.3290) | D65 |
| ACES AP0 (ST 2065-1) | (0.7347, 0.2653) | (0.0000, 1.0000) | (0.0001, -0.0770) | (0.32168, 0.33767) | ACES D60 |
| ACES AP1 (ACEScc/cg) | (0.7130, 0.2930) | (0.1650, 0.8300) | (0.1280, 0.0440) | (0.32168, 0.33767) | ACES D60 |

## 3. Deterministic Mathematical Formulation
$M_{RGB \to XYZ} = \begin{bmatrix} X_r/y_r & X_g/y_g & X_b/y_b \\ 1 & 1 & 1 \\ Z_r/y_r & Z_g/y_g & Z_b/y_b \end{bmatrix} \cdot \text{diag}(\vec{S})$ where $\vec{S}$ is solved from white point.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: All intermediate color transforms in the monorepo occur inside ACES AP1 color primaries.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
