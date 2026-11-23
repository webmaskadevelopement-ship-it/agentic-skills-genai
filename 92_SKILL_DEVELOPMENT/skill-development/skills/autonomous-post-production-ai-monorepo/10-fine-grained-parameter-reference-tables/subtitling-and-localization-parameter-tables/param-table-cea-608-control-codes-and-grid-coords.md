---
file_id: "[560]"
table_title: "CEA-608 Closed Caption Control Codes and Grid Coordinates"
governing_standard: "CTA-608-E Line 21 Data Standard"
archetype: "F"
---

# [560] 32x15 character grid row/column pac-codes and control byte hex pairs

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `CTA-608-E Line 21 Data Standard`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `CEA-608 Closed Caption Control Codes and Grid Coordinates`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Function / Command | Channel 1 Hex Pair | Channel 2 Hex Pair | Grid Interpretation | Action |
|---|---|---|---|---|
| Roll-Up 2 Lines (RU2) | `0x14 0x25` | `0x1C 0x25` | Rows 14–15 | Sets 2-line continuous scroll |
| Roll-Up 3 Lines (RU3) | `0x14 0x26` | `0x1C 0x26` | Rows 13–15 | Sets 3-line continuous scroll |
| Pop-On Captions (RCL) | `0x14 0x20` | `0x1C 0x20` | Off-screen Buffer | Resume caption loading |
| Erase Displayed Mem (EDM) | `0x14 0x2C` | `0x1C 0x2C` | Visible Screen | Clear current on-screen text |
| End of Caption (EOC) | `0x14 0x2F` | `0x1C 0x2F` | Display Swap | Swap off-screen buffer to screen |
| Preamble Address (Row 15, Indent 0) | `0x11 0x50` | `0x19 0x50` | Row 15 Col 0 | White text bottom baseline |
| Preamble Address (Row 1, Indent 0) | `0x11 0x40` | `0x19 0x40` | Row 1 Col 0 | White text top of screen |

## 3. Deterministic Mathematical Formulation
Grid dimensions: Exactly 32 columns wide by 15 rows tall. Parity: Odd parity bit on bit 7.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: CEA-608 transmission is bandwidth-limited to 2 bytes per field (60 bytes/second maximum throughput).
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
