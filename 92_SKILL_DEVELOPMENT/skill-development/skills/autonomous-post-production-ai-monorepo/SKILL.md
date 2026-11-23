---
file_id: "[001]"
skill_path: "SKILL.md"
role: "Master Root Router, Intent Classifier & Global Contract"
parent_router: "NONE"
child_nodes:
  - "[031]" # Dept 01: Ingest, Dailies & Assistant Editing
  - "[101]" # Dept 02: Editorial Craft, Selects & Pacing
  - "[177]" # Dept 03: Color Grading & Look Development
  - "[267]" # Dept 04: Sound Design, Dialogue, Foley & Mixing
  - "[335]" # Dept 05: Subtitling, Captioning & Localization
  - "[378]" # Dept 06: VFX, Motion Graphics, Cleanup & Conforming
  - "[410]" # Dept 07: Finishing, Mastering & Automated QC
  - "[454]" # Dept 08: Specialized Genre & Format Playbooks
  - "[479]" # Registry 09: Skill Master Commands ([480]–[529])
  - "[530]" # Tables 10: Fine-Grained Parameter Reference Tables ([531]–[565])
  - "[566]" # Validators 11: Deterministic Validation & Calculation Specs ([567]–[592])
  - "[593]" # Adapters 12: NLE & DAW Automation Bridge Adapters ([594]–[610])
  - "[611]" # Exemplars 13: Production-Grade Golden Examples ([612]–[633])
  - "[634]" # Edge Cases 14: Anomaly Remediation & Recovery ([635]–[680])
  - "[681]" # Meta 15: System Orchestration & Meta-Skills ([682]–[720])
schema_locks:
  - "[014]" # Ingest Manifest
  - "[015]" # Word-Level Transcript
  - "[016]" # Paper Edit Blueprint
  - "[017]" # EDL Cut Manifest (File A)
  - "[018]" # Rhythm & Pacing Map
  - "[019]" # Color Grade Specification (File B)
  - "[020]" # Shot-Match Delta Matrix
  - "[021]" # Subtitle Timed-Text Cue
  - "[022]" # Subtitle Compliance Audit (File C)
  - "[023]" # Dialogue Edit Decision List
  - "[024]" # Sound Design & Foley Cue
  - "[025]" # Mix & Loudness Specification (File D)
  - "[026]" # VFX Turnover & Pull Sheet
  - "[027]" # Online Conform Relink Map
  - "[028]" # Delivery & Mastering Spec (File E)
  - "[029]" # Automated QC Gate Report
  - "[030]" # IMF & DCP Package Manifest
