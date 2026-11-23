---
file_id: "[629]"
example_title: "Complete File D exemplar: Trailer DME stem breakdown and LFE hits"
archetype: "H"
cluster: "13-production-grade-golden-examples-and-templates"
---

# [629] Golden Example: Complete File D exemplar: Trailer DME stem breakdown and LFE hits

## 1. Operational Context & Production Brief
This golden exemplar documents an authoritative, real-world post-production artifact representing `Complete File D exemplar: Trailer DME stem breakdown and LFE hits`.
- **Project**: `FILMCRAFT_DEMO_PRODUCTION`
- **Timebase**: `23.976 fps` (NDF, 10,594,560,000 FilmCraft ticks per frame)
- **Active Raster**: `3840 x 2160 UHD` (16:9 1.78:1)
- **Audio Standards**: `EBU R128 / ITU-R BS.1770-4` (-23.0 LUFS ±0.5 LU, -1.0 dBTP ceiling)
- **Color Pipeline**: `ACEScct / ACES AP1` with Rec.709 display transform

## 2. Upstream Input & Raw Telemetry
```json
{
  "input_session_id": "SES_629_PROD",
  "source_media_pool": ["A001_C001_1024AX.MOV", "A001_C002_1024BX.MOV", "DX_BOOM_SC01.WAV"],
  "scene_intent": "Complete File D exemplar: Trailer DME stem breakdown and LFE hits",
  "upstream_gate": "[004] PICTURE_LOCK",
  "measured_parameters": {
    "dialogue_integrated_lufs": -21.4,
    "scene_contrast_ratio": 4.5,
    "average_shot_length_sec": 3.2
  }
}
```

## 3. Algorithmic Reasoning Trace
```
1. Ingest telemetry indicates +1.6 LU offset from target -23.0 LUFS.
2. Calculate broadband dialogue gain trim: Delta_G = -23.0 - (-21.4) = -1.60 dB.
3. Quantize all timeline cuts to Bar/Beat boundary with -2 frame syncopation.
4. Align skin-tone centroid to 123° I-line vectorscope target (measured at 122.8°).
5. Verify subtitle readability against Netflix English standard (CPS <= 20.0, CPL <= 42).
6. Emit complete unabridged artifact.
```

## 4. Complete Production-Grade Output Artifact
```json
{
  "deliverable_type": "GOLDEN_PRODUCTION_ARTIFACT",
  "file_id": "[629]",
  "name": "example-mix-spec-trailer-high-impact-stems-and-lfe.md",
  "version": "1.0.0",
  "compliance_verified": true,
  "metrics": {
    "integrated_lufs": -23.0,
    "true_peak_dbtp": -1.0,
    "max_cps": 17.5,
    "max_cpl": 38,
    "vectorscope_skin_angle_deg": 123.0,
    "middle_grey_ire": 39.0
  },
  "timeline_events": [
    {
      "event_index": 1,
      "source_clip": "A001_C001_1024AX.MOV",
      "source_in": "01:00:10:00",
      "source_out": "01:00:14:12",
      "record_in": "01:00:00:00",
      "record_out": "01:00:04:12",
      "duration_frames": 108,
      "selection_rationale": "Strong character introduction, clear eyeline match on action axis, no disfluency"
    },
    {
      "event_index": 2,
      "source_clip": "A001_C002_1024BX.MOV",
      "source_in": "01:00:05:08",
      "source_out": "01:00:09:20",
      "record_in": "01:00:04:12",
      "record_out": "01:00:09:00",
      "duration_frames": 108,
      "selection_rationale": "Reaction coverage, pupil height matching within 3% tolerance"
    }
  ]
}
```

## 5. Verification Sign-Off
- **Validation Gate**: `[592] VAL_MASTER_QC_SIGNOFF` -> `PASS`
- **Status**: Production-Ready
