# Changelog

## v26 (2026-04-01) — Audit & Cleanup

### Fixed
- **CRITICAL**: `customTH` declared after first use → ReferenceError in browser (let not hoisted)
- **Scoring**: NGR MoM -102% scored 49 (yellow) → now 0 (red). Formula handles negative y thresholds
- **Scoring**: NGR MoM thresholds g=0/y=-20 → g=5/y=-15 (require real growth for green)
- **Data**: CAC $33.6 → null for all GEOs (platform-level, distorted per-GEO comparison)
- **Data**: whale_top20 69.7% → null for all GEOs (platform-level, identical scores meaningless)

### Added
- Platform category blocks on main screen (avg across all GEOs)
- Summary card: replaced cac/whale with M3 Retention and Core Retention
- Standalone HTML version with settings modal and localStorage

### Architecture
- Restructured code into 8 numbered sections with documentation header
- Added update instructions for next month's data refresh
- Prepared for GitHub deployment

## v25 — NGR Sparkline

- Added 8-month NGR trend sparkline (Aug25→Mar26) on GEO detail screen
- Zero-line for GEOs with negative months
- Color: green if last value ≥0, red if negative

## v24 — Retention Recalibration

- Recalibrated retention thresholds: M1 g=25/y=15, M3 g=10/y=5, Core g=25/y=12, MoM g=10/y=0
- Bangladesh M1=25% (green) → M3=8% (yellow) = activation cliff now visible

## v23 — M3 Retention

- Replaced "one-timer rate" with M3 Retention (catches activation cliff)
- Bangladesh: dashboard score dropped from 82 to 66 (honest)

## v22 — Per-GEO Retention

- Replaced platform M2M 31.4% with per-GEO retention from user_activity_matrix
- India Core 32.6% (best), Bangladesh Core 5.8% (worst)

## v21 — Weighted Scoring

- Replaced equal weights + 3-step scoring with weighted blocks + linear 0-100
- Payments 25%, Revenue 20%, Acquisition 15%, Retention 15%, Sport 10%, Casino 7%, Base 5%, Support 3%

## v1-v20 — Development

- Progressive build from 1 block to 8 blocks
- Data ingestion from 58+ source files
- NGR cross-verification from 3 sources ($159,913)
- Player-level whale analysis (Top20 = 69.7%)
- Support KPI from BAS (FRT, CSAT, AHT, AR%)
- Peru ⛔ flag (payments disabled)
- Settings panel with per-metric threshold customization
