# [026] Schema Lock: VFX Turnover and Pull Sheet Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[524] CMD_EMIT_VFX_TURNOVER`
- **Validation Gate**: `[588] VAL_VFX_HANDLES`
- **Downstream Consumers**: `[378]` VFX, `[380]` Plate Preparation

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/vfx-turnover.json",
  "title": "VFXTurnoverManifest",
  "type": "object",
  "additionalProperties": false,
  "required": ["turnover_id", "vendor", "handle_frames", "color_space", "shots"],
  "properties": {
    "turnover_id": { "type": "string" },
    "vendor": { "type": "string" },
    "handle_frames": { "type": "integer", "enum": [8, 12, 24] },
    "color_space": { "type": "string", "enum": ["ACEScg", "ACES2065-1", "Linear Rec.709"] },
    "shots": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["vfx_shot_code", "source_file", "head_handle_tc", "cut_in_tc", "cut_out_tc", "tail_handle_tc", "comp_notes"],
        "properties": {
          "vfx_shot_code": { "type": "string", "pattern": "^VFX_[A-Z0-9]+_[0-9]{3,4}$" },
          "source_file": { "type": "string" },
          "head_handle_tc": { "type": "string" },
          "cut_in_tc": { "type": "string" },
          "cut_out_tc": { "type": "string" },
          "tail_handle_tc": { "type": "string" },
          "comp_notes": { "type": "string" }
        }
      }
    }
  }
}
```
