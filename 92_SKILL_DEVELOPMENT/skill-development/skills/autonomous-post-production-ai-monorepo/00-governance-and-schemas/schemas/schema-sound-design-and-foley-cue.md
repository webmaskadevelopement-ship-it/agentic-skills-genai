# [024] Schema Lock: Sound Design and Foley Cue Sheet Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[520] CMD_SYNC_FOLEY_CUES`
- **Validation Gate**: `[586] VAL_FOLEY_SYNC`
- **Downstream Consumers**: `[267]` Sound Design, `[306]` Foley & SFX

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/foley-cue-sheet.json",
  "title": "SoundDesignAndFoleyCueSheet",
  "type": "object",
  "additionalProperties": false,
  "required": ["cue_sheet_id", "project_code", "cues"],
  "properties": {
    "cue_sheet_id": { "type": "string" },
    "project_code": { "type": "string" },
    "cues": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["cue_id", "category", "sync_tc", "asset_path", "gain_db", "pan_lr_percent"],
        "properties": {
          "cue_id": { "type": "string" },
          "category": { "type": "string", "enum": ["FOLEY_FOOTSTEPS", "FOLEY_CLOTH", "SFX_HARD", "SFX_BACKGROUND", "SFX_TRANSITION"] },
          "sync_tc": { "type": "string" },
          "asset_path": { "type": "string" },
          "gain_db": { "type": "number", "minimum": -60.0, "maximum": 6.0 },
          "pan_lr_percent": { "type": "integer", "minimum": -100, "maximum": 100 }
        }
      }
    }
  }
}
```
