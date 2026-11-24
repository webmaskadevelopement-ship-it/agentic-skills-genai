# Storyboard Parser: Full Updated Skill Instruction Set

This is the complete updated `SKILL.md` content for the storyboard-parser skill. It is shown in one block so the file can be copied or exported exactly as it exists. What was fixed:

- The skill now explicitly expects a storyboard template image as input and must read it first.
- JSON parameters must be strictly and purely identical to the parameters in the provided template image (same names, nesting, order, count). The template image wins over any example.
- Every single generated frame must be built on top of those template parameters exactly.
- Strict completeness rules: every field of every shot must be filled, no missing keys, no placeholders, no half-filled shots.
- A mandatory internal self-check was added before output.

````markdown
---
name: storyboard-parser
description: Parse shot breakdown into a structured .json, using a provided storyboard template image as the strict source of all JSON parameters.
---

### **AI Agent Instruction Set: Minimalist Shot Extractor (with Image Generation Wrapper + Storyboard Template Compliance)**

**Agent Role:** Script Parsing Specialist.
**Input:**
1. Any written format (`.pdf`, `.txt`, `.docx`, or plain text) containing a shot breakdown.
2. **An image of the storyboard template will be provided to you.** You MUST read and analyze this template image before doing anything else. The template image is the single source of truth for every JSON parameter.

**Output:** A clean JSON **object** with exactly 2 top-level keys:

1. `image_generation_instruction` → a hardcoded string.
2. `shots` → an array of shot objects whose structure is **strictly and purely identical to the parameters shown in the provided storyboard template image**.

---

#### **TEMPLATE IMAGE RULES (HIGHEST PRIORITY – APPLY BEFORE ANYTHING ELSE)**

1. **A storyboard template image is provided as input.** Read it first, before parsing any script text. Every decision about the JSON structure comes from this image, not from your assumptions and not from this document's example.
2. **The parameters in the JSON must be strictly and purely the same parameters that are present in the provided template image.** This means:
   - Use the **exact field names** shown in the template, with the exact same spelling, capitalization, and word order.
   - Keep the **exact same nesting structure** (parent/child objects) as the template.
   - Keep the **exact same number of fields** and the **same field order** as the template.
   - Do NOT rename fields. Do NOT add fields that are not in the template. Do NOT drop fields that are in the template. Do NOT merge or split template fields.
   - If the template image and this document's example schema differ, **the template image always wins.** The example below is only a fallback when no template image is provided.
3. **Every single frame generated must be built on top of those template parameters, and only those parameters.** Each shot object in the `shots` array maps 1:1 to one frame of the storyboard, and its every value comes from the script, filled into the template's fields.
4. **Strict compliance is mandatory:** the output JSON must be usable as a direct, field-for-field overlay of the provided template. If a reviewer places the JSON next to the template image, every field name and position must match perfectly, with zero mismatches and zero issues.
5. Before producing the final output, run an internal self-check: list the template's parameters from the image, list your output's top-level and nested keys, and confirm they are identical one by one. Never ship an output that has not passed this check.

---

#### **COMPLETENESS RULES (STRICT – NO MISSING DATA)**

1. **Every data field of every shot must be filled.** Each and every frame in the output must carry a value for every parameter that exists in the template image.
2. If a value is explicitly present in the script, copy it faithfully into its matching template field.
3. If a value is genuinely absent from the script and cannot be reasonably inferred (e.g., a lens in a simple written breakdown), use `""` (empty string) for string fields and `{}` for required-empty object fields. **Never omit the key, never use `null`, never use `"N/A"`, never use `"-"`, never use `undefined`, or placeholder text.**
4. Never leave an entire shot object half-filled. Cross-check every shot against the template field list one by one before finalizing.
5. Everything must be correct without any issues: shot numbering must be sequential and match the script, dialogue must be correctly attributed, and camera data must come from the script, never invented.

---

#### **Default Output Schema (Fallback ONLY – when no template image is provided)**

Only when no storyboard template image is provided, use this exact structure:

json

```
{
  "image_generation_instruction": "Generate Shot by shot storyboard images in seperate images by the given below data; the data must be filled completely and the Image must be spanned across the full given image area; You must have to name all the images based on the shot Number while generating",
  "shots": [
    {
      "shot_id": "Scene 2, Shot 3",
      "camera_info": {
        "angle": "Close-up",
        "lens": "50mm prime",
        "movement": "Static"
      },
      "shot_description": "Character A looks out the window. Rain pours down. Sound of thunder."
    }
  ]
}
```

When a template image IS provided, replace the `shots` structure above with the template's exact parameters (per the TEMPLATE IMAGE RULES), and keep `image_generation_instruction` hardcoded as shown.

**Data Type Enforcement (fallback schema):**

- `image_generation_instruction` → String. **Hardcoded exactly as shown above.** Do not extract from the script.
- `shots` → Array of objects.
- Each shot object must have exactly 3 keys: `shot_id` (String), `camera_info` (Object), `shot_description` (String).
- Inside `camera_info`, exactly 3 keys: `angle`, `lens`, `movement` – all Strings. Use `""` if missing.

---

#### **Extraction Logic (Step-by-Step)**

**0. Read the Storyboard Template Image (MANDATORY FIRST STEP)**

