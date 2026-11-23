# Model Prompt Guide — Open Higgsfield studio

Per-model prompt guiding distilled from the Open-Higgsfield-AI studio catalogs
(`packages/studio/src/models.js`, auto-generated from `models_dump.json`; pulled
2026-11-05). Each entry: what the prompt field should contain, real example
prompts, and the option enums (aspect ratios, durations, resolutions, modes).
Use as a quick reference when writing portable prompts per model.

## Text-to-Image (51 models)

### Nano Banana (`nano-banana`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "A portrait of me in a modern living room. Change it so I’m dressed in 1950s attire with a polka-dot dress, while maintaining my face and hairstyle."
- **Options:** aspect_ratio: 1:1, 3:4, 4:3, 9:16, 16:9, 3:2, 2:3, 5:4, 4:5, 21:9

### Flux Dev (`flux-dev-image`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word "FLUX" is painted over it in big, white brush strokes with visible texture."

### Flux Dev Lora (`flux-dev-lora`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "A female warrior in ornate armor standing on a cliff during sunset, flowing cape, wind blowing through her hair, detailed fantasy art style."

### Flux Kontext Dev T2I (`flux-kontext-dev-t2i`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "A powerful wizard casting a glowing spell in a dark forest, wearing a hooded robe, with swirling magical energy, epic fantasy art."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9, 9:21

### Hidream I1 Fast (`hidream-i1-fast`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "A colorful cartoon-style cat sitting on a skateboard, wide smile, playful background, 2D flat illustration style."

### Hidream I1 Dev (`hidream-i1-dev`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "A colorful cartoon-style cat sitting on a skateboard, wide smile, playful background, 2D flat illustration style."

### Hidream I1 Full (`hidream-i1-full`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "A majestic elven queen standing in a glowing forest, wearing intricate golden armor with emerald details, sunlight rays filtering through the trees, ultra-detailed fantasy concept art."

### Ai Anime Generator (`ai-anime-generator`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A cheerful anime girl with short pink hair and green eyes, wearing a school uniform, standing under cherry blossom trees, soft lighting, anime style."

### Wan2.1 Text To Image (`wan2.1-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A young woman with freckles and natural makeup, standing in soft sunlight, sharp focus, DSLR photo style, ultra-realistic skin texture."

### Flux Kontext Pro T2I (`flux-kontext-pro-t2i`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A steampunk owl with mechanical wings, perched on a glowing gear, cinematic lighting."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 16:21

### Flux Kontext Max T2I (`flux-kontext-max-t2i`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A realistic portrait of a woman with curly hair, wearing a silk blouse, studio lighting, high detail."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 16:21

### Gpt4o Text To Image (`gpt4o-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A diagram of the solar system with labeled planets, cartoon style."
- **Options:** aspect_ratio: 1:1, 2:3, 3:2

### Midjourney v7 Text To Image (`midjourney-v7-text-to-image`)
- **Prompt:** The prompt to generate the image
- **Example:** "A sprawling futuristic city at dusk, illuminated with vibrant neon signs, layered skyscrapers, elevated highways with flying cars, warm atmospheric glow, ultra-detailed sci-fi architecture, cinematic composition — digital art, high contrast, 8K"
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 1:2, 2:1, 2:3, 3:2, 5:6, 6:5

### Flux Schnell (`flux-schnell-image`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "A cozy mountain cabin surrounded by pine trees during snowfall, warm light glowing from windows, twilight scene"

### Bytedance Seedream v3 (`bytedance-seedream-v3`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A magical forest with glowing mushrooms and a crystal river under a starry sky, dreamy and ethereal style."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3

### Qwen Image (`qwen-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A serene Japanese garden in autumn, with red maple leaves falling gently, a small stone bridge over a koi pond, photorealistic detail, soft morning light"
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 9:21, 3:2, 2:3

### Flux Pulid (`flux-pulid`)
- **Prompt:** Text prompt describing the image (max 1500 characters).
- **Example:** "Recreate the same person in a Renaissance-style painting with ornate collar and soft candlelight ambiance."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4

### Ideogram v3 T2I (`ideogram-v3-t2i`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A retro 80s style poster with the words 'MUAPI APP' glowing in pink and blue neon lights, cyberpunk city skyline in the background, cinematic design, highly detailed."
- **Options:** aspect_ratio: 1:1, 3:4, 4:3, 9:16, 16:9 · style: Auto, General, Realistic, Design

### Google Imagen4 (`google-imagen4`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "A grand waterfall cascading down glowing crystal cliffs under a twilight sky, bioluminescent plants illuminating the scene, a lone explorer standing on a cliff edge with a futuristic lantern, cinematic ultra-realism."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4

### Google Imagen4 Fast (`google-imagen4-fast`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "A playful panda astronaut bouncing on the moon, leaving heart-shaped footprints, with a pastel-colored galaxy in the background."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4

### Google Imagen4 Ultra (`google-imagen4-ultra`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "A close-up portrait of an old lighthouse keeper, wrinkled hands holding a brass lantern, stormy sea waves crashing behind, ultra-detailed realism."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4

### Sdxl Image (`sdxl-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "An elven archer standing in a bioluminescent forest at night, glowing foliage, intricate leather armor, dynamic pose, painterly high-detail concept art."

### Bytedance Seedream v4 (`bytedance-seedream-v4`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A tranquil shoreline at dawn where waves turn into glowing ribbons of light, painting the sky with dreamlike hues of violet and gold. A figure walks along the edge, leaving footsteps that bloom into luminous flowers, symbolizing imagination flowing seamlessly into reality."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 2:3, 3:2, 21:9 · resolution: 1K, 2K, 4K

### Hunyuan Image 2.1 (`hunyuan-image-2.1`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A vast ink-wash landscape where misty mountains rise into drifting clouds, rivers flowing like silver threads across valleys. In the distance, a solitary pavilion glows with warm lantern light, blending classical Chinese painting aesthetics with modern cinematic realism."

### Chroma Image (`chroma-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A futuristic studio bathed in radiant beams of shifting neon colors — cyan, magenta, amber, and emerald — that blend into surreal gradients across walls and objects. A crystal-like prism floats at the center, splitting light into vibrant chromatic waves that ripple outward, painting the scene in glowing, ever-changing hues."

### Flux Redux (`flux-redux`)
- **Prompt:** Text prompt describing the image (max 1500 characters).
- **Example:** "Reimagine the forest cabin as a mystical fantasy retreat at twilight, glowing lanterns hanging from the trees, magical fireflies in the air, cinematic atmosphere with enchanted vibes."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9, 9:21

### Flux Krea Dev (`flux-krea-dev`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "Close-up shot of a midnight blue sports car on wet asphalt, city lights reflected in its paint, shallow depth of field, cinematic realism."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9, 9:21

### Perfect Pony Xl (`perfect-pony-xl`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A warm, photorealistic portrait of a dappled pony standing in a sunlit stable, dust motes floating in golden light, textured mane, high detail on fur and eyes."

### Neta Lumina (`neta-lumina`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A poised young woman with long silver hair and heterochromatic eyes (one blue, one green), wearing a flowing cheongsam with cranes embroidered, standing in a dimly lit grand staircase. Soft ethereal lighting, painterly anime style, rich textures, delicate lace and pearl accessories."

### Wan2.5 Text To Image (`wan2.5-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A majestic waterfall cascading from towering cliffs into a misty valley, with glowing bioluminescent plants along the riverbanks, a lone explorer standing on a rock, cinematic lighting and ultra-detailed scenery."

