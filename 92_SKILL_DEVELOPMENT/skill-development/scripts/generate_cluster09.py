#!/usr/bin/env python3
"""
Populate Cluster 09: Skill Master Commands & Procedures ([480]-[529])
Strictly enforces Archetype E template, deterministic algorithms, and FilmCraft MCP command bindings.
"""

import json
import os
import re

ROOT = "/Volumes/DISK 1/AGENTS TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo"

with open(os.path.join(ROOT, "file_catalog.json")) as f:
    catalog = {item["id"]: item for item in json.load(f)}

# Mapping commands to appropriate FilmCraft native commands and schemas
COMMAND_META = {
    # Ingest (480-485)
    "480": ("CMD_INGEST_VERIFY_MEDIA_HASHES", "media.verify_hash", "[014]", "[567]", "media_path, algorithm", "hash_manifest", "ERR_HASH_MISMATCH"),
    "481": ("CMD_INGEST_PARSE_CAMERA_METADATA", "media.read_metadata", "[014]", "[568]", "clip_path", "clip_metadata_json", "ERR_METADATA_UNREADABLE"),
    "482": ("CMD_INGEST_SYNC_MULTICAM_AND_AUDIO", "timeline.sync_tracks", "[014]", "[569]", "video_clips, audio_stems, method", "sync_map", "ERR_AUDIO_SYNC_FAILED"),
    "483": ("CMD_INGEST_LOAD_TIMED_TRANSCRIPT", "media.import_transcript", "[015]", "[570]", "transcript_file, media_id", "phoneme_alignment", "ERR_ALIGNMENT_DRIFT"),
    "484": ("CMD_INGEST_INDEX_VISUAL_SHOTS", "doc_inspect", "[014]", "[568]", "timeline_id", "shot_catalog", "ERR_INDEXING_FAILED"),
    "485": ("CMD_INGEST_BUILD_NLE_BIN_STRUCTURE", "project.create_bin", "[014]", "[567]", "taxonomy_rule, project_id", "bin_hierarchy", "ERR_BIN_CREATION_FAILED"),
    # Editorial (486-496)
    "486": ("CMD_EDIT_EVALUATE_AND_RANK_TAKES", "sequence_inspect", "[016]", "[571]", "scene_id, take_list", "ranked_takes_manifest", "ERR_NO_VALID_TAKE"),
    "487": ("CMD_EDIT_DISQUALIFY_FLAWED_TAKES", "timeline.mark_flaw", "[016]", "[571]", "take_id, flaw_criteria", "disqualification_report", "ERR_ALL_TAKES_DISQUALIFIED"),
    "488": ("CMD_EDIT_TRIM_SILENT_OPENERS_AND_TAILS", "timeline.razor", "[016]", "[571]", "clip_id, silence_threshold_db", "trimmed_clip_manifest", "ERR_OVER_TRIM"),
    "489": ("CMD_EDIT_GENERATE_PAPER_EDIT", "timeline.assemble_blueprint", "[016]", "[571]", "story_beats, selects_manifest", "paper_edit_json", "ERR_STORY_BEAT_MISSING"),
    "490": ("CMD_EDIT_COMPILE_ASSEMBLY_SEQUENCE", "timeline.place", "[017]", "[572]", "paper_edit_json, target_track", "assembly_manifest", "ERR_ASSEMBLY_GAP_DETECTED"),
    "491": ("CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT", "timeline.ripple_trim", "[017]", "[572]", "sequence_id, pacing_curve", "fine_cut_edl", "ERR_RHYTHM_IRREGULARITY"),
    "492": ("CMD_EDIT_CALCULATE_JL_SPLIT_TRANSITIONS", "timeline.split_edit", "[017]", "[572]", "cut_event_id, split_frames, direction", "split_transition_spec", "ERR_INSUFFICIENT_HANDLES"),
    "493": ("CMD_EDIT_VERIFY_MURCH_SIX_PRIORITIES", "timeline.audit_transition", "[017]", "[572]", "cut_a, cut_b, murch_weights", "six_priority_audit", "ERR_MURCH_WEIGHT_VIOLATION"),
    "494": ("CMD_EDIT_PROFILE_RHYTHM_AND_PACING", "timeline.analyze_pacing", "[018]", "[572]", "sequence_id, target_duration", "pacing_variance_map", "ERR_PACING_OUT_OF_BOUNDS"),
    "495": ("CMD_EDIT_VALIDATE_EDL_TIMECODE_MONOTONICITY", "timeline.verify_tc", "[017]", "[566]", "edl_manifest", "monotonicity_report", "ERR_NON_MONOTONIC_TIMECODE"),
    "496": ("CMD_EDIT_EMIT_EDL_MANIFEST", "timeline.export_edl", "[017]", "[567]", "sequence_id, export_format", "file_a_edl_manifest", "ERR_EDL_EXPORT_FAILED"),
    # Color (497-506)
    "497": ("CMD_COLOR_LOAD_SHOT_METADATA", "media.read_color_metadata", "[019]", "[573]", "clip_id", "color_metadata", "ERR_INVALID_COLOR_METADATA"),
    "498": ("CMD_COLOR_ANALYZE_SCOPES", "render_frame", "[019]", "[574]", "frame_tc, scope_types", "scope_telemetry_data", "ERR_SCOPE_EXTRACTION_FAILED"),
    "499": ("CMD_COLOR_BUILD_NODE_GRAPH", "effects.create_graph", "[019]", "[575]", "clip_id, graph_topology", "node_graph_manifest", "ERR_GRAPH_CYCLE_DETECTED"),
    "500": ("CMD_COLOR_SET_PRIMARY_BALANCE", "effects.set_wheels", "[019]", "[576]", "clip_id, lift, gamma, gain, offset", "primary_balance_spec", "ERR_VALUE_OUT_OF_RANGE"),
    "501": ("CMD_COLOR_APPLY_HSL_QUALIFIER", "effects.set_qualifier", "[019]", "[576]", "node_id, hue_center, hue_width, soft", "qualifier_spec", "ERR_EMPTY_MATTE"),
    "502": ("CMD_COLOR_SHAPE_TONAL_CURVES", "effects.set_curves", "[019]", "[577]", "node_id, spline_points", "tonal_curve_spec", "ERR_NON_INVERTIBLE_CURVE"),
    "503": ("CMD_COLOR_MATCH_TO_REFERENCE", "effects.match_frames", "[020]", "[574]", "source_clip, reference_clip", "shot_match_delta", "ERR_MATCH_ERROR_THRESHOLD_EXCEEDED"),
    "504": ("CMD_COLOR_APPLY_FILM_LOOK_AND_FX", "effects.apply_lut", "[019]", "[578]", "node_id, lut_profile, grain_strength", "look_dev_spec", "ERR_LUT_FILE_NOT_FOUND"),
    "505": ("CMD_COLOR_VALIDATE_GRADE_LEGAL_RANGE", "effects.audit_range", "[019]", "[573]", "clip_id, standard", "legal_range_audit", "ERR_GAMUT_EXCURSION"),
    "506": ("CMD_COLOR_EMIT_GRADE_SPEC", "effects.export_spec", "[019]", "[573]", "sequence_id", "file_b_color_grade_spec", "ERR_GRADE_EMISSION_FAILED"),
    # Subtitles (507-514)
    "507": ("CMD_SUB_SEGMENT_CUES", "subtitle.segment", "[021]", "[579]", "transcript_json, min_ms, max_ms", "segmented_cues_json", "ERR_SEGMENTATION_COLLISION"),
    "508": ("CMD_SUB_CALCULATE_METRICS", "subtitle.calculate_metrics", "[022]", "[580]", "cue_list, fps", "metrics_report", "ERR_CPS_LIMIT_EXCEEDED"),
    "509": ("CMD_SUB_CONDENSE_HIGH_CPS_TEXT", "subtitle.condense_text", "[021]", "[581]", "cue_id, target_cps", "condensed_cue", "ERR_MEANING_ALTERED"),
    "510": ("CMD_SUB_SNAP_TO_SHOT_CHANGES", "subtitle.snap_shot_changes", "[021]", "[582]", "cue_list, cut_events, dead_zone", "snapped_cues_json", "ERR_DEAD_ZONE_VIOLATION"),
    "511": ("CMD_SUB_INJECT_SDH_AND_FN_TAGS", "subtitle.inject_sdh", "[021]", "[583]", "cue_list, sdh_events", "sdh_annotated_cues", "ERR_SDH_SYNTAX_ERROR"),
    "512": ("CMD_SUB_ENFORCE_STANDARD", "subtitle.enforce_standard", "[022]", "[584]", "cue_list, standard_code", "standardized_cues", "ERR_STANDARD_COMPLIANCE_FAILED"),
    "513": ("CMD_SUB_GENERATE_FORMAT", "subtitle.export_file", "[021]", "[579]", "cue_list, format_type", "formatted_timed_text_file", "ERR_SERIALIZATION_FAILED"),
    "514": ("CMD_SUB_EMIT_COMPLIANCE_REPORT", "subtitle.export_report", "[022]", "[580]", "cue_list, ruleset", "file_c_subtitle_compliance_report", "ERR_AUDIT_GENERATION_FAILED"),
    # Sound (515-522)
    "515": ("CMD_SOUND_CLEAN_AND_LEVEL_DIALOGUE", "audio.denoise_and_level", "[023]", "[585]", "dialogue_track, noise_profile", "leveled_dialogue_manifest", "ERR_PHASE_DISTORTION"),
    "516": ("CMD_SOUND_SYNTHESIZE_ROOM_TONE_FILLS", "audio.fill_room_tone", "[023]", "[585]", "gaps_manifest, room_tone_profile", "filled_audio_track", "ERR_FILL_TEXTURE_MISMATCH"),
    "517": ("CMD_SOUND_SPOT_FOLEY_AND_HARD_SFX", "audio.place_foley", "[024]", "[586]", "sync_points, sfx_library", "spotted_sfx_manifest", "ERR_SFX_SYNC_DRIFT"),
    "518": ("CMD_SOUND_LAYER_AMBIENCE_AND_REVERB", "audio.apply_spatial_reverb", "[024]", "[587]", "scene_layout, impulse_response", "layered_ambience_spec", "ERR_IMPULSE_FILE_MISSING"),
    "519": ("CMD_SOUND_ALIGN_MUSIC_AND_DUCKING", "audio.apply_ducking", "[025]", "[587]", "dialogue_stem, music_stem, duck_db", "ducked_music_manifest", "ERR_DUCKING_PUMPING_DETECTED"),
    "520": ("CMD_SOUND_CALIBRATE_LUFS_AND_TRUE_PEAK", "audio.normalize_lufs", "[025]", "[588]", "mix_stem, target_lufs, peak_dbtp", "loudness_calibrated_stem", "ERR_LIMITER_DISTORTION"),
    "521": ("CMD_SOUND_VERIFY_DME_STEM_PARITY", "audio.verify_sum", "[025]", "[589]", "dx_stem, mx_stem, fx_stem, print_master", "parity_audit_report", "ERR_STEM_SUM_MISMATCH"),
    "522": ("CMD_SOUND_EMIT_MIX_SPEC", "audio.export_spec", "[025]", "[588]", "session_id", "file_d_sound_mix_spec", "ERR_MIX_SPEC_FAILED"),
    # VFX & Finishing (523-529)
    "523": ("CMD_VFX_RELINK_AND_CONFORM_RAW", "project.relink_raw", "[027]", "[589]", "offline_edl, raw_dir", "conformed_raw_timeline", "ERR_RAW_FILE_UNRESOLVED"),
    "524": ("CMD_VFX_GENERATE_EXR_PULL_SHEET", "timeline.export_vfx_pulls", "[026]", "[588]", "vfx_shots, handle_frames", "vfx_pull_manifest", "ERR_HANDLE_FRAME_UNDERRUN"),
    "525": ("CMD_FINISH_CONFIGURE_MASTER_CODEC", "render.set_codec_profile", "[028]", "[590]", "codec_name, color_depth, bitrate", "codec_configuration", "ERR_UNSUPPORTED_PROFILE"),
    "526": ("CMD_FINISH_ASSEMBLE_LEADERS_AND_2POP", "timeline.insert_leaders", "[028]", "[591]", "timeline_id, head_duration_sec", "master_leader_spec", "ERR_2POP_SYNC_MISMATCH"),
    "527": ("CMD_FINISH_RUN_AUTOMATED_QC_GATES", "render.audit_qc", "[029]", "[591]", "master_file_path, standard", "file_e_qc_report", "ERR_CRITICAL_QC_FAIL"),
    "528": ("CMD_FINISH_PACKAGE_IMF_OR_DCP", "package.build_distribution", "[030]", "[592]", "cpl_manifest, package_type", "distribution_package_manifest", "ERR_PACKAGE_INTEGRITY_FAIL"),
    "529": ("CMD_FINISH_EMIT_DELIVERY_SPEC", "project.export_delivery_spec", "[028]", "[590]", "project_id, deliverable_code", "file_e_delivery_spec_sheet", "ERR_DELIVERY_SPEC_FAILED")
}

