---
file_id: "[568]"
validator_name: "VAL_EDL_CONTINUITY"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [568] Verifying `clip[i].record_out == clip[i+1].record_in` across sequence

## 1. Specification & Contract
- **Validator Identifier**: `VAL_EDL_CONTINUITY`
- **Scope**: Deterministic validation of Verifying `clip[i].record_out == clip[i+1].record_in` across sequence.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_edl_continuity(events, fps):
    violations = []
    for i in range(len(events) - 1):
        curr_out = events[i]["record_out_frames"]
        next_in = events[i+1]["record_in_frames"]
        if curr_out != next_in:
            delta = next_in - curr_out
            violations.append(f"Discontinuity between event {i} and {i+1}: delta = {delta} frames")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