### Hunyuan Image 3.0 (`hunyuan-image-3.0`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A traditional Chinese courtyard with red lanterns hanging from wooden beams, moonlight reflecting from jade floor tiles. In the courtyard, a modern artist sits painting on an easel, neon blue sneakers, graffiti-style mural beginning behind them. Blend of classical aesthetics and modern street art."

### Leonardoai Phoenix 1.0 (`leonardoai-phoenix-1.0`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A magical forest at twilight, giant bioluminescent mushrooms illuminating a misty path, a crystal-clear river winding through twisted trees, fireflies dancing, soft ambient glow, ancient stone ruins partially visible, cinematic fantasy lighting, high-detail textures on foliage and moss, ethereal atmosphere, volumetric lighting rays piercing through branches."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 4:5, 5:4, 2:3, 3:2

### Leonardoai Lucid Origin (`leonardoai-lucid-origin`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A towering medieval castle perched on a cliff, waterfalls cascading around it, sunrise casting golden light on the stone walls, mist rising from the valley below, flying dragons circling above, realistic clouds and sky reflections, cinematic wide-angle view, ultra-detailed textures on stone and water, epic fantasy atmosphere."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 4:5, 5:4, 2:3, 3:2

### Reve Text To Image (`reve-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "An astronaut stands in a strange, bioluminescent purple jungle on an alien planet. She slowly reaches out her hand as a graceful creature made of translucent energy curiously approaches, gently touching her glove's fingertip with its tendril. The reflection of the planet's two moons is visible on her helmet's visor. Sense of wonder, photorealistic, cinematic."
- **Options:** aspect_ratio: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16, 9:21

### Grok Imagine Text To Image (`grok-imagine-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A futuristic samurai standing under glowing neon lights in a rainy cyberpunk alley, reflections on wet pavement, dramatic rim lighting, highly detailed armor, cinematic atmosphere, ultra-realistic style."
- **Options:** aspect_ratio: 9:16, 16:9, 2:3, 3:2, 1:1

### Nano Banana Pro (`nano-banana-pro`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "A radiant golden banana floating in a futuristic glass chamber, surrounded by swirling particles of light and data streams forming geometric shapes. Electric blue reflections ripple across the surface as energy pulses outward, turning fragments of light into vivid artworks suspended mid-air. Symbolizing playful innovation, AI precision, and evolution of creative power."
- **Options:** aspect_ratio: 1:1, 3:4, 4:3, 9:16, 16:9, 3:2, 2:3, 5:4, 4:5, 21:9 · resolution: 1k, 2k, 4k

### Kling O1 Text To Image (`kling-o1-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A towering arcology city at dusk built into a canyon, terraces lit with warm lanterns and bioluminescent gardens cascading down the rock face. Floating trams glide between terraces, mist curls from hidden waterfalls, and a faint green aurora shivers above the canyon rim. Deep orange sunset meets teal dusk, dramatic rim lighting, ultra-detailed architecture, cinematic wide-angle composition, 8k, hyperreal textures."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2, 21:9 · resolution: 1k, 2k

### Z Image Turbo (`z-image-turbo`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A colossal glass hourglass floating in a dark void, filled not with sand but with glowing galaxies swirling inside. Each galaxy emits colorful nebula clouds that leak through cracks in the glass, forming cosmic streams drifting into the darkness. Bright rim lighting around the hourglass, reflective glass surfaces, deep space background, ultra-detailed sci-fi render, 8k quality, volumetric glow, high contrast."

### Flux 2 Dev (`flux-2-dev`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A giant mechanical butterfly made of chrome wings and glowing blue energy veins, hovering above a mirror-smooth lake during twilight. Each wing reflects the sky while emitting soft neon trails. The lake surface ripples lightly from the energy pulses. Mist rolls across the water, and distant mountains fade into a deep violet horizon. Ultra-realistic lighting, cinematic composition, 8k render, high contrast, reflective metal textures."

### Flux 2 Flex (`flux-2-flex`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A monumental crystalline arch towering above an endless desert of shifting silver sand, glowing with internal prisms that refract rainbow beams across the dunes. Beneath the arch floats a slowly rotating orb of condensed starlight, casting long ethereal shadows. In the distance, colossal sand whales breach from metallic dunes, their bodies shimmering with mirrored scales. Overhead, a fractured moon illuminates the scene with cold blue radiance. Ultra-detailed fantasy–sci-fi fusion, cinematic wide-angle view, volumetric light rays, 8k clarity, high contrast, dreamlike atmosphere."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2 · resolution: 1k, 2k

### Flux 2 Pro (`flux-2-pro`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A colossal throne forged from intertwining meteor-iron branches, floating above a storm-torn ocean. Each branch pulses with glowing red runes, casting fiery reflections across the churning waves below. Above the throne hovers a massive eclipsed sun, its corona exploding into swirling arcs of molten light. Lightning erupts from the clouds and climbs the metal branches like living serpents. A lone hooded figure stands at the edge of the water, cloak whipping in the wind, illuminated only by the molten eclipse. Ultra-cinematic composition, hyper-detailed textures, 8k resolution, dramatic contrast, dark epic fantasy atmosphere."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2 · resolution: 1k, 2k

### Vidu Q2 Text To Image (`vidu-q2-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A colossal floating serpent made of shimmering stardust coils around a broken moon suspended in deep space. Each scale glows with shifting nebula colors, sending ripples of light across the void. Meteor fragments drift slowly around the creature, leaving trails of violet plasma. Beneath the serpent, a crystalline ring structure orbits the shattered moon, reflecting cosmic beams in intricate patterns. The background is a star field swirling into a spiral galaxy, with vibrant energy storms crackling along the horizon. Ultra-cinematic cosmic fantasy, high contrast, 8k detail, volumetric glow, deep space atmosphere."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2, 21:9 · resolution: 1k, 2k, 4k

### Bytedance Seedream V4.5 (`bytedance-seedream-v4.5`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A massive floating temple forged from translucent sapphire glass hovers above a storm-lit ocean. Crystalline towers refract lightning into rainbow shards that scatter across the waves below. Gigantic chains made of glowing runes suspend the temple in the air as swirling storm clouds coil around it. Beneath the structure, a vortex of shimmering water spirals upward, feeding energy into the floating palace. Distant thunder illuminates the scene with cold blue flashes, casting dramatic shadows across the ocean surface. Ultra-cinematic fantasy–sci-fi fusion, hyper-detailed textures, volumetric lighting, 8k clarity."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2, 21:9 · quality: basic, high

### Gpt Image 1.5 (`gpt-image-1.5`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A colossal hourglass floating in a silent cosmic void, its upper chamber filled with swirling golden sand that transforms into glowing constellations as it falls. The lower chamber contains a miniature ocean suspended in zero gravity, with waves frozen mid-motion and bioluminescent creatures glowing beneath the surface. Cracks in the glass emit thin beams of white light that bend and refract through drifting stardust. In the background, fragmented planets orbit slowly, partially illuminated by a distant supernova. Ultra-cinematic surreal concept, dramatic contrast between warm gold and deep blue, hyper-detailed textures, volumetric light rays, 8k clarity, dreamlike atmosphere."
- **Options:** aspect_ratio: 1:1, 2:3, 3:2 · quality: low, medium, high

### Wan2.6 Text To Image (`wan2.6-text-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A colossal floating bridge forged from glowing white stone spans a vast abyss filled with swirling clouds of light. Along the bridge, towering statues carved from ancient marble stand in silent formation, their eyes emitting faint golden beams that illuminate engraved runes beneath their feet. Below the bridge, fragments of ruined cities drift slowly through the mist, catching reflections from the glowing stone above. Overhead, a twilight sky fades from deep blue to soft amber, with distant stars beginning to appear. Cinematic fantasy environment, high contrast lighting, volumetric fog, ultra-detailed textures, epic scale."

