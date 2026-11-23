# [027] Schema Lock: Online Conform Relink Map Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[526] CMD_CONFORM_ONLINE_TIMELINE`
- **Validation Gate**: `[589] VAL_CONFORM_ACCURACY`
- **Downstream Consumers**: `[410]` Finishing, `[420]` Mastering

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/online-conform.json",
  "title": "OnlineConformRelinkMap",
  "type": "object",
  "additionalProperties": false,
  "required": ["conform_id", "offline_edl_hash", "total_events", "relinks"],
  "properties": {
    "conform_id": { "type": "string" },
    "offline_edl_hash": { "type": "string" },
    "total_events": { "type": "integer" },
    "relinks": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["event_index", "proxy_file", "raw_master_file", "tc_match", "scaling_algorithm"],
        "properties": {
          "event_index": { "type": "integer" },
          "proxy_file": { "type": "string" },
          "raw_master_file": { "type": "string" },
          "tc_match": { "type": "boolean" },
          "scaling_algorithm": { "type": "string", "enum": ["LANCZOS3", "BICUBIC_SPLINE"] }
        }
      }
    }
  }
}
```
