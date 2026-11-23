---
file_id: "[072]"
skill_path: "01-ingest-dailies-and-assistant-editing/transcript-and-phoneme-indexing/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Word-Level Transcription, Diarization & Alignment"
parent_router: "[031]"
child_nodes:
  - "[073]"
  - "[074]"
  - "[075]"
  - "[076]"
  - "[077]"
  - "[078]"
  - "[079]"
  - "[080]"
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

# [072] Sub-Router: Word-Level Transcription, Diarization & Alignment

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `01-ingest-dailies-and-assistant-editing/transcript-and-phoneme-indexing`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(asr|word|and|phoneme|timestamp|alignment)` | `[073]` | `asr-word-and-phoneme-timestamp-alignment.md` | Sub-10ms forced alignment of spoken words to timecode frames |
| `(?i)(multi|speaker|diarization|and|character|binding)` | `[074]` | `multi-speaker-diarization-and-character-binding.md` | Mapping voice embeddings to script character names and ISO tracks |
| `(?i)(filler|word|and|disfluency|tagging|engine)` | `[075]` | `filler-word-and-disfluency-tagging-engine.md` | Indexing "um", "uh", "like", stutters, and false starts |
| `(?i)(mid|sentence|pause|and|silence|duration|profiler)` | `[076]` | `mid-sentence-pause-and-silence-duration-profiler.md` | Calculating exact millisecond duration of every silent gap |
| `(?i)(vocal|energy|pitch|and|cadence|prosody|analyzer)` | `[077]` | `vocal-energy-pitch-and-cadence-prosody-analyzer.md` | Scoring delivery intensity, inflection direction, and warmth |
| `(?i)(script|to|transcript|fuzzy|line|alignment)` | `[078]` | `script-to-transcript-fuzzy-line-alignment.md` | Mapping improvised or paraphrased takes back to script lines |
| `(?i)(profanity|and|broadcast|compliance|word|scanner)` | `[079]` | `profanity-and-broadcast-compliance-word-scanner.md` | Flagging FCC/Ofcom restricted words with frame-exact timestamps |
| `(?i)(multilingual|code|switching|transcript|handler)` | `[080]` | `multilingual-code-switching-transcript-handler.md` | Tagging mid-sentence language shifts for downstream subtitling |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[072]`.
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

