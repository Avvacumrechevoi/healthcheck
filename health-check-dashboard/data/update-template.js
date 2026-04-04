/*
 * ═══════════════════════════════════════════════════
 * DATA UPDATE TEMPLATE — Copy values into index.html
 * ═══════════════════════════════════════════════════
 * 
 * Sources needed:
 *   1. Marketing Reports (Power BI) → AU, FTD, Reg→FTD, Avg Dep, ARPPU, Cashout%
 *   2. Margin_Data → NGR, Deps, Wds, Margin%, Players
 *   3. user_activity_matrix (MGM.io) → M1, M3, Core Retention, Active MoM
 *   4. profit_software_games (admin) → Casino/Sport GGR, Margin, Players
 *   5. BAS support export → FRT, CSAT, AHT, AR%
 *   6. клиенты_*.xlsx (player-level) → Whale%, Segment analysis
 *
 * Steps:
 *   1. Fill in values below
 *   2. Replace D object in index.html
 *   3. Move current D values to PREV
 *   4. Append NGR to TREND arrays, shift TL labels
 *   5. Update FLAGS if needed
 */

// PREV (current month becomes previous)
const PREV = {
  "🇧🇷 Brazil":     {ngr: 81765},
  "🇦🇷 Argentina":  {ngr: 35907},
  "🇨🇱 Chile":      {ngr: 20039},
  "🇲🇽 Mexico":     {ngr: 10482},
  "🇵🇪 Peru":       {ngr: -1174},
  "🇨🇴 Colombia":   {ngr: 652},
  "🇮🇳 India":      {ngr: 6305},
  "🇧🇩 Bangladesh": {ngr: 5488},
  "🇵🇱 Poland":     {ngr: 14457},
  "🇵🇹 Portugal":   {ngr: 802},
};

// D — fill with new month's data
const D = {
  "🇧🇷 Brazil": {
    // Acquisition (Marketing Report)
    au: null,              // Active Unique players
    ftd_count: null,       // First Time Depositors
    reg_ftd_conv: null,    // Registration → FTD conversion %
    cac: null,             // Cost per acquisition (need per-GEO spend)
    // Payments (Marketing Report)
    dep_approval: null,    // Deposit approval rate %
    wd_approval: null,     // Withdrawal approval rate %
    avg_deposit: null,     // Average deposit amount $
    cashout_pct: null,     // Withdrawals / Deposits %
    // Revenue (Margin_Data)
    ngr: null,             // Net Gaming Revenue $
    ngr_mom: null,         // NGR Month-over-Month change %
    ngr_target: null,      // NGR / $150K target %
    arppu: null,           // Average Revenue Per Paying User $
    // Casino (profit_software_games)
    casino_share: null,    // Casino GGR / Total GGR %
    casino_margin: null,   // Casino net margin %
    casino_players: null,  // Casino unique players
    casino_ggr_mom: null,  // Casino GGR MoM %
    // Sport (profit_software_games)
    sport_margin: null,    // Sport net margin %
    sport_players: null,   // Sport bets per day
    sport_ggr_mom: null,   // Sport GGR MoM %
    avg_bet: null,         // Average bet size $
    // Retention (user_activity_matrix)
    d30_retention: null,   // M1 cohort retention %
    d90_retention: null,   // M3 cohort retention %
    core_retention: null,  // Core retention (4+ of last 6 months) %
    active_mom: null,      // Active players MoM change %
    // Player Health (player-level data)
    bettor_pct: null,      // % of active players who bet
    active_daily: null,    // Average daily active players
    bettor_ret: null,      // Bettor retention %
    whale_top20: null,     // Top 20 players NGR share % (need per-GEO)
    // Support (BAS)
    frt_sec: null,         // First Response Time median seconds
    csat: null,            // Customer Satisfaction %
    abandon_rate: null,    // Abandoned chats %
    aht_min: null,         // Average Handle Time median minutes
  },
  // ... repeat for each GEO
};

// TREND — append new month, remove oldest
// const TL = ["Sep","Oct","Nov","Dec","Jan","Feb","Mar","Apr"];
