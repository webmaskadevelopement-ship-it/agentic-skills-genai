---
file_id: "[369]"
skill_path: "05-subtitling-captioning-and-localization/timed-text-serialization-and-compliance-auditing/SKILL.md"
role: "Sub-Skill Router: Sub-Router: SRT, WebVTT, TTML/IMSC1, EBU-STL & SCC Generators"
parent_router: "[335]"
child_nodes:
  - "[370]"
  - "[371]"
  - "[372]"
  - "[373]"
  - "[374]"
  - "[375]"
  - "[376]"
  - "[377]"
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

# [369] Sub-Router: SRT, WebVTT, TTML/IMSC1, EBU-STL & SCC Generators

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `05-subtitling-captioning-and-localization/timed-text-serialization-and-compliance-auditing`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(subrip|srt|utf8|bom|plain|text|serializer)` | `[370]` | `subrip-srt-utf8-bom-plain-text-serializer.md` | Generating sequential `HH:MM:SS,mmm --> HH:MM:SS,mmm` UTF-8 `.srt` |
| `(?i)(webvtt|vtt|html5|cue|settings|and|css|serializer)` | `[371]` | `webvtt-vtt-html5-cue-settings-and-css-serializer.md` | Generating `WEBVTT` with `line:`, `position:`, `align:` properties |
| `(?i)(w3c|ttml1|and|imsc1|1|xml|netflix|profile|builder)` | `[372]` | `w3c-ttml1-and-imsc1-1-xml-netflix-profile-builder.md` | Generating frame-accurate `ttp:frameRate` XML with region layout styles |
| `(?i)(ebu|tt|d|and|ebu|stl|binary|broadcast|serializer)` | `[373]` | `ebu-tt-d-and-ebu-stl-binary-broadcast-serializer.md` | Generating European Broadcast Union teletext and XML timed text |
| `(?i)(cea|608|and|708|line|21|scc|mcc|caption|encoder)` | `[374]` | `cea-608-and-708-line-21-scc-mcc-caption-encoder.md` | Encoding Pop-On, Paint-On, and Roll-Up hex byte-pairs for N.A. broadcast |
| `(?i)(dcp|cinecanvas|interop|and|smpte|428|7|xml|builder)` | `[375]` | `dcp-cinecanvas-interop-and-smpte-428-7-xml-builder.md` | Generating theatrical digital cinema subtitle XML + PNG font packages |
| `(?i)(per|cue|cps|cpl|duration|compliance|auditor)` | `[376]` | `per-cue-cps-cpl-duration-compliance-auditor.md` | Evaluating every cue as `pass`, `warn`, or `fail` with exact violation code |
| `(?i)(subtitle|compliance|report|json|and|md|serializer)` | `[377]` | `subtitle-compliance-report-json-and-md-serializer.md` | Compiling complete File C Subtitle & Compliance Report artifact |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[369]`.
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

