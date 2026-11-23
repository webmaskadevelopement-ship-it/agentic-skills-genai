---
file_id: "[297]"
skill_path: "04-sound-design-dialogue-foley-and-mixing/ambience-and-acoustic-space-modeling/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Backgrounds, Room Tones & Convolution Reverb"
parent_router: "[267]"
child_nodes:
  - "[298]"
  - "[299]"
  - "[300]"
  - "[301]"
  - "[302]"
  - "[303]"
  - "[304]"
  - "[305]"
schema_locks:
  - "[017]"
  - "[019]"
  - "[022]"
  - "[025]"
  - "[028]"
master_commands:
  - "EMIT_EDL_MANIFEST"
  - "EMIT_GRADE_SPEC"
  - "EMIT_COMPLIANCE_REPORT"
  - "EMIT_MIX_SPEC"
  - "EMIT_DELIVERY_SPEC"
validation_gates:
  - "[566]"
---

# [297] Sub-Router: Backgrounds, Room Tones & Convolution Reverb

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `04-sound-design-dialogue-foley-and-mixing/ambience-and-acoustic-space-modeling`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(interior|room|tone|acoustic|signature|taxonomy)` | `[298]` | `interior-room-tone-acoustic-signature-taxonomy.md` | Selecting quiet residential, fluorescent office, or warehouse air beds |
| `(?i)(exterior|urban|traffic|and|city|skyline|layering)` | `[299]` | `exterior-urban-traffic-and-city-skyline-layering.md` | Building distant city rumble + intermittent sirens + wind passes |
| `(?i)(exterior|nature|wind|foliage|and|fauna|beds)` | `[300]` | `exterior-nature-wind-foliage-and-fauna-beds.md` | Avoiding repetitive bird loops via polyrhythmic stem offsetting |
| `(?i)(weather|rain|thunder|and|storm|intensity|scaling)` | `[301]` | `weather-rain-thunder-and-storm-intensity-scaling.md` | Matching acoustic rain density to visual droplet size on lens/ground |
| `(?i)(crowd|walla|and|background|chatter|density|control)` | `[302]` | `crowd-walla-and-background-chatter-density-control.md` | Ensuring background walla contains zero intelligible distracting words |
| `(?i)(scene|boundary|ambience|checkerboarding|and|fades)` | `[303]` | `scene-boundary-ambience-checkerboarding-and-fades.md` | Hard-cutting or micro-fading BG stems precisely on visual scene cuts |
| `(?i)(impulse|response|convolution|reverb|space|matching)` | `[304]` | `impulse-response-convolution-reverb-space-matching.md` | Selecting IR spaces (car, bathroom, alley, hall) matching camera lens |
| `(?i)(pre|delay|and|early|reflection|depth|positioning)` | `[305]` | `pre-delay-and-early-reflection-depth-positioning.md` | Shortening pre-delay to push background elements deeper into the screen |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[297]`.
2. Identify the target leaf file among child nodes and load exactly 1 to 3 relevant child files.
3. Load the corresponding Parameter Reference Table from Cluster 10 (`[530]`–`[565]`).
4. Load the target Schema Lock file from Cluster 00 (`[014]`–`[030]`).
5. Explicitly declare loaded file IDs at the top of the operational response.

## 4. Stage-Gate Precondition Contract

Before executing tasks routed by this gateway:
- Upstream stage gates specified in `[004] stage-gate-progression-protocol.md` must record verified status.
- Any input artifact must pass its mapped schema validation gate before mutation.
- Timeline modifications must compute frame offsets in integer frames or 254,016,000,000 FilmCraft ticks.

## 5. Evidence-Gated Output Contract

All output emitted under this router must comply with `[005] evidence-gated-reasoning-contract.md`:
- Cites exact empirical scope values, loudness meters, phoneme timestamps, or frame numbers.
- Banned phrases ('warm look', 'smooth cut', 'natural mix') result in immediate rejection.

## 6. Escalation & Edge-Case Fallback Table

| Failure Mode | Detection Signature | Escalation Target | Resolution |
|---|---|---|---|
| Parameter Out of Bounds | Validator gate status == 'fail' | `[012]` Auto-Remediation | Recalculate parameters |
| Subjective Aesthetic Ambiguity | Conflicting creative options | `[006]` Taste-Gate | Present 2–3 structured options |
| Upstream Incomplete Data | Missing input telemetry | `[684]` Studio Defaults | Assign deterministic standard |

