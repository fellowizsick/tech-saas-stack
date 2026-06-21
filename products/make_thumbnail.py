from PIL import Image, ImageDraw, ImageFont
import math

size = 1258
img = Image.new('RGB', (size, size), '#0d0d0d')
draw = ImageDraw.Draw(img)

# Dark gradient top-to-bottom
for y in range(size):
    ratio = y / size
    r = int(13 * (1 - ratio) + 20 * ratio)
    g = int(13 * (1 - ratio) + 18 * ratio)
    b = int(13 * (1 - ratio) + 25 * ratio)
    draw.line([(0, y), (size, y)], fill=(r, g, b))

# Subtle accent glow at top (soft cyan)
for y in range(200):
    alpha = 1 - (y / 200)
    for x in range(0, size, 3):
        dist = abs(x - size/2) / (size/2)
        bright = max(0, 1 - dist * 1.5) * alpha * 15
        cx, cy = x, y
        px = img.getpixel((cx, cy))
        draw.point((cx, cy), fill=(
            min(255, int(px[0] + bright * 0.6)),
            min(255, int(px[1] + bright * 0.8)),
            min(255, int(px[2] + bright))
        ))

# Load fonts - try multiple sizes
arial_path = "C:/Windows/Fonts/arial.ttf"
arialbd_path = "C:/Windows/Fonts/arialbd.ttf"
calibri_path = "C:/Windows/Fonts/calibri.ttf"
calibrib_path = "C:/Windows/Fonts/calibrib.ttf"

# Badge
badge_size = 40
try:
    badge_font = ImageFont.truetype(arialbd_path, badge_size)
except:
    badge_font = ImageFont.truetype(arial_path, badge_size)

badge_text = "DIGITAL PRODUCT"
badge_bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
badge_w = badge_bbox[2] - badge_bbox[0]
badge_h = badge_bbox[3] - badge_bbox[1]

badge_pad_x = 40
badge_pad_y = 14
badge_x = (size - badge_w - badge_pad_x * 2) // 2
badge_y = 280 - badge_h // 2

# Rounded badge background
draw.rounded_rectangle(
    [badge_x, badge_y, badge_x + badge_w + badge_pad_x * 2, badge_y + badge_h + badge_pad_y * 2],
    radius=30,
    fill='#1a2a3a',
    outline='#3a7cad',
    width=2
)
draw.text(
    (badge_x + badge_pad_x, badge_y + badge_pad_y),
    badge_text,
    fill='#7fc9ff',
    font=badge_font
)

# Main title
title = "Affiliate Marketing\nStarter Kit"
title_size = 90
try:
    title_font = ImageFont.truetype(arialbd_path, title_size)
except:
    title_font = ImageFont.truetype(arial_path, title_size)

lines = title.split('\n')
line_h = 0
total_h = 0
line_dims = []
for i, line in enumerate(lines):
    bbox = draw.textbbox((0, 0), line, font=title_font)
    lw = bbox[2] - bbox[0]
    lh = bbox[3] - bbox[1]
    line_dims.append((line, lw, lh))
    if i > 0:
        total_h += 16  # spacing
    total_h += lh

start_y = badge_y + badge_h + badge_pad_y * 2 + 60
cy = start_y

for line, lw, lh in line_dims:
    x = (size - lw) // 2
    # Draw text with slight glow effect for title
    glow_color = (80, 120, 160)
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if dx != 0 or dy != 0:
                draw.text((x + dx, cy + dy), line, fill=glow_color, font=title_font)
    draw.text((x, cy), line, fill='#f0e6c0', font=title_font)
    cy += lh + 16

# Subtitle
sub = "Your blueprint to build a profitable\naffiliate business from scratch"
sub_size = 34
try:
    sub_font = ImageFont.truetype(calibri_path, sub_size)
except:
    sub_font = ImageFont.truetype(arial_path, sub_size)

sub_lines = sub.split('\n')
cy += 40
for line in sub_lines:
    bbox = draw.textbbox((0, 0), line, font=sub_font)
    sw = bbox[2] - bbox[0]
    sh = bbox[3] - bbox[1]
    draw.text(((size - sw) // 2, cy), line, fill='#999999', font=sub_font)
    cy += sh + 10

# Price pill
price = "$17"
price_size = 72
try:
    price_font = ImageFont.truetype(arialbd_path, price_size)
except:
    price_font = ImageFont.truetype(arial_path, price_size)

pbbox = draw.textbbox((0, 0), price, font=price_font)
pw = pbbox[2] - pbbox[0]
ph = pbbox[3] - pbbox[1]

pill_pad_x = 60
pill_pad_y = 20
pill_x = (size - pw - pill_pad_x * 2) // 2
pill_y = cy + 40

draw.rounded_rectangle(
    [pill_x, pill_y, pill_x + pw + pill_pad_x * 2, pill_y + ph + pill_pad_y * 2],
    radius=50,
    fill='#1a3a2a',
    outline='#2ecc71',
    width=3
)
draw.text(
    (pill_x + pill_pad_x, pill_y + pill_pad_y),
    price,
    fill='#2ecc71',
    font=price_font
)

# Bottom accent line
line_y = size - 80
draw.rounded_rectangle(
    [(size - 400) // 2, line_y, (size + 400) // 2, line_y + 4],
    radius=2,
    fill='#2ecc71'
)

# Small text at bottom
bottom_text = "Tech & SaaS Stack ★"
bt_size = 24
try:
    bt_font = ImageFont.truetype(calibri_path, bt_size)
except:
    bt_font = ImageFont.truetype(arial_path, bt_size)

bt_bbox = draw.textbbox((0, 0), bottom_text, font=bt_font)
btw = bt_bbox[2] - bt_bbox[0]
bth = bt_bbox[3] - bt_bbox[1]
draw.text(
    ((size - btw) // 2, line_y + 16),
    bottom_text,
    fill='#555555',
    font=bt_font
)

# Save
out_path = "C:/Users/1990j/blog/products/gumroad-thumb.png"
img.save(out_path, "PNG")
print(f"Saved to {out_path}")
print(f"Size: {img.size[0]}x{img.size[1]}")
