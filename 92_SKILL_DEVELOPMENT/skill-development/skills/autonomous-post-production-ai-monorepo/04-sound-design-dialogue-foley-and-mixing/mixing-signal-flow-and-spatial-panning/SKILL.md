---
file_id: "[315]"
skill_path: "04-sound-design-dialogue-foley-and-mixing/mixing-signal-flow-and-spatial-panning/SKILL.md"
role: "Sub-Skill Router: Sub-Router: EQ, Dynamics, Bus Architecture & Spatial Formats"
parent_router: "[267]"
child_nodes:
  - "[316]"
  - "[317]"
  - "[318]"
  - "[319]"
  - "[320]"
  - "[321]"
  - "[322]"
  - "[323]"
  - "[324]"
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

# [315] Sub-Router: EQ, Dynamics, Bus Architecture & Spatial Formats

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `04-sound-design-dialogue-foley-and-mixing/mixing-signal-flow-and-spatial-panning`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(dialogue|eq|high|pass|mud|cut|and|presence|boost)` | `[316]` | `dialogue-eq-high-pass-mud-cut-and-presence-boost.md` | 80 Hz HPF, 250 Hz box cut, 3 kHz intelligibility, 6 kHz de-ess |
| `(?i)(dialogue|serial|compression|fast|peak|plus|leveler)` | `[317]` | `dialogue-serial-compression-fast-peak-plus-leveler.md` | 1176-style fast peak catch (4:1) into LA-2A/Fairchild smooth leveling |
| `(?i)(center|channel|dialogue|anchor|and|divergence)` | `[318]` | `center-channel-dialogue-anchor-and-divergence.md` | Locking dialogue 100% Center in 5.1/7.1/Atmos for theater seating |
| `(?i)(stereo|2|0|lo|ro|and|lt|rt|downmix|compatibility)` | `[319]` | `stereo-2-0-lo-ro-and-lt-rt-downmix-compatibility.md` | Checking phase correlation (+1.0 to 0.0) to prevent mono sum cancellation |
| `(?i)(surround|5|1|and|7|1|channel|routing|l|r|c|lfe|ls|rs)` | `[320]` | `surround-5-1-and-7-1-channel-routing-l-r-c-lfe-ls-rs.md` | SMPTE channel order validation and surround decorrelation |
| `(?i)(dolby|atmos|7|1|2|bed|and|dynamic|object|metadata)` | `[321]` | `dolby-atmos-7-1-2-bed-and-dynamic-object-metadata.md` | Assigning 3D X/Y/Z coordinates and size metadata for Atmos renderer |
| `(?i)(binaural|headphone|spatial|rendering|validation)` | `[322]` | `binaural-headphone-spatial-rendering-validation.md` | Verifying HRTF binaural fold-down for mobile and streaming listeners |
| `(?i)(dme|stem|architecture|dialogue|music|effects|split)` | `[323]` | `dme-stem-architecture-dialogue-music-effects-split.md` | Ensuring DX + MX + FX stems sum mathematically identically to Full Mix |
| `(?i)(international|m|and|e|music|and|effects|validation)` | `[324]` | `international-m-and-e-music-and-effects-validation.md` | Auditing 100% foley/cloth coverage in M&E stem for foreign dubbing |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[315]`.
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

