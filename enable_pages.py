#!/usr/bin/env python3
"""Enable GitHub Pages on fellowizsick/tech-saas-stack"""
import json, urllib.request, sys, os

token = os.environ.get("GH_TOKEN")
if not token:
    print("ERROR: GH_TOKEN env var not set")
    sys.exit(1)

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
    "Content-Type": "application/json"
}

# Enable Pages
req = urllib.request.Request(
    "https://api.github.com/repos/fellowizsick/tech-saas-stack/pages",
    data=json.dumps({
        "source": {
            "branch": "main",
            "path": "/"
        }
    }).encode(),
    headers=headers,
    method="POST"
)

try:
    resp = urllib.request.urlopen(req)
    print(f"GitHub Pages enabled: {resp.status}")
except urllib.error.HTTPError as e:
    body = json.loads(e.read())
    print(f"STATUS: {e.code} - {body}")
    if e.code == 409 and "already" in str(body):
        print("Pages already configured")

# Verify
req2 = urllib.request.Request(
    "https://api.github.com/repos/fellowizsick/tech-saas-stack/pages",
    headers=headers
)
try:
    resp2 = urllib.request.urlopen(req2)
    data = json.loads(resp2.read())
    print(f"Pages URL: {data.get('html_url', 'pending...')}")
    print(f"Status: {data.get('status', 'unknown')}")
except urllib.error.HTTPError as e:
    print(f"Verify status: {e.code}")
