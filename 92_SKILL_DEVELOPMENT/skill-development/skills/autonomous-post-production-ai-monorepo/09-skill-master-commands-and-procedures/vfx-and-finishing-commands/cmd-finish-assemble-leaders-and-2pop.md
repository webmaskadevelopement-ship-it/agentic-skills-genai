---
file_id: "[526]"
command_name: "CMD_FINISH_ASSEMBLE_LEADERS_AND_2POP"
filmcraft_bridge_command: "timeline.insert_leaders"
input_schema_lock: "[028]"
validation_gate: "[591]"
error_code: "ERR_2POP_SYNC_MISMATCH"
archetype: "E"
---

# [526] Command Spec: `ASSEMBLE_LEADERS_AND_2POP`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_FINISH_ASSEMBLE_LEADERS_AND_2POP`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `timeline.insert_leaders`
- **Input Parameters**:
  - `timeline_id, head_duration_sec`
- **Return Artifact**:
  - `master_leader_spec` (conforming strictly to schema `[028]`)
- **Error Exceptions**:
  - `ERR_2POP_SYNC_MISMATCH` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_FINISH_ASSEMBLE_LEADERS_AND_2POP`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[028]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "timeline.insert_leaders",
  "parameters": {
    "inputs": "timeline_id, head_duration_sec",
    "schema_target": "[028]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (timeline_id, head_duration_sec).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (master_leader_spec).
7. Invoke post-condition validator [591].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_2POP_SYNC_MISMATCH and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[591]` returns status `pass`.
- Zero violations detected in `master_leader_spec`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_2POP_SYNC_MISMATCH` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[028]` | Re-serialize with strict validator | 1 retry failure |
