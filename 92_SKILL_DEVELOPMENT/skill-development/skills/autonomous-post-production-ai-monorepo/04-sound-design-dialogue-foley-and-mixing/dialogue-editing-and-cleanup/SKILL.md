---
file_id: "[268]"
skill_path: "04-sound-design-dialogue-foley-and-mixing/dialogue-editing-and-cleanup/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Production Dialogue Assembly, Restoration & ADR"
parent_router: "[267]"
child_nodes:
  - "[269]"
  - "[270]"
  - "[271]"
  - "[272]"
  - "[273]"
  - "[274]"
  - "[275]"
  - "[276]"
  - "[277]"
  - "[278]"
  - "[279]"
  - "[280]"
  - "[281]"
  - "[282]"
  - "[283]"
  - "[284]"
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

# [268] Sub-Router: Production Dialogue Assembly, Restoration & ADR

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `04-sound-design-dialogue-foley-and-mixing/dialogue-editing-and-cleanup`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(boom|vs|lavalier|microphone|selection|matrix)` | `[269]` | `boom-vs-lavalier-microphone-selection-matrix.md` | Prioritizing natural boom perspective over chesty lavs unless noisy |
| `(?i)(sub|sample|phase|alignment|boom|and|lav|blending)` | `[270]` | `sub-sample-phase-alignment-boom-and-lav-blending.md` | Eliminating comb filtering via time-delay and polarity alignment |
| `(?i)(dialogue|checkerboarding|by|speaker|and|scene|track)` | `[271]` | `dialogue-checkerboarding-by-speaker-and-scene-track.md` | Alternating speakers across DX1–DX8 tracks for independent EQ/comp |
| `(?i)(word|and|syllable|filler|surgical|excision)` | `[272]` | `word-and-syllable-filler-surgical-excision.md` | Removing "ums", lip smacks, and swallows at zero-crossing points |
| `(?i)(breath|attenuation|and|natural|cadence|preservation)` | `[273]` | `breath-attenuation-and-natural-cadence-preservation.md` | Reducing distracting gasps by -6 to -12 dB without sounding robotic |
| `(?i)(room|tone|harvesting|and|seamless|fill|synthesis)` | `[274]` | `room-tone-harvesting-and-seamless-fill-synthesis.md` | Extracting clean 5s noise prints and crossfading under every edit gap |
| `(?i)(spectral|de|click|and|mouth|noise|restoration)` | `[275]` | `spectral-de-click-and-mouth-noise-restoration.md` | Attenuating transient saliva clicks between 2 kHz and 10 kHz |
| `(?i)(spectral|de|plosive|p|and|b|pop|suppression)` | `[276]` | `spectral-de-plosive-p-and-b-pop-suppression.md` | Dynamic low-band surgical removal of 20 Hz–120 Hz mic blasts |
| `(?i)(clothing|rustle|and|lavalier|scratch|attenuation)` | `[277]` | `clothing-rustle-and-lavalier-scratch-attenuation.md` | Separating high-frequency fabric friction from vocal formants |
| `(?i)(broadband|de|noise|and|hvac|rumble|extraction)` | `[278]` | `broadband-de-noise-and-hvac-rumble-extraction.md` | Neural/spectral noise reduction preserving vocal consonant clarity |
| `(?i)(electrical|50hz|60hz|hum|and|harmonic|notch|filter)` | `[279]` | `electrical-50hz-60hz-hum-and-harmonic-notch-filter.md` | High-Q notch filtering fundamental hum and up to 16 odd/even harmonics |
| `(?i)(de|reverb|and|boxy|room|reflection|suppression)` | `[280]` | `de-reverb-and-boxy-room-reflection-suppression.md` | Tightening reverberant location dialogue to match close-up visuals |
| `(?i)(de|clip|and|digital|distortion|waveform|rebuild)` | `[281]` | `de-clip-and-digital-distortion-waveform-rebuild.md` | Reconstructing squared-off clipped peaks from unexpected shouts |
| `(?i)(clip|gain|syllable|leveling|pre|compression)` | `[282]` | `clip-gain-syllable-leveling-pre-compression.md` | Leveling raw dialogue within ±2 dB window before hitting bus compressor |
| `(?i)(adr|spotting|cue|sheet|and|beep|sync|generator)` | `[283]` | `adr-spotting-cue-sheet-and-beep-sync-generator.md` | Generating ADR cue sheets with 3-beep streamer timing and reason codes |
| `(?i)(adr|worldizing|eq|and|reverb|match|to|production)` | `[284]` | `adr-worldizing-eq-and-reverb-match-to-production.md` | Matching clean studio ADR to noisy exterior production acoustics |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[268]`.
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

