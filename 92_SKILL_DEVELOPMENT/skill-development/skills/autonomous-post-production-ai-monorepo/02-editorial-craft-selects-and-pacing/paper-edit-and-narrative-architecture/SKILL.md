---
file_id: "[115]"
skill_path: "02-editorial-craft-selects-and-pacing/paper-edit-and-narrative-architecture/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Paper Edit Construction & Story Architecture"
parent_router: "[101]"
child_nodes:
  - "[116]"
  - "[117]"
  - "[118]"
  - "[119]"
  - "[120]"
  - "[121]"
  - "[122]"
  - "[123]"
  - "[124]"
  - "[125]"
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

# [115] Sub-Router: Paper Edit Construction & Story Architecture

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `02-editorial-craft-selects-and-pacing/paper-edit-and-narrative-architecture`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(paper|edit|a|roll|spine|assembly)` | `[116]` | `paper-edit-a-roll-spine-assembly.md` | Sequencing primary dialogue bites into a self-standing radio edit |
| `(?i)(paper|edit|three|act|dramatic|structure|mapper)` | `[117]` | `paper-edit-three-act-dramatic-structure-mapper.md` | Mapping Inciting Incident, Midpoint, Climax & Resolution beats |
| `(?i)(paper|edit|documentary|thematic|weaving)` | `[118]` | `paper-edit-documentary-thematic-weaving.md` | Intercutting interviews, verite scenes, and archival evidence |
| `(?i)(paper|edit|commercial|hook|retain|payoff|arc)` | `[119]` | `paper-edit-commercial-hook-retain-payoff-arc.md` | Structuring 15s/30s/60s spots with 3-second thumb-stop hooks |
| `(?i)(paper|edit|short|form|retention|curve|optimizer)` | `[120]` | `paper-edit-short-form-retention-curve-optimizer.md` | Engineering pattern interrupts every 4–7 seconds for vertical video |
| `(?i)(paper|edit|corporate|and|educational|clarity|arc)` | `[121]` | `paper-edit-corporate-and-educational-clarity-arc.md` | Problem -> Agitation -> Solution -> Proof -> Call-to-Action mapping |
| `(?i)(paper|edit|b|roll|visual|counterpoint|pairing)` | `[122]` | `paper-edit-b-roll-visual-counterpoint-pairing.md` | Pairing literal vs metaphorical visuals against spoken transcript |
| `(?i)(paper|edit|scene|objective|and|conflict|auditor)` | `[123]` | `paper-edit-scene-objective-and-conflict-auditor.md` | Verifying every scene advances plot or reveals character—else cut |
| `(?i)(paper|edit|exposition|trimming|and|late|entry)` | `[124]` | `paper-edit-exposition-trimming-and-late-entry.md` | Applying "Enter Late, Leave Early" heuristic to scene boundaries |
| `(?i)(paper|edit|to|assembly|edl|compiler)` | `[125]` | `paper-edit-to-assembly-edl-compiler.md` | Translating approved Paper Edit markdown directly into Assembly EDL |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[115]`.
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

