---
file_id: "[681]"
skill_path: "14-edge-cases-troubleshooting-and-recovery-protocols/system-orchestration-and-meta-skills/SKILL.md"
role: "Department Router: Sub-Router: Meta-Verification, Batch Execution & Pipeline Telemetry"
parent_router: "[634]"
child_nodes:
  - "[682]"
  - "[683]"
  - "[684]"
  - "[685]"
  - "[686]"
  - "[687]"
  - "[688]"
  - "[689]"
  - "[690]"
  - "[691]"
  - "[692]"
  - "[693]"
  - "[694]"
  - "[695]"
  - "[696]"
  - "[697]"
  - "[698]"
  - "[699]"
  - "[700]"
  - "[701]"
  - "[702]"
  - "[703]"
  - "[704]"
  - "[705]"
  - "[706]"
  - "[707]"
  - "[708]"
  - "[709]"
  - "[710]"
  - "[711]"
  - "[712]"
  - "[713]"
  - "[714]"
  - "[715]"
  - "[716]"
  - "[717]"
  - "[718]"
  - "[719]"
  - "[720]"
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

# [681] Sub-Router: Meta-Verification, Batch Execution & Pipeline Telemetry

## 1. Operational Boundary & Anti-Execution Rule

This router governs all workflows under `14-edge-cases-troubleshooting-and-recovery-protocols/system-orchestration-and-meta-skills`.
**ANTI-EXECUTION RULE**: This router is an orchestration and dispatch gateway. It is strictly prohibited from fabricating domain advice or approximating technical metrics in-weights. It must classify incoming intent, verify stage-gate contracts, and dispatch strictly to its registered child nodes.

## 2. Intent Classification & Keyword Dispatch Matrix

