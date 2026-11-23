#!/usr/bin/env python3
"""
Populate all 60 SKILL.md router files across the autonomous post-production monorepo.
Enforces Archetype A & B templates strictly.
"""

import json
import os
import re

ROOT = "/Volumes/DISK 1/AGENTS TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo"

with open(os.path.join(ROOT, "file_catalog.json")) as f:
    catalog = json.load(f)

dir_to_router = {}
for item in catalog:
    if item["file_name"] == "SKILL.md":
        dir_to_router[item["parent_dir"]] = item


def get_parent_router_id(parent_dir):
    if parent_dir == ROOT:
        return "NONE"
    p = os.path.dirname(parent_dir)
    while p and len(p) >= len(ROOT):
        if p in dir_to_router:
            return "[" + dir_to_router[p]["id"] + "]"
        p = os.path.dirname(p)
    return "[001]"


router_children = {}
for item in catalog:
    pdir = item["parent_dir"]
    if pdir in dir_to_router and item["file_name"] != "SKILL.md":
        router_children.setdefault(dir_to_router[pdir]["id"], []).append(item)
    for sdir, srouter in dir_to_router.items():
        if os.path.dirname(sdir) == pdir and sdir != pdir:
            router_children.setdefault(dir_to_router[pdir]["id"], []).append(srouter)

for rid in router_children:
    seen = set()
    unique = []
    for it in sorted(router_children[rid], key=lambda x: int(x["id"])):
        if it["id"] not in seen and it["id"] != rid:
            seen.add(it["id"])
            unique.append(it)
    router_children[rid] = unique

written_count = 0
for rdir, ritem in dir_to_router.items():
    rid = ritem["id"]
    if rid in ["001", "593"]:
        continue  # Already custom-authored

    rpath = ritem["rel_path"]
    rdesc = ritem["description"]
    parent_id = get_parent_router_id(rdir)
    children = router_children.get(rid, [])
    child_ids = ["[" + c["id"] + "]" for c in children]

    is_dept = int(rid) in [
        31, 101, 177, 267, 335, 378, 410, 454, 479, 530, 566, 593, 611, 634, 681
    ]
    role_str = "Department Router" if is_dept else "Sub-Skill Router"

    lines = []
    lines.append("---")
    lines.append(f'file_id: "[{rid}]"')
    lines.append(f'skill_path: "{rpath}"')
    lines.append(f'role: "{role_str}: {rdesc}"')
    lines.append(f'parent_router: "{parent_id}"')
    lines.append("child_nodes:")
    for cid in child_ids:
        lines.append(f'  - "{cid}"')
    lines.append("schema_locks:")
    lines.append('  - "[017]"')
    lines.append('  - "[019]"')
    lines.append('  - "[022]"')
    lines.append('  - "[025]"')
    lines.append('  - "[028]"')
    lines.append("master_commands:")
    lines.append('  - "EMIT_EDL_MANIFEST"')
    lines.append('  - "EMIT_GRADE_SPEC"')
    lines.append('  - "EMIT_COMPLIANCE_REPORT"')
    lines.append('  - "EMIT_MIX_SPEC"')
    lines.append('  - "EMIT_DELIVERY_SPEC"')
    lines.append("validation_gates:")
    lines.append('  - "[566]"')
    lines.append("---")
    lines.append("")
    lines.append(f"# [{rid}] {rdesc}")
    lines.append("")
    lines.append("## 1. Operational Boundary & Anti-Execution Rule")
    lines.append("")
    lines.append(f"This router governs all workflows under `{os.path.dirname(rpath)}`.")
    lines.append(
        "**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. "
        "It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. "
        "It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes."
    )
    lines.append("")
    lines.append("## 2. Intent Classification & Keyword Dispatch Matrix")
    lines.append("")
    lines.append("| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |")
    lines.append("|---|---|---|---|")
    for c in children:
        c_id = c["id"]
        c_name = c["file_name"]
        c_desc = c["description"]
        clean_key = re.sub(r"[^a-zA-Z0-9]+", "|", c_name.replace(".md", ""))
        trigger_regex = f"(?i)({clean_key})"
        lines.append(f"| `{trigger_regex}` | `[{c_id}]` | `{c_name}` | {c_desc} |")
    lines.append("")
    lines.append("## 3. Minimal Context Loading Protocol")
    lines.append("")
    lines.append("When this router activates, the agent MUST load only the minimal leaf subset:")
    lines.append(f"1. Load this router `[{rid}]`.")
    lines.append("2. Identify the target leaf file among child nodes and load exactly 1 to 3 relevant child files.")
    lines.append("3. Load the corresponding Parameter Reference Table from Cluster 10 (`[530]`–`[565]`).")
    lines.append("4. Load the target Schema Lock file from Cluster 00 (`[014]`–`[030]`).")
    lines.append("5. Explicitly declare loaded file IDs at the top of the operational response.")
    lines.append("")
    lines.append("## 4. Stage-Gate Precondition Contract")
    lines.append("")
    lines.append("Before executing tasks routed by this gateway:")
    lines.append("- Upstream stage gates specified in `[004] stage-gate-progression-protocol.md` must record verified status.")
    lines.append("- Any input artifact must pass its mapped schema validation gate before mutation.")
    lines.append("- Timeline modifications must compute frame offsets in integer frames or 254,016,000,000 FilmCraft ticks.")
    lines.append("")
    lines.append("## 5. Evidence-Gated Output Contract")
    lines.append("")
    lines.append("All output emitted under this router must comply with `[005] evidence-gated-reasoning-contract.md`:")
    lines.append("- Cites exact empirical scope values, loudness meters, phoneme timestamps, or frame numbers.")
    lines.append("- Banned phrases ('warm look', 'smooth cut', 'natural mix') result in immediate rejection.")
    lines.append("")
    lines.append("## 6. Escalation & Edge-Case Fallback Table")
    lines.append("")
    lines.append("| Failure Mode | Detection Signature | Escalation Target | Resolution |")
    lines.append("|---|---|---|---|")
    lines.append("| Parameter Out of Bounds | Validator gate status == 'fail' | `[012]` Auto-Remediation | Recalculate parameters |")
    lines.append("| Subjective Aesthetic Ambiguity | Conflicting creative options | `[006]` Taste-Gate | Present 2–3 structured options |")
    lines.append("| Upstream Incomplete Data | Missing input telemetry | `[684]` Studio Defaults | Assign deterministic standard |")
    lines.append("")

    filepath = ritem["abs_path"]
    with open(filepath, "w") as out:
        out.write("\n".join(lines) + "\n")
    written_count += 1

print(f"Successfully populated {written_count} SKILL.md router files!")