master_commands:
  - "VERIFY_MEDIA_HASHES"
  - "PARSE_CAMERA_METADATA"
  - "SYNC_MULTICAM_AND_AUDIO"
  - "LOAD_TIMED_TRANSCRIPT"
  - "INDEX_VISUAL_SHOTS"
  - "BUILD_NLE_BIN_STRUCTURE"
  - "EVALUATE_AND_RANK_TAKES"
  - "DISQUALIFY_FLAWED_TAKES"
  - "TRIM_SILENT_OPENERS_AND_TAILS"
  - "GENERATE_PAPER_EDIT"
  - "COMPILE_ASSEMBLY_SEQUENCE"
  - "REFINE_ROUGH_TO_FINE_CUT"
  - "CALCULATE_JL_SPLIT_TRANSITIONS"
  - "VERIFY_MURCH_SIX_PRIORITIES"
  - "PROFILE_RHYTHM_AND_PACING"
  - "VALIDATE_EDL_TIMECODE_MONOTONICITY"
  - "EMIT_EDL_MANIFEST"
  - "LOAD_SHOT_METADATA"
  - "ANALYZE_SCOPES"
  - "BUILD_NODE_GRAPH"
  - "SET_PRIMARY_BALANCE"
  - "APPLY_HSL_QUALIFIER"
  - "SHAPE_TONAL_CURVES"
  - "MATCH_TO_REFERENCE"
  - "APPLY_FILM_LOOK_AND_FX"
  - "VALIDATE_GRADE_LEGAL_RANGE"
  - "EMIT_GRADE_SPEC"
  - "SEGMENT_CUES"
  - "CALCULATE_METRICS"
  - "CONDENSE_HIGH_CPS_TEXT"
  - "SNAP_TO_SHOT_CHANGES"
  - "INJECT_SDH_AND_FN_TAGS"
  - "ENFORCE_STANDARD"
  - "GENERATE_FORMAT"
  - "EMIT_COMPLIANCE_REPORT"
  - "CLEAN_AND_LEVEL_DIALOGUE"
  - "SYNTHESIZE_ROOM_TONE_FILLS"
  - "SPOT_FOLEY_AND_HARD_SFX"
  - "LAYER_AMBIENCE_AND_REVERB"
  - "ALIGN_MUSIC_AND_DUCKING"
  - "CALIBRATE_LUFS_AND_TRUE_PEAK"
  - "VERIFY_DME_STEM_PARITY"
  - "EMIT_MIX_SPEC"
  - "RELINK_AND_CONFORM_RAW"
  - "GENERATE_EXR_PULL_SHEET"
  - "CONFIGURE_MASTER_CODEC"
  - "ASSEMBLE_LEADERS_AND_2POP"
  - "RUN_AUTOMATED_QC_GATES"
  - "PACKAGE_IMF_OR_DCP"
  - "EMIT_DELIVERY_SPEC"
validation_gates:
  - "[567]" # validator-edl-schema-and-required-fields
  - "[568]" # validator-edl-record-timecode-continuity
  - "[569]" # validator-edl-source-in-out-duration-parity
  - "[570]" # validator-edl-transition-handle-sufficiency
  - "[571]" # validator-edl-no-duplicate-adjacent-frames
  - "[572]" # validator-edl-stage-gate-readiness
  - "[573]" # validator-grade-schema-and-scope-evidence
  - "[574]" # validator-grade-lift-gamma-gain-bounds
  - "[575]" # validator-grade-node-graph-topological-order
  - "[576]" # validator-grade-skin-tone-vector-tolerance
  - "[577]" # validator-grade-sdr-hdr-legal-ire-compliance
  - "[578]" # validator-grade-shot-match-delta-convergence
  - "[579]" # validator-subtitle-schema-and-cue-index-order
  - "[580]" # validator-subtitle-cps-and-cpl-hard-ceilings
  - "[581]" # validator-subtitle-duration-floor-and-ceiling
  - "[582]" # validator-subtitle-shot-change-dead-zone-audit
  - "[583]" # validator-subtitle-orphan-words-and-tag-balance
  - "[584]" # validator-subtitle-sdh-and-fn-completeness
  - "[585]" # validator-mix-schema-and-stem-completeness
  - "[586]" # validator-mix-integrated-lufs-and-dbtp-bounds
  - "[587]" # validator-mix-dialogue-room-tone-continuity
  - "[588]" # validator-mix-music-ducking-clearance
  - "[589]" # validator-mix-sfx-timecode-to-edl-sync
  - "[590]" # validator-delivery-spec-cross-artifact-consistency
  - "[591]" # validator-leader-2pop-and-ffoa-frame-exactness
  - "[592]" # validator-master-qc-all-gates-green-signoff
---

# [001] Master Root Router, Intent Classifier & Global Contract

## 1. Operational Boundary & Anti-Execution Rule

This file is the top-level orchestrator and immutable gateway for the entire `autonomous-post-production-ai-monorepo/`.