### Qwen Text To Image 2512 (`qwen-text-to-image-2512`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "A colossal biomechanical whale swimming slowly through a vast sky made of soft clouds and fractured light. Its translucent body reveals glowing internal organs shaped like rotating gears and flowing energy veins. Below it, a sprawling patchwork of farmland and rivers curves with the planet’s surface, catching reflections from the whale’s luminous glow. Long fabric banners trail from the whale’s fins, fluttering gently in the wind like ceremonial streamers. The camera angle is wide and aerial, emphasizing scale and serenity. Soft sunrise colors, cinematic depth, ultra-detailed surreal sci-fi atmosphere."

### Flux 2 Klein 4b (`flux-2-klein-4b`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A small round robot sitting at a café table outdoors, holding a tiny cup of coffee with both hands. The robot has a simple white body, a glowing digital face showing a happy expression, and short stubby legs dangling from the chair. Morning sunlight casts soft shadows on the pavement, potted plants surround the café, and steam gently rises from the coffee cup. Clean, minimal, cute, modern illustration style, bright colors, friendly mood."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9, 9:21

### Flux 2 Klein 9b (`flux-2-klein-9b`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A cute corgi puppy wearing a tiny yellow raincoat stands on a wet sidewalk after rain. Small puddles reflect the city lights, and the puppy looks up with bright curious eyes while holding a green leaf in its mouth. Soft evening light, shallow depth of field, clean background, warm and cheerful mood, high detail fur texture, realistic yet adorable style."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9, 9:21

### Z Image Base (`z-image-base`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A cozy late-night diner interior with warm yellow lighting, rain tapping against large glass windows, and a lone barista cleaning the counter. A slice of pie sits under a glass dome, steam rises from a fresh cup of coffee, and neon signs outside softly glow and reflect across the wet street. Cinematic realism, shallow depth of field, calm mood, high detail, modern photography style."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9, 9:21

### Nano Banana 2 (`nano-banana-2`)
- **Prompt:** Positive prompt for generation.
- **Example:** "A futuristic cityscape with glowing neon lights reflected in rain-soaked streets, ultra-detailed 4K photography."
- **Options:** aspect_ratio: 1:1, 1:4, 1:8, 2:3, 3:2, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16 (+3 more) · resolution: 1k, 2k, 4k

### Seedream 5.0 (`seedream-5.0`)
- **Prompt:** Text prompt describing the image to generate.
- **Example:** "A futuristic city with soaring crystalline towers, suspended gardens, and neon-lit skyways under a twin-moon sky, captured in a cinematic, high-detail digital art style."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2, 21:9 · quality: basic, high

## Text-to-Video (42 models)

### Seedance Lite (`seedance-lite-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 9:21 · resolution: 480p, 720p, 1080p

### Seedance Pro (`seedance-pro-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 9:21 · resolution: 480p, 720p, 1080p

### Seedance Pro Fast (`seedance-pro-t2v-fast`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9 · resolution: 480p, 720p, 1080p

### Seedance v1.5 Pro (`seedance-v1.5-pro-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9 · resolution: 480p, 720p, 1080p

### Seedance v1.5 Pro Fast (`seedance-v1.5-pro-t2v-fast`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9 · resolution: 720p, 1080p

### Seedance 2.0 (`seedance-v2.0-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 4:3, 3:4 · duration: 5, 10, 15 · quality: high, basic

### Seedance 2.0 Extend (`seedance-v2.0-extend`)
- **Prompt:** Optional prompt to guide the extension. If omitted, the model continues with the original scene.
- **Options:** duration: 5, 10, 15 · quality: high, basic

### Kling v2.1 Master (`kling-v2.1-master-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Kling v2.5 Turbo Pro (`kling-v2.5-turbo-pro-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Kling v2.6 Pro (`kling-v2.6-pro-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · duration: 5, 10

### Kling O1 Pro (`kling-o1-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · duration: 5, 10

### Kling v3.0 Pro (`kling-v3.0-pro-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Kling v3.0 Standard (`kling-v3.0-standard-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Veo 3 (`veo3-text-to-video`)
- **Prompt:** Text prompt describing the desired video content.
- **Options:** aspect_ratio: 16:9, 9:16

### Veo 3 Fast (`veo3-fast-text-to-video`)
- **Prompt:** Text prompt describing the desired video content.
- **Options:** aspect_ratio: 16:9, 9:16

### Veo 3.1 (`veo3.1-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 8 · resolution: 1080p

### Veo 3.1 Fast (`veo3.1-fast-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 8 · resolution: 1080p

### Runway Gen-3 (`runway-text-to-video`)
- **Prompt:** The prompt to be used to generate a video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · duration: 5, 8 · resolution: 720p, 1080p

### Wan 2.1 (`wan2.1-text-to-video`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 480p, 720p · quality: medium, high

### Wan 2.2 (`wan2.2-text-to-video`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 480p, 720p · quality: medium, high

### Wan 2.2 Fast (`wan2.2-5b-fast-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · resolution: 480p, 580p, 720p

### Wan 2.5 (`wan2.5-text-to-video`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 480p, 720p, 1080p

### Wan 2.5 Fast (`wan2.5-text-to-video-fast`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 720p, 1080p

### Wan 2.6 (`wan2.6-text-to-video`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 5, 10, 15 · resolution: 720p, 1080p

### Hunyuan (`hunyuan-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Hunyuan Fast (`hunyuan-fast-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Pixverse v4.5 (`pixverse-v4.5-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · resolution: 360p, 540p, 720p, 1080p

### Pixverse v5 (`pixverse-v5-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · resolution: 360p, 540p, 720p, 1080p

### Pixverse v5.5 (`pixverse-v5.5-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · duration: 5, 8, 10 · resolution: 360p, 540p, 720p, 1080p

### Hailuo 02 Standard (`minimax-hailuo-02-standard-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** duration: 6, 10 · resolution: 768P

### Hailuo 02 Pro (`minimax-hailuo-02-pro-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** duration: 6 · resolution: 1080P

### Hailuo 2.3 Pro (`minimax-hailuo-2.3-pro-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** resolution: 1080p

### Hailuo 2.3 Standard (`minimax-hailuo-2.3-standard-t2v`)
- **Prompt:** Text prompt describing the video.
- **Options:** duration: 6, 10

### Sora (`openai-sora`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · resolution: 480p, 720p, 1080p

### Sora 2 (`openai-sora-2-text-to-video`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 10, 15

### Sora 2 Pro (`openai-sora-2-pro-text-to-video`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 10, 15, 25 · resolution: 720p, 1080p

### Vidu v2.0 (`vidu-v2.0-t2v`)
- **Prompt:** The prompt to generate the video
- **Options:** aspect_ratio: 9:16 · duration: 4 · resolution: 1080p

### OVI (`ovi-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16

### Grok Imagine (`grok-imagine-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 9:16, 16:9, 2:3, 3:2, 1:1 · duration: 6, 10, 15 · mode: fun, normal, spicy

### LTX 2 Pro (`ltx-2-pro-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** duration: 6, 8, 10

### LTX 2 Fast (`ltx-2-fast-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** duration: 6, 8, 10, 12, 14, 16, 18, 20

### LTX 2 19B (`ltx-2-19b-text-to-video`)
- **Prompt:** Text prompt describing the video.
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 480p, 720p, 1080p

## Image-to-Image (57 models)

### AI Image Upscaler (`ai-image-upscale`)

### AI Image Face Swap (`ai-image-face-swap`)

