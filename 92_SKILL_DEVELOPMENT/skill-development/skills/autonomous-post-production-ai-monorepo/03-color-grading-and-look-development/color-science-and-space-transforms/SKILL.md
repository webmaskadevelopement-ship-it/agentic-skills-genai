---
file_id: "[178]"
skill_path: "03-color-grading-and-look-development/color-science-and-space-transforms/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Color Spaces, Transfer Functions & CST Math"
parent_router: "[177]"
child_nodes:
  - "[179]"
  - "[180]"
  - "[181]"
  - "[182]"
  - "[183]"
  - "[184]"
  - "[185]"
  - "[186]"
  - "[187]"
  - "[188]"
  - "[189]"
  - "[190]"
  - "[191]"
  - "[192]"
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

# [178] Sub-Router: Color Spaces, Transfer Functions & CST Math

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `03-color-grading-and-look-development/color-science-and-space-transforms`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(aces|v1|3|acescct|and|acescc|pipeline|config)` | `[179]` | `aces-v1-3-acescct-and-acescc-pipeline-config.md` | Configuring IDT -> ACESAP0 -> ACEScct Working -> RRT+ODT pipeline |
| `(?i)(davinci|wide|gamut|intermediate|color|managed|math)` | `[180]` | `davinci-wide-gamut-intermediate-color-managed-math.md` | Mapping camera raw into DWG/Intermediate logarithmic working space |
| `(?i)(arri|logc3|to|logc4|reveal|color|science|transform)` | `[181]` | `arri-logc3-to-logc4-reveal-color-science-transform.md` | Handling ARRI ALEXA 35 LogC4 / AWG4 vs legacy LogC3 / AWG3 |
| `(?i)(red|log3g10|and|redwidegamutrgb|input|transform)` | `[182]` | `red-log3g10-and-redwidegamutrgb-input-transform.md` | Exact CST parameters for RED IPP2 sensor gamut normalization |
| `(?i)(sony|slog3|and|sgamut3|cine|input|transform)` | `[183]` | `sony-slog3-and-sgamut3-cine-input-transform.md` | Distinguishing S-Gamut3 vs S-Gamut3.Cine chromaticity primaries |
| `(?i)(canon|log2|log3|and|cinema|gamut|transform)` | `[184]` | `canon-log2-log3-and-cinema-gamut-transform.md` | Mapping Canon Cinema Gamut without magenta highlight clipping |
| `(?i)(blackmagic|film|gen5|wide|gamut|transform)` | `[185]` | `blackmagic-film-gen5-wide-gamut-transform.md` | Normalizing Pocket/URSA Gen 5 curves to working space |
| `(?i)(dji|dlog|and|dlog|m|aerial|camera|normalization)` | `[186]` | `dji-dlog-and-dlog-m-aerial-camera-normalization.md` | Matching drone 10-bit H.265/ProRes log profiles to A-cam hero |
| `(?i)(rec709|gamma|2|4|vs|gamma|2|2|web|delivery|math)` | `[187]` | `rec709-gamma-2-4-vs-gamma-2-2-web-delivery-math.md` | Managing dim-surround Broadcast 2.4 vs sRGB/Mac QuickTime gamma shift |
| `(?i)(dci|p3|d65|and|theatrical|2|6|gamma|output|transform)` | `[188]` | `dci-p3-d65-and-theatrical-2-6-gamma-output-transform.md` | Configuring theatrical projection white point and transfer curve |
| `(?i)(hdr|st2084|pq|1000|4000|nit|mastering|transform)` | `[189]` | `hdr-st2084-pq-1000-4000-nit-mastering-transform.md` | Absolute luminance mapping in Perceptual Quantizer space |
| `(?i)(hdr|bt2100|hlg|hybrid|log|gamma|broadcast|transform)` | `[190]` | `hdr-bt2100-hlg-hybrid-log-gamma-broadcast-transform.md` | Scene-referred HLG backward-compatible SDR/HDR transform |
| `(?i)(dolby|vision|l1|l2|l8|dynamic|metadata|trim|pass)` | `[191]` | `dolby-vision-l1-l2-l8-dynamic-metadata-trim-pass.md` | Generating shot-by-shot PQ statistical analysis and 100-nit SDR trims |
| `(?i)(gamut|mapping|saturation|compression|knee|rolloff)` | `[192]` | `gamut-mapping-saturation-compression-knee-rolloff.md` | Compressing out-of-gamut neon/LED primaries into legal container |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[178]`.
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

