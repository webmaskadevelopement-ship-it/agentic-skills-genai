---
file_id: "[306]"
skill_path: "04-sound-design-dialogue-foley-and-mixing/music-editing-and-score-integration/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Music Spotting, Stem Editing, Retiming & Ducking"
parent_router: "[267]"
child_nodes:
  - "[307]"
  - "[308]"
  - "[309]"
  - "[310]"
  - "[311]"
  - "[312]"
  - "[313]"
  - "[314]"
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

# [306] Sub-Router: Music Spotting, Stem Editing, Retiming & Ducking

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `04-sound-design-dialogue-foley-and-mixing/music-editing-and-score-integration`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(music|spotting|emotional|arc|and|entry|motivation)` | `[307]` | `music-spotting-emotional-arc-and-entry-motivation.md` | Entering music on emotional turn or reaction rather than scene cut |
| `(?i)(music|cue|out|point|button|vs|ring|out|decay)` | `[308]` | `music-cue-out-point-button-vs-ring-out-decay.md` | Ending cues on dramatic impact button vs seamless reverb tail fade |
| `(?i)(music|stem|deconstruction|drums|bass|melody|pads)` | `[309]` | `music-stem-deconstruction-drums-bass-melody-pads.md` | Muting vocal-range lead instruments during dense dialogue passages |
| `(?i)(musical|bar|and|beat|seamless|duration|retiming)` | `[310]` | `musical-bar-and-beat-seamless-duration-retiming.md` | Cutting on matching harmonic downbeats to shorten/lengthen a 3m cue to 45s |
| `(?i)(tempo|map|and|meter|change|hit|point|alignment)` | `[311]` | `tempo-map-and-meter-change-hit-point-alignment.md` | Aligning orchestral swells and downbeats to locked visual cut frames |
| `(?i)(dynamic|dialogue|sidechain|ducking|envelope|math)` | `[312]` | `dynamic-dialogue-sidechain-ducking-envelope-math.md` | Pre-ducking music -4 to -9 dB 300ms before speech onset, 800ms release |
| `(?i)(frequency|selective|spectral|ducking|1khz|4khz)` | `[313]` | `frequency-selective-spectral-ducking-1khz-4khz.md` | Carving only the 1 kHz–4 kHz presence pocket in music when DX speaks |
| `(?i)(music|cue|sheet|pro|rights|metadata|compiler)` | `[314]` | `music-cue-sheet-pro-rights-metadata-compiler.md` | Generating ASCAP/BMI/PRS cue sheet with composer, publisher, and usage TC |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[306]`.
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

