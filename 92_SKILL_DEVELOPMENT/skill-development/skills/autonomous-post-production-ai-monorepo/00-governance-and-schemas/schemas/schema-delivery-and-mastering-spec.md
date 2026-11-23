---
file_id: "[028]"
skill_path: "00-governance-and-schemas/schemas/schema-delivery-and-mastering-spec.md"
role: "Master Schema Lock: Delivery & Mastering Specification (File E)"
parent_router: "[001]"
department_router: "[410]"
master_commands:
  - "CONFIGURE_MASTER_CODEC"
  - "ASSEMBLE_LEADERS_AND_2POP"
  - "RUN_AUTOMATED_QC_GATES"
  - "EMIT_DELIVERY_SPEC"
validators:
  - "[590]" # validator-delivery-spec-cross-artifact-consistency
  - "[591]" # validator-leader-2pop-and-ffoa-frame-exactness
  - "[592]" # validator-master-qc-all-gates-green-signoff
---

# [028] Master Schema Lock: Delivery & Mastering Specification (File E)

## Block 1: Schema Identity & System Binding

* **Deliverable ID**: File E — Master Delivery, Finishing & Automated QC Specification.
* **Governing Standard**: SMPTE ST 2067 (IMF), SMPTE 429 (DCP), ITU-R BT.709/BT.2020, and RFC 8259 JSON.
* **Upstream Generator Commands**: `CONFIGURE_MASTER_CODEC` (`[525]`), `ASSEMBLE_LEADERS_AND_2POP` (`[526]`), `RUN_AUTOMATED_QC_GATES` (`[527]`), `PACKAGE_IMF_OR_DCP` (`[528]`), `EMIT_DELIVERY_SPEC` (`[529]`).
* **Downstream Consumers**: Broadcast playout servers, studio archival vaults, distributor ingest gates.
* **Inspection Validators**: `[590]`, `[591]`, `[592]`.

---

