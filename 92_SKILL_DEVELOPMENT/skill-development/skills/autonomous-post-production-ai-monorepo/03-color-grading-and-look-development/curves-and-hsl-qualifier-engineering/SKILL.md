---
file_id: "[231]"
skill_path: "03-color-grading-and-look-development/curves-and-hsl-qualifier-engineering/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Spline Curves, Hue/Sat/Lum Curves & 3D Qualifiers"
parent_router: "[177]"
child_nodes:
  - "[232]"
  - "[233]"
  - "[234]"
  - "[235]"
  - "[236]"
  - "[237]"
  - "[238]"
  - "[239]"
  - "[240]"
  - "[241]"
  - "[242]"
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

# [231] Sub-Router: Spline Curves, Hue/Sat/Lum Curves & 3D Qualifiers

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `03-color-grading-and-look-development/curves-and-hsl-qualifier-engineering`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(custom|luma|curve|filmic|toe|and|shoulder|design)` | `[232]` | `custom-luma-curve-filmic-toe-and-shoulder-design.md` | Plotting 5-point bezier coordinates for creamy highlight roll-off |
| `(?i)(per|channel|rgb|curves|split|toning|control)` | `[233]` | `per-channel-rgb-curves-split-toning-control.md` | Lifting Blue in shadows while warming Red/Green in mid-highs |
| `(?i)(hue|vs|hue|targeted|color|rotation|math)` | `[234]` | `hue-vs-hue-targeted-color-rotation-math.md` | Rotating turquoise skies to deep cobalt or yellow grass to autumn gold |
| `(?i)(hue|vs|saturation|selective|chroma|taming)` | `[235]` | `hue-vs-saturation-selective-chroma-taming.md` | Pulling back neon signage and oversaturated wardrobe primaries |
| `(?i)(hue|vs|luminance|color|density|sculpting)` | `[236]` | `hue-vs-luminance-color-density-sculpting.md` | Darkening blue skies or lifting skin luminance via hue band |
| `(?i)(luma|vs|saturation|clean|blacks|and|whites|curve)` | `[237]` | `luma-vs-saturation-clean-blacks-and-whites-curve.md` | Rolling off saturation to 0.0 at 0 IRE and 100 IRE for filmic purity |
| `(?i)(sat|vs|sat|high|saturation|compression|curve)` | `[238]` | `sat-vs-sat-high-saturation-compression-curve.md` | Taming only the most extreme 20% of saturated pixels |
| `(?i)(hsl|qualifier|hue|center|width|and|symmetry|math)` | `[239]` | `hsl-qualifier-hue-center-width-and-symmetry-math.md` | Calculating exact degree center, width, and feather to avoid chatter |
| `(?i)(hsl|qualifier|saturation|and|luminance|bound|gates)` | `[240]` | `hsl-qualifier-saturation-and-luminance-bound-gates.md` | Isolating skin from warm wood walls using Sat/Lum low-high softness |
| `(?i)(qualifier|matte|finesse|clean|black|white|blur|math)` | `[241]` | `qualifier-matte-finesse-clean-black-white-blur-math.md` | Eradicating 4:2:0/4:2:2 blocky chroma key artifacts via matte blur |
| `(?i)(color|warper|spiderweb|grid|pin|and|drag|vectors)` | `[242]` | `color-warper-spiderweb-grid-pin-and-drag-vectors.md` | Simultaneous Hue-Saturation vector warping with adjacent pin locking |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[231]`.
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