### AI Dress Change (`ai-dress-change`)

### AI Background Remover (`ai-background-remover`)

### AI Product Shot (`ai-product-shot`)

### AI Skin Enhancer (`ai-skin-enhancer`)

### AI Color Photo (`ai-color-photo`)

### Flux Kontext Dev I2I (`flux-kontext-dev-i2i`)
- **Prompt:** Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.
- **Example:** "A cozy outdoor coffee shop on a small street, people sitting at tables enjoying drinks, a barista serving coffee, leaves gently falling from nearby trees, and soft warm lighting adding a friendly vibe."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9, 9:21

### AI Product Photography (`ai-product-photography`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Promoting brand in professional look"

### AI Ghibli Style (`ai-ghibli-style`)

### AI Image Extension (`ai-image-extension`)

### AI Object Eraser (`ai-object-eraser`)

### Flux Kontext Pro I2I (`flux-kontext-pro-i2i`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Transform into a digital painting, soft fur texture, dreamy pastel colors"
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 16:21

### Flux Kontext Max I2I (`flux-kontext-max-i2i`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Re-render in a luxury studio setting, reflective surface, high contrast shadows, ad campaign look."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 16:21

### GPT-4o Image To Image (`gpt4o-image-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Convert this sunny park photo into a snowy winter scene, with snow-covered trees, cloudy skies, and people in winter coats."
- **Options:** aspect_ratio: 1:1, 2:3, 3:2

### GPT-4o Edit (`gpt4o-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Replace the barista with a humanoid robot in a sleek metallic design."
- **Options:** aspect_ratio: 1:1, 2:3, 3:2

### Midjourney v7 Image To Image (`midjourney-v7-image-to-image`)
- **Prompt:** The prompt to generate the image
- **Example:** "Make the scene sunrise instead of stormy, with soft lighting and a peaceful mood"
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 1:2, 2:1, 2:3, 3:2, 5:6, 6:5

### Bytedance Seededit v3 (`bytedance-seededit-image`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Change the outfit to a red evening gown with elegant styling, matching the reference image's pose and lighting."

### Midjourney v7 Style Reference (`midjourney-v7-style-reference`)
- **Prompt:** The prompt to generate the image
- **Example:** "A futuristic city built on waterfalls, glowing towers in the mist, colorful sky at dusk, cinematic lighting, hyper-detailed architecture."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 1:2, 2:1, 2:3, 3:2, 5:6, 6:5

### Midjourney v7 Omni Reference (`midjourney-v7-omni-reference`)
- **Prompt:** The prompt to generate the image
- **Example:** "A futuristic samurai girl exploring an ancient overgrown temple in a neon-lit jungle, glowing plants surrounding her, mist in the air, cinematic composition."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 1:2, 2:1, 2:3, 3:2, 5:6, 6:5

### Minimax Image 01 Subject Reference (`minimax-01-subject-reference`)
- **Prompt:** Text prompt describing the image (max 1500 characters).
- **Example:** "Generate the same person dressed in Renaissance-style attire, standing in a candlelit castle hall with ornate tapestries and warm low lighting."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9

### Ideogram Character (`ideogram-character`)
- **Prompt:** Text prompt describing the image (max 1500 characters).
- **Example:** "Create the same character as a medieval knight standing in a candlelit castle corridor, wearing chainmail and holding a torch."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · style: Auto, Realistic, Fiction

### Flux Pulid (`flux-pulid`)
- **Prompt:** Text prompt describing the image (max 1500 characters).
- **Example:** "Recreate the same person in a Renaissance-style painting with ornate collar and soft candlelight ambiance."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4

### Qwen Image Edit (`qwen-image-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Replace the field with a snowy mountain landscape."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9, 9:21, 3:2, 2:3

### Image Effects (`image-effects`)

### Nano Banana Edit (`nano-banana-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Change her facial expression to a confident smile, and adjust the lighting to dramatic blue and purple hues. Keep her hairstyle and outfit consistent across multiple edits."
- **Options:** aspect_ratio: Auto, 1:1, 3:4, 4:3, 9:16, 16:9, 3:2, 2:3, 5:4, 4:5, 21:9

### Ideogram v3 Reframe (`ideogram-v3-reframe`)
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · style: Auto, General, Realistic, Design

### Bytedance Seedream Edit v4 (`bytedance-seedream-edit-v4`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A tranquil shoreline at dawn where waves turn into glowing ribbons of light, painting the sky with dreamlike hues of violet and gold. A figure walks along the edge, leaving footsteps that bloom into luminous flowers, symbolizing imagination flowing seamlessly into reality."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 2:3, 3:2, 21:9 · resolution: 1K, 2K, 4K

### Nano Banana Effects (`nano-banana-effects`)
- **Options:** aspect_ratio: Auto, 1:1, 3:4, 4:3, 9:16, 16:9, 3:2, 2:3, 5:4, 4:5, 21:9

### Flux Kontext Effects (`flux-kontext-effects`)
- **Prompt:** Text prompt describing the image.
- **Example:** "20 years older"

### Flux Redux (`flux-redux`)
- **Prompt:** Text prompt describing the image (max 1500 characters).
- **Example:** "Reimagine the forest cabin as a mystical fantasy retreat at twilight, glowing lanterns hanging from the trees, magical fireflies in the air, cinematic atmosphere with enchanted vibes."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 3:2, 2:3, 21:9, 9:21

### Qwen Image Edit Plus (`qwen-image-edit-plus`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Replace the watch strap with a rich brown leather band, add subtle engravings on the bezel, increase the contrast slightly, and warm the overall lighting to golden-hour tones, keeping reflections realistic."

### Wan2.5 Image Edit (`wan2.5-image-edit`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Reimagine the scene under a raging thunderstorm at night: lightning forks across the sky, illuminating the samurai in stark flashes of white light."

### Higgsfield Soul Image To Image (`higgsfield-soul-image-to-image`)
- **Prompt:** Text prompt describing the image (max 1500 characters).
- **Example:** "Transform into a cinematic editorial portrait — same woman now in a Parisian café at dusk, with soft neon reflections on the window, elegant lighting, subtle film grain. Style preset: Evening Editorial."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 4:5, 5:4, 21:9, 9:21 · quality: medium, high · style: Creatures, Medieval, Spotlight, Giant People, Red balloon, green editorial, Subway, Library, Realistic, DigitalCam, Grillz Selfie, Bleached Brows (+94 more)

### Reve Image Edit (`reve-image-edit`)
- **Prompt:** Text prompt describing the image.
- **Example:** "A photorealistic fantasy portrait, transforming the woman in the image into an elegant high elf. Give her long, gracefully pointed ears that peek through her hair. Her skin has a subtle, ethereal glow. Replace her white blazer and necklaces with ornate, flowing elven robes made of shimmering silver fabric and intricate leaf patterns. The background is a mystical, twilight forest with glowing magical flora. **CRITICAL:** Maintain her exact original pose, serene smiling expression, and facial structure. Cinematic lighting, masterpiece, hyper-detailed."

### Topaz Image Upscale (`topaz-image-upscale`)

### Seedvr2 Image Upscale (`seedvr2-image-upscale`)
- **Options:** resolution: 2k, 4k, 8k

### Qwen Image Edit Plus Lora (`qwen-image-edit-plus-lora`)

### Nano Banana Pro Edit (`nano-banana-pro-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Keep the same scene and subject, but change the lighting to warm golden sunset tones, remove the neon signs, add soft sunlight beams from the side, enhance surface details, keep reflections subtle and natural."
- **Options:** aspect_ratio: 1:1, 3:4, 4:3, 9:16, 16:9, 3:2, 2:3, 5:4, 4:5, 21:9 · resolution: 1k, 2k, 4k

