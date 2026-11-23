---
file_id: "[008]"
skill_path: "00-governance-and-schemas/governance/deterministic-timecode-arithmetic-engine.md"
role: "Deterministic Timecode Arithmetic & Frame Math Engine"
parent_router: "[001]"
schema_locks:
  - "[014]"
  - "[017]"
  - "[021]"
parameter_tables:
  - "[531]" # param-table-smpte-frame-rates-and-drop-frame-rules
validators:
  - "[568]" # validator-edl-record-timecode-continuity
  - "[569]" # validator-edl-source-in-out-duration-parity
---

# [008] Deterministic Timecode Arithmetic & Frame Math Engine

## 1. Principle & Operational Mandate

In digital non-linear editing, **floating-point second representations accumulate rounding drift** that breaks frame-accurate alignment over multi-hour timelines. Edits, audio sync, and subtitle cueing must be calculated on **exact integer frame counters** or **high-frequency integer ticks**.

This skill defines the authoritative mathematical transformations between SMPTE timecode strings (`HH:MM:SS:FF` or `HH:MM:SS;FF`), total cumulative frames ($F \in \mathbb{Z}^+$), and FilmCraft integer engine ticks ($254,016,000,000\text{ ticks/sec}$).

---

## 2. Supported Frame Rates & Mathematical Constants

| Timebase | Nominal FPS | Exact Rational Multiplier | Frame Duration (ms) | Drop-Frame Supported | FilmCraft Ticks / Frame |
|---|---|---|---|---|---|
| **23.976p** | 24 | $24000 / 1001 \approx 23.97602398$ | $41.708333\dots$ | No | $10,594,000,000$ |
| **24.000p** | 24 | $24 / 1$ | $41.666667\dots$ | No | $10,584,000,000$ |
| **25.000p** | 25 | $25 / 1$ | $40.000000$ | No | $10,160,640,000$ |
| **29.970 NDF** | 30 | $30000 / 1001 \approx 29.97002997$ | $33.366667\dots$ | No | $8,475,200,000$ |
| **29.970 DF** | 30 | $30000 / 1001 \approx 29.97002997$ | $33.366667\dots$ | **Yes** (Skip ;00, ;01) | $8,475,200,000$ |
| **30.000p** | 30 | $30 / 1$ | $33.333333\dots$ | No | $8,467,200,000$ |
| **50.000p** | 50 | $50 / 1$ | $20.000000$ | No | $5,080,320,000$ |
| **59.940 DF** | 60 | $60000 / 1001 \approx 59.94005994$ | $16.683333\dots$ | **Yes** (Skip ;00..;03) | $4,237,600,000$ |
| **60.000p** | 60 | $60 / 1$ | $16.666667\dots$ | No | $4,233,600,000$ |

*Notice: $254,016,000,000$ divides evenly by every common film, television, and audio sample rate ($48,000\text{ Hz}$, $96,000\text{ Hz}$, $192,000\text{ Hz}$, $23.976$, $24$, $25$, $29.97$, $30$, $50$, $59.94$, $60\text{ fps}$), completely eliminating floating-point rounding drift.*

---

## 3. Forward Timecode-to-Frame Conversion Algorithms

### 3.1 Non-Drop Frame (NDF) Conversion Formula
For any progressive or NDF timecode `HH:MM:SS:FF`:

$$F = \Big( \big( \text{HH} \times 3600 + \text{MM} \times 60 + \text{SS} \big) \times \text{Nominal\_FPS} \Big) + \text{FF}$$

### 3.2 Drop-Frame (29.97 DF) Conversion Formula
In 29.97 Drop-Frame timecode (delimited by semicolon `;`), frame numbers `;00` and `;01` are omitted at the start of every minute, **except** minutes divisible by 10 (`00`, `10`, `20`, `30`, `40`, `50`).
To calculate cumulative frames $F$ from `HH:MM:SS;FF`:

1. Calculate total elapsed minutes:
   $$M_{\text{total}} = (\text{HH} \times 60) + \text{MM}$$
