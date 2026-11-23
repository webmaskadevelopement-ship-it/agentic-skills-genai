---
file_id: "[017]"
skill_path: "00-governance-and-schemas/schemas/schema-edl-cut-manifest.md"
role: "Master Schema Lock: Edit Decision List (EDL) / Cut Manifest (File A)"
parent_router: "[001]"
department_router: "[101]"
master_commands:
  - "COMPILE_ASSEMBLY_SEQUENCE"
  - "REFINE_ROUGH_TO_FINE_CUT"
  - "EMIT_EDL_MANIFEST"
validators:
  - "[567]" # validator-edl-schema-and-required-fields
  - "[568]" # validator-edl-record-timecode-continuity
  - "[569]" # validator-edl-source-in-out-duration-parity
  - "[570]" # validator-edl-transition-handle-sufficiency
---

# [017] Master Schema Lock: Edit Decision List (EDL) / Cut Manifest (File A)

## Block 1: Schema Identity & System Binding

* **Deliverable ID**: File A — Master Edit Decision List (EDL) & Cut Manifest.
* **Governing Standard**: SMPTE 12M Timecode, CMX 3600 Specification, and RFC 8259 JSON.
* **Upstream Generator Commands**: `COMPILE_ASSEMBLY_SEQUENCE` (`[490]`), `REFINE_ROUGH_TO_FINE_CUT` (`[491]`), `EMIT_EDL_MANIFEST` (`[496]`).
* **Downstream Consumers**:
  - Color Grading (`[177]`): Source timecodes, reel names, clip IDs.
  - Sound Design (`[267]`): Cut boundaries, dialogue scene tracks, speech offsets.
  - Subtitling (`[335]`): Cut frame indices for shot-change dead zone snapping.
  - VFX & Conform (`[378]`): Camera RAW relinking, handles, pull ranges.
* **Inspection Validators**: `[567]`, `[568]`, `[569]`, `[570]`, `[571]`, `[572]`.

---

