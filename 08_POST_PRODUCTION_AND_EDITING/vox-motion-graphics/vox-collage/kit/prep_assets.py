#!/usr/bin/env python3
"""Prepare generated images for the Vox Collage template.

  cut  SRC NAME [--max 2400]        background-removed PNG -> comp/img/NAME.png
                                    (solidifies half-transparent insides, keys out leftover green,
                                     trims to the subject; real holes such as a ring building stay open)
  flat SRC NAME [--crop 0.03] [--max 1600]   photo/texture -> comp/img/NAME.jpg
  tip  NAME                         print where the top of a cut-out is (fraction of its width),
                                    use it as "heroTip" (hero.png) or "lensX"/"lensY" (hands.png)
"""
import sys, argparse
import numpy as np
from PIL import Image
from scipy import ndimage as nd

OUT = "comp/img/"

def solidify(a, thr=40, er=4):
    m = a > thr
    core = nd.binary_erosion(m, iterations=er)
    a2 = a.copy(); a2[core] = 255
    a2[~nd.binary_dilation(m, iterations=2)] = 0
    return a2

def cut(src, name, maxdim):
    arr = np.array(Image.open(src).convert("RGBA")).astype(np.int32)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    green = (g > r + 28) & (g > b + 18) & (g > 60)
    a = np.where(green, 0, arr[..., 3]).astype(np.uint8)
    a = solidify(a)
    a[green] = 0
    arr = arr.astype(np.uint8); arr[..., 3] = a
    ys, xs = np.where(a > 8)
    if not len(ys):
        sys.exit(f"{src}: nothing left after cutting, check the background removal")
    y0, y1, x0, x1 = max(ys.min() - 6, 0), ys.max() + 7, max(xs.min() - 6, 0), xs.max() + 7
    im = Image.fromarray(arr[y0:y1, x0:x1])
    if max(im.size) > maxdim:
        im.thumbnail((maxdim, maxdim), Image.LANCZOS)
    im.save(OUT + name + ".png", optimize=True)
    print(name, im.size, "aspect %.3f" % (im.size[0] / im.size[1]))

def flat(src, name, crop, maxdim):
    im = Image.open(src).convert("RGB"); w, h = im.size
    im = im.crop((int(w * crop), int(h * crop), int(w * (1 - crop)), int(h * (1 - crop))))
    im.thumbnail((maxdim, maxdim), Image.LANCZOS)
    im.save(OUT + name + ".jpg", quality=89)
    print(name, im.size)

def tip(name):
    a = np.array(Image.open(OUT + name + ".png"))[..., 3]
    h, w = a.shape; ys, xs = np.where(a > 128); top = ys.min()
    print(name, "top x=%.3f y=%.3f" % (xs[ys < top + 6].mean() / w, top / h))

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["cut", "flat", "tip"])
    p.add_argument("src"); p.add_argument("name", nargs="?")
    p.add_argument("--max", type=int, default=0); p.add_argument("--crop", type=float, default=0.03)
    a = p.parse_args()
    if a.mode == "cut": cut(a.src, a.name, a.max or 2400)
    elif a.mode == "flat": flat(a.src, a.name, a.crop, a.max or 1600)
    else: tip(a.src)
