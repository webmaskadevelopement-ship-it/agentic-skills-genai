---
file_id: "[532]"
table_title: "Dialogue Pause Duration Classification Thresholds"
governing_standard: "Phonetic Acoustic Pacing Standards & ASR Segmentation"
archetype: "F"
---

# [532] Micro-pause (150ms), Breath (400ms), Dramatic (900ms), Dead (>2000ms)

## 1. Governing Standard & Engineering Scope
- **Governing Standard**: `Phonetic Acoustic Pacing Standards & ASR Segmentation`
- **Technical Scope**: This reference table establishes the authoritative, mathematically verified physical parameters for `Dialogue Pause Duration Classification Thresholds`.
- **Enforcement Principle**: Autonomous agents and FilmCraft MCP commands are strictly bound to the numerical values below; improvising or interpolating outside specified thresholds is prohibited.

## 2. Complete Parameter Lookup Matrix
| Pause Class | Duration Range (ms) | Duration Frames (24fps) | Editorial Action | Acoustic Treatment |
|---|---|---|---|---|
| Micro-Pause | 80 ms – 200 ms | 2 – 5 frames | Preserve (natural rhythm) | Untouched |
| Breath Pause | 200 ms – 500 ms | 5 – 12 frames | Evaluate breath volume | De-breath / Attenuate -6dB |
| Sentence Cadence | 500 ms – 900 ms | 12 – 22 frames | Normal turn-taking gap | Room tone bridge crossfade |
| Dramatic Silence | 900 ms – 2000 ms | 22 – 48 frames | Intentional pause | Clean room tone fill; hold tension |
| Dead Air / Flaw | > 2000 ms | > 48 frames | Truncate to 600–800 ms | Insert room-tone print; ripple cut |

## 3. Deterministic Mathematical Formulation
$Frames = \text{round}\left(\frac{Duration_{ms}}{1000} \times fps\right)$. Minimum room-tone crossfade length = $\max(2 \text{ frames}, 80\text{ms})$.

## 4. NLE and DAW Implementation Notes
- **Implementation Guidance**: Never cut dialogue dead air without inserting a room-tone fill from the same microphone and scene print.
- **FilmCraft MCP Hook**: Bound to validator `[566]` and verified during timeline operations.
