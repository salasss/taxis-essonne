"""Détourage du logo JPG : fond retiré (color-to-alpha), recadrage, déclinaisons web.

Usage : python design/detourer-logo.py design/logo-source.jpg assets/logo
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

src, out_dir = Path(sys.argv[1]), Path(sys.argv[2])
out_dir.mkdir(parents=True, exist_ok=True)

img = np.asarray(Image.open(src).convert("RGB")).astype(np.float64)
h, w, _ = img.shape

# Couleur du fond = médiane des bords
border = np.concatenate([img[:20].reshape(-1, 3), img[-20:].reshape(-1, 3),
                         img[:, :20].reshape(-1, 3), img[:, -20:].reshape(-1, 3)])
bg = np.median(border, axis=0)
print("fond:", bg.round())

# Color-to-alpha : les encres (bleu, rouge) sont plus sombres que le fond,
# donc seul l'assombrissement compte (les pixels plus clairs = bruit du fond)
alpha = np.clip(((bg - img) / bg).max(axis=2), 0, 1)
alpha = np.clip((alpha - 0.04) / 0.96, 0, 1)  # bruit JPEG du fond
a3 = np.maximum(alpha, 1e-6)[..., None]
color = np.clip(bg + (img - bg) / a3, 0, 255)

# Recadrage serré + marge
ys, xs = np.where(alpha > 0.15)
pad = 12
y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad, h)
x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad, w)
alpha, color = alpha[y0:y1, x0:x1], color[y0:y1, x0:x1]

def save(rgb, a, name, width=None):
    rgba = np.dstack([rgb, a * 255]).round().astype(np.uint8)
    im = Image.fromarray(rgba, "RGBA")
    if width and im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(out_dir / name, optimize=True)
    print(name, im.size)
    return im

# Couleurs de la charte du site (bleu-blanc-rouge)
INK = np.array([10, 36, 99], dtype=np.float64)     # #0A2463
RED = np.array([225, 0, 15], dtype=np.float64)     # #E1000F
WHITE = np.array([255, 255, 255], dtype=np.float64)

is_red = (color[..., 0] > 150) & (color[..., 1] < 130) & (color[..., 2] < 130)
# Le rouge plafonne à ~75 % d'opacité (son canal le plus sombre) : on le rend plein
alpha = np.where(is_red, np.clip(alpha / 0.75, 0, 1), alpha)

# 1. Logo complet (fond transparent) : bleu marine + rouge
color = np.where(is_red[..., None], RED, INK)
save(color, alpha, "logo.png", 1200)

# 2. Version claire pour fonds sombres : blanc + rouge
light = np.where(is_red[..., None], RED, WHITE)
save(light, alpha, "logo-blanc.png", 1200)

# 3. Icône : le van seul (colonnes avant le plus grand vide entre van et texte)
cols = (alpha > 0.15).any(axis=0)
runs, start = [], None
for x, filled in enumerate(cols):
    if not filled and start is None:
        start = x
    if filled and start is not None:
        runs.append((x - start, start, x)); start = None
gap = max(r for r in runs if r[1] > 0)
van_a, van_c = alpha[:, : gap[1]], color[:, : gap[1]]
ys, xs = np.where(van_a > 0.15)
van_a = van_a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
van_c = van_c[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
vh, vw = van_a.shape
side = int(max(vh, vw) * 1.04)
sq_a = np.zeros((side, side)); sq_c = np.zeros((side, side, 3))
oy, ox = (side - vh) // 2, (side - vw) // 2
sq_a[oy:oy + vh, ox:ox + vw] = van_a; sq_c[oy:oy + vh, ox:ox + vw] = van_c
icon = save(sq_c, sq_a, "logo-icone.png", 512)
icon.resize((64, 64), Image.LANCZOS).save(out_dir / "favicon.png", optimize=True)

# 4. Icône iPhone (fond blanc opaque, 180 px)
touch = Image.new("RGBA", (180, 180), (255, 255, 255, 255))
small = icon.resize((150, 150), Image.LANCZOS)
touch.alpha_composite(small, (15, 15))
touch.convert("RGB").save(out_dir / "apple-touch-icon.png", optimize=True)
print("ok")
