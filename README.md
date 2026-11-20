# THE WORLD — Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/zihaeakb/news-image-20261120-v2/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/zihaeakb/news-image-20261120-v2/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A newspaper front page summing up the world's news of Friday 20 November
2026 in one image. Drawn from scratch with PIL (`draw.py`, Noto Serif Black
headlines / Noto Sans body); `main.py` copies `entry.png` to
`/output/entry.png` (byte-identical on every run).

## The eight stories

1. **THE HAGUE — WORLD COURT: Myanmar guilty of Rohingya genocide (LEAD).**
   On 19 Nov the ICJ ruled 9-6 that Myanmar committed genocide against the
   Rohingya in its 2016-17 "clearance operations" — the first genocide finding
   against a state. ~10,000 killed, ~400 villages destroyed. The court ordered
   reparations and the return of the displaced.
   Sources: UN News (https://news.un.org/en/story/2026/11/1168836),
   Human Rights Watch (https://www.hrw.org/news/2026/11/19/world-court-finds-myanmar-committed-rohingya-genocide),
   CNN (https://www.cnn.com/2026/11/19/asia/icj-myanmar-genocide-rohingya-ruling-intl-hnk)
2. **SHENZHEN — SUMMIT: Trump, Xi & Putin sign peace pledge.** First-ever
   three-way summit, 19 Nov at Kylin Villa. Joint declaration: "a nuclear war
   cannot be won and must never be fought". No breakthrough on Ukraine, Iran,
   Taiwan, trade or AI.
   Sources: Reuters via BusinessWorld (https://bworldonline.com/world/2026/11/20/795454/trump-xi-and-putin-release-peace-declaration-from-unprecedented-summit/),
   The Times (https://www.thetimes.com/world/asia/article/trump-xi-putin-summit-shenzhen-latest-news-ddskr7pcx)
3. **KYIV — WAR: Russia strikes Kyiv overnight.** 110+ missiles (27 ballistic)
   + 400+ drones; Zelenskyy called it "the biggest this year". 3 Dnipro bridges
   hit; 8 killed, 28 injured; power/water outages. 79 cruise missiles shot down.
   Hours after Putin left Shenzhen.
   Sources: Reuters via SRN (https://srnnews.com/fire-broke-out-in-ukraines-kyiv-after-missile-strike-mayor-says/),
   CNN (https://www.cnn.com/2026/11/20/europe/russia-ukraine-putin-trump-intl-hnk),
   Military.com (https://www.military.com/ukraine-reports-russian-missile-blitz-after-putin-met-with-trump)
4. **RIYADH — MIDDLE EAST: Houthi missile hits Riyadh tower.** 19 Nov: missile
   struck PIF Tower — 80 stories, 1,263 ft, Riyadh's tallest, HQ of the Saudi
   sovereign wealth fund. Windows blown out across 7-8 floors; no injuries;
   financial district closed/evacuated. Second Houthi hit on a financial-district
   landmark in under 2 weeks (Aramco tower, 8 Nov).
   Sources: Reuters via SRN (https://srnnews.com/houthi-missile-threat-towards-riyadh-causes-damage-saudi-led-coalition-says/),
   WSJ (https://www.wsj.com/world/middle-east/houthi-attack-damages-saudi-capitals-tallest-tower-f4e15874)
5. **HORMUZ — TANKER ABLAZE.** 20 Nov: a tanker caught fire after a projectile
   strike 8 nautical miles off Oman's Khasab (UKMTO); no casualties. Iran claims
   mines hit two supertankers — unverified/disputed.
   Sources: Reuters (https://www.reuters.com/world/middle-east/fire-reported-tanker-after-projectile-strike-off-oman-ukmto-says-2026-11-20/),
   MarineLink (https://www.marinelink.com/news/tanker-fire-struck-projectile-near-strait-544511)
6. **POLAND — RUSSIAN MISSILES BREACH NATO AIRSPACE.** Overnight 20 Nov: a
   Kh-101 cruise missile + a probable second missile + a jet-powered drone
   crossed into Poland; the Kh-101 spent ~3 minutes over NATO and fell burning
   near Nowy Lipowiec. No injuries. Polish F-16s + Swedish Gripens scrambled,
   Patriots activated; no weapons fired. PM Tusk: "intentional provocation".
   NATO chief Rutte: "grave violation."
   Sources: AP via EuropeSays (https://www.europesays.com/poland/38911/),
   SOFREP (https://sofrep.com/news/russian-missiles-and-drone-breach-polish-airspace-as-nato-jets-scramble-and-hold-fire/)
7. **ANTALYA — COP31 DROPS FOSSIL FUELS.** 19 Nov draft strips ALL fossil-fuel
   phase-out language (Monday's draft had it). Instead: electrification
   ("35 by 35"), CCUS target 500M tons CO2/yr by 2035, and the $120B
   adaptation-finance target dropped. First COP to admit the 1.5C overshoot.
   ~200 countries; deadline Friday, talks likely into overtime.
   Sources: UN News (https://news.un.org/en/story/2026/11/1168839),
   Reuters (https://www.reuters.com/sustainability/climate-focus-cop31-draft-deal-strips-fossil-fuel-references-2026-11-20/)
8. **MARKETS — NIKKEI DIVES AS STOCKS SLIDE.** Nikkei -4.8%, Kospi -4.7%,
   S&P 500 -2%, Dow -2.19% to 49,097, Nasdaq -2.25%. SoftBank -16%.
   Anthropic +17% on a record $81B Nasdaq debut (closed $97 vs $83 offer;
   opened $111.50), then slid after hours.
   Sources: Reuters via TradingView (https://www.tradingview.com/news/reuters.com,2026:newsml_L2N471015:0-japan-s-nikkei-falls-more-than-4-after-anthropic-s-ipo-fails-to-restore-ai-confidence/),
   The Times (https://www.thetimes.com/business/companies-markets/article/anthropic-soars-2trn-record-ipo-djrbvrgkk)

## Files

- `entry.png` — the 1024x1024 front page (PNG, under 1 MiB)
- `draw.py` — the drawing script that produces `entry.png`
- `main.py` — entry program: copies `entry.png` to `/output/entry.png`
- `LICENSE` — MIT

## Verify

```sh
python3 draw.py                       # regenerate entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
