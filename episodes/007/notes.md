# Episode 7: sources and checks (made Fri 27 Nov 2026 for Sat 28 Nov, slot B)
Slot B: no markets segment (it is in ep 6, slot A); script links to ep 6 instead.
Lesson: curriculum v4 W2 #2, present value, future value, discounting. Concepts: CFA Level I Quantitative Methods, "Time value of money" (tier 1); Bodie, Kane, Marcus, Investments (tier 2); Damodaran, Investment Valuation, ch. on discounting (tier 2). Fund-manager repo (tier 4): docs/curriculum.md day 5 "Time value of money", interview question "What is $1 received in 10 years worth today?" used as the interview corner.

## Numbers (recomputed with Python)
- 1,000 at 5% for 10 yrs = 1,628.89 ("about 1,629"), from ep 6.
- $1 in 10 yrs at 5%: 1/1.05^10 = 0.6139 ("about 61 cents", discount factor "about 0.61"); 0.6139*1.05^10 = 1.00.
- $1,000 in 30 yrs: at 5% = 231.38 ("about 231"); at 7% = 131.37 ("about 131"); 131.37/231.38-1 = -43.2% ("more than forty percent").
- Zero-coupon example (simplified: annual compounding, US10Y par yield used as a zero rate, 12 days of time ignored; script says so): US10Y from prices.csv (main, re-fetched 27 Nov 22:11 UTC): Fri 13 Nov 5.154 -> 1000/1.05154^10 = 604.98 ("about 605"); Wed 25 Nov 4.848 -> 1000/1.04848^10 = 622.87 ("about 623"); change +2.96% ("about three percent"); 5.154-4.848 = 0.306 pts ("about thirty basis points").
- Prize: 1.5m in 10 yrs at 5% = 920,870 ("about 921 thousand"); at 4% = 1,013,346 ("about one million and thirteen thousand").
- Lotteries offering lump sum vs annual payments: US Powerball and Mega Millions both offer a cash option or an annuity paid over 29 years (30 payments) (powerball.com, megamillions.com, game rules; stated generally in script, no figures).
- Project: -1,000 then 400 x 3 at 8%: PV inflows 1,030.84, NPV = +30.84 ("about 31"); at 12%: NPV = -39.27 ("about minus 39").
- Rate from 1,000 -> 2,000 in 10 yrs: 2^(1/10)-1 = 7.177% ("about 7.18"); rule of 72: 72/10 = 7.2.
- Continuous: 1000*e^(-0.05*10) = 606.53 ("about 607"); annual 613.91 ("614").
- Stern Review (HM Treasury, 30 Oct 2006): discount rate approx 1.4% (pure time preference 0.1% + growth 1.3% x elasticity 1). Source: Stern Review, ch. 2 and annex; Nordhaus, W. (2007) "A Review of the Stern Review on the Economics of Climate Change", Journal of Economic Literature 45(3), criticises the low rate and argues for a higher one. 4.5% in script is an illustration only, not attributed to Nordhaus.
- $100 in 100 yrs: at 1.4% = 24.90 ("about 25"); at 4.5% = 1.23 ("about one dollar twenty").
- Quiz: 1000/1.05^2 = 907.03 ("about 907"); NPV 1,050-1,000 = 50.
Terms repeated in quiz: face value (ep 3).
New terms: time value of money, future value, present value, discounting, discount rate, discount factor, opportunity cost, risk premium, zero-coupon bond, net present value.
- Critic round 1 (27 Nov): 2 FIX applied with the critic's exact text (row 28 'value ... expected to pay'; row 29 consols repaid 2015). Also from 'not proven': 4.5% marked as the writer's illustrative rate; 'Take the million now' reworded as a comparison.
