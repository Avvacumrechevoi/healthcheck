#!/usr/bin/env python3
"""
Sync Google Sheet → data.json for Health Check Dashboard.

Reads a public Google Sheet with GEO metrics, parses it,
merges with existing data.json (preserving trend/prev/flags),
and writes the updated file.

Usage:
  python sync/sync_google_sheet.py

Env vars:
  SHEET_ID       — Google Spreadsheet ID (from URL)
  SHEET_GID      — (optional) sheet tab GID, default "0"
  DATA_JSON_PATH — (optional) path to data.json, default "health-check-dashboard/data.json"

The Google Sheet must be published or shared with "anyone with link".
"""

import csv
import io
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

# ─── Config ───

SHEET_ID = os.environ.get("SHEET_ID", "")
SHEET_GID = os.environ.get("SHEET_GID", "0")
DATA_JSON_PATH = os.environ.get("DATA_JSON_PATH", "health-check-dashboard/data.json")

GEO_ALIASES = {
    "brazil": "🇧🇷 Brazil", "бразилия": "🇧🇷 Brazil", "brasil": "🇧🇷 Brazil", "br": "🇧🇷 Brazil",
    "argentina": "🇦🇷 Argentina", "аргентина": "🇦🇷 Argentina", "ar": "🇦🇷 Argentina",
    "chile": "🇨🇱 Chile", "чили": "🇨🇱 Chile", "cl": "🇨🇱 Chile",
    "mexico": "🇲🇽 Mexico", "мексика": "🇲🇽 Mexico", "mx": "🇲🇽 Mexico", "méxico": "🇲🇽 Mexico",
    "peru": "🇵🇪 Peru", "перу": "🇵🇪 Peru", "pe": "🇵🇪 Peru", "perú": "🇵🇪 Peru",
    "colombia": "🇨🇴 Colombia", "колумбия": "🇨🇴 Colombia", "co": "🇨🇴 Colombia",
    "india": "🇮🇳 India", "индия": "🇮🇳 India", "in": "🇮🇳 India",
    "bangladesh": "🇧🇩 Bangladesh", "бангладеш": "🇧🇩 Bangladesh", "bd": "🇧🇩 Bangladesh",
    "poland": "🇵🇱 Poland", "польша": "🇵🇱 Poland", "pl": "🇵🇱 Poland", "polska": "🇵🇱 Poland",
    "portugal": "🇵🇹 Portugal", "португалия": "🇵🇹 Portugal", "pt": "🇵🇹 Portugal",
}

KNOWN_GEOS = list({v for v in GEO_ALIASES.values()})

COLUMN_MAP = {
    "au": [r"active.?unique", r"\bau\b", r"активн.*уник"],
    "ftd_count": [r"\bftd\b", r"first.?time.?dep", r"первый.?деп"],
    "reg_ftd_conv": [r"reg.*ftd", r"conv", r"конверс"],
    "cac": [r"\bcac\b", r"cost.?per.?acq"],
    "dep_approval": [r"dep.*approv", r"одобр.*деп", r"deposit.*approv"],
    "wd_approval": [r"wd.*approv|withdraw.*approv", r"одобр.*выв"],
    "avg_deposit": [r"avg.*dep|сред.*деп|average.*dep"],
    "cashout_pct": [r"cashout|кэшаут|cash.*out"],
    "ngr": [r"^ngr$", r"net.?gaming"],
    "ngr_mom": [r"ngr.*mom|mom.*ngr"],
    "ngr_target": [r"ngr.*target|ngr.*150"],
    "arppu": [r"arppu|arpu"],
    "casino_share": [r"casino.*share|доля.*казино"],
    "casino_margin": [r"casino.*margin|маржа.*казино"],
    "casino_players": [r"casino.*player|игроки.*казино"],
    "casino_ggr_mom": [r"casino.*ggr.*mom"],
    "sport_margin": [r"sport.*margin|маржа.*спорт"],
    "sport_players": [r"sport.*player|ставок|bets.*day"],
    "sport_ggr_mom": [r"sport.*ggr.*mom"],
    "avg_bet": [r"avg.*bet|сред.*ставк"],
    "d30_retention": [r"d30|m1.*ret|ret.*m1|ret.*30"],
    "d90_retention": [r"d90|m3.*ret|ret.*m3|ret.*90"],
    "core_retention": [r"core.*ret|удерж.*ядр"],
    "active_mom": [r"active.*mom|актив.*mom"],
    "bettor_pct": [r"bettor.*pct|бетт"],
    "active_daily": [r"active.*daily|актив.*день|daily.*active|\bdau\b"],
    "bettor_ret": [r"bettor.*ret"],
    "whale_top20": [r"whale|top.*20|кит"],
    "frt_sec": [r"\bfrt\b|first.*resp"],
    "csat": [r"\bcsat\b|satisf"],
    "abandon_rate": [r"abandon|ar%|пропущ"],
    "aht_min": [r"\baht\b|handle.*time"],
}


