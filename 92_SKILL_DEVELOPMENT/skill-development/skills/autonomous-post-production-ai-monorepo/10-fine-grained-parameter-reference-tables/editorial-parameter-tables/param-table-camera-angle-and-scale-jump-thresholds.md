---
file_id: "[536]"
table_title: "Camera Angle and Scale Jump Thresholds (180-Degree and 30-Degree Rules)"
governing_standard: "Classical Hollywood Grammar / SMPTE Cinematography Rules"
archetype: "F"
---

# [536] Focal length delta (mm) and angular displacement (°) matrices

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Classical Hollywood Grammar / SMPTE Cinematography Rules`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Camera Angle and Scale Jump Thresholds (180-Degree and 30-Degree Rules)`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Parameter | Minimum Delta | Recommended Delta | Violation Consequence | Remediation Action |
|---|---|---|---|---|
| Angular Displacement | >= 30° | 45° – 90° | Jump cut perception | Insert cutaway or scale shift |
| Focal Length Delta | >= 20mm | >= 35mm (e.g. 50mm -> 85mm) | Jarring lens stutter | Enforce 2x shot scale jump |
| Shot Scale Difference | >= 1 full scale | Wide -> Medium -> Close-up | Awkward framing collision | Re-order coverage |
| 180° Action Axis | 0° (same side) | Strictly maintain eyeline axis | Disorienting screen reversal | Flip shot or insert neutral head-on |
| Eyeline Screen Height | <= 5% delta | Match pupil horizontal band | Unsettling eyeline wobble | Reposition / reframe digitally |

## 3. Deterministic Mathematical Formulation
Angular Displacement: $\theta = \arccos(\vec{C_1} \cdot \vec{C_2})$. Violation flag triggered if $\theta < 30^\circ$ on identical subject framing.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: When 30° rule cannot be met, cut must jump at least two scale classes (e.g. Extreme Wide -> Medium Close-Up).
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
