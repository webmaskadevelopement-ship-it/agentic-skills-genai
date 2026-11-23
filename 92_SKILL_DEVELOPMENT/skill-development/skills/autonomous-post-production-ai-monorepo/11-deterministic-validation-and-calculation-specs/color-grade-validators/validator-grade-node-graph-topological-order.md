---
file_id: "[575]"
validator_name: "VAL_GRADE_TOPOLOGY"
archetype: "G"
validation_type: "Deterministic Python Assertion"
---

# [575] Ensuring Input CST is Node 1 and Output CST + Legal Limiter is final node

## 1. Specification & Contract
- **Validator Identifier**: `VAL_GRADE_TOPOLOGY`
- **Scope**: Deterministic validation of Ensuring Input CST is Node 1 and Output CST + Legal Limiter is final node.
- **Exit State**: Returns strictly `pass`, `warn`, or `fail` with structured violations list.

## 2. Executable Python Implementation
```python
def validate_node_graph_topology(nodes):
    violations = []
    if not nodes or nodes[0].get("node_type") != "INPUT_CST":
        violations.append("Node 1 must be INPUT_CST")
    if nodes and nodes[-1].get("node_type") != "LEGAL_LIMITER":
        violations.append("Final node must be LEGAL_LIMITER")
    status = "fail" if violations else "pass"
    return {"status": status, "violations": violations}
```

## 3. Integration with FilmCraft Auto-Remediation Loop
- If status == `'pass'`: Pipeline advances immediately to next stage gate.
- If status == `'fail'`: Error is caught and dispatched to auto-remediation loop `[012]`.
