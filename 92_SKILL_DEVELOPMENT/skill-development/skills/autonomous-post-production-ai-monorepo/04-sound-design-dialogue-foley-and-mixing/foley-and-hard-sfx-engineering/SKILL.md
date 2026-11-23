---
file_id: "[285]"
skill_path: "04-sound-design-dialogue-foley-and-mixing/foley-and-hard-sfx-engineering/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Foley Spotting, Surface Taxonomy & Hard Effects"
parent_router: "[267]"
child_nodes:
  - "[286]"
  - "[287]"
  - "[288]"
  - "[289]"
  - "[290]"
  - "[291]"
  - "[292]"
  - "[293]"
  - "[294]"
  - "[295]"
  - "[296]"
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

# [285] Sub-Router: Foley Spotting, Surface Taxonomy & Hard Effects

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `04-sound-design-dialogue-foley-and-mixing/foley-and-hard-sfx-engineering`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(foley|footsteps|surface|and|footwear|taxonomy)` | `[286]` | `foley-footsteps-surface-and-footwear-taxonomy.md` | Matching heel-toe weight to shoe type (boot/sneaker/heel) and floor |
| `(?i)(foley|cloth|and|movement|continuous|pass|design)` | `[287]` | `foley-cloth-and-movement-continuous-pass-design.md` | Layering subtle fabric rustle to anchor characters in physical space |
| `(?i)(foley|prop|handling|and|tactile|micro|sync)` | `[288]` | `foley-prop-handling-and-tactile-micro-sync.md` | Frame-accurate sync for cup set-downs, key jingles, paper turns, phones |
| `(?i)(hard|sfx|door|vehicle|and|mechanical|layering)` | `[289]` | `hard-sfx-door-vehicle-and-mechanical-layering.md` | Multi-layering latch + creak + thud + air displacement for realism |
| `(?i)(combat|and|impact|transient|body|sweetener|stack)` | `[290]` | `combat-and-impact-transient-body-sweetener-stack.md` | Combining high snap + mid meat thud + sub-bass weight for impacts |
| `(?i)(weapons|and|ballistics|mech|blast|tail|design)` | `[291]` | `weapons-and-ballistics-mech-blast-tail-design.md` | Layering mechanical action, muzzle transient, and environmental tail |
| `(?i)(cinematic|whooshes|swells|and|transition|sfx)` | `[292]` | `cinematic-whooshes-swells-and-transition-sfx.md` | Syncing frequency-swept whooshes to camera whip pans and graphics |
| `(?i)(UI|hud|and|digital|screen|telemetry|beeps)` | `[293]` | `UI-hud-and-digital-screen-telemetry-beeps.md` | Designing non-fatiguing mid-high frequency tech interface cues |
| `(?i)(lfe|sub|bass|boom|and|low|end|management)` | `[294]` | `lfe-sub-bass-boom-and-low-end-management.md` | Filtering LFE effects below 80–120 Hz without muddying main channels |
| `(?i)(doppler|shift|and|pass|by|panning|automation)` | `[295]` | `doppler-shift-and-pass-by-panning-automation.md` | Calculating pitch drop and L-C-R pan velocity for passing vehicles |
| `(?i)(perspective|filtering|off|screen|and|next|room|sfx)` | `[296]` | `perspective-filtering-off-screen-and-next-room-sfx.md` | Low-pass filtering + early reflection boost for occluded sound sources |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[285]`.
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

