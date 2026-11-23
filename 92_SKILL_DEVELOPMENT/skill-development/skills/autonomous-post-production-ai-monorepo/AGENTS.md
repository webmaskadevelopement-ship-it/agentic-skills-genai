---
file_id: "[002]"
skill_path: "AGENTS.md"
role: "Multi-Agent Swarm Topology, Department Hand-offs & State Machine"
parent_router: "[001]"
child_nodes:
  - "[031]"
  - "[101]"
  - "[177]"
  - "[267]"
  - "[335]"
  - "[378]"
  - "[410]"
schema_locks:
  - "[014]"
  - "[016]"
  - "[017]"
  - "[019]"
  - "[022]"
  - "[025]"
  - "[028]"
---

# [002] Multi-Agent Swarm Topology, Department Hand-offs & State Machine

## 1. Executive Multi-Agent Architecture

The post-production lifecycle within `autonomous-post-production-ai-monorepo/` is executed by a decentralized swarm of **7 specialized Department Agents**, governed by strict stage gates, read/write boundaries, and deterministic state transitions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MULTI-AGENT SWARM TOPOLOGY                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [1] Assistant Editor Agent ([031]–[100])                                   │
│      └─ Ingest Manifest [014], Timed Transcript [015], Multi-Cam Sync       │
│                                │                                            │
│                                ▼                                            │
│  [2] Lead Picture Editor Agent ([101]–[176])                                │
│      └─ Paper Edit [016], Selects Evaluation, Cut Manifest [017] (File A)   │
│                                │                                            │
│                 PICTURE LOCK & 2-POP SIGN-OFF [132]                         │
│                                │                                            │
│        ┌───────────────────────┼───────────────────────┐                    │
│        ▼                       ▼                       ▼                    │
│  [3] Senior Digital      [4] Supervising Sound   [5] Lead Localization      │
│      Colorist Agent          Mixer Agent             Editor Agent           │
│      ([177]–[266])           ([267]–[334])           ([335]–[377])          │
│      └─ Grade Spec [019]     └─ Mix Spec [025]       └─ Subtitle Audit [022]│
│         (File B)                (File D)                (File C)            │
│        │                       │                       │                    │
│        └───────────────────────┼───────────────────────┘                    │
│                                │                                            │
│                                ▼                                            │
│  [6] Online Conform & VFX Supervisor Agent ([378]–[409])                    │
│      └─ RAW Relink [027], EXR Pulls [026], Titles & Safe Area [405]         │
│                                │                                            │
│                                ▼                                            │
│  [7] Finishing & QC Supervisor Agent ([410]–[453])                          │
│      └─ Leaders/2-Pop [440], 9 Automated QC Gates [444]–[452],              │
│         Delivery Spec Sheet [028] (File E)                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Department Agent Specifications & Read/Write Boundaries

### Agent 1: Assistant Editor Agent (`[031]`–`[100]`)
* **Role**: Ingest integrity, checksum verification, camera RAW metadata extraction, multi-cam/audio synchronization, transcript phoneme alignment, and NLE bin organization.
* **Governing Skills**: `[031]`–`[100]`.
* **Read Permissions**: Raw camera media cards, BWF audio files, sound reports, script supervisor logs.
* **Write Permissions**:
  - `[014] schema-ingest-manifest.md`
  - `[015] schema-word-level-transcript.md`
  - Standardized NLE Bin Structures & Sync Sequences.
* **Exit Gate Assertion**: Gate 01 (`[100]`) pass: 100% byte verification, LTC/waveform audio sync <= 0.4ms delta, and phoneme alignment confidence >= 0.95.

### Agent 2: Lead Picture Editor Agent (`[101]`–`[176]`)
* **Role**: Story architecture, selects ranking, dead-pause excision, Walter Murch Rule of Six evaluation, J/L split cutting, rhythm/tempo modulation, and EDL serialization.
* **Governing Skills**: `[101]`–`[176]`.
* **Read Permissions**: `[014]` Ingest Manifest, `[015]` Word-Level Transcript.
* **Write Permissions**:
  - `[016] schema-paper-edit-blueprint.md`
  - `[017] schema-edl-cut-manifest.md` (File A)
  - `[018] schema-rhythm-and-pacing-map.md`
