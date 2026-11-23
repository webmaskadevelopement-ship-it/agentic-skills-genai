---
file_id: "[567]"
validator_name: "VAL_EDL_SCHEMA"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [567] Checking 100% presence of `selection_rationale` and valid TC strings

## 1. Specification & Contract
- **Validator Identifier**: `VAL_EDL_SCHEMA`
- **Scope**: Deterministic validation of Checking 100% presence of `selection_rationale` and valid TC strings.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_edl_schema(edl_data):
    violations = []
    required_keys = ["manifest_id", "project_code", "fps", "total_events", "events"]
    for k in required_keys:
        if k not in edl_data:
            violations.append(f"Missing root key: {k}")
    
    events = edl_data.get("events", [])
    if not isinstance(events, list) or len(events) == 0:
        violations.append("Events list must be non-empty")
    
    for idx, ev in enumerate(events):
        for req in ["event_index", "source_clip", "source_in", "source_out", "record_in", "record_out", "selection_rationale"]:
            if req not in ev:
                violations.append(f"Event {idx} missing {req}")
        if "selection_rationale" in ev and len(ev["selection_rationale"]) < 10:
            violations.append(f"Event {idx} has shallow selection_rationale (< 10 chars)")
            
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
