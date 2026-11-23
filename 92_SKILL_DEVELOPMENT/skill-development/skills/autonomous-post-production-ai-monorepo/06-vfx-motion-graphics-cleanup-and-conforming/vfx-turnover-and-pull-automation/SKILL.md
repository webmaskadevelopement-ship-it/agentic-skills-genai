---
file_id: "[388]"
skill_path: "06-vfx-motion-graphics-cleanup-and-conforming/vfx-turnover-and-pull-automation/SKILL.md"
role: "Sub-Skill Router: Sub-Router: VFX Spotting, EXR Plate Pulls & Camera Metadata"
parent_router: "[378]"
child_nodes:
  - "[389]"
  - "[390]"
  - "[391]"
  - "[392]"
  - "[393]"
  - "[394]"
  - "[395]"
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

# [388] Sub-Router: VFX Spotting, EXR Plate Pulls & Camera Metadata

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `06-vfx-motion-graphics-cleanup-and-conforming/vfx-turnover-and-pull-automation`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(vfx|shot|identification|and|naming|registry)` | `[389]` | `vfx-shot-identification-and-naming-registry.md` | Enforcing `SHOW_EP101_020_010_v001` naming and status tracking |
| `(?i)(openexr|16bit|half|float|acescg|linear|plate|pull)` | `[390]` | `openexr-16bit-half-float-acescg-linear-plate-pull.md` | Exporting unclipped linear AP1 plates with PI-Z / DWAA compression |
| `(?i)(vfx|handle|padding|8|12|24|frame|head|tail|math)` | `[391]` | `vfx-handle-padding-8-12-24-frame-head-tail-math.md` | Extending source pulls by exact handle length with slate Frame 1001 |
| `(?i)(vfx|count|sheet|and|thumbnail|turnover|generator)` | `[392]` | `vfx-count-sheet-and-thumbnail-turnover-generator.md` | Generating CSV/PDF/MD count sheets with frame ranges and brief notes |
| `(?i)(lens|distortion|grid|stmap|uv|export|protocol)` | `[393]` | `lens-distortion-grid-stmap-uv-export-protocol.md` | Generating 32-bit float RG UV warpers for undistort/redistort workflow |
| `(?i)(3d|camera|track|point|cloud|and|fbx|usd|exporter)` | `[394]` | `3d-camera-track-point-cloud-and-fbx-usd-exporter.md` | Solving focal length and 6-DOF camera path for CG integration |
| `(?i)(on|set|hdri|chrome|ball|and|macbeth|reference|pack)` | `[395]` | `on-set-hdri-chrome-ball-and-macbeth-reference-pack.md` | Bundling lighting spheres and Neutral Grade CDL (.ccc) with plates |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[388]`.
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

