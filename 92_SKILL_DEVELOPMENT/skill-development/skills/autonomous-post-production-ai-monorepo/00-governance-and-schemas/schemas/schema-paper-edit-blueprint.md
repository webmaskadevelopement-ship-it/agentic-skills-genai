# [016] Schema Lock: Paper Edit and Assembly Blueprint

## 1. Schema Identity & Binding
- **Emitting Command**: `[488] CMD_GENERATE_PAPER_EDIT`
- **Validation Gate**: `[571] VAL_PAPER_EDIT_STRUCTURE`
- **Downstream Consumers**: `[101]` Rough Assembly, `[103]` Selects Roll

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/paper-edit-blueprint.json",
  "title": "PaperEditBlueprint",
  "type": "object",
  "additionalProperties": false,
  "required": ["blueprint_id", "project_code", "target_runtime_sec", "story_beats", "total_estimated_frames"],
  "properties": {
    "blueprint_id": { "type": "string" },
    "project_code": { "type": "string" },
    "target_runtime_sec": { "type": "number", "minimum": 1.0 },
    "total_estimated_frames": { "type": "integer", "minimum": 24 },
    "story_beats": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["beat_index", "beat_name", "narrative_goal", "selected_clip_id", "source_in_tc", "source_out_tc", "estimated_duration_frames", "selection_rationale"],
        "properties": {
          "beat_index": { "type": "integer", "minimum": 1 },
          "beat_name": { "type": "string" },
          "narrative_goal": { "type": "string" },
          "selected_clip_id": { "type": "string" },
          "source_in_tc": { "type": "string" },
          "source_out_tc": { "type": "string" },
          "estimated_duration_frames": { "type": "integer", "minimum": 1 },
          "selection_rationale": { "type": "string", "minLength": 20 }
        }
      }
    }
  }
}
```
