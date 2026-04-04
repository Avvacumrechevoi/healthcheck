# 🏥 Health Check Dashboard — SapphireBet

Interactive health monitoring dashboard for iGaming platform across 10 GEO markets.

**Zero dependencies. Dynamic data. Auto-sync from Google Sheets.**

## 🚀 Quick Start

Open `index.html` in any browser. Or deploy via GitHub Pages.

On first load, the dashboard fetches `data.json`. After that you can edit data directly in the browser — changes save to localStorage.

## 🔄 Auto-Sync from Google Sheets (recommended)

The dashboard auto-updates 2x/day from a Google Sheet.

### Setup (one time):

1. **Create a Google Sheet** with your data (see [template](../sync/GOOGLE_SHEET_TEMPLATE.md))
   - First row = headers: `Country | NGR | FTD | AU | ...`
   - One row per country: `Brazil | 81765 | 810 | 1297 | ...`
   - Empty cells = null (metric not available)

2. **Share the sheet**: File → Share → Anyone with link → Viewer

3. **Copy the Sheet ID** from the URL:
   ```
   https://docs.google.com/spreadsheets/d/1ABC...XYZ/edit#gid=0
                                           ^^^^^^^^^^^^
                                           this is SHEET_ID
   ```

4. **Add to GitHub repo** (Settings → Variables and secrets → Variables):
   - `SHEET_ID` = your spreadsheet ID
   - `SHEET_GID` = tab number (default `0`)

5. **Done!** GitHub Actions runs `sync/sync_google_sheet.py` at 08:00 and 20:00 UTC.
   You can also trigger manually: Actions → "Sync data from Google Sheet" → Run workflow.

### How it works:

```
Google Sheet (you edit) → GitHub Actions (2x/day) → data.json → GitHub Pages → Dashboard
```

Column names are auto-mapped to metrics (NGR, FTD, CSAT, etc). Country names work in English, Russian, or ISO codes.

## 📊 Other Ways to Update Data

### CSV upload in browser
1. Export CSV from WebManagement
2. Open dashboard → 📝 → 📊 CSV tab → upload file
3. Auto-maps columns and countries → Apply

### JSON editor
1. Click **📝** in header → **📄 JSON** or **🌍 По GEO** tab
2. Edit metrics directly, then **⬇ Download JSON**

### Edit data.json directly
1. Edit `data.json` in text editor
2. Commit and push — GitHub Pages auto-deploys

## 📊 Metrics Structure

**3-level drill-down:** Platform → GEO → Category → 4 metrics each.

### 8 Blocks × 4 Metrics = 32 per GEO

| Block | Weight | Metrics |
|-------|--------|---------|
| 💳 Платежи | 25% | Deposit approval, Withdrawal approval, Avg deposit, Cashout % |
| 💰 Выручка | 20% | NGR, NGR MoM, NGR vs target, ARPPU |
| 📥 Привлечение | 15% | AU, FTD count, Reg→FTD conv, CAC |
| 🔄 Удержание | 15% | M1 ret, M3 ret, Core ret (4+/6m), Active MoM |
| ⚽ Спорт | 10% | Sport margin, Bets/day, Sport GGR MoM, Avg bet |
| 🎰 Казино | 7% | Casino share, Casino margin, Casino players, Casino GGR MoM |
| 👥 База | 5% | Bettor %, Daily active, Bettor ret, Whale Top20% |
| 🎧 Саппорт | 3% | FRT, CSAT, Abandon rate, AHT |

### Scoring
Linear 0–100 per metric. 🟢 ≥70 | 🟡 ≥40 | 🔴 <40. Weighted average → GEO score → Platform score.

## 🛠 Features

- **Auto-sync**: Google Sheet → data.json via GitHub Actions (2x/day)
- **CSV import**: upload from WebManagement with auto column mapping
- **Dynamic data**: loads from `data.json`, editable in browser
- **Data editor**: built-in UI to edit metrics, import/export JSON
- **localStorage**: edits persist between sessions
- Platform NGR sparkline (8 months)
- NGR amounts under GEO spheres
- Tap platform block → GEO ranking by that block
- Telegram export — copy formatted report
- Editable scoring thresholds
- Operational flags (e.g. Peru payments offline)
- Trend arrows (prev month comparison)
- Mobile-first, touch navigation

## 📁 Structure

```
├── health-check-dashboard/
│   ├── index.html              # Dashboard (dynamic)
│   ├── data.json               # Data file (auto-updated)
│   ├── README.md
│   ├── CHANGELOG.md
│   └── docs/
│       ├── CHANGELOG.md
│       └── UPDATE-GUIDE.md
├── sync/
│   ├── sync_google_sheet.py    # Google Sheet → data.json
│   └── GOOGLE_SHEET_TEMPLATE.md
└── .github/workflows/
    ├── pages.yml               # GitHub Pages deployment
    └── sync-data.yml           # Auto-sync cron (2x/day)
```

## 10 GEOs

🇧🇷 Brazil · 🇦🇷 Argentina · 🇨🇱 Chile · 🇲🇽 Mexico · 🇵🇪 Peru · 🇨🇴 Colombia · 🇮🇳 India · 🇧🇩 Bangladesh · 🇵🇱 Poland · 🇵🇹 Portugal
