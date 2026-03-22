#!/usr/bin/env python3
"""
Market data from free government APIs: Census Bureau, FRED, BLS, World Bank.
Usage: python market_data.py --source fred --series GDP,CPIAUCSL
       python market_data.py --source worldbank --indicator NY.GDP.MKTP.CD --country US
       python market_data.py --source bls --series CES0000000001
       python market_data.py --source census --naics 54 --api-key YOUR_KEY

Free API keys:
  FRED:   https://fred.stlouisfed.org/docs/api/api_key.html
  Census: https://api.census.gov/data/key_signup.html
  BLS:    No key needed (v1 endpoint)
  World Bank: No key needed
"""

import argparse
import json
import urllib.request
import urllib.parse


def fetch_fred(series_ids: list[str], api_key: str = None, limit: int = 24):
    """Fetch time series from FRED (Federal Reserve Economic Data)."""
    if not api_key:
        return {"error": "FRED API key required. Get free at https://fred.stlouisfed.org/docs/api/api_key.html"}
    results = {}
    for sid in series_ids:
        params = urllib.parse.urlencode({
            "series_id": sid.strip(),
            "api_key": api_key,
            "file_type": "json",
            "sort_order": "desc",
            "limit": limit,
        })
        url = f"https://api.stlouisfed.org/fred/series/observations?{params}"
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                observations = data.get("observations", [])
                results[sid] = [
                    {"date": o["date"], "value": o["value"]}
                    for o in observations if o["value"] != "."
                ]
        except Exception as e:
            results[sid] = {"error": str(e)}
    return results


def fetch_worldbank(indicator: str, country: str = "US", years: int = 10):
    """Fetch indicators from World Bank API. No auth required."""
    current_year = 2026
    start_year = current_year - years
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&per_page={years}&date={start_year}:{current_year}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            if len(data) > 1:
                return [
                    {"year": entry["date"], "value": entry["value"], "country": entry["country"]["value"]}
                    for entry in data[1] if entry["value"] is not None
                ]
            return {"error": "No data returned"}
    except Exception as e:
        return {"error": str(e)}


def fetch_bls(series_ids: list[str], start_year: int = 2020, end_year: int = 2025):
    """Fetch data from Bureau of Labor Statistics API v1 (no auth needed)."""
    url = "https://api.bls.gov/publicAPI/v1/timeseries/data/"
    payload = json.dumps({
        "seriesid": [s.strip() for s in series_ids],
        "startyear": str(start_year),
        "endyear": str(end_year),
    }).encode()
    try:
        req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            results = {}
            for series in data.get("Results", {}).get("series", []):
                sid = series["seriesID"]
                results[sid] = [
                    {"year": d["year"], "period": d["period"], "value": d["value"]}
                    for d in series.get("data", [])[:24]
                ]
            return results
    except Exception as e:
        return {"error": str(e)}


def fetch_census_business_patterns(naics: str, api_key: str = None):
    """Fetch County Business Patterns data from Census Bureau.
    Free key: https://api.census.gov/data/key_signup.html
    NAICS examples: 54=Professional services, 52=Finance, 62=Healthcare
    """
    if not api_key:
        return {"error": "Census API key required. Get free at https://api.census.gov/data/key_signup.html"}
    url = (
        f"https://api.census.gov/data/2022/cbp"
        f"?get=NAICS2017,NAICS2017_LABEL,ESTAB,EMP,PAYANN"
        f"&for=us:*&NAICS2017={naics}&key={api_key}"
    )
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            if len(data) > 1:
                headers = data[0]
                row = data[1]
                return dict(zip(headers, row))
            return {"error": "No data returned"}
    except Exception as e:
        return {"error": str(e)}


def _to_rows(source: str, result: dict | list) -> list[dict]:
    """Flatten API result into a list of flat dicts for Excel export."""
    if isinstance(result, dict) and "error" in result:
        return [{"error": result["error"]}]
    if source == "fred":
        rows = []
        for series_id, obs in result.items():
            if isinstance(obs, list):
                for o in obs:
                    rows.append({"series": series_id, **o})
        return rows
    if source == "worldbank":
        return result if isinstance(result, list) else [result]
    if source == "bls":
        rows = []
        for series_id, obs in result.items():
            if isinstance(obs, list):
                for o in obs:
                    rows.append({"series": series_id, **o})
        return rows
    if source == "census":
        return [result] if isinstance(result, dict) else result
    return [{"raw": json.dumps(result)}]


if __name__ == "__main__":
    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))

    parser = argparse.ArgumentParser(description="Market data fetcher")
    parser.add_argument("--source", required=True, choices=["fred", "worldbank", "bls", "census"])
    parser.add_argument("--series", default=None, help="Comma-separated series IDs (FRED/BLS)")
    parser.add_argument("--indicator", default=None, help="World Bank indicator code")
    parser.add_argument("--country", default="US", help="Country code")
    parser.add_argument("--naics", default=None, help="NAICS code for Census")
    parser.add_argument("--api-key", default=None, help="API key (FRED, Census)")
    parser.add_argument("--excel", default=None, metavar="FILE.xlsx",
                        help="Also save results as Excel workbook (requires openpyxl)")
    args = parser.parse_args()

    if args.source == "fred":
        series = [s.strip() for s in (args.series or "GDP").split(",")]
        result = fetch_fred(series, args.api_key)
    elif args.source == "worldbank":
        result = fetch_worldbank(args.indicator or "NY.GDP.MKTP.CD", args.country)
    elif args.source == "bls":
        series = [s.strip() for s in (args.series or "CES0000000001").split(",")]
        result = fetch_bls(series)
    elif args.source == "census":
        result = fetch_census_business_patterns(args.naics or "54", args.api_key)
    else:
        result = {"error": f"Unknown source: {args.source}"}

    print(json.dumps(result, indent=2))

    if args.excel:
        from excel_utils import check_openpyxl, save_to_excel
        if check_openpyxl():
            sheet_name = args.source.upper()
            rows = _to_rows(args.source, result)
            save_to_excel(args.excel, {sheet_name: rows})
