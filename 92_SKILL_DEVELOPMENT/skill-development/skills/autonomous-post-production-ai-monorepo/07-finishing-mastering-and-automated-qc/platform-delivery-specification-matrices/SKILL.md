---
file_id: "[427]"
skill_path: "07-finishing-mastering-and-automated-qc/platform-delivery-specification-matrices/SKILL.md"
role: "Sub-Skill Router: Sub-Router: Streamer, Broadcast & Social Spec Compliance"
parent_router: "[410]"
child_nodes:
  - "[428]"
  - "[429]"
  - "[430]"
  - "[431]"
  - "[432]"
  - "[433]"
  - "[434]"
  - "[435]"
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

# [427] Sub-Router: Streamer, Broadcast & Social Spec Compliance

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `07-finishing-mastering-and-automated-qc/platform-delivery-specification-matrices`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(netflix|branded|post|delivery|specification)` | `[428]` | `netflix-branded-post-delivery-specification.md` | UHD IMF Dolby Vision + Atmos + -27 LKFS + IMSC1.1 timed text matrix |
| `(?i)(amazon|prime|video|direct|and|studios|spec)` | `[429]` | `amazon-prime-video-direct-and-studios-spec.md` | ProRes 422 HQ / IMF + 5.1/2.0 PCM + SMPTE-TT / TTML delivery matrix |
| `(?i)(apple|tv|plus|and|itunes|store|package|spec)` | `[430]` | `apple-tv-plus-and-itunes-store-package-spec.md` | .itmsp package structure, ProRes, Dolby Atmos, and ITT caption matrix |
| `(?i)(bbc|and|uk|dpp|as|11|mxf|broadcast|delivery|spec)` | `[431]` | `bbc-and-uk-dpp-as-11-mxf-broadcast-delivery-spec.md` | AS-11 UK DPP HD/UHD MXF, EBU R128 -23 LUFS, PSE Harding, and EBU-TT |
| `(?i)(us|network|broadcast|pbs|nbc|cbs|abc|delivery|spec)` | `[432]` | `us-network-broadcast-pbs-nbc-cbs-abc-delivery-spec.md` | XDCAM HD422 / ProRes, ATSC A/85 -24 LKFS, CEA-708 captions, and slates |
| `(?i)(youtube|4k|hdr|and|sdr|optimal|upload|master|spec)` | `[433]` | `youtube-4k-hdr-and-sdr-optimal-upload-master-spec.md` | High-bitrate ProRes/H.264, -14 LUFS, BT.709/PQ tags, and SRT tracks |
| `(?i)(tiktok|instagram|reels|and|shorts|9x16|master|spec)` | `[434]` | `tiktok-instagram-reels-and-shorts-9x16-master-spec.md` | 1080x1920 30/60fps, UI safe-zone clearance, -14 LUFS, burned-in hooks |
| `(?i)(festival|screener|and|vimeo|pro|archive|spec)` | `[435]` | `festival-screener-and-vimeo-pro-archive-spec.md` | Password-protected 1080p/4K H.264 25-50 Mbps + backup DCP spec |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[427]`.
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

