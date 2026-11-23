---
file_id: "[257]"
skill_name: "kodak-portra-400-and-vision3-500t-5219-emulation"
role: "Craft Decompilation Leaf Skill: Negative stock latitude, fine grain structure, and warm midtones"
parent_router: "[253]"
input_schema_lock: "[019] schema-color-grade-specification.md"
master_command: "[506] CMD_COLOR_EMIT_GRADE_SPEC"
parameter_table: "[541] param-table-skin-tone-ire-and-vectorscope-angles.md"
output_validator: "[573] validator-grade-schema-and-scope-evidence.md"
archetype: "D"
---

# [257] Negative stock latitude, fine grain structure, and warm midtones

## Section 1: Header & Dependency Graph
- **Skill Identifier**: `SKILL_257_KODAK_PORTRA_400_AND_VISION3_500T_5219_EMULATION`
- **Parent Sub-Router**: `[253]`
- **Required Upstream Input**: `[019] schema-color-grade-specification.md`
- **Bound Master Command**: `[506] CMD_COLOR_EMIT_GRADE_SPEC`
- **Parameter Reference Table**: `[541] param-table-skin-tone-ire-and-vectorscope-angles.md`
- **Output Validation Gate**: `[573] validator-grade-schema-and-scope-evidence.md`
- **Domain Cluster**: `Color Grading & Look Development`

## Section 2: Craft Decompilation & Physical/Post Principle
This leaf skill codifies the micro-procedural operations of a world-class post-production specialist performing `Negative stock latitude, fine grain structure, and warm midtones`.
In professional finishing, generic human intuition is replaced by rigorous adherence to physical, perceptual, and mathematical standards:
1. **Perceptual Justification**: Human cognitive attention and biological limits dictate boundary constraints (eye saccades take 150–200ms; luminance adaptation requires gradual toe curvature).
2. **Deterministic Reproducibility**: Given identical input telemetry, this skill computes identical cut points, gain offsets, color node coefficients, and timed-text tags across all executions.
3. **FilmCraft Engine Binding**: Every decision is transformed into frame-exact parameters executed through FilmCraft's native loopback socket.

## Section 3: Typed Input Parameters & Default Inference
| Parameter Name | Data Type | Physical Unit | Valid Range | Studio Fallback Default ([684]) |
|---|---|---|---|---|
| `target_timebase` | Float | Frames per second | 23.976, 24.0, 25.0, 29.97, 59.94 | 23.976 fps |
| `primary_metric_level` | Float | IRE | Numerical bounds | Platform standard |
| `temporal_head_offset` | Integer | Integer frames | -48 to +48 frames | 0 frames |
| `tolerance_envelope` | Float | Percent / LU / dB | ±0.5 to ±2.0 | Exact broadcast tolerance |
| `selection_rationale` | String | UTF-8 text | min length 20 chars | Explicit reasoning string |

## Section 4: Deterministic Mathematical & Algorithmic Core
Execution is governed strictly by the following physical formulation:
Printer lights: $Gain = 2^{Points \times 0.025}$. Skin vectorscope centroid: $\theta = 123^\circ \pm 2^\circ$. Code Value $CV_{10} = \text{round}(64 + (IRE / 100) \times 876)$.

### Execution Algorithm
```
1. Ingest input payload conforming to [019] schema-color-grade-specification.md.
2. Check stage-gate status against [004]; halt if upstream dependencies are unverified.
3. Quantize input timestamps to FilmCraft tick resolution (254,016,000,000 ticks/sec).
4. Query [541] param-table-skin-tone-ire-and-vectorscope-angles.md for authoritative physical constants.
5. Compute mathematical transformation matrices (color balance, loudness trim, or cut frames).
6. Verify output candidate against physical safety clamps to prevent clipping or drift.
7. Construct schema-locked output fragment conforming to COLOR_GRADE_SPECIFICATION.
8. Invoke validation gate [573] validator-grade-schema-and-scope-evidence.md and verify status == 'pass'.
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
  "file_id": "[257]",
  "evidence_citation": {
    "measured_telemetry": "IRE, Kelvin, EV stops, degrees (°), code values",
    "applied_correction": "Exact delta value",
    "governing_threshold": "[541] param-table-skin-tone-ire-and-vectorscope-angles.md",
    "verification_status": "PASS"
  }
}
```

## Section 7: Shallow AI Default vs. Production-Grade Execution Table
| Typical Shallow LLM Output (Banned) | Required Autonomous Production Execution (Mandatory) |
|---|---|
| "Apply a warm LUT" | "Node 09 Offset R:+0.012, G:+0.004, B:-0.015; Node 10 Kodak 2383 D60 LUT at 75% blend; Vectorscope skin centroid at 123° I-line, 32% saturation." |
| "Fix exposure on dark shot" | "Apply +1.4 EV linear gain trim ($2^{1.4} = 2.639	ext{x}$) in Node 02; roll off toe below 8 IRE to preserve clean black floor at 64 CV." |
| "Match shot B to shot A" | "Measure middle grey delta (-4.2 IRE) and Kelvin delta (+320K); neutralize with Lift R:-0.004, G:0.000, B:+0.008 and Gain 1.08x." |

## Section 8: Failure Modes, Edge Cases & HITL Triggers
- **Failure Mode 1**: Telemetry input exceeds valid physical range -> Route to auto-remediation loop `[012]`.
- **Failure Mode 2**: Equal-confidence artistic conflict detected -> Trigger human-in-the-loop escalation `[006]`.
- **Failure Mode 3**: Downstream validator `[566]` fails after 3 iterations -> Suspend pipeline and log diagnostic trace.

## Section 9: Schema-Locked Output Fragment
```json
{
  "leaf_skill_id": "[257]",
  "action_executed": "kodak-portra-400-and-vision3-500t-5219-emulation",
  "parameters": {
    "timebase_fps": 23.976,
    "status": "VERIFIED_COMPLIANT",
    "deliverable_type": "COLOR_GRADE_SPECIFICATION"
  },
  "selection_rationale": "Deterministic craft execution complying with Color Grading & Look Development technical standards."
}
```
