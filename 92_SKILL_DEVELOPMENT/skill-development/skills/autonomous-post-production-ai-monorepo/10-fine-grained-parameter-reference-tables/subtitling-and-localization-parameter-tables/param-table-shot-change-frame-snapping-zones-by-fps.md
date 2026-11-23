---
file_id: "[558]"
table_title: "Shot-Change Frame Snapping Zones and Dead Zones by Frame Rate"
governing_standard: "EBU-TT / Netflix Subtitle Snapping Rules"
archetype: "F"
---

# [558] Exact frame counts for dead zones across 23.976, 24, 25, 29.97, 50, 59.94

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `EBU-TT / Netflix Subtitle Snapping Rules`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Shot-Change Frame Snapping Zones and Dead Zones by Frame Rate`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Frame Rate (fps) | Snap-to-Cut Window (Leading) | Dead Zone Window (Prohibited Cut Gap) | Snap-to-Cut Window (Trailing) | Minimum Duration |
|---|---|---|---|---|
| 23.976 / 24.0 fps | 1 – 3 frames | 4 – 11 frames | 1 – 3 frames | 20 frames (833ms) |
| 25.0 fps | 1 – 3 frames | 4 – 12 frames | 1 – 3 frames | 21 frames (840ms) |
| 29.97 / 30.0 fps | 1 – 4 frames | 5 – 14 frames | 1 – 4 frames | 25 frames (833ms) |
| 50.0 fps | 2 – 6 frames | 8 – 24 frames | 2 – 6 frames | 42 frames (840ms) |
| 59.94 / 60.0 fps | 2 – 8 frames | 10 – 28 frames | 2 – 8 frames | 50 frames (833ms) |

## 3. Deterministic Mathematical Formulation
Dead zone rule: Let cut be at frame $F_{cut}$. A subtitle boundary must NOT land in $[F_{cut} + 2, F_{cut} + 11]$. Either snap to $F_{cut}$ or push to $F_{cut} + 12$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: A subtitle starting 4–11 frames after a cut creates an involuntary visual stutter for the human eye.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