**ANTI-EXECUTION RULE**:
Under no circumstances may this master router fabricate domain heuristics, approximate frame math, emit unvalidated timecodes, or generate deliverables directly in-weights without disembarking to and executing the exact underlying leaf markdown specifications (`[004]` through `[720]`).
This router parses user intent, enforces global post-production contracts, executes topological stage-gate handoffs, and invokes leaf skills deterministically via `[683] meta-skill-minimal-sub-skill-context-loader.md`.

---

## 2. Intent Classification & Keyword Dispatch Matrix

Every prompt entering the system is evaluated against the following deterministic classification matrix:

| User Intent & Trigger Regex | Primary Dept Router | Required Input Artifacts | Leaf Skills to Load | Bound Master Command | Target Output Schema |
|---|---|---|---|---|---|
| `(?i)(offload\|checksum\|ingest\|camera raw\|dailies\|sync multicam)` | `[031]` Ingest & Dailies | Camera media, checksums, scratch audio | `[033]`, `[041]`–`[047]`, `[052]`–`[062]`, `[064]`–[071] | `VERIFY_MEDIA_HASHES` (`[480]`), `PARSE_CAMERA_METADATA` (`[481]`), `SYNC_MULTICAM_AND_AUDIO` (`[482]`) | `[014]` Ingest Manifest, `[015]` Word Transcript |
| `(?i)(edit\|cut\|selects\|pacing\|assembly\|rough cut\|fine cut\|edl\|murch\|trim)` | `[101]` Editorial Craft | Ingest Manifest `[014]`, Transcripts `[015]` | `[103]`–`[114]`, `[116]`–`[125]`, `[127]`–`[133]`, `[135]`–`[144]`, `[146]`–`[155]`, `[157]`–`[166]` | `EVALUATE_AND_RANK_TAKES` (`[486]`), `COMPILE_ASSEMBLY_SEQUENCE` (`[490]`), `EMIT_EDL_MANIFEST` (`[496]`) | `[017]` EDL Cut Manifest (File A), `[018]` Rhythm Map |
| `(?i)(color\|grade\|lut\|scopes\|waveform\|vectorscope\|skin tone\|aces\|hdr\|cst)` | `[177]` Color Grading | Locked EDL `[017]`, Camera Log metadata | `[179]`–`[192]`, `[194]`–`[205]`, `[207]`–`[218]`, `[220]`–`[230]`, `[244]`–`[252]`, `[254]`–`[265]` | `ANALYZE_SCOPES` (`[498]`), `BUILD_NODE_GRAPH` (`[499]`), `SET_PRIMARY_BALANCE` (`[500]`), `EMIT_GRADE_SPEC` (`[506]`) | `[019]` Color Grade Spec (File B), `[020]` Shot Match Matrix |
| `(?i)(sound\|audio\|mix\|lufs\|dbtp\|foley\|dialogue cleanup\|eq\|reverb\|ducking)` | `[267]` Sound Design & Mix | Locked EDL `[017]`, Audio Stems | `[269]`–`[284]`, `[286]`–`[296]`, `[298]`–`[305]`, `[307]`–`[314]`, `[316]`–`[324]`, `[326]`–`[333]` | `CLEAN_AND_LEVEL_DIALOGUE` (`[515]`), `ALIGN_MUSIC_AND_DUCKING` (`[519]`), `CALIBRATE_LUFS_AND_TRUE_PEAK` (`[520]`), `EMIT_MIX_SPEC` (`[522]`) | `[023]` DX EDL, `[024]` Foley Cue, `[025]` Mix Spec (File D) |
| `(?i)(subtitle\|caption\|sdh\|cps\|cpl\|timed text\|srt\|vtt\|ttml\|imsc1)` | `[335]` Subtitling & Localization | Locked EDL `[017]`, Timed Transcript `[015]` | `[337]`–`[348]`, `[350]`–`[359]`, `[361]`–`[368]`, `[370]`–`[376]` | `SEGMENT_CUES` (`[507]`), `CALCULATE_METRICS` (`[508]`), `CONDENSE_HIGH_CPS_TEXT` (`[509]`), `EMIT_COMPLIANCE_REPORT` (`[514]`) | `[021]` Subtitle Cue, `[022]` Subtitle Audit (File C) |
| `(?i)(vfx\|conform\|plate pull\|exr\|roto\|cleanup\|paint\|motion graphics\|titles)` | `[378]` VFX & Conform | Locked EDL `[017]`, Camera RAW | `[380]`–`[387]`, `[389]`–`[395]`, `[397]`–`[403]`, `[405]`–`[409]` | `RELINK_AND_CONFORM_RAW` (`[523]`), `GENERATE_EXR_PULL_SHEET` (`[524]`) | `[026]` VFX Pull Sheet, `[027]` Online Conform Map |
| `(?i)(finish\|master\|imf\|dcp\|qc\|prores\|dnxhr\|2-pop\|leader\|harding)` | `[410]` Finishing & QC | Files A, B, C, D complete | `[412]`–`[419]`, `[421]`–`[426]`, `[428]`–`[435]`, `[437]`–`[442]`, `[444]`–`[452]` | `CONFIGURE_MASTER_CODEC` (`[525]`), `ASSEMBLE_LEADERS_AND_2POP` (`[526]`), `RUN_AUTOMATED_QC_GATES` (`[527]`), `EMIT_DELIVERY_SPEC` (`[529]`) | `[028]` Delivery Spec (File E), `[029]` QC Report, `[030]` Package Manifest |
| `(?i)(commercial\|trailer\|podcast\|youtube\|documentary\|narrative playbook)` | `[454]` Genre Playbooks | Story beat, raw rushes | `[456]`–`[460]`, `[462]`–`[466]`, `[468]`–`[472]`, `[474]`–`[478]` | Delegated to Depts 02, 03, 04, 05 | Specific Genre Master Package |

