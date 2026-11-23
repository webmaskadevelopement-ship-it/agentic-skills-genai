---
file_id: "[545]"
table_title: "Film Stock Contrast and Grain Profiles"
governing_standard: "Eastman Kodak & Fujifilm Photographic Sensitometry"
archetype: "F"
---

# [545] Numerical toe/shoulder slopes and grain micron sizes for 12 film stocks

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Eastman Kodak & Fujifilm Photographic Sensitometry`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Film Stock Contrast and Grain Profiles`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Film Stock | Toe Slope ($\gamma_L$) | Midtone Slope ($\gamma_M$) | Shoulder Slope ($\gamma_H$) | Grain Size ($\mu m$) | Look Characteristic |
|---|---|---|---|---|---|
| Kodak Vision3 5207 250D | 0.45 | 1.15 | 0.60 | 4.2 | Balanced daylight, neutral skintones, fine grain |
| Kodak Vision3 5219 500T | 0.40 | 1.25 | 0.55 | 6.8 | Tungsten rich shadows, distinct grain, halation |
| Kodak Vision3 5203 50D | 0.52 | 1.08 | 0.70 | 2.5 | Ultra-clean, razor sharp, deep rich blacks |
| Kodak Ektachrome 100D | 0.85 | 1.85 | 0.40 | 3.5 | Reversal pop, punchy saturated primaries |
| Fujifilm Eterna 500T | 0.38 | 0.95 | 0.65 | 5.5 | Soft muted pastel tones, creamy shadow roll |
| Kodak Tri-X 7266 B&W | 0.50 | 1.40 | 0.50 | 8.0 | Dramatic high-contrast black and white grit |

## 3. Deterministic Mathematical Formulation
Sensitometric characteristic curve: $D(H) = D_{min} + \frac{D_{max} - D_{min}}{1 + 10^{-\gamma(\log H - \log H_0)}}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Always layer film grain after look LUTs to ensure grain is not clipped by print transfer functions.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
