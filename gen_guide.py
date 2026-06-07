import sys
p=r'C:/Users/1990j/AppData/Local/hermes/audio_cache/Home Solar Guide.md'
with open(p,"w") as f:
 f.write(sys.stdin.read())
print("Written")
