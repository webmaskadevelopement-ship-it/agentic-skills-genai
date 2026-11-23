---
file_id: "[543]"
table_title: "Printer Lights to Linear Gain Conversion Factors"
governing_standard: "Laboratory Cinex Printer Light Standards (0–50 scale)"
archetype: "F"
---

# [543] Converting 1–50 Printer Light points to exact RGB multiplier ratios

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Laboratory Cinex Printer Light Standards (0–50 scale)`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Printer Lights to Linear Gain Conversion Factors`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Printer Light Delta | Exposure Delta (EV / Stops) | Linear Gain Multiplier ($2^{\Delta EV}$) | Code Value Delta (10-bit Log) |
|---|---|---|---|
| +1 Point | +0.025 Stops | 1.0175x | +2.2 CV |
| +2 Points | +0.050 Stops | 1.0353x | +4.4 CV |
| +4 Points | +0.100 Stops | 1.0718x | +8.8 CV |
| +8 Points | +0.200 Stops | 1.1487x | +17.5 CV |
| +12 Points | +0.300 Stops | 1.2311x | +26.3 CV |
| +24 Points | +0.600 Stops | 1.5157x | +52.6 CV |
| +40 Points (1 Stop) | +1.000 Stop | 2.0000x | +87.6 CV |
| -40 Points (-1 Stop) | -1.000 Stop | 0.5000x | -87.6 CV |

## 3. Deterministic Mathematical Formulation
$1 \text{ Printer Light Point} = 0.025 \text{ EV}$. Gain multiplier $M = 2^{(Points \times 0.025)}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Printer lights provide orthogonal, non-interfering exposure compensation across R, G, and B channels.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
