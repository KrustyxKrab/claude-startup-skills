#!/usr/bin/env python3
"""
Competitive landscape scanning: domain saturation + SEC EDGAR + patent activity.
Usage: python competitive_scan.py --keywords "fintech,payments" --domain-search "payment app"

APIs used:
  - crt.sh (certificate transparency log) — free, no auth required
  - SEC EDGAR full-text search — free, no auth required
  - PatentsView — free API key required: https://patentsview.org/apis/api-key
      Pass key via --patents-key or PATENTSVIEW_API_KEY env var.
      Without a key, patent search is skipped and a signup link is printed.
"""

import argparse
import json
import os
import urllib.request
import urllib.parse


def search_domains(query: str, limit: int = 20):
    """Estimate domain saturation via crt.sh certificate transparency log (free, no auth).

    crt.sh indexes SSL certificates — a good proxy for how many live websites/products
    exist in a space. Falls back gracefully if crt.sh is temporarily unavailable (503).
    """
    import time
    encoded = urllib.parse.quote(f"%{query}%")
    url = f"https://crt.sh/?q={encoded}&output=json"
    last_error = None
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "StartupResearch/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
            seen: set[str] = set()
            domains = []
            for record in data:
                raw_names = [record.get("common_name") or ""] + (record.get("name_value") or "").split("\n")
                for name in raw_names:
                    name = (name or "").strip().lstrip("*.")
                    if name and "." in name and name not in seen:
                        seen.add(name)
                        domains.append({"domain": name, "issued": record.get("not_before", "")[:10]})
            total = len(seen)
            return {
                "total": total,
                "domains": domains[:limit],
                "saturation_signal": "high" if total > 500 else "medium" if total > 100 else "low",
                "source": "crt.sh (SSL certificate transparency)",
            }
        except Exception as e:
            last_error = str(e)
            if attempt == 0:
                time.sleep(3)
    return {
        "error": last_error,
        "fallback": f"crt.sh temporarily unavailable. Search manually: https://crt.sh/?q=%25{urllib.parse.quote(query)}%25",
        "saturation_signal": "unknown",
    }


def search_sec_edgar(query: str, limit: int = 10):
    """Search SEC EDGAR full-text search (free, no auth, 10 req/sec).
    Useful for finding public company filings related to the space.
    """
    params = urllib.parse.urlencode({
        "q": query,
        "dateRange": "custom",
        "startdt": "2023-01-01",
        "enddt": "2026-12-31",
    })
    url = f"https://efts.sec.gov/LATEST/search-index?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "StartupResearch/1.0 research@example.com"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            hits = data.get("hits", {}).get("hits", [])
            return {
                "total": data.get("hits", {}).get("total", {}).get("value", 0),
                "filings": [
                    {
                        # display_names is a list like ["Acme Corp (ACM) (CIK 0001234)"]
                        "entity": (h.get("_source", {}).get("display_names") or [""])[0].split("(")[0].strip(),
                        "form_type": h.get("_source", {}).get("form", ""),
                        "filed": h.get("_source", {}).get("file_date", ""),
                        "description": (h.get("_source", {}).get("file_description", "") or "")[:200],
                    }
                    for h in hits[:limit]
                ],
            }
    except Exception as e:
        fallback = f"https://efts.sec.gov/LATEST/search-index?q={urllib.parse.quote(query)}"
        return {"error": str(e), "fallback_url": fallback}


def search_patents(query: str, limit: int = 20, api_key: str = None):
    """Search USPTO patents via PatentsView API.

    Requires a free API key: https://patentsview.org/apis/api-key
    Pass via --patents-key flag or PATENTSVIEW_API_KEY environment variable.
    Without a key, this function returns a helpful skip message.
    """
    key = api_key or os.environ.get("PATENTSVIEW_API_KEY")
    if not key:
        return {
            "skipped": True,
            "reason": "PatentsView API key not provided.",
            "get_key": "Free key at https://patentsview.org/apis/api-key (instant signup)",
            "usage": "Pass via --patents-key YOUR_KEY or set PATENTSVIEW_API_KEY env var",
        }
    url = "https://search.patentsview.org/api/v1/patent/"
    params = {
        "q": json.dumps({"_text_any": {"patent_abstract": query}}),
        "f": json.dumps(["patent_number", "patent_title", "patent_date", "assignees"]),
        "o": json.dumps({"per_page": limit}),
    }
    full_url = f"{url}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(full_url, headers={
            "User-Agent": "StartupResearch/1.0",
            "X-Api-Key": key,
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            patents = data.get("patents", [])
            total = data.get("total_patent_count", 0)
            return {
                "total_count": total,
                "patents": [
                    {
                        "number": p.get("patent_number", ""),
                        "title": p.get("patent_title", ""),
                        "date": p.get("patent_date", ""),
                        "assignee": (
                            p.get("assignees", [{}])[0].get("assignee_organization", "")
                            if p.get("assignees") else ""
                        ),
                    }
                    for p in patents[:limit]
                ],
                "ip_activity": "high" if total > 100 else "moderate" if total > 20 else "low",
            }
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(__file__))

    parser = argparse.ArgumentParser(description="Competitive landscape scan")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords for patent/SEC search")
    parser.add_argument("--domain-search", default=None, help="Domain keyword search query")
    parser.add_argument("--patents-key", default=None,
                        help="PatentsView API key (free at https://patentsview.org/apis/api-key). "
                             "Also reads from PATENTSVIEW_API_KEY env var.")
    parser.add_argument("--excel", default=None, metavar="FILE.xlsx",
                        help="Also save results as Excel workbook (requires openpyxl)")
    args = parser.parse_args()

    keywords = args.keywords
    excel_sheets: dict = {}

    if args.domain_search:
        print("=" * 60)
        print("DOMAIN SATURATION CHECK")
        print("=" * 60)
        domains = search_domains(args.domain_search)
        print(json.dumps(domains, indent=2))
        if args.excel:
            excel_sheets["Domains"] = domains.get("domains", [])

    print("\n" + "=" * 60)
    print("SEC EDGAR FILINGS")
    print("=" * 60)
    sec = search_sec_edgar(keywords)
    print(json.dumps(sec, indent=2))
    if args.excel:
        excel_sheets["SEC Filings"] = sec.get("filings", [])

    print("\n" + "=" * 60)
    print("PATENT LANDSCAPE")
    print("=" * 60)
    patents = search_patents(keywords, api_key=args.patents_key)
    print(json.dumps(patents, indent=2))
    if args.excel and not patents.get("skipped"):
        excel_sheets["Patents"] = patents.get("patents", [])

    if args.excel and excel_sheets:
        from excel_utils import check_openpyxl, save_to_excel
        if check_openpyxl():
            save_to_excel(args.excel, excel_sheets)
