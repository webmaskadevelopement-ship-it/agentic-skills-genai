---
file_id: "[504]"
command_name: "CMD_COLOR_APPLY_FILM_LOOK_AND_FX"
filmcraft_bridge_command: "effects.apply_lut"
input_schema_lock: "[019]"
validation_gate: "[578]"
error_code: "ERR_LUT_FILE_NOT_FOUND"
archetype: "E"
---

# [504] Command Spec: `APPLY_FILM_LOOK_AND_FX`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_COLOR_APPLY_FILM_LOOK_AND_FX`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `effects.apply_lut`
- **Input Parameters**:
  - `node_id, lut_profile, grain_strength`
- **Return Artifact**:
  - `look_dev_spec` (conforming strictly to schema `[019]`)
- **Error Exceptions**:
  - `ERR_LUT_FILE_NOT_FOUND` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_COLOR_APPLY_FILM_LOOK_AND_FX`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[019]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "effects.apply_lut",
  "parameters": {
    "inputs": "node_id, lut_profile, grain_strength",
    "schema_target": "[019]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (node_id, lut_profile, grain_strength).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (look_dev_spec).
7. Invoke post-condition validator [578].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_LUT_FILE_NOT_FOUND and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[578]` returns status `pass`.
- Zero violations detected in `look_dev_spec`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_LUT_FILE_NOT_FOUND` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[019]` | Re-serialize with strict validator | 1 retry failure |
