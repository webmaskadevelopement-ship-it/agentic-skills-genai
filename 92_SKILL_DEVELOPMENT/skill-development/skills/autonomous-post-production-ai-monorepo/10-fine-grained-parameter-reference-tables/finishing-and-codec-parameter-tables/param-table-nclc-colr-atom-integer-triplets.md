---
file_id: "[564]"
table_title: "NCLC colr Atom Integer Triplets for QuickTime MP4 and MOV"
governing_standard: "ISO/IEC 14496-12 / ISO/IEC 23091-2"
archetype: "F"
---

# [564] Complete ISO/IEC 23091-2 ColourPrimaries, TransferCharacteristics, Matrix

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `ISO/IEC 14496-12 / ISO/IEC 23091-2`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `NCLC colr Atom Integer Triplets for QuickTime MP4 and MOV`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Profile Description | Primaries (Index 1) | Transfer Function (Index 2) | Matrix Coefficients (Index 3) | NCLC String | Common Use Case |
|---|---|---|---|---|---|
| Standard Rec.709 (HDTV) | 1 (BT.709) | 1 (BT.709) | 1 (BT.709) | `1-1-1` | Standard Broadcast SDR |
| QuickTime Rec.709 (macOS Gamma 1.96) | 1 (BT.709) | 2 (Unspecified / sRGB) | 1 (BT.709) | `1-2-1` | Apple QuickTime Tagging |
| Rec.709 with BT.1886 Display | 1 (BT.709) | 13 (IEC 61966-2-4) | 1 (BT.709) | `1-13-1` | Web Video Color Fidelity |
| P3-D65 SDR Display | 12 (P3-D65) | 1 (BT.709) | 1 (BT.709) | `12-1-1` | Apple Display P3 SDR |
| HDR10 PQ (Rec.2020) | 9 (BT.2020) | 16 (SMPTE ST 2084) | 9 (BT.2020-non-const) | `9-16-9` | Ultra HD HDR10 Master |
| HLG HDR (Rec.2020) | 9 (BT.2020) | 18 (ARIB STD-B67) | 9 (BT.2020-non-const) | `9-18-9` | Broadcast HLG Live Master |

## 3. Deterministic Mathematical Formulation
NCLC QuickTime atom layout: `colr` atom with type `nclc` followed by 3x unsigned 16-bit big-endian integers.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Tagging `1-1-1` vs `1-2-1` resolves the infamous 'QuickTime gamma shift' on macOS.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
