# CRITIC REPORT: Episode 6 (Sat 28 Nov 2026), round 1

Inputs: `episodes/006/script.txt`, `episodes/006/notes.md`, `market-news-lab/data/prices.csv` (as provided, freshly pulled from main), and `episodes/005/script.txt` for the correction claim only. All numbers recomputed with my own Python.

| # | Claim or line | Check and source | Result (PASS / FIX / FAIL) | Exact fix |
|---|---|---|---|---|
| 1 | L1 "episode six, Saturday, the twenty-eighth of November ... start of week two ... Quick recap of yesterday" | 28 Nov 2026 is a Saturday; ep 5 was Fri 27 Nov (ep 5 script line 1), so "yesterday" is right. | PASS | none |
| 2 | L5 data coverage: last full US stock close Wed 25; Europe, gold, oil Thu 26; Friday partial | prices.csv: SPX, US10Y last row 2026-11-25; DAX, SX5E, GOLD, BRENT, DXY last row 2026-11-26; only BTC, ETH, EURUSD, USDJPY on 2026-11-27. US Thanksgiving Thu 26 Nov 2026. | PASS | none |
| 3 | L7 S&P 500 "about seven thousand one hundred and eighty-three, down a quarter of a percent" (Wed 25) | SPX 2026-11-25 close 7,182.78, change -0.25%. Rounds to 7,183. | PASS | none |
| 4 | L7 ten year "four point eight five percent" (Wed 25) | US10Y 2026-11-25 = 4.848, rounds to 4.85. | PASS | none |
| 5 | L9 Thu 26: DAX and Euro Stoxx 50 "about two percent"; gold +3.5% to "about 3,658"; Brent -2.5% to "about 92" | DAX +2.08%, SX5E +2.04%, GOLD 3,658.10 +3.46%, BRENT 92.24 -2.51%. | PASS | none |
| 6 | L9 Fri 27: Bitcoin "about sixty-one thousand four hundred", "up almost one percent"; euro "about one point one dollars"; "only prices are crypto and currencies" | BTC 61,409.80 +0.87%; EURUSD 1.0979; Fri rows are BTC, ETH, EURUSD, USDJPY only. | PASS | none |
| 7 | L11 correction: ep 5 said gold "about 3,605" on Wednesday; now 3,536 | Ep 5 line 11: "gold bounced to about three thousand six hundred and five dollars ... and Brent ... on Wednesday". GOLD 2026-11-25 now 3,535.80, rounds to 3,536. Paraphrase is fair. | PASS | none |
| 8 | L13 ten year 5.15 on Fri 13 Nov to 4.85 on Wed 25, "about thirty basis points ... three tenths of a percentage point"; "two weeks" | US10Y 2026-11-13 = 5.154 (a Friday), 2026-11-25 = 4.848; difference 0.306 pt = 30.6 bp. 12 days, about two weeks. | PASS | none |
| 9 | L13 cause: "I did not find a published source for the reason, so I will not invent one" | No cause claimed for any move anywhere in the script. Rates down, bond prices up is the standard price-yield relation (CFA L1 Fixed Income; Fabozzi), not a cause claim. | PASS | none |
| 10 | L19 "The lender gives up money today and is paid for two things: waiting, and risk." | CFA L1 Quantitative Methods (Time Value of Money / interest rates): interest rate = real risk-free rate + **inflation premium** + default risk premium + liquidity premium + maturity premium. Bodie-Kane-Marcus ch. 5 (Fisher): nominal rate covers expected inflation. Leaving out inflation is a simplification that becomes wrong, and it clashes with this same episode's real-vs-nominal section. | FIX | Replace with: "The lender gives up money today and is paid for three things: waiting, expected inflation, and risk." |
| 11 | L19 "$1,000 at five percent, fifty dollars a year"; supply and demand; credit spread | 1000 x 0.05 = 50. Loanable funds view (BKM ch. 5). Credit spread definition correct (Fabozzi). | PASS | none |
| 12 | L21 savings account = lending to the bank; bank keeps the difference | Standard (net interest margin), simplified but not wrong. | PASS | none |
| 13 | L23 simple $150 in 3 yrs; year 2 interest $52.50; 3 yrs "about 1,158"; FV = PV(1+r)^n | 1000 x 0.05 x 3 = 150; 1050 x 0.05 = 52.50; 1000 x 1.05^3 = 1,157.63. Formula matches CFA L1 TVM. | PASS | none |
| 14 | L25 10 yrs "about 1,629"; 30 yrs "about 4,320"; simple 30 yrs 2,500 | 1000 x 1.05^10 = 1,628.89; 1000 x 1.05^30 = 4,321.94 (about 4,320 is acceptable rounding); 1000 + 30 x 50 = 2,500. | PASS | none |
| 15 | L27 rule of 72: 6% about 12 yrs, 9% about 8 yrs | 72/6 = 12 (exact ln2/ln1.06 = 11.90); 72/9 = 8 (exact 8.04). Labelled an approximation. | PASS | none |
| 16 | L29 5% monthly, effective "about five point one two percent" | (1 + 0.05/12)^12 - 1 = 5.116%, rounds to 5.12. | PASS | none |
| 17 | L29 "That is why loans and savings products quote an effective annual rate" | Too broad. US loans quote APR under the Truth in Lending Act (Fed Regulation Z), which is a stated nominal rate, not an effective rate; US savings quote APY (Regulation DD) which is effective; EU loans must show an effective APRC (Consumer Credit Directive). The script itself says three paragraphs later "Always convert to the effective rate before comparing", which only makes sense if quoted rates are often not effective. A beginner would wrongly trust any quoted loan rate as effective. | FIX | Replace with: "That is why many savings products, and in Europe loans, must also show an effective annual rate: it lets you compare like with like." |
| 18 | L31 continuous 5%, effective "about five point one three percent"; used in option pricing and risk models | e^0.05 - 1 = 5.127%; Hull (Options, Futures and Other Derivatives, ch. 4) uses continuous compounding. "Gains shrink after monthly": 5.116% vs 5.127%. | PASS | none |
| 19 | L33 "A bank advertises a loan at five percent, and another at four point nine percent compounded monthly. Which is cheaper? ... the second loan is actually a touch more expensive." | 4.9% monthly = (1 + 0.049/12)^12 - 1 = 5.012%, correct. But the first loan's compounding is not stated. If it is also monthly (common for loans), it is 5.116% effective and the second loan is cheaper, so the stated answer is not proven by the question as worded. The episode's own checklist (L41) says to ask "how often?". | FIX | Replace the first sentence with: "A bank advertises a loan at five percent a year, compounded once a year, and another bank offers four point nine percent compounded monthly." |
| 20 | L35 real return: 5% nominal, 3% inflation, about 2%; exact 1.05/1.03 - 1 "about one point nine four percent" | 1.05/1.03 - 1 = 1.942%. Fisher relation (BKM ch. 5; CFA L1). | PASS | none |
| 21 | L37 "A pension fund promises future payments in real terms." | Stated as true of all pension funds; it is not. Many defined-benefit plans promise nominal payments with no or capped inflation indexing (e.g. most US corporate DB plans); others are indexed. CFA L1 Portfolio Management (pension plan liabilities) treats indexing as plan-specific. | FIX | Replace with: "Many pension funds promise future payments that rise with inflation." |
| 22 | L37 4% bond with 5% inflation loses buying power; inflation-linked bonds | 1.04/1.05 - 1 = -0.95% real. Correct. | PASS | none |
| 23 | L39 safe government rate as yardstick, "almost no credit risk"; market sets long rates; Fed sets a short-term rate | Standard (CFA L1; Fed sets the federal funds target range). No current Fed level quoted. Simplified but not wrong. | PASS | none |
| 24 | L41 four checks (compounding, nominal/real, per year, risk-free comparison) | Sound. | PASS | none |
| 25 | L51 model answer: definition, three reasons, 5.15 to 4.85 in two weeks | Matches L13 and data (5.154, 4.848). | PASS | none |
| 26 | Quiz Q1 1,102.50; Q2 9 years; Q3 about 2%, exactly 1.92%; Q4 coupon | 1000 x 1.05^2 = 1,102.50; 72/8 = 9 (exact 9.006); 1.06/1.04 - 1 = 1.923%; coupon = yearly interest a bond pays (Fabozzi). | PASS | none |
| 27 | L77 "Next, right after this, in episode seven: present value." | Ep 7 is dated 2026-11-28, slot B, title "Present value, future value and discounting" (episodes/007/meta.json). Fits a same-day release after ep 6 (slot A). | PASS | none |
| 28 | L77 ending: "... Educational, not financial advice. See you in the next one." | Rule (CLAUDE.md, CRITIC.md 7): the episode must END with "Educational, not financial advice." Here a sentence follows it. | FIX | Replace the last two sentences with: "See you in the next one. Educational, not financial advice." |
| 29 | Rules: no buy advice; no personal data | No recommendation to buy or sell anything; no names or personal details. | PASS | none |
| 30 | Language and TTS | Numbers written as words; "S and P 500", "E T Fs" spell-outs fine; no typos found. | PASS | none |