---

## 3. Minimal Context Loading Protocol

To prevent context exhaustion and hallucination, this router enforces the **3–8 Leaf Loading Rule**:
1. Identify the primary task from the prompt.
2. Load exactly **one** primary department router (`[031]`, `[101]`, `[177]`, `[267]`, `[335]`, `[378]`, or `[410]`).
3. Load between **3 and 8** targeted leaf `.md` files directly addressing the micro-task.
4. Load exactly **one** parameter reference table (`[531]`–`[565]`).
5. Load exactly **one** schema lock file (`[014]`–`[030]`).
6. Load the associated validator gate (`[567]`–`[592]`).
7. Explicitly emit the loaded file identifiers at the head of every operational trace:
   `LOADED_SKILLS: ["[001]", "[101]", "[102]", "[105]", "[114]", "[017]", "[532]", "[567]"]`

---

## 4. Stage-Gate Precondition Contract

Every request must satisfy topological DAG stage dependencies before execution:

```
[014] INGEST_LOCKED
        │
        ▼
[016] PAPER_EDIT_APPROVED
        │
        ▼
[017] ASSEMBLY_CUT ──► ROUGH_CUT ──► FINE_CUT ──► PICTURE_LOCK (2-Pop + FFOA)
                                                        │
                      ┌─────────────────────────────────┼─────────────────────────────────┐
                      ▼                                 ▼                                 ▼
           [019] COLOR_GRADE_LOCKED           [025] SOUND_MIX_LOCKED           [022] SUBTITLES_COMPLIANT
                      │                                 │                                 │
                      └─────────────────────────────────┼─────────────────────────────────┘
                                                        ▼
                                              [027] ONLINE_CONFORM
                                                        │
                                                        ▼
                                              [029] QC_ALL_GATES_PASS
                                                        │
                                                        ▼
                                              [028] MASTER_DELIVERED (File E)
```

* **Gate Rule 1**: Color (`[177]`), Sound (`[267]`), Subtitles (`[335]`), and VFX (`[378]`) may **NEVER** commence work on non-locked timelines without explicit ripple propagation tracking (`[009]`).
* **Gate Rule 2**: No master deliverable (`[028]`) may be emitted unless all 9 Automated QC Gates (`[444]`–`[452]`) record `"status": "pass"`.

