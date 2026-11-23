---
file_id: "[102]"
skill_path: "02-editorial-craft-selects-and-pacing/selects-and-take-evaluation-engine/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Algorithmic & Craft-Based Take Selection"
parent_router: "[101]"
child_nodes:
  - "[103]"
  - "[104]"
  - "[105]"
  - "[106]"
  - "[107]"
  - "[108]"
  - "[109]"
  - "[110]"
  - "[111]"
  - "[112]"
  - "[113]"
  - "[114]"
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

# [102] Sub-Router: Algorithmic & Craft-Based Take Selection

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `02-editorial-craft-selects-and-pacing/selects-and-take-evaluation-engine`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(selects|heuristic|fewest|filler|words)` | `[103]` | `selects-heuristic-fewest-filler-words.md` | Scoring and penalizing takes by disfluency ratio per 100 words |
| `(?i)(selects|heuristic|later|take|warm|up|preference)` | `[104]` | `selects-heuristic-later-take-warm-up-preference.md` | Weighting later takes higher as speaker performance settles |
| `(?i)(selects|heuristic|mid|sentence|dead|pause|filter)` | `[105]` | `selects-heuristic-mid-sentence-dead-pause-filter.md` | Disqualifying takes with unmotivated pauses > 2000ms mid-clause |
| `(?i)(selects|heuristic|silent|gap|opener|trimmer)` | `[106]` | `selects-heuristic-silent-gap-opener-trimmer.md` | Locating exact zero-crossing before first phoneme to avoid word-clip |
| `(?i)(selects|heuristic|incomplete|line|and|false|start)` | `[107]` | `selects-heuristic-incomplete-line-and-false-start.md` | Detecting abandoned clauses and stitching clean pickups |
| `(?i)(selects|heuristic|emotional|authenticity|scoring)` | `[108]` | `selects-heuristic-emotional-authenticity-scoring.md` | Evaluating vocal tremor, eye engagement, and subtext delivery |
| `(?i)(selects|heuristic|pacing|and|wpm|consistency)` | `[109]` | `selects-heuristic-pacing-and-wpm-consistency.md` | Matching delivery cadence between adjacent takes so cuts feel native |
| `(?i)(selects|heuristic|technical|disqualification|gate)` | `[110]` | `selects-heuristic-technical-disqualification-gate.md` | Rejecting takes with clothing rustle on lav, boom dip, or soft focus |
| `(?i)(selects|frankenbite|and|syllable|stitch|constructor)` | `[111]` | `selects-frankenbite-and-syllable-stitch-constructor.md` | Constructing seamless composite dialogue from multiple takes |
| `(?i)(selects|reaction|shot|harvesting|protocol)` | `[112]` | `selects-reaction-shot-harvesting-protocol.md` | Extracting non-verbal nods, listens, and micro-reactions from tails |
| `(?i)(selects|b|roll|hero|moment|isolation)` | `[113]` | `selects-b-roll-hero-moment-isolation.md` | Isolating peak-action windows with clean entry/exit camera motion |
| `(?i)(selects|rationale|documentation|generator)` | `[114]` | `selects-rationale-documentation-generator.md` | Writing mandatory `selection_rationale` and `disqualification_notes` |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[102]`.
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

