---
file_id: "[193]"
skill_path: "03-color-grading-and-look-development/scope-analytics-and-evidence-extraction/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Waveform, Vectorscope, Parade & Histogram Analysis"
parent_router: "[177]"
child_nodes:
  - "[194]"
  - "[195]"
  - "[196]"
  - "[197]"
  - "[198]"
  - "[199]"
  - "[200]"
  - "[201]"
  - "[202]"
  - "[203]"
  - "[204]"
  - "[205]"
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

# [193] Sub-Router: Waveform, Vectorscope, Parade & Histogram Analysis

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `03-color-grading-and-look-development/scope-analytics-and-evidence-extraction`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(waveform|luma|ire|black|point|calibration)` | `[194]` | `waveform-luma-ire-black-point-calibration.md` | Setting shadow floor between 2–5 IRE without crushing detail at 0 |
| `(?i)(waveform|luma|ire|white|point|and|specular|ceiling)` | `[195]` | `waveform-luma-ire-white-point-and-specular-ceiling.md` | Controlling diffuse white (80–90 IRE) vs specular peaks (95–100 IRE) |
| `(?i)(waveform|midtone|exposure|placement|by|key|type)` | `[196]` | `waveform-midtone-exposure-placement-by-key-type.md` | Placing facial key exposure: High-Key (55–65 IRE), Low-Key (25–40 IRE) |
| `(?i)(vectorscope|skin|tone|i|line|alignment|protocol)` | `[197]` | `vectorscope-skin-tone-i-line-alignment-protocol.md` | Aligning human melanin reflectance along the 123° I-line axis |
| `(?i)(vectorscope|melanin|saturation|vs|luminance|scaling)` | `[198]` | `vectorscope-melanin-saturation-vs-luminance-scaling.md` | Adjusting vector magnitude for deep vs fair complexions accurately |
| `(?i)(vectorscope|global|color|cast|centroid|diagnosis)` | `[199]` | `vectorscope-global-color-cast-centroid-diagnosis.md` | Identifying trace drift away from center reticle on neutral grays |
| `(?i)(vectorscope|broadcast|legal|75|percent|box|auditor)` | `[200]` | `vectorscope-broadcast-legal-75-percent-box-auditor.md` | Detecting chrominance excursions beyond SMPTE legal vector targets |
| `(?i)(rgb|parade|shadow|neutralization|alignment)` | `[201]` | `rgb-parade-shadow-neutralization-alignment.md` | Balancing R=G=B shadow floors to eliminate muddy green/magenta blacks |
| `(?i)(rgb|parade|highlight|neutralization|and|tint|check)` | `[202]` | `rgb-parade-highlight-neutralization-and-tint-check.md` | Equalizing R/G/B ceiling heights on specular and cloud highlights |
| `(?i)(histogram|tonal|spread|and|banding|detector)` | `[203]` | `histogram-tonal-spread-and-banding-detector.md` | Identifying 8-bit comb gaps and posterization risks after heavy push |
| `(?i)(cie|1931|xy|chromaticity|gamut|boundary|analyzer)` | `[204]` | `cie-1931-xy-chromaticity-gamut-boundary-analyzer.md` | Auditing exact wavelength coordinates against Rec.709/P3 triangles |
| `(?i)(false|color|ire|zone|exposure|mapper)` | `[205]` | `false-color-ire-zone-exposure-mapper.md` | Translating Pink/Green/Grey/Red/Purple false-color zones to node math |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[193]`.
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

