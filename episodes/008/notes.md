# Episode 8: sources and checks (made Fri 27 Nov 2026 for Sat 28 Nov, slot C)
Slot C: no markets segment (it is in ep 6, slot A). Saturday follows the weekday 3-slot plan (Ehsan, 27 Nov); C = new lesson, continuing curriculum order as listed in STATUS.md "Next episodes".
Lesson: curriculum v4 W2 #3, annuities and perpetuities (mortgage example). Concepts: CFA Level I Quantitative Methods, "Time value of money" (ordinary annuity, annuity due, perpetuity, growing perpetuity) (tier 1); Bodie, Kane, Marcus, Investments; Damodaran, Investment Valuation (terminal value, growth below economy growth) (tier 2). Fund-manager repo (tier 4): docs/curriculum.md day 5 "Time value of money" and day 27 "dividend discount model" (Gordon model link) consulted; no separate interview question there for annuities, so the interview question is the writer's (standard valuation question).

## Numbers (recomputed with Python)
- Perpetuity 50/0.05 = 1,000. Quiz: 100/0.04 = 2,500.
- Gordon growth: 4/(0.08-0.03) = 80; 4/(0.08-0.07) = 400.
- Ordinary annuity 10,000 x 10 yrs at 5%: 10,000*(1-1.05^-10)/0.05 = 77,217 ("about 77,200"); annuity due x1.05 = 81,078 ("about 81,100").
- Mortgage (example rate, not a market rate; script says so): 300,000, 4%/12, 300 months: payment = 1,583.51 ("about 1,584"); total 475,053 ("about 475 thousand"); interest 175,053 ("about 175 thousand"); first-month interest 300,000*0.04/12 = 1,000.00; first principal 583.51 ("about 584"); balance after 120 payments 214,078 ("about 214 thousand").
- Same at 6%: payment 1,932.90 ("about 1,933"); total interest 279,871 ("about 280 thousand"); 279,871/175,053 = 1.60 ("about sixty percent more").
- Saving 500/month, 360 months, 5%/12: FV = 416,129 ("about 416 thousand"); paid in 180,000; growth share (416,129-180,000)/416,129 = 57% ("more than half").
- Quiz: 200,000*0.06/12 = 1,000. EAR 5% monthly = 5.116% (ep 6).

## Claims
- Consols: British government undated bonds; consolidated annuities first issued 1751; the government redeemed the remaining undated gilts (4% Consols, 3.5% War Loan and others) in 2015 (HM Treasury announcements Oct 2014 to 2015; UK Debt Management Office). 1751 to 2015 = 264 yrs ("about two hundred and sixty").
- Perpetual preferred shares: fixed dividend, no maturity (CFA L1 Equity / Fixed Income readings).
- Gordon growth model named after Myron J. Gordon (Gordon 1959/1962) (tier 2 textbooks).
- Growth cannot exceed the economy's growth forever; terminal value often over half of DCF value: Damodaran, Investment Valuation, terminal value chapter (tier 2). Stated as "often", not as a fixed share.
- Spreadsheet functions PV and PMT exist in Excel and Google Sheets.
Terms repeated in quiz: effective annual rate (ep 6).
New terms: annuity, perpetuity, ordinary annuity, annuity due, growing perpetuity, Gordon growth model, amortization, amortization schedule, terminal value, preferred share.
- Critic round 1 (27 Nov): 1 FIX (row 13, perpetuity-minus-perpetuity timing wording) applied with the critic's exact text.
