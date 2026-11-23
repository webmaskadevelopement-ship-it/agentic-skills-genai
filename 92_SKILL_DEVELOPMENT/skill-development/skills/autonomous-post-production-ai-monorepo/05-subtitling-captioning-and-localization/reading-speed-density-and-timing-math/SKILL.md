---
file_id: "[336]"
skill_path: "05-subtitling-captioning-and-localization/reading-speed-density-and-timing-math/SKILL.md"
role: "Sub-Skill Router: Sub-Router: CPS, CPL, Duration & Shot-Change Mathematics"
parent_router: "[335]"
child_nodes:
  - "[337]"
  - "[338]"
  - "[339]"
  - "[340]"
  - "[341]"
  - "[342]"
  - "[343]"
  - "[344]"
  - "[345]"
  - "[346]"
  - "[347]"
  - "[348]"
schema_locks:
  - "[017]"
  - "[019]"
  - "[022]"
  - "[025]"
  - "[028]"
master_commands:
  - "EMIT_EDL_MANIFEST"
  - "EMIT_GRADE_SPEC"
  - "EMIT_COMPLIANCE_REPORT"
  - "EMIT_MIX_SPEC"
  - "EMIT_DELIVERY_SPEC"
validation_gates:
  - "[566]"
---

# [336] Sub-Router: CPS, CPL, Duration & Shot-Change Mathematics

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `05-subtitling-captioning-and-localization/reading-speed-density-and-timing-math`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(cps|characters|per|second|calculation|engine)` | `[337]` | `cps-characters-per-second-calculation-engine.md` | Exact formula: `total_visible_chars_including_spaces / duration_seconds` |
| `(?i)(adult|20|cps|vs|17|cps|reading|speed|governor)` | `[338]` | `adult-20-cps-vs-17-cps-reading-speed-governor.md` | Enforcing 20 CPS ceiling (Netflix EN) or 17 CPS (non-EN/broadcast) |
| `(?i)(children|programming|13|to|17|cps|governor)` | `[339]` | `children-programming-13-to-17-cps-governor.md` | Enforcing strict lower reading speed ceiling for youth demographics |
| `(?i)(wpm|words|per|minute|160|180|broadcast|converter)` | `[340]` | `wpm-words-per-minute-160-180-broadcast-converter.md` | Converting 5-char word equivalents to WPM broadcast standards |
| `(?i)(cpl|42|char|streaming|vs|37|char|bbc|line|limiter)` | `[341]` | `cpl-42-char-streaming-vs-37-char-bbc-line-limiter.md` | Counting glyph-plus-space width per line excluding markup tags |
| `(?i)(double|byte|cjk|16|to|23|cpl|character|metrics)` | `[342]` | `double-byte-cjk-16-to-23-cpl-character-metrics.md` | Enforcing Chinese/Japanese/Korean full-width character line limits |
| `(?i)(maximum|two|lines|per|cue|vertical|constraint)` | `[343]` | `maximum-two-lines-per-cue-vertical-constraint.md` | Prohibiting 3-line cues across all theatrical and streaming specs |
| `(?i)(minimum|cue|duration|833ms|and|1000ms|floor)` | `[344]` | `minimum-cue-duration-833ms-and-1000ms-floor.md` | Enforcing >= 20 frames (at 24fps) / 833ms minimum display duration |
| `(?i)(maximum|cue|duration|7000ms|split|threshold)` | `[345]` | `maximum-cue-duration-7000ms-split-threshold.md` | Splitting long sustained sentences exceeding 7.0 seconds on screen |
| `(?i)(inter|cue|minimum|2|frame|gap|enforcer)` | `[346]` | `inter-cue-minimum-2-frame-gap-enforcer.md` | Inserting mandatory 2-frame blink gap between consecutive cues |
| `(?i)(shot|change|snapping|dead|zone|2|to|11|frames)` | `[347]` | `shot-change-snapping-dead-zone-2-to-11-frames.md` | Snapping out-cues to cut or extending >= 12 frames across the cut |
| `(?i)(audio|lead|in|and|lag|out|frame|tolerance)` | `[348]` | `audio-lead-in-and-lag-out-frame-tolerance.md` | Syncing cue in-point within ±3 frames of vocal onset, +12f tail extension |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[336]`.
2. Identify the target leaf file among child nodes and load exactly 1 to 3 relevant child files.
3. Load the corresponding Parameter Reference Table from Cluster 10 (`[530]`–`[565]`).
4. Load the target Schema Lock file from Cluster 00 (`[014]`–`[030]`).
5. Explicitly declare loaded file IDs at the top of the operational response.

## 4. Stage-Gate Precondition Contract

Before executing tasks routed by this gateway:
- Upstream stage gates specified in `[004] stage-gate-progression-protocol.md` must record verified status.
- Any input artifact must pass its mapped schema validation gate before mutation.
- Timeline modifications must compute frame offsets in integer frames or 254,016,000,000 FilmCraft ticks.

## 5. Evidence-Gated Output Contract

All output emitted under this router must comply with `[005] evidence-gated-reasoning-contract.md`:
- Cites exact empirical scope values, loudness meters, phoneme timestamps, or frame numbers.
- Banned phrases ('warm look', 'smooth cut', 'natural mix') result in immediate rejection.

## 6. Escalation & Edge-Case Fallback Table

| Failure Mode | Detection Signature | Escalation Target | Resolution |
|---|---|---|---|
| Parameter Out of Bounds | Validator gate status == 'fail' | `[012]` Auto-Remediation | Recalculate parameters |
| Subjective Aesthetic Ambiguity | Conflicting creative options | `[006]` Taste-Gate | Present 2–3 structured options |
| Upstream Incomplete Data | Missing input telemetry | `[684]` Studio Defaults | Assign deterministic standard |

