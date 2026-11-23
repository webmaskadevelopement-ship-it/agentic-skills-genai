---
file_id: "[081]"
skill_path: "01-ingest-dailies-and-assistant-editing/visual-scene-and-shot-indexing/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Visual Content Analysis, Shot Scale & Camera Motion"
parent_router: "[031]"
child_nodes:
  - "[082]"
  - "[083]"
  - "[084]"
  - "[085]"
  - "[086]"
  - "[087]"
  - "[088]"
  - "[089]"
  - "[090]"
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

# [081] Sub-Router: Visual Content Analysis, Shot Scale & Camera Motion

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `01-ingest-dailies-and-assistant-editing/visual-scene-and-shot-indexing`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(optical|shot|boundary|and|sub|clip|detector)` | `[082]` | `optical-shot-boundary-and-sub-clip-detector.md` | Detecting camera starts/stops, whip pans, and slate out-frames |
| `(?i)(shot|scale|classification|ecu|cu|ms|ws|ews)` | `[083]` | `shot-scale-classification-ecu-cu-ms-ws-ews.md` | Classifying Extreme Close-Up to Extreme Wide Shot geometry |
| `(?i)(camera|movement|taxonomy|pan|tilt|dolly|handheld)` | `[084]` | `camera-movement-taxonomy-pan-tilt-dolly-handheld.md` | Vector-flow classification of static, pan, tilt, gimbal, handheld |
| `(?i)(face|detection|eyeline|and|gaze|vector|tracker)` | `[085]` | `face-detection-eyeline-and-gaze-vector-tracker.md` | Tracking screen-left/screen-right eyelines for 180-degree rule |
| `(?i)(blink|detection|and|micro|expression|indexer)` | `[086]` | `blink-detection-and-micro-expression-indexer.md` | Frame-exact indexing of actor eye blinks for Murch blink-cutting |
| `(?i)(focus|sharpness|and|hunting|disqualification|scorer)` | `[087]` | `focus-sharpness-and-hunting-disqualification-scorer.md` | Laplacian variance scoring to flag soft-focus or hunting frames |
| `(?i)(camera|shake|and|unintended|bump|detector)` | `[088]` | `camera-shake-and-unintended-bump-detector.md` | Identifying tripod bumps, operator stumbles, and lens zooms |
| `(?i)(b|roll|semantic|object|and|action|tagger)` | `[089]` | `b-roll-semantic-object-and-action-tagger.md` | Indexing visual nouns and verbs in coverage for paper-edit matching |
| `(?i)(continuity|prop|wardrobe|and|position|tracker)` | `[090]` | `continuity-prop-wardrobe-and-position-tracker.md` | Flagging continuity mismatches across takes within the same scene |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[081]`.
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