### Image Passthrough (`image-passthrough`)

### Kling O1 Edit Image (`kling-o1-edit-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Replace the hanging lanterns with floating bioluminescent orbs that emit soft cyan light, keep the garden composition and city reflections unchanged, ensure the orbs cast subtle cyan rim-light on nearby leaves and glass, preserve overall twilight mood and depth of field."
- **Options:** aspect_ratio: auto, 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2, 21:9 · resolution: 1k, 2k

### Flux 2 Dev Edit (`flux-2-dev-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Replace the floating stained-glass cathedral with a colossal crystal tree glowing from within, while keeping the stormy sky, ocean waves, rainbow reflections, and dramatic lighting intact."

### Flux 2 Flex Edit (`flux-2-flex-edit`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Replace the molten gold in the lower chamber with a swirling vortex of glowing sapphire mist, keep the crystal panels, star map, orbiting metallic rings, and aurora sky unchanged, ensure the new mist casts cool blue highlights and interacts naturally with the surrounding lightning."
- **Options:** aspect_ratio: auto, 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2 · resolution: 1k, 2k

### Flux 2 Pro Edit (`flux-2-pro-edit`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Replace the central spherical chronometer with a floating crystalline lotus emitting soft golden light, keep the asteroid chamber, star charts, cosmic dust streams, and prismatic beams unchanged, ensure the lotus casts warm highlights and seamlessly integrates with the scene’s lighting."
- **Options:** aspect_ratio: auto, 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2 · resolution: 1k, 2k

### Vidu Q2 Reference To Image (`vidu-q2-reference-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Create a new scene where the masked wanderer stands inside an ancient stone observatory illuminated by rotating celestial beams; preserve the character’s clothing style and silhouette while adding glowing runes carved into the walls, mist swirling across the floor, and a dramatic cosmic light shaft from above; cinematic composition, high detail."
- **Options:** aspect_ratio: auto, 16:9, 9:16, 1:1, 4:3, 3:4, 2:3, 3:2, 21:9 · resolution: 1k, 2k, 4k

### Bytedance Seedream v4.5 Edit (`bytedance-seedream-v4.5-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Replace the glowing amethyst flame at the tower’s peak with a levitating orb of swirling turquoise water, keeping the spiral tower, crystalline desert, floating shards, and aurora-lit sky unchanged; ensure the water orb emits cool reflections and integrates naturally with the existing lighting."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2, 21:9 · quality: basic, high

### Qwen Image Edit 2511 (`qwen-image-edit-2511`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Replace the glass observatory with a floating bronze astrolabe composed of interlocking rings and engraved symbols, keep the glowing desert, dusk sky, dust trails, and lighting unchanged; ensure the bronze surface reflects the warm sunset tones naturally and integrates seamlessly with the scene."

### Wan2.6 Image Edit (`wan2.6-image-edit`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Replace the glowing crystal spires with towering living trees made of luminous jade leaves and silver bark, keep the floating citadel structure, ocean reflections, mist, moonlight, and twilight color palette unchanged; ensure the new trees cast soft green highlights that blend naturally with the existing lighting."

### Qwen Text To Image 2512 (`qwen-text-to-image-2512`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "A colossal biomechanical whale swimming slowly through a vast sky made of soft clouds and fractured light. Its translucent body reveals glowing internal organs shaped like rotating gears and flowing energy veins. Below it, a sprawling patchwork of farmland and rivers curves with the planet’s surface, catching reflections from the whale’s luminous glow. Long fabric banners trail from the whale’s fins, fluttering gently in the wind like ceremonial streamers. The camera angle is wide and aerial, emphasizing scale and serenity. Soft sunrise colors, cinematic depth, ultra-detailed surreal sci-fi atmosphere."

### Gpt Image 1.5 Edit (`gpt-image-1.5-edit`)
- **Prompt:** Text prompt for edit image.
- **Example:** "Replace the abandoned car with a sleek autonomous electric vehicle made of brushed metal and soft glowing panels, keep the desert highway, sunset lighting, heat distortion, power lines, and approaching storm unchanged; ensure reflections and shadows match the original environment naturally."
- **Options:** aspect_ratio: 1:1, 2:3, 3:2 · quality: low, medium, high

### Grok Imagine Image To Image (`grok-imagine-image-to-image`)
- **Prompt:** Text prompt describing the image.
- **Example:** "Replace the arriving train with a silent magnetic levitation transit pod made of matte white composite and glass, keep the platform, people, lighting, reflections, and urban environment unchanged; ensure the new vehicle fits naturally into the scene with correct scale, shadows, and motion blur."

### Api Node (`Api Node`)

### Flux 2 Klein 4b Edit (`flux-2-klein-4b-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Add a tiny blue knitted scarf around the kitten’s neck, keep the kitten’s pose, table, lighting, and cozy indoor environment unchanged; make the scarf soft and cute, fitting naturally without covering the kitten’s face."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9, 9:21

### Flux 2 Klein 9b Edit (`flux-2-klein-9b-edit`)
- **Prompt:** Text prompt describing the image, what you want the final edited image to look like.
- **Example:** "Add a small red bow tie around the puppy’s neck, slightly fluffy fabric texture, keep the puppy’s pose, facial expression, sofa, lighting, and living room environment unchanged; ensure the bow tie matches the warm lighting and looks naturally placed."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9, 9:21

### Add Image Watermark (`add-image-watermark`)

### Nano Banana 2 Edit (`nano-banana-2-edit`)
- **Prompt:** Positive prompt for generation.
- **Example:** "Transform the portrait into a cyberpunk style with neon lighting, metallic accessories, and a rain-soaked city background, maintaining the subject's facial features."
- **Options:** aspect_ratio: 1:1, 1:4, 1:8, 2:3, 3:2, 3:4, 4:1, 4:3, 4:5, 5:4, 8:1, 9:16 (+3 more) · resolution: 1k, 2k, 4k

### Seedream 5.0 Edit (`seedream-5.0-edit`)
- **Prompt:** Text prompt describing the desired modification.
- **Example:** "Change the daytime forest scene to a moonlit winter landscape with shimmering snow on the trees and a soft blue glow from a distant cottage window."
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 4:3, 3:4, 2:3, 3:2, 21:9 · quality: basic, high

## Image-to-Video (61 models)

### AI Video Effects (`generate_wan_ai_effects`)
- **Prompt:** The prompt to insert into the predefined prompt template for the selected effect.
- **Example:** "a cute kitten"
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · duration: 5, 10 · resolution: 480p, 720p · quality: medium, high

### Motion Controls (`generate_wan_ai_effects`)
- **Prompt:** The prompt to insert into the predefined prompt template for the selected effect.
- **Example:** "a blueberry person"
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · duration: 5, 10 · resolution: 480p, 720p · quality: medium, high

### VFX (`generate_wan_ai_effects`)
- **Prompt:** The prompt to insert into the predefined prompt template for the selected effect.
- **Example:** "a Mercedes bench car"
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · duration: 5, 10 · resolution: 480p, 720p · quality: medium, high

### Veo3 Image To Video (`veo3-image-to-video`)
- **Prompt:** Text prompt describing the desired video content.
- **Example:** "On a neon-lit street corner, a hyped street performer with a mic shouts: 'Yo! Big drop today! VEO3 just launched on muapi!' A crowd cheers as holograms of videos burst into the air and the muapi logo spins above."
- **Options:** aspect_ratio: 16:9, 9:16

