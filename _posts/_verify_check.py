#!/usr/bin/env python3
"""Ad-hoc structural verification for blog post. Run with python."""
import re, os

filepath = r"C:\Users\1990j\blog\_posts\2026-06-25-best-shared-web-hosting-2026.md"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

checks = []

# Frontmatter
checks.append(("Frontmatter opens with ---", content.startswith('---')))
frontmatter_end = content.find('\n---', 3)
checks.append(("Frontmatter closes with ---", frontmatter_end > 0))

# Required frontmatter fields
fm_fields = ['layout:', 'title:', 'date:', 'categories:', 'permalink:', 'description:']
for field in fm_fields:
    checks.append((f"Frontmatter has {field}", field in content[:frontmatter_end+5]))

# No pipe tables
pipe_lines = [l for l in content.split('\n') if re.match(r'^\|.+\|.*\|', l) and not re.match(r'^\[.+\]:\s', l)]
checks.append((f"No markdown pipe tables ({len(pipe_lines)} found)", len(pipe_lines) == 0))

# HTML table balance
opens = content.count('<table')
closes = content.count('</table>')
checks.append((f"HTML tables balanced ({opens} open / {closes} close)", opens == closes))

# Affiliate link rel
aff_hrefs = re.findall(r'href="https?://[^"]*(?:interserver\.net|siteground\.com|cloudways\.com|scalahosting\.com)[^"]*"', content)
aff_tags = re.findall(r'<a\s[^>]*href="https?://[^"]*(?:interserver\.net|siteground\.com|cloudways\.com|scalahosting\.com)[^"]*"[^>]*>', content)
missing_rel = [t for t in aff_tags if 'nofollow sponsored' not in t]
checks.append((f"All {len(aff_hrefs)} affiliate links have rel=nofollow sponsored ({len(missing_rel)} missing)", len(missing_rel) == 0))

# Disclosure
checks.append(("Disclosure bar present", 'disclosure-bar' in content))

# Internal links
internal = re.findall(r'href="(/comparison/[^"]+)"', content)
checks.append((f"Internal links: {len(internal)}", len(internal) >= 2))

# Word count
wc = len(content.split())
checks.append((f"Word count: ~{wc}", wc >= 2000))

print("=== Ad-hoc verification: 2026-06-25-best-shared-web-hosting-2026.md ===")
all_pass = True
for desc, result in checks:
    status = "✅" if result else "❌"
    if not result:
        all_pass = False
    print(f"  {status} {desc}")

print(f"\nResult: {'PASS' if all_pass else 'FAIL'}")