## Block 2: Formal JSON Schema (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://autonomous-post.ai/schemas/edl-cut-manifest.json",
  "title": "EDLCutManifest",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "project",
    "sequence",
    "fps",
    "timecode_format",
    "edit_stage",
    "timeline_hash",
    "scenes",
    "pacing_notes",
    "rhythm_map"
  ],
  "properties": {
    "project": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
    "sequence": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
    "fps": { "type": "number", "enum": [23.976, 24.0, 25.0, 29.97, 30.0, 50.0, 59.94, 60.0] },
    "timecode_format": { "type": "string", "enum": ["NDF", "DF"] },
    "edit_stage": { "type": "string", "enum": ["assembly", "rough_cut", "fine_cut", "final_cut"] },
    "timeline_hash": { "type": "string", "pattern": "^[a-f0-9]{64}$" },
    "scenes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "scene_number",
          "scene_title",
          "candidate_takes",
          "selection_rationale",
          "clips"
        ],
        "properties": {
          "scene_number": { "type": "integer", "minimum": 1 },
          "scene_title": { "type": "string", "minLength": 2 },
          "candidate_takes": {
            "type": "array",
            "items": { "type": "string", "pattern": "^Take_[0-9]+$" }
          },
          "selection_rationale": { "type": "string", "minLength": 30 },
          "clips": {
            "type": "array",
            "minItems": 1,
            "items": {
              "type": "object",
              "additionalProperties": false,
              "required": [
                "event_id",
                "reel_name",
                "clip_name",
                "track",
                "source_in",
                "source_out",
                "record_in",
                "record_out",
                "speed",
                "transition_in",
                "transition_out",
                "first_words",
                "disqualification_notes"
              ],
              "properties": {
                "event_id": { "type": "integer", "minimum": 1 },
                "reel_name": { "type": "string", "pattern": "^[A-Z0-9]{1,8}$" },
                "clip_name": { "type": "string", "minLength": 4 },
                "track": { "type": "string", "pattern": "^(V[1-9]|A[1-9]|A1[0-9]|A20)$" },
                "source_in": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
                "source_out": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
                "record_in": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
                "record_out": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
                "speed": { "type": "number", "minimum": 0.1, "maximum": 10.0 },
                "transition_in": {
                  "type": "object",
                  "additionalProperties": false,
                  "required": ["type", "duration_frames"],
                  "properties": {
                    "type": { "type": "string", "enum": ["cut", "dissolve", "dip_to_black", "wipe"] },
                    "duration_frames": { "type": "integer", "minimum": 0, "maximum": 120 }
                  }
                },
                "transition_out": {
                  "type": "object",
                  "additionalProperties": false,
                  "required": ["type", "duration_frames"],
                  "properties": {
                    "type": { "type": "string", "enum": ["cut", "dissolve", "dip_to_black", "wipe"] },
                    "duration_frames": { "type": "integer", "minimum": 0, "maximum": 120 }
                  }
                },
                "first_words": { "type": "string" },
                "disqualification_notes": { "type": "string" }
              }
            }
          }
        }
      }
    },
    "pacing_notes": { "type": "string", "minLength": 20 },
    "rhythm_map": {
      "type": "object",
      "additionalProperties": false,
      "required": ["asl_seconds", "cut_density_bpm_sync", "tension_curve"],
      "properties": {
        "asl_seconds": { "type": "number", "minimum": 0.5, "maximum": 30.0 },
        "cut_density_bpm_sync": { "type": "boolean" },
        "tension_curve": {
          "type": "array",
          "items": { "type": "number", "minimum": 0.0, "maximum": 10.0 }
        }
      }
    }
  }
}
```

---

## Block 3: Load-Bearing Evidence Fields

1. `selection_rationale`:
   - Mandatory at the scene level. Omitting this field or submitting `< 30` characters triggers automatic schema rejection via `[567]`.
   - Must document why the selected take was chosen over alternatives (filler ratio, vocal energy, physical performance).
2. `disqualification_notes`:
   - Mandatory for every clip. Cites rejected takes and empirical flaws (dead pauses, boom shadow, mic rustle, focus hunts).
3. `timeline_hash`:
   - Cryptographic SHA-256 string locking the exact event sequence. Prevents downstream departments from working on out-of-date cuts.

---

## Block 4: Cross-Field Mathematical Invariants

For every clip $C_j$ in the manifest:
1. **Source/Record Duration Parity**:
   $$\text{to\_frames}(C_j.\text{record\_out}) - \text{to\_frames}(C_j.\text{record\_in}) \equiv \text{round}\left( \frac{\text{to\_frames}(C_j.\text{source\_out}) - \text{to\_frames}(C_j.\text{source\_in})}{C_j.\text{speed}} \right)$$
2. **Timeline Monotonic Continuity**:
   For adjacent primary clips $C_j, C_{j+1}$ on the same track:
   $$\text{to\_frames}(C_{j+1}.\text{record\_in}) \equiv \text{to\_frames}(C_j.\text{record\_out})$$
   *(Enforced by `[568]`; deviations trigger black frame or track collision warnings).*

---

## Block 5: Canonical Valid Payload (File A Example)

```json
{
  "project": "APOLLO_11_DOC",
  "sequence": "SC04_TRANQUILITY",
  "fps": 24.0,
  "timecode_format": "NDF",
  "edit_stage": "final_cut",
  "timeline_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "scenes": [
    {
      "scene_number": 4,
      "scene_title": "Lunar Landing Contact",
      "candidate_takes": ["Take_1", "Take_2", "Take_3", "Take_4"],
      "selection_rationale": "Selected Take 4 (01:14:22:08–01:14:29:16): Zero filler tokens, calm technical delivery (152 WPM), opener cleanly trimmed 3 frames before 'Contact light'. WPM matches preceding capcom telemetry within 3 WPM.",
      "clips": [
        {
          "event_id": 1,
          "reel_name": "A001R1AB",
          "clip_name": "A001_C014_261024_R1AB.mov",
          "track": "V1",
          "source_in": "01:14:22:08",
          "source_out": "01:14:29:16",
          "record_in": "01:00:00:00",
          "record_out": "01:00:07:08",
          "speed": 1.0,
          "transition_in": { "type": "cut", "duration_frames": 0 },
          "transition_out": { "type": "cut", "duration_frames": 0 },
          "first_words": "Contact light. Engine stop.",
          "disqualification_notes": "Disqualified Take 1 (telemetry glitch at 01:04:12:00); Disqualified Take 2 (2,450ms dead pause between 'light' and 'engine'); Disqualified Take 3 (garbled comms drop on 'engine')."
        },
        {
          "event_id": 2,
          "reel_name": "A002R1AB",
          "clip_name": "A002_C008_261024_R1AB.mov",
          "track": "V1",
          "source_in": "02:05:10:00",
          "source_out": "02:05:14:12",
          "record_in": "01:00:07:08",
          "record_out": "01:00:11:20",
          "speed": 1.0,
          "transition_in": { "type": "cut", "duration_frames": 0 },
          "transition_out": { "type": "cut", "duration_frames": 0 },
          "first_words": "Tranquility base here. The Eagle has landed.",
          "disqualification_notes": "Selected Take 2: Unbroken historical statement, zero disfluency, audio levels hit -24 LKFS cleanly."
        }
      ]
    }
  ],
  "pacing_notes": "Progressive acceleration into touchdown: Event 1 (7.33s hold on lunar surface shadow) cuts on thruster shutdown transient into Event 2 MCU Houston relief (4.50s hold).",
  "rhythm_map": {
    "asl_seconds": 5.91,
    "cut_density_bpm_sync": false,
    "tension_curve": [8.5, 9.8, 10.0, 4.2]
  }
}
```

---

## Block 6: Canonical Invalid Payload & Error Trace

### Invalid Snippet (Missing Rationale & Negative Frame Gap)
```json
{
  "project": "APOLLO_11_DOC",
  "sequence": "SC04",
  "fps": 24.0,
  "timecode_format": "NDF",
  "edit_stage": "final_cut",
  "timeline_hash": "invalid-short-hash",
  "scenes": [
    {
      "scene_number": 4,
      "scene_title": "Lunar Landing",
      "candidate_takes": ["Take_1"],
      "selection_rationale": "Looks good.",
      "clips": [
        {
          "event_id": 1,
          "reel_name": "A001R1AB",
          "clip_name": "A001_C014.mov",
          "track": "V1",
          "source_in": "01:14:22:08",
          "source_out": "01:14:29:16",
          "record_in": "01:00:00:00",
          "record_out": "01:00:07:08",
          "speed": 1.0,
          "transition_in": { "type": "cut", "duration_frames": 0 },
          "transition_out": { "type": "cut", "duration_frames": 0 },
          "first_words": "Contact",
          "disqualification_notes": "None"
        },
        {
          "event_id": 2,
          "reel_name": "A002R1AB",
          "clip_name": "A002_C008.mov",
          "track": "V1",
          "source_in": "02:05:10:00",
          "source_out": "02:05:14:12",
          "record_in": "01:00:07:06",
          "record_out": "01:00:11:18",
          "speed": 1.0,
          "transition_in": { "type": "cut", "duration_frames": 0 },
          "transition_out": { "type": "cut", "duration_frames": 0 },
          "first_words": "Tranquility",
          "disqualification_notes": "None"
        }
      ]
    }
  ],
  "pacing_notes": "Standard",
  "rhythm_map": {
    "asl_seconds": 5.9,
    "cut_density_bpm_sync": false,
    "tension_curve": [5.0]
  }
}
```

### Validator Diagnostic Error Trace
```
VALIDATION FAILED: [567] validator-edl-schema-and-required-fields
- ERROR 1: /timeline_hash: does not match pattern "^[a-f0-9]{64}$" (got: "invalid-short-hash")
- ERROR 2: /scenes/0/selection_rationale: string length 11 is less than minimum 30 characters (Anti-Shallowness Violation)
- ERROR 3: /pacing_notes: string length 8 is less than minimum 20 characters
VALIDATION FAILED: [568] validator-edl-record-timecode-continuity
- ERROR 4: Record Timecode Collision between Event 1 and Event 2:
           Event 1 record_out: 01:00:07:08 (frame 108176)
           Event 2 record_in:  01:00:07:06 (frame 108174)
           Delta: -2 frames overlap (Overwriting V1 media without edit transition).
```
