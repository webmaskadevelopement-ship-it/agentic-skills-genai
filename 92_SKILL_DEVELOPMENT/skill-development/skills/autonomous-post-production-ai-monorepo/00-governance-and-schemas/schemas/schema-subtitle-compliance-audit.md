---
file_id: "[022]"
skill_path: "00-governance-and-schemas/schemas/schema-subtitle-compliance-audit.md"
role: "Master Schema Lock: Subtitle & Timed-Text Compliance Audit (File C)"
parent_router: "[001]"
department_router: "[335]"
master_commands:
  - "SEGMENT_CUES"
  - "CALCULATE_METRICS"
  - "CONDENSE_HIGH_CPS_TEXT"
  - "SNAP_TO_SHOT_CHANGES"
  - "EMIT_COMPLIANCE_REPORT"
validators:
  - "[579]" # validator-subtitle-schema-and-cue-index-order
  - "[580]" # validator-subtitle-cps-and-cpl-hard-ceilings
  - "[581]" # validator-subtitle-duration-floor-and-ceiling
  - "[582]" # validator-subtitle-shot-change-dead-zone-audit
  - "[583]" # validator-subtitle-orphan-words-and-tag-balance
---

# [022] Master Schema Lock: Subtitle & Timed-Text Compliance Audit (File C)

## Block 1: Schema Identity & System Binding

* **Deliverable ID**: File C — Subtitle / Timed-Text Compliance Audit & Metric Sheet.
* **Governing Standard**: Netflix Timed Text Style Guide, BBC Subtitle Guidelines, W3C IMSC1.1, and RFC 8259 JSON.
* **Upstream Generator Commands**: `SEGMENT_CUES` (`[507]`), `CALCULATE_METRICS` (`[508]`), `CONDENSE_HIGH_CPS_TEXT` (`[509]`), `SNAP_TO_SHOT_CHANGES` (`[510]`), `EMIT_COMPLIANCE_REPORT` (`[514]`).
* **Downstream Consumers**:
  - Timed Text Serializers (`[370]` `.srt`, `[371]` `.vtt`, `[372]` `.ttml`).
  - Automated QC Gate 08 (`[451]`).
* **Inspection Validators**: `[579]`, `[580]`, `[581]`, `[582]`, `[583]`, `[584]`.

---