### Veo3 Fast Image To Video (`veo3-fast-image-to-video`)
- **Prompt:** Text prompt describing the desired video content.
- **Example:** "A spaceship hovers over Earth. A digital billboard beams out: 'MuAPI is broadcasting creativity across the galaxy.' A robot host floats in zero gravity holding a prompt card: 'Let’s turn this into a story.' Suddenly, video panels fly around the ship with generated content."
- **Options:** aspect_ratio: 16:9, 9:16

### Runway Image To Video (`runway-image-to-video`)
- **Prompt:** The prompt to be used to generate a video
- **Example:** "The camera smoothly zooms in on the sleek, futuristic race car as it speeds through a neon-lit urban tunnel at twilight, its glossy white surface reflecting the vibrant pink and blue lights streaking past. The precise detailing of the car’s aerodynamic curves and glowing accents is highlighted as droplets of water spray from the spinning tires, adding a palpable sense of motion and intensity. The driver’s black helmet, contrasted against the car’s gleaming body, remains sharply in focus, emphasizing the thrilling high-speed chase through the city. The blurred cityscape and illuminated digital billboards in the background create a high-tech, cyberpunk atmosphere, intensifying the scene’s adrenaline and futuristic vibe."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · duration: 5, 8 · resolution: 720p, 1080p

### Wan2.1 Image To Video (`wan2.1-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Animate the girl in the painting to blink and look around while her hair moves gently in the wind."
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 480p, 720p · quality: medium, high

### Midjourney v7 Image To Video (`midjourney-v7-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Add slow drifting fog, glowing mushrooms pulsating softly, and subtle camera zoom"
- **Options:** aspect_ratio: 1:1, 16:9, 9:16, 3:4, 4:3, 1:2, 2:1, 2:3, 3:2, 5:6, 6:5 · resolution: 480p, 1080p

### Hunyuan Image To Video (`hunyuan-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "The camera begins with a slow, deliberate zoom out from the figure standing on the rain-soaked rooftop, revealing the sleek, armored silhouette clutching a glowing katana that pulses with ominous red light. The deep blues and purples of the wet cityscape set a moody, cyberpunk atmosphere, with neon signs in vibrant pinks, blues, and oranges casting reflections on the glistening surfaces below. The mist and rain softly blur the distant buildings and streetlights, emphasizing the isolation of the lone warrior framed against the sprawling urban expanse. As the camera pulls back, the subtle hum of the futuristic city grows louder, immersing the viewer in a world of tension and anticipation, where danger lurks in the glowing depths of the rain-drenched streets."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Kling v2.1 Master I2V (`kling-v2.1-master-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Animates wind effects, camera panning, and subtle movements like blinking or background motion, transforming the image into a compelling cinematic shot."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Kling v2.1 Standard I2V (`kling-v2.1-standard-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "A female explorer stands at the edge of a cliff overlooking a dense jungle, her hair and cape rustling gently in the wind as the dramatic sunset casts warm, golden hues across the sky and landscape, capturing a moment of awe and adventure."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Kling v2.1 Pro I2V (`kling-v2.1-pro-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "A cyberpunk woman with neon tattoos stands in a rainy alley as glowing signs reflect vividly in puddles around her. Her coat flutters slightly in the breeze, and she makes subtle head movements, capturing the moody, futuristic atmosphere without any scene changes."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Wan2.2 Image To Video (`wan2.2-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "A close-up video of a young woman smiling gently in the rain, with raindrops glistening on her face and eyelashes. The camera focuses on the delicate details of her expression and the shimmering water droplets, while soft light softly reflects off her skin, emphasizing the rainy atmosphere."
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 480p, 720p · quality: medium, high

### Runway Act Two I2V (`runway-act-two-i2v`)
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4, 21:9

### Pixverse v4.5 I2V (`pixverse-v4.5-i2v`)
- **Prompt:** The prompt to generate the video
- **Example:** "A cat dressed in a sharp business suit stands confidently on a TED Talk stage, delivering an engaging lecture on quantum physics. The audience is filled with attentive dogs wearing glasses, reacting thoughtfully to the presentation. The video features dramatic camera zooms that highlight the cat speaker’s expressions and the intrigued faces of the canine audience, maintaining the setting and characters without altering the scene."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · resolution: 360p, 540p, 720p, 1080p

### Vidu v2.0 I2V (`vidu-v2.0-i2v`)
- **Prompt:** The prompt to generate the video
- **Example:** "A baby dragon wearing a tiny cape attempts to fly, wobbling uncertainly in the air with playful flaps of its wings, set against a bright and cheerful background. Light, upbeat music plays throughout, capturing the dragon's joyful effort. The video ends with the baby dragon gently crashing in a cute and harmless tumble, smiling and unfazed."
- **Options:** aspect_ratio: 16:9, 1:1 · duration: 4 · resolution: 360p, 720p, 1080p

