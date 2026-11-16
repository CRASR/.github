"""Convert shaped text to SVG path data so graphics render identically everywhere."""
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONT_DIR = "/usr/share/fonts/opentype/inter/"
_cache = {}


def _load(name):
    if name not in _cache:
        path = FONT_DIR + name + ".otf"
        blob = hb.Blob.from_file_path(path)
        face = hb.Face(blob)
        font = hb.Font(face)
        tt = TTFont(path)
        _cache[name] = (font, tt, tt["head"].unitsPerEm)
    return _cache[name]


def text_path(text, font="Inter-Bold", size=40, x=0, y=0, anchor="start", tracking=0):
    """Return (svg path d, width). tracking is in em/1000 units."""
    hbfont, tt, upem = _load(font)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": True})
    gs = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    scale = size / upem
    track = tracking * upem / 1000
    pen_x = 0
    glyphs = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        glyphs.append((order[info.codepoint], pen_x + pos.x_offset, pos.y_offset))
        pen_x += pos.x_advance + track
    width = (pen_x - track) * scale
    x0 = {"start": x, "middle": x - width / 2, "end": x - width}[anchor]
    spen = SVGPathPen(gs)
    for gname, gx, gy in glyphs:
        t = (scale, 0, 0, -scale, x0 + gx * scale, y - gy * scale)
        gs[gname].draw(TransformPen(spen, t))
    return spen.getCommands(), width
