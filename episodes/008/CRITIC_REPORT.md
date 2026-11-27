# CRITIC REPORT: Episode 8, "Annuities and perpetuities" (Sat 28 Nov 2026, slot C)
Critic: fresh agent, inputs script.txt, notes.md only (no market numbers in this episode, so prices.csv not needed). Numbers recomputed with my own Python. Sources: CFA Level I Quantitative Methods, "Time Value of Money" (tier 1); Bodie, Kane, Marcus, Investments; Damodaran, Investment Valuation (tier 2); UK Debt Management Office / HM Treasury (tier 1) for consols.

| # | Claim or line | Check and source | Result (PASS / FIX / FAIL) | Exact fix |
|---|---|---|---|---|
| 1 | Recap: "one dollar in ten years is worth about sixty-one cents today at five percent" | 1/1.05^10 = 0.6139 -> "about sixty-one cents" | PASS | |
| 2 | Recap: discount rate = opportunity cost, safe rate plus risk premium; higher rate, lower value | Matches ep 7 / GLOSSARY rows 41-44; CFA L1 TVM | PASS | |
| 3 | Annuity = equal payments, equal intervals, fixed number of periods | CFA L1: annuity is a finite set of level sequential cash flows. Matches GLOSSARY row 47 | PASS | |
| 4 | Perpetuity = annuity that never ends; PV = payment / rate; 50/0.05 = 1,000 | CFA L1 (PV = A/r, first payment one period from now). Computed 1,000.00 | PASS | |
| 5 | "Put one thousand dollars in an account at five percent ... pays fifty dollars a year forever" | Correct intuition (BKM) | PASS | |
| 6 | Consols: about 260 years, first issued in the 1750s, no repayment date, last repaid in 2015 | Consolidated 3% Annuities created 1751-52; HM Treasury/DMO redeemed all remaining undated gilts (4% Consols Feb 2015, 3.5% War Loan Mar 2015, 2.5% Consols etc. Jul 2015). 1751 to 2015 = 264 years. "No date to pay back" is right (they were callable at the government's option, which is how they were repaid) | PASS | |
| 7 | Preferred shares pay a fixed dividend with no end date ("certain" preferred shares) | CFA L1 Equity: perpetual (non-redeemable) preferred stock valued as a perpetuity. "Certain" correctly hedges that many preferreds are redeemable | PASS | |
| 8 | Gordon growth: PV = next year's payment / (rate - growth); 4/(0.08-0.03) = 80 | CFA L1 Equity Valuation (Gordon growth DDM, V0 = D1/(r-g)); computed 80.00. Uses D1, correctly said "next year's" | PASS | |
| 9 | Named after the economist Myron Gordon | Gordon (1959, 1962), Gordon and Shapiro (1956); standard attribution in BKM and CFA | PASS | |
| 10 | Growth 3% -> 7%: gap 5 points -> 1, value 80 -> 400 | 4/0.01 = 400.00 | PASS | |
| 11 | Formula breaks if growth equal to or above discount rate; no company can outgrow the economy forever | CFA L1 (requires r > g); Damodaran, Investment Valuation, terminal value chapter (stable growth rate cannot exceed the economy's growth rate) | PASS | |
| 12 | Ordinary annuity PV formula (payment x (1 - 1/(1+r)^N) / r), payments at end of period | CFA L1 TVM | PASS | |
| 13 | "it is a perpetuity that starts today, minus a perpetuity that starts after the last payment" | The correct decomposition is a perpetuity whose first payment is at the end of period 1, minus one whose first payment is at period N+1. Six paragraphs later the script uses "starting today" to mean first payment today (the annuity due). So a listener who uses the script's own meaning gets a perpetuity due (first payment at time 0), which gives the wrong value (it would value the annuity due, not the ordinary annuity). This is a timing error in the very lesson that teaches "start or end of the period?" | FIX | Replace "The idea is simple: it is a perpetuity that starts today, minus a perpetuity that starts after the last payment." with "The idea is simple: it is a perpetuity that pays from the end of the first period, minus a perpetuity that pays from the period after the last payment." |
| 14 | Spreadsheet functions PV and PMT | Exist in Excel and Google Sheets | PASS | |
| 15 | 10,000 x 10 years at 5% = "about seventy-seven thousand two hundred" | 77,217.35 -> 77,200 | PASS | |
| 16 | Annuity due = ordinary x (1 + r); "about eighty-one thousand one hundred" | CFA L1 TVM; 81,078.22 -> 81,100 | PASS | |
| 17 | Mortgage 300,000, 25 yrs, 4%/12, 300 payments: "about one thousand five hundred and eighty-four" a month | PMT = 1,583.51 -> 1,584 | PASS | |
| 18 | Total "about four hundred and seventy-five thousand"; interest "about one hundred and seventy-five thousand" | 475,053.16; 175,053.16 | PASS | |
| 19 | First-month interest exactly 1,000; principal "about five hundred and eighty-four" | 300,000 x 0.04/12 = 1,000.00; 583.51 | PASS | |
| 20 | Balance after ten years "about two hundred and fourteen thousand" | Simulated 120 payments: 214,078.19 | PASS | |
| 21 | Amortization / amortization schedule definitions | Standard (Fabozzi, BKM) | PASS | |
| 22 | At 6%: "about one thousand nine hundred and thirty-three" a month; interest "about two hundred and eighty thousand"; "about sixty percent more interest" | 1,932.90; 279,871.26; 279,871/175,053 = 1.599 | PASS | |
| 23 | Saving 500/month, 30 yrs, 5%/12: paid in 180,000, end "about four hundred and sixteen thousand", more than half is compounding | FV (end-of-month payments) = 416,129.32; growth share 56.7% | PASS | |
| 24 | Terminal value "often more than half of the total value" | Damodaran, Investment Valuation (terminal value typically the majority of DCF value); hedged with "often" | PASS | |
| 25 | Pension funds, bond coupons, insurers' annuities | Standard (Ang, Asset Management; BKM) | PASS | |
| 26 | Quiz 1: 100/0.04 = 2,500 | 2,500.00 | PASS | |
| 27 | Quiz 2: annuity due worth more | Correct for r > 0 | PASS | |
| 28 | Quiz 3: 200,000 x 6%/12 = 1,000 | 1,000.00 | PASS | |
| 29 | Quiz 4: 5% monthly = "about five point one two percent", effective annual rate, "from episode six" | (1+0.05/12)^12 - 1 = 5.116%; ep 6 script line 29 teaches it | PASS | |
| 30 | Causes of market moves | None claimed; the rates line ("a move in rates ... changes what families can afford") is a general mechanism, not a cause of a specific move | PASS | |
| 31 | Terms used before taught | dividend (ep 2), coupon (ep 3), discount rate, opportunity cost, risk premium (ep 7), effective annual rate (ep 6); new terms each get a plain definition when introduced | PASS | |
| 32 | Language and TTS | Numbers written as words; "P V", "P M T" spelled out; "2015" in digits but ep 7 already uses digit years ("2006"), edge-tts reads it as a year. No typos or grammar errors found | PASS | |
| 33 | Rules: no buy advice; ends with "Educational, not financial advice."; no personal data | No product or security recommended; closing line present (followed only by the sign-off "See you in the next one."); no personal data | PASS | |

## Not proven (objections that change nothing)
- Life pensions and insurer "annuities" usually pay until death, so the number of payments is not fixed; strictly they are life annuities (valued with mortality probabilities), which sits a little uneasily with the "fixed number of periods" definition given a few lines earlier. Acceptable everyday usage; the writer could add "for life" later in a pensions lesson.
- "A small change in a guess about forever": three to seven percent growth is a big change in a growth assumption; the point (value is hypersensitive to r minus g) stands. Style only.
- Strongest counter-view on the Gordon model: Miller and Modigliani's dividend irrelevance and the fact that many companies pay no dividends; practitioners also use exit multiples instead of a perpetuity for terminal value (Damodaran notes both). The script calls Gordon "one of the first" tools, not the only one, so it is fair. Some (Damodaran) go further and cap stable growth at the risk-free rate; the script's "below the growth of the economy" is the standard, softer version.
- The dividend discount idea predates Gordon (John Burr Williams, 1938). Naming the model after Gordon is still the standard textbook attribution.
- "More than half of the final amount is compounding": strictly it is interest earned (including interest on interest). Loose but not wrong for a beginner.
- Rate moves change what families can afford mainly for new or variable-rate borrowers; existing fixed-rate borrowers are not affected until they refinance. Not needed at this level.
- Mortgage convention: some euro-area markets also quote an effective annual rate; the example uses the nominal rate divided by twelve, which is the standard way the monthly payment is computed, so it is correct.
- Spreadsheet PV returns a negative number by sign convention; a beginner may be confused when trying it. A later tip could mention this.
- "Consols" may be read by the TTS like "consoles"; that is close to the real pronunciation.

## Round 2 (re-check of the changed line only)
| # | Claim or line | Check and source | Result (PASS / FIX / FAIL) | Exact fix |
|---|---|---|---|---|
| 13 | "The idea is simple: it is a perpetuity that pays from the end of the first period, minus a perpetuity that pays from the period after the last payment." | Applied verbatim (script line 19; "starts today" no longer appears). Matches CFA L1: PV = A/r - (A/r)/(1+r)^N, with first payments at t=1 and t=N+1. Fits the sentences around it ("end of the period" formula before, "Your calculator or spreadsheet does the rest" after). The grammar is fine and the voice will read it correctly | PASS | |

Note: confirmed the last line now ends "See you in the next one. Educational, not financial advice.", so the disclaimer is the final words, it appears only once, and the rule is met (PASS).

OVERALL: PASS
