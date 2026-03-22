#!/usr/bin/env python3
"""
Trend analysis using pytrends (Google Trends) and NewsAPI.
Usage: python trend_analysis.py --keywords "keyword1,keyword2" --timeframe "today 5-y"
       python trend_analysis.py --keywords "fintech,payments" --news-key YOUR_KEY --news-query "fintech startup"

Dependencies: pip install pytrends
Free NewsAPI key: https://newsapi.org/register
"""

import argparse
import json
import sys
from datetime import datetime, timedelta


def search_google_trends(keywords: list[str], timeframe: str = "today 5-y", geo: str = ""):
    """Pull Google Trends interest-over-time data."""
    try:
        from pytrends.request import TrendReq
        pytrends = TrendReq(hl='en-US', tz=360)
        all_results = {}
        for i in range(0, len(keywords), 5):
            batch = keywords[i:i+5]
            pytrends.build_payload(batch, cat=0, timeframe=timeframe, geo=geo)
            data = pytrends.interest_over_time()
            if not data.empty:
                for kw in batch:
                    if kw in data.columns:
                        series = data[kw]
                        all_results[kw] = {
                            "current": int(series.iloc[-1]),
                            "peak": int(series.max()),
                            "mean": round(float(series.mean()), 1),
                            "trend_direction": "rising" if series.iloc[-1] > series.iloc[-13] else "declining",
                            "yoy_change_pct": round(
                                ((series.iloc[-1] - series.iloc[-13]) / max(series.iloc[-13], 1)) * 100, 1
                            ),
                            "data_points": len(series),
                        }
        return all_results
    except ImportError:
        return {"error": "pytrends not installed. Run: pip install pytrends --break-system-packages"}
    except Exception as e:
        return {"error": str(e)}


def search_related_queries(keywords: list[str], geo: str = ""):
    """Pull related and rising queries from Google Trends."""
    try:
        from pytrends.request import TrendReq
        pytrends = TrendReq(hl='en-US', tz=360)
        results = {}
        for kw in keywords[:5]:
            pytrends.build_payload([kw], cat=0, timeframe="today 12-m", geo=geo)
            related = pytrends.related_queries()
            if kw in related:
                top = related[kw].get("top")
                rising = related[kw].get("rising")
                results[kw] = {
                    "top_queries": top.head(10).to_dict("records") if top is not None and not top.empty else [],
                    "rising_queries": rising.head(10).to_dict("records") if rising is not None and not rising.empty else [],
                }
        return results
    except ImportError:
        return {"error": "pytrends not installed"}
    except Exception as e:
        return {"error": str(e)}


def search_news_api(query: str, api_key: str = None, days_back: int = 30):
    """Search recent news articles via NewsAPI (free tier: 100 req/day)."""
    import urllib.request
    import urllib.parse
    if not api_key:
        return {"error": "NewsAPI key required. Get free key at https://newsapi.org/register"}
    from_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    params = urllib.parse.urlencode({
        "q": query,
        "from": from_date,
        "sortBy": "relevancy",
        "language": "en",
        "pageSize": 20,
        "apiKey": api_key,
    })
    url = f"https://newsapi.org/v2/everything?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "StartupResearch/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            articles = data.get("articles", [])
            return {
                "total_results": data.get("totalResults", 0),
                "articles": [
                    {
                        "title": a.get("title", ""),
                        "source": a.get("source", {}).get("name", ""),
                        "published": a.get("publishedAt", ""),
                        "description": (a.get("description", "") or "")[:200],
                        "url": a.get("url", ""),
                    }
                    for a in articles[:10]
                ],
            }
    except Exception as e:
        return {"error": str(e)}


def check_dependencies() -> bool:
    """Check required dependencies and print actionable install instructions if missing."""
    missing = []
    try:
        import pytrends  # noqa: F401
    except ImportError:
        missing.append("pytrends")
    if missing:
        print("WARNING: Missing dependencies for trend_analysis.py:")
        for pkg in missing:
            print(f"  pip install {pkg} --break-system-packages")
        print("Google Trends data will not be available. Continuing with NewsAPI only (if key provided).")
        print("=" * 60)
        return False
    return True


if __name__ == "__main__":
    import os
    sys.path.insert(0, os.path.dirname(__file__))

    _has_pytrends = check_dependencies()
    parser = argparse.ArgumentParser(description="Startup trend analysis")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords")
    parser.add_argument("--timeframe", default="today 5-y", help="Google Trends timeframe")
    parser.add_argument("--geo", default="", help="Country code (e.g., US, DE)")
    parser.add_argument("--news-key", default=None, help="NewsAPI key (optional)")
    parser.add_argument("--news-query", default=None, help="News search query (optional)")
    parser.add_argument("--excel", default=None, metavar="FILE.xlsx",
                        help="Also save results as Excel workbook (requires openpyxl)")
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",")]

    excel_sheets: dict = {}

    if _has_pytrends:
        print("=" * 60)
        print("GOOGLE TRENDS ANALYSIS")
        print("=" * 60)
        trends = search_google_trends(keywords, args.timeframe, args.geo)
        print(json.dumps(trends, indent=2))
        if args.excel and isinstance(trends, dict) and "error" not in trends:
            excel_sheets["Trends"] = [
                {"keyword": kw, **vals}
                for kw, vals in trends.items()
                if isinstance(vals, dict)
            ]

        print("\n" + "=" * 60)
        print("RELATED & RISING QUERIES")
        print("=" * 60)
        related = search_related_queries(keywords, args.geo)
        print(json.dumps(related, indent=2))
        if args.excel and isinstance(related, dict) and "error" not in related:
            rising_rows = []
            for kw, data in related.items():
                for q in data.get("rising_queries", []):
                    rising_rows.append({"keyword": kw, "type": "rising", **q})
                for q in data.get("top_queries", []):
                    rising_rows.append({"keyword": kw, "type": "top", **q})
            if rising_rows:
                excel_sheets["Related Queries"] = rising_rows
    else:
        print("GOOGLE TRENDS ANALYSIS — SKIPPED (pytrends not installed)")
        print("Install with: pip install pytrends --break-system-packages")

    if args.news_key and args.news_query:
        print("\n" + "=" * 60)
        print("NEWS ANALYSIS")
        print("=" * 60)
        news = search_news_api(args.news_query, args.news_key)
        print(json.dumps(news, indent=2))
        if args.excel and isinstance(news, dict) and "articles" in news:
            excel_sheets["News"] = news["articles"]

    if args.excel and excel_sheets:
        from excel_utils import check_openpyxl, save_to_excel
        if check_openpyxl():
            save_to_excel(args.excel, excel_sheets)
