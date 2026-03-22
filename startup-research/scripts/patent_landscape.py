#!/usr/bin/env python3
"""
Focused patent landscape analysis via PatentsView API.
Usage: python patent_landscape.py --query "machine learning fraud detection" --key YOUR_KEY
       python patent_landscape.py --query "drone delivery" --key YOUR_KEY --excel drone-patents.xlsx

Requires a free API key: https://patentsview.org/apis/api-key (instant signup)
Also reads from PATENTSVIEW_API_KEY environment variable.

More targeted than the quick patent search in competitive_scan.py.
Docs: https://search.patentsview.org/docs/
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.parse
from collections import Counter


def search_patents_by_abstract(query: str, limit: int = 50, api_key: str = None):
    """Search patents by abstract text. Requires PatentsView API key."""
    key = api_key or os.environ.get("PATENTSVIEW_API_KEY")
    if not key:
        return {
            "error": "PatentsView API key required.",
            "get_key": "Free instant signup at https://patentsview.org/apis/api-key",
            "usage": "Pass via --key YOUR_KEY or set PATENTSVIEW_API_KEY env var",
        }
    url = "https://search.patentsview.org/api/v1/patent/"
    params = {
        "q": json.dumps({"_text_any": {"patent_abstract": query}}),
        "f": json.dumps([
            "patent_number", "patent_title", "patent_date",
            "patent_abstract", "assignees", "inventors",
        ]),
        "o": json.dumps({"per_page": limit}),
    }
    full_url = f"{url}?{urllib.parse.urlencode(params)}"
    try:
        req = urllib.request.Request(full_url, headers={
            "User-Agent": "StartupResearch/1.0",
            "X-Api-Key": key,
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}


def analyze_patent_landscape(data: dict) -> dict:
    """Derive signals from raw patent data."""
    patents = data.get("patents", [])
    if not patents:
        return {"error": "No patents found", "total": data.get("total_patent_count", 0)}

    # Top assignees (companies filing in this space)
    assignees = []
    for p in patents:
        for a in p.get("assignees", []):
            org = a.get("assignee_organization", "")
            if org:
                assignees.append(org)

    # Filing trend by year
    yearly = Counter()
    for p in patents:
        date = p.get("patent_date", "")
        if date:
            year = date[:4]
            yearly[year] += 1

    sorted_years = sorted(yearly.items())
    trend = "rising" if len(sorted_years) >= 2 and sorted_years[-1][1] > sorted_years[-2][1] else "stable/declining"

    total = data.get("total_patent_count", 0)
    return {
        "total_patents": total,
        "ip_activity_level": "high" if total > 100 else "moderate" if total > 20 else "low",
        "filing_trend": trend,
        "filing_by_year": dict(sorted_years[-5:]),  # last 5 years
        "top_assignees": [org for org, _ in Counter(assignees).most_common(10)],
        "sample_patents": [
            {
                "number": p.get("patent_number", ""),
                "title": p.get("patent_title", ""),
                "date": p.get("patent_date", ""),
                "assignee": (p.get("assignees", [{}])[0].get("assignee_organization", "") if p.get("assignees") else ""),
            }
            for p in patents[:10]
        ],
        "strategic_signals": _derive_signals(total, assignees, trend),
    }


def _derive_signals(total: int, assignees: list, trend: str) -> list[str]:
    signals = []
    if total > 200:
        signals.append("Heavy patent activity — space is crowded and defensible by incumbents")
    elif total > 50:
        signals.append("Moderate patent activity — some IP risk, but room for innovation")
    else:
        signals.append("Low patent activity — space is open, early mover IP advantage possible")

    top = Counter(assignees).most_common(3)
    if top:
        names = ", ".join(org for org, _ in top)
        signals.append(f"Top IP holders: {names}")

    if trend == "rising":
        signals.append("Rising filing trend — growing corporate interest in this space")
    return signals


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(__file__))

    parser = argparse.ArgumentParser(description="Patent landscape analysis")
    parser.add_argument("--query", required=True, help="Keywords to search in patent abstracts")
    parser.add_argument("--limit", type=int, default=50, help="Max patents to fetch (default: 50)")
    parser.add_argument("--key", default=None,
                        help="PatentsView API key (free at https://patentsview.org/apis/api-key). "
                             "Also reads from PATENTSVIEW_API_KEY env var.")
    parser.add_argument("--excel", default=None, metavar="FILE.xlsx",
                        help="Also save results as Excel workbook (requires openpyxl)")
    args = parser.parse_args()

    print(f"Searching PatentsView for: '{args.query}'...")
    raw = search_patents_by_abstract(args.query, args.limit, api_key=args.key)

    if "error" in raw:
        print(json.dumps(raw, indent=2))
    else:
        analysis = analyze_patent_landscape(raw)
        print("\n" + "=" * 60)
        print("PATENT LANDSCAPE ANALYSIS")
        print("=" * 60)
        print(json.dumps(analysis, indent=2))

        if args.excel:
            from excel_utils import check_openpyxl, save_to_excel
            if check_openpyxl():
                excel_sheets = {}
                # Summary sheet
                excel_sheets["Summary"] = [
                    {"metric": "Total Patents", "value": analysis.get("total_patents", 0)},
                    {"metric": "IP Activity Level", "value": analysis.get("ip_activity_level", "")},
                    {"metric": "Filing Trend", "value": analysis.get("filing_trend", "")},
                ]
                for signal in analysis.get("strategic_signals", []):
                    excel_sheets["Summary"].append({"metric": "Strategic Signal", "value": signal})

                # Filing by year
                filing_by_year = analysis.get("filing_by_year", {})
                if filing_by_year:
                    excel_sheets["Filing by Year"] = [
                        {"year": year, "patent_count": count}
                        for year, count in sorted(filing_by_year.items())
                    ]

                # Top assignees
                top_assignees = analysis.get("top_assignees", [])
                if top_assignees:
                    excel_sheets["Top Assignees"] = [
                        {"rank": i + 1, "assignee": org}
                        for i, org in enumerate(top_assignees)
                    ]

                # Sample patents
                sample = analysis.get("sample_patents", [])
                if sample:
                    excel_sheets["Sample Patents"] = sample

                save_to_excel(args.excel, excel_sheets)
