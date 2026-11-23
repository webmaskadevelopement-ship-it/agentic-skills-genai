---
file_id: "[134]"
skill_path: "02-editorial-craft-selects-and-pacing/murch-rule-of-six-and-cutting-mechanics/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Walter Murch Prioritization & Cut Point Physics"
parent_router: "[101]"
child_nodes:
  - "[135]"
  - "[136]"
  - "[137]"
  - "[138]"
  - "[139]"
  - "[140]"
  - "[141]"
  - "[142]"
  - "[143]"
  - "[144]"
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

# [134] Sub-Router: Walter Murch Prioritization & Cut Point Physics

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `02-editorial-craft-selects-and-pacing/murch-rule-of-six-and-cutting-mechanics`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(murch|priority|1|emotion|51|percent|evaluator)` | `[135]` | `murch-priority-1-emotion-51-percent-evaluator.md` | Prioritizing emotional truth over spatial or continuity errors |
| `(?i)(murch|priority|2|story|advancement|23|percent)` | `[136]` | `murch-priority-2-story-advancement-23-percent.md` | Ensuring every cut delivers new narrative information |
| `(?i)(murch|priority|3|rhythm|10|percent|timing|grid)` | `[137]` | `murch-priority-3-rhythm-10-percent-timing-grid.md` | Aligning cut points to internal visual and cadence pulse |
| `(?i)(murch|priority|4|eye|trace|7|percent|screen|quadrant)` | `[138]` | `murch-priority-4-eye-trace-7-percent-screen-quadrant.md` | Matching viewer focal point coordinates (X,Y) across cut boundaries |
| `(?i)(murch|priority|5|2d|plane|of|screen|5|percent)` | `[139]` | `murch-priority-5-2d-plane-of-screen-5-percent.md` | Respecting stage line, screen direction, and vector continuity |
| `(?i)(murch|priority|6|3d|spatial|continuity|4|percent)` | `[140]` | `murch-priority-6-3d-spatial-continuity-4-percent.md` | Maintaining physical room geography only when Priorities 1–5 hold |
| `(?i)(cut|on|action|motion|peak|frame|calculator)` | `[141]` | `cut-on-action-motion-peak-frame-calculator.md` | Cutting 2–3 frames before or during velocity peak for seamless flow |
| `(?i)(cut|on|actor|blink|frame|synchronizer)` | `[142]` | `cut-on-actor-blink-frame-synchronizer.md` | Aligning outgoing or incoming cut point to actor eyelid closure |
| `(?i)(rule|of|180|degree|axis|violation|detector)` | `[143]` | `rule-of-180-degree-axis-violation-detector.md` | Detecting eyeline inversions and unintentional axis crosses |
| `(?i)(rule|of|30|degree|focal|and|angle|delta|checker)` | `[144]` | `rule-of-30-degree-focal-and-angle-delta-checker.md` | Preventing accidental jump cuts by verifying >= 30° angle/scale shift |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[134]`.
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

