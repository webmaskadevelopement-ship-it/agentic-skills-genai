---
file_id: "[025]"
skill_path: "00-governance-and-schemas/schemas/schema-mix-and-loudness-specification.md"
role: "Master Schema Lock: Sound Design & Mix Specification (File D)"
parent_router: "[001]"
department_router: "[267]"
master_commands:
  - "CLEAN_AND_LEVEL_DIALOGUE"
  - "SYNTHESIZE_ROOM_TONE_FILLS"
  - "SPOT_FOLEY_AND_HARD_SFX"
  - "ALIGN_MUSIC_AND_DUCKING"
  - "CALIBRATE_LUFS_AND_TRUE_PEAK"
  - "EMIT_MIX_SPEC"
validators:
  - "[585]" # validator-mix-schema-and-stem-completeness
  - "[586]" # validator-mix-integrated-lufs-and-dbtp-bounds
  - "[587]" # validator-mix-dialogue-room-tone-continuity
  - "[588]" # validator-mix-music-ducking-clearance
  - "[589]" # validator-mix-sfx-timecode-to-edl-sync
---

# [025] Master Schema Lock: Sound Design & Mix Specification (File D)

## Block 1: Schema Identity & System Binding

* **Deliverable ID**: File D — Master Sound Design, Dialogue, Foley & Mix Specification.
* **Governing Standard**: ITU-R BS.1770-4, EBU R128, ATSC A/85, and RFC 8259 JSON.
* **Upstream Generator Commands**: `CLEAN_AND_LEVEL_DIALOGUE` (`[515]`), `SYNTHESIZE_ROOM_TONE_FILLS` (`[516]`), `SPOT_FOLEY_AND_HARD_SFX` (`[517]`), `LAYER_AMBIENCE_AND_REVERB` (`[518]`), `ALIGN_MUSIC_AND_DUCKING` (`[519]`), `CALIBRATE_LUFS_AND_TRUE_PEAK` (`[520]`), `EMIT_MIX_SPEC` (`[522]`).
* **Downstream Consumers**:
  - Pro Tools PTSL Automation Adapter (`[605]`).
  - Resolve Fairlight Audio Adapter (`[598]`).
  - FFmpeg Loudnorm Mastering Filter (`[608]`).
  - Automated QC Gate 05 (`[448]`).
* **Inspection Validators**: `[585]`, `[586]`, `[587]`, `[588]`, `[589]`.

---

