# [029] Schema Lock: Automated QC Gate Report Specification

## 1. Schema Identity & Binding
- **Emitting Command**: `[529] CMD_AUDIT_FINAL_DELIVERABLE`
- **Validation Gate**: `[591] VAL_DELIVERY_SPEC_COMPLIANCE`
- **Downstream Consumers**: `[410]` Finishing & QC

## 2. Formal JSON Schema (Draft 2020-12)
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://filmcraft.ai/schemas/qc-report.json",
  "title": "AutomatedQCGateReport",
  "type": "object",
  "additionalProperties": false,
  "required": ["report_id", "file_inspected", "overall_status", "loudness_audit", "video_audit", "timed_text_audit"],
  "properties": {
    "report_id": { "type": "string" },
    "file_inspected": { "type": "string" },
    "overall_status": { "type": "string", "enum": ["PASS", "WARN", "FAIL"] },
    "loudness_audit": {
      "type": "object",
      "required": ["integrated_lufs", "true_peak_dbtp", "lra_lu", "status"],
      "properties": {
        "integrated_lufs": { "type": "number" },
        "true_peak_dbtp": { "type": "number" },
        "lra_lu": { "type": "number" },
        "status": { "type": "string", "enum": ["PASS", "FAIL"] }
      }
    },
    "video_audit": {
      "type": "object",
      "required": ["gamut_error_count", "flash_frames_detected", "pse_harding_pass", "status"],
      "properties": {
        "gamut_error_count": { "type": "integer" },
        "flash_frames_detected": { "type": "integer" },
        "pse_harding_pass": { "type": "boolean" },
        "status": { "type": "string", "enum": ["PASS", "FAIL"] }
      }
    },
    "timed_text_audit": {
      "type": "object",
      "required": ["cps_violations", "cpl_violations", "overlap_errors", "status"],
      "properties": {
        "cps_violations": { "type": "integer" },
        "cpl_violations": { "type": "integer" },
        "overlap_errors": { "type": "integer" },
        "status": { "type": "string", "enum": ["PASS", "FAIL"] }
      }
    }
  }
}
```
