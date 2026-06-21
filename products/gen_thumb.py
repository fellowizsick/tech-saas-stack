import struct, zlib

def create_png(width, height, pixels):
    def write_chunk(chunk_type, data):
        chunk = chunk_type + data
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', zlib.crc32(chunk) & 0xFFFFFFFF)
    
    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'
        for x in range(width):
            raw_data += bytes(pixels[y * width + x])
    
    compressed = zlib.compress(raw_data)
    
    return sig + write_chunk(b'IHDR', ihdr) + write_chunk(b'IDAT', compressed) + write_chunk(b'IEND', b'')

def lerp_color(c1, c2, t):
    return (int(c1[0] + (c2[0] - c1[0]) * t), int(c1[1] + (c2[1] - c1[1]) * t), int(c1[2] + (c2[2] - c1[2]) * t))

w, h = 600, 600
pixels = []

dark1 = (15, 15, 21)
dark2 = (26, 26, 46)
dark3 = (22, 33, 62)

for y in range(h):
    for x in range(w):
        nx, ny = x / w, y / h
        bg = lerp_color(lerp_color(dark1, dark2, nx), dark3, ny * 0.5)
        
        dx = x - 480
        dy = y - 120
        dist = (dx*dx + dy*dy) ** 0.5
        if dist < 180:
            alpha = 1 - dist / 180
            bg = (min(bg[0] + int(99 * alpha * 0.12), 255), min(bg[1] + int(102 * alpha * 0.12), 255), min(bg[2] + int(241 * alpha * 0.12), 255))
        
        dx = x - 150
        dy = y - 450
        dist = (dx*dx + dy*dy) ** 0.5
        if dist < 160:
            alpha = 1 - dist / 160
            bg = (min(bg[0] + int(245 * alpha * 0.08), 255), min(bg[1] + int(158 * alpha * 0.08), 255), min(bg[2] + int(11 * alpha * 0.08), 255))
        
        pixels.append(bg)

png_data = create_png(w, h, pixels)

with open('thumbnail-600.png', 'wb') as f:
    f.write(png_data)

print(f'Created {w}x{h} PNG')
