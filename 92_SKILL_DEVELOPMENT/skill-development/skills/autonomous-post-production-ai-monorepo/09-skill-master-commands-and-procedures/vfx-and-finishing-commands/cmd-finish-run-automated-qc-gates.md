---
file_id: "[527]"
command_name: "CMD_FINISH_RUN_AUTOMATED_QC_GATES"
filmcraft_bridge_command: "render.audit_qc"
input_schema_lock: "[029]"
validation_gate: "[591]"
error_code: "ERR_CRITICAL_QC_FAIL"
archetype: "E"
---

# [527] Command Spec: `RUN_AUTOMATED_QC_GATES`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_FINISH_RUN_AUTOMATED_QC_GATES`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `render.audit_qc`
- **Input Parameters**:
  - `master_file_path, standard`
- **Return Artifact**:
  - `file_e_qc_report` (conforming strictly to schema `[029]`)
- **Error Exceptions**:
  - `ERR_CRITICAL_QC_FAIL` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_FINISH_RUN_AUTOMATED_QC_GATES`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[029]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "render.audit_qc",
  "parameters": {
    "inputs": "master_file_path, standard",
    "schema_target": "[029]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (master_file_path, standard).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (file_e_qc_report).
7. Invoke post-condition validator [591].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_CRITICAL_QC_FAIL and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[591]` returns status `pass`.
- Zero violations detected in `file_e_qc_report`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_CRITICAL_QC_FAIL` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[029]` | Re-serialize with strict validator | 1 retry failure |
