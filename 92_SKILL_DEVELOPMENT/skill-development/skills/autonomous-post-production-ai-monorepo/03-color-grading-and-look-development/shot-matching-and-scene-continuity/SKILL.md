---
file_id: "[243]"
skill_path: "03-color-grading-and-look-development/shot-matching-and-scene-continuity/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Multi-Camera & Scene-Wide Shot Matching Protocol"
parent_router: "[177]"
child_nodes:
  - "[244]"
  - "[245]"
  - "[246]"
  - "[247]"
  - "[248]"
  - "[249]"
  - "[250]"
  - "[251]"
  - "[252]"
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

# [243] Sub-Router: Multi-Camera & Scene-Wide Shot Matching Protocol

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `03-color-grading-and-look-development/shot-matching-and-scene-continuity`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(hero|shot|selection|and|reference|still|locking)` | `[244]` | `hero-shot-selection-and-reference-still-locking.md` | Choosing the master wide or key close-up as scene anchor |
| `(?i)(four|step|shot|match|exposure|wb|contrast|skin)` | `[245]` | `four-step-shot-match-exposure-wb-contrast-skin.md` | Sequential matching: 1. Luma IRE -> 2. Parade WB -> 3. Contrast -> 4. Skin |
| `(?i)(reverse|angle|lighting|ratio|reconciliation)` | `[246]` | `reverse-angle-lighting-ratio-reconciliation.md` | Matching sunlit A-side to backlit/shaded B-side reverse coverage |
| `(?i)(mixed|color|temperature|lighting|neutralization)` | `[247]` | `mixed-color-temperature-lighting-neutralization.md` | Balancing 3200K tungsten practicals against 5600K daylight windows |
| `(?i)(fluorescent|and|cheap|led|green|spike|removal)` | `[248]` | `fluorescent-and-cheap-led-green-spike-removal.md` | Countering CRI gaps and green-magenta tint shifts in location footage |
| `(?i)(x|rite|colorchecker|chart|matrix|alignment)` | `[249]` | `x-rite-colorchecker-chart-matrix-alignment.md` | Calculating objective 24-patch delta-E minimization across cameras |
| `(?i)(cloud|cover|and|time|of|day|exterior|drift|matching)` | `[250]` | `cloud-cover-and-time-of-day-exterior-drift-matching.md` | Matching golden-hour takes to harsh mid-day pickups seamlessly |
| `(?i)(archival|and|stock|footage|grade|harmonization)` | `[251]` | `archival-and-stock-footage-grade-harmonization.md` | De-sharpening and re-graining stock clips to match cinema A-cam |
| `(?i)(group|pre|clip|and|post|clip|shared|node|routing)` | `[252]` | `group-pre-clip-and-post-clip-shared-node-routing.md` | Structuring Shot-Level balance in Clip nodes vs Scene Look in Group Post-Clip |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[243]`.
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

