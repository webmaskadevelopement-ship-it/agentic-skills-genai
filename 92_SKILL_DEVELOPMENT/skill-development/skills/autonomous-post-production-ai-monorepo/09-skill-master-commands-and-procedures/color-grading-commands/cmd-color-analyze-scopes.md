---
file_id: "[498]"
command_name: "CMD_COLOR_ANALYZE_SCOPES"
filmcraft_bridge_command: "render_frame"
input_schema_lock: "[019]"
validation_gate: "[574]"
error_code: "ERR_SCOPE_EXTRACTION_FAILED"
archetype: "E"
---

# [498] Command Spec: `ANALYZE_SCOPES`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_COLOR_ANALYZE_SCOPES`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `render_frame`
- **Input Parameters**:
  - `frame_tc, scope_types`
- **Return Artifact**:
  - `scope_telemetry_data` (conforming strictly to schema `[019]`)
- **Error Exceptions**:
  - `ERR_SCOPE_EXTRACTION_FAILED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_COLOR_ANALYZE_SCOPES`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[019]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "render_frame",
  "parameters": {
    "inputs": "frame_tc, scope_types",
    "schema_target": "[019]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (frame_tc, scope_types).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (scope_telemetry_data).
7. Invoke post-condition validator [574].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_SCOPE_EXTRACTION_FAILED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[574]` returns status `pass`.
- Zero violations detected in `scope_telemetry_data`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_SCOPE_EXTRACTION_FAILED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[019]` | Re-serialize with strict validator | 1 retry failure |
