---
file_id: "[555]"
table_title: "Electrical Mains Hum Frequencies by Country and Harmonics"
governing_standard: "IEC 60038 Worldwide Electricity Standards"
archetype: "F"
---

# [555] 50 Hz vs 60 Hz regional grid and harmonic series up to 1000 Hz

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `IEC 60038 Worldwide Electricity Standards`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Electrical Mains Hum Frequencies by Country and Harmonics`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Country / Region | Fundamental Grid Hz | 2nd Harmonic | 3rd Harmonic | 4th Harmonic | 5th Harmonic | Corrective Filter |
|---|---|---|---|---|---|---|
| North America (USA, CAN) | 60.0 Hz | 120.0 Hz | 180.0 Hz | 240.0 Hz | 300.0 Hz | Comb filter notch Q=10 at 60Hz multiples |
| Europe & UK | 50.0 Hz | 100.0 Hz | 150.0 Hz | 200.0 Hz | 250.0 Hz | Comb filter notch Q=10 at 50Hz multiples |
| Japan (Eastern - Tokyo) | 50.0 Hz | 100.0 Hz | 150.0 Hz | 200.0 Hz | 250.0 Hz | 50 Hz Comb Notch |
| Japan (Western - Osaka) | 60.0 Hz | 120.0 Hz | 180.0 Hz | 240.0 Hz | 300.0 Hz | 60 Hz Comb Notch |
| Australia / NZ | 50.0 Hz | 100.0 Hz | 150.0 Hz | 200.0 Hz | 250.0 Hz | 50 Hz Comb Notch |
| India | 50.0 Hz | 100.0 Hz | 150.0 Hz | 200.0 Hz | 250.0 Hz | 50 Hz Comb Notch |

## 3. Deterministic Mathematical Formulation
Harmonic series notch: $f_n = n \times f_0$ where $n \in \{1, 2, 3, 4, 5\}$. Filter bandwidth $BW = f_n / Q$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: In North America, ground loop hum is primarily 60Hz and 120Hz; fluorescent lighting adds 180Hz.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
