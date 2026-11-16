# Generator for the CRASR logo, banners, and social-preview template.
# Requires: pip install fonttools uharfbuzz, plus the Inter font (rsms.me/inter).
# Set FONT_DIR in textpath.py to your Inter .otf folder, then: python build.py
import math, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from textpath import text_path

GREEN = "#154734"      # Baylor Green
GOLD = "#FFB81C"       # University Gold
DEEP = "#0C2E21"       # deeper green for depth layers
MID = "#1E5C44"        # lighter green layer
OUT = "."  


def wave(x0, x1, y, amp, wl, phase=0, bottom=None, n=120):
    """Filled wave band from a sinusoidal top edge down to `bottom` (or stroke if None)."""
    pts = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        pts.append((x, y + amp * math.sin(2 * math.pi * (x - x0) / wl + phase)))
    d = "M" + " L".join(f"{x:.1f},{yy:.1f}" for x, yy in pts)
    if bottom is not None:
        d += f" L{x1:.1f},{bottom:.1f} L{x0:.1f},{bottom:.1f} Z"
    return d


def waves_block(x0, x1, top, bottom, amp, wl, layers):
    """Stacked water-column layers (epilimnion → hypolimnion)."""
    out = []
    for (dy, color, phase) in layers:
        out.append(f'<path d="{wave(x0, x1, top + dy, amp, wl, phase, bottom)}" fill="{color}"/>')
    return "\n  ".join(out)


# Water column layers: gold surface layer, then progressively deeper greens
LAYERS = [(0, GOLD, 0.0), (0.09, MID, 0.9), (0.20, DEEP, 1.8)]


def logo_mark(size=1024):
    """Square logo: CRASR wordmark over a stratified water column."""
    s = size
    word, _ = text_path("CRASR", "InterDisplay-Black", s * 0.24, s / 2, s * 0.45,
                        anchor="middle", tracking=-5)
    top = s * 0.66
    layers = [(s * f, c, p) for f, c, p in LAYERS]
    body = waves_block(-2, s + 2, top, s + 2, s * 0.022, s * 0.62, layers)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s} {s}" width="{s}" height="{s}">
  <title>CRASR</title>
  <rect width="{s}" height="{s}" fill="{GREEN}"/>
  <path d="{word}" fill="{GOLD}"/>
  {body}
</svg>
'''


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    open(f"{OUT}/crasr-logo.svg", "w").write(logo_mark())


def banner(dark=False, w=1280, h=320):
    bg = "#0B2219" if dark else GREEN
    word, ww = text_path("CRASR", "InterDisplay-Black", 112, 72, 168, tracking=-5)
    dx = 72 + ww + 44
    l1, _ = text_path("Center for Reservoir &", "InterDisplay-SemiBold", 40, dx + 44, 112)
    l2, _ = text_path("Aquatic Systems Research", "InterDisplay-SemiBold", 40, dx + 44, 162)
    tag, _ = text_path("Baylor University  ·  Modeling  ·  Data science  ·  Software  ·  Open science",
                       "Inter-Medium", 21, 74, 222, tracking=10)
    mid, deep = ("#123D2D", "#071711") if dark else (MID, DEEP)
    layers = [(0, GOLD, 0.0), (13, mid, 0.9), (29, deep, 1.8)]
    body = waves_block(-2, w + 2, 262, h + 2, 8, 640, layers)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <title>CRASR - Center for Reservoir and Aquatic Systems Research, Baylor University</title>
  <rect width="{w}" height="{h}" fill="{bg}"/>
  <path d="{word}" fill="{GOLD}"/>
  <rect x="{dx:.1f}" y="76" width="3" height="96" rx="1.5" fill="{GOLD}" fill-opacity="0.7"/>
  <path d="{l1}" fill="#FFFFFF"/>
  <path d="{l2}" fill="#FFFFFF"/>
  <path d="{tag}" fill="#FFFFFF" fill-opacity="0.78"/>
  {body}
</svg>
'''


def social_template(w=1280, h=640):
    """Repo social-preview template. {{...}} placeholders are filled by make-social-preview.R."""
    word, _ = text_path("CRASR", "InterDisplay-Black", 54, 80, 118, tracking=-5)
    foot, _ = text_path("github.com/CRASR", "Inter-SemiBold", 24, w - 80, 118, anchor="end", tracking=20)
    layers = [(0, GOLD, 0.0), (22, MID, 0.9), (48, DEEP, 1.8)]
    body = waves_block(-2, w + 2, 540, h + 2, 10, 640, layers)
    font = "Inter, 'Inter Display', 'Segoe UI', Helvetica, Arial, sans-serif"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{GREEN}"/>
  <path d="{word}" fill="{GOLD}"/>
  <path d="{foot}" fill="#FFFFFF" fill-opacity="0.7"/>
  <rect x="80" y="160" width="64" height="5" rx="2.5" fill="{GOLD}"/>
  <text x="80" y="268" font-family="{font}" font-weight="800" font-size="84" fill="#FFFFFF">{{{{TITLE}}}}</text>
  <text font-family="{font}" font-weight="500" font-size="34" fill="#FFFFFF" fill-opacity="0.82">
    <tspan x="80" y="344">{{{{DESC1}}}}</tspan>
    <tspan x="80" y="392">{{{{DESC2}}}}</tspan>
    <tspan x="80" y="440">{{{{DESC3}}}}</tspan>
  </text>
  {body}
</svg>
'''


if __name__ == "__main__":
    open(f"{OUT}/banner-light.svg", "w").write(banner(False))
    open(f"{OUT}/banner-dark.svg", "w").write(banner(True))
    open(f"{OUT}/social-preview-template.svg", "w").write(social_template())