2. Apply the drop-frame subtraction:
   $$D = 2 \times \left( M_{\text{total}} - \left\lfloor \frac{M_{\text{total}}}{10} \right\rfloor \right)$$
3. Compute total frames:
   $$F = (108000 \times \text{HH}) + (1800 \times \text{MM}) + (30 \times \text{SS}) + \text{FF} - D$$

---

## 4. Reverse Frame-to-Timecode Conversion Algorithms

### 4.1 Non-Drop Frame (NDF) Frame-to-TC Algorithm
Given integer frame count $F$ and $\text{Nominal\_FPS}$:

$$\text{FF} = F \pmod{\text{Nominal\_FPS}}$$
$$S_{\text{total}} = \left\lfloor \frac{F}{\text{Nominal\_FPS}} \right\rfloor$$
$$\text{SS} = S_{\text{total}} \pmod{60}$$
$$M_{\text{total}} = \left\lfloor \frac{S_{\text{total}}}{60} \right\rfloor$$
$$\text{MM} = M_{\text{total}} \pmod{60}$$
$$\text{HH} = \left\lfloor \frac{M_{\text{total}}}{60} \right\rfloor$$

Format output string: `f"{HH:02d}:{MM:02d}:{SS:02d}:{FF:02d}"`.

### 4.2 Drop-Frame (29.97 DF) Frame-to-TC Algorithm
Given integer frame count $F$:

1. Define 10-minute frame count:
   $$F_{10\text{m}} = 17982 \quad (10 \text{ minutes} \times 60 \text{ sec} \times 30 \text{ frames} - 18 \text{ dropped frames})$$
2. Define 1-minute frame count:
   $$F_{1\text{m}} = 1798 \quad (1 \text{ minute} \times 30 \text{ frames} - 2 \text{ dropped frames})$$
3. Compute 10-minute blocks and remainder:
   $$D_{10} = \left\lfloor \frac{F}{F_{10\text{m}}} \right\rfloor, \quad R_{10} = F \pmod{F_{10\text{m}}}$$
4. Compute 1-minute blocks within the 10-minute cycle:
   $$\text{If } R_{10} \ge 2: \quad D_1 = \left\lfloor \frac{R_{10} - 2}{F_{1\text{m}}} \right\rfloor + 1, \quad \text{else } D_1 = 0$$
5. Compute total adjusted frame counter:
   $$F_{\text{adj}} = F + 2 \times (9 \times D_{10} + D_1)$$
6. Calculate timecode digits from $F_{\text{adj}}$ using nominal 30 fps:
   $$\text{FF} = F_{\text{adj}} \pmod{30}, \quad \text{SS} = \left\lfloor \frac{F_{\text{adj}}}{30} \right\rfloor \pmod{60}, \quad \text{MM} = \left\lfloor \frac{F_{\text{adj}}}{1800} \right\rfloor \pmod{60}, \quad \text{HH} = \left\lfloor \frac{F_{\text{adj}}}{108000} \right\rfloor$$

Format output string: `f"{HH:02d}:{MM:02d}:{SS:02d};{FF:02d}"`.

---

## 5. Event Duration & Continuity Invariants

For any editorial event $E_k$ in `schema-edl-cut-manifest.md` (`[017]`):

1. **Duration Invariant**:
   $$\text{Duration\_Frames}(E_k) = \text{to\_frames}(\text{record\_out}) - \text{to\_frames}(\text{record\_in})$$
2. **Speed-Ratio Invariant** (when speed == 1.0):
   $$\text{to\_frames}(\text{record\_out}) - \text{to\_frames}(\text{record\_in}) \equiv \text{to\_frames}(\text{source\_out}) - \text{to\_frames}(\text{source\_in})$$
3. **Monotonic Sequence Continuity**:
   $$\text{to\_frames}(E_{k+1}.\text{record\_in}) \equiv \text{to\_frames}(E_k.\text{record\_out})$$
   *(Any deviation $> 0$ represents an unintended digital black frame; any deviation $< 0$ represents an unintended track collision).*
