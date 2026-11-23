---
file_id: "[067]"
skill_name: "on-set-asc-cdl-and-show-lut-application"
role: "Craft Decompilation Leaf Skill: Baking Slope/Offset/Power/Saturation + 33x33x33 .cube into proxies"
parent_router: "[063]"
input_schema_lock: "[014] schema-ingest-manifest.md"
master_command: "[480] CMD_INGEST_VERIFY_MEDIA_HASHES"
parameter_table: "[531] param-table-smpte-frame-rates-and-drop-frame-rules.md"
output_validator: "[567] validator-edl-schema-and-required-fields.md"
archetype: "D"
---

# [067] Baking Slope/Offset/Power/Saturation + 33x33x33 .cube into proxies

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_067_ON_SET_ASC_CDL_AND_SHOW_LUT_APPLICATION`
- **Parent Sub-Router**: `[063]`
- **Required Upstream Input**: `[014] schema-ingest-manifest.md`
- **Bound Master Command**: `[480] CMD_INGEST_VERIFY_MEDIA_HASHES`
- **Parameter Reference Table**: `[531] param-table-smpte-frame-rates-and-drop-frame-rules.md`
- **Output Validation Gate**: `[567] validator-edl-schema-and-required-fields.md`
- **Domain Cluster**: `Ingest, Dailies & Assistant Editing`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `Baking Slope/Offset/Power/Saturation + 33x33x33 .cube into proxies`.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | MB/s | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
Throughput $T = \frac{Bytes}{\Delta t \times 10^6} \text{ MB/s}$. Frame ticks = $F \times 10,594,560,000$.

### Execution Algorithm
```
1. Ingest input payload conforming to [014] schema-ingest-manifest.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [531] param-table-smpte-frame-rates-and-drop-frame-rules.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to INGEST_METADATA_MANIFEST.
8. Invoke validation gate [567] validator-edl-schema-and-required-fields.md and verify status == 'pass'.
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
  "file_id": "[067]",
  "evidence_citation": {
    "measured_telemetry": "MB/s, checksum, ticks, frames",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[531] param-table-smpte-frame-rates-and-drop-frame-rules.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Check that footage transferred fine" | "Run xxHash64 bit-for-bit checksum verification against volume label A001_R1AX with 0 byte error tolerance." |
| "Sync audio by waveform roughly" | "Cross-correlate 48kHz PCM dialogue boom against camera scratch audio; align to nearest FilmCraft sub-tick (<0.1ms)." |
| "Organize media in bins" | "Construct standardized ISO taxonomic bin structure: 01_PROJECT_MANAGEMENT, 02_FOOTAGE_CAMERA, 03_AUDIO_STEMS." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[067]",
  "action_executed": "on-set-asc-cdl-and-show-lut-application",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "INGEST_METADATA_MANIFEST"
  },
  "selection_rationale": "Deterministic craft execution complying with Ingest, Dailies & Assistant Editing technical standards."
}
```
