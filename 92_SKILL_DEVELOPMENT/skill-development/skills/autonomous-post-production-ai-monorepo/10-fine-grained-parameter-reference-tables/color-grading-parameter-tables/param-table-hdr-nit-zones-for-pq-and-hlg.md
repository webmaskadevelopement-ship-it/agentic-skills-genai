---
file_id: "[547]"
table_title: "HDR Nit Zones for SMPTE ST 2084 (PQ) and HLG Delivery"
governing_standard: "SMPTE ST 2084 / ITU-R BT.2100-2"
archetype: "F"
---

# [547] Diffuse white (203 nits PQ), Skin (70–120 nits), Specular (400–1000 nits)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `SMPTE ST 2084 / ITU-R BT.2100-2`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `HDR Nit Zones for SMPTE ST 2084 (PQ) and HLG Delivery`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Picture Zone | PQ Target Nits ($cd/m^2$) | 10-Bit PQ Code Value | 12-Bit PQ Code Value | HLG Signal Ratio |
|---|---|---|---|---|
| Black Level Reference | 0.005 nits | 64 CV | 256 CV | 0.000 |
| Low Shadow Detail | 0.1 – 1.0 nits | 135 – 262 CV | 540 – 1048 CV | 0.050 – 0.150 |
| 18% Middle Grey | 25 – 35 nits | 440 – 465 CV | 1760 – 1860 CV | 0.380 – 0.420 |
| Caucasian Skin Tone | 70 – 120 nits | 512 – 555 CV | 2048 – 2220 CV | 0.550 – 0.650 |
| Reference Diffuse White | 203 nits | 592 CV | 2368 CV | 0.750 |
| Practical Interior Lights | 400 – 600 nits | 660 – 700 CV | 2640 – 2800 CV | 0.850 – 0.920 |
| Specular Highlights | 800 – 1000 nits | 730 – 769 CV | 2920 – 3076 CV | 0.980 – 1.000 |

## 3. Deterministic Mathematical Formulation
ST 2084 PQ electro-optical transfer function: $L = 10000 \times \left(\frac{\max(V^{1/m_2} - c_1, 0)}{c_2 - c_3 V^{1/m_2}}\right)^{1/m_1}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Never push standard diffuse graphics or UI white beyond 203 nits in HDR master files.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
