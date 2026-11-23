---
file_id: "[365]"
skill_name: "forced-narrative-fn-on-screen-text-and-signage"
role: "Craft Decompilation Leaf Skill: Translating plot-critical signs, texts, and newspapers in ALL CAPS"
parent_router: "[360]"
input_schema_lock: "[021] schema-subtitle-timed-text-cue.md"
master_command: "[514] CMD_SUB_EMIT_COMPLIANCE_REPORT"
parameter_table: "[557] param-table-cps-and-cpl-limits-across-40-languages.md"
output_validator: "[580] validator-subtitle-cps-and-cpl-hard-ceilings.md"
archetype: "D"
---

# [365] Translating plot-critical signs, texts, and newspapers in ALL CAPS

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_365_FORCED_NARRATIVE_FN_ON_SCREEN_TEXT_AND_SIGNAGE`
- **Parent Sub-Router**: `[360]`
- **Required Upstream Input**: `[021] schema-subtitle-timed-text-cue.md`
- **Bound Master Command**: `[514] CMD_SUB_EMIT_COMPLIANCE_REPORT`
- **Parameter Reference Table**: `[557] param-table-cps-and-cpl-limits-across-40-languages.md`
- **Output Validation Gate**: `[580] validator-subtitle-cps-and-cpl-hard-ceilings.md`
- **Domain Cluster**: `Subtitling, Captioning & Localization`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `Translating plot-critical signs, texts, and newspapers in ALL CAPS`.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | CPS | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
$CPS = \frac{\text{chars}}{t_{sec}} \le 20.0$. Dead-zone constraint: $t_{in} - t_{cut} \notin [2, 11] \text{ frames}$. Minimum duration $= 833\text{ ms}$.

### Execution Algorithm
```
1. Ingest input payload conforming to [021] schema-subtitle-timed-text-cue.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [557] param-table-cps-and-cpl-limits-across-40-languages.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to SUBTITLE_COMPLIANCE_MANIFEST.
8. Invoke validation gate [580] validator-subtitle-cps-and-cpl-hard-ceilings.md and verify status == 'pass'.
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
  "file_id": "[365]",
  "evidence_citation": {
    "measured_telemetry": "CPS, CPL, ms, frames, characters",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[557] param-table-cps-and-cpl-limits-across-40-languages.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Make subtitles readable" | "Enforce Netflix English SDH standard: CPS <= 20.0, CPL <= 42 chars, max 2 lines, duration bounds [833ms, 7000ms], 2-frame minimum inter-cue gap, and shot-change dead-zone snapping [2..11 frames]." |
| "Break subtitle lines nicely" | "Wrap lines at natural linguistic boundaries: prepositional phrases, commas, and conjunctions; never orphan a single noun on line 2." |
| "Add sound effects subtitles" | "Inject standardized uppercase bracketed SDH descriptors: `[door slashes shut]`, `[suspenseful orchestral swell]`, synchronized within 3 frames of audio transient." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[365]",
  "action_executed": "forced-narrative-fn-on-screen-text-and-signage",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "SUBTITLE_COMPLIANCE_MANIFEST"
  },
  "selection_rationale": "Deterministic craft execution complying with Subtitling, Captioning & Localization technical standards."
}
```
