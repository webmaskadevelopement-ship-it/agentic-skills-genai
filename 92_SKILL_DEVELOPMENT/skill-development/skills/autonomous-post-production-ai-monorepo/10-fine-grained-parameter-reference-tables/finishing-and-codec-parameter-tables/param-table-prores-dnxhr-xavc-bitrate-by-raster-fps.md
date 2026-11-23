---
file_id: "[562]"
table_title: "Mezzanine Video Codec Bitrates and Storage Footprints"
governing_standard: "Apple ProRes Whitepaper / Avid DNxHR Specifications"
archetype: "F"
---

# [562] Exact Mbps and GB-per-hour storage footprints for all mezzanine codecs

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Apple ProRes Whitepaper / Avid DNxHR Specifications`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Mezzanine Video Codec Bitrates and Storage Footprints`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Codec Profile | Raster (Width x Height) | Frame Rate | Data Rate (Mbps) | Gigabytes / Hour | Quality Target |
|---|---|---|---|---|---|
| Apple ProRes 422 Proxy | 1920 x 1080 | 23.976 fps | 45 Mbps | 20.25 GB/hr | Offline Editorial Draft |
| Apple ProRes 422 LT | 1920 x 1080 | 23.976 fps | 102 Mbps | 45.90 GB/hr | Lightweight Finishing |
| Apple ProRes 422 HQ | 1920 x 1080 | 23.976 fps | 220 Mbps | 99.00 GB/hr | Broadcast SDR Master |
| Apple ProRes 422 HQ | 3840 x 2160 (4K UHD) | 23.976 fps | 884 Mbps | 397.80 GB/hr | UHD Commercial Delivery |
| Apple ProRes 4444 | 3840 x 2160 (4K UHD) | 23.976 fps | 1,326 Mbps | 596.70 GB/hr | HDR Master / VFX Turnover |
| Apple ProRes 4444 XQ | 3840 x 2160 (4K UHD) | 23.976 fps | 1,988 Mbps | 894.60 GB/hr | Archival RAW Grade Master |
| Avid DNxHR HQX | 3840 x 2160 (4K UHD) | 23.976 fps | 734 Mbps | 330.30 GB/hr | 10-bit Avid Online Finishing |

## 3. Deterministic Mathematical Formulation
$Storage_{GB} = \frac{Bitrate_{Mbps} \times Duration_{sec}}{8000}$. 1 hr of 4K ProRes 4444 = 596.7 GB.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Always allocate 20% storage headroom for render cache and scratch files.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
