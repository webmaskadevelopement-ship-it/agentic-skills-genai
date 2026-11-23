---
file_id: "[508]"
command_name: "CMD_SUB_CALCULATE_METRICS"
filmcraft_bridge_command: "subtitle.calculate_metrics"
input_schema_lock: "[022]"
validation_gate: "[580]"
error_code: "ERR_CPS_LIMIT_EXCEEDED"
archetype: "E"
---

# [508] Command Spec: `CALCULATE_METRICS`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SUB_CALCULATE_METRICS`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `subtitle.calculate_metrics`
- **Input Parameters**:
  - `cue_list, fps`
- **Return Artifact**:
  - `metrics_report` (conforming strictly to schema `[022]`)
- **Error Exceptions**:
  - `ERR_CPS_LIMIT_EXCEEDED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SUB_CALCULATE_METRICS`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[022]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "subtitle.calculate_metrics",
  "parameters": {
    "inputs": "cue_list, fps",
    "schema_target": "[022]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (cue_list, fps).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (metrics_report).
7. Invoke post-condition validator [580].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_CPS_LIMIT_EXCEEDED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[580]` returns status `pass`.
- Zero violations detected in `metrics_report`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_CPS_LIMIT_EXCEEDED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[022]` | Re-serialize with strict validator | 1 retry failure |
