---
file_id: "[126]"
skill_path: "02-editorial-craft-selects-and-pacing/progressive-edit-stage-gates/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Stage-by-Stage Refinement Pipeline"
parent_router: "[101]"
child_nodes:
  - "[127]"
  - "[128]"
  - "[129]"
  - "[130]"
  - "[131]"
  - "[132]"
  - "[133]"
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

# [126] Sub-Router: Stage-by-Stage Refinement Pipeline

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `02-editorial-craft-selects-and-pacing/progressive-edit-stage-gates`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(stage|1|radio|edit|dialogue|only|gate)` | `[127]` | `stage-1-radio-edit-dialogue-only-gate.md` | Evaluating narrative coherence with eyes closed (audio-only pass) |
| `(?i)(stage|2|assembly|cut|completeness|gate)` | `[128]` | `stage-2-assembly-cut-completeness-gate.md` | Laying all script scenes in order without over-tightening |
| `(?i)(stage|3|rough|cut|structural|reordering|gate)` | `[129]` | `stage-3-rough-cut-structural-reordering-gate.md` | Scene transposition, intercutting, and dead-weight scene deletion |
| `(?i)(stage|4|fine|cut|frame|level|tightening|gate)` | `[130]` | `stage-4-fine-cut-frame-level-tightening-gate.md` | Shaving 2-to-8 frames off heads/tails, perfecting J/L overlaps |
| `(?i)(stage|5|director|and|producer|notes|reconciler)` | `[131]` | `stage-5-director-and-producer-notes-reconciler.md` | Parsing timecoded review notes into deterministic EDL mutations |
| `(?i)(stage|6|picture|lock|freeze|and|signoff|gate)` | `[132]` | `stage-6-picture-lock-freeze-and-signoff-gate.md` | Freezing frame counts, adding 2-pop, and locking turnover hashes |
| `(?i)(runtime|target|compression|and|expansion|engine)` | `[133]` | `runtime-target-compression-and-expansion-engine.md` | Hitting exact broadcast clock (e.g., 21:30:00) via distributed trims |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[126]`.
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

