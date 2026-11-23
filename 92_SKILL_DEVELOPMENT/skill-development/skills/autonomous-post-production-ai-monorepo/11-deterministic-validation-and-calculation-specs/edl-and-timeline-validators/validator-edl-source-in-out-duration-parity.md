---
file_id: "[569]"
validator_name: "VAL_EDL_DURATION_PARITY"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [569] Verifying `(source_out - source_in) * speed == (record_out - record_in)`

## 1. Specification & Contract
- **Validator Identifier**: `VAL_EDL_DURATION_PARITY`
- **Scope**: Deterministic validation of Verifying `(source_out - source_in) * speed == (record_out - record_in)`.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_duration_parity(events):
    violations = []
    for idx, ev in enumerate(events):
        src_dur = ev["source_out_frames"] - ev["source_in_frames"]
        rec_dur = ev["record_out_frames"] - ev["record_in_frames"]
        speed = ev.get("speed_ratio", 1.0)
        expected = round(src_dur / speed)
        if rec_dur != expected:
            violations.append(f"Event {idx}: duration parity mismatch (rec={rec_dur}, expected={expected})")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
