---
file_id: "[360]"
skill_path: "05-subtitling-captioning-and-localization/sdh-closed-captions-and-forced-narratives/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Deaf/Hard-of-Hearing, Forced Narratives & Positioning"
parent_router: "[335]"
child_nodes:
  - "[361]"
  - "[362]"
  - "[363]"
  - "[364]"
  - "[365]"
  - "[366]"
  - "[367]"
  - "[368]"
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

# [360] Sub-Router: Deaf/Hard-of-Hearing, Forced Narratives & Positioning

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `05-subtitling-captioning-and-localization/sdh-closed-captions-and-forced-narratives`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(sdh|speaker|identification|brackets|and|placement)` | `[361]` | `sdh-speaker-identification-brackets-and-placement.md` | Formatting `[SARAH]` or `(Sarah)` when speaker is off-screen or ambiguous |
| `(?i)(sdh|non|verbal|sound|effect|description|taxonomy)` | `[362]` | `sdh-non-verbal-sound-effect-description-taxonomy.md` | Present-tense lower-case descriptive tags: `[heavy footsteps approaching]` |
| `(?i)(sdh|music|mood|genre|and|lyric|formatting)` | `[363]` | `sdh-music-mood-genre-and-lyric-formatting.md` | Formatting `[somber cello music playing]` and `♪ lyric lines ♪` |
| `(?i)(sdh|whispered|muttered|and|accent|manner|tags)` | `[364]` | `sdh-whispered-muttered-and-accent-manner-tags.md` | Indicating vocal delivery manner `[whispering]`, `[in French accent]` |
| `(?i)(forced|narrative|fn|on|screen|text|and|signage)` | `[365]` | `forced-narrative-fn-on-screen-text-and-signage.md` | Translating plot-critical signs, texts, and newspapers in ALL CAPS |
| `(?i)(forced|narrative|foreign|dialogue|part|subtitles)` | `[366]` | `forced-narrative-foreign-dialogue-part-subtitles.md` | Generating FN-only stream for foreign lines inside native audio track |
| `(?i)(vertical|positioning|an8|top|screen|collision|avoid)` | `[367]` | `vertical-positioning-an8-top-screen-collision-avoid.md` | Moving cues to top-center (`{\an8}` / `line:10%`) over lower-thirds |
| `(?i)(burn|in|open|caption|font|stroke|and|shadow|spec)` | `[368]` | `burn-in-open-caption-font-stroke-and-shadow-spec.md` | Helvetica/Arial/Inter, 80% black box or 3px outline for mobile readability |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[360]`.
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

