import json, colorsys
from PIL import Image, ImageDraw, ImageFont

frames = json.load(open("frames.json"))
CHARS = " .:-=+*#%@"
COLS, ROWS = 60, 25
CELL_W, CELL_H = 9, 17
W, H = COLS * CELL_W, ROWS * CELL_H
font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSansMono.ttf", 15)

def ramp(i, n):
    if i <= 0: return (13, 17, 23)
    t = i / (n - 1)
    if t < 0.4: c = colorsys.hsv_to_rgb(0.42 + t * 1.3, 0.9, 0.35 + t * 1.0)
    elif t < 0.8: c = colorsys.hsv_to_rgb(0.5 - (t - 0.4) * 0.8, 0.9, 1.0)
    else: c = colorsys.hsv_to_rgb(0.25 - (t - 0.8) * 1.4, 0.8, 1.0)
    return tuple(int(v * 255) for v in c)

rgb_imgs = []
for fr in frames:
    img = Image.new("RGB", (W, H), (13, 17, 23))
    d = ImageDraw.Draw(img)
    for y, line in enumerate(fr["grid"]):
        for x, ch in enumerate(line):
            if ch == " ": continue
            i = CHARS.find(ch)
            if i < 0: i = len(CHARS) - 1
            d.text((x * CELL_W, y * CELL_H), ch, fill=ramp(i, len(CHARS)), font=font)
    rgb_imgs.append(img)

canvas = Image.new("RGB", (COLS, H))
for i, im in enumerate(rgb_imgs[:16]):
    canvas.paste(im, (0, 0))
palette_img = canvas.quantize(colors=64)
imgs = [im.quantize(palette=palette_img, dither=Image.Dither.NONE) for im in rgb_imgs]

imgs[0].save("ascii_live.gif", save_all=True, append_images=imgs[1:], duration=120, loop=0, optimize=True)
print("ascii_live.gif", len(imgs), "frames,", imgs[0].size)
