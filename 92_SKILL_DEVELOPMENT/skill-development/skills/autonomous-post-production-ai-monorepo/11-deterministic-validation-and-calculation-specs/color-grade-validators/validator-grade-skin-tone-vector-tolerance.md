---
file_id: "[576]"
validator_name: "VAL_SKIN_VECTOR"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [576] Checking skin qualifier output lands within ±4° of vectorscope I-line

## 1. Specification & Contract
- **Validator Identifier**: `VAL_SKIN_VECTOR`
- **Scope**: Deterministic validation of Checking skin qualifier output lands within ±4° of vectorscope I-line.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_skin_vector(skin_angle_deg):
    violations = []
    target = 123.0
    tolerance = 4.0
    if abs(skin_angle_deg - target) > tolerance:
        violations.append(f"Skin tone vector {skin_angle_deg}° deviates > {tolerance}° from 123° I-line")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
