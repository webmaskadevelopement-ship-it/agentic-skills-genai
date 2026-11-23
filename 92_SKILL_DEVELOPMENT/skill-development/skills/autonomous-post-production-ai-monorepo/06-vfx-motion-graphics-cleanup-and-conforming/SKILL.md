---
file_id: "[378]"
skill_path: "06-vfx-motion-graphics-cleanup-and-conforming/SKILL.md"
role: "Department Router: Department Router: Online Conform, VFX Pulls, Cleanup & GFX"
parent_router: "[001]"
child_nodes:
  - "[379]"
  - "[388]"
  - "[396]"
  - "[404]"
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

# [378] Department Router: Online Conform, VFX Pulls, Cleanup & GFX

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `06-vfx-motion-graphics-cleanup-and-conforming`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(SKILL)` | `[379]` | `SKILL.md` | Sub-Router: Proxy-to-RAW Relinking, Pan-Scan & Reconform |
| `(?i)(SKILL)` | `[388]` | `SKILL.md` | Sub-Router: VFX Spotting, EXR Plate Pulls & Camera Metadata |
| `(?i)(SKILL)` | `[396]` | `SKILL.md` | Sub-Router: Chroma Key, Paint-Out, Screen Comp & Beauty |
| `(?i)(SKILL)` | `[404]` | `SKILL.md` | Sub-Router: Typography, Lower Thirds, Sub-safe Zones & Credits |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[378]`.
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