written = 0
for fid, (cmd_name, fc_cmd, schema_lock, val_gate, inputs, output, err_code) in COMMAND_META.items():
    if fid not in catalog:
        continue
    item = catalog[fid]
    filepath = item["abs_path"]
    desc = item["description"]

    content = f"""---
file_id: "[{fid}]"
command_name: "{cmd_name}"
filmcraft_bridge_command: "{fc_cmd}"
input_schema_lock: "{schema_lock}"
validation_gate: "{val_gate}"
error_code: "{err_code}"
archetype: "E"
---

# [{fid}] {desc}

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `{cmd_name}`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `{fc_cmd}`
- **Input Parameters**:
  - `{inputs}`
- **Return Artifact**:
  - `{output}` (conforming strictly to schema `{schema_lock}`)
- **Error Exceptions**:
  - `{err_code}` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `{cmd_name}`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `{schema_lock}` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{{
  "command": "{fc_cmd}",
  "parameters": {{
    "inputs": "{inputs}",
    "schema_target": "{schema_lock}",
    "deterministic_mode": true
  }}
}}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple ({inputs}).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload ({output}).
7. Invoke post-condition validator {val_gate}.
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise {err_code} and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `{val_gate}` returns status `pass`.
- Zero violations detected in `{output}`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `{err_code}` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `{schema_lock}` | Re-serialize with strict validator | 1 retry failure |
"""

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(content.strip() + "\n")
    written += 1
    print("Populated [" + fid + "] " + item["file_name"])

print(f"Cluster 09 population complete: {written} command specification files written.")
