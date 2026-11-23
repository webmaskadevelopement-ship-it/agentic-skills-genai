---
file_id: "[325]"
skill_path: "04-sound-design-dialogue-foley-and-mixing/loudness-compliance-and-master-limiting/SKILL.md"
role: "Sub-Skill Router: Sub-Router: ITU-R BS.1770-4 Loudness & True Peak Mastering"
parent_router: "[267]"
child_nodes:
  - "[326]"
  - "[327]"
  - "[328]"
  - "[329]"
  - "[330]"
  - "[331]"
  - "[332]"
  - "[333]"
  - "[334]"
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

# [325] Sub-Router: ITU-R BS.1770-4 Loudness & True Peak Mastering

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `04-sound-design-dialogue-foley-and-mixing/loudness-compliance-and-master-limiting`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(ebu|r128|european|broadcast|23|lufs|compliance)` | `[326]` | `ebu-r128-european-broadcast-23-lufs-compliance.md` | Integrated -23.0 LUFS (±0.5 LU), Max -1.0 dBTP, Short-term <= -18 LUFS |
| `(?i)(atsc|a85|us|broadcast|24|lkfs|compliance)` | `[327]` | `atsc-a85-us-broadcast-24-lkfs-compliance.md` | Integrated -24.0 LKFS (±1.0 LU), Max -2.0 dBTP, anchor dialogue intelligence |
| `(?i)(netflix|streaming|27|lkfs|dialog|gated|spec)` | `[328]` | `netflix-streaming-27-lkfs-dialog-gated-spec.md` | Dolby Dialog-Gated -27.0 LKFS (±1.0 LU) and -2.0 dBTP ceiling |
| `(?i)(youtube|tiktok|social|14|lufs|high|impact|spec)` | `[329]` | `youtube-tiktok-social-14-lufs-high-impact-spec.md` | Integrated -14.0 LUFS, -1.0 dBTP, tight LRA (4–7 LU) for mobile speakers |
| `(?i)(podcast|and|mobile|voice|16|lufs|spec)` | `[330]` | `podcast-and-mobile-voice-16-lufs-spec.md` | Apple/Spotify podcast -16.0 LUFS stereo / -19.0 LUFS mono spec |
| `(?i)(theatrical|85|dbc|pink|noise|reference|calibration)` | `[331]` | `theatrical-85-dbc-pink-noise-reference-calibration.md` | Mixing in uncompressed room-calibrated SPL reference environment |
| `(?i)(loudness|range|lra|dynamic|envelope|controller)` | `[332]` | `loudness-range-lra-dynamic-envelope-controller.md` | Controlling macro dynamics between whisper and explosion (LRA 6–15 LU) |
| `(?i)(inter|sample|true|peak|brickwall|limiter|math)` | `[333]` | `inter-sample-true-peak-brickwall-limiter-math.md` | 4x/8x oversampled lookahead limiting to prevent DAC reconstruction clipping |
| `(?i)(sound|mix|spec|json|and|stem|manifest|serializer)` | `[334]` | `sound-mix-spec-json-and-stem-manifest-serializer.md` | Compiling complete File D Sound Design & Mix Spec artifact |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[325]`.
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

