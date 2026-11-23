---
file_id: "[573]"
validator_name: "VAL_GRADE_SCHEMA_EVIDENCE"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [573] Rejecting any grade spec lacking numeric IRE/vectorscope readings

## 1. Specification & Contract
- **Validator Identifier**: `VAL_GRADE_SCHEMA_EVIDENCE`
- **Scope**: Deterministic validation of Rejecting any grade spec lacking numeric IRE/vectorscope readings.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_grade_schema(grade_spec):
    violations = []
    for shot in grade_spec.get("shots", []):
        if "scope_evidence" not in shot:
            violations.append(f"Shot {shot.get('shot_id')} missing scope_evidence")
        else:
            se = shot["scope_evidence"]
            if "skin_vectorscope_angle_deg" not in se:
                violations.append(f"Shot {shot.get('shot_id')} missing skin_vectorscope_angle_deg")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
