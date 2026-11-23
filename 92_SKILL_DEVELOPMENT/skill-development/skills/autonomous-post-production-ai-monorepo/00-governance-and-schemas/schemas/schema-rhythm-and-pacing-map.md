# [018] Schema Lock: Rhythm and Pacing Map Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[498] CMD_MAP_RHYTHM_PACING`
- **Validation Gate**: `[572] VAL_PACING_COHERENCE`
- **Downstream Consumers**: `[126]` Cutting on Beat, `[145]` Scene Pacing

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/pacing-map.json",
  "title": "RhythmAndPacingMap",
  "type": "object",
  "additionalProperties": false,
  "required": ["map_id", "sequence_id", "fps", "bpm_grid", "shots"],
  "properties": {
    "map_id": { "type": "string" },
    "sequence_id": { "type": "string" },
    "fps": { "type": "number" },
    "bpm_grid": {
      "type": "object",
      "required": ["bpm", "meter", "frames_per_beat"],
      "properties": {
        "bpm": { "type": "number", "minimum": 40.0, "maximum": 240.0 },
        "meter": { "type": "string", "enum": ["4/4", "3/4", "6/8"] },
        "frames_per_beat": { "type": "number" }
      }
    },
    "shots": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["shot_index", "duration_frames", "energy_rating_1_to_10", "beat_sync_offset_frames", "cut_type"],
        "properties": {
          "shot_index": { "type": "integer" },
          "duration_frames": { "type": "integer", "minimum": 1 },
          "energy_rating_1_to_10": { "type": "integer", "minimum": 1, "maximum": 10 },
          "beat_sync_offset_frames": { "type": "integer" },
          "cut_type": { "type": "string", "enum": ["HARD_CUT", "J_CUT", "L_CUT", "DISSOLVE"] }
        }
      }
    }
  }
}
```
