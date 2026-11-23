---
file_id: "[520]"
command_name: "CMD_SOUND_CALIBRATE_LUFS_AND_TRUE_PEAK"
filmcraft_bridge_command: "audio.normalize_lufs"
input_schema_lock: "[025]"
validation_gate: "[588]"
error_code: "ERR_LIMITER_DISTORTION"
archetype: "E"
---

# [520] Command Spec: `CALIBRATE_LUFS_AND_TRUE_PEAK`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_SOUND_CALIBRATE_LUFS_AND_TRUE_PEAK`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `audio.normalize_lufs`
- **Input Parameters**:
  - `mix_stem, target_lufs, peak_dbtp`
- **Return Artifact**:
  - `loudness_calibrated_stem` (conforming strictly to schema `[025]`)
- **Error Exceptions**:
  - `ERR_LIMITER_DISTORTION` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_SOUND_CALIBRATE_LUFS_AND_TRUE_PEAK`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[025]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "audio.normalize_lufs",
  "parameters": {
    "inputs": "mix_stem, target_lufs, peak_dbtp",
    "schema_target": "[025]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (mix_stem, target_lufs, peak_dbtp).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (loudness_calibrated_stem).
7. Invoke post-condition validator [588].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_LIMITER_DISTORTION and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[588]` returns status `pass`.
- Zero violations detected in `loudness_calibrated_stem`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_LIMITER_DISTORTION` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[025]` | Re-serialize with strict validator | 1 retry failure |
