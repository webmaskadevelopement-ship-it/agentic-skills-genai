---
file_id: "[156]"
skill_path: "02-editorial-craft-selects-and-pacing/rhythm-pacing-and-emotional-tempo/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Pacing Curves, ASL & Musical Quantization"
parent_router: "[101]"
child_nodes:
  - "[157]"
  - "[158]"
  - "[159]"
  - "[160]"
  - "[161]"
  - "[162]"
  - "[163]"
  - "[164]"
  - "[165]"
  - "[166]"
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

# [156] Sub-Router: Pacing Curves, ASL & Musical Quantization

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `02-editorial-craft-selects-and-pacing/rhythm-pacing-and-emotional-tempo`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(average|shot|length|asl|curve|profiler)` | `[157]` | `average-shot-length-asl-curve-profiler.md` | Profiling rolling ASL across scenes to visualize tension arcs |
| `(?i)(action|sequence|exponential|acceleration|curve)` | `[158]` | `action-sequence-exponential-acceleration-curve.md` | Progressively shortening shot durations toward climax impact |
| `(?i)(dramatic|dialogue|tension|and|hold|frame|logic)` | `[159]` | `dramatic-dialogue-tension-and-hold-frame-logic.md` | Holding on silent listener face after heavy line delivery |
| `(?i)(comedic|timing|setup|pause|punchline|button|math)` | `[160]` | `comedic-timing-setup-pause-punchline-button-math.md` | Frame-exact trimming of comedic beats and late-cut buttons |
| `(?i)(horror|and|suspense|dread|elongation|pacing)` | `[161]` | `horror-and-suspense-dread-elongation-pacing.md` | Subverting expected cut rhythm with uncomfortable long holds |
| `(?i)(montage|compression|of|time|progression|builder)` | `[162]` | `montage-compression-of-time-progression-builder.md` | Structuring training/travel/process montages with clear milestones |
| `(?i)(music|bpm|beat|grid|and|transient|quantizer)` | `[163]` | `music-bpm-beat-grid-and-transient-quantizer.md` | Snapping cuts to 1/4, 1/2, or bar downbeats without feeling robotic |
| `(?i)(syncopated|off|beat|cutting|for|organic|groove)` | `[164]` | `syncopated-off-beat-cutting-for-organic-groove.md` | Cutting 2 frames ahead of the beat for perceived visual energy |
| `(?i)(speed|ramp|and|timewarp|bezier|curve|calculator)` | `[165]` | `speed-ramp-and-timewarp-bezier-curve-calculator.md` | Calculating 100% -> 400% -> 25% velocity ramps with smooth tangents |
| `(?i)(rhythm|map|beat|by|beat|tempo|serializer)` | `[166]` | `rhythm-map-beat-by-beat-tempo-serializer.md` | Generating the `rhythm_map` and `pacing_notes` fields for the EDL |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[156]`.
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

