---
file_id: "[436]"
skill_path: "07-finishing-mastering-and-automated-qc/leaders-slates-and-sync-verification/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Bars & Tone, Universal Leaders, 2-Pops & Slates"
parent_router: "[410]"
child_nodes:
  - "[437]"
  - "[438]"
  - "[439]"
  - "[440]"
  - "[441]"
  - "[442]"
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

# [436] Sub-Router: Bars & Tone, Universal Leaders, 2-Pops & Slates

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `07-finishing-mastering-and-automated-qc/leaders-slates-and-sync-verification`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(smpte|rp|219|hd|and|arib|std|b28|uhd|color|bars)` | `[437]` | `smpte-rp-219-hd-and-arib-std-b28-uhd-color-bars.md` | Placing 60s of 75%/100% SMPTE Bars at 00:58:30:00 pre-program |
| `(?i)(reference|tone|1khz|minus|20|dbfs|channel|id|spec)` | `[438]` | `reference-tone-1khz-minus-20-dbfs-channel-id-spec.md` | Generating -20 dBFS (US) or -18 dBFS (EBU) 1 kHz sine with BLITS ID |
| `(?i)(production|information|slate|metadata|layout)` | `[439]` | `production-information-slate-metadata-layout.md` | Formatting Title, Version, Runtime, FPS, Color Space, Audio Config |
| `(?i)(countdown|leader|and|head|2|pop|00|59|58|00|spec)` | `[440]` | `countdown-leader-and-head-2-pop-00-59-58-00-spec.md` | Placing exact 1-frame white circle + 1 kHz beep 2.00 seconds before FFOA |
| `(?i)(first|frame|of|action|ffoa|01|00|00|00|lock|check)` | `[441]` | `first-frame-of-action-ffoa-01-00-00-00-lock-check.md` | Enforcing exact program start at Hour 01:00:00:00 (or 00:00:00:00 IMF) |
| `(?i)(tail|2|pop|and|post|roll|black|pad|specification)` | `[442]` | `tail-2-pop-and-post-roll-black-pad-specification.md` | Placing 1-frame tail pop 2.00 seconds after LFOA + 10s silent black |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[436]`.
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

