# [013] Multi-Agent Conflict Resolution Arbitrator

## 1. Conflict Scenarios in Autonomous Post-Production
In a multi-agent post-production swarm (`[002]`), distinct domain personas frequently encounter conflicting objectives:
1. **Editor vs. Subtitler**: The Editor cuts rapid montage (6 frames/shot), but the Subtitler requires minimum 20 frames for reading comprehension.
2. **Colorist vs. VFX Artist**: The Colorist demands full linear dynamic range plates, while the VFX Artist comped against an sRGB display-referred preview.
3. **Sound Designer vs. Dialogue Mixer**: Heavy explosive sound effects mask critical narrative dialogue frequencies in the 1–4 kHz range.

## 2. Hierarchical Priority Matrix
When conflicts cannot be reconciled mathematically, the following invariant priority hierarchy governs:
$$\text{Legal / QC Compliance} > \text{Dialogue Intelligibility} > \text{Narrative Continuity} > \text{Aesthetic Stylization}$$

### 2.1 Resolution Rules
- **Rule 1 (Pacing vs. Reading)**: If a dialogue line must be read, the shot cannot be cut below the subtitle reading duration ($Dur_{min} = \max(20 	ext{ frames}, rac{	ext{chars}}{20} 	imes 	ext{fps})$), unless subtitles are split into two sequential sub-cues or dialogue is summarized under `[341]`.
- **Rule 2 (Dialogue vs. Sound Effects)**: Dialogue intelligibility is sovereign. The Dialogue Ducking engine (`[323]`) must attenuate FX/MX by $-4.0 	ext{ dB}$ to $-6.0 	ext{ dB}$ whenever dialogue RMS exceeds $-36.0 	ext{ dBFS}$.
- **Rule 3 (Gamut vs. Creative Look)**: Legal broadcast gamut boundaries override creative saturation. Any look exceeding legal broadcast range is automatically compressed by `[248]`.
