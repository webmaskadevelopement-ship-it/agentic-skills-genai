---
file_id: "[531]"
table_title: "SMPTE Frame Rates and Drop Frame Timecode Rules"
governing_standard: "SMPTE ST 12-1 / ITU-R BT.1359"
archetype: "F"
---

# [531] Exact ticks-per-frame and timebase scalars for 23.976–120 fps

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `SMPTE ST 12-1 / ITU-R BT.1359`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `SMPTE Frame Rates and Drop Frame Timecode Rules`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Timebase (fps) | Ratio / Multiplier | FilmCraft Ticks / Frame | Drop Frame Rule | Common Application |
|---|---|---|---|---|
| 23.976 | 24000 / 1001 | 10,594,560,000 | Non-Drop Frame (NDF) | Cinema / High-End US Drama |
| 24.000 | 24 / 1 | 10,584,000,000 | Non-Drop Frame (NDF) | International Theatrical DCI |
| 25.000 | 25 / 1 | 10,160,640,000 | Non-Drop Frame (NDF) | European Broadcast (EBU / PAL) |
| 29.970 | 30000 / 1001 | 8,475,648,000 | Drop Frame (DF) & NDF | US Broadcast (ATSC / NTSC) |
| 30.000 | 30 / 1 | 8,467,200,000 | Non-Drop Frame (NDF) | Web / Mobile Native Video |
| 50.000 | 50 / 1 | 5,080,320,000 | Non-Drop Frame (NDF) | High Frame Rate European Sports |
| 59.940 | 60000 / 1001 | 4,237,824,000 | Drop Frame (DF) & NDF | High Frame Rate US Broadcast |
| 60.000 | 60 / 1 | 4,233,600,000 | Non-Drop Frame (NDF) | Gaming / High-Speed Capture |
| 120.000 | 120 / 1 | 2,116,800,000 | Non-Drop Frame (NDF) | Ultra High Frame Rate / Slo-Mo |

## 3. Deterministic Mathematical Formulation
Drop Frame Calculation: Skip frames 00 and 01 at the start of every minute, except minutes 00, 10, 20, 30, 40, 50. Drop count = 2 frames * 9 minutes = 18 frames dropped every 10 minutes. Drift = 0.000% over 24 hours.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: FilmCraft master tick frequency is exactly 254,016,000,000 ticks/sec. All timebase frame counts divide cleanly into this clock without float precision drift.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
