# CRITIC REPORT: Episode 7, Present value, future value and discounting (Sat 28 Nov 2026, slot B)

Critic: fresh agent, did not write the script. Inputs: script.txt, notes.md, market-news-lab/data/prices.csv (main, as read 27 Nov 2026), GLOSSARY.md, episode 6 script (to check back-references only).
All numbers recomputed with my own Python (`1000*1.05**10`, `1/1.05**10`, `1000/1.05154**10`, NPV sums, `2**0.1-1`, `1000*exp(-0.5)`, `100/1.014**100`, etc.). Weekdays checked with `datetime`: 13 Nov 2026 = Friday, 25 Nov = Wednesday, 28 Nov = Saturday.

| # | Claim or line | Check and source | Result (PASS / FIX / FAIL) | Exact fix |
|---|---|---|---|---|
| 1 | "episode seven, Saturday, the twenty-eighth of November" | Calendar: 28 Nov 2026 is a Saturday; meta.json date 2026-11-28, slot B | PASS | |
| 2 | Recap: 1,000 at 5% becomes "about one thousand six hundred and twenty-nine" after 10 years | 1000*1.05^10 = 1,628.89 -> 1,629; matches ep 6 | PASS | |
| 3 | Time value of money: "a dollar today is worth more than a dollar tomorrow"; reasons: earn interest, consume now, uncertainty | CFA L1 Quant, Time Value of Money; BKM Investments ch. on interest rates | PASS | |
| 4 | FV = PV x (1+r)^n; PV = FV / (1+r)^n; "discounting", "discount rate" | CFA L1 Quant (TVM): FV_N = PV(1+r)^N, PV = FV_N(1+r)^-N | PASS | |
| 5 | $1 in 10 yrs at 5% "about sixty-one cents"; 0.61 grows back to "about one dollar"; discount factor "about zero point six one" | 1/1.05^10 = 0.6139; 0.61*1.05^10 = 0.994 | PASS | |
| 6 | Discount factor: further away, smaller factor | 1/(1+r)^n falls with n for r>0 | PASS | |
| 7 | Discount rate = opportunity cost; layers: real rate + expected inflation (~ safe government rate) + risk premium | CFA L1 Quant: r = real risk-free rate + inflation premium + default + liquidity + maturity premiums; rates read as required return, discount rate or opportunity cost. Script's 3-layer version is a labelled simplification ("roughly") | PASS | |
| 8 | $1,000 in 30 yrs: "about two hundred and thirty-one" at 5%, "about one hundred and thirty-one" at 7%; drop "more than forty percent" | 231.38; 131.37; -43.2% | PASS | |
| 9 | Bond price = PV of promised payments; rates up, price down (see-saw ep 3) | CFA L1 Fixed Income, bond pricing with a market discount rate; Fabozzi | PASS | |
| 10 | US10Y "Friday, the thirteenth of November ... five point one five percent" | prices.csv 2026-11-13,US10Y,5.154 -> 5.15 | PASS | |
| 11 | US10Y "Wednesday, the twenty-fifth ... four point eight five percent" | prices.csv 2026-11-25,US10Y,4.848 -> 4.85 (latest US10Y row in file) | PASS | |
| 12 | Zero-coupon prices "about six hundred and five" and "about six hundred and twenty-three" | 1000/1.05154^10 = 604.98; 1000/1.04848^10 = 622.87 (with rounded rates: 605.21 / 622.75, same rounding) | PASS | |
| 13 | "rate fell by about thirty basis points, ... price rose by about three percent" | 5.154-4.848 = 0.306 pts = 30.6 bp; 622.87/604.98-1 = +2.96% | PASS | |
| 14 | Zero-coupon bond definition; "use the ten year ... rate ... compounded once a year" as simplification, flagged | CFA L1 Fixed Income (zero-coupon = single payment at maturity); simplification is stated in script and notes (par yield used as zero rate, 12 days ignored) | PASS | |
| 15 | No "why the market moved" claim | Script gives no cause for the 10y move; ep 6 already said no published source was found | PASS | |
| 16 | Prize: 1.5m in 10 yrs = "about nine hundred and twenty-one thousand" at 5%; "about one million and thirteen thousand" at 4% | 920,870; 1,013,346 | PASS | |
| 17 | "Real lotteries in America offer ... a lump sum today, or yearly payments over many years" | Powerball / Mega Millions game rules: cash option or annuity of 30 payments over 29 years (cited in notes, tier 1-type official issuer rules) | PASS | |
| 18 | Project 400 x 3 at 8%: PV "about one thousand and thirty-one", NPV "about thirty-one"; at 12% "about minus thirty-nine" | 1,030.84; +30.84; -39.27 | PASS | |
| 19 | NPV definition; "If it is positive, the project earns more than your required rate" | CFA L1 Corporate Issuers, capital investment: NPV>0 <=> IRR > required rate (conventional cash flows) | PASS | |
| 20 | 1,000 -> 2,000 in 10 yrs: "about seven point one eight percent"; rule of 72: 72/10 = 7.2 | 2^(1/10)-1 = 7.177%; 7.2 | PASS | |
| 21 | Continuous: "about six hundred and seven" vs "six hundred and fourteen" yearly | 1000*e^-0.5 = 606.53; 1000/1.05^10 = 613.91 | PASS | |
| 22 | Stern Review 2006, for the British government, discount rate "around one point four percent", finds early action worth it | Stern Review (HM Treasury, published 30 Oct 2006): pure time preference 0.1% + elasticity 1 x growth ~1.3% = ~1.4%; conclusion "benefits of strong, early action far outweigh the costs". Nordhaus (2007, JEL 45(3)) himself characterises Stern's rate as ~1.4% | PASS | |
| 23 | "William Nordhaus argued that the rate should be clearly higher" | Nordhaus (2007) JEL review: criticises near-zero time preference, prefers rates consistent with market returns (roughly 4 to 6% real in DICE) | PASS | |
| 24 | $100 in 100 yrs: "about twenty-five dollars" at 1.4%; "about one dollar and twenty cents" at 4.5% | 24.90; 1.226 -> "about one dollar twenty" OK | PASS | |
| 25 | Counter-view fairness (discount rate is a judgment; show several rates) | Fair; names the best-known dispute (Stern vs Nordhaus) and does not take a side | PASS | |
| 26 | Interview model answer | Consistent with lesson; 61 cents at 5% matches #5 | PASS | |
| 27 | Quiz 1: 1,000 in 2 yrs at 5% "about nine hundred and seven"; Quiz 3: NPV fifty; Quiz 4: face value = amount paid back at the end | 907.03; 1050-1000 = 50; GLOSSARY ep 3 "Face value" | PASS | |
| 28 | Sum-up: "every price in finance, a bond, a stock, a project, is a present value of future cash" | Over-reach that becomes wrong: CFA L1 Equity distinguishes intrinsic value from market price (price can differ from value); assets with no cash flows (gold, bitcoin, which this podcast reports on daily) are not PV of cash; and the cash is *expected*, not certain. BKM: intrinsic value = PV of expected cash flows | FIX | Replace "And every price in finance, a bond, a stock, a project, is a present value of future cash." with "And the value of a bond, a stock or a project is the present value of the cash it is expected to pay." |
| 29 | Teaser: payment "forever, like a few very old British government bonds" | Present tense implies such bonds still exist. HM Treasury redeemed the 4% Consols (Feb 2015) and all remaining undated gilts, incl. 3.5% War Loan and 2.5% Consols, during 2015 (UK DMO). None are outstanding as of Nov 2026 | FIX | Replace "or forever, like a few very old British government bonds." with "or forever, like the old British government bonds called consols, which paid interest with no end date until they were repaid in 2015." |
| 30 | Terms used before taught | Checked against GLOSSARY: bond, face value, see-saw (ep 3), basis point, compounding, rule of 72, continuous compounding, safe rate (ep 6). New terms are all defined when first used (present value, discount rate, discount factor, opportunity cost, risk premium, zero-coupon bond, NPV) | PASS | |
| 31 | Language / TTS | Numbers written as words; no digits, symbols or abbreviations the voice would misread; grammar fine | PASS | |
| 32 | Rules: no buy advice; ends with "Educational, not financial advice."; no personal data | "Educational, not financial advice." present in closing; no security recommended; no personal data | PASS | |

