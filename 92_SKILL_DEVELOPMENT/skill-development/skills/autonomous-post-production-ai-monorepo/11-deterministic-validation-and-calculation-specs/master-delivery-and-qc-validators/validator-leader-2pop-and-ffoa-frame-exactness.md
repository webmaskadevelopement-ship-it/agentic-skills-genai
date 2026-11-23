---
file_id: "[591]"
validator_name: "VAL_LEADER_2POP"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [591] Verifying 2-pop at 00:59:58:00 and FFOA at 01:00:00:00

## 1. Specification & Contract
- **Validator Identifier**: `VAL_LEADER_2POP`
- **Scope**: Deterministic validation of Verifying 2-pop at 00:59:58:00 and FFOA at 01:00:00:00.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_leader_2pop(leader_events):
    violations = []
    # 2-Pop at exactly 00:59:58:00 (frame duration = 1 frame)
    # FFOA at exactly 01:00:00:00
    if leader_events.get("pop_frame_tc") != "00:59:58:00":
        violations.append(f"2-pop audio sync tone not at 00:59:58:00 (got {leader_events.get('pop_frame_tc')})")
    if leader_events.get("ffoa_tc") != "01:00:00:00":
        violations.append(f"FFOA (First Frame of Action) not at 01:00:00:00 (got {leader_events.get('ffoa_tc')})")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
