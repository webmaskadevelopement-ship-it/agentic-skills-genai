---
file_id: "[461]"
skill_path: "08-specialized-genre-and-format-playbooks/documentary-and-unscripted-non-fiction/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Feature Doc, Docuseries & True Crime Post"
parent_router: "[454]"
child_nodes:
  - "[462]"
  - "[463]"
  - "[464]"
  - "[465]"
  - "[466]"
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

# [461] Sub-Router: Feature Doc, Docuseries & True Crime Post

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `08-specialized-genre-and-format-playbooks/documentary-and-unscripted-non-fiction`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(multi|hour|interview|synthesis|into|narrative|pods)` | `[462]` | `multi-hour-interview-synthesis-into-narrative-pods.md` | Distilling 40+ hours of talking heads into thematic story chapters |
| `(?i)(verite|observational|scene|invisible|stitching)` | `[463]` | `verite-observational-scene-invisible-stitching.md` | Cutting chaotic handheld verite using B-roll bridges and natural sound |
| `(?i)(archival|photo|ken|burns|and|parallax|2|5d|rigging)` | `[464]` | `archival-photo-ken-burns-and-parallax-2-5d-rigging.md` | Animating still photographs with subtle depth separation and film dust |
| `(?i)(true|crime|evidence|callout|and|timeline|graphics)` | `[465]` | `true-crime-evidence-callout-and-timeline-graphics.md` | Highlighting documents, 911 audio waveforms, and map progressions |
| `(?i)(documentary|ethical|frankenbite|disclosure|auditor)` | `[466]` | `documentary-ethical-frankenbite-disclosure-auditor.md` | Ensuring composite edits never invert or fabricate speaker meaning |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[461]`.
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