* **Exit Gate Assertion**: Gate 02: Monotonic timecode continuity (`[568]`), source handle availability (`[570]`), and Picture Lock with 2-Pop at `00:59:58:00` and FFOA at `01:00:00:00` (`[132]`).

### Agent 3: Senior Digital Colorist Agent (`[177]`–`[266]`)
* **Role**: Color science transforms (ACES/DWG), exposure calibration, white balancing, 12-node serial/parallel grading, skin-tone vectorscope alignment (123° I-line), and film print emulation.
* **Governing Skills**: `[177]`–`[266]`.
* **Read Permissions**: Locked `[017]` EDL Cut Manifest, camera metadata from `[014]`.
* **Write Permissions**:
  - `[019] schema-color-grade-specification.md` (File B)
  - `[020] schema-shot-match-delta-matrix.md`
  - 3D LUTs (`.cube`) and DRX node trees.
* **Exit Gate Assertion**: Gate 03: Black floor at 2.0–5.0 IRE, diffuse white <= 90 IRE, skin vector at 123° ± 3°, and zero un-scoped grade parameters (`[573]`).

### Agent 4: Supervising Sound Designer & Re-Recording Mixer Agent (`[267]`–`[334]`)
* **Role**: Dialogue surgical restoration, room tone synthesis, Foley/hard SFX layering, acoustic space convolution, music dynamic/spectral ducking, and ITU-R BS.1770-4 loudness compliance.
* **Governing Skills**: `[267]`–`[334]`.
* **Read Permissions**: Locked `[017]` EDL Cut Manifest, BWF audio tracks, music cues.
* **Write Permissions**:
  - `[023] schema-dialogue-edit-decision-list.md`
  - `[024] schema-sound-design-and-foley-cue.md`
  - `[025] schema-mix-and-loudness-specification.md` (File D)
  - DME Stems (Dialogue, Music, Effects) & Full Mix master.
* **Exit Gate Assertion**: Gate 04: Integrated loudness hits platform spec (e.g., -23.0 LUFS ±0.5 LU EBU or -24.0 LKFS ATSC), True Peak <= -1.0 dBTP, and zero digital -inf dBFS holes in dialogue (`[586]`, `[587]`).

### Agent 5: Lead Localization & Timed-Text Editor Agent (`[335]`–`[377]`)
* **Role**: Syntactic line breaking, reading speed enforcement (CPS <= 20.0), CPL ceilings (<= 42 chars), shot-change dead-zone snapping, SDH tags, and timed-text format serialization.
* **Governing Skills**: `[335]`–`[377]`.
* **Read Permissions**: Locked `[017]` EDL Cut Manifest, `[015]` Word-Level Transcript.
* **Write Permissions**:
  - `[021] schema-subtitle-timed-text-cue.md`
  - `[022] schema-subtitle-compliance-audit.md` (File C)
  - Timed text artifacts (`.srt`, `.vtt`, `.ttml`, `.scc`).
* **Exit Gate Assertion**: Gate 05: 100% compliance across all cues (`cps <= 20.0`, `cpl <= 42`, `duration_ms` between 833ms and 7000ms, and zero shot-change dead zone collisions `[580]`–`[582]`).

### Agent 6: Online Conform & VFX Supervisor Agent (`[378]`–`[409]`)
* **Role**: Proxy-to-camera-RAW conform, difference matte verification, 16-bit half-float ACEScg OpenEXR plate pulls, planar tracking, screen replacement, and broadcast title safe area enforcement.
* **Governing Skills**: `[378]`–`[409]`.
* **Read Permissions**: Locked `[017]` EDL Cut Manifest, camera RAW pool, VFX turnovers.
* **Write Permissions**:
  - `[026] schema-vfx-turnover-and-pull-sheet.md`
  - `[027] schema-online-conform-relink-map.md`
  - Conformed high-res sequence timeline.
