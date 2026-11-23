---
file_id: "[517]"
command_name: "CMD_SOUND_SPOT_FOLEY_AND_HARD_SFX"
filmcraft_bridge_command: "audio.place_foley"
input_schema_lock: "[024]"
validation_gate: "[586]"
error_code: "ERR_SFX_SYNC_DRIFT"
archetype: "E"
---

# [517] Command Spec: `SPOT_FOLEY_AND_HARD_SFX`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SOUND_SPOT_FOLEY_AND_HARD_SFX`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `audio.place_foley`
- **Input Parameters**:
  - `sync_points, sfx_library`
- **Return Artifact**:
  - `spotted_sfx_manifest` (conforming strictly to schema `[024]`)
- **Error Exceptions**:
  - `ERR_SFX_SYNC_DRIFT` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SOUND_SPOT_FOLEY_AND_HARD_SFX`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[024]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "audio.place_foley",
  "parameters": {
    "inputs": "sync_points, sfx_library",
    "schema_target": "[024]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (sync_points, sfx_library).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (spotted_sfx_manifest).
7. Invoke post-condition validator [586].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_SFX_SYNC_DRIFT and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[586]` returns status `pass`.
- Zero violations detected in `spotted_sfx_manifest`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_SFX_SYNC_DRIFT` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[024]` | Re-serialize with strict validator | 1 retry failure |
