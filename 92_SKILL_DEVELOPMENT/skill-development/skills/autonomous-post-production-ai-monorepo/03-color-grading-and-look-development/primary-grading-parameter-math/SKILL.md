---
file_id: "[219]"
skill_path: "03-color-grading-and-look-development/primary-grading-parameter-math/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Lift, Gamma, Gain, Offset & HDR Wheel Mathematics"
parent_router: "[177]"
child_nodes:
  - "[220]"
  - "[221]"
  - "[222]"
  - "[223]"
  - "[224]"
  - "[225]"
  - "[226]"
  - "[227]"
  - "[228]"
  - "[229]"
  - "[230]"
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

# [219] Sub-Router: Lift, Gamma, Gain, Offset & HDR Wheel Mathematics

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `03-color-grading-and-look-development/primary-grading-parameter-math`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(lift|rgb|shadow|black|point|offset|math)` | `[220]` | `lift-rgb-shadow-black-point-offset-math.md` | Calculating R/G/B additive shadow shifts keeping white anchored at 1.0 |
| `(?i)(gamma|rgb|midtone|power|function|math)` | `[221]` | `gamma-rgb-midtone-power-function-math.md` | Calculating non-linear R/G/B exponent shifts preserving 0.0 and 1.0 |
| `(?i)(gain|rgb|highlight|multiplier|slope|math)` | `[222]` | `gain-rgb-highlight-multiplier-slope-math.md` | Calculating R/G/B multiplicative slope shifts anchored at 0.0 |
| `(?i)(offset|rgb|master|wheel|global|translation|math)` | `[223]` | `offset-rgb-master-wheel-global-translation-math.md` | Uniform additive translation across log/intermediate code values |
| `(?i)(printer|lights|quarter|half|full|point|calibration)` | `[224]` | `printer-lights-quarter-half-full-point-calibration.md` | Photochemical Red/Green/Blue/Cyan/Magenta/Yellow trim increments |
| `(?i)(contrast|and|pivot|s|curve|mathematical|model)` | `[225]` | `contrast-and-pivot-s-curve-mathematical-model.md` | Sigmoidal contrast gain and inflection point positioning |
| `(?i)(color|boost|vs|saturation|vs|subtractive|density)` | `[226]` | `color-boost-vs-saturation-vs-subtractive-density.md` | Comparing additive HSV saturation against filmic subtractive density |
| `(?i)(shadow|and|highlight|log|wheel|range|isolation)` | `[227]` | `shadow-and-highlight-log-wheel-range-isolation.md` | Using Low-Range and High-Range crossover sliders for tight toe/shoulder |
| `(?i)(hdr|wheels|black|dark|shadow|zone|exposure)` | `[228]` | `hdr-wheels-black-dark-shadow-zone-exposure.md` | Quarter-stop exposure & saturation control in lower stops |
| `(?i)(hdr|wheels|light|highlight|specular|zone|control)` | `[229]` | `hdr-wheels-light-highlight-specular-zone-control.md` | Recovering blown windows and shaping specular roll-off by stop |
| `(?i)(rgb|channel|mixer|crosstalk|3x3|matrix|math)` | `[230]` | `rgb-channel-mixer-crosstalk-3x3-matrix-math.md` | Designing 3x3 color matrices for custom primary calibration |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[219]`.
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

