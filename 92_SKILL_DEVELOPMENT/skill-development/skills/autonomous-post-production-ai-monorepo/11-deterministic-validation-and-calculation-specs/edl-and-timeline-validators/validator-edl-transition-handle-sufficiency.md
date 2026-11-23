---
file_id: "[570]"
validator_name: "VAL_EDL_HANDLES"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [570] Checking source clip bounds support requested J/L and dissolve frames

## 1. Specification & Contract
- **Validator Identifier**: `VAL_EDL_HANDLES`
- **Scope**: Deterministic validation of Checking source clip bounds support requested J/L and dissolve frames.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_transition_handles(events, transition_type, duration_frames):
    violations = []
    half_handle = duration_frames // 2
    for idx, ev in enumerate(events):
        avail_head = ev.get("source_head_handle_frames", 0)
        avail_tail = ev.get("source_tail_handle_frames", 0)
        if avail_head < half_handle:
            violations.append(f"Event {idx}: insufficient head handle ({avail_head} < {half_handle})")
        if avail_tail < half_handle:
            violations.append(f"Event {idx}: insufficient tail handle ({avail_tail} < {half_handle})")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