## Block 2: Formal JSON Schema (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://autonomous-post.ai/schemas/mix-and-loudness-specification.json",
  "title": "SoundMixSpecification",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "project",
    "scene",
    "dialogue_edit",
    "foley_sfx",
    "ambience",
    "music",
    "mix_spec"
  ],
  "properties": {
    "project": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
    "scene": { "type": "integer", "minimum": 1 },
    "dialogue_edit": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "clip_name",
          "word_level_transcript_reference",
          "filler_removal",
          "room_tone",
          "clip_gain_db",
          "automation_notes"
        ],
        "properties": {
          "clip_name": { "type": "string" },
          "word_level_transcript_reference": { "type": "string" },
          "filler_removal": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "required": ["token", "start_tc", "end_tc", "zero_crossing_verified"],
              "properties": {
                "token": { "type": "string" },
                "start_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
                "end_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
                "zero_crossing_verified": { "type": "boolean" }
              }
            }
          },
          "room_tone": {
            "type": "object",
            "additionalProperties": false,
            "required": ["source_print", "crossfade_frames", "gain_db"],
            "properties": {
              "source_print": { "type": "string" },
              "crossfade_frames": { "type": "integer", "minimum": 2, "maximum": 12 },
              "gain_db": { "type": "number", "minimum": -60.0, "maximum": 0.0 }
            }
          },
          "clip_gain_db": { "type": "number", "minimum": -24.0, "maximum": 12.0 },
          "automation_notes": { "type": "string", "minLength": 10 }
        }
      }
    },
    "foley_sfx": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["event", "timecode", "asset_reference", "level_db", "pan", "notes"],
        "properties": {
          "event": { "type": "string" },
          "timecode": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
          "asset_reference": { "type": "string" },
          "level_db": { "type": "number", "minimum": -60.0, "maximum": 0.0 },
          "pan": { "type": "number", "minimum": -1.0, "maximum": 1.0 },
          "notes": { "type": "string" }
        }
      }
    },
    "ambience": {
      "type": "object",
      "additionalProperties": false,
      "required": ["bed_name", "level_db", "loop", "notes"],
      "properties": {
        "bed_name": { "type": "string" },
        "level_db": { "type": "number", "minimum": -60.0, "maximum": -10.0 },
        "loop": { "type": "boolean" },
        "notes": { "type": "string" }
      }
    },
    "music": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["cue_name", "in_timecode", "out_timecode", "emotional_target", "duck_under_dialogue", "level_db"],
        "properties": {
          "cue_name": { "type": "string" },
          "in_timecode": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
          "out_timecode": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
          "emotional_target": { "type": "string", "minLength": 10 },
          "duck_under_dialogue": {
            "type": "object",
            "additionalProperties": false,
            "required": ["enabled", "attenuation_db", "spectral_dip_hz", "lookahead_ms", "release_ms"],
            "properties": {
              "enabled": { "type": "boolean" },
              "attenuation_db": { "type": "number", "minimum": -24.0, "maximum": 0.0 },
              "spectral_dip_hz": { "type": "array", "items": { "type": "number" }, "minItems": 2, "maxItems": 2 },
              "lookahead_ms": { "type": "integer", "minimum": 50, "maximum": 1000 },
              "release_ms": { "type": "integer", "minimum": 100, "maximum": 2000 }
            }
          },
          "level_db": { "type": "number", "minimum": -60.0, "maximum": 0.0 }
        }
      }
    },
    "mix_spec": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "loudness_standard",
        "dialogue_target_lufs",
        "music_target_lufs",
        "effects_target_lufs",
        "true_peak_ceiling_dbtp",
        "stem_deliverables"
      ],
      "properties": {
        "loudness_standard": { "type": "string", "enum": ["EBU_R128", "ATSC_A85", "Netflix_Dialog_Gated", "YouTube_Social"] },
        "dialogue_target_lufs": { "type": "number", "minimum": -31.0, "maximum": -10.0 },
        "music_target_lufs": { "type": "number", "minimum": -36.0, "maximum": -12.0 },
        "effects_target_lufs": { "type": "number", "minimum": -36.0, "maximum": -12.0 },
        "true_peak_ceiling_dbtp": { "type": "number", "minimum": -6.0, "maximum": 0.0 },
        "stem_deliverables": {
          "type": "object",
          "additionalProperties": false,
          "required": ["dx_stem", "mx_stem", "fx_stem", "me_stem", "null_test_verified"],
          "properties": {
            "dx_stem": { "type": "string" },
            "mx_stem": { "type": "string" },
            "fx_stem": { "type": "string" },
            "me_stem": { "type": "string" },
            "null_test_verified": { "type": "boolean" }
          }
        }
      }
    }
  }
}
```

---

## Block 3: Load-Bearing Evidence Fields

1. `filler_removal` & `room_tone`:
   - Every excised disfluency must cite exact timecode bounds and zero-crossing verification.
   - Dialogue edit gaps must be bridged with a declared room tone source print and crossfade frame duration.
2. `duck_under_dialogue`:
   - Must specify physical ducking envelope: lookahead (300ms), broadband attenuation (-6.0 dB), and spectral carving bounds (1.2 kHz–3.8 kHz).
3. `stem_deliverables.null_test_verified`:
   - Boolean confirming that `Sum(DX + MX + FX)` nulls with the Full Mix master within $\pm 0.01\text{ dB}$.

---

## Block 4: Cross-Field Mathematical Invariants

1. **Loudness Standards Invariant**:
   - For `EBU_R128`: `dialogue_target_lufs == -23.0` ($\pm 0.5\text{ LU}$), `true_peak_ceiling_dbtp <= -1.0`.
   - For `ATSC_A85`: `dialogue_target_lufs == -24.0` ($\pm 1.0\text{ LKFS}$), `true_peak_ceiling_dbtp <= -2.0`.
   - For `Netflix_Dialog_Gated`: `dialogue_target_lufs == -27.0` ($\pm 1.0\text{ LKFS}$), `true_peak_ceiling_dbtp <= -2.0`.
2. **Dialogue Continuity**:
   Zero digital silence ($-\infty\text{ dBFS}$) frames permitted during active narrative scenes.

---

## Block 5: Canonical Valid Payload (File D Example)

```json
{
  "project": "APOLLO_11_DOC",
  "scene": 4,
  "dialogue_edit": [
    {
      "clip_name": "A001_C014_Audio.wav",
      "word_level_transcript_reference": "transcript_sc04_v02.json",
      "filler_removal": [
        {
          "token": "um",
          "start_tc": "01:14:23:14",
          "end_tc": "01:14:23:22",
          "zero_crossing_verified": true
        }
      ],
      "room_tone": {
        "source_print": "RT_LUNAR_MODULE_CABIN_01",
        "crossfade_frames": 4,
        "gain_db": -38.5
      },
      "clip_gain_db": +1.5,
      "automation_notes": "Slight HF shelf lift (+2 dB at 4 kHz) to improve capcom helmet comms clarity."
    }
  ],
  "foley_sfx": [
    {
      "event": "thruster_shutdown_thud",
      "timecode": "01:00:02:18",
      "asset_reference": "SFX_SOLENOID_VALVE_HEAVY_02.wav",
      "level_db": -18.2,
      "pan": 0.0,
      "notes": "Low-end weight at 60 Hz to accent engine shutdown."
    }
  ],
  "ambience": {
    "bed_name": "AMB_APOLLO_CABIN_AIR_RUMBLE_LOOP",
    "level_db": -36.0,
    "loop": true,
    "notes": "Subtle continuous 400 Hz electrical gyro hum."
  },
  "music": [
    {
      "cue_name": "MX_TRANQUILITY_CLIMAX",
      "in_timecode": "01:00:00:00",
      "out_timecode": "01:00:11:20",
      "emotional_target": "Rising tension holding breath until Eagle has landed.",
      "duck_under_dialogue": {
        "enabled": true,
        "attenuation_db": -6.5,
        "spectral_dip_hz": [1200, 3800],
        "lookahead_ms": 300,
        "release_ms": 800
      },
      "level_db": -22.0
    }
  ],
  "mix_spec": {
    "loudness_standard": "EBU_R128",
    "dialogue_target_lufs": -23.0,
    "music_target_lufs": -26.5,
    "effects_target_lufs": -24.0,
    "true_peak_ceiling_dbtp": -1.0,
    "stem_deliverables": {
      "dx_stem": "APOLLO_SC04_STEM_DX.wav",
      "mx_stem": "APOLLO_SC04_STEM_MX.wav",
      "fx_stem": "APOLLO_SC04_STEM_FX.wav",
      "me_stem": "APOLLO_SC04_STEM_ME.wav",
      "null_test_verified": true
    }
  }
}
```

---

## Block 6: Canonical Invalid Payload & Error Trace

### Invalid Snippet (Missing Ducking Envelope & True Peak Violation)
```json
{
  "project": "APOLLO_11_DOC",
  "scene": 4,
  "dialogue_edit": [],
  "foley_sfx": [],
  "ambience": { "bed_name": "room", "level_db": -30.0, "loop": true, "notes": "ambience" },
  "music": [
    {
      "cue_name": "MX_01",
      "in_timecode": "01:00:00:00",
      "out_timecode": "01:00:10:00",
      "emotional_target": "Exciting",
      "duck_under_dialogue": { "enabled": true, "attenuation_db": 0.0, "spectral_dip_hz": [1000, 2000], "lookahead_ms": 10, "release_ms": 50 },
      "level_db": -10.0
    }
  ],
  "mix_spec": {
    "loudness_standard": "EBU_R128",
    "dialogue_target_lufs": -16.0,
    "music_target_lufs": -10.0,
    "effects_target_lufs": -12.0,
    "true_peak_ceiling_dbtp": +0.8,
    "stem_deliverables": { "dx_stem": "", "mx_stem": "", "fx_stem": "", "me_stem": "", "null_test_verified": false }
  }
}
```

### Validator Diagnostic Error Trace
```
VALIDATION FAILED: [586] validator-mix-integrated-lufs-and-dbtp-bounds
- ERROR 1: /mix_spec/dialogue_target_lufs: -16.0 violates EBU R128 requirement of -23.0 LUFS (+7.0 LU delta)
- ERROR 2: /mix_spec/true_peak_ceiling_dbtp: +0.8 dBTP exceeds maximum 0.0 dBFS (Digital Inter-Sample Clipping)
VALIDATION FAILED: [588] validator-mix-music-ducking-clearance
- ERROR 3: /music/0/duck_under_dialogue/attenuation_db: 0.0 dB provides zero dialogue clearance (minimum -4.0 dB required)
VALIDATION FAILED: [585] validator-mix-schema-and-stem-completeness
- ERROR 4: /mix_spec/stem_deliverables/null_test_verified is false (Mathematical Stem Parity Failed)
```
