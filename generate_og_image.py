#!/usr/bin/env python3
"""Generate a branded default Open Graph image (1200x630) for techsaasstack.com.
On-brand dark navy theme. This single image unblocks ALL posts that lack a
featured image -> Pinterest/social thumbnails stop being blank -> traffic unblocked.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
img = Image.new("RGB", (W, H), "#0f1420")
d = ImageDraw.Draw(img)

# vertical gradient navy -> slightly lighter
top = (15, 20, 32)
bot = (26, 38, 54)
for y in range(H):
    r = int(top[0] + (bot[0]-top[0])*y/H)
    g = int(top[1] + (bot[1]-top[1])*y/H)
    b = int(top[2] + (bot[2]-top[2])*y/H)
    d.line([(0, y), (W, y)], fill=(r, g, b))

# top accent bar
d.rectangle([0, 0, W, 8], fill=(10, 140, 255))

# subtle glow top-left
for i in range(40):
    a = 3 - i*0.07
    if a <= 0:
        break
    d.ellipse([-200+i*6, -200+i*6, 500-i*6, 500-i*6], outline=(10, 140, 255), width=2)

# fonts
def font(path, sz):
    try:
        return ImageFont.truetype(path, sz)
    except Exception:
        return ImageFont.load_default()

arialbd = "C:/Windows/Fonts/arialbd.ttf"
arial = "C:/Windows/Fonts/arial.ttf"
calibri = "C:/Windows/Fonts/calibri.ttf"

# domain pill top-left
d.text((60, 50), "techsaasstack.com", font=font(arial, 28), fill=(122, 139, 168))

# title
title = "Tech & SaaS Stack"
d.text((60, 200), title, font=font(arialbd, 76), fill=(255, 255, 255))
# subtitle
d.text((62, 300), "Honest hosting & SaaS reviews", font=font(calibri, 38), fill=(200, 212, 230))
d.text((62, 350), "that actually help you choose.", font=font(calibri, 38), fill=(200, 212, 230))

# CTA pill bottom
d.rounded_rectangle([60, 470, 520, 540], radius=15, fill=(10, 140, 255))
d.text((90, 488), "Read the full comparison ->", font=font(arialbd, 28), fill=(255, 255, 255))

img.save("assets/images/og-default.png", "PNG")
print("WROTE assets/images/og-default.png", img.size)
