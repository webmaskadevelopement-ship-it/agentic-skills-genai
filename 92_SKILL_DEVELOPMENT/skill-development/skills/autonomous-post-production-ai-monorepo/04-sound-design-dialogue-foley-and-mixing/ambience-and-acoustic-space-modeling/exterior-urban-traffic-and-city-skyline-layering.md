---
file_id: "[299]"
skill_name: "exterior-urban-traffic-and-city-skyline-layering"
role: "Craft Decompilation Leaf Skill: Building distant city rumble + intermittent sirens + wind passes"
parent_router: "[297]"
input_schema_lock: "[025] schema-mix-and-loudness-specification.md"
master_command: "[522] CMD_SOUND_EMIT_MIX_SPEC"
parameter_table: "[553] param-table-platform-lufs-lra-and-dbtp-targets.md"
output_validator: "[586] validator-mix-integrated-lufs-and-dbtp-bounds.md"
archetype: "D"
---

# [299] Building distant city rumble + intermittent sirens + wind passes

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_299_EXTERIOR_URBAN_TRAFFIC_AND_CITY_SKYLINE_LAYERING`
- **Parent Sub-Router**: `[297]`
- **Required Upstream Input**: `[025] schema-mix-and-loudness-specification.md`
- **Bound Master Command**: `[522] CMD_SOUND_EMIT_MIX_SPEC`
- **Parameter Reference Table**: `[553] param-table-platform-lufs-lra-and-dbtp-targets.md`
- **Output Validation Gate**: `[586] validator-mix-integrated-lufs-and-dbtp-bounds.md`
- **Domain Cluster**: `Sound Design, Dialogue, Foley & Mixing`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `Building distant city rumble + intermittent sirens + wind passes`.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | LUFS | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
Integrated Loudness $LUFS = -0.691 + 10 \log_{10} \sum G_i z_i$. Dialogue ducking attenuation $G_{duck} \in [-4.0\text{ dB}, -6.0\text{ dB}]$.

### Execution Algorithm
```
1. Ingest input payload conforming to [025] schema-mix-and-loudness-specification.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [553] param-table-platform-lufs-lra-and-dbtp-targets.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to SOUND_MIX_SPECIFICATION.
8. Invoke validation gate [586] validator-mix-integrated-lufs-and-dbtp-bounds.md and verify status == 'pass'.
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
  "file_id": "[299]",
  "evidence_citation": {
    "measured_telemetry": "LUFS, dBTP, dBFS, Hz, Q, ms, RT60",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[553] param-table-platform-lufs-lra-and-dbtp-targets.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Mix audio for broadcast" | "Calibrate integrated loudness to -23.0 LUFS (±0.5 LU) per EBU R128 / ITU-R BS.1770-4, True Peak ceiling <= -1.0 dBTP via 8x oversampled brickwall limiter, Short-Term max <= -18.0 LUFS, LRA = 8.5 LU." |
| "Add reverb for room effect" | "Apply convolution reverb with 0.65s RT60 domestic living room impulse response; pre-delay 12ms, wet/dry mix 18%, high-shelf damping at 3.5 kHz." |
| "Denoise the dialogue track" | "Apply dynamic spectral subtraction with -12dB maximum suppression floor; notch out 60Hz mains hum and 120Hz/180Hz harmonics with Q=10." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[299]",
  "action_executed": "exterior-urban-traffic-and-city-skyline-layering",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "SOUND_MIX_SPECIFICATION"
  },
  "selection_rationale": "Deterministic craft execution complying with Sound Design, Dialogue, Foley & Mixing technical standards."
}
```
