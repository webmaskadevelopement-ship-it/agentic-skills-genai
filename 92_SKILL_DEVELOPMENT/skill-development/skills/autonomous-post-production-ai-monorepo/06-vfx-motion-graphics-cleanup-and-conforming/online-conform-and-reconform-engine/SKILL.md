---
file_id: "[379]"
skill_path: "06-vfx-motion-graphics-cleanup-and-conforming/online-conform-and-reconform-engine/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Proxy-to-RAW Relinking, Pan-Scan & Reconform"
parent_router: "[378]"
child_nodes:
  - "[380]"
  - "[381]"
  - "[382]"
  - "[383]"
  - "[384]"
  - "[385]"
  - "[386]"
  - "[387]"
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

# [379] Sub-Router: Proxy-to-RAW Relinking, Pan-Scan & Reconform

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `06-vfx-motion-graphics-cleanup-and-conforming/online-conform-and-reconform-engine`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(proxy|to|camera|raw|reel|and|timecode|relinker)` | `[380]` | `proxy-to-camera-raw-reel-and-timecode-relinker.md` | Resolving proxy EDL cuts back to uncompressed R3D/ARRIRAW/X-OCN |
| `(?i)(offline|reference|pic|difference|matte|verifier)` | `[381]` | `offline-reference-pic-difference-matte-verifier.md` | Running pixel-difference blend check against offline locked QuickTime |
| `(?i)(reconform|delta|engine|edl|v1|to|edl|v2|differ)` | `[382]` | `reconform-delta-engine-edl-v1-to-edl-v2-differ.md` | Migrating existing grades and VFX across picture-lock revisions |
| `(?i)(optical|flow|vs|frame|blend|speed|change|conform)` | `[383]` | `optical-flow-vs-frame-blend-speed-change-conform.md` | Selecting motion-estimation vectors vs shutter blend for retimed clips |
| `(?i)(spatial|scaling|lanczos|catmull|rom|super|scale)` | `[384]` | `spatial-scaling-lanczos-catmull-rom-super-scale.md` | Upscaling HD archival or punched-in 4K shots cleanly to UHD/4K master |
| `(?i)(stabilization|translation|rotation|perspective|lock)` | `[385]` | `stabilization-translation-rotation-perspective-lock.md` | Smoothing unwanted camera jitter with minimum zoom crop penalty |
| `(?i)(rolling|shutter|jello|skew|compensation|math)` | `[386]` | `rolling-shutter-jello-skew-compensation-math.md` | Correcting CMOS sensor scanline skew during fast pans |
| `(?i)(smart|reframe|16x9|to|9x16|4x5|1x1|pan|scan)` | `[387]` | `smart-reframe-16x9-to-9x16-4x5-1x1-pan-scan.md` | Keyframing X-axis subject tracking for multi-aspect social deliverables |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[379]`.
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

