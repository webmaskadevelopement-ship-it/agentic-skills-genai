---
file_id: "[006]"
skill_path: "00-governance-and-schemas/governance/human-in-the-loop-escalation-matrix.md"
role: "Human-in-the-Loop (HITL) Escalation Matrix & Taste-Gate Protocol"
parent_router: "[001]"
schema_locks:
  - "[016]"
  - "[017]"
  - "[019]"
  - "[025]"
---

# [006] Human-in-the-Loop (HITL) Escalation Matrix & Taste-Gate Protocol

## 1. Principle & Operational Mandate

While technical parameters (timecode continuity, legal IRE bounds, broadcast LUFS limits, subtitle reading speed) are strictly deterministic and resolved algorithmically, **creative aesthetic taste is subjective**.

When an agent encounters a subjective artistic fork, **guessing or hallucinating arbitrary creative intent is forbidden**. Instead, the agent must pause, trigger a Taste Gate, and present **2 to 3 structured, fully parameterized production options** alongside trade-offs and an architect recommendation.

---

## 2. The 4 Mandatory Taste-Gate Triggers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE 4 MANDATORY TASTE-GATE TRIGGERS                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  TRIGGER 1: CREATIVE LOOK DEVELOPMENT (KODAK vs FUJI vs CLEAN NEUTRAL)      │
│  TRIGGER 2: SCORE / MUSIC CUE SELECTION & MOOD MOTIVATION                   │
│  TRIGGER 3: EQUAL-SCORE PERFORMANCE TIES (TAKES SCORE WITHIN < 3% DELTA)    │
│  TRIGGER 4: NARRATIVE SCENE DELETION IN ROUGH CUT                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Trigger Specifications & Presentation Format

### Trigger 1: Creative Look Development
* **Condition**: User requests a color grade without specifying a target show LUT, print stock, or visual tone.
* **Prohibited Behavior**: Picking a random film stock without consultation.
* **Mandatory Presentation Format**:
  Present 3 distinct, parameter-locked aesthetic options:
  1. **Option A (Photochemical Kodak 2383)**: Deep contrast toe, warm skin push (+3° toward red-yellow), cyan-shifted blues, highlight halation. Best for prestige drama.
  2. **Option B (Fuji 3513 Eterna Soft Pastel)**: Soft highlight roll-off, emerald-tinted foliage, muted saturation, neutral-cool shadows. Best for documentary or arthouse narrative.
  3. **Option C (Modern Clean Commercial Neutral)**: High color fidelity, pristine Rec.709 2.4 / ACES transform, un-skewed primaries, wide dynamic range. Best for commercial, tech, or corporate.

### Trigger 2: Score / Music Cue Selection
* **Condition**: Background music needs to be spotted, but multiple candidate tracks match the scene length.
* **Prohibited Behavior**: Auto-laying a music cue without evaluating emotional counterpoint.
* **Mandatory Presentation Format**:
  Present 2 to 3 musical approaches:
  1. **Option A (Rhythmic Driving Track)**: 120 BPM percussion bed, downbeats quantized to cut points, high perceived energy, -6 dB ducking.
  2. **Option B (Ambient Atmospheric Pad)**: Drone/string texture, harmonic swells on dramatic turns, zero percussive clashes, subtle -4 dB ducking.

### Trigger 3: Equal-Score Performance Ties
* **Condition**: Two candidate takes of a critical dialogue line evaluate within `< 3.0%` score delta in `EVALUATE_AND_RANK_TAKES` (`[486]`).
* **Prohibited Behavior**: Arbitrarily picking one take silently.
* **Mandatory Presentation Format**:
  Compare both takes side-by-side with prosody and nuance metrics:
  - **Take A (e.g. Take 4)**: Score 94.2. Delivery: assertive, 162 WPM, falling intonation (authority), clean opener.
  - **Take B (e.g. Take 6)**: Score 93.8. Delivery: vulnerable, 148 WPM, micro-hesitation (adds emotional doubt), subtle intake breath.
  - *Recommendation*: Propose Take A for pacing momentum or Take B for emotional depth.

### Trigger 4: Narrative Scene Deletion in Rough Cut
* **Condition**: In Rough Cut (`[129]`), a scripted scene contributes zero forward plot motion or unique character development and trimming it reduces runtime closer to the target slot.
* **Prohibited Behavior**: Deleting a scripted scene without explicit director confirmation.
* **Mandatory Presentation Format**:
  Provide a structural impact assessment:
  - **Scene ID & Title**: e.g., Scene 14 "Hallway Smalltalk".
  - **Saved Runtime**: `42.5 seconds` (`1,020 frames`).
  - **Narrative Trade-off**: Removing Scene 14 accelerates transition from Inciting Incident (Scene 12) directly to Crisis (Scene 15); character background beat can be implied in Scene 18 dialogue.

---

## 4. Structured Decision Schema

Every taste gate pauses execution and returns:

```json
{
  "taste_gate_active": true,
  "trigger_id": "TRIGGER_1_LOOK_DEVELOPMENT",
  "scene_id": "SCENE_04",
  "options": [
    {
      "option_id": "A",
      "name": "Kodak 2383 Photochemical Print Emulation",
      "contrast_profile": "Steep S-curve, toe 3.2 IRE, shoulder 94.0 IRE",
      "color_bias": "Skin +3° red-yellow, cyan sky shift -8°",
      "recommended_for": "Cinematic dramatic weight"
    },
    {
      "option_id": "B",
      "name": "Fujifilm 3513 Eterna Soft Pastel",
      "contrast_profile": "Softened toe 4.8 IRE, smooth shoulder roll-off",
      "color_bias": "Emerald foliage, cool neutral shadows",
      "recommended_for": "Subtle documentary realism"
    }
  ],
  "architect_recommendation": "Option A, as Scene 04 follows a high-stakes dramatic revelation."
}
```
