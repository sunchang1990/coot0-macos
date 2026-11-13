#!/usr/bin/env python
"""Make the splash images for the macOS build from the original coot-0.9.8.96.png (580 x 478).

  coot-0.9.8.96.png   580 x 478   same size as the original, new tagline (used by Coot's own start-up window when the native splash is off)
  coot-splash@2x.png  1160 x 956  high-resolution version, shown by bin/coot-splash at 580 x 478 points (crisp on Retina screens)

What is done (the original artwork is only 580 x 478 pixels; nothing can add real detail to the painting itself):
  * the old tagline ("Goodbye Old Coot") and the black "Version ..." / "Marina Bay" lettering are taken out of the picture
    (filled from their surroundings) and drawn again as crisp 2x text: the tagline in Open Sans Italic, the black lettering from the
    original letter shapes with sharpened edges;
  * the painting is enlarged 2x with a Lanczos filter and a light unsharp mask.
usage: make_splash.py ORIGINAL.png OUTDIR "tagline" [OpenSansItalic.ttf]
"""
import sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy import ndimage as ndi

def fill_masked(rgb, mask, iters=60):
    """fill masked pixels from the unmasked neighbours (repeated 5x5 means: smooth, texture-free)"""
    out = rgb.astype(np.float64).copy(); known = ~mask
    for _ in range(iters):
        if known.all(): break
        w = ndi.uniform_filter(known.astype(np.float64), size=5, mode="nearest")
        acc = np.stack([ndi.uniform_filter(out[..., c] * known, size=5, mode="nearest") for c in range(3)], axis=-1)
        new = (w > 0.15) & ~known
        out[new] = acc[new] / w[new][:, None]
        known = known | new
    return out

def smoothstep(x, lo, hi):
    t = np.clip((x - lo) / (hi - lo), 0, 1); return t * t * (3 - 2 * t)

def main(orig, outdir, tagline, fontfile):
    src = Image.open(orig).convert("RGB"); a = np.asarray(src).astype(np.float64); H, W = a.shape[:2]
    lum = a.mean(axis=2); sat = a.max(axis=2) - a.min(axis=2)
    # --- old tagline (light, grey-pink, thin strokes) in the lower right
    box_t = (295, 410, 520, 450)
    mt = np.zeros((H, W), bool)
    sub = (lum[box_t[1]:box_t[3], box_t[0]:box_t[2]] > 140) & (sat[box_t[1]:box_t[3], box_t[0]:box_t[2]] < 70)
    mt[box_t[1]:box_t[3], box_t[0]:box_t[2]] = sub
    mt = ndi.binary_dilation(mt, iterations=2)
    # --- black "Version ..." and "Marina Bay"
    box_v = (45, 150, 245, 230)
    dark = np.zeros((H, W), bool)
    dsub = lum[box_v[1]:box_v[3], box_v[0]:box_v[2]] < 85
    dark[box_v[1]:box_v[3], box_v[0]:box_v[2]] = dsub
    dark_core = ndi.binary_opening(dark, structure=np.ones((2, 2)))          # (the bird's shadow etc. are bigger blobs; text strokes survive)
    mv = ndi.binary_dilation(dark_core, iterations=2)
    # smooth, texture-free fill of both regions (only the small areas under the letters)
    clean = fill_masked(a, mt | mv)
    clean = np.where((mt | mv)[..., None], clean, a)
    # add back some of the painting's grain so the filled letters do not look smooth
    rng = np.random.default_rng(7)
    grain = ndi.gaussian_filter(rng.normal(0, 1, (H, W)), 0.7) * 6
    clean = np.clip(np.where((mt | mv)[..., None], clean + grain[..., None], clean), 0, 255)
    # --- black letters: alpha from the original darkness, enlarged and sharpened
    bg_l = clean.mean(axis=2)
    alpha1 = np.clip((bg_l - lum) / np.maximum(bg_l - 12, 1), 0, 1) * mv
    A = Image.fromarray((alpha1 * 255).astype(np.uint8)).resize((W * 2, H * 2), Image.BICUBIC)
    alpha2 = smoothstep(np.asarray(A).astype(np.float64) / 255, 0.30, 0.70)
    # --- enlarge the painting
    big = Image.fromarray(np.clip(clean, 0, 255).astype(np.uint8)).resize((W * 2, H * 2), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2))
    b = np.asarray(big).astype(np.float64)
    b = b * (1 - alpha2[..., None]) + np.array([8, 8, 8]) * alpha2[..., None]
    big = Image.fromarray(np.clip(b, 0, 255).astype(np.uint8)).convert("RGBA")
    # --- new tagline, right-aligned where the old one ended, same baseline and size as the old lettering
    font = ImageFont.truetype(fontfile, 48)
    draw = ImageDraw.Draw(big)
    right, baseline = 507 * 2, 438 * 2
    l, t, r, bt = draw.textbbox((0, 0), tagline, font=font, anchor="ls")
    layer = Image.new("RGBA", big.size, (0, 0, 0, 0)); d2 = ImageDraw.Draw(layer)
    d2.text((right - r, baseline), tagline, font=font, fill=(205, 196, 201, 255), anchor="ls")
    shadow = layer.filter(ImageFilter.GaussianBlur(2)); sh = np.asarray(shadow).copy(); sh[..., :3] = 0; sh[..., 3] = (sh[..., 3] * 0.55).astype(np.uint8)
    big = Image.alpha_composite(big, Image.fromarray(sh)); big = Image.alpha_composite(big, layer)
    os.makedirs(outdir, exist_ok=True)
    big.save(os.path.join(outdir, "coot-splash@2x.png"), dpi=(144, 144))
    big.resize((W, H), Image.LANCZOS).save(os.path.join(outdir, "coot-0.9.8.96.png"), dpi=(72, 72))
    print("wrote", os.listdir(outdir), "text width at 2x:", r - l)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "OpenSansItalic.ttf")
