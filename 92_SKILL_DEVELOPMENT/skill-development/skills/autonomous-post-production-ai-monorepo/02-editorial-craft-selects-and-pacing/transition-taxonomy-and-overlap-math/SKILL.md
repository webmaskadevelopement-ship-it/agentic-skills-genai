---
file_id: "[145]"
skill_path: "02-editorial-craft-selects-and-pacing/transition-taxonomy-and-overlap-math/SKILL.md"
role: "Sub-Skill Router: Sub-Router: J-Cuts, L-Cuts, Match Cuts & Dissolve Mechanics"
parent_router: "[101]"
child_nodes:
  - "[146]"
  - "[147]"
  - "[148]"
  - "[149]"
  - "[150]"
  - "[151]"
  - "[152]"
  - "[153]"
  - "[154]"
  - "[155]"
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

# [145] Sub-Router: J-Cuts, L-Cuts, Match Cuts & Dissolve Mechanics

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `02-editorial-craft-selects-and-pacing/transition-taxonomy-and-overlap-math`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(j|cut|audio|lead|in|frame|offset|calculator)` | `[146]` | `j-cut-audio-lead-in-frame-offset-calculator.md` | Pre-lapping incoming dialogue 12–48 frames under outgoing reaction |
| `(?i)(l|cut|audio|trail|out|frame|offset|calculator)` | `[147]` | `l-cut-audio-trail-out-frame-offset-calculator.md` | Extending outgoing audio under incoming visual coverage or cutaways |
| `(?i)(graphic|match|cut|shape|and|composition|aligner)` | `[148]` | `graphic-match-cut-shape-and-composition-aligner.md` | Matching silhouette, horizon line, or geometric form across scenes |
| `(?i)(motion|vector|match|cut|velocity|aligner)` | `[149]` | `motion-vector-match-cut-velocity-aligner.md` | Matching pan/tilt/zoom direction and angular speed across cuts |
| `(?i)(audio|bridge|and|sound|match|cut|designer)` | `[150]` | `audio-bridge-and-sound-match-cut-designer.md` | Linking disparate scenes via shared acoustic transient (e.g. kettle->train) |
| `(?i)(smash|cut|contrast|maximizer)` | `[151]` | `smash-cut-contrast-maximizer.md` | Maximizing tonal, acoustic, and visual contrast for shock transitions |
| `(?i)(invisible|whip|pan|and|wipe|by|stitcher)` | `[152]` | `invisible-whip-pan-and-wipe-by-stitcher.md` | Hiding cuts inside motion-blurred foreground objects or whip pans |
| `(?i)(intentional|jump|cut|stylistic|cadence|controller)` | `[153]` | `intentional-jump-cut-stylistic-cadence-controller.md` | Governing rhythmic jump cuts for time-compression or anxiety |
| `(?i)(cross|dissolve|duration|and|handle|validator)` | `[154]` | `cross-dissolve-duration-and-handle-validator.md` | Verifying sufficient source handles exist for 12/24/48-frame dissolves |
| `(?i)(dip|to|black|and|fade|from|black|chapter|pacing)` | `[155]` | `dip-to-black-and-fade-from-black-chapter-pacing.md` | Calculating black-hold frames between major narrative acts |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[145]`.
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

