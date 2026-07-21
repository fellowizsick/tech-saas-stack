#!/usr/bin/env python3
"""
Fetch sitemap.xml from techsaasstack.com, parse all URLs,
and submit them to IndexNow API (Bing/Yandex/Seznam).
Uses verified key 924c5f4229bef1e57d26850c89e21708
"""
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import sys
import ssl

SITEMAP_URL = "https://techsaasstack.com/sitemap.xml"
HOST = "techsaasstack.com"
KEY = "924c5f4229bef1e57d26850c89e21708"

ENDPOINTS = [
    ("api.indexnow.org", f"https://api.indexnow.org/indexnow"),
    ("Bing", f"https://www.bing.com/indexnow"),
    ("Yandex", f"https://yandex.com/indexnow"),
]

def fetch_xml(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        return resp.read()

def parse_sitemap(xml_data):
    urls = []
    root = ET.fromstring(xml_data)
    ns = {}
    if root.tag.startswith("{"):
        ns_match = root.tag.split("}")
        ns["sm"] = ns_match[0][1:]
    if ns:
        for url_elem in root.findall(".//sm:loc", ns):
            urls.append(url_elem.text.strip())
    else:
        for url_elem in root.findall(".//loc"):
            urls.append(url_elem.text.strip())
    return urls

def submit_to_endpoint(name, endpoint_url, urls):
    payload = {
        "host": HOST,
        "key": KEY,
        "urlList": urls,
        "keyLocation": f"https://{HOST}/{KEY}.txt"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint_url,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IndexNow-TechSaaSStack/1.0"
        },
        method="POST"
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            body = resp.read().decode("utf-8", errors="replace") if resp.length else "(empty)"
            return {"name": name, "status": resp.status, "body": body[:200], "ok": True}
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace") if e.fp else "(empty)"
        return {"name": name, "status": e.code, "body": body[:200], "ok": False}
    except Exception as e:
        return {"name": name, "status": 0, "body": str(e), "ok": False}

def main():
    print(f"IndexNow Ping — techsaasstack.com")
    print(f"Key: {KEY}")
    print(f"Key file: https://{HOST}/{KEY}.txt")
    print(f"Total URLs in sitemap to be sent to each endpoint")
    print()
    
    # Step 1: Verify key file
    key_url = f"https://{HOST}/{KEY}.txt"
    try:
        kreq = urllib.request.Request(key_url, headers={"User-Agent": "Mozilla/5.0"})
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(kreq, timeout=10, context=ctx) as resp:
            kc = resp.read().decode("utf-8").strip()
        key_ok = (kc == KEY)
        print(f"✓ Key file verified: HTTP {resp.status}, content matches" if key_ok
              else f"⚠ Key file content mismatch: got '{kc}' expected '{KEY}'")
    except Exception as e:
        key_ok = False
        print(f"✗ Key file check failed: {e}")
    
    if not key_ok:
        print("\n⚠ Proceeding without verified key (submissions may be rejected)")
    
    # Step 2: Fetch and parse sitemap
    print(f"\nFetching sitemap from {SITEMAP_URL}...")
    xml_data = fetch_xml(SITEMAP_URL)
    all_urls = parse_sitemap(xml_data)
    print(f"Found {len(all_urls)} URLs in sitemap\n")
    
    # Step 3: Submit to each endpoint
    results = []
    for name, url in ENDPOINTS:
        result = submit_to_endpoint(name, url, all_urls)
        results.append(result)
        status_icon = "✓" if result["ok"] else "✗"
        print(f"  {status_icon} {name}: HTTP {result['status']} — {result['body'][:80]}")
    
    # Step 4: Summary
    ok_count = sum(1 for r in results if r["ok"])
    print(f"\n{'='*50}")
    print(f"SUMMARY")
    print(f"{'='*50}")
    print(f"  Sitemap URLs:     {len(all_urls)}")
    print(f"  Key verified:     {'YES' if key_ok else 'NO — key file missing'}")
    print(f"  Endpoints OK:     {ok_count}/{len(results)}")
    for r in results:
        print(f"    {'✓' if r['ok'] else '✗'} {r['name']}: HTTP {r['status']}")
    
    summary = {
        "site": HOST,
        "key": KEY,
        "key_verified": key_ok,
        "total_urls": len(all_urls),
        "endpoints": {r["name"]: {"status": r["status"], "ok": r["ok"]} for r in results},
        "success_count": ok_count,
        "total_endpoints": len(results)
    }
    print(f"\n---STRUCTURED_SUMMARY:{json.dumps(summary)}")

if __name__ == "__main__":
    main()
