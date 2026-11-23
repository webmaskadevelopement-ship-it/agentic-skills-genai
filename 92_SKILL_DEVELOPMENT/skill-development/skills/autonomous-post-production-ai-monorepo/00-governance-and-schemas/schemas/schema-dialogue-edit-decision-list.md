# [023] Schema Lock: Dialogue Edit Decision List Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[517] CMD_EMIT_DIALOGUE_EDL`
- **Validation Gate**: `[585] VAL_DIALOGUE_INTEGRITY`
- **Downstream Consumers**: `[267]` Sound Design, `[285]` Dialogue Editing

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/dialogue-edl.json",
  "title": "DialogueEditDecisionList",
  "type": "object",
  "additionalProperties": false,
  "required": ["dialogue_edl_id", "track_index", "events"],
  "properties": {
    "dialogue_edl_id": { "type": "string" },
    "track_index": { "type": "integer" },
    "events": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["event_id", "source_clip", "record_in", "record_out", "clip_gain_db", "crossfade_head_frames", "crossfade_tail_frames"],
        "properties": {
          "event_id": { "type": "string" },
          "source_clip": { "type": "string" },
          "record_in": { "type": "string" },
          "record_out": { "type": "string" },
          "clip_gain_db": { "type": "number", "minimum": -60.0, "maximum": 12.0 },
          "crossfade_head_frames": { "type": "integer", "minimum": 2 },
          "crossfade_tail_frames": { "type": "integer", "minimum": 2 },
          "room_tone_fill_applied": { "type": "boolean" }
        }
      }
    }
  }
}
```
