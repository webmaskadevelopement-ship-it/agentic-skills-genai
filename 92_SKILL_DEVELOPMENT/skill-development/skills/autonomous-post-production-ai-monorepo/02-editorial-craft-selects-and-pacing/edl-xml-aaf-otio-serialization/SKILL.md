---
file_id: "[167]"
skill_path: "02-editorial-craft-selects-and-pacing/edl-xml-aaf-otio-serialization/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Timeline Interchange Serialization & Validation"
parent_router: "[101]"
child_nodes:
  - "[168]"
  - "[169]"
  - "[170]"
  - "[171]"
  - "[172]"
  - "[173]"
  - "[174]"
  - "[175]"
  - "[176]"
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

# [167] Sub-Router: Timeline Interchange Serialization & Validation

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `02-editorial-craft-selects-and-pacing/edl-xml-aaf-otio-serialization`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(json|edl|cut|manifest|compiler)` | `[168]` | `json-edl-cut-manifest-compiler.md` | Compiling the master JSON EDL with `selection_rationale` |
| `(?i)(cmx|3600|plain|text|edl|exporter)` | `[169]` | `cmx-3600-plain-text-edl-exporter.md` | Emitting strict 8-char reel CMX 3600 EDL with `* FROM CLIP NAME` |
| `(?i)(final|cut|pro|7|xml|v5|interchange|generator)` | `[170]` | `final-cut-pro-7-xml-v5-interchange-generator.md` | Generating legacy xmeml v5 for Premiere/Resolve/Baselight import |
| `(?i)(apple|fcpxml|v1|11|spine|and|lane|serializer)` | `[171]` | `apple-fcpxml-v1-11-spine-and-lane-serializer.md` | Emitting asset-clip, gap, and connected-lane FCPXML structures |
| `(?i)(avid|aaf|composition|mob|and|master|mob|mapper)` | `[172]` | `avid-aaf-composition-mob-and-master-mob-mapper.md` | Mapping EditRate, SourceClip, and TimelineMobSlot structures |
| `(?i)(opentimelineio|otio|universal|schema|adapter)` | `[173]` | `opentimelineio-otio-universal-schema-adapter.md` | Serializing Pixar OTIO Stack, Track, Clip, and ExternalReference |
| `(?i)(edl|monotonic|record|timecode|validator)` | `[174]` | `edl-monotonic-record-timecode-validator.md` | Ensuring zero record-TC overlaps, gaps, or negative durations |
| `(?i)(source|handle|availability|bounds|checker)` | `[175]` | `source-handle-availability-bounds-checker.md` | Verifying `source_in - handle >= media_start` across all cuts |
| `(?i)(human|readable|markdown|cut|rationale|report)` | `[176]` | `human-readable-markdown-cut-rationale-report.md` | Rendering executive review document for timeline-free signoff |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[167]`.
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

