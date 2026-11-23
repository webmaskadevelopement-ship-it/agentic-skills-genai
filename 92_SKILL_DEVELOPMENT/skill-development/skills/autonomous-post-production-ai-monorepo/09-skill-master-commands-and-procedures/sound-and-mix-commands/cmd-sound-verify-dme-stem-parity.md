---
file_id: "[521]"
command_name: "CMD_SOUND_VERIFY_DME_STEM_PARITY"
filmcraft_bridge_command: "audio.verify_sum"
input_schema_lock: "[025]"
validation_gate: "[589]"
error_code: "ERR_STEM_SUM_MISMATCH"
archetype: "E"
---

# [521] Command Spec: `VERIFY_DME_STEM_PARITY`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SOUND_VERIFY_DME_STEM_PARITY`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `audio.verify_sum`
- **Input Parameters**:
  - `dx_stem, mx_stem, fx_stem, print_master`
- **Return Artifact**:
  - `parity_audit_report` (conforming strictly to schema `[025]`)
- **Error Exceptions**:
  - `ERR_STEM_SUM_MISMATCH` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SOUND_VERIFY_DME_STEM_PARITY`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[025]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "audio.verify_sum",
  "parameters": {
    "inputs": "dx_stem, mx_stem, fx_stem, print_master",
    "schema_target": "[025]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (dx_stem, mx_stem, fx_stem, print_master).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (parity_audit_report).
7. Invoke post-condition validator [589].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_STEM_SUM_MISMATCH and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[589]` returns status `pass`.
- Zero violations detected in `parity_audit_report`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_STEM_SUM_MISMATCH` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[025]` | Re-serialize with strict validator | 1 retry failure |
