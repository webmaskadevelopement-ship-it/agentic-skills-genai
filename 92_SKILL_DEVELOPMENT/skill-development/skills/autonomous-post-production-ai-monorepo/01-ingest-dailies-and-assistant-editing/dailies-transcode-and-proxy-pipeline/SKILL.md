---
file_id: "[063]"
skill_path: "01-ingest-dailies-and-assistant-editing/dailies-transcode-and-proxy-pipeline/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Dailies Generation, Burn-ins & Proxy Encoding"
parent_router: "[031]"
child_nodes:
  - "[064]"
  - "[065]"
  - "[066]"
  - "[067]"
  - "[068]"
  - "[069]"
  - "[070]"
  - "[071]"
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

# [063] Sub-Router: Dailies Generation, Burn-ins & Proxy Encoding

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `01-ingest-dailies-and-assistant-editing/dailies-transcode-and-proxy-pipeline`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(prores|422|proxy|and|lt|encoding|profile)` | `[064]` | `prores-422-proxy-and-lt-encoding-profile.md` | Optimal bitrates, gov structures & audio mapping for NLE proxies |
| `(?i)(avid|dnxhr|lb|and|sq|mxf|op|atom|packager)` | `[065]` | `avid-dnxhr-lb-and-sq-mxf-op-atom-packager.md` | Generating Avid MediaFiles OP-Atom structures and .pmr/.mdb databases |
| `(?i)(h264|h265|all|intra|review|dailies|profile)` | `[066]` | `h264-h265-all-intra-review-dailies-profile.md` | Frame-accurate scrubbing web proxies without B-frame lag |
| `(?i)(on|set|asc|cdl|and|show|lut|application)` | `[067]` | `on-set-asc-cdl-and-show-lut-application.md` | Baking Slope/Offset/Power/Saturation + 33x33x33 .cube into proxies |
| `(?i)(frame|burn|in|overlay|geometry|spec)` | `[068]` | `frame-burn-in-overlay-geometry-spec.md` | Positioning Reel, Clip, Source TC, Record TC, FPS & Watermark |
| `(?i)(aspect|ratio|framing|guide|overlay)` | `[069]` | `aspect-ratio-framing-guide-overlay.md` | Rendering 2.39:1, 1.85:1, 16:9, and 9:16 social center-cut guides |
| `(?i)(polyphonic|bwf|wav|channel|splitting|and|routing)` | `[070]` | `polyphonic-bwf-wav-channel-splitting-and-routing.md` | Mapping ISO tracks + Mix track from field recorder iXML metadata |
| `(?i)(circle|take|filtering|and|script|supervisor|reconcile)` | `[071]` | `circle-take-filtering-and-script-supervisor-reconcile.md` | Filtering print/circle takes from ScriptE / Filemaker XML logs |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[063]`.
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

