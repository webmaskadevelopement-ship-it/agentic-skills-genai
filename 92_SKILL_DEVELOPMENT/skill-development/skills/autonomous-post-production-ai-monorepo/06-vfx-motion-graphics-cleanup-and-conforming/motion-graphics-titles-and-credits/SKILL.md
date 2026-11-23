---
file_id: "[404]"
skill_path: "06-vfx-motion-graphics-cleanup-and-conforming/motion-graphics-titles-and-credits/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Typography, Lower Thirds, Sub-safe Zones & Credits"
parent_router: "[378]"
child_nodes:
  - "[405]"
  - "[406]"
  - "[407]"
  - "[408]"
  - "[409]"
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

# [404] Sub-Router: Typography, Lower Thirds, Sub-safe Zones & Credits

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `06-vfx-motion-graphics-cleanup-and-conforming/motion-graphics-titles-and-credits`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(broadcast|title|safe|90|and|action|safe|93|guides)` | `[405]` | `broadcast-title-safe-90-and-action-safe-93-guides.md` | Enforcing SMPTE RP-2046-2 safe area boundaries for all text overlays |
| `(?i)(lower|third|entry|hold|exit|kinetic|typography)` | `[406]` | `lower-third-entry-hold-exit-kinetic-typography.md` | Calculating reading duration (min 3.5s) and smooth cubic-bezier easing |
| `(?i)(end|credit|scroll|integer|pixel|per|frame|anti|judder)` | `[407]` | `end-credit-scroll-integer-pixel-per-frame-anti-judder.md` | Enforcing exact integer vertical velocity (e.g., 3.0 or 4.0 px/frame) |
| `(?i)(main|title|card|contrast|and|luminance|legibility)` | `[408]` | `main-title-card-contrast-and-luminance-legibility.md` | Ensuring legal SDR/HDR peak brightness (<= 100–200 nits) on white titles |
| `(?i)(graphics|alpha|channel|straight|vs|premultiplied)` | `[409]` | `graphics-alpha-channel-straight-vs-premultiplied.md` | Preventing dark fringes on ProRes 4444 / EXR graphic overlays |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[404]`.
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

