# Google Sheets Template for Health Check Dashboard

## Quick Setup

1. Create a new Google Sheet
2. Make first row = headers (see below)
3. Fill in data for each GEO (one row per country)
4. Share: **File → Share → Anyone with link → Viewer**

## Sheet Format

First row must be headers. One row per country. Use any of these column names:

| Column Name | Metric | Notes |
|------------|--------|-------|
| **Country** or **Страна** | (GEO identifier) | Required. First column recommended |
| **NGR** | ngr | Net Gaming Revenue $ |
| **NGR MoM** | ngr_mom | NGR month-over-month % |
| **NGR Target** | ngr_target | NGR vs $150K target % |
| **ARPPU** | arppu | Avg Revenue Per Paying User $ |
| **AU** or **Active Unique** | au | Active unique players |
| **FTD** | ftd_count | First time depositors |
| **Reg FTD Conv** | reg_ftd_conv | Registration → FTD conversion % |
| **CAC** | cac | Cost per acquisition $ |
| **Dep Approval** or **Deposit Approval** | dep_approval | Deposit approval rate % |
| **Wd Approval** or **Withdraw Approval** | wd_approval | Withdrawal approval rate % |
| **Avg Deposit** | avg_deposit | Average deposit $ |
| **Cashout** | cashout_pct | Withdrawals / Deposits % |
| **Casino Share** | casino_share | Casino GGR / Total GGR % |
| **Casino Margin** | casino_margin | Casino net margin % |
| **Casino Players** | casino_players | Casino unique players |
| **Casino GGR MoM** | casino_ggr_mom | Casino GGR month-over-month % |
| **Sport Margin** | sport_margin | Sport net margin % |
| **Sport Players** or **Bets/day** | sport_players | Sport bets per day |
| **Sport GGR MoM** | sport_ggr_mom | Sport GGR month-over-month % |
| **Avg Bet** | avg_bet | Average bet $ |
| **D30 Retention** or **M1 Ret** | d30_retention | Month 1 retention % |
| **D90 Retention** or **M3 Ret** | d90_retention | Month 3 retention % |
| **Core Retention** | core_retention | Core retention (4+/6m) % |
| **Active MoM** | active_mom | Active players MoM % |
| **Bettor Pct** | bettor_pct | % of active who bet |
| **Active Daily** or **DAU** | active_daily | Daily active players |
| **Bettor Ret** | bettor_ret | Bettor retention % |
| **Whale Top20** | whale_top20 | Top 20 players NGR share % |
| **FRT** | frt_sec | First response time seconds |
| **CSAT** | csat | Customer satisfaction % |
| **Abandon Rate** or **AR%** | abandon_rate | Abandoned chats % |
| **AHT** | aht_min | Average handle time minutes |

## Country Names

Any of these will work in the Country column:

| Dashboard GEO | Accepted names |
|--------------|----------------|
| 🇧🇷 Brazil | Brazil, Бразилия, Brasil, BR |
| 🇦🇷 Argentina | Argentina, Аргентина, AR |
| 🇨🇱 Chile | Chile, Чили, CL |
| 🇲🇽 Mexico | Mexico, Мексика, México, MX |
| 🇵🇪 Peru | Peru, Перу, Perú, PE |
| 🇨🇴 Colombia | Colombia, Колумбия, CO |
| 🇮🇳 India | India, Индия, IN |
| 🇧🇩 Bangladesh | Bangladesh, Бангладеш, BD |
| 🇵🇱 Poland | Poland, Польша, Polska, PL |
| 🇵🇹 Portugal | Portugal, Португалия, PT |

## Example Sheet

```
Country     | NGR    | FTD  | AU   | Dep Approval | CSAT | D30 Retention
Brazil      | 81765  | 810  | 1297 | 86.6         | 54.4 | 15.3
Argentina   | 35907  | 1696 | 2195 | 75.4         | 52.8 | 13.1
Chile       | 20039  | 423  | 522  | 61.2         | 60.0 | 13.1
Mexico      | 10482  | 123  | 225  | 55.9         | 68.8 | 10.7
Peru        | -1174  | 84   | 161  | 0            | 67.6 | 17.3
Colombia    | 652    | 67   |      | 86.1         | 76.9 | 22.6
India       | 6305   | 27   |      | 24.1         | 37.1 | 26.5
Bangladesh  | 5488   | 243  |      | 47.3         | 57.4 | 24.8
Poland      | 14457  | 14   |      | 84.7         | 36.1 | 21.0
Portugal    | 802    | 30   |      | 77.5         | 58.3 | 15.5
```

Empty cells = `null` (metric not available, excluded from scoring).

## Sheet ID

Your Sheet URL looks like:
```
https://docs.google.com/spreadsheets/d/1ABC...XYZ/edit#gid=0
```

The **SHEET_ID** is the part between `/d/` and `/edit`:
```
1ABC...XYZ
```

The **SHEET_GID** is the number after `#gid=` (default `0` for first tab).
