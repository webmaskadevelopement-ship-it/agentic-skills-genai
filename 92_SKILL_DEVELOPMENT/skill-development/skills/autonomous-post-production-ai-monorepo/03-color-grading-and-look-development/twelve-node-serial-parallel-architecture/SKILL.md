---
file_id: "[206]"
skill_path: "03-color-grading-and-look-development/twelve-node-serial-parallel-architecture/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Standardized 12-Node Pipeline Construction"
parent_router: "[177]"
child_nodes:
  - "[207]"
  - "[208]"
  - "[209]"
  - "[210]"
  - "[211]"
  - "[212]"
  - "[213]"
  - "[214]"
  - "[215]"
  - "[216]"
  - "[217]"
  - "[218]"
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

# [206] Sub-Router: Standardized 12-Node Pipeline Construction

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `03-color-grading-and-look-development/twelve-node-serial-parallel-architecture`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(node|01|technical|input|cst|and|noise|reduction)` | `[207]` | `node-01-technical-input-cst-and-noise-reduction.md` | Spatial/Temporal NR (2 frames, Medium luma) + Input Color Transform |
| `(?i)(node|02|global|exposure|offset|and|printer|lights)` | `[208]` | `node-02-global-exposure-offset-and-printer-lights.md` | Linear exposure positioning before non-linear contrast shaping |
| `(?i)(node|03|contrast|ratio|and|pivot|center|shaping)` | `[209]` | `node-03-contrast-ratio-and-pivot-center-shaping.md` | Establishing dynamic range spread around middle-grey pivot (0.435) |
| `(?i)(node|04|primary|balance|lift|gamma|gain|wb)` | `[210]` | `node-04-primary-balance-lift-gamma-gain-wb.md` | Neutralizing scene color temperature and green/magenta tint shifts |
| `(?i)(node|05|parallel|hsl|skin|tone|isolation|and|heal)` | `[211]` | `node-05-parallel-hsl-skin-tone-isolation-and-heal.md` | Dedicated parallel node for complexion vector alignment and softening |
| `(?i)(node|06|parallel|hsl|sky|and|foliage|sculpting)` | `[212]` | `node-06-parallel-hsl-sky-and-foliage-sculpting.md` | Controlling cyan/blue sky density and yellow-green foliage shift |
| `(?i)(node|07|power|windows|vignette|and|eye|light)` | `[213]` | `node-07-power-windows-vignette-and-eye-light.md` | Tracked circular/polygon masks for subject separation and relighting |
| `(?i)(node|08|depth|map|z|buffer|atmospheric|separation)` | `[214]` | `node-08-depth-map-z-buffer-atmospheric-separation.md` | Foreground vs background contrast and haze separation |
| `(?i)(node|09|creative|look|split|tone|and|matrix)` | `[215]` | `node-09-creative-look-split-tone-and-matrix.md` | Scene-level creative color palette and RGB mixer cross-talk |
| `(?i)(node|10|film|print|emulation|and|tonal|curve)` | `[216]` | `node-10-film-print-emulation-and-tonal-curve.md` | Applying film stock response curve under output space constraints |
| `(?i)(node|11|halation|bloom|and|organic|film|grain)` | `[217]` | `node-11-halation-bloom-and-organic-film-grain.md` | Emulating emulsion red scatter, optical diffusion, and silver halide |
| `(?i)(node|12|output|cst|gamut|limiter|and|legal|clip)` | `[218]` | `node-12-output-cst-gamut-limiter-and-legal-clip.md` | Final transform to delivery display space with hard legal soft-clip |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[206]`.
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

