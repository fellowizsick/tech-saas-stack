"""Crop center square from a PNG file using pure Python."""
import struct, zlib

def read_png(path):
    with open(path, 'rb') as f:
        data = f.read()
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError('Not a PNG')
    
    pos = 8
    ihdr_data = None
    idat_chunks = []
    
    while pos < len(data):
        length = struct.unpack('>I', data[pos:pos+4])[0]
        chunk_type = data[pos+4:pos+8].decode('ascii')
        chunk_data = data[pos+8:pos+8+length]
        
        if chunk_type == 'IHDR':
            ihdr_data = chunk_data
        elif chunk_type == 'IDAT':
            idat_chunks.append(chunk_data)
        elif chunk_type == 'IEND':
            break
        
        pos += 12 + length
    
    width = struct.unpack('>I', ihdr_data[0:4])[0]
    height = struct.unpack('>I', ihdr_data[4:8])[0]
    
    raw = zlib.decompress(b''.join(idat_chunks))
    
    pixels = []
    stride = width * 3 + 1
    for y in range(height):
        row_start = y * stride
        row_data = raw[row_start+1:row_start+stride]
        for x in range(width):
            px = row_data[x*3:(x+1)*3]
            pixels.append((px[0], px[1], px[2]))
    
    return width, height, pixels

def write_png(width, height, pixels, path):
    def chunk(t, d):
        c = t.encode() + d
        return struct.pack('>I', len(d)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    
    raw = b''
    for y in range(height):
        raw += b'\x00'
        for x in range(width):
            px = pixels[y * width + x]
            raw += bytes(px)
    
    png = b'\x89PNG\r\n\x1a\n'
    png += chunk('IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    png += chunk('IDAT', zlib.compress(raw))
    png += chunk('IEND', b'')
    
    with open(path, 'wb') as f:
        f.write(png)

# Read
w, h, pixels = read_png('thumbnail-square.png')
print(f'Read {w}x{h}')

# Crop center 600x600
size = 600
ox = (w - size) // 2
oy = (h - size) // 2

cropped = []
for y in range(size):
    for x in range(size):
        cropped.append(pixels[(oy + y) * w + (ox + x)])

write_png(size, size, cropped, 'thumbnail-final.png')
print(f'Wrote {size}x{size} -> thumbnail-final.png')
