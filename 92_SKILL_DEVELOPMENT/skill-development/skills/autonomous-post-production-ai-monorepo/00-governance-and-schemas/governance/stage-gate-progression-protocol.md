---
file_id: "[004]"
skill_path: "00-governance-and-schemas/governance/stage-gate-progression-protocol.md"
role: "Stage-Gate Progression Protocol & Lifecycle Enforcer"
parent_router: "[001]"
schema_locks:
  - "[014]"
  - "[016]"
  - "[017]"
  - "[028]"
validators:
  - "[572]" # validator-edl-stage-gate-readiness
  - "[592]" # validator-master-qc-all-gates-green-signoff
---

# [004] Stage-Gate Progression Protocol & Lifecycle Enforcer

## 1. Principle & Operational Mandate

In professional film, television, and commercial post-production, **stage skipping is strictly prohibited**. Attempting to color grade, sound design, or conform an editorial cut that has not formally cleared Picture Lock creates unrecoverable ripple overhead, redundant conform costs, and version desynchronization.

This protocol enforces **6 sequential, deterministic stage gates** from raw ingest to final release. Every stage transition requires an explicit validator sign-off before downstream departments are permitted to read the sequence.

---

## 2. The 6 Progressive Editorial Stage Gates

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROGRESSIVE STAGE-GATE PIPELINE                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  STAGE 1: RADIO EDIT (AUDIO-ONLY SPINE)                                     │
│  ▼ (Gate 1 Pass: Scripted Dialogue Coverage >= 95%, WPM continuity)         │
│  STAGE 2: ASSEMBLY CUT                                                      │
│  ▼ (Gate 2 Pass: 100% Scenes placed in script order, zero orphan clips)     │
│  STAGE 3: ROUGH CUT                                                         │
│  ▼ (Gate 3 Pass: Structural fat trimmed >= 20%, narrative beats advance plot)│
│  STAGE 4: FINE CUT                                                          │
│  ▼ (Gate 4 Pass: Frame-accurate heads/tails, J/L overlaps, handles verified)│
│  STAGE 5: PICTURE LOCK & 2-POP (FREEZE)                                     │
│  ▼ (Gate 5 Pass: 2-Pop at 00:59:58:00, FFOA at 01:00:00:00, hash locked)   │
│  STAGE 6: PARALLEL FINISHING -> MASTER RELEASE                              │
│    (Gate 6 Pass: All 9 Automated QC Gates [444]–[452] record "pass")        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Stage Criteria & Entry/Exit Gates

### Stage 1: Radio Edit (Dialogue-Only Spine)
* **Objective**: Establish complete verbal narrative coherence on audio tracks (A1–A8) with picture disabled.
* **Entry Criteria**: Ingest Manifest (`[014]`) verified; word-level transcript (`[015]`) aligned to <= 10ms.
* **Required Operations**:
  - Filter unmotivated dead pauses (> 2000ms) via `[105]`.
  - Eliminate filler words ("um", "uh") via `[103]`.
  - Assemble A-roll dialogue bites into a linear spoken argument (`[116]`).
* **Exit Gate 1 Criteria**:
  - Scripted core dialogue coverage >= 95.0%.
  - Dialogue intelligibility confirmed; speaker WPM within normal conversational bounds (130–175 WPM).
  - Emits `schema-paper-edit-blueprint.md` (`[016]`).

### Stage 2: Assembly Cut
* **Objective**: Place 100% of scripted scenes and visual coverage onto the timeline in script sequence.
* **Entry Criteria**: Approved Stage 1 Paper Edit (`[016]`).
* **Required Operations**:
  - Place best candidate takes on V1 and A1–A4 (`[128]`).
  - Retain generous heads and tails (minimum 12–24 frame safety handles).
  - Do NOT micro-trim or obsess over rhythm at this stage.
* **Exit Gate 2 Criteria**:
  - 100% of scenes from script/storyboard are present.
  - Zero timeline gaps or orphan media clips.
  - Emits `schema-edl-cut-manifest.md` with `edit_stage: "assembly"`.

### Stage 3: Rough Cut
* **Objective**: Structural restructuring, pacing modulation, scene deletions, and dramatic arc shaping.
* **Entry Criteria**: Approved Stage 2 Assembly Cut.
* **Required Operations**:
  - Delete redundant exposition or non-advancing scenes ("Enter late, leave early" `[124]`).
  - Reorder scenes to optimize dramatic conflict and suspense (`[129]`).
  - Trim runtime fat by >= 20.0% relative to Assembly duration.
