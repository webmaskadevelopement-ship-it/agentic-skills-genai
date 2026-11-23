---
file_id: "[396]"
skill_path: "06-vfx-motion-graphics-cleanup-and-conforming/invisible-cleanup-roto-and-compositing/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Chroma Key, Paint-Out, Screen Comp & Beauty"
parent_router: "[378]"
child_nodes:
  - "[397]"
  - "[398]"
  - "[399]"
  - "[400]"
  - "[401]"
  - "[402]"
  - "[403]"
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

# [396] Sub-Router: Chroma Key, Paint-Out, Screen Comp & Beauty

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `06-vfx-motion-graphics-cleanup-and-conforming/invisible-cleanup-roto-and-compositing`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(chroma|key|core|matte|plus|soft|edge|combination)` | `[397]` | `chroma-key-core-matte-plus-soft-edge-combination.md` | Combining IBK/Delta keyer soft hair edges with solid core garbage matte |
| `(?i)(green|blue|spill|suppression|and|edge|light|wrap)` | `[398]` | `green-blue-spill-suppression-and-edge-light-wrap.md` | Despilling reflections and wrapping background luminance onto edges |
| `(?i)(wire|rig|and|boom|mic|temporal|clone|paint|out)` | `[399]` | `wire-rig-and-boom-mic-temporal-clone-paint-out.md` | Planar tracking clean background patches to erase production gear |
| `(?i)(dead|pixel|sensor|dust|and|lens|flare|dirt|removal)` | `[400]` | `dead-pixel-sensor-dust-and-lens-flare-dirt-removal.md` | Automated median/spatial healing of hot pixels and dust spots |
| `(?i)(planar|corner|pin|phone|and|monitor|screen|comp)` | `[401]` | `planar-corner-pin-phone-and-monitor-screen-comp.md` | Sub-pixel Mocha planar tracking with reflection, finger roto & defocus |
| `(?i)(frequency|separation|skin|blemish|and|beauty|work)` | `[402]` | `frequency-separation-skin-blemish-and-beauty-work.md` | Separating high-frequency skin pores from low-frequency blotchiness |
| `(?i)(composite|grain|matching|and|color|space|roundtrip)` | `[403]` | `composite-grain-matching-and-color-space-roundtrip.md` | Re-graining clean patches only inside the alpha matte to match plate |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[396]`.
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

