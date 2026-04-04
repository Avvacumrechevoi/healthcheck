# 🏥 Health Check Dashboard — SapphireBet

Interactive health monitoring dashboard for iGaming platform across 10 GEO markets.

**Zero dependencies. Dynamic data. Works offline.**

## 🚀 Quick Start

Open `index.html` in any browser. Or deploy via GitHub Pages.

On first load, the dashboard fetches `data.json`. After that you can edit data directly in the browser — changes save to localStorage.

## 📊 How to Update Data

### Option 1: Edit in browser (recommended)
1. Open dashboard, click **📝 (data icon)** in header
2. Switch to **🌍 По GEO** tab — edit metrics per GEO
3. Or paste full JSON in **📄 JSON** tab
4. Click **⬇ Скачать JSON** to export and commit to repo

### Option 2: Edit data.json directly
1. Edit `data.json` in text editor
2. Commit and push — GitHub Pages auto-deploys

### Option 3: Upload file
1. Click **📝** → **📂 Загрузить файл** → select your `.json`
2. Dashboard updates instantly

## 📁 data.json Format

```json
{
  "meta": {
    "month": "Апрель 2026",
    "month_short": "Apr",
    "prev_month_short": "мар",
    "version": "v28",
    "updated": "2026-05-01"
  },
  "flags": {},
  "trend_labels": ["Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr"],
  "plat_trend": [150972, 170247, ...],
  "prev": { "🇧🇷 Brazil": {"ngr": 81765}, ... },
  "trend": { "🇧🇷 Brazil": [51287, 79210, ...], ... },
  "data": {
    "🇧🇷 Brazil": {
      "au": 1500, "ftd_count": 900, "ngr": 95000, ...
    }
  }
}
```

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
├── index.html              # Dashboard (dynamic)
├── data.json               # Data file (editable)
├── README.md
├── CHANGELOG.md
├── docs/
│   ├── CHANGELOG.md
│   └── UPDATE-GUIDE.md
└── data/
    ├── sources.md
    └── update-template.js
```

## 10 GEOs

🇧🇷 Brazil · 🇦🇷 Argentina · 🇨🇱 Chile · 🇲🇽 Mexico · 🇵🇪 Peru · 🇨🇴 Colombia · 🇮🇳 India · 🇧🇩 Bangladesh · 🇵🇱 Poland · 🇵🇹 Portugal
