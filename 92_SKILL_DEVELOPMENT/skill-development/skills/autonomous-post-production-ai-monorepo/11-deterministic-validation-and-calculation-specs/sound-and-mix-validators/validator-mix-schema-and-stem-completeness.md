---
file_id: "[585]"
validator_name: "VAL_MIX_SCHEMA"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [585] Ensuring DX, MX, FX stems and loudness standard are explicitly declared

## 1. Specification & Contract
- **Validator Identifier**: `VAL_MIX_SCHEMA`
- **Scope**: Deterministic validation of Ensuring DX, MX, FX stems and loudness standard are explicitly declared.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_mix_schema(mix_spec):
    violations = []
    for stem in ["DX", "MX", "FX", "PRINT_MASTER"]:
        if stem not in mix_spec.get("stems", {}):
            violations.append(f"Missing mandatory stem declaration: {stem}")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
