---
file_id: "[253]"
skill_path: "03-color-grading-and-look-development/look-development-and-finishing-optics/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Film Emulation, LUT Engineering & Optical FX"
parent_router: "[177]"
child_nodes:
  - "[254]"
  - "[255]"
  - "[256]"
  - "[257]"
  - "[258]"
  - "[259]"
  - "[260]"
  - "[261]"
  - "[262]"
  - "[263]"
  - "[264]"
  - "[265]"
  - "[266]"
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

# [253] Sub-Router: Film Emulation, LUT Engineering & Optical FX

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `03-color-grading-and-look-development/look-development-and-finishing-optics`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(kodak|2383|print|film|emulation|curve|and|matrix)` | `[254]` | `kodak-2383-print-film-emulation-curve-and-matrix.md` | Classic Hollywood print contrast, cyan-shifted blues & warm skin |
| `(?i)(kodak|2393|premier|high|contrast|print|emulation)` | `[255]` | `kodak-2393-premier-high-contrast-print-emulation.md` | Deep shadow density and rich primary saturation characteristics |
| `(?i)(fujifilm|3510|and|3513|eterna|print|emulation)` | `[256]` | `fujifilm-3510-and-3513-eterna-print-emulation.md` | Soft pastel roll-off, emerald greens, and neutral shadow rendering |
| `(?i)(kodak|portra|400|and|vision3|500t|5219|emulation)` | `[257]` | `kodak-portra-400-and-vision3-500t-5219-emulation.md` | Negative stock latitude, fine grain structure, and warm midtones |
| `(?i)(bleach|bypass|silver|retention|look|architecture)` | `[258]` | `bleach-bypass-silver-retention-look-architecture.md` | High local contrast, desaturated midtones, and metallic speculars |
| `(?i)(teal|and|orange|complementary|split|tone|design)` | `[259]` | `teal-and-orange-complementary-split-tone-design.md` | Controlled shadow-cooling and skin-warming without plasticky clipping |
| `(?i)(day|for|night|convincing|moonlight|conversion)` | `[260]` | `day-for-night-convincing-moonlight-conversion.md` | Underexposing -2.5 stops, softening contrast, cooling gamma, masking sky |
| `(?i)(halation|emulsion|red|scatter|physics|model)` | `[261]` | `halation-emulsion-red-scatter-physics-model.md` | High-contrast edge detection -> red-orange channel blur -> screen blend |
| `(?i)(optical|bloom|and|pro|mist|filtration|emulation)` | `[262]` | `optical-bloom-and-pro-mist-filtration-emulation.md` | Highlight threshold extraction -> multi-octave Gaussian glow |
| `(?i)(organic|film|grain|8mm|16mm|35mm|65mm|synthesis)` | `[263]` | `organic-film-grain-8mm-16mm-35mm-65mm-synthesis.md` | Size, strength, roughness, and shadow-weighted grain opacity curves |
| `(?i)(lens|vignette|and|anamorphic|edge|aberration)` | `[264]` | `lens-vignette-and-anamorphic-edge-aberration.md` | Subtle optical falloff and peripheral lateral chromatic aberration |
| `(?i)(3d|lut|33x33x33|cube|export|and|stress|testing)` | `[265]` | `3d-lut-33x33x33-cube-export-and-stress-testing.md` | Validating LUT continuity against ramp sweeps to prevent quantization tears |
| `(?i)(grade|spec|json|and|drx|metadata|serializer)` | `[266]` | `grade-spec-json-and-drx-metadata-serializer.md` | Compiling complete File B Grade Specification with scope evidence |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[253]`.
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