---

## 5. The 5 Immutable System Contracts

1. **NEVER emit a Color Grade** without numeric `scope_evidence`:
   - Waveform: `black_point_ire`, `white_point_ire`, `highlight_clipping`, `shadow_crush`.
   - Vectorscope: `skin_tone_alignment` (123° ± 3° I-line), `saturation_envelope`.
   - Parade: `channel_balance` (R=G=B floor and ceiling alignment).
2. **NEVER emit an EDL event** without `selection_rationale` and `disqualification_notes`:
   - Must cite candidate take scores, filler counts, exact millisecond dead pauses, and opener/tail trim frames.
3. **NEVER emit a Subtitle Cue** without calculated metrics:
   - Must include `cps` (<= 20.0), `cpl` (<= 42), `line_count` (<= 2), `duration_ms` ([833ms, 7000ms]), and shot-change dead-zone compliance.
4. **NEVER emit a Sound Mix Specification** without calibrated physical targets:
   - Must include `dialogue_target_lufs`, `true_peak_ceiling_dbtp`, `duck_under_dialogue`, and mathematical DME stem parity.
5. **NEVER emit any deliverable** without passing its mapped deterministic validator gate (`[566]`).

---

## 6. Escalation & Edge-Case Fallback Table

When execution anomalies occur, dispatch immediately to the recovery matrix:

| Anomaly Class | Trigger Condition | Escalation Target | Resolution Action |
|---|---|---|---|
| **Editorial Failure** | Zero clean takes available | `[635]` | Syllable composite Frankenbite reconstruction |
| **Pacing Drift** | Sequence exceeds broadcast slot | `[133]` | Distributed proportional micro-trimming |
| **Gamut Excursion** | Saturated LEDs exceed legal boundary | `[647]` / `[192]` | ACES parametric saturation compression |
| **Skin Vector Mismatch** | Sunburn or mixed lighting blotches | `[648]` | Dual-qualifier hue rotation & softening |
| **Acoustic Wind Buffeting**| Lav capsule clipped by air velocity | `[655]` | Dynamic low-shelf + harmonic overtone synthesis |
| **Reading Speed Violation**| Spoken dialogue exceeds 20.0 CPS | `[353]` / `[509]` | Deterministic linguistic condensation (-25% chars) |
| **Epilepsy Safety Gate** | Flash frequency > 3 Hz, > 20 cd/m² | `[444]` / `[678]` | Temporal luma attenuation pass |
| **Human Taste Gate** | Ambiguous Look Dev / Music Cue / Take Tie| `[006]` | Pause and present 2–3 structured trade-off options |

---

## 7. Execution Hand-Off to Runtime

To execute incoming tasks, the agent must initialize the runtime trace:
`INIT_RUNTIME: file_id="[001]", status="DISPATCHING_DEPARTMENT", stage_gate_checked=true`
and invoke the designated Department Router.

---

## 8. FilmCraft Native CLI & Bridge Execution Layer

All Skill Master Commands (`[480]`–`[529]`) and operational workflows connect directly to the FilmCraft open-source editing engine via:
- **Command Specification & Subsystem Directory**: [FILMCRAFT_COMMAND_ROUTING_BRIDGE.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo/FILMCRAFT_COMMAND_ROUTING_BRIDGE.md) (All 701 commands mapped across 42 subsystems).
- **Execution Bridge Module**: [filmcraft_cli_bridge.py](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/filmcraft_cli_bridge.py)
- **Live GUI Loopback Port**: `127.0.0.1:9876` (`filmcraft-cli --bridge 127.0.0.1:9876`)
- **Headless Pipeline**: `filmcraft-cli --project <path.fcproj> exec <command_id>`