def resolve_geo(raw: str) -> str | None:
    s = raw.strip()
    if not s:
        return None
    low = s.lower()
    if low in GEO_ALIASES:
        return GEO_ALIASES[low]
    for geo in KNOWN_GEOS:
        country = geo.split(" ", 1)[-1].lower()
        if country in low or low in country:
            return geo
    return None


def guess_metric(col_name: str) -> str:
    low = col_name.strip().lower()
    for metric, patterns in COLUMN_MAP.items():
        for p in patterns:
            if re.search(p, low, re.IGNORECASE):
                return metric
    return ""


def guess_country_col(headers: list[str]) -> int:
    hints = ["country", "страна", "geo", "гео", "region", "регион"]
    for i, h in enumerate(headers):
        low = h.lower()
        for hint in hints:
            if hint in low:
                return i
    return 0


def parse_number(raw: str) -> float | None:
    s = raw.strip().replace("\xa0", "").replace(" ", "")
    if not s or s == "-" or s.lower() in ("null", "n/a", "na", "—", "–"):
        return None
    s = s.replace(",", ".")
    s = re.sub(r"[%$€]", "", s)
    try:
        return float(s)
    except ValueError:
        return None


def download_sheet_csv(sheet_id: str, gid: str = "0") -> str:
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    print(f"[sync] Downloading: {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    text = data.decode("utf-8-sig")
    print(f"[sync] Downloaded {len(text)} bytes")
    return text


def parse_sheet(csv_text: str) -> dict:
    reader = csv.reader(io.StringIO(csv_text))
    rows = list(reader)
    if len(rows) < 2:
        raise ValueError("Sheet has less than 2 rows")

    headers = rows[0]
    data_rows = rows[1:]

    country_col = guess_country_col(headers)
    print(f"[sync] Country column: {country_col} ({headers[country_col]})")

    col_mapping = {}
    for i, h in enumerate(headers):
        if i == country_col:
            continue
        metric = guess_metric(h)
        if metric:
            col_mapping[i] = metric
            print(f"[sync] Column {i} '{h}' → {metric}")
        else:
            print(f"[sync] Column {i} '{h}' → (skipped)")

    if not col_mapping:
        raise ValueError("No columns could be mapped to metrics")

    result = {}
    for row in data_rows:
        if len(row) <= country_col:
            continue
        raw_geo = row[country_col]
        geo = resolve_geo(raw_geo)
        if not geo:
            print(f"[sync] ⚠ Unknown GEO: '{raw_geo}' — skipped")
            continue

        geo_data = {}
        for col_idx, metric in col_mapping.items():
            if col_idx < len(row):
                val = parse_number(row[col_idx])
                if val is not None:
                    geo_data[metric] = val

        if geo_data:
            result[geo] = geo_data
            print(f"[sync] ✓ {geo}: {len(geo_data)} metrics")

    return result


def merge_data(existing: dict, new_geo_data: dict) -> dict:
    """Merge new metric values into existing data.json structure."""
    ds = json.loads(json.dumps(existing))

    if "data" not in ds:
        ds["data"] = {}

    for geo, metrics in new_geo_data.items():
        if geo not in ds["data"]:
            ds["data"][geo] = {}
        for mk, val in metrics.items():
            ds["data"][geo][mk] = val

    ds["meta"]["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return ds


def main():
    if not SHEET_ID:
        print("[sync] ERROR: SHEET_ID env var not set")
        print("[sync] Set it to the Google Spreadsheet ID from the URL:")
        print("[sync]   https://docs.google.com/spreadsheets/d/SHEET_ID/edit")
        sys.exit(1)

    csv_text = download_sheet_csv(SHEET_ID, SHEET_GID)

    new_data = parse_sheet(csv_text)
    if not new_data:
        print("[sync] WARNING: No data parsed from sheet")
        sys.exit(1)

    print(f"[sync] Parsed {len(new_data)} GEOs from sheet")

    if os.path.exists(DATA_JSON_PATH):
        with open(DATA_JSON_PATH, "r", encoding="utf-8") as f:
            existing = json.load(f)
        print(f"[sync] Loaded existing {DATA_JSON_PATH}")
    else:
        existing = {
            "meta": {"month": "", "month_short": "", "prev_month_short": "", "version": "v29", "updated": ""},
            "flags": {},
            "trend_labels": [],
            "plat_trend": [],
            "prev": {},
            "trend": {},
            "data": {},
        }
        print(f"[sync] No existing data.json — creating new")

    merged = merge_data(existing, new_data)

    with open(DATA_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f"[sync] ✅ Written to {DATA_JSON_PATH}")
    print(f"[sync] GEOs in file: {list(merged['data'].keys())}")


if __name__ == "__main__":
    main()
