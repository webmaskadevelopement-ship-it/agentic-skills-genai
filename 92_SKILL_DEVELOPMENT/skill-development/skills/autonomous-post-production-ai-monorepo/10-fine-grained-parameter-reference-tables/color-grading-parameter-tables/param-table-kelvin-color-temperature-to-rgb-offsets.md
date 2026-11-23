---
file_id: "[542]"
table_title: "Kelvin Color Temperature to RGB Gain and Offset Compensation Matrix"
governing_standard: "Planckian Locus Blackbody Radiation Tables"
archetype: "F"
---

# [542] 1800K Candlelight to 10000K Blue Sky RGB gain/offset compensation values

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Planckian Locus Blackbody Radiation Tables`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Kelvin Color Temperature to RGB Gain and Offset Compensation Matrix`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Correlated Color Temp (K) | Source Description | Red Gain Multiplier | Green Gain Multiplier | Blue Gain Multiplier | Neutralizing RGB Offset |
|---|---|---|---|---|---|
| 1800 K | Candlelight | 0.550 | 0.880 | 1.820 | R:-0.045, G:-0.012, B:+0.082 |
| 2700 K | Warm Incandescent | 0.720 | 0.940 | 1.380 | R:-0.028, G:-0.006, B:+0.038 |
| 3200 K | Studio Tungsten 3200K | 0.810 | 0.980 | 1.210 | R:-0.019, G:-0.002, B:+0.021 |
| 4300 K | Warm Fluorescent | 0.920 | 1.050 | 1.080 | R:-0.008, G:+0.005, B:+0.008 |
| 5600 K | Daylight / HMI Baseline | 1.000 | 1.000 | 1.000 | R:0.000, G:0.000, B:0.000 |
| 6500 K | Overcast Daylight / D65 | 1.060 | 0.990 | 0.940 | R:+0.006, G:-0.001, B:-0.006 |
| 7500 K | Open Shade Daylight | 1.140 | 0.980 | 0.880 | R:+0.014, G:-0.002, B:-0.012 |
| 10000 K | Blue Sky / Heavy Cloud | 1.280 | 0.960 | 0.760 | R:+0.028, G:-0.004, B:-0.024 |

## 3. Deterministic Mathematical Formulation
White balance adjustment: $R_{out} = R_{in} \cdot Gain_R + Offset_R$, preserving skin centroid at $123^\circ$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Always apply chromatic adaptation transforms (CAT02 or Bradford) in linear space before tone curve mapping.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
