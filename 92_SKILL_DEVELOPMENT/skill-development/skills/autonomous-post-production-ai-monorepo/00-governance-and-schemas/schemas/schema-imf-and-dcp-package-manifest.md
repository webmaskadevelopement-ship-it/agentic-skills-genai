# [030] Schema Lock: IMF and DCP Package Manifest Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[528] CMD_GENERATE_IMF_DCP_PACKAGE`
- **Validation Gate**: `[592] VAL_IMF_DCP_INTEGRITY`
- **Downstream Consumers**: `[410]` Finishing, `[443]` Package Mastering

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/imf-dcp-manifest.json",
  "title": "IMFDCPPackageManifest",
  "type": "object",
  "additionalProperties": false,
  "required": ["package_id", "package_type", "cpl_uuid", "pkl_uuid", "content_title", "assets"],
  "properties": {
    "package_id": { "type": "string" },
    "package_type": { "type": "string", "enum": ["IMF_APP2E", "IMF_APP5", "DCP_SMPTE", "DCP_INTEROP"] },
    "cpl_uuid": { "type": "string", "pattern": "^urn:uuid:[0-9a-fA-F-]{36}$" },
    "pkl_uuid": { "type": "string", "pattern": "^urn:uuid:[0-9a-fA-F-]{36}$" },
    "content_title": { "type": "string" },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["asset_uuid", "asset_type", "file_name", "hash_sha1"],
        "properties": {
          "asset_uuid": { "type": "string" },
          "asset_type": { "type": "string", "enum": ["PICTURE_MXF", "SOUND_MXF", "TIMED_TEXT_XML", "CPL_XML", "PKL_XML"] },
          "file_name": { "type": "string" },
          "hash_sha1": { "type": "string" }
        }
      }
    }
  }
}
```
