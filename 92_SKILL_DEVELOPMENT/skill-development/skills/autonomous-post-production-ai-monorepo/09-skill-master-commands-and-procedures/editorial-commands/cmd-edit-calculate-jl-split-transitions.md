---
file_id: "[492]"
command_name: "CMD_EDIT_CALCULATE_JL_SPLIT_TRANSITIONS"
filmcraft_bridge_command: "timeline.split_edit"
input_schema_lock: "[017]"
validation_gate: "[572]"
error_code: "ERR_INSUFFICIENT_HANDLES"
archetype: "E"
---

# [492] Command Spec: `CALCULATE_JL_SPLIT_TRANSITIONS`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_EDIT_CALCULATE_JL_SPLIT_TRANSITIONS`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `timeline.split_edit`
- **Input Parameters**:
  - `cut_event_id, split_frames, direction`
- **Return Artifact**:
  - `split_transition_spec` (conforming strictly to schema `[017]`)
- **Error Exceptions**:
  - `ERR_INSUFFICIENT_HANDLES` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_EDIT_CALCULATE_JL_SPLIT_TRANSITIONS`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[017]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "timeline.split_edit",
  "parameters": {
    "inputs": "cut_event_id, split_frames, direction",
    "schema_target": "[017]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (cut_event_id, split_frames, direction).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (split_transition_spec).
7. Invoke post-condition validator [572].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_INSUFFICIENT_HANDLES and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[572]` returns status `pass`.
- Zero violations detected in `split_transition_spec`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_INSUFFICIENT_HANDLES` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[017]` | Re-serialize with strict validator | 1 retry failure |
