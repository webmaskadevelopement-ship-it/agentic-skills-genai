# [014] Schema Lock: Ingest Metadata and Offload Manifest

## 1. Schema Identity & Binding
- **Emitting Command**: `[480] CMD_INGEST_CAMERA_CARD`
- **Validation Gate**: `[567] VAL_INGEST_MANIFEST_COMPLIANCE`
- **Downstream Consumers**: `[031]` Dailies, `[033]` Proxy Transcode, `[101]` Editorial

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/ingest-manifest.json",
  "title": "IngestMetadataManifest",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "manifest_id",
    "project_code",
    "timestamp_utc",
    "volume_label",
    "total_clips",
    "total_bytes",
    "checksum_algorithm",
    "clips"
  ],
  "properties": {
    "manifest_id": { "type": "string", "pattern": "^ING_[0-9]{8}_[A-Z0-9]+$" },
    "project_code": { "type": "string", "pattern": "^[A-Z0-9_-]{3,16}$" },
    "timestamp_utc": { "type": "string", "format": "date-time" },
    "volume_label": { "type": "string", "minLength": 1 },
    "total_clips": { "type": "integer", "minimum": 1 },
    "total_bytes": { "type": "integer", "minimum": 1 },
    "checksum_algorithm": { "type": "string", "enum": ["MD5", "XXH64", "SHA256"] },
    "clips": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "clip_id",
          "file_name",
          "relative_path",
          "file_size_bytes",
          "checksum",
          "video_format",
          "audio_tracks",
          "timecode"
        ],
        "properties": {
          "clip_id": { "type": "string" },
          "file_name": { "type": "string" },
          "relative_path": { "type": "string" },
          "file_size_bytes": { "type": "integer", "minimum": 1 },
          "checksum": { "type": "string" },
          "video_format": {
            "type": "object",
            "additionalProperties": false,
            "required": ["codec", "width", "height", "fps_numerator", "fps_denominator", "color_space", "transfer_function"],
            "properties": {
              "codec": { "type": "string" },
              "width": { "type": "integer", "minimum": 1280 },
              "height": { "type": "integer", "minimum": 720 },
              "fps_numerator": { "type": "integer", "minimum": 24 },
              "fps_denominator": { "type": "integer", "minimum": 1 },
              "color_space": { "type": "string" },
              "transfer_function": { "type": "string" }
            }
          },
          "audio_tracks": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "required": ["channel_index", "sample_rate_hz", "bit_depth", "channel_layout"],
              "properties": {
                "channel_index": { "type": "integer", "minimum": 0 },
                "sample_rate_hz": { "type": "integer", "enum": [48000, 96000, 192000] },
                "bit_depth": { "type": "integer", "enum": [16, 24, 32] },
                "channel_layout": { "type": "string" }
              }
            }
          },
          "timecode": {
            "type": "object",
            "additionalProperties": false,
            "required": ["start_smpte", "end_smpte", "total_frames"],
            "properties": {
              "start_smpte": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
              "end_smpte": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
              "total_frames": { "type": "integer", "minimum": 1 }
            }
          }
        }
      }
    }
  }
}
```

## 3. Canonical Valid Payload
```json
{
  "manifest_id": "ING_20261024_CARD01",
  "project_code": "FILMCRAFT_PROD",
  "timestamp_utc": "2026-10-24T06:00:00Z",
  "volume_label": "A001_R1AX",
  "total_clips": 1,
  "total_bytes": 4294967296,
  "checksum_algorithm": "XXH64",
  "clips": [
    {
      "clip_id": "A001_C001_1024_001",
      "file_name": "A001_C001_1024AX.MOV",
      "relative_path": "CLIPS/A001_C001_1024AX.MOV",
      "file_size_bytes": 4294967296,
      "checksum": "4f8a3b2c1d0e9f8a",
      "video_format": {
        "codec": "Apple ProRes 422 HQ",
        "width": 3840,
        "height": 2160,
        "fps_numerator": 24000,
        "fps_denominator": 1001,
        "color_space": "Rec.709",
        "transfer_function": "BT.709"
      },
      "audio_tracks": [
        { "channel_index": 0, "sample_rate_hz": 48000, "bit_depth": 24, "channel_layout": "mono_boom" },
        { "channel_index": 1, "sample_rate_hz": 48000, "bit_depth": 24, "channel_layout": "mono_lav1" }
      ],
      "timecode": {
        "start_smpte": "01:00:00:00",
        "end_smpte": "01:02:30:00",
        "total_frames": 3600
      }
    }
  ]
}
```
