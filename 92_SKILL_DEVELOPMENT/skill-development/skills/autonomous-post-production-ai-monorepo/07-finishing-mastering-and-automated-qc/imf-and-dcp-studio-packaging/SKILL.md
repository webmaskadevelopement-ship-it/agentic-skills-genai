---
file_id: "[420]"
skill_path: "07-finishing-mastering-and-automated-qc/imf-and-dcp-studio-packaging/SKILL.md"
role: "Sub-Skill Router: Sub-Router: SMPTE IMF ST.2067 & Digital Cinema Package (DCP)"
parent_router: "[410]"
child_nodes:
  - "[421]"
  - "[422]"
  - "[423]"
  - "[424]"
  - "[425]"
  - "[426]"
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

# [420] Sub-Router: SMPTE IMF ST.2067 & Digital Cinema Package (DCP)

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `07-finishing-mastering-and-automated-qc/imf-and-dcp-studio-packaging`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(smpte|imf|app|2e|jpeg2000|video|track|file|builder)` | `[421]` | `smpte-imf-app-2e-jpeg2000-video-track-file-builder.md` | Packaging lossless/visually-lossless J2K MXF track files |
| `(?i)(smpte|imf|composition|playlist|cpl|xml|generator)` | `[422]` | `smpte-imf-composition-playlist-cpl-xml-generator.md` | Constructing multi-version regional CPL timelines without re-rendering video |
| `(?i)(smpte|imf|packing|list|pkl|and|assetmap|builder)` | `[423]` | `smpte-imf-packing-list-pkl-and-assetmap-builder.md` | Generating SHA-1 asset hashes and UUID cross-reference manifests |
| `(?i)(supplemental|imf|package|imp|delta|patch|builder)` | `[424]` | `supplemental-imf-package-imp-delta-patch-builder.md` | Exporting only fixed frames/shots as a lightweight supplemental IMP |
| `(?i)(theatrical|dcp|xyz|12bit|2|6|gamma|j2k|encoder)` | `[425]` | `theatrical-dcp-xyz-12bit-2-6-gamma-j2k-encoder.md` | Converting RGB to CIE XYZ 250 Mbps JPEG 2000 frame sequences |
| `(?i)(dcp|kdm|encryption|and|smpte|rdd52|validator)` | `[426]` | `dcp-kdm-encryption-and-smpte-rdd52-validator.md` | Validating SMPTE DCP structure, 24.000 fps lock, and 5.1/7.1 PCM essence |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[420]`.
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