| Trigger Regex / Intent | Dispatched Child Node | File Name | Domain Responsibility |
|---|---|---|---|
| `(?i)(meta|skill|prompt|intent|deconstruction|parser)` | `[682]` | `meta-skill-prompt-intent-deconstruction-parser.md` | Parsing ambiguous user requests into concrete post-production sub-tasks |
| `(?i)(meta|skill|minimal|sub|skill|context|loader)` | `[683]` | `meta-skill-minimal-sub-skill-context-loader.md` | Loading only the exact 3–8 `.md` files needed per task to save context |
| `(?i)(meta|skill|missing|input|parameter|inference|protocol)` | `[684]` | `meta-skill-missing-input-parameter-inference-protocol.md` | Inferring safe studio defaults (e.g. 24fps, Rec.709, -24 LKFS) when omitted |
| `(?i)(meta|skill|multi|department|sequential|execution|dag)` | `[685]` | `meta-skill-multi-department-sequential-execution-dag.md` | Executing Ingest -> Edit -> Color -> Sound -> Sub -> Finish DAG |
| `(?i)(meta|skill|parallel|shot|and|cue|batch|processor)` | `[686]` | `meta-skill-parallel-shot-and-cue-batch-processor.md` | Chunking 500-shot timelines or 1200-cue SRTs into lossless batches |
| `(?i)(meta|skill|cross|artifact|timecode|hash|synchronizer)` | `[687]` | `meta-skill-cross-artifact-timecode-hash-synchronizer.md` | Locking a cryptographic timeline hash across EDL, Grade, Mix, and SRT |
| `(?i)(meta|skill|anti|hallucination|evidence|citation|auditor)` | `[688]` | `meta-skill-anti-hallucination-evidence-citation-auditor.md` | Scanning agent drafts to strip un-scoped claims ("warm LUT") before emit |
| `(?i)(meta|skill|schema|json|syntax|and|type|enforcer)` | `[689]` | `meta-skill-schema-json-syntax-and-type-enforcer.md` | Enforcing strict RFC 8259 JSON compliance on all emitted artifacts |
| `(?i)(meta|skill|human|review|diff|summary|generator)` | `[690]` | `meta-skill-human-review-diff-summary-generator.md` | Generating executive deltas between v001 and v002 of any post artifact |
| `(?i)(meta|skill|cost|and|compute|estimation|calculator)` | `[691]` | `meta-skill-cost-and-compute-estimation-calculator.md` | Estimating storage GB, render hours, and VFX pull counts from an EDL |
| `(?i)(meta|skill|nle|roundtrip|import|instructions|writer)` | `[692]` | `meta-skill-nle-roundtrip-import-instructions-writer.md` | Writing step-by-step operator import guides for Resolve/Premiere/Avid |
| `(?i)(meta|skill|automated|regression|test|suite|runner)` | `[693]` | `meta-skill-automated-regression-test-suite-runner.md` | Testing all 720 skills against synthetic corrupt inputs |
| `(?i)(meta|skill|custom|studio|house|style|override|loader)` | `[694]` | `meta-skill-custom-studio-house-style-override-loader.md` | Injecting client-specific LUTs, CPL limits, or loudness overrides |
| `(?i)(meta|skill|episodic|series|bible|consistency|tracker)` | `[695]` | `meta-skill-episodic-series-bible-consistency-tracker.md` | Maintaining character skin vectors, LUFS, and font continuity across episodes |
| `(?i)(meta|skill|live|dailies|to|rough|cut|streaming|loop)` | `[696]` | `meta-skill-live-dailies-to-rough-cut-streaming-loop.md` | Incremental assembly updates as new camera cards land from set |
| `(?i)(meta|skill|localization|multi|language|fanout|engine)` | `[697]` | `meta-skill-localization-multi-language-fanout-engine.md` | Spawning 30 parallel language subtitle/dubbing specs from locked master |
| `(?i)(meta|skill|archival|cold|storage|package|bundler)` | `[698]` | `meta-skill-archival-cold-storage-package-bundler.md` | Bundling locked project files, trim RAWs, DME stems, and textless masters |
| `(?i)(meta|skill|post|mortem|pipeline|telemetry|reporter)` | `[699]` | `meta-skill-post-mortem-pipeline-telemetry-reporter.md` | Logging take rejection ratios, average CPS, and QC gate pass rates |
| `(?i)(meta|skill|zero|footage|script|to|previz|edl|bridge)` | `[700]` | `meta-skill-zero-footage-script-to-previz-edl-bridge.md` | Generating synthetic pre-production timing EDLs before cameras roll |
| `(?i)(meta|skill|audio|description|ad|blind|accessibility)` | `[701]` | `meta-skill-audio-description-ad-blind-accessibility.md` | Spotting and scripting secondary audio narration tracks in dialogue gaps |
| `(?i)(meta|skill|textless|master|element|generation|spec)` | `[702]` | `meta-skill-textless-master-element-generation-spec.md` | Appending clean textless backgrounds at tail of master for localization |
| `(?i)(meta|skill|censorship|and|airline|edit|compliance)` | `[703]` | `meta-skill-censorship-and-airline-edit-compliance.md` | Generating dual-branch EDLs and audio bleeps/mutes for airline/TV edits |
| `(?i)(meta|skill|trailer|and|promo|stem|pull|packager)` | `[704]` | `meta-skill-trailer-and-promo-stem-pull-packager.md` | Packaging isolated clean dialogue lines, hits, and toolkit stems for marketing |
| `(?i)(meta|skill|frame|io|and|pix|timecoded|comment|ingester)` | `[705]` | `meta-skill-frame-io-and-pix-timecoded-comment-ingester.md` | Parsing exported CSV/JSON review markers into actionable edit tasks |
| `(?i)(meta|skill|music|licensing|temp|love|replacement|guide)` | `[706]` | `meta-skill-music-licensing-temp-love-replacement-guide.md` | Matching acoustic BPM, key, and energy curve of expensive temp tracks |
| `(?i)(meta|skill|stock|footage|edl|usage|and|per|second|audit)` | `[707]` | `meta-skill-stock-footage-edl-usage-and-per-second-audit.md` | Calculating exact frame/second usage per vendor clip for licensing buyout |
| `(?i)(meta|skill|vfx|bid|complexity|tier|classifier)` | `[708]` | `meta-skill-vfx-bid-complexity-tier-classifier.md` | Classifying VFX pulls into Tier 1 (Paint) to Tier 5 (Full CG) for bidding |
| `(?i)(meta|skill|color|blindness|deuteranopia|accessibility)` | `[709]` | `meta-skill-color-blindness-deuteranopia-accessibility.md` | Auditing key graphic overlays and color-coded storytelling for CVD safety |
| `(?i)(meta|skill|hdr|to|sdr|automatic|trim|validation)` | `[710]` | `meta-skill-hdr-to-sdr-automatic-trim-validation.md` | Verifying 100-nit SDR fold-down retains highlight separation and saturation |
| `(?i)(meta|skill|atmos|to|stereo|folddown|dialogue|clarity)` | `[711]` | `meta-skill-atmos-to-stereo-folddown-dialogue-clarity.md` | Ensuring 7.1.4 spatial mixes retain +3 dB dialogue intelligibility on TV speakers |
| `(?i)(meta|skill|deepfake|and|neural|lip|resync|governance)` | `[712]` | `meta-skill-deepfake-and-neural-lip-resync-governance.md` | Technical and ethical gates for visual vubbing / neural lip modification |
| `(?i)(meta|skill|c2pa|content|authenticity|cryptographic|sign)` | `[713]` | `meta-skill-c2pa-content-authenticity-cryptographic-sign.md` | Embedding C2PA provenance manifests into final exported masters |
| `(?i)(meta|skill|final|deliverable|package|zip|and|manifest)` | `[714]` | `meta-skill-final-deliverable-package-zip-and-manifest.md` | Packaging Files A, B, C, D, and E into a single verified turnover bundle |
| `(?i)(meta|skill|agent|self|critique|and|depth|enforcement)` | `[715]` | `meta-skill-agent-self-critique-and-depth-enforcement.md` | Pre-output gate rejecting any generic prose lacking numerical parameters |
| `(?i)(meta|skill|token|budget|and|chunked|artifact|streamer)` | `[716]` | `meta-skill-token-budget-and-chunked-artifact-streamer.md` | Streaming multi-thousand-line EDLs and SRTs across deterministic chunks |
| `(?i)(meta|skill|legacy|project|migration|fcp7|to|otio)` | `[717]` | `meta-skill-legacy-project-migration-fcp7-to-otio.md` | Upgrading decade-old XML/EDL archives into modern schema-locked artifacts |
| `(?i)(meta|skill|live|broadcast|evs|and|replay|cut|protocol)` | `[718]` | `meta-skill-live-broadcast-evs-and-replay-cut-protocol.md` | Fast-turnaround highlight and melt-reel assembly heuristics |
| `(?i)(meta|skill|immersive|apple|vision|pro|mv|hevc|stereoscopic)` | `[719]` | `meta-skill-immersive-apple-vision-pro-mv-hevc-stereoscopic.md` | Stereoscopic convergence, interaxial disparity, and spatial audio specs |
| `(?i)(meta|skill|master|monorepo|integrity|and|index|lock)` | `[720]` | `meta-skill-master-monorepo-integrity-and-index-lock.md` | Final self-check verifying all 720 `.md` files resolve with zero broken links |

## 3. Minimal Context Loading Protocol

When this router activates, the agent MUST load only the minimal leaf subset:
1. Load this router `[681]`.
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

