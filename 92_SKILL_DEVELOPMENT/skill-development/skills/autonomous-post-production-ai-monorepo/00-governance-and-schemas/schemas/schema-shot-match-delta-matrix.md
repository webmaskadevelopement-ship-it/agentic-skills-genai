# [020] Schema Lock: Shot Match Delta Matrix Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[508] CMD_MATCH_SHOT_PAIR`
- **Validation Gate**: `[574] VAL_SHOT_MATCH_ERROR`
- **Downstream Consumers**: `[177]` Color Grade, `[206]` Shot Matching

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/shot-match-delta.json",
  "title": "ShotMatchDeltaMatrix",
  "type": "object",
  "additionalProperties": false,
  "required": ["session_id", "hero_shot_id", "target_shot_id", "measured_deltas", "corrective_adjustments"],
  "properties": {
    "session_id": { "type": "string" },
    "hero_shot_id": { "type": "string" },
    "target_shot_id": { "type": "string" },
    "measured_deltas": {
      "type": "object",
      "required": ["exposure_delta_ev", "kelvin_delta", "tint_delta_green_magenta", "skin_chroma_delta_percent"],
      "properties": {
        "exposure_delta_ev": { "type": "number" },
        "kelvin_delta": { "type": "number" },
        "tint_delta_green_magenta": { "type": "number" },
        "skin_chroma_delta_percent": { "type": "number" }
      }
    },
    "corrective_adjustments": {
      "type": "object",
      "required": ["offset_rgb", "lift_rgb", "gain_rgb", "saturation_multiplier"],
      "properties": {
        "offset_rgb": { "type": "array", "items": { "type": "number" }, "minItems": 3, "maxItems": 3 },
        "lift_rgb": { "type": "array", "items": { "type": "number" }, "minItems": 3, "maxItems": 3 },
        "gain_rgb": { "type": "array", "items": { "type": "number" }, "minItems": 3, "maxItems": 3 },
        "saturation_multiplier": { "type": "number", "minimum": 0.0, "maximum": 2.0 }
      }
    }
  }
}
```
