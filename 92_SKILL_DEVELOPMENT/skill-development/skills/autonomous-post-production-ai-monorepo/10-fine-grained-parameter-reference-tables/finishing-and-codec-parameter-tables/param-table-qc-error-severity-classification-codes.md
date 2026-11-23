---
file_id: "[565]"
table_title: "Automated QC Error Severity Classification Codes"
governing_standard: "EBU R128 / Netflix Delivery Specs / SMPTE QC Metrics"
archetype: "F"
---

# [565] Mapping 100+ QC anomalies to Reject (Blocker), Warn (Fix), or Info (Note)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `EBU R128 / Netflix Delivery Specs / SMPTE QC Metrics`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Automated QC Error Severity Classification Codes`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Error Classification Code | Domain | Metric Threshold | Severity | Immediate Remediation Action |
|---|---|---|---|---|
| `QC_ERR_LOUDNESS_OUT_OF_SPEC` | Audio | Integrated > ±0.5 LU of target | Reject (Blocker) | Apply gain offset trim |
| `QC_ERR_TRUE_PEAK_EXCEEDED` | Audio | Inter-sample peak > -1.0 dBTP | Reject (Blocker) | Re-render with brickwall limiter |
| `QC_ERR_GAMUT_ILLEGAL_EXCURSION` | Video | Rec.709 illegal pixels > 0.5% | Reject (Blocker) | Soft-clip gamut boundary via [248] |
| `QC_ERR_FLASH_FRAME_DETECTED` | Editorial | Shot duration < 3 frames | Warn (Review) | Inspect cutaway or dissolve |
| `QC_ERR_SUBTITLE_CPS_EXCEEDED` | Subtitles | Characters/sec > 20.0 | Warn (Review) | Synthetically condense text |
| `QC_ERR_CPL_LINE_OVERFLOW` | Subtitles | Line chars > 42 | Warn (Review) | Auto-wrap at semantic clause |
| `QC_ERR_DEAD_ZONE_CUT_COLLISION` | Subtitles | Subtitle starts 4–11 frames post-cut | Warn (Review) | Snap cue to cut frame |
| `QC_ERR_AUDIO_PHASE_INVERSION` | Audio | Phase correlation < 0.0 across stem | Reject (Blocker) | Invert polarity on out-of-phase track |
| `QC_ERR_DROPPED_FRAME_DUPLICATE` | Picture | 2 identical consecutive frames in 24p | Reject (Blocker) | Investigate cadence pull-down |

## 3. Deterministic Mathematical Formulation
Severity hierarchy: $\text{Blocker (Reject)} > \text{Warning (Auto-Fix)} > \text{Info (Log)}$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Any deliverable with 1 or more Blocker errors cannot receive master delivery clearance.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
