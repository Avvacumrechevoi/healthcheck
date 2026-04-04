# 📐 Data Sources & Verification

## March 2026 Data

### NGR Cross-Verification (3 sources → $174,723)

| Source | Value | Match |
|--------|-------|-------|
| Margin_Data FIN_Result | $174,723 | ✅ |
| Marketing reports (sum 10 GEO) | $174,723 | ✅ |
| Player-level клиенты_март sum | $174,723 | ✅ |
| CEO dashboard (gross) | $209,265 | ❌ Different methodology (Deps-Wds, no bonus/commission deduction) |

### Source Files Used (58 total)

**Marketing reports (per GEO, monthly):**
- `маркетинговый_отчет_март_2026_бразилия.xlsx` — AU, FTD, NGR, ARPPU, Cashout%
- Same for: Argentina, Chile, Mexico, Peru

**Financial:**
- `Margin_Data_Aug2025_Mar2026.xlsx` — NGR, Deposits, Withdrawals, Margin%, Players per GEO per month

**Retention:**
- MGM.io export `user_activity_matrix` — 48,788 rows, per-GEO M1/M3/Core retention

**Support:**
- BAS `geo_healthcheck` — FRT, CSAT, AR%, AHT per GEO (4,852 dialogs)

**Player-level:**
- `клиенты_март_2026.xlsx` — individual player NGR, deposits, withdrawals, segment

### Platform NGR Sum Reconciliation

Dashboard D.ngr sum = $174,723 (PLAT_TREND March value). Previously documented as $159,913 — corrected after v27 data re-import.

### Known Data Gaps

| Metric | Status | Reason |
|--------|--------|--------|
| CAC per GEO | null | Only platform-level ($33.6) available |
| whale_top20 per GEO | null | No "Country" field in player-level files |
| Casino data (5 GEOs) | null | Missing profit_software_games for IN, BD, PL, PT, CO |
| casino_ggr_mom, sport_ggr_mom | null | Missing February profit files for comparison |

### Transit Accounts (excluded from raw transaction analysis)

IDs: 782755341, 912332471, 524097265, 669280217, 982181233

These do NOT appear in BI player-level files (клиенты_*.xlsx) but inflate withdrawals in raw transaction exports.

### VIP++ Verification (March 2026)

Top negative NGR players verified as real (not transit):
- Player #4029 (Вип++): NGR -$38,946 — real player, deposited $12K, withdrew $51K
- Player #6535 (Вип++): NGR -$25,357 — real player, deposited $102K, withdrew $128K

All 5 transit account IDs confirmed absent from клиенты_март_2026.xlsx.
