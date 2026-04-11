# Changelog

## v31 (2026-04-12) — Current
### Added
- **Heatmap matrix**: 10×8 GEO × Category table on main screen — cross-GEO comparison at a glance
- **Signal actions**: every alert now includes prescriptive action ("→ Проверить платёжки")
- **Cross-GEO metric ranking**: category drill-down shows mini-ranking of all GEOs per metric
- **Gray-first design**: green (score ≥70) spheres are muted gray; only problems are colorful
- **Extended Telegram report**: platform pulse (NGR, Margin, AU, FTD), QoQ, TOP-3 problems, unicode sparklines ▁▂▃▅▇
- **Dynamic dates**: all hardcoded "Q1 2026", "фев→мар", "март 2026" replaced with META-driven labels
- **Target visibility**: each metric row shows green threshold as "→25%" target
- **NLG exec summary**: margin%, AU, FTD, worst category diagnostic, concentration warning
- **Mobile CSS**: compact grid on <480px screens
- **Expanded prev data**: all 32 metrics per GEO stored in prev for full trend arrows

### Changed
- Version bumped to v31
- Telegram report restructured: pulse → problems → ranking → blocks → growth
- Sphere function accepts grayFirst parameter for muted healthy states

## v30 (2026-04-08)
### Added
- Segments section (VIP++, VIP+, Core, etc.) with MoM comparison
- Retention table with M1/M3/Core/Bettor columns
- Deposit conversion funnel (Reg→Dep→CR2→CR3→CR5)
- Per-GEO history sparklines (players, ARPPU, margin, cashout)
- Platform pulse mini-KPIs (NGR, Deposits, Margin, Players)
- QoQ comparison card

## v28 (2026-04-04)
### Added
- **Dynamic data**: extracted all data from index.html into `data.json`
- **Data editor**: built-in UI with 3 tabs (JSON / Per GEO / Meta)
- **File upload**: drag & drop or file picker for JSON import
- **JSON export**: download current data as JSON file
- **localStorage persistence**: edits survive page reload
- **Reset to file**: one-click revert to data.json
- Data source badge in header (local/json/empty)

### Changed
- Data no longer hardcoded in index.html
- Dashboard loads data.json on startup, localStorage takes priority
- Telegram report uses dynamic month from meta
- Version bumped to v28

## v27 (2026-04-01)
### Added
- Platform NGR sparkline on main screen (8-month trend)
- NGR dollar amounts under GEO spheres (replaces status text)
- Tap platform block → GEO ranking dropdown by that category
- Telegram export button (✈) — copies formatted CEO report to clipboard
- Toast notification on clipboard copy

### Changed
- Header: two buttons (Telegram + Settings) instead of one

## v26 (2026-03-31) — Audit Release
### Fixed
- **CRITICAL**: `customTH` declared after first use → ReferenceError on load
- NGR MoM scoring: Peru -102% was scoring 49 (yellow), now correctly 0 (red)
- Negative threshold formula: linear decay to 0 instead of clamping at 49

### Changed
- CAC → null for all GEOs (platform-level $33.6 distorted per-GEO comparison)
- whale_top20 → null for all GEOs (identical 69.7% = meaningless scores)
- NGR MoM thresholds: g=0/y=-20 → g=5/y=-15 (require real growth for green)
- Summary card: replaced CAC/whale with M3 retention + Core retention

### Added
- Platform category blocks on main screen (avg across all GEOs)
- Code documentation header with update instructions

## v25 (2026-03-30)
### Added
- NGR sparkline trend per GEO (8 months Aug25→Mar26)
- Settings panel (⚙) with per-metric threshold editor
- localStorage persistence for custom thresholds

## v24 (2026-03-29)
### Changed
- Retention thresholds recalibrated: M1 g=25/y=15, M3 g=10/y=5, Core g=25/y=12

## v23 (2026-03-28)
### Changed
- Replaced one-timer rate with M3 Retention (catches activation cliff)
- Bangladesh M1=24.8% → M3=7.9% = 68% churn now visible

## v22 (2026-03-27)
### Changed
- Per-GEO M2M retention from user_activity_matrix (was platform 31.4% for all)

## v21 (2026-03-26)
### Added
- Weighted block scoring (Payments 25%, Revenue 20%, etc.)
- Linear 0-100 scoring (replaced 3-step green/yellow/red)

## v1-v20 (2026-03-15 → 2026-03-25)
- Initial build, data collection from 58 source files
- 10 GEOs, 8 blocks, 32 metrics per GEO
- Cross-verified NGR from 3 sources ($174,723)
- Peru ⛔ flag, breadcrumb nav, mobile optimization
