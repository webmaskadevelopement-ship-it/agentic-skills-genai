---
file_id: "[537]"
table_title: "CMX 3600 Transition Codes and Modifier Tokens"
governing_standard: "SMPTE 258M / CMX 3600 EDL Specification"
archetype: "F"
---

# [537] Complete CMX 3600 `C`, `D`, `W001`–`W999` & `K` key transition codes

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `SMPTE 258M / CMX 3600 EDL Specification`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `CMX 3600 Transition Codes and Modifier Tokens`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| CMX Code | Description | Parameter Argument | FilmCraft Command |
|---|---|---|---|
| `C` | Hard Cut | None | `timeline.razor` |
| `D` | Cross Dissolve | Duration in frames (`024`) | `timeline.add_transition(DISSOLVE)` |
| `W001`–`W999` | Wipe Pattern (SMPTE standard) | Wipe code + duration (`W001 030`) | `timeline.add_transition(WIPE)` |
| `K` | Key Overlay | In/Out/Level | `timeline.add_key_track` |
| `B` | Black Matte Generator | Duration in frames | `timeline.insert_color_matte(BLACK)` |
| `* FROM CLIP NAME:` | Extended Comment | File basename | Extracted to `source_clip` metadata |
| `* ASC_SOP` | CDL Grade Tokens | `(Slope)(Offset)(Power)` | Parsed into Node 01 primary CDL |
| `* ASC_SAT` | CDL Saturation Token | Saturation scalar (`1.050`) | Parsed into CDL saturation node |

## 3. Deterministic Mathematical Formulation
CMX Timecode line syntax: `[Event] [Reel] [Track] [Type] [Duration] [SrcIn] [SrcOut] [RecIn] [RecOut]`.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Always preserve ASC_SOP comments in EDL export for downstream color conform.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
