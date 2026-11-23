# [021] Schema Lock: Subtitle Timed-Text Cue Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[513] CMD_EMIT_SUBTITLE_CUES`
- **Validation Gate**: `[580] VAL_SUBTITLE_CUE_INTEGRITY`
- **Downstream Consumers**: `[335]` Subtitling, `[410]` Finishing

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/subtitle-timed-text-cue.json",
  "title": "SubtitleTimedTextCueList",
  "type": "object",
  "additionalProperties": false,
  "required": ["manifest_id", "language_code", "fps", "cues"],
  "properties": {
    "manifest_id": { "type": "string" },
    "language_code": { "type": "string" },
    "fps": { "type": "number" },
    "cues": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["cue_index", "start_tc", "end_tc", "duration_ms", "cps", "lines"],
        "properties": {
          "cue_index": { "type": "integer", "minimum": 1 },
          "start_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
          "end_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
          "duration_ms": { "type": "integer", "minimum": 833, "maximum": 7000 },
          "cps": { "type": "number", "maximum": 20.0 },
          "lines": {
            "type": "array",
            "minItems": 1,
            "maxItems": 2,
            "items": { "type": "string", "maxLength": 42 }
          }
        }
      }
    }
  }
}
```
