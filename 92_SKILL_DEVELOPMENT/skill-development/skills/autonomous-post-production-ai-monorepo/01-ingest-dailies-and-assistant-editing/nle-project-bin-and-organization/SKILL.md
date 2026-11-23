---
file_id: "[091]"
skill_path: "01-ingest-dailies-and-assistant-editing/nle-project-bin-and-organization/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Bin Architecture, Stringouts & Kem Rolls"
parent_router: "[031]"
child_nodes:
  - "[092]"
  - "[093]"
  - "[094]"
  - "[095]"
  - "[096]"
  - "[097]"
  - "[098]"
  - "[099]"
  - "[100]"
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

# [091] Sub-Router: Bin Architecture, Stringouts & Kem Rolls

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `01-ingest-dailies-and-assistant-editing/nle-project-bin-and-organization`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(standardized|bin|hierarchy|generator)` | `[092]` | `standardized-bin-hierarchy-generator.md` | Building 01_SEQ, 02_FOOTAGE, 03_AUDIO, 04_GFX, 05_VFX, 06_OUT |
| `(?i)(kem|roll|and|scene|stringout|builder)` | `[093]` | `kem-roll-and-scene-stringout-builder.md` | Assembling chronological camera rolls with 2-second black spacers |
| `(?i)(line|by|line|multi|take|lineup|sequence|builder)` | `[094]` | `line-by-line-multi-take-lineup-sequence-builder.md` | Concatenating all takes of Line A consecutively for rapid comparison |
| `(?i)(marker|color|coding|taxonomy)` | `[095]` | `marker-color-coding-taxonomy.md` | Assigning Red/Green/Blue/Yellow/Cyan NLE markers by meaning |
| `(?i)(subclip|naming|Scene|Shot|Take|Angle|spec)` | `[096]` | `subclip-naming-Scene-Shot-Take-Angle-spec.md` | Enforcing `14A-03_B` standard naming across all NLE items |
| `(?i)(audio|track|layout|assignment|matrix)` | `[097]` | `audio-track-layout-assignment-matrix.md` | A1-A2 Boom, A3-A8 Lavs, A9-A12 SFX, A13-A16 Ambience, A17-A20 MX |
| `(?i)(video|track|layering|convention)` | `[098]` | `video-track-layering-convention.md` | V1 Primary Storyline, V2 B-Roll, V3 PIP/VFX, V4 Titles, V5 Burn-ins |
| `(?i)(archival|unused|media|pruning|analyzer)` | `[099]` | `archival-unused-media-pruning-analyzer.md` | Identifying zero-reference media vs safety coverage |
| `(?i)(ingest|to|editorial|turnover|gate|validator)` | `[100]` | `ingest-to-editorial-turnover-gate-validator.md` | Gate 01 Validator: Ensuring 100% sync, metadata & transcript parity |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[091]`.
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

