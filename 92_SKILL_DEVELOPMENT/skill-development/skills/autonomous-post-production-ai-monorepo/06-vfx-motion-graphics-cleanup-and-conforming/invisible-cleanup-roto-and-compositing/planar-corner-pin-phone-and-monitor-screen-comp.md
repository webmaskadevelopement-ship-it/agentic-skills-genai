---
file_id: "[401]"
skill_name: "planar-corner-pin-phone-and-monitor-screen-comp"
role: "Craft Decompilation Leaf Skill: Sub-pixel Mocha planar tracking with reflection, finger roto & defocus"
parent_router: "[396]"
input_schema_lock: "[026] schema-vfx-turnover-and-pull-sheet.md"
master_command: "[524] CMD_VFX_GENERATE_EXR_PULL_SHEET"
parameter_table: "[546] param-table-halation-and-bloom-radius-by-resolution.md"
output_validator: "[588] validator-mix-music-ducking-clearance.md"
archetype: "D"
---

# [401] Sub-pixel Mocha planar tracking with reflection, finger roto & defocus

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_401_PLANAR_CORNER_PIN_PHONE_AND_MONITOR_SCREEN_COMP`
- **Parent Sub-Router**: `[396]`
- **Required Upstream Input**: `[026] schema-vfx-turnover-and-pull-sheet.md`
- **Bound Master Command**: `[524] CMD_VFX_GENERATE_EXR_PULL_SHEET`
- **Parameter Reference Table**: `[546] param-table-halation-and-bloom-radius-by-resolution.md`
- **Output Validation Gate**: `[588] validator-mix-music-ducking-clearance.md`
- **Domain Cluster**: `VFX, Motion Graphics, Cleanup & Conforming`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `Sub-pixel Mocha planar tracking with reflection, finger roto & defocus`.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | pixels | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
VFX handle frame bounds: $F_{in}' = F_{in} - 12$, $F_{out}' = F_{out} + 12$. Pixel scaling: Lanczos-3 with clamp to legal range.

### Execution Algorithm
```
1. Ingest input payload conforming to [026] schema-vfx-turnover-and-pull-sheet.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [546] param-table-halation-and-bloom-radius-by-resolution.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to VFX_TURNOVER_MANIFEST.
8. Invoke validation gate [588] validator-mix-music-ducking-clearance.md and verify status == 'pass'.
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
  "file_id": "[401]",
  "evidence_citation": {
    "measured_telemetry": "pixels, frames, handles, ACEScg, half-float",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[546] param-table-halation-and-bloom-radius-by-resolution.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Export plates for VFX" | "Generate 16-bit half-float OpenEXR plates in ACEScg color space with 12-frame head/tail handles and embedded camera lens metadata." |
| "Conform proxies to RAW" | "Execute deterministic relink from 1080p ProRes Proxy to 4.5K REDCODE RAW R3D using Reel Name and Source Timecode parity check." |
| "Remove boom mic from frame" | "Track planar patch with Mocha planar solver; clone adjacent clean ceiling texture with Poisson feathering blend over 48 frames." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[401]",
  "action_executed": "planar-corner-pin-phone-and-monitor-screen-comp",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "VFX_TURNOVER_MANIFEST"
  },
  "selection_rationale": "Deterministic craft execution complying with VFX, Motion Graphics, Cleanup & Conforming technical standards."
}
```
