#!/usr/bin/env python3
"""Create GitHub repo tech-saas-stack"""
import json, urllib.request, sys

token_file = "C:/Users/1990j/blog/.gh_token"
with open(token_file) as f:
    token = f.read().strip()

req = urllib.request.Request(
    "https://api.github.com/user/repos",
    data=json.dumps({
        "name": "tech-saas-stack",
        "description": "Tech & SaaS Stack — Honest reviews, comparisons, and tutorials",
        "private": False,
        "auto_init": False
    }).encode(),
    headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
)

try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    print(f"SUCCESS: {data['full_name']}")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    err = json.loads(body)
    if any(ed.get("message","") == "name already exists on this account" for ed in err.get("errors",[])):
        print("REPO_EXISTS")
    else:
        print(f"ERROR: {err}")
        sys.exit(1)
