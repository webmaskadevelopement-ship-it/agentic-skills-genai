# [012] Error Taxonomy and Auto-Remediation Loop Specification

## 1. Purpose & Architectural Flow
When a downstream validation gate (`[566]`–`[592]`) fails, this specification governs the deterministic triage and automated remediation loop. Errors are classified into three severity tiers:
- **Tier 1: Deterministic Auto-Remediable** (Resolved programmatically without human intervention)
- **Tier 2: Algorithmic Fallback** (Clamped to conservative studio default `[684]`)
- **Tier 3: Human Taste-Gate Escalation** (Execution suspended via `[006]`)

## 2. Standardized Error Taxonomy
| Error Code | Category | Description | Auto-Remediation Action |
|---|---|---|---|
| `ERR_LOUDNESS_OVER_CEILING` | Audio | Integrated LUFS exceeds target by >0.5 LU | Apply broadband gain trim $\Delta G = Target - Measured$ |
| `ERR_TRUE_PEAK_EXCEEDED` | Audio | Inter-sample peak > -1.0 dBTP | Engage 8x oversampled brickwall limiter at -1.0 dBTP |
| `ERR_COLOR_GAMUT_VIOLATION` | Color | Gamut excursion beyond target color space | Apply soft-clip knee roll-off at 99.5% boundary |
| `ERR_SUBTITLE_CPS_EXCEEDED` | Subtitles | Characters per second > 20.0 | Compress text synthetically or extend duration into tail |
| `ERR_TIMECODE_DRIFT` | Editorial | Non-drop frame mismatch accumulated over time | Requantize to nearest SMPTE frame boundary |
| `ERR_FLASH_FRAME` | Editorial | Shot duration < minimum threshold (4 frames) | Ripple extend or merge with adjacent shot |

## 3. Closed-Loop Remediation Cycle
```
[Execution Step] ---> [Emit Deliverable] ---> [Cluster 11 Validator]
      ^                                                |
      |                                                v
      +--- [Apply Auto-Remedy] <--- FAIL (T1/T2) <--- [Pass?]
                                                       |
                                                      YES
                                                       v
                                               [Proceed to Next Gate]
```
Max iterations per loop: 3. If validation fails on 3rd retry, escalate to Tier 3 HITL (`[006]`).
