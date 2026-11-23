---
file_id: "[349]"
skill_path: "05-subtitling-captioning-and-localization/linguistic-segmentation-and-line-treatment/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Syntactic Line Breaking, Condensation & Punctuation"
parent_router: "[335]"
child_nodes:
  - "[350]"
  - "[351]"
  - "[352]"
  - "[353]"
  - "[354]"
  - "[355]"
  - "[356]"
  - "[357]"
  - "[358]"
  - "[359]"
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

# [349] Sub-Router: Syntactic Line Breaking, Condensation & Punctuation

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `05-subtitling-captioning-and-localization/linguistic-segmentation-and-line-treatment`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(syntactic|clause|boundary|line|break|rules)` | `[350]` | `syntactic-clause-boundary-line-break-rules.md` | Breaking at punctuation, conjunctions, or prepositional boundaries |
| `(?i)(forbidden|linguistic|splits|article|noun|verb)` | `[351]` | `forbidden-linguistic-splits-article-noun-verb.md` | Never splitting article+noun, pronoun+verb, auxiliary+verb, or names |
| `(?i)(bottom|heavy|pyramid|vs|balanced|line|geometry)` | `[352]` | `bottom-heavy-pyramid-vs-balanced-line-geometry.md` | Minimizing ocular travel by balancing line lengths or pyramid weighting |
| `(?i)(text|condensation|and|paraphrasing|for|cps|rescue)` | `[353]` | `text-condensation-and-paraphrasing-for-cps-rescue.md` | Reducing word count by 20–35% while preserving 100% plot/tone intent |
| `(?i)(dual|speaker|dialogue|hyphen|and|line|separation)` | `[354]` | `dual-speaker-dialogue-hyphen-and-line-separation.md` | Assigning `- Speaker 1` on Line 1 and `- Speaker 2` on Line 2 |
| `(?i)(continuation|ellipses|vs|unpunctuated|flow|rules)` | `[355]` | `continuation-ellipses-vs-unpunctuated-flow-rules.md` | Applying modern Netflix no-ellipsis rule vs legacy broadcast `...` |
| `(?i)(interrupted|speech|double|hyphen|vs|em|dash|spec)` | `[356]` | `interrupted-speech-double-hyphen-vs-em-dash-spec.md` | Formatting abrupt mid-word or mid-sentence interruptions accurately |
| `(?i)(italics|protocol|offscreen|electronic|and|foreign)` | `[357]` | `italics-protocol-offscreen-electronic-and-foreign.md` | Applying `<i>` for voices through phones/radios, thoughts, and songs |
| `(?i)(numbers|digits|vs|spelled|out|one|to|ten|rules)` | `[358]` | `numbers-digits-vs-spelled-out-one-to-ten-rules.md` | Spelling out one through ten; using numerals for 11+ and units |
| `(?i)(bidirectional|rtl|arabic|hebrew|unicode|control)` | `[359]` | `bidirectional-rtl-arabic-hebrew-unicode-control.md` | Injecting LRM/RLM Unicode markers (`U+200E`/`U+200F`) to fix punctuation flip |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[349]`.
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

