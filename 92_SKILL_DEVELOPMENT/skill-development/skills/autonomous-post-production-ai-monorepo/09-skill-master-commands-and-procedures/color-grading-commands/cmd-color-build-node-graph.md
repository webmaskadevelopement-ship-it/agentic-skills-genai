---
file_id: "[499]"
command_name: "CMD_COLOR_BUILD_NODE_GRAPH"
filmcraft_bridge_command: "effects.create_graph"
input_schema_lock: "[019]"
validation_gate: "[575]"
error_code: "ERR_GRAPH_CYCLE_DETECTED"
archetype: "E"
---

# [499] Command Spec: `BUILD_NODE_GRAPH`

## 1. Command Identifier & Typed Signature
- **Command Identifier**: `CMD_COLOR_BUILD_NODE_GRAPH`
- **FilmCraft Bridge Mapping**: Native MCP tool `command_run` with action `effects.create_graph`
- **Input Parameters**:
  - `clip_id, graph_topology`
- **Return Artifact**:
  - `node_graph_manifest` (conforming strictly to schema `[019]`)
- **Error Exceptions**:
  - `ERR_GRAPH_CYCLE_DETECTED` (triggers auto-remediation loop `[012]`)

## 2. Pre-Condition Assertions
Before invoking `CMD_COLOR_BUILD_NODE_GRAPH`:
1. Upstream stage gates verified under `[004] stage-gate-progression-protocol.md`.
2. Input payload conforms to schema `[019]` without validation warnings.
3. FilmCraft control socket verified active via `filmcraft-mcp-bridge.py` on loopback port 9876.
4. Active sequence lock status confirmed.

## 3. Invocation Protocol & FilmCraft Bridge Call
The agent issues execution through the FilmCraft MCP `command_run` interface:
```json
{
  "command": "effects.create_graph",
  "parameters": {
    "inputs": "clip_id, graph_topology",
    "schema_target": "[019]",
    "deterministic_mode": true
  }
}
```

## 4. Deterministic Execution Algorithm
```
1. Receive input tuple (clip_id, graph_topology).
2. Validate non-null boundaries and numerical ranges against Parameter Reference Tables ([530]-[565]).
3. Convert all temporal references to integer frames and 254,016,000,000 FilmCraft ticks.
4. Execute core algorithmic transformation under target domain rules.
5. Record empirical telemetry (IRE scope values, LUFS loudness readings, phoneme millisecond boundaries).
6. Construct candidate output payload (node_graph_manifest).
7. Invoke post-condition validator [575].
8. If status == 'pass', commit to timeline and emit schema-locked deliverable.
9. If status == 'fail', raise ERR_GRAPH_CYCLE_DETECTED and route to auto-remediation loop [012].
```

## 5. Post-Condition Verification
Execution is asserted complete only when:
- `[575]` returns status `pass`.
- Zero violations detected in `node_graph_manifest`.
- Timeline state hash in FilmCraft matches expected state.

## 6. Exception Codes & Fallback Matrix
| Exception Code | Failure Root Cause | Immediate Fallback Action | HITL Escalation Threshold |
|---|---|---|---|
| `ERR_GRAPH_CYCLE_DETECTED` | Parameter violation or execution abort | Apply auto-remediation rule from `[012]` | 3 consecutive failures |
| `ERR_TIMEOUT` | Socket response delayed > 5000ms | Reconnect `filmcraft-mcp-bridge.py` | 1 retry failure |
| `ERR_SCHEMA_MISMATCH` | Emitted JSON deviates from `[019]` | Re-serialize with strict validator | 1 retry failure |
