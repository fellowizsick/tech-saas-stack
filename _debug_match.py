import re

with open("C:\\Users\\1990j\\blog\\_posts\\2026-06-26-cheapest-web-hosting-2026.md", "r", encoding="utf-8") as f:
    content = f.read()

patterns = [
    (r'\$\d+\.\d{2}\s*/(mo|month|year)\b.*\b(forever|always|lifetime|lifelong)\b', "Pattern 1: forever/always/lifetime"),
    (r'\bonly\s+\$\d+\.?\d*\s*/(mo|month|year)\b(?!\s+(intro|renewal|for new|starting))', "Pattern 2: only $X/mo"),
    (r'\bprices? (will )?(never|won\'?t) (change|increase|go up|rise)\b', "Pattern 3: prices never change"),
    (r'\b(locked in|lifetime price)\b(?!\s+(introductory|for new|first term))', "Pattern 4: locked in"),
]

for pat, name in patterns:
    for m in re.finditer(pat, content, re.IGNORECASE):
        line_num = content[:m.start()].count('\n') + 1
        context = content[max(0, m.start() - 60):m.end() + 60].replace('\n', ' ')
        print(f"--- {name} --- L{line_num}: matched '{m.group()}'")
        print(f"  ...{context}...")
        print()
