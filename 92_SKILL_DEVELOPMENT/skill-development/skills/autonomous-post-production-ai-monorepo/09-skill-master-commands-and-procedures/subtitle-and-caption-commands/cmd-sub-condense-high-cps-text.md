---
file_id: "[509]"
command_name: "CMD_SUB_CONDENSE_HIGH_CPS_TEXT"
filmcraft_bridge_command: "subtitle.condense_text"
input_schema_lock: "[021]"
validation_gate: "[581]"
error_code: "ERR_MEANING_ALTERED"
archetype: "E"
---

# [509] Command Spec: `CONDENSE_HIGH_CPS_TEXT`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SUB_CONDENSE_HIGH_CPS_TEXT`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `subtitle.condense_text`
- **Input Parameters**:
  - `cue_id, target_cps`
- **Return Artifact**:
  - `condensed_cue` (conforming strictly to schema `[021]`)
- **Error Exceptions**:
  - `ERR_MEANING_ALTERED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SUB_CONDENSE_HIGH_CPS_TEXT`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[021]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "subtitle.condense_text",
  "parameters": {
    "inputs": "cue_id, target_cps",
    "schema_target": "[021]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (cue_id, target_cps).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (condensed_cue).
7. Invoke post-condition validator [581].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_MEANING_ALTERED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[581]` returns status `pass`.
- Zero violations detected in `condensed_cue`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_MEANING_ALTERED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[021]` | Re-serialize with strict validator | 1 retry failure |
