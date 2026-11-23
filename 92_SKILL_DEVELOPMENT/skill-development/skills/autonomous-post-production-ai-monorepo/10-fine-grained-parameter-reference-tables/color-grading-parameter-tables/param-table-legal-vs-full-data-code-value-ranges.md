---
file_id: "[548]"
table_title: "Legal vs Full Data Code Value Ranges"
governing_standard: "ITU-R BT.601 / BT.709 / SMPTE RP 136"
archetype: "F"
---

# [548] 8-bit (16–235), 10-bit (64–940), 12-bit (256–3760) legal vs full bounds

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `ITU-R BT.601 / BT.709 / SMPTE RP 136`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Legal vs Full Data Code Value Ranges`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Bit Depth | Range Type | Black Level CV | White Level CV | Excursion Ceiling CV | Headroom / Footroom |
|---|---|---|---|---|---|
| 8-Bit | Legal / Video Range | 16 | 235 | 254 | Foot: 1-15, Head: 236-254 |
| 8-Bit | Full / Data Range | 0 | 255 | 255 | None |
| 10-Bit | Legal / Video Range | 64 | 940 | 1019 | Foot: 1-63, Head: 941-1019 |
| 10-Bit | Full / Data Range | 0 | 1023 | 1023 | None |
| 12-Bit | Legal / Video Range | 256 | 3760 | 4076 | Foot: 1-255, Head: 3761-4076 |
| 12-Bit | Full / Data Range | 0 | 4095 | 4095 | None |

## 3. Deterministic Mathematical Formulation
$CV_{legal}(x) = \text{round}\left(64 \times 2^{b-10} + x \times (876 \times 2^{b-10})\right)$ where $x \in [0.0, 1.0]$ and $b$ is bit depth.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Broadcast MXF deliverables require strict legal scaling. Web ProRes and MP4 require full range.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