## Not proven (objections that change nothing)
1. L11 "The data has since been revised": I cannot confirm from the given inputs that the 25 Nov gold row was revised (rather than ep 5 having read it wrong); git history was out of scope. The corrected number itself is right.
2. L5 "Friday was a short session": correct per the usual NYSE early close after Thanksgiving, but notes.md gives no source for it.
3. L7 "Remember that number, because it is today's lesson": the number is an example for the lesson, not the lesson itself. Style only.
4. L9 "Bitcoin closed at": crypto trades around the clock; "closed" means the data's daily close. Fine for a beginner.
5. L25 "In episode four you heard that a one percent yearly fee costs thousands over twenty years": ep 4 was not in my inputs, so not checked.
6. L39 "the return you can get with almost no credit risk": a ten year bond still has interest-rate and inflation risk, and is only "safe" in nominal terms if held to maturity. Many textbooks use a T-bill as the risk-free rate for short horizons. Acceptable simplification.
7. Q4 "The yearly interest a bond pays": many bonds (e.g. US Treasuries) pay the coupon in two halves a year; the annual figure is still the coupon. Fine.
8. Ep 5 told listeners "On Monday, we start with interest"; the move to Saturday is not mentioned. Not an error in ep 6.
9. Strongest counter-view: the script's supply-and-demand (loanable funds, Fisher time preference) view of interest is mainstream; Keynes' liquidity-preference view (interest as the reward for giving up liquidity) and the modern view that central banks largely set short rates are the main alternatives. The script nods to the central bank at L39, so it is fair enough for a beginner.
10. "As of" wording: the script dates every market number by day instead of saying "as of". Clear enough; not marked.

