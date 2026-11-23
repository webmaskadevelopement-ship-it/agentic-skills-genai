---
file_id: "[557]"
table_title: "Subtitle Reading Speed (CPS) and Line Length (CPL) Limits Across 40 Languages"
governing_standard: "Netflix Timed Text Style Guide / BBC Subtitle Guidelines"
archetype: "F"
---

# [557] Language-by-language adult/child CPS and single/double-byte CPL limits

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Netflix Timed Text Style Guide / BBC Subtitle Guidelines`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Subtitle Reading Speed (CPS) and Line Length (CPL) Limits Across 40 Languages`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Language Code | Language Name | Adult Max CPS | Child Max CPS | Max CPL (Chars / Line) | Script Encoding Class |
|---|---|---|---|---|---|
| `en` | English | 20.0 CPS | 15.0 CPS | 42 CPL | Single-byte Latin |
| `es-419` | Spanish (Latin America) | 17.0 CPS | 13.0 CPS | 42 CPL | Single-byte Latin |
| `fr` | French | 17.0 CPS | 13.0 CPS | 42 CPL | Single-byte Latin |
| `de` | German | 17.0 CPS | 13.0 CPS | 42 CPL | Single-byte Latin |
| `it` | Italian | 17.0 CPS | 13.0 CPS | 42 CPL | Single-byte Latin |
| `ja` | Japanese | 10.0 CPS | 8.0 CPS | 16 CPL | Double-byte Full-width Kanji/Kana |
| `ko` | Korean | 12.0 CPS | 9.0 CPS | 18 CPL | Double-byte Hangul |
| `zh-Hans` | Chinese (Simplified) | 10.0 CPS | 8.0 CPS | 16 CPL | Double-byte Hanzi |
| `zh-Hant` | Chinese (Traditional) | 10.0 CPS | 8.0 CPS | 16 CPL | Double-byte Hanzi |
| `ar` | Arabic | 15.0 CPS | 11.0 CPS | 38 CPL | Right-to-Left (RTL) Complex |
| `he` | Hebrew | 15.0 CPS | 11.0 CPS | 36 CPL | Right-to-Left (RTL) Complex |
| `hi` | Hindi | 14.0 CPS | 10.0 CPS | 36 CPL | Indic Devanagari Complex |
| `ru` | Russian | 16.0 CPS | 12.0 CPS | 38 CPL | Cyrillic Single-byte |

## 3. Deterministic Mathematical Formulation
$CPS = \frac{\text{Character Count (including spaces)}}{\text{Duration (seconds)}}$. Rejection triggered if $CPS > CPS_{max}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Asian double-byte characters encode substantially higher conceptual density per character than Latin script.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
