# Skill Development & Editing System Workspace

This workspace houses the complete autonomous post-production intelligence architecture, including the 720-file Autonomous Post-Production Monorepo, the 39-style Editing Taxonomy Templates, and the FilmCraft Native CLI & MCP bridge engine.

## Directory Structure

```
skill-development/
├── blueprints/              # Master specifications and system constitution
│   └── AGENT_INSTRUCTION_SET.md
├── editing-templates/       # 39 Comprehensive Editing Taxonomy Templates
│   ├── INDEX.md             # Master directory & cross-reference guide
│   ├── 01-paradigms/        # Linear, NLE, Offline, Online
│   ├── 02-narrative-styles/ # Continuity, Montage, Classical, Experimental, Narrative, Discontinuous
│   ├── 03-format-genres/    # Doc, Podcast, Vlog, Commercial, Social, Trailer, Reality, Music Video...
│   └── 04-techniques/       # Match cut, Jump cut, Cut on action, J/L cut, Kuleshov, Split screen...
├── skills/
│   ├── _template/           # Professional Post-Production Skill Template (SKILL.md)
│   └── autonomous-post-production-ai-monorepo/ # 720-file Complete Monorepo ([001]-[720])
│       ├── SKILL.md         # Master Root Router & Intent Classifier
│       ├── AGENTS.md        # 7-Persona Swarm Topology & Handoff DAG
│       ├── FILMCRAFT_COMMAND_ROUTING_BRIDGE.md # All 701 FilmCraft commands mapped
│       └── ...              # 15 domain clusters ([001]-[720])
├── scripts/                 # Population, verification, and bridge automation scripts
│   ├── filmcraft_cli_bridge.py
│   └── build_editing_templates.py
├── monorepo.txt             # Authoritative 720-file monorepo blueprint
└── README.md
```

## Core Execution Tools
- **FilmCraft CLI Bridge**: [filmcraft_cli_bridge.py](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/filmcraft_cli_bridge.py)
  - Execute native commands: `python3 filmcraft_cli_bridge.py exec timeline.razor '{"seconds": 10.5}'`
  - Route high-level skills: `python3 filmcraft_cli_bridge.py route CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT`
  - Inspect project/sequence: `python3 filmcraft_cli_bridge.py inspect sequence`
- **Editing Taxonomy Master Index**: [editing-templates/INDEX.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/editing-templates/INDEX.md)
- **FilmCraft Command Routing Guide**: [FILMCRAFT_COMMAND_ROUTING_BRIDGE.md](file:///Volumes/DISK%201/AGENTS%20TRAIN/EDITING_SYSTEM/skill-development/skills/autonomous-post-production-ai-monorepo/FILMCRAFT_COMMAND_ROUTING_BRIDGE.md)

## Workspace Integration
The root `.agents/skills` folder links directly to `skill-development/skills/`. Any skill authored here is automatically discovered and loaded by Antigravity App and Antigravity IDE.
