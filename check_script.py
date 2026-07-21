import sys
print("Python path:")
for p in sys.path:
    if p:
        print(f"  {p}")
print("---")
import os
home = os.path.expanduser("~")
scripts_dir = os.path.join(home, "AppData", "Local", "hermes", "scripts")
print(f"Scripts dir: {scripts_dir}")
if os.path.isdir(scripts_dir):
    for f in sorted(os.listdir(scripts_dir)):
        if "index" in f.lower() or "sitemap" in f.lower() or "seo" in f.lower() or "indexnow" in f.lower():
            print(f"  {f}")
else:
    print("  (not found)")
print("---")
# Also check current working directory
print(f"CWD: {os.getcwd()}")
for f in os.listdir("."):
    if "index" in f.lower() or "sitemap" in f.lower() or "seo" in f.lower():
        print(f"  CWD file: {f}")