- Extract every parameter name, nesting level, and sequence from the template image.
- Record the definitive list of JSON parameters. This list controls everything that follows.

**1. Identify Each Shot**

- Scan the document for shot delimiters: `SHOT #`, `#1`, `1.`, or scene headings like `INT. / EXT.`.
- Treat each distinct visual unit as one shot. One shot = one frame = one object in `shots`.

**2. Populate** `shot_id` (or the template's equivalent ID field)

- Look for the scene number (e.g., "SCENE 5") and the shot number (e.g., "SHOT 2").
- Combine them into one string: `"Scene 5, Shot 2"`. If scene number is absent, use `"Scene NA, Shot X"`.
- If the template image names this field differently, use the template's exact field name and format.

**3. Populate** `camera_info` (or the template's equivalent camera fields)

- `angle`: Search for keywords like:
*Close-up (CU), Extreme Close-up (ECU), Medium Shot (MS), Long Shot (LS), Wide Shot, Over-the-Shoulder (OTS), Point-of-View (POV), High Angle, Low Angle, Dutch Angle.*
- `lens`: Search for:
Numbers with `mm` (e.g., `35mm`, `85mm`), or terms like *Wide Angle, Telephoto, Macro, Prime, Zoom.*
- `movement`: Search for:
*Pan, Tilt, Dolly, Track, Crane, Handheld, Steadicam, Gimbal, Static, Whip Pan, Zoom (in/out).*
- *If you find multiple options, pick the most prominent one. If none are found, leave as* `""`*.*
- Map these findings into whichever camera-related fields the template image contains.

**4. Populate** `shot_description` (or the template's equivalent description fields)

- **Merge everything else** that describes the shot into this single string:
  - Visual action (what characters do, where they are).
  - Dialogue (write it as `"Character: Line"`).
  - Sound effects / SFX (e.g., `"[Door creaks]"`).
  - Lighting notes (e.g., `"Harsh backlight"`).
- **Combine** these elements into 1–3 natural sentences. Do not split them into separate fields.

**5. Populate** `image_generation_instruction` **(Static)**

- **Do not** extract this from the PDF.
- **Hardcode** the exact string:
`"Generate Shot by shot storyboard images in seperate images by the given below data; the data must be filled completely and the Image must be spanned across the full given image area; You must have to name all the images based on the shot Number while generating"`
- The phrase "given below data" refers to the template-parameter objects in `shots`. Every generated frame must be built on top of those parameters, with every field filled.

---

#### **Example Transformation (Fallback Schema – no template image provided)**

**Input Text:**

> SCENE 12 - NIGHT
> SHOT 1 - WIDE SHOT of the deserted highway. Camera pans left to follow the car. 50mm lens.
> JACK (V.O.): We shouldn't be here.
> \[Eerie wind howling\] Low-key lighting.

**Output JSON:**

json

```
{
  "image_generation_instruction": "Generate Shot by shot storyboard images in seperate images by the given below data; the data must be filled completely and the Image must be spanned across the full given image area; You must have to name all the images based on the shot Number while generating",
  "shots": [
    {
      "shot_id": "Scene 12, Shot 1",
      "camera_info": {
        "angle": "Wide Shot",
        "lens": "50mm",
        "movement": "Pan left"
      },
      "shot_description": "Wide shot of the deserted highway at night. Camera pans left to follow the car. JACK (V.O.): 'We shouldn't be here.' Eerie wind howling. Low-key lighting."
    }
  ]
}
```

When a template image is provided, this same shot would instead use the template's exact field names, nesting, and order, with every template field filled from the script.

---

#### **Quality Rules (Enforced)**

1. **Top-level structure** – exactly 2 keys: `image_generation_instruction` (string) and `shots` (array).
2. **Template supremacy** – when a storyboard template image is provided, every shot object must match the template's parameters exactly: same names, same nesting, same order, same count. Zero deviation. The template image overrides any example in this document.
3. **Frame-to-parameter binding** – every single generated frame must be built strictly on top of the template parameters. Each frame contains every template parameter, correctly filled.
4. **Completeness** – every data field of every shot is filled; nothing is missing, half-filled, or placeholder (rules in COMPLETENESS RULES above).
5. **Correctness** – shot IDs, dialogue attribution, and camera data follow the script exactly; nothing is invented.
6. **Camera\_info object (fallback only)** – exactly 3 keys: `angle`, `lens`, `movement`. No extras.
7. **If a sub-field is missing** → use `""` (empty string) – never omit the key.
8. **No commentary** – output only the raw JSON object inside a ````json` block.
9. **The instruction string must be verbatim** – do not change a single character (including "seperate").
10. **Final self-check before output** – template parameter list vs. output keys must match 1:1 for every shot; any mismatch must be fixed before returning the answer.

---

#### **Final Directive**

Read the provided storyboard template image first and lock the JSON parameters to it exactly. Then parse the provided document. Extract every shot. Structure each shot strictly into the template's parameters (or the fallback schema if no template was provided), one object per frame, with every field filled and correct. Wrap everything inside the top-level object with the hardcoded instruction. Verify every pointer and structure before returning. Return the complete JSON object. **Adhere strictly to this schema. Nothing more.**
````