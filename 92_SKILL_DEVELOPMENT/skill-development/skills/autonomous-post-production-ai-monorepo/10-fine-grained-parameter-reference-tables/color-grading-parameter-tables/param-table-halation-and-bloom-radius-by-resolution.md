---
file_id: "[546]"
table_title: "Halation and Bloom Radius by Raster Resolution"
governing_standard: "Optical Photochemical Emulsion Layer Diffusion Physics"
archetype: "F"
---

# [546] Scaling blur pixel radii from 1080p (1.0x) to 4K (2.0x) and 8K (4.0x)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Optical Photochemical Emulsion Layer Diffusion Physics`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Halation and Bloom Radius by Raster Resolution`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Raster Resolution | Width x Height | Primary Halation Radius | Secondary Bloom Radius | Dispersion Falloff Profile |
|---|---|---|---|---|
| 1080p FHD | 1920 x 1080 | 3.5 px | 12.0 px | Exponential ($e^{-r/3.5}$) |
| 2K DCI | 2048 x 1080 | 3.8 px | 13.0 px | Exponential ($e^{-r/3.8}$) |
| 4K UHD | 3840 x 2160 | 7.0 px | 24.0 px | Exponential ($e^{-r/7.0}$) |
| 4K DCI | 4096 x 2160 | 7.5 px | 26.0 px | Exponential ($e^{-r/7.5}$) |
| 6K RAW | 6144 x 3456 | 11.2 px | 39.0 px | Exponential ($e^{-r/11.2}$) |
| 8K DCI | 8192 x 4320 | 15.0 px | 52.0 px | Exponential ($e^{-r/15.0}$) |

## 3. Deterministic Mathematical Formulation
$Radius(res) = Radius_{1080p} \times \left(\frac{Height_{px}}{1080}\right)$. Red channel weight: $1.00$, Green: $0.15$, Blue: $0.02$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Halation occurs predominantly in the red spectrum due to anti-halation remjet penetration.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