* **Exit Gate Assertion**: Gate 06: Difference matte vs offline reference Pixel_Delta == 0.0 (`[381]`), title safe margins >= 90% (`[405]`), and scroll anti-judder integer velocity (`[407]`).

### Agent 7: Finishing & QC Supervisor Agent (`[410]`–`[453]`)
* **Role**: Mastering codec configuration, SMPTE RP-219 bars and 1 kHz tone lineup, 2-pop placement, IMF/DCP packaging, execution of the 9 Automated QC Gates, and final release sign-off.
* **Governing Skills**: `[410]`–`[453]`.
* **Read Permissions**: Files A, B, C, D, conformed media, stems.
* **Write Permissions**:
  - `[028] schema-delivery-and-mastering-spec.md` (File E)
  - `[029] schema-automated-qc-gate-report.md`
  - `[030] schema-imf-and-dcp-package-manifest.md`
* **Exit Gate Assertion**: Gate 07: All 9 Automated QC Gates (`[444]`–`[452]`) record `"status": "pass"`.

---

## 3. The 10-Stage Deterministic Handoff State Machine

```
State 01: INGEST_LOCKED
          Trigger: Ingest Agent completes hash checks and transcript alignment.
          Artifacts Locked: [014] Ingest Manifest, [015] Word Transcript.

State 02: PAPER_EDIT_APPROVED
          Trigger: Lead Picture Editor establishes story beat arc and candidate selects.
          Artifacts Locked: [016] Paper Edit Blueprint.

State 03: ASSEMBLY_CUT
          Trigger: 100% of scripted dialogue lines and scenes placed on V1/A1–A8.
          Artifacts Emitted: [017] EDL (stage: "assembly").

State 04: ROUGH_CUT
          Trigger: Structural scenes reordered, >=20% fat trimmed, scenes advance plot.
          Artifacts Emitted: [017] EDL (stage: "rough_cut").

State 05: FINE_CUT
          Trigger: Frame-accurate trimming (2–8 frames), J/L audio overlaps locked.
          Artifacts Emitted: [017] EDL (stage: "fine_cut").

State 06: PICTURE_LOCK
          Trigger: Runtime frozen, head 2-pop placed at 00:59:58:00, FFOA at 01:00:00:00.
          Artifacts Emitted: [017] EDL (stage: "final_cut"), cryptographic timeline hash [687].

State 07: PARALLEL_FINISHING
          Trigger: Parallel dispatch of Colorist, Sound Mixer, and Subtitle Agents on locked EDL.
          Artifacts Emitted: [019] Grade Spec (File B), [025] Mix Spec (File D), [022] Subtitles (File C).

State 08: ONLINE_CONFORM
          Trigger: VFX plates pulled and proxy timeline relinked to camera RAW.
          Artifacts Emitted: [026] VFX Pulls, [027] Conform Relink Map.

State 09: QC_AUDIT_EXECUTION
          Trigger: Finishing Agent executes all 9 Automated QC Gates ([444]–[452]).
          Artifacts Emitted: [029] Automated QC Gate Report.

State 10: MASTER_DELIVERED
          Trigger: 100% QC Pass; master package and File E released.
          Artifacts Emitted: [028] Delivery Spec (File E), [030] Package Manifest.
```

---

## 4. Conflict Resolution & Arbitration Hierarchy

When two department recommendations clash during production, the following priority order is strictly enforced by `[013]`:

1. **Safety & Legal Broadcast QC (`[444]`–`[452]`)**: Overrides all artistic preferences. (e.g., Harding flash failures require luminance reduction regardless of director intent).
2. **Narrative & Emotional Priority (`[135]`)**: Overrides technical/spatial continuity. (Walter Murch Priority 1 & 2 override Priority 6).
3. **Dialogue Intelligibility (`[268]`, `[316]`)**: Overrides music volume and background SFX density.
4. **Skin-Tone Continuity (`[197]`, `[245]`)**: Overrides aggressive stylized LUT pushes.
5. **Reading Speed Ceilings (`[338]`)**: Overrides verbatim dialogue transcription when CPS > 20.0.
