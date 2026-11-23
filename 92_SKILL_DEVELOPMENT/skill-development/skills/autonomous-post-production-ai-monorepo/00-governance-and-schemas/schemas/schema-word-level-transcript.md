# [015] Schema Lock: Word-Level Transcript and Phoneme Alignment Manifest

## 1. Schema Identity & Binding
- **Emitting Command**: `[484] CMD_ALIGN_PHONEMES`
- **Validation Gate**: `[570] VAL_TRANSCRIPT_ALIGNMENT`
- **Downstream Consumers**: `[101]` Paper Edit, `[116]` Dialogue Trimming, `[335]` Subtitling

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/transcript-manifest.json",
  "title": "WordLevelTranscriptManifest",
  "type": "object",
  "additionalProperties": false,
  "required": ["transcript_id", "clip_id", "language", "speakers", "words"],
  "properties": {
    "transcript_id": { "type": "string" },
    "clip_id": { "type": "string" },
    "language": { "type": "string", "pattern": "^[a-z]{2,3}(-[A-Z]{2})?$" },
    "speakers": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["speaker_id", "label"],
        "properties": {
          "speaker_id": { "type": "string" },
          "label": { "type": "string" }
        }
      }
    },
    "words": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["word", "start_ms", "end_ms", "start_frame", "end_frame", "speaker_id", "confidence"],
        "properties": {
          "word": { "type": "string" },
          "start_ms": { "type": "integer", "minimum": 0 },
          "end_ms": { "type": "integer", "minimum": 0 },
          "start_frame": { "type": "integer", "minimum": 0 },
          "end_frame": { "type": "integer", "minimum": 0 },
          "speaker_id": { "type": "string" },
          "confidence": { "type": "number", "minimum": 0.0, "maximum": 1.0 },
          "is_disfluency": { "type": "boolean" },
          "phonemes": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["ipa_symbol", "start_ms", "end_ms"],
              "properties": {
                "ipa_symbol": { "type": "string" },
                "start_ms": { "type": "integer" },
                "end_ms": { "type": "integer" }
              }
            }
          }
        }
      }
    }
  }
}
```

## 3. Mathematical Invariant
For every word item $k$:
$$start\_ms(k) < end\_ms(k)$$
$$start\_frame(k) = 	ext{round}\left(rac{start\_ms(k)}{1000} 	imes 	ext{fps}ight)$$
$$end\_frame(k) = 	ext{round}\left(rac{end\_ms(k)}{1000} 	imes 	ext{fps}ight)$$
