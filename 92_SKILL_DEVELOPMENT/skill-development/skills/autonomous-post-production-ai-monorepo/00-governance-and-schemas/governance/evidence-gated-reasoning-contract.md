---
file_id: "[005]"
skill_path: "00-governance-and-schemas/governance/evidence-gated-reasoning-contract.md"
role: "Evidence-Gated Reasoning & Anti-Hallucination Contract"
parent_router: "[001]"
schema_locks:
  - "[015]"
  - "[017]"
  - "[019]"
  - "[022]"
  - "[025]"
validators:
  - "[567]"
  - "[573]"
  - "[580]"
  - "[586]"
  - "[688]" # meta-skill-anti-hallucination-evidence-citation-auditor
---

# [005] Evidence-Gated Reasoning & Anti-Hallucination Contract

## 1. Principle & Operational Mandate

In this monorepo, **unsubstantiated prose is treated as an execution defect**. AI agents frequently hallucinate aesthetic platitudes ("gives it a warm cinematic vibe", "trimmed for better flow", "mixed nicely"). Such phrases are completely banned.

Every operational decision, cut point, grading parameter, audio fader movement, and subtitle cue emitted by any agent must be permanently bound to an **empirical measurement** derived from audio waveforms, colorimetric scopes, phoneme timestamps, or ITU-R loudness meters.

---

## 2. Mandatory Evidence Citation Standards by Department

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEPARTMENTAL EVIDENCE CITATION STANDARDS                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [1] EDITORIAL CRAFT                                                        │
│      └─ [Word ID + Millisecond Timestamp + Intra-Clause Pause Duration]     │
│                                                                             │
│  [2] COLOR GRADING                                                          │
│      └─ [Waveform Min/Max IRE + Vectorscope Skin Vector + Parade Balance]   │
│                                                                             │
│  [3] SOUND DESIGN & MIXING                                                  │
│      └─ [Integrated LUFS + Max Short-Term LUFS + Oversampled True Peak dBTP]│
│                                                                             │
│  [4] SUBTITLING & LOCALIZATION                                              │
│      └─ [Visible Glyph Count / (Duration ms / 1000) = CPS, Max CPL]        │
│                                                                             │
│  [5] FINISHING & CONFORM                                                    │
│      └─ [Difference Matte Pixel_Delta == 0.0, Safe Area >= 90%, nclc Tag]  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Strict Citation Specifications

### 3.1 Editorial Evidence Standard (File A — `[017]`)
Every event in an EDL cut manifest MUST declare two load-bearing evidence fields:
1. `selection_rationale`:
   - Must cite candidate take number evaluated.
   - Must cite Disfluency Rate: `(N_fillers / Total_Words) * 100`.
   - Must cite conversational cadence (WPM).
   - Must cite exact zero-crossing opener/tail trim frames.
   - *Example*: `"Selected Take 4 (A001C014): 0 filler words, 158 WPM natural cadence, opener trimmed 3 frames before phoneme onset at 01:14:22:08. WPM matches incoming shot within 4 WPM."`
2. `disqualification_notes`:
   - Must cite every rejected candidate take with exact millisecond pause timestamps or physical defects.
   - *Example*: `"Disqualified Take 1 (3 'ums' at words w04, w12, w19); Disqualified Take 2 (2,380ms dead pause between 'our' at 01:08:14:02 and 'infrastructure' at 01:08:16:15); Disqualified Take 3 (clothing scratch on lav during 'launch')."`

### 3.2 Color Grading Evidence Standard (File B — `[019]`)
Every color grade specification MUST declare the `scope_evidence` object:
1. `waveform`:
   - `black_point_ire`: Float `[0.0, 10.0]` (target `2.0–5.0 IRE` for filmic blacks).
   - `white_point_ire`: Float `[70.0, 100.0]` (`80–90 IRE` diffuse white, `92–99 IRE` specular).
   - `highlight_clipping`: `"none"` | `"controlled"`.
   - `shadow_crush`: `"none"` | `"silhouetted"`.
2. `vectorscope`:
   - `skin_tone_alignment`: String declaring exact degree alignment on 123° I-line (e.g. `"123.4° on I-line (±1.5° tolerance)"`).
   - `saturation_envelope`: Percentage of 75% SMPTE legal target radius (e.g. `"28% radius (naturalistic)"`).
   - `dominant_color_cast`: Center reticle delta `(Δu, Δv)` (e.g. `"neutral (Δu: +0.001, Δv: -0.002)"`).
3. `parade`:
   - `channel_balance`: String certifying R=G=B alignment (e.g. `"Equalized shadow toe: R_min=3.1, G_min=3.0, B_min=3.2 IRE; specular highlight: R_max=96.4, G_max=96.1, B_max=96.3 IRE"`).

### 3.3 Sound Design & Mix Evidence Standard (File D — `[025]`)
Every mix specification MUST declare the physical acoustic telemetry:
1. `dialogue_target_lufs`: Float matching platform target (`-23.0` EBU / `-24.0` ATSC / `-27.0` Netflix).
2. `true_peak_ceiling_dbtp`: Float ceiling (`-1.0 dBTP` or `-2.0 dBTP`).
3. `max_short_term_lufs`: Maximum 3-second sliding window reading (e.g. `-18.0 LUFS`).
4. `loudness_range_lra`: Macro-dynamic envelope spread (e.g. `8.5 LU`).
5. `duck_under_dialogue`: Explicit attenuation parameters (e.g. `"-6.0 dB broadband attenuation + -4.5 dB parametric dip at 2.8 kHz (Q=1.4), lookahead=300ms, release=800ms"`).
6. `stem_deliverables`: Verification of mathematical stem unity: `Sum(DX + MX + FX) == Full_Mix ± 0.01 dB`.

### 3.4 Subtitling & Timed-Text Evidence Standard (File C — `[022]`)
Every subtitle cue MUST include deterministic readability metrics:
1. `cps`: Visible glyph count divided by display seconds: `len(visible_chars) / (duration_ms / 1000.0)`. Must be `<= 20.0` (Adult English) or `<= 17.0` (Broadcast).
2. `cpl`: Character count of longest line. Must be `<= 42` (Streaming) or `<= 37` (BBC).
3. `duration_ms`: Must satisfy `833ms <= duration_ms <= 7000ms`.
4. `shot_change_dead_zone`: Distance from adjacent visual cuts $|F_{\text{cue}} - F_{\text{cut}}| \notin [2..11\text{ frames}]$.

---

## 4. Pre-Emission Citation Verification

Before emitting any final artifact, the agent executes `[688] meta-skill-anti-hallucination-evidence-citation-auditor.md`.
* If any required numerical parameter is missing, the output is rejected.
* The agent must compute the missing value from raw source metadata or invoke `[684]` to declare safe studio defaults.
