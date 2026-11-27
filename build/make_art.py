"""Podcast artwork (free: Pillow + the Inter font, SIL Open Font License, in assets/fonts).
make_art.py <out_dir>  -> cover.png (3000x3000) and art/NNN.png (1400x1400) for every episode in episodes/*/meta.json"""
import datetime as dt, json, pathlib, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
FONTS = ROOT / "assets" / "fonts"
NAVY_TOP, NAVY_BOTTOM = (8, 22, 38), (16, 52, 78)
WHITE, MUTED, GOLD = (245, 247, 250), (150, 175, 198), (242, 184, 75)
SLOT_COLOR = {"A": GOLD, "B": (64, 200, 180), "C": (240, 120, 100)}
# a fixed, made-up price path used only as decoration (not market data)
PATH = [0.30, 0.34, 0.31, 0.38, 0.36, 0.44, 0.41, 0.50, 0.47, 0.56, 0.53, 0.62, 0.66, 0.61, 0.72, 0.70, 0.80, 0.86]


def font(weight, size):
    return ImageFont.truetype(str(FONTS / f"Inter-{weight}.otf"), size)


def background(size):
    img = Image.new("RGB", (size, size))
    d = ImageDraw.Draw(img)
    for y in range(size):
        t = y / size
        d.line([(0, y), (size, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(NAVY_TOP, NAVY_BOTTOM)))
    step = size // 12
    for i in range(1, 12):  # faint chart grid
        d.line([(i * step, 0), (i * step, size)], fill=(255, 255, 255, 0) if False else (30, 60, 88), width=max(1, size // 1000))
        d.line([(0, i * step), (size, i * step)], fill=(30, 60, 88), width=max(1, size // 1000))
    return img, d


def chart(d, size, color, top, bottom):
    """Rising line with candles along the bottom of the image."""
    n = len(PATH)
    xs = [int(size * (0.06 + 0.88 * i / (n - 1))) for i in range(n)]
    ys = [int(bottom - (bottom - top) * v) for v in PATH]
    w = max(4, size // 120)
    for i in range(1, n):  # candles
        up = PATH[i] >= PATH[i - 1]
        c = color if up else MUTED
        x, y0, y1 = xs[i], ys[i - 1], ys[i]
        d.line([(x, min(y0, y1) - size // 60), (x, max(y0, y1) + size // 60)], fill=c, width=max(2, w // 3))
        d.rectangle([x - w, min(y0, y1), x + w, max(y0, y1) + 2], fill=c)
    d.line(list(zip(xs, ys)), fill=color, width=max(3, size // 250), joint="curve")
    r = size // 70
    d.ellipse([xs[-1] - r, ys[-1] - r, xs[-1] + r, ys[-1] + r], fill=WHITE, outline=color, width=r // 2)


def wrap(d, text, f, width):
    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if d.textlength(trial, font=f) <= width or not line:
            line = trial
        else:
            lines.append(line); line = word
    return lines + [line] if line else lines


def cover(path, size=3000):
    img, d = background(size)
    m = int(size * 0.08)
    d.rectangle([m, m, m + size // 6, m + size // 60], fill=GOLD)
    d.text((m, m + size // 22), "DAILY", font=font("Black", size // 5), fill=WHITE)
    d.text((m, m + size // 22 + int(size * 0.19)), "BRIEF", font=font("Black", size // 5), fill=GOLD)
    d.text((m, int(size * 0.53)), "Markets · Lessons · Interviews", font=font("Medium", size // 26), fill=WHITE)
    d.text((m, int(size * 0.53) + size // 18), "From beginner to asset manager", font=font("Medium", size // 30), fill=MUTED)
    chart(d, size, GOLD, int(size * 0.66), int(size * 0.94))
    img.save(path, optimize=True)


def episode(meta, path, size=1400):
    slot = meta.get("slot", "")
    color = SLOT_COLOR.get(slot, GOLD)
    img, d = background(size)
    m = int(size * 0.08)
    d.text((m, m), "DAILY BRIEF", font=font("Black", size // 18), fill=WHITE)
    day = dt.date.fromisoformat(meta["date"]).strftime("%a %-d %b %Y")
    label = f"{slot}  ·  {day}" if slot else day
    f = font("Bold", size // 30)
    tw = d.textlength(label, font=f)
    y = m + size // 10
    d.rounded_rectangle([m, y, m + tw + size // 20, y + size // 17], radius=size // 34, fill=color)
    d.text((m + size // 40, y + size // 90), label, font=f, fill=NAVY_TOP)
    d.text((m - size // 80, y + size // 14), f"{meta['number']:03d}", font=font("Black", size // 4), fill=color)
    tf = font("Bold", size // 13)
    lines = wrap(d, meta["title"], tf, size - 2 * m)
    if len(lines) > 3:
        tf = font("Bold", size // 17); lines = wrap(d, meta["title"], tf, size - 2 * m)[:4]
    ty = int(size * 0.50)
    for line in lines:
        d.text((m, ty), line, font=tf, fill=WHITE); ty += int(tf.size * 1.15)
    chart(d, size, color, int(size * 0.80), int(size * 0.95))
    img.save(path, optimize=True)


if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "_site")
    (out / "art").mkdir(parents=True, exist_ok=True)
    cover(out / "cover.png")
    for p in sorted((ROOT / "episodes").glob("*/meta.json")):
        meta = json.loads(p.read_text())
        episode(meta, out / "art" / f"{meta['number']:03d}.png")
    print(f"artwork written to {out}")
