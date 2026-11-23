---
file_id: "[443]"
skill_path: "07-finishing-mastering-and-automated-qc/automated-quality-control-qc-gates/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Final Automated QC Inspection & Gate Sign-Off"
parent_router: "[410]"
child_nodes:
  - "[444]"
  - "[445]"
  - "[446]"
  - "[447]"
  - "[448]"
  - "[449]"
  - "[450]"
  - "[451]"
  - "[452]"
  - "[453]"
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

# [443] Sub-Router: Final Automated QC Inspection & Gate Sign-Off

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `07-finishing-mastering-and-automated-qc/automated-quality-control-qc-gates`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(qc|gate|01|harding|fpa|pse|photosensitive|epilepsy)` | `[444]` | `qc-gate-01-harding-fpa-pse-photosensitive-epilepsy.md` | Auditing luminance/red flashes (>3 flashes/sec above candela delta) |
| `(?i)(qc|gate|02|broadcast|legal|gamut|and|ire|excursion)` | `[445]` | `qc-gate-02-broadcast-legal-gamut-and-ire-excursion.md` | Checking 0–100 IRE luma and 16–235 / 64–940 code value compliance |
| `(?i)(qc|gate|03|unintended|black|frame|and|flash|frame)` | `[446]` | `qc-gate-03-unintended-black-frame-and-flash-frame.md` | Scanning for 1–3 frame single-frame edit gaps or orphan tail frames |
| `(?i)(qc|gate|04|freeze|frame|and|dropped|render|frame)` | `[447]` | `qc-gate-04-freeze-frame-and-dropped-render-frame.md` | Detecting accidental duplicate frames or GPU render glitches |
| `(?i)(qc|gate|05|audio|clipping|dropout|and|dc|offset)` | `[448]` | `qc-gate-05-audio-clipping-dropout-and-dc-offset.md` | Auditing for digital overs, sudden 1-frame mute drops, and DC bias |
| `(?i)(qc|gate|06|lip|sync|drift|millisecond|correlation)` | `[449]` | `qc-gate-06-lip-sync-drift-millisecond-correlation.md` | Verifying audio-visual sync stays within -15ms lead to +45ms lag |
| `(?i)(qc|gate|07|clipped|dialogue|words|at|edit|boundaries)` | `[450]` | `qc-gate-07-clipped-dialogue-words-at-edit-boundaries.md` | Auditing every cut point to ensure zero first/last phoneme truncation |
| `(?i)(qc|gate|08|subtitle|sync|cps|cpl|and|safe|area|gate)` | `[451]` | `qc-gate-08-subtitle-sync-cps-cpl-and-safe-area-gate.md` | Final gate pass on all timed-text streams against visual lower-thirds |
| `(?i)(qc|gate|09|file|naming|container|and|checksum|gate)` | `[452]` | `qc-gate-09-file-naming-container-and-checksum-gate.md` | Validating final deliverable filename regex and sidecar hash integrity |
| `(?i)(delivery|finishing|spec|sheet|markdown|serializer)` | `[453]` | `delivery-finishing-spec-sheet-markdown-serializer.md` | Compiling complete File E Delivery / Finishing Spec Sheet artifact |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[443]`.
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

