---
file_id: "[493]"
command_name: "CMD_EDIT_VERIFY_MURCH_SIX_PRIORITIES"
filmcraft_bridge_command: "timeline.audit_transition"
input_schema_lock: "[017]"
validation_gate: "[572]"
error_code: "ERR_MURCH_WEIGHT_VIOLATION"
archetype: "E"
---

# [493] Command Spec: `VERIFY_MURCH_SIX_PRIORITIES`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_EDIT_VERIFY_MURCH_SIX_PRIORITIES`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `timeline.audit_transition`
- **Input Parameters**:
  - `cut_a, cut_b, murch_weights`
- **Return Artifact**:
  - `six_priority_audit` (conforming strictly to schema `[017]`)
- **Error Exceptions**:
  - `ERR_MURCH_WEIGHT_VIOLATION` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_EDIT_VERIFY_MURCH_SIX_PRIORITIES`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[017]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "timeline.audit_transition",
  "parameters": {
    "inputs": "cut_a, cut_b, murch_weights",
    "schema_target": "[017]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (cut_a, cut_b, murch_weights).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (six_priority_audit).
7. Invoke post-condition validator [572].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_MURCH_WEIGHT_VIOLATION and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[572]` returns status `pass`.
- Zero violations detected in `six_priority_audit`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_MURCH_WEIGHT_VIOLATION` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[017]` | Re-serialize with strict validator | 1 retry failure |