## Not proven objections (they change nothing)
- "the number e" is used without saying what it is (about two point seven one eight). Ep 6 taught continuous compounding but never named e. Listener has a Master of Finance, so likely fine; a short "the number e, about two point seven two" would help a true beginner.
- "Take the million now." is phrased as a command; it is clearly a worked example under a given rate, not advice, but "the million now is worth more" would be softer.
- The 4.5% illustration follows directly after Nordhaus; a listener may think 4.5% is Nordhaus's number. Notes say it is an illustration only. It is in his range, so not wrong, but "for example four and a half percent" would make the status explicit.
- Risk premium described only as "the chance you will not be paid in full" (default). CFA also lists liquidity and maturity premiums, and for stocks the premium is for uncertainty of returns, not only non-payment. Acceptable for a three-layer first pass.
- "real rate + expected inflation = roughly the safe government rate": strictly that is the short risk-free rate; a ten-year government rate also carries a maturity (term) premium. "Roughly" covers it.
- "Present value is only as good as the discount rate you choose": equally only as good as the cash-flow forecast; could add "and the cash flows you expect".
- "you can expect it early in any finance interview": "any" is an overclaim; "many" is safer.
- Other counter-views on climate discounting (Weitzman's fat tails / declining discount rates, UK Green Book declining schedule) are not mentioned; not required for fairness here.
- NPV "earns more than your required rate" holds for conventional cash flows (one outflow then inflows), which is the example used.

## Round 2 (re-check of changed lines only)
Old text checked gone: "every price in finance", "a few very old", "Take the million now" are no longer in script.txt.

| # | Changed line | Check | Result | Exact fix |
|---|---|---|---|---|
| R2-1 | Sum-up: "And the value of a bond, a stock or a project is the present value of the cash it is expected to pay." | Verbatim row 28 fix; matches BKM / CFA intrinsic value; fits the sum-up flow | PASS | |
| R2-2 | Teaser: "...or forever, like the old British government bonds called consols, which paid interest with no end date until they were repaid in 2015." | Verbatim row 29 fix; UK DMO: last undated gilts redeemed 2015. "2015" as digits is read as a year by edge-tts ("twenty fifteen"), same as "In 2006" earlier in the script | PASS | |
| R2-3 | "...at four and a half percent, a rate I chose just to show the effect." | Makes clear 4.5% is not Nordhaus's figure; number unchanged (1.23); grammar fine | PASS | |
| R2-5 | Last line now ends "...See you in the next one. Educational, not financial advice." | Disclaimer appears once and is now the final sentence of the script, per the rule; nothing follows it | PASS | |
| R2-4 | "So the million today is worth more." | Correct: 1,000,000 > 920,870 at 5%; no longer a command; still contrasts with "Now the later payment wins." | PASS | |

OVERALL: PASS