### Vidu Q1 Reference (`vidu-q1-reference`)
- **Prompt:** Text prompt describing the desired video content.
- **Example:** "Animate the character walking through the foggy forest at dawn, swinging the sword gracefully. Add cinematic camera pan and soft ambient lighting."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Minimax Hailuo 02 Standard I2V (`minimax-hailuo-02-standard-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Animate her looking out at the horizon as gentle waves crash, with her hair moving in the wind. Light, smooth motion, perfect for social clips."
- **Options:** duration: 6, 10 · resolution: 512P, 768P

### Minimax Hailuo 02 Pro I2V (`minimax-hailuo-02-pro-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Transform this still image into a dramatic cinematic sequence: the scholar walks slowly through an ancient library where shelves tower endlessly into the shadows. The lantern’s flame flickers, casting moving patterns across scrolls and statues. Dust motes dance in golden light as the camera glides smoothly behind him, then pans upward to reveal an infinite expanse of glowing constellations painted across the ceiling that begin to shimmer and move as if alive."
- **Options:** duration: 6 · resolution: 1080p

### Video Effects (`video-effects`)

### Seedance Lite I2V (`seedance-lite-i2v`)
- **Prompt:** The prompt to generate the video
- **Example:** "A lively dog is running swiftly across a sunlit park, with green trees softly blurred in the background to emphasize quick motion, capturing the energetic and joyful movement during the day."
- **Options:** resolution: 480p, 720p, 1080p

### Seedance Pro I2V (`seedance-pro-i2v`)
- **Prompt:** The prompt to generate the video
- **Example:** "A slow cinematic pan following a knight riding through a dense, foggy forest at dawn, with dramatic lighting casting long shadows and soft rays filtering through the misty trees, emphasizing the mysterious and atmospheric mood."
- **Options:** resolution: 480p, 720p, 1080p

### Pixverse v5 I2V (`pixverse-v5-i2v`)
- **Prompt:** The prompt to generate the video
- **Example:** "Animate the glowing stag slowly walking forward, fireflies drifting in the air, soft mist rolling across the clearing, camera gently circling around for a magical cinematic motion."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · resolution: 360p, 540p, 720p, 1080p

### Seedance Lite Reference Video (`seedance-lite-reference-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "The businessman walks towards the sports car on the rooftop, places his hand on the hood, and gazes at the glowing skyline as the camera circles around dramatically, capturing the neon-lit atmosphere in ultra-realism."
- **Options:** resolution: 480p, 720p

### Wan2.1 Reference Video (`wan2.1-reference-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "The motorcycle driving through the neon tunnel, reflections glowing on its body, dynamic tracking shot, cinematic product ad style."
- **Options:** aspect_ratio: 16:9, 9:16 · resolution: 480p, 720p

### Kling v2.5 Turbo Pro I2V (`kling-v2.5-turbo-pro-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Animate subtle cloak movement, glowing energy pulsing from the staff, storm clouds rolling above, camera orbiting slightly to add depth and atmosphere."

### Wan2.5 Image To Video (`wan2.5-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Animate the scene: camera slowly dollies forward toward the robot, neon city lights begin to flicker, soft reflections shift across the dome glass, twilight deepens into night with subtle ambient glow. The robot raises its head and speaks in a clear futuristic voice: ‘WAN 2.5 is now available on the MuAPI app.’"
- **Options:** resolution: 480p, 720p, 1080p

### Wan2.5 Image To Video Fast (`wan2.5-image-to-video-fast`)
- **Prompt:** The prompt to generate the video
- **Example:** "The camera slowly pulls back from the portrait, revealing the rooftop garden swaying in the breeze, clouds drifting across the orange-pink sky. The city lights begin to flicker on in the distance as the sun sets. She gazes at the horizon and softly says: “Every ending feels like the start of something new.” Natural ambient sounds of wind and faint city life in the background."
- **Options:** resolution: 720p, 1080p

### Openai Sora 2 Image To Video (`openai-sora-2-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Camera pans along the platform as the bullet train doors open, passengers step forward with rolling suitcases. Footsteps and soft chatter fill the air. A female announcer says: ‘Train number 2245 to Tokyo is now departing from platform 3.’ Wheels screech lightly as the train starts moving."
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 10, 15

### Ovi Image To Video (`ovi-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Camera: static medium shot. The scientist speaks: <S>We have discovered life beyond Earth.<E> <AUDCAP>Soft electronic hum, distant Beep of instruments<ENDAUDCAP>"

### Openai Sora 2 Pro Image To Video (`openai-sora-2-pro-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Scene: Submerged coral clearing, soft light filtering from above.
Characters: Tiny jellyfish with monocle and top hat, hosting tea for small seahorses.
Action: Jellyfish floats and pours tea → bubbles rise slowly; seahorses sip → tiny octopus clumsily serves cake.
Camera: Wide underwater → tracking floating jellyfish → macro on bubbles.
Look & Lighting: Aqua-blue palette; subtle caustics on sand; shimmering reflections on water surfaces.
Motion/Physics: Water currents gently sway characters; bubbles rise naturally; floating cakes wobble lightly.
Audio: Bubbling water + faint harp melody; line: “Tea, my dear friends, before it drifts away.”"
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 10, 15, 25 · resolution: 720p, 1080p

### Leonardoai Motion 2.0 (`leonardoai-motion-2.0`)
- **Prompt:** Text prompt describing the video.
- **Example:** "A diver swimming through a coral reef, colorful fish darting around, sunlight filtering through the water, slow-motion effect."
- **Options:** aspect_ratio: 16:9, 9:16

### Higgsfield Dop Image To Video (`higgsfield-dop-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Rotate the camera around the scene."

### Veo3.1 Image To Video (`veo3.1-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Scene: Giant floating library orbiting in zero-gravity space.
Characters: Astronaut-librarian flipping glowing pages suspended midair.
Action: Camera rotates 360° around drifting books → zooms through a floating page into a nebula outside window.
Camera: Orbit + push-through transition.
Lighting: Cool cosmic ambient with warm page glows; rim lighting on suit.
Motion: Slow rotational drift; pages react with fluid inertia.
Audio: Ethereal synth pads + book rustle in vacuum hush.
Mood: Awe, wonder, intellectual calm.
Line: “Wow veo3.1 launched in Muapiapp. Let's go!”"
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 8 · resolution: 1080p

### Veo3.1 Fast Image To Video (`veo3.1-fast-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Scene: Lantern festival by the river at night.
Characters: Young boy with his grandmother.
Action: Camera starts behind them → tracks one lantern downstream → lift to sky full of lights.
Lighting: Warm candlelight vs cool night reflections.
Audio: Gentle music, water flow.
Dialogue:
Grandmother: “Every lantern carries a wish.”
Boy: “Then mine’s for you to stay forever.”
Grandmother (smiling): “I’ll be right there, glowing among them.”"
- **Options:** aspect_ratio: 16:9, 9:16 · duration: 8 · resolution: 1080p

### Veo3.1 Reference To Video (`veo3.1-reference-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "A small robotic fox exploring a sun-drenched enchanted forest. The fox hops across a sparkling stream, pauses on mossy rocks, and looks curiously at glowing fireflies. Cinematic camera pans follow the fox from behind, then orbit slightly to reveal sunbeams filtering through the canopy. Warm dappled lighting with volumetric light rays and soft particle effects. Gentle ambient forest sounds and faint magical chimes. Dialogue: ‘Everything shines differently under the forest light…’"
- **Options:** duration: 8 · resolution: 720p, 1080p

### Seedance Pro I2V Fast (`seedance-pro-i2v-fast`)
- **Prompt:** The prompt to generate the video
- **Example:** "The cyberpunk samurai turns slowly toward the camera, raindrops gliding off his glowing armor, neon lights reflecting on wet metal, camera pans around him in a slow 360°, subtle lightning flashes illuminate the skyline."
- **Options:** resolution: 480p, 720p, 1080p

### Ltx 2 Pro Image To Video (`ltx-2-pro-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "An ancient stone portal deep in an enchanted forest, glowing runes, beams of sunlight breaking through the canopy, cinematic tracking shot, warm colour grading."
- **Options:** duration: 6, 8, 10

### Ltx 2 Fast Image To Video (`ltx-2-fast-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Image of two explorers standing atop a dune. Now the viewpoint shifts: camera slowly dollies backward while sun rises behind them, sand drifts around feet, warm golden light, soft wind in audio."
- **Options:** duration: 6, 8, 10, 12, 14, 16, 18, 20

### Vidu Q2 Reference (`vidu-q2-reference`)
- **Prompt:** The prompt to generate the video
- **Example:** "The female explorer walks slowly across the alien terrain, crystals glimmering around her. The camera glides beside her as light from twin suns scatters across her reflective suit. Wind stirs the mist as she looks up toward the horizon, where a colossal planet looms above — evoking awe and wonder."
- **Options:** aspect_ratio: 16:9, 9:16, 4:3, 3:4, 1:1 · resolution: 360p, 540p, 720p, 1080p

### Vidu Q2 Turbo Start End Video (`vidu-q2-turbo-start-end-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "The camera begins behind the traveler standing amid the misty ancient ruins. Leaves swirl in the air as golden light flickers. A surge of energy surrounds the traveler — ruins start to dissolve into bright particles. The environment morphs into a neon-lit futuristic city as the traveler continues walking forward, entering the new world."
- **Options:** resolution: 720p, 1080p

### Vidu Q2 Pro Start End Video (`vidu-q2-pro-start-end-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Camera begins behind the cabin as snowflakes drift through pale dawn light. Warm sunlight pierces the mist — the snow slowly melts, trees turn green, and the ground blossoms with flowers. The air brightens into a spring sunrise as birds take flight over the cabin, symbolizing rebirth and renewal."
- **Options:** resolution: 720p, 1080p

### Minimax Hailuo 2.3 Pro I2V (`minimax-hailuo-2.3-pro-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "The camera slowly moves around the woman as the wind gently sways the tall grass. Her hair flows with the breeze, sunlight flickering through passing clouds. The atmosphere feels calm, nostalgic, and cinematic."
- **Options:** resolution: 1080p

### Minimax Hailuo 2.3 Standard I2V (`minimax-hailuo-2.3-standard-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Camera slowly moves forward over the lake surface as light wind ripples the water. The clouds drift across the mountains, and sunlight flickers on the waves, creating a peaceful cinematic mood."
- **Options:** duration: 6, 10

### Minimax Hailuo 2.3 Fast (`minimax-hailuo-2.3-fast`)
- **Prompt:** Text prompt describing the video.
- **Example:** "The camera gently moves around the woman as snowflakes drift through the air. Her expression shifts slightly as the wind brushes her hair. The background lights shimmer softly, creating a calm cinematic mood."
- **Options:** duration: 6, 10

### Kling v2.5 Turbo Std I2V (`kling-v2.5-turbo-std-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Animate subtle cloak movement, glowing energy pulsing from the staff, storm clouds rolling above, camera orbiting slightly to add depth and atmosphere."

### Grok Imagine Image To Video (`grok-imagine-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Camera glides through vines toward temple entrance, mist disperses as sunlight pierces canopy, birds fly off, subtle dust motes in the air, adventure-style cinematic score."
- **Options:** duration: 6, 10, 15 · mode: fun, normal, spicy

### Kling O1 Image To Video (`kling-o1-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "A gentle dolly forward toward the cabin as morning light intensifies, mist lifts in streaks, subtle water ripples, birds take flight, warm golden hour soundscape."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · duration: 5, 10

### Kling O1 Reference To Video (`kling-o1-reference-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Cinematic orbit camera move around the pilot in a futuristic hangar, holographic lights flickering, armor reflections shifting, soft mechanical ambience."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1

### Kling v2.6 Pro I2V (`kling-v2.6-pro-i2v`)
- **Prompt:** The prompt to generate the video
- **Example:** "Slow cinematic orbit around the floating obsidian throne, holographic runes pulsing gently, drifting quartz shards rotating with soft parallax, molten crystal canyon glowing brighter with movement, and subtle particle storms rising toward the cosmic vortex; maintain original lighting, style, and atmosphere."
- **Options:** duration: 5, 10

### Pixverse v5.5 I2V (`pixverse-v5.5-i2v`)
- **Prompt:** The prompt to generate the video
- **Example:** "Slow upward camera glide along the staircase, lanterns gently swaying, stardust drifting in soft spirals, nebula clouds subtly shifting, and the cosmic gateway pulsing with rhythmic light; maintain original colors, composition, and celestial atmosphere with smooth cinematic motion."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 4:3, 3:4 · duration: 5, 8, 10 · resolution: 360p, 540p, 720p, 1080p · style: none, anime, 3d_animation, clay, comic, cyberpunk

### Wan2.2 Spicy Image To Video (`wan2.2-spicy-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Animate the scene with intense fiery motion—lava cracking and flowing down the phoenix wings, embers drifting upward, volcanic smoke swirling dramatically, floating stones shifting with parallax depth; camera performs a slow power-shot push-in toward the phoenix statue while preserving the glowing, high-contrast cinematic atmosphere."
- **Options:** duration: 5, 8 · resolution: 480p, 720p

### Wan2.6 Image To Video (`wan2.6-image-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Add slow cinematic camera movement circling the floating lighthouse, orbiting symbol rings rotating gently with parallax depth, ocean waves shimmering and moving naturally, clouds drifting and lightning flashing subtly in the distance, and the lighthouse beam pulsing softly while preserving the original lighting and dramatic mood."
- **Options:** duration: 5, 10, 15 · resolution: 720p, 1080p

### Kling O1 Standard Image To Video (`kling-o1-standard-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Add gentle camera drift forward with slight parallax depth, waterfalls flowing softly, clouds slowly moving beneath the island, birds gliding naturally through the scene, and sunlight shifting subtly while maintaining the calm cinematic mood and original lighting."
- **Options:** duration: 5, 10

### Kling O1 Standard Reference To Video (`kling-o1-standard-reference-to-video`)
- **Prompt:** The prompt to generate the video
- **Example:** "Blend the reference scenes into a single cinematic shot with gentle forward camera movement, soft parallax depth between the bridge and forest valley, fog drifting slowly above the river, leaves swaying lightly in the breeze, and sunlight shifting subtly while maintaining a calm, realistic atmosphere."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1 · duration: 5, 10

### Seedance v1.5 Pro I2V (`seedance-v1.5-pro-i2v`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Add a slow cinematic orbit around the floating archive, gentle parallax between cloud layers and spires, flowing data streams pulsing softly, fog drifting naturally, and sky colors deepening slightly while preserving the original lighting, scale, and cinematic mood."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9 · resolution: 480p, 720p, 1080p

### Seedance v1.5 Pro I2V Fast (`seedance-v1.5-pro-i2v-fast`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Add gentle forward camera movement toward the floating observatory, subtle parallax between clouds and structure, soft cloud drift below, interior window lights glowing steadily, and sunlight rays shifting slightly while keeping motion smooth, minimal, and fast."
- **Options:** aspect_ratio: 16:9, 9:16, 1:1, 3:4, 4:3, 21:9 · resolution: 720p, 1080p

### Ltx 2 19b Image To Video (`ltx-2-19b-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "Animate the scene so the camera slowly pushes toward the billboard, the text characters on the woman’s face subtly scrolling and re-forming, rain falling continuously, reflections on the wet road shifting as car headlights flicker, pedestrians making small natural movements while the city lights pulse softly; maintain realistic motion, urban mood, and cinematic pacing."
- **Options:** resolution: 480p, 720p, 1080p

### Kling v3.0 Pro Image To Video (`kling-v3.0-pro-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "The camera begins on the railway station platform beside a stationary train as morning sunlight filters through the roof. Passengers make small natural movements while the train doors are open. The camera moves forward and enters the train, transitioning smoothly into a window-seat point of view. As the doors close, the train starts moving. The view shifts fully to the window, showing the city passing by outside with gentle motion blur, buildings and trees sliding past. Sunlight reflects on the glass, faint interior reflections appear, and the ride feels calm and realistic with smooth, cinematic motion."

### Kling v3.0 Standard Image To Video (`kling-v3.0-standard-image-to-video`)
- **Prompt:** Text prompt describing the video.
- **Example:** "The hamster begins on the left side of the tabletop and quickly runs across the surface toward the right. Its tiny legs move rapidly, body bouncing slightly with natural motion. As it runs, the sunflower seeds blur slightly beneath it. The hamster slows near the bowl, stops, and stands upright to grab a seed. The camera remains fixed, depth of field stays shallow, and lighting remains soft and consistent for a realistic, cute result."

### Seedance 2.0 I2V (`seedance-v2.0-i2v`)
- **Prompt:** The prompt to guide video generation from the image.
- **Options:** aspect_ratio: 16:9, 9:16, 4:3, 3:4 · duration: 5, 10, 15 · quality: high, basic

## Video-to-Video (1 models)

### AI Video Watermark Remover (`video-watermark-remover`)

## Lip Sync (image/video input) (9 models)

### Infinite Talk (`infinitetalk-image-to-video`) · image
- **Options:** resolution: 480p, 720p

### Wan 2.2 Speech to Video (`wan2.2-speech-to-video`) · image
- **Options:** resolution: 480p, 720p

### LTX 2.3 Lipsync (`ltx-2.3-lipsync`) · image
- **Options:** resolution: 480p, 720p, 1080p

### LTX 2 19B Lipsync (`ltx-2-19b-lipsync`) · image
- **Options:** resolution: 480p, 720p, 1080p

### Sync Lipsync (`sync-lipsync`) · video

### LatentSync (`latentsync-video`) · video

### Creatify Lipsync (`creatify-lipsync`) · video

### Veed Lipsync (`veed-lipsync`) · video

### Infinite Talk V2V (`infinitetalk-video-to-video`) · video
- **Options:** resolution: 480p, 720p

---
*221 models total.*
