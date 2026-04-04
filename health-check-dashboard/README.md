# 🏥 Health Check Dashboard — SapphireBet

Interactive health monitoring dashboard for iGaming platform across 10 GEO markets.

**Zero dependencies. Single file. Works offline.**

## 🚀 Quick Start

Open `index.html` in any browser. Or deploy via GitHub Pages.

## 📊 What It Shows

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

- Platform NGR sparkline (8 months)
- NGR amounts under GEO spheres
- Tap platform block → GEO ranking by that block
- ✈ Telegram export — copy formatted report for CEO
- ⚙ Editable thresholds (localStorage)
- ⛔ Operational flags (e.g. Peru payments offline)
- Feb → Mar trend arrows
- Mobile-first, touch navigation

## 📁 Structure

```
├── index.html              # Dashboard
├── README.md
├── docs/
│   ├── CHANGELOG.md        # Version history
│   └── UPDATE-GUIDE.md     # How to update for next month
└── data/
    └── sources.md          # Data sources & verification
```

## 🔄 Monthly Update

See [docs/UPDATE-GUIDE.md](docs/UPDATE-GUIDE.md). Edit 3 objects in `index.html`: `D`, `TREND`, `PREV`.

## 10 GEOs

🇧🇷 Brazil · 🇦🇷 Argentina · 🇨🇱 Chile · 🇲🇽 Mexico · 🇵🇪 Peru · 🇨🇴 Colombia · 🇮🇳 India · 🇧🇩 Bangladesh · 🇵🇱 Poland · 🇵🇹 Portugal
