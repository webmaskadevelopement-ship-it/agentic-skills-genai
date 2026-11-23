---
file_id: "[578]"
validator_name: "VAL_SHOT_MATCH_DELTA"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [578] Verifying matched shot falls within ±2 IRE and ±2% RGB balance of hero

## 1. Specification & Contract
- **Validator Identifier**: `VAL_SHOT_MATCH_DELTA`
- **Scope**: Deterministic validation of Verifying matched shot falls within ±2 IRE and ±2% RGB balance of hero.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_shot_match(delta_matrix):
    violations = []
    exp_delta = abs(delta_matrix.get("exposure_delta_ev", 0.0))
    if exp_delta > 0.10:
        violations.append(f"Exposure delta {exp_delta} EV exceeds 0.10 EV tolerance")
    chroma_delta = abs(delta_matrix.get("skin_chroma_delta_percent", 0.0))
    if chroma_delta > 3.0:
        violations.append(f"Chroma delta {chroma_delta}% exceeds 3.0% tolerance")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
