---
file_id: "[051]"
skill_path: "01-ingest-dailies-and-assistant-editing/timecode-and-multi-cam-sync/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Timecode Math, Frame Rate Conversion & Sync"
parent_router: "[031]"
child_nodes:
  - "[052]"
  - "[053]"
  - "[054]"
  - "[055]"
  - "[056]"
  - "[057]"
  - "[058]"
  - "[059]"
  - "[060]"
  - "[061]"
  - "[062]"
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

# [051] Sub-Router: Timecode Math, Frame Rate Conversion & Sync

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `01-ingest-dailies-and-assistant-editing/timecode-and-multi-cam-sync`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(smpte|12m|ltc|linear|timecode|decoder)` | `[052]` | `smpte-12m-ltc-linear-timecode-decoder.md` | Decoding audio-channel LTC into frame-accurate metadata TC |
| `(?i)(vitc|and|ancillary|timecode|extractor)` | `[053]` | `vitc-and-ancillary-timecode-extractor.md` | Extracting RP-188 / VITC from SDI/MXF data streams |
| `(?i)(drop|frame|vs|non|drop|frame|reconciler)` | `[054]` | `drop-frame-vs-non-drop-frame-reconciler.md` | Reconciling 29.97/59.94 DF (;00;02 skip rules) vs NDF (:00) |
| `(?i)(pulldown|2|3|and|3|2|cadence|removal)` | `[055]` | `pulldown-2-3-and-3-2-cadence-removal.md` | Inverse telecine (IVTC) from 29.97i back to true 23.976p |
| `(?i)(frame|rate|conform|23976|to|24000|math)` | `[056]` | `frame-rate-conform-23976-to-24000-math.md` | 0.1% pull-up/pull-down speed & audio pitch compensation |
| `(?i)(pal|25fps|to|ntsc|23976|2997|standards|conversion)` | `[057]` | `pal-25fps-to-ntsc-23976-2997-standards-conversion.md` | 4% speed change vs optical flow motion-compensated conversion |
| `(?i)(audio|waveform|cross|correlation|sync)` | `[058]` | `audio-waveform-cross-correlation-sync.md` | Sub-frame FFT phase correlation for scratch-to-boom syncing |
| `(?i)(optical|slate|clapstick|closure|detector)` | `[059]` | `optical-slate-clapstick-closure-detector.md` | Visual frame detection of physical clapperboard impact |
| `(?i)(smart|slate|digislate|ocr|timecode|reader)` | `[060]` | `smart-slate-digislate-ocr-timecode-reader.md` | Reading LED timecode digits off smart slates when jam fails |
| `(?i)(clock|drift|and|sample|rate|mismatch|corrector)` | `[061]` | `clock-drift-and-sample-rate-mismatch-corrector.md` | Fixing 48.000 kHz vs 48.048 kHz drift over long takes |
| `(?i)(multicam|group|clip|angle|synchronizer)` | `[062]` | `multicam-group-clip-angle-synchronizer.md` | Building N-angle synchronized multicam banks by time-of-day TC |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[051]`.
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