## Block 2: Formal JSON Schema (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://autonomous-post.ai/schemas/subtitle-compliance-audit.json",
  "title": "SubtitleComplianceAudit",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "project",
    "language",
    "delivery_spec",
    "fps",
    "global_metrics",
    "cues"
  ],
  "properties": {
    "project": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
    "language": { "type": "string", "pattern": "^[a-z]{2}(-[A-Z0-9]{2,4})?$" },
    "delivery_spec": { "type": "string", "enum": ["Netflix_Adult_EN", "Netflix_Non_EN", "BBC_Broadcast", "EBU_Standard", "Custom"] },
    "fps": { "type": "number", "enum": [23.976, 24.0, 25.0, 29.97, 30.0, 50.0, 59.94, 60.0] },
    "global_metrics": {
      "type": "object",
      "additionalProperties": false,
      "required": ["total_cues", "avg_cps", "max_cps_observed", "max_cpl_observed", "violations"],
      "properties": {
        "total_cues": { "type": "integer", "minimum": 1 },
        "avg_cps": { "type": "number", "minimum": 5.0, "maximum": 25.0 },
        "max_cps_observed": { "type": "number", "minimum": 5.0, "maximum": 35.0 },
        "max_cpl_observed": { "type": "integer", "minimum": 10, "maximum": 60 },
        "violations": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": ["cue_index", "type", "measured_value", "threshold", "resolution"],
            "properties": {
              "cue_index": { "type": "integer", "minimum": 1 },
              "type": { "type": "string", "enum": ["CPS_EXCEEDED", "CPL_EXCEEDED", "DURATION_TOO_SHORT", "DURATION_TOO_LONG", "SHOT_CHANGE_DEAD_ZONE"] },
              "measured_value": { "type": "number" },
              "threshold": { "type": "number" },
              "resolution": { "type": "string", "minLength": 10 }
            }
          }
        }
      }
    },
    "cues": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "cue_index",
          "in_timecode",
          "out_timecode",
          "duration_ms",
          "text",
          "char_count",
          "cps",
          "cpl",
          "line_count",
          "speaker",
          "style",
          "compliance",
          "issue"
        ],
        "properties": {
          "cue_index": { "type": "integer", "minimum": 1 },
          "in_timecode": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
          "out_timecode": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
          "duration_ms": { "type": "integer", "minimum": 500, "maximum": 10000 },
          "text": { "type": "string", "minLength": 1 },
          "char_count": { "type": "integer", "minimum": 1 },
          "cps": { "type": "number", "minimum": 1.0, "maximum": 40.0 },
          "cpl": { "type": "integer", "minimum": 1, "maximum": 60 },
          "line_count": { "type": "integer", "minimum": 1, "maximum": 2 },
          "speaker": { "type": ["string", "null"] },
          "style": { "type": "string", "enum": ["standard", "sdh", "forced_narrative", "top_an8"] },
          "compliance": { "type": "string", "enum": ["pass", "warn", "fail"] },
          "issue": { "type": ["string", "null"] }
        }
      }
    }
  }
}
```

---

## Block 3: Load-Bearing Evidence Fields

1. `cps` (Characters Per Second):
   - Formula: $\text{CPS} = \text{char\_count} / (\text{duration\_ms} / 1000.0)$.
   - Hard threshold: $\text{CPS} \le 20.0$ for Netflix Adult English. Any value $> 20.0$ marks `"compliance": "fail"`.
2. `cpl` (Characters Per Line):
   - Maximum glyph length among visible lines. Hard ceiling $\le 42$ characters.
3. `line_count`:
   - Maximum 2 lines per cue strictly.

---

## Block 4: Cross-Field Mathematical Invariants

1. **Non-Overlapping Monotonic Timecode Invariant**:
   For adjacent cues $k, k+1$:
   $$\text{to\_ms}(\text{cues}[k+1].\text{in\_timecode}) - \text{to\_ms}(\text{cues}[k].\text{out\_timecode}) \ge \text{round}\left( \frac{2}{fps} \times 1000 \right)$$
   *(Enforces minimum 2-frame blink gap between consecutive subtitles).*
2. **Shot-Change Dead-Zone Snapping**:
   For all cut frame numbers $F_{\text{cut}}$ in File A:
   $$\big| \text{to\_frames}(\text{cue}.\text{in\_timecode}) - F_{\text{cut}} \big| \notin [2..11\text{ frames}]$$
   $$\big| \text{to\_frames}(\text{cue}.\text{out\_timecode}) - F_{\text{cut}} \big| \notin [2..11\text{ frames}]$$

---

## Block 5: Canonical Valid Payload (File C Example)

```json
{
  "project": "APOLLO_11_DOC",
  "language": "en",
  "delivery_spec": "Netflix_Adult_EN",
  "fps": 24.0,
  "global_metrics": {
    "total_cues": 2,
    "avg_cps": 15.6,
    "max_cps_observed": 17.2,
    "max_cpl_observed": 34,
    "violations": []
  },
  "cues": [
    {
      "cue_index": 1,
      "in_timecode": "01:00:00:12",
      "out_timecode": "01:00:03:00",
      "duration_ms": 2500,
      "text": "[ARMSTRONG]\nContact light. Engine stop.",
      "char_count": 39,
      "cps": 15.6,
      "cpl": 27,
      "line_count": 2,
      "speaker": "ARMSTRONG",
      "style": "sdh",
      "compliance": "pass",
      "issue": null
    },
    {
      "cue_index": 2,
      "in_timecode": "01:00:07:08",
      "out_timecode": "01:00:10:14",
      "duration_ms": 3250,
      "text": "Tranquility Base here.\nThe Eagle has landed.",
      "char_count": 44,
      "cps": 13.5,
      "cpl": 23,
      "line_count": 2,
      "speaker": "ARMSTRONG",
      "style": "standard",
      "compliance": "pass",
      "issue": null
    }
  ]
}
```

---

## Block 6: Canonical Invalid Payload & Error Trace

### Invalid Snippet (CPS Exceeded & 3 Lines)
```json
{
  "project": "APOLLO_11_DOC",
  "language": "en",
  "delivery_spec": "Netflix_Adult_EN",
  "fps": 24.0,
  "global_metrics": { "total_cues": 1, "avg_cps": 26.5, "max_cps_observed": 26.5, "max_cpl_observed": 52, "violations": [] },
  "cues": [
    {
      "cue_index": 1,
      "in_timecode": "01:00:00:12",
      "out_timecode": "01:00:02:00",
      "duration_ms": 1500,
      "text": "Houston, Tranquility Base here, the Eagle has landed safely.\nWe copy you down, Eagle.\nYou got a bunch of guys about to turn blue.",
      "char_count": 131,
      "cps": 87.3,
      "cpl": 60,
      "line_count": 3,
      "speaker": "ARMSTRONG",
      "style": "standard",
      "compliance": "pass",
      "issue": null
    }
  ]
}
```

### Validator Diagnostic Error Trace
```
VALIDATION FAILED: [580] validator-subtitle-cps-and-cpl-hard-ceilings
- ERROR 1: /cues/0/cps: 87.3 exceeds platform ceiling 20.0 CPS (Netflix Violation)
- ERROR 2: /cues/0/cpl: 60 exceeds maximum 42 CPL
- ERROR 3: /cues/0/line_count: 3 exceeds maximum 2 lines per cue
REMEDIATION REQUIRED:
- Trigger [509] CONDENSE_HIGH_CPS_TEXT and [507] SEGMENT_CUES to split cue across 2 events.
```
