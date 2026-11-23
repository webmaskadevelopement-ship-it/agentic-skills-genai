---
file_id: "[487]"
command_name: "CMD_EDIT_DISQUALIFY_FLAWED_TAKES"
filmcraft_bridge_command: "timeline.mark_flaw"
input_schema_lock: "[016]"
validation_gate: "[571]"
error_code: "ERR_ALL_TAKES_DISQUALIFIED"
archetype: "E"
---

# [487] Command Spec: `DISQUALIFY_FLAWED_TAKES`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_EDIT_DISQUALIFY_FLAWED_TAKES`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `timeline.mark_flaw`
- **Input Parameters**:
  - `take_id, flaw_criteria`
- **Return Artifact**:
  - `disqualification_report` (conforming strictly to schema `[016]`)
- **Error Exceptions**:
  - `ERR_ALL_TAKES_DISQUALIFIED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_EDIT_DISQUALIFY_FLAWED_TAKES`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[016]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "timeline.mark_flaw",
  "parameters": {
    "inputs": "take_id, flaw_criteria",
    "schema_target": "[016]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (take_id, flaw_criteria).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (disqualification_report).
7. Invoke post-condition validator [571].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_ALL_TAKES_DISQUALIFIED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[571]` returns status `pass`.
- Zero violations detected in `disqualification_report`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_ALL_TAKES_DISQUALIFIED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[016]` | Re-serialize with strict validator | 1 retry failure |
