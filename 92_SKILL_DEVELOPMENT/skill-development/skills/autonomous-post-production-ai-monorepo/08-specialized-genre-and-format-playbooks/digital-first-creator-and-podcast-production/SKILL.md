---
file_id: "[473]"
skill_path: "08-specialized-genre-and-format-playbooks/digital-first-creator-and-podcast-production/SKILL.md"
role: "Sub-Skill Router: Sub-Router: YouTube, Video Podcasts & Vertical Social Engines"
parent_router: "[454]"
child_nodes:
  - "[474]"
  - "[475]"
  - "[476]"
  - "[477]"
  - "[478]"
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

# [473] Sub-Router: YouTube, Video Podcasts & Vertical Social Engines

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `08-specialized-genre-and-format-playbooks/digital-first-creator-and-podcast-production`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(youtube|first|30|seconds|hook|and|proof|engineering)` | `[474]` | `youtube-first-30-seconds-hook-and-proof-engineering.md` | Eliminating throat-clearing intros to maximize 30-second retention |
| `(?i)(video|podcast|3|camera|auto|switching|heuristics)` | `[475]` | `video-podcast-3-camera-auto-switching-heuristics.md` | Switching to active speaker + cutting to two-shot on shared laughter |
| `(?i)(vertical|9x16|dynamic|caption|word|highlight|engine)` | `[476]` | `vertical-9x16-dynamic-caption-word-highlight-engine.md` | Generating active-word karaoke pop captions in center-safe zone |
| `(?i)(educational|screen|recording|zoom|and|cursor|smooth)` | `[477]` | `educational-screen-recording-zoom-and-cursor-smooth.md` | Keyframing smooth pan-and-zooms to follow UI clicks and code blocks |
| `(?i)(multi|platform|repurposing|1|long|to|15|micro|cuts)` | `[478]` | `multi-platform-repurposing-1-long-to-15-micro-cuts.md` | Extracting self-contained viral micro-stories from long-form master |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[473]`.
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

