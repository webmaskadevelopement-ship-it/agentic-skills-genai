---
file_id: "[539]"
table_title: "Camera Log Middle Grey and White Reference IRE Values"
governing_standard: "Manufacturer Whitepapers (ARRI, Sony, Canon, RED)"
archetype: "F"
---

# [539] 18% grey IRE in LogC3 (39%), LogC4 (28%), S-Log3 (41%), Log3G10 (33%)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Manufacturer Whitepapers (ARRI, Sony, Canon, RED)`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Camera Log Middle Grey and White Reference IRE Values`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Camera Format / Color Space | Middle Grey (18%) IRE | 90% Reflectance White IRE | Sensor Dynamic Range | Native Base ISO |
|---|---|---|---|---|
| ARRI LogC3 (Alexa Mini / SXT) | 39.0 IRE | 68.0 IRE | 14.5 Stops | 800 ISO |
| ARRI LogC4 (Alexa 35) | 28.0 IRE | 62.0 IRE | 17.0 Stops | 800 ISO |
| Sony S-Log3 / S-Gamut3.Cine | 41.0 IRE | 61.0 IRE | 15.0 Stops | 800 / 3200 Dual Base |
| RED Log3G10 / REDWideGamut | 33.3 IRE | 60.0 IRE | 16.5 Stops | 800 ISO |
| Canon Log 2 / Cinema Gamut | 32.0 IRE | 63.0 IRE | 16.0 Stops | 800 ISO |
| Blackmagic Gen 5 Film | 38.4 IRE | 61.5 IRE | 14.0 Stops | 400 / 3200 Dual Base |
| Panasonic V-Log / V-Gamut | 42.0 IRE | 61.0 IRE | 14.0 Stops | 640 / 4000 Dual Base |
| Rec.709 Linear / SDR Display | 41.0 – 43.0 IRE | 100.0 IRE | 6.0 Stops | N/A |

## 3. Deterministic Mathematical Formulation
Luminance in 10-bit code values: $CV_{10} = \text{round}(64 + (IRE / 100) \times 876)$. LogC4 middle grey $28\% \approx 309$ CV.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Do not expose LogC4 at LogC3 target levels; doing so results in +1.2 stops overexposure.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
