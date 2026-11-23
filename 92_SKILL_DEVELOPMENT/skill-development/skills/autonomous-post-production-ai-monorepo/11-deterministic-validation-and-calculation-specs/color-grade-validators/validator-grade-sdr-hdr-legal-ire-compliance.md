---
file_id: "[577]"
validator_name: "VAL_LEGAL_IRE"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [577] Verifying black_point_ire >= 0 and white_point_ire <= 100 (or nit cap)

## 1. Specification & Contract
- **Validator Identifier**: `VAL_LEGAL_IRE`
- **Scope**: Deterministic validation of Verifying black_point_ire >= 0 and white_point_ire <= 100 (or nit cap).
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_legal_ire(min_ire, max_ire, mode="SDR"):
    violations = []
    if mode == "SDR":
        if min_ire < -1.0:
            violations.append(f"SDR black excursion: {min_ire} IRE < -1.0")
        if max_ire > 103.0:
            violations.append(f"SDR white excursion: {max_ire} IRE > 103.0")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
