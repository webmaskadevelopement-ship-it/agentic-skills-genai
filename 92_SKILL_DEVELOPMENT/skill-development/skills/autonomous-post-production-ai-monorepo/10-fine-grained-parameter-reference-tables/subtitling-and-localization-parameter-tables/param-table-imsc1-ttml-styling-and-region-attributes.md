---
file_id: "[561]"
table_title: "W3C IMSC1.1 and TTML2 Styling and Region Attributes"
governing_standard: "W3C TTML2 / IMSC 1.1 Recommendation"
archetype: "F"
---

# [561] Complete W3C TTML2/IMSC1.1 namespace and `tts:` styling attribute index

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `W3C TTML2 / IMSC 1.1 Recommendation`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `W3C IMSC1.1 and TTML2 Styling and Region Attributes`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| TTML Attribute | Valid Values | Standard Default | Purpose |
|---|---|---|---|
| `tts:fontFamily` | `"proportionalSansSerif"`, `"monospaceSansSerif"` | `"proportionalSansSerif"` | Typography family |
| `tts:fontSize` | `"80%"`, `"100%"`, `"4.5c"` | `"100%"` | Text scale relative to cell |
| `tts:color` | `"#FFFFFF"`, `"#FFFF00"` (Yellow) | `"#FFFFFF"` | Font primary fill |
| `tts:backgroundColor` | `"#000000C0"`, `"transparent"` | `"transparent"` | Background pill or bar |
| `tts:textOutline` | `"#000000 0.1c 0.1c"` | `"#000000 1px 1px"` | Legibility shadow stroke |
| `tts:textAlign` | `"center"`, `"left"`, `"right"` | `"center"` | Alignment within region |
| `tts:origin` | `"10% 80%"`, `"10% 10%"` | `"10% 80%"` | Screen region anchor coordinates |
| `tts:extent` | `"80% 15%"` | `"80% 20%"` | Region bounding box width/height |

## 3. Deterministic Mathematical Formulation
Cell coordinates: `c` represents 1/32 of video grid width and 1/15 of height.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Netflix and SMPTE ST 2052 require valid IMSC1 profiles with full XML namespace declarations.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
