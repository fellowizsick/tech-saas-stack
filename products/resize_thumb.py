"""Resize a PNG to 600x600 with bilinear interpolation, pad with dark background."""
import struct, zlib, math

def read_png(path):
    with open(path, 'rb') as f:
        data = f.read()
    pos = 8
    ihdr, idats = None, []
    while pos < len(data):
        l = struct.unpack('>I', data[pos:pos+4])[0]
        t = data[pos+4:pos+8].decode('ascii')
        d = data[pos+8:pos+8+l]
        if t == 'IHDR': ihdr = d
        elif t == 'IDAT': idats.append(d)
        elif t == 'IEND': break
        pos += 12 + l
    w = struct.unpack('>I', ihdr[0:4])[0]
    h = struct.unpack('>I', ihdr[4:8])[0]
    raw = zlib.decompress(b''.join(idats))
    pixels = [[(0,0,0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        r = raw[y*(w*3+1)+1:(y+1)*(w*3+1)]
        for x in range(w):
            pixels[y][x] = (r[x*3], r[x*3+1], r[x*3+2])
    return w, h, pixels

def write_png(pixels, path):
    h, w = len(pixels), len(pixels[0])
    def c(t, d):
        ct = t.encode()+d
        return struct.pack('>I',len(d))+ct+struct.pack('>I',zlib.crc32(ct)&0xffffffff)
    raw = b''
    for y in range(h):
        raw += b'\x00'
        for x in range(w):
            raw += bytes(pixels[y][x])
    png = b'\x89PNG\r\n\x1a\n'
    png += c('IHDR', struct.pack('>IIBBBBB',w,h,8,2,0,0,0))
    png += c('IDAT', zlib.compress(raw))
    png += c('IEND', b'')
    with open(path, 'wb') as f: f.write(png)

def resize_bilinear(src_pixels, src_w, src_h, dst_w, dst_h):
    result = [[(0,0,0) for _ in range(dst_w)] for _ in range(dst_h)]
    for dy in range(dst_h):
        for dx in range(dst_w):
            sx = dx * src_w / dst_w
            sy = dy * src_h / dst_h
            ix, iy = int(sx), int(sy)
            fx, fy = sx - ix, sy - iy
            ix = min(ix, src_w - 2)
            iy = min(iy, src_h - 2)
            c = [(0,0,0) for _ in range(4)]
            c[0] = src_pixels[iy][ix]
            c[1] = src_pixels[iy][ix+1]
            c[2] = src_pixels[iy+1][ix]
            c[3] = src_pixels[iy+1][ix+1]
            r = int((1-fx)*(1-fy)*c[0][0] + fx*(1-fy)*c[1][0] + (1-fx)*fy*c[2][0] + fx*fy*c[3][0])
            g = int((1-fx)*(1-fy)*c[0][1] + fx*(1-fy)*c[1][1] + (1-fx)*fy*c[2][1] + fx*fy*c[3][1])
            b = int((1-fx)*(1-fy)*c[0][2] + fx*(1-fy)*c[1][2] + (1-fx)*fy*c[2][2] + fx*fy*c[3][2])
            result[dy][dx] = (min(255,r), min(255,g), min(255,b))
    return result

# Read the fullscreen browser screenshot
w, h, pixels = read_png('fullscreen.png')
print(f'Source: {w}x{h}')

# Resize to fit within 600x600 maintaining aspect ratio
target = 600
if w > h:
    new_w = target
    new_h = int(h * target / w)
else:
    new_h = target
    new_w = int(w * target / h)

resized = resize_bilinear(pixels, w, h, new_w, new_h)
print(f'Resized to: {new_w}x{new_h}')

# Pad to 600x600 with dark background color
bg = (15, 15, 21)
pad_h = (target - new_h) // 2
pad_w = (target - new_w) // 2

final = [[bg for _ in range(target)] for _ in range(target)]
for y in range(new_h):
    for x in range(new_w):
        final[y + pad_h][x + pad_w] = resized[y][x]

write_png(final, 'thumbnail-padded.png')
print(f'Final: 600x600 -> thumbnail-padded.png')
