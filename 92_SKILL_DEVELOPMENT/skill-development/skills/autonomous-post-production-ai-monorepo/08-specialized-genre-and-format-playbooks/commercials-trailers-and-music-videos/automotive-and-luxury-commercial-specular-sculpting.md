---
file_id: "[470]"
skill_name: "automotive-and-luxury-commercial-specular-sculpting"
role: "Craft Decompilation Leaf Skill: Power-window car paint rolling highlights and engine exhaust tuning"
parent_router: "[467]"
input_schema_lock: "[017] schema-edl-cut-manifest.md"
master_command: "[494] CMD_EDIT_PROFILE_RHYTHM_AND_PACING"
parameter_table: "[535] param-table-average-shot-length-benchmarks-by-era.md"
output_validator: "[590] validator-delivery-spec-cross-artifact-consistency.md"
archetype: "D"
---

# [470] Power-window car paint rolling highlights and engine exhaust tuning

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_470_AUTOMOTIVE_AND_LUXURY_COMMERCIAL_SPECULAR_SCULPTING`
- **Parent Sub-Router**: `[467]`
- **Required Upstream Input**: `[017] schema-edl-cut-manifest.md`
- **Bound Master Command**: `[494] CMD_EDIT_PROFILE_RHYTHM_AND_PACING`
- **Parameter Reference Table**: `[535] param-table-average-shot-length-benchmarks-by-era.md`
- **Output Validation Gate**: `[590] validator-delivery-spec-cross-artifact-consistency.md`
- **Domain Cluster**: `Specialized Genre & Format Playbooks`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `Power-window car paint rolling highlights and engine exhaust tuning`.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | ASL sec | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
Genre ASL target modulation: $ASL_{trailer} \in [0.8\text{s}, 1.5\text{s}]$, $ASL_{drama} \in [4.0\text{s}, 6.0\text{s}]$. Safe title zone: 90% action, 80% text.

### Execution Algorithm
```
1. Ingest input payload conforming to [017] schema-edl-cut-manifest.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [535] param-table-average-shot-length-benchmarks-by-era.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to GENRE_PLAYBOOK_SPECIFICATION.
8. Invoke validation gate [590] validator-delivery-spec-cross-artifact-consistency.md and verify status == 'pass'.
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
  "file_id": "[470]",
  "evidence_citation": {
    "measured_telemetry": "ASL sec, energy rating 1-10, safe-area %",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[535] param-table-average-shot-length-benchmarks-by-era.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Edit a punchy promo" | "Build 3-act trailer arc: Act 1 teaser (ASL 3.2s), Act 2 escalation (ASL 1.8s), Act 3 staccato montage (ASL 0.8s) with stereo impact risers." |
| "Format for Instagram Reels" | "Center-crop 16:9 master to 9:16 vertical 1080x1920; position subtitles within 80% vertical safe zone above UI bottom overlay." |
| "Cut documentary interview" | "Anchor narrative on A-roll audio spine; cover cut points with contextual archival B-roll using L-cuts extending 18 frames past sentence pauses." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[470]",
  "action_executed": "automotive-and-luxury-commercial-specular-sculpting",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "GENRE_PLAYBOOK_SPECIFICATION"
  },
  "selection_rationale": "Deterministic craft execution complying with Specialized Genre & Format Playbooks technical standards."
}
```
