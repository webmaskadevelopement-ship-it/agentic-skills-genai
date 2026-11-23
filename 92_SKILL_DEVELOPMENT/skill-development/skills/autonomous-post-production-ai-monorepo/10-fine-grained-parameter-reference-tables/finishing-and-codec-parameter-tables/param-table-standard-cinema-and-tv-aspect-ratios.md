---
file_id: "[563]"
table_title: "Standard Cinema and Television Aspect Ratios and Active Rasters"
governing_standard: "SMPTE ST 2048 / DCI System Specification"
archetype: "F"
---

# [563] Exact active pixel dimensions for 1.33, 1.66, 1.78, 1.85, 2.00, 2.20, 2.39

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `SMPTE ST 2048 / DCI System Specification`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Standard Cinema and Television Aspect Ratios and Active Rasters`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Aspect Ratio | Ratio Notation | Container Dimensions | Active Picture Dimensions | Letterbox / Pillarbox | Common Name |
|---|---|---|---|---|---|
| 1.33:1 | 4:3 | 1920 x 1080 | 1440 x 1080 | Pillarbox (240px L/R) | Standard Academy TV |
| 1.78:1 | 16:9 | 1920 x 1080 | 1920 x 1080 | Full Frame (0px) | HDTV Broadcast |
| 1.78:1 | 16:9 | 3840 x 2160 | 3840 x 2160 | Full Frame (0px) | 4K UHD Broadcast |
| 1.85:1 | Flat | 2048 x 1080 (2K DCI) | 1998 x 1080 | Pillarbox (25px L/R) | DCI 2K Flat |
| 1.85:1 | Flat | 4096 x 2160 (4K DCI) | 3996 x 2160 | Pillarbox (50px L/R) | DCI 4K Flat |
| 2.39:1 | Scope | 2048 x 1080 (2K DCI) | 2048 x 858 | Letterbox (111px T/B) | DCI 2K Scope |
| 2.39:1 | Scope | 4096 x 2160 (4K DCI) | 4096 x 1716 | Letterbox (222px T/B) | DCI 4K Scope |
| 2.00:1 | Univisium | 3840 x 2160 (4K UHD) | 3840 x 1920 | Letterbox (120px T/B) | Modern Streaming Drama |
| 0.56:1 | 9:16 Vertical | 1080 x 1920 | 1080 x 1920 | Full Frame (Vertical) | Social / Mobile Reels |

## 3. Deterministic Mathematical Formulation
$Height_{active} = \text{round}\left(\frac{Width_{container}}{Ratio}\right)$. Letterbox bars $= \frac{Height_{container} - Height_{active}}{2}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Ensure matte bars are encoded as clean digital zero black (CV 16 in legal, CV 0 in full data).
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