* **Exit Gate 3 Criteria**:
  - Dramatic conflict verified for every retained scene (`[123]`).
  - Total runtime within 115% of target delivery slot.
  - Emits `schema-edl-cut-manifest.md` with `edit_stage: "rough_cut"`.

### Stage 4: Fine Cut
* **Objective**: Frame-level precision cutting, emotional resonance, rhythm quantization, and audio overlap integration.
* **Entry Criteria**: Approved Stage 3 Rough Cut; director/producer structural consensus.
* **Required Operations**:
  - Shave 2 to 8 frames off clip heads and tails (`[130]`).
  - Calculate J-cut audio lead-ins (12–36 frames) and L-cut trail-outs (12–48 frames) (`[146]`, `[147]`).
  - Enforce Walter Murch Rule of Six cutting priorities (`[135]`–`[140]`).
  - Cut on action motion peaks (`[141]`) and actor blinks (`[142]`).
* **Exit Gate 4 Criteria**:
  - Zero unmotivated jump cuts (`[144]`).
  - All transitions have verified source handle reserves (`[175]`).
  - Emits `schema-edl-cut-manifest.md` with `edit_stage: "fine_cut"`.

### Stage 5: Picture Lock & 2-Pop Freeze
* **Objective**: Finalize timeline frame count permanently to enable parallel finishing.
* **Entry Criteria**: Unanimous editorial and directorial sign-off on Fine Cut.
* **Required Operations**:
  - Freeze all cut points, speed ramps, and frame durations permanently.
  - Attach Universal Broadcast Leader:
    - `00:58:30:00 – 00:59:30:00`: SMPTE RP-219 Color Bars + 1 kHz Tone (-20 dBFS / -18 dBFS).
    - `00:59:50:00 – 00:59:58:00`: Production Slate + Countdown.
    - `00:59:58:00 – 00:59:58:01`: **Head 2-Pop** (1 frame flash + 1 kHz sine beep).
    - `01:00:00:00`: **First Frame of Action (FFOA)**.
    - `LFOA + 00:00:02:00`: **Tail 2-Pop**.
  - Compute cryptographic timeline SHA-256 hash (`[687]`).
* **Exit Gate 5 Criteria**:
  - Sequence duration and frame indices locked.
  - Emits `schema-edl-cut-manifest.md` with `edit_stage: "final_cut"`.
  - **Dispatches parallel downstream turnover** to Color (`[177]`), Sound (`[267]`), Subtitles (`[335]`), and VFX (`[378]`).

### Stage 6: Parallel Finishing -> Master Release
* **Objective**: Multi-department conform, high-resolution rendering, and delivery package generation.
* **Entry Criteria**: Picture Lock hash confirmed across all department sessions.
* **Required Operations**:
  - Color: 12-node grade, scope compliance, 123° skin alignment (`[177]`).
  - Sound: Dialogue cleanup, room tone loop, DME stem balance, -23.0 LUFS / -24.0 LKFS mix (`[267]`).
  - Subtitles: 20 CPS / 42 CPL, dead zone snapping (`[335]`).
  - Conform: Camera RAW relink, EXR plate composite, safe-zone titles (`[378]`).
  - Run the 9 Automated QC Gates (`[444]`–`[452]`).
* **Exit Gate 6 Criteria**:
  - 100% of QC gates report `"status": "pass"`.
  - Emits `schema-delivery-and-mastering-spec.md` (`[028]`, File E).

---

## 4. Stage-Gate Violation Handling

If an agent attempts to execute an action out of sequence (e.g., executing Color Grading on an `assembly` EDL):
1. **Immediate Execution Halt**: Reject request with error code `STAGE_GATE_VIOLATION_E001`.
2. **State Diagnostic Trace**:
   ```json
   {
     "status": "error",
     "error_code": "STAGE_GATE_VIOLATION_E001",
     "current_stage": "assembly",
     "required_stage": "final_cut",
     "message": "Downstream finishing requires Picture Lock sign-off. Execute [129] and [130] first."
   }
   ```
3. Route to `[009] cross-department-ripple-propagation.md` if an emergency cut mutation is forced post-lock.
