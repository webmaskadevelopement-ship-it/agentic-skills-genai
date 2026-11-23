#!/bin/bash
# Vox Collage render helper. Run from the workspace root (the folder with comp/ and kit/).
#   bash kit/render.sh stills ["0.2s,1.4s,..."]   QA sheet -> qa/stills.jpg (look at it with image_paths)
#   bash kit/render.sh full                       SFX bed + full render + capped delivery file -> out/final.mp4
set -e
export HF_WORKFLOWS=${HF_WORKFLOWS:-/home/user/.higgsfield/workflows}
RR=$HF_WORKFLOWS/katana/scripts
case "$1" in
  stills)
    python3 $RR/comp/render.py render . --no-sfx --audio none \
      --stills "${2:-0.15s,1.4s,2.5s,3.9s,5.6s,6.6s,7.8s,9.4s,10.4s,11.9s,12.9s,14.8s}" \
      --sheet qa/stills.jpg --cols 4 --tile-w 300 | tail -1 | cut -c1-160 ;;
  full)
    mkdir -p audio out
    python3 $RR/sfx.py bed . --cues kit/cues.json --dur 15.0 --out audio/sfx_bed.wav | tail -1
    ffmpeg -v error -y -i audio/sfx_bed.wav -af "aresample=48000,volume=6dB,alimiter=limit=0.84:level=disabled" -c:a aac -b:a 256k audio/sfx.m4a
    python3 $RR/comp/render.py render . --no-sfx --aac | tail -1 | cut -c1-200
    python3 $RR/deliver.py out/comp.mp4 out/film.mp4 | tail -1 | cut -c1-200
    ffmpeg -v error -y -i out/film.mp4 -c copy -movflags +faststart out/final.mp4
    ffprobe -v error -show_entries stream=codec_type,width,height,nb_frames -show_entries format=duration,size -of compact=p=0:nk=1 out/final.mp4 | tr '\n' ' '; echo
    echo "DONE out/final.mp4" ;;
  *) echo "usage: bash kit/render.sh stills [times] | full"; exit 2 ;;
esac
