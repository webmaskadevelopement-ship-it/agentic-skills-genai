---
file_id: "[502]"
command_name: "CMD_COLOR_SHAPE_TONAL_CURVES"
filmcraft_bridge_command: "effects.set_curves"
input_schema_lock: "[019]"
validation_gate: "[577]"
error_code: "ERR_NON_INVERTIBLE_CURVE"
archetype: "E"
---

# [502] Command Spec: `SHAPE_TONAL_CURVES`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_COLOR_SHAPE_TONAL_CURVES`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `effects.set_curves`
- **Input Parameters**:
  - `node_id, spline_points`
- **Return Artifact**:
  - `tonal_curve_spec` (conforming strictly to schema `[019]`)
- **Error Exceptions**:
  - `ERR_NON_INVERTIBLE_CURVE` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_COLOR_SHAPE_TONAL_CURVES`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[019]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "effects.set_curves",
  "parameters": {
    "inputs": "node_id, spline_points",
    "schema_target": "[019]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (node_id, spline_points).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (tonal_curve_spec).
7. Invoke post-condition validator [577].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_NON_INVERTIBLE_CURVE and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[577]` returns status `pass`.
- Zero violations detected in `tonal_curve_spec`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_NON_INVERTIBLE_CURVE` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[019]` | Re-serialize with strict validator | 1 retry failure |
