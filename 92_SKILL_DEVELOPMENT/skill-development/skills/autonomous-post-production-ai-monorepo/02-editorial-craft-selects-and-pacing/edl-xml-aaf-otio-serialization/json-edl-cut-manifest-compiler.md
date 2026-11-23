---
file_id: "[168]"
skill_name: "json-edl-cut-manifest-compiler"
role: "Craft Decompilation Leaf Skill: Compiling the master JSON EDL with `selection_rationale`"
parent_router: "[167]"
input_schema_lock: "[017] schema-edl-cut-manifest.md"
master_command: "[496] CMD_EDIT_EMIT_EDL_MANIFEST"
parameter_table: "[533] param-table-jl-cut-frame-offset-ranges-by-genre.md"
output_validator: "[568] validator-edl-record-timecode-continuity.md"
archetype: "D"
---

# [168] Compiling the master JSON EDL with `selection_rationale`

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_168_JSON_EDL_CUT_MANIFEST_COMPILER`
- **Parent Sub-Router**: `[167]`
- **Required Upstream Input**: `[017] schema-edl-cut-manifest.md`
- **Bound Master Command**: `[496] CMD_EDIT_EMIT_EDL_MANIFEST`
- **Parameter Reference Table**: `[533] param-table-jl-cut-frame-offset-ranges-by-genre.md`
- **Output Validation Gate**: `[568] validator-edl-record-timecode-continuity.md`
- **Domain Cluster**: `Editorial Craft, Selects & Pacing`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `Compiling the master JSON EDL with `selection_rationale``.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | frames | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
J/L Cut Offset $\Delta F = F_{rec\_in}(audio) - F_{rec\_in}(video) \in [-14, +18]$. ASL $= \frac{\text{TRT}}{\text{Cuts}}$. Eyeline $\Delta y \le 0.05 \times H$.

### Execution Algorithm
```
1. Ingest input payload conforming to [017] schema-edl-cut-manifest.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [533] param-table-jl-cut-frame-offset-ranges-by-genre.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to EDL_CUT_MANIFEST.
8. Invoke validation gate [568] validator-edl-record-timecode-continuity.md and verify status == 'pass'.
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
  "file_id": "[168]",
  "evidence_citation": {
    "measured_telemetry": "frames, ms, BPM, % screen height",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[533] param-table-jl-cut-frame-offset-ranges-by-genre.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Cut to the beat" | "Quantize cut to Bar 14 Beat 1 transient at 01:00:18:12 (120 BPM = 12 frames/beat at 24.000 fps) with -2 frame pre-beat syncopation offset." |
| "Remove filler words and pauses" | "Excise disfluency token 'um' [01:02:14:04 -> 01:02:14:19] at zero-crossing points; bridge 625ms gap with synthesized room tone using 4-frame equal-power crossfades." |
| "Make the pacing faster" | "Reduce Average Shot Length (ASL) from 4.8s to 2.1s; cut on subject head turn to mask 30° jump angle." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[168]",
  "action_executed": "json-edl-cut-manifest-compiler",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "EDL_CUT_MANIFEST"
  },
  "selection_rationale": "Deterministic craft execution complying with Editorial Craft, Selects & Pacing technical standards."
}
```