## Block 2: Formal JSON Schema (Draft 2020-12)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://autonomous-post.ai/schemas/delivery-mastering-spec.json",
  "title": "DeliveryMasteringSpec",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "project",
    "master_id",
    "version",
    "platform_target",
    "picture_spec",
    "audio_spec",
    "subtitle_spec",
    "leader_and_sync",
    "qc_gates",
    "master_release_approved"
  ],
  "properties": {
    "project": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
    "master_id": { "type": "string", "pattern": "^[A-Za-z0-9_-]+$" },
    "version": { "type": "string", "pattern": "^v[0-9]{2,3}$" },
    "platform_target": {
      "type": "string",
      "enum": ["Netflix_IMF_HDR", "Theatrical_DCP_4K", "BBC_DPP_AS11", "US_Broadcast_XDCAM", "YouTube_4K_HDR", "Social_9x16_Vertical"]
    },
    "picture_spec": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "resolution",
        "aspect_ratio",
        "frame_rate",
        "color_space",
        "transfer_function",
        "bit_depth",
        "codec",
        "container",
        "nclc_tag"
      ],
      "properties": {
        "resolution": { "type": "string", "pattern": "^[0-9]{3,4}x[0-9]{3,4}$" },
        "aspect_ratio": { "type": "string", "pattern": "^[0-9]+:[0-9]+(\\.[0-9]+)?$" },
        "frame_rate": { "type": "number", "enum": [23.976, 24.0, 25.0, 29.97, 30.0, 50.0, 59.94, 60.0] },
        "color_space": { "type": "string", "enum": ["Rec.709", "DCI-P3", "Rec.2020", "ACEScg"] },
        "transfer_function": { "type": "string", "enum": ["Gamma_2.4", "Gamma_2.2", "Gamma_2.6", "ST.2084_PQ", "BT.2100_HLG"] },
        "bit_depth": { "type": "integer", "enum": [8, 10, 12, 16] },
        "codec": { "type": "string" },
        "container": { "type": "string", "enum": ["mov", "mxf", "mp4", "dcp", "imf"] },
        "nclc_tag": { "type": "string", "pattern": "^[0-9]+-[0-9]+-[0-9]+$" }
      }
    },
    "audio_spec": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "sample_rate_hz",
        "bit_depth",
        "channel_layout",
        "loudness_standard",
        "integrated_lufs",
        "true_peak_dbtp",
        "stems"
      ],
      "properties": {
        "sample_rate_hz": { "type": "integer", "enum": [48000, 96000] },
        "bit_depth": { "type": "integer", "enum": [16, 24, 32] },
        "channel_layout": { "type": "string", "enum": ["Stereo_2.0", "5.1_Surround", "7.1_Surround", "7.1.4_Dolby_Atmos"] },
        "loudness_standard": { "type": "string" },
        "integrated_lufs": { "type": "number" },
        "true_peak_dbtp": { "type": "number", "maximum": 0.0 },
        "stems": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "subtitle_spec": {
      "type": "object",
      "additionalProperties": false,
      "required": ["format", "encoding", "max_cps", "max_cpl", "max_lines", "min_duration_ms"],
      "properties": {
        "format": { "type": "string", "enum": ["srt", "vtt", "imsc1.1_ttml", "ebu_stl", "scc", "burned_in"] },
        "encoding": { "type": "string", "enum": ["UTF-8", "UTF-8_BOM"] },
        "max_cps": { "type": "number", "maximum": 20.0 },
        "max_cpl": { "type": "integer", "maximum": 42 },
        "max_lines": { "type": "integer", "enum": [1, 2] },
        "min_duration_ms": { "type": "integer", "minimum": 833 }
      }
    },
    "leader_and_sync": {
      "type": "object",
      "additionalProperties": false,
      "required": ["head_2pop_tc", "ffoa_tc", "lfoa_tc", "tail_2pop_tc"],
      "properties": {
        "head_2pop_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
        "ffoa_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
        "lfoa_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" },
        "tail_2pop_tc": { "type": "string", "pattern": "^[0-9]{2}:[0-9]{2}:[0-9]{2}[:;][0-9]{2}$" }
      }
    },
    "qc_gates": {
      "type": "array",
      "minItems": 9,
      "maxItems": 9,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["gate_id", "gate_name", "threshold", "measured_value", "status"],
        "properties": {
          "gate_id": { "type": "string", "pattern": "^GATE_[0-9]{2}$" },
          "gate_name": { "type": "string" },
          "threshold": { "type": "string" },
          "measured_value": { "type": "string" },
          "status": { "type": "string", "enum": ["pass", "fail"] }
        }
      }
    },
    "master_release_approved": { "type": "boolean" }
  }
}
```

---

## Block 3: Load-Bearing Evidence Fields

1. `qc_gates` (The 9 Automated Gates):
   - Exactly 9 gates required (`GATE_01` through `GATE_09`).
   - Every gate MUST record `"status": "pass"`. A single `"status": "fail"` blocks `master_release_approved` via `[592]`.
2. `leader_and_sync`:
   - Exact timecode frame anchoring: `head_2pop_tc` at `00:59:58:00` and `ffoa_tc` at `01:00:00:00`.

---

## Block 4: Cross-Field Mathematical Invariants

1. **2-Pop Sync Offset**:
   $$\text{to\_frames}(\text{ffoa\_tc}) - \text{to\_frames}(\text{head\_2pop\_tc}) \equiv 48\text{ frames (at 24.000 fps)} \equiv 2.000\text{ seconds}$$
2. **Master Release Blocker**:
   $$\text{master\_release\_approved} \equiv \big( \forall g \in \text{qc\_gates}: g.\text{status} == \text{"pass"} \big)$$

---

## Block 5: Canonical Valid Payload (File E Example)

```json
{
  "project": "APOLLO_11_DOC",
  "master_id": "APOLLO11_EP01_MASTER",
  "version": "v01",
  "platform_target": "BBC_DPP_AS11",
  "picture_spec": {
    "resolution": "1920x1080",
    "aspect_ratio": "16:9",
    "frame_rate": 25.0,
    "color_space": "Rec.709",
    "transfer_function": "Gamma_2.4",
    "bit_depth": 10,
    "codec": "Apple ProRes 422 HQ",
    "container": "mov",
    "nclc_tag": "1-1-1"
  },
  "audio_spec": {
    "sample_rate_hz": 48000,
    "bit_depth": 24,
    "channel_layout": "Stereo_2.0",
    "loudness_standard": "EBU_R128",
    "integrated_lufs": -23.0,
    "true_peak_dbtp": -1.0,
    "stems": ["DX_Stem.wav", "MX_Stem.wav", "FX_Stem.wav"]
  },
  "subtitle_spec": {
    "format": "ebu_stl",
    "encoding": "UTF-8",
    "max_cps": 17.0,
    "max_cpl": 37,
    "max_lines": 2,
    "min_duration_ms": 1000
  },
  "leader_and_sync": {
    "head_2pop_tc": "09:59:58:00",
    "ffoa_tc": "10:00:00:00",
    "lfoa_tc": "10:00:11:20",
    "tail_2pop_tc": "10:00:13:20"
  },
  "qc_gates": [
    { "gate_id": "GATE_01", "gate_name": "Harding PSE Flash Test", "threshold": "< 3 flashes/s", "measured_value": "0 flashes detected", "status": "pass" },
    { "gate_id": "GATE_02", "gate_name": "Broadcast Legal Gamut", "threshold": "0–100 IRE", "measured_value": "Min 3.4 IRE, Max 94.2 IRE", "status": "pass" },
    { "gate_id": "GATE_03", "gate_name": "Unintended Black Frames", "threshold": "0 frames", "measured_value": "0 black gaps detected", "status": "pass" },
    { "gate_id": "GATE_04", "gate_name": "Dropped & Freeze Frames", "threshold": "0 frames", "measured_value": "Continuous motion parity confirmed", "status": "pass" },
    { "gate_id": "GATE_05", "gate_name": "Audio True Peak & Clip", "threshold": "<= -1.0 dBTP", "measured_value": "-1.0 dBTP peak, 0 overs", "status": "pass" },
    { "gate_id": "GATE_06", "gate_name": "Lip-Sync Drift", "threshold": "-15ms to +45ms", "measured_value": "0.0ms drift at clapper/phoneme", "status": "pass" },
    { "gate_id": "GATE_07", "gate_name": "Clipped Spoken Words", "threshold": "0 occurrences", "measured_value": "All cuts clear phoneme boundaries", "status": "pass" },
    { "gate_id": "GATE_08", "gate_name": "Subtitle CPS & Safe Area", "threshold": "<= 17.0 CPS, Safe >= 90%", "measured_value": "Max 15.6 CPS, Safe 92.5%", "status": "pass" },
    { "gate_id": "GATE_09", "gate_name": "Naming & Hash Verification", "threshold": "xxHash64 Parity", "measured_value": "Hash match verified", "status": "pass" }
  ],
  "master_release_approved": true
}
```

---

## Block 6: Canonical Invalid Payload & Error Trace

### Invalid Snippet (Failing Gate 05 & Unapproved Release)
```json
{
  "project": "APOLLO_11_DOC",
  "master_id": "APOLLO11_EP01_MASTER",
  "version": "v01",
  "platform_target": "BBC_DPP_AS11",
  "picture_spec": { "resolution": "1920x1080", "aspect_ratio": "16:9", "frame_rate": 25.0, "color_space": "Rec.709", "transfer_function": "Gamma_2.4", "bit_depth": 10, "codec": "ProRes", "container": "mov", "nclc_tag": "1-1-1" },
  "audio_spec": { "sample_rate_hz": 48000, "bit_depth": 24, "channel_layout": "Stereo_2.0", "loudness_standard": "EBU_R128", "integrated_lufs": -21.0, "true_peak_dbtp": +0.4, "stems": [] },
  "subtitle_spec": { "format": "srt", "encoding": "UTF-8", "max_cps": 20.0, "max_cpl": 42, "max_lines": 2, "min_duration_ms": 1000 },
  "leader_and_sync": { "head_2pop_tc": "09:59:58:00", "ffoa_tc": "10:00:00:00", "lfoa_tc": "10:00:10:00", "tail_2pop_tc": "10:00:12:00" },
  "qc_gates": [
    { "gate_id": "GATE_01", "gate_name": "Harding PSE", "threshold": "pass", "measured_value": "pass", "status": "pass" },
    { "gate_id": "GATE_02", "gate_name": "Gamut", "threshold": "pass", "measured_value": "pass", "status": "pass" },
    { "gate_id": "GATE_03", "gate_name": "Blacks", "threshold": "pass", "measured_value": "pass", "status": "pass" },
    { "gate_id": "GATE_04", "gate_name": "Freeze", "threshold": "pass", "measured_value": "pass", "status": "pass" },
    { "gate_id": "GATE_05", "gate_name": "Audio Overs", "threshold": "<= -1.0 dBTP", "measured_value": "+0.4 dBTP", "status": "fail" },
    { "gate_id": "GATE_06", "gate_name": "Lip-Sync", "threshold": "pass", "measured_value": "pass", "status": "pass" },
    { "gate_id": "GATE_07", "gate_name": "Clipped Words", "threshold": "pass", "measured_value": "pass", "status": "pass" },
    { "gate_id": "GATE_08", "gate_name": "Subtitles", "threshold": "pass", "measured_value": "pass", "status": "pass" },
    { "gate_id": "GATE_09", "gate_name": "Naming", "threshold": "pass", "measured_value": "pass", "status": "pass" }
  ],
  "master_release_approved": true
}
```

### Validator Diagnostic Error Trace
```
VALIDATION FAILED: [592] validator-master-qc-all-gates-green-signoff
- ERROR 1: GATE_05 status is "fail": measured True Peak +0.4 dBTP exceeds -1.0 dBTP ceiling.
- ERROR 2: Invariant Violation: master_release_approved cannot be true while any QC gate fails.
RELEASE BLOCKED:
- Downstream delivery package halted. Route to [520] CALIBRATE_LUFS_AND_TRUE_PEAK to apply brickwall limiting.
```
