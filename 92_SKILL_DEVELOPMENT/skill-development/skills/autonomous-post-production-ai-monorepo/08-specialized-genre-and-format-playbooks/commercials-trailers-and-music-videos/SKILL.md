---
file_id: "[467]"
skill_path: "08-specialized-genre-and-format-playbooks/commercials-trailers-and-music-videos/SKILL.md"
role: "Sub-Skill Router: Sub-Router: High-Impact Short-Form, Trailers & Music Videos"
parent_router: "[454]"
child_nodes:
  - "[468]"
  - "[469]"
  - "[470]"
  - "[471]"
  - "[472]"
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

# [467] Sub-Router: High-Impact Short-Form, Trailers & Music Videos

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `08-specialized-genre-and-format-playbooks/commercials-trailers-and-music-videos`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(movie|trailer|three|act|cold|open|build|climax|spec)` | `[468]` | `movie-trailer-three-act-cold-open-build-climax-spec.md` | Structuring Act 1 World, Act 2 Turn, Act 3 Montage + Stinger Button |
| `(?i)(trailer|braam|riser|and|sub|drop|punctuation|grid)` | `[469]` | `trailer-braam-riser-and-sub-drop-punctuation-grid.md` | Placing acoustic blackout stops and signature percussion hits |
| `(?i)(automotive|and|luxury|commercial|specular|sculpting)` | `[470]` | `automotive-and-luxury-commercial-specular-sculpting.md` | Power-window car paint rolling highlights and engine exhaust tuning |
| `(?i)(food|and|beverage|tabletop|macro|color|and|sizzle)` | `[471]` | `food-and-beverage-tabletop-macro-color-and-sizzle.md` | Enhancing warm appetite hues, water droplets, and hyper-crisp foley |
| `(?i)(music|video|lip|sync|multicam|and|performance|energy)` | `[472]` | `music-video-lip-sync-multicam-and-performance-energy.md` | Syncing 24/30/48/60fps playback takes to master studio audio track |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[467]`.
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

