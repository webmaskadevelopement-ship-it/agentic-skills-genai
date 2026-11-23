#!/usr/bin/env python3
"""Write comp/edl.json for the Vox Collage template.
usage: python3 kit/make_edl.py [1:1|9:16|16:9|4:5] > comp/edl.json"""
import json, sys
SIZES = {"1:1": (1080, 1080), "9:16": (1080, 1920), "16:9": (1920, 1080), "4:5": (1080, 1350)}
aspect = sys.argv[1] if len(sys.argv) > 1 else "1:1"
if aspect not in SIZES:
    sys.exit(f"unknown aspect {aspect}; use one of {', '.join(SIZES)}")
w, h = SIZES[aspect]
edl = {
    "_about": f"Vox Collage animation, 15 s, {w}x{h}, 30 fps. The 'voxcollage' special in comp/fx.js draws everything.",
    "canvas": {"w": w, "h": h, "fps": 30, "frames": 450, "bg": "#e8e3da"},
    "fonts": [
        {"family": "Abril", "url": "comp/fonts/AbrilFatface-Regular.ttf"},
        {"family": "Plex", "url": "comp/fonts/IBMPlexMono-Regular.ttf", "weight": "400"},
        {"family": "Plex", "url": "comp/fonts/IBMPlexMono-Medium.ttf", "weight": "500"},
        {"family": "Anton", "url": "comp/fonts/Anton-Regular.ttf"},
    ],
    "shots": [{"t0": 0, "t1": 15.0, "special": {"type": "voxcollage"}}],
    "post": {"grain": {"amt": 0.22}},
    "sfx": {"auto": False},
    "audio": {"src": "audio/sfx.m4a", "start": 0, "sfx": False},
}
print(json.dumps(edl, indent=1))
