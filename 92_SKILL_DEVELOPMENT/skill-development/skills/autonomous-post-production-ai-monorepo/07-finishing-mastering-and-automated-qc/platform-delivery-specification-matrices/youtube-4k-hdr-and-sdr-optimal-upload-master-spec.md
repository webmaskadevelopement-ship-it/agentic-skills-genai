---
file_id: "[433]"
skill_name: "youtube-4k-hdr-and-sdr-optimal-upload-master-spec"
role: "Craft Decompilation Leaf Skill: High-bitrate ProRes/H.264, -14 LUFS, BT.709/PQ tags, and SRT tracks"
parent_router: "[427]"
input_schema_lock: "[028] schema-delivery-and-mastering-spec.md"
master_command: "[529] CMD_FINISH_EMIT_DELIVERY_SPEC"
parameter_table: "[562] param-table-prores-dnxhr-xavc-bitrate-by-raster-fps.md"
output_validator: "[591] validator-leader-2pop-and-ffoa-frame-exactness.md"
archetype: "D"
---

# [433] High-bitrate ProRes/H.264, -14 LUFS, BT.709/PQ tags, and SRT tracks

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_433_YOUTUBE_4K_HDR_AND_SDR_OPTIMAL_UPLOAD_MASTER_SPEC`
- **Parent Sub-Router**: `[427]`
- **Required Upstream Input**: `[028] schema-delivery-and-mastering-spec.md`
- **Bound Master Command**: `[529] CMD_FINISH_EMIT_DELIVERY_SPEC`
- **Parameter Reference Table**: `[562] param-table-prores-dnxhr-xavc-bitrate-by-raster-fps.md`
- **Output Validation Gate**: `[591] validator-leader-2pop-and-ffoa-frame-exactness.md`
- **Domain Cluster**: `Finishing, Mastering & Automated QC`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `High-bitrate ProRes/H.264, -14 LUFS, BT.709/PQ tags, and SRT tracks`.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | Mbps | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
Master leader cadence: 2-Pop at 00:59:58:00 (1 frame 1kHz @ -20dBFS). FFOA at 01:00:00:00. Bitrate: $Mbps \times 3600 / 8000$ GB/hr.

### Execution Algorithm
```
1. Ingest input payload conforming to [028] schema-delivery-and-mastering-spec.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [562] param-table-prores-dnxhr-xavc-bitrate-by-raster-fps.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to DELIVERY_MASTERING_SPEC.
8. Invoke validation gate [591] validator-leader-2pop-and-ffoa-frame-exactness.md and verify status == 'pass'.
```

## Section 5: Step-by-Step Execution Procedure
1. **Initialize Telemetry**: Read source clip parameters and measure active scope/loudness/cadence signals.
2. **Cross-Reference Governance**: Ensure operational envelope does not violate honest limits defined in `[007]`.
3. **Compute Corrective Delta**: Calculate difference between measured state and target specification.
4. **Apply Micro-Trim**: Execute temporal or spectral modification in integer units.
5. **Enforce Crossfade Continuity**: Apply minimum 2-frame equal-power transitions at audio edit points.
6. **Harmonize Metadata**: Write clip metadata, color CDL values, or timed-text cues into timeline manifest.
7. **Run Self-Validation**: Execute local assertion checks before passing artifact to router.

## Section 6: Mandatory Evidence Citation Format
Every decision output emitted by this skill MUST cite concrete numerical evidence:
```json
{
  "file_id": "[433]",
  "evidence_citation": {
    "measured_telemetry": "Mbps, GB/hr, nits, SMPTE TC, UUID",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[562] param-table-prores-dnxhr-xavc-bitrate-by-raster-fps.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Export final video master" | "Encode Apple ProRes 422 HQ 3840x2160 23.976p master with NCLC 1-1-1 QuickTime atom tags and uncompressed 24-bit 48kHz 5.1 + stereo audio." |
| "Build IMF delivery package" | "Author SMPTE ST 2067-2 App 2e IMF package with XML Composition Playlist (CPL), AssetMap, and Packing List (PKL) with SHA-1 checksums." |
| "Run QC check" | "Execute automated Harding FPA flash test (fail on >3 flashes/sec exceeding 20 nits), gamut compliance audit, and audio loudness scan." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[433]",
  "action_executed": "youtube-4k-hdr-and-sdr-optimal-upload-master-spec",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "DELIVERY_MASTERING_SPEC"
  },
  "selection_rationale": "Deterministic craft execution complying with Finishing, Mastering & Automated QC technical standards."
}
```
