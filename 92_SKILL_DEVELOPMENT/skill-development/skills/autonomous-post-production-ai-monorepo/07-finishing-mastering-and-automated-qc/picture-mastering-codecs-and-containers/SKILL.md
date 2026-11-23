---
file_id: "[411]"
skill_path: "07-finishing-mastering-and-automated-qc/picture-mastering-codecs-and-containers/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Mezzanine Codecs, Bitrates, Rasters & Blankings"
parent_router: "[410]"
child_nodes:
  - "[412]"
  - "[413]"
  - "[414]"
  - "[415]"
  - "[416]"
  - "[417]"
  - "[418]"
  - "[419]"
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

# [411] Sub-Router: Mezzanine Codecs, Bitrates, Rasters & Blankings

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `07-finishing-mastering-and-automated-qc/picture-mastering-codecs-and-containers`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(apple|prores|422|hq|and|4444|xq|mastering|profile)` | `[412]` | `apple-prores-422-hq-and-4444-xq-mastering-profile.md` | 10-bit 4:2:2 (220 Mbps) vs 12-bit 4:4:4:4 XQ (500 Mbps) MOV profiles |
| `(?i)(avid|dnxhr|hqx|10bit|and|444|12bit|mxf|op1a)` | `[413]` | `avid-dnxhr-hqx-10bit-and-444-12bit-mxf-op1a.md` | SMPTE RDD-36 MXF OP1a broadcast mastering container specs |
| `(?i)(sony|xavc|intra|class|300|and|480|mxf|master)` | `[414]` | `sony-xavc-intra-class-300-and-480-mxf-master.md` | CBG 10-bit 4:2:2 Intra-frame mastering for UHD broadcast delivery |
| `(?i)(h264|and|hevc|h265|abr|streaming|encoding|ladder)` | `[415]` | `h264-and-hevc-h265-abr-streaming-encoding-ladder.md` | 2-pass VBR/CRF rate control, GOP size (2s), and profile/level settings |
| `(?i)(av1|and|vp9|next|gen|web|distribution|encoding)` | `[416]` | `av1-and-vp9-next-gen-web-distribution-encoding.md` | Configuring 10-bit film-grain synthesis and tile-based web encoding |
| `(?i)(resolution|and|raster|validation|hd|uhd|dci2k|dci4k)` | `[417]` | `resolution-and-raster-validation-hd-uhd-dci2k-dci4k.md` | Verifying exact pixel dimensions and 1.0 square pixel aspect ratio |
| `(?i)(active|image|area|and|letterbox|blanking|auditor)` | `[418]` | `active-image-area-and-letterbox-blanking-auditor.md` | Ensuring 100% pure digital black (R=0,G=0,B=0) in matte bars, zero half-pixels |
| `(?i)(quicktime|nclc|color|atoms|1|1|1|vs|1|2|1|tagger)` | `[419]` | `quicktime-nclc-color-atoms-1-1-1-vs-1-2-1-tagger.md` | Writing exact Primaries/Transfer/Matrix metadata tags into MOV/MP4 headers |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[411]`.
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