## Round 2 (re-check of changed lines only)
| # | Changed line | Check | Result |
|---|---|---|---|
| 10 | L19 "...paid for three things: waiting, expected inflation, and risk." | Matches CFA L1 rate breakdown and Fisher (BKM ch. 5). Reads naturally before "The interest rate is that price..."; "inflation" is plain English and is taught properly at L35. | PASS |
| 17 | L29 "That is why many savings products, and in Europe loans, must also show an effective annual rate: it lets you compare like with like." | True (US APY under Reg DD; EU APRC under the Consumer Credit Directive). No longer contradicts L33 "Always convert...". Grammar fine for TTS. | PASS |
| 19 | L33 "A bank advertises a loan at five percent a year, compounded once a year, and another bank offers four point nine percent compounded monthly." | First loan now 5.000% effective; second (1+0.049/12)^12-1 = 5.012%. "The second loan is actually a touch more expensive" now follows. | PASS |
| 21 | L37 "Many pension funds promise future payments that rise with inflation." | True as a "many" claim; fits the next sentence about losing buying power. | PASS |
| 28 | L77 "...See you in the next one. Educational, not financial advice." | File's final text is "Educational, not financial advice." followed by a newline. Rule met. | PASS |

All 5 fixes were applied verbatim and fit the sentences around them. No new issues.

OVERALL: PASS
