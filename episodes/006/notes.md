# Episode 6: sources and checks (made Fri 27 Nov 2026; moved to Sat 28 Nov, slot A)
Data: market-news-lab/data/prices.csv, main re-fetched Fri 27 Nov 22:11 UTC (latest commit 298b2d7 'Update prices for 2026-11-27'); every number below re-checked against it, none changed. Data ends: US stocks/US10Y/EEM/NDX at Wed 25 Nov (Thu 26 US holiday; Fri 27 not in data); Europe, gold, Brent, DXY at Thu 26; BTC, ETH, EURUSD, USDJPY at Fri 27. Nothing after is guessed. Episode date Sat 28 Nov: markets closed; Sat 28 crypto prices not in data and not used. Script says which close is used per market.
- SPX Wed 25: 7,182.78, -0.25% ("about seven thousand one hundred eighty-three").
- US10Y Wed 25: 4.848 (spoken 4.85); Fri 13 Nov: 5.154. Fall = 5.154-4.848 = 0.306 pts = ~30 bp ("three tenths of a point").
- Thu 26: DAX 25,215.52 +2.08%; SX5E 6,014.74 +2.04% ("about two percent"); GOLD 3,658.10 +3.46%; BRENT 92.24 -2.51%.
- Fri 27: BTC 61,409.80 +0.87%; EURUSD 1.0979 ("about 1.1").
- CORRECTION: ep 5 said gold Wed 25 = 3,605.20. Data now: 3,535.80 (-0.73%). Revised after ep 5 was made; ep 5 not re-rendered (per rules), corrected in ep 6 audio.
- No published source for the rate fall: audio says price data tells what, not why. "Rates down -> existing bond prices up" is the see-saw rule, not a measured bond price.
Lesson rewritten 27 Nov (faster pace, curriculum v4 W2 #1: interest, compounding, real returns). Standard concepts (CFA L1 Quant "Time value of money"; Bodie-Kane-Marcus ch. 5), recomputed with Python:
- $1,000 at 5% simple: $50/yr, $150 in 3 yrs. Compound: 1000*1.05^2 = 1,102.50; ^3 = 1,157.63 ("about 1,158"); ^10 = 1,628.89 ("about 1,629"); ^30 = 4,321.94 ("about 4,320"). Simple 30 yrs: 1,000 + 30*50 = 2,500.
- Rule of 72: 72/6 = 12, 72/9 = 8, 72/8 = 9 (approximation; exact doubling at 8% = ln2/ln1.08 = 9.006 yrs).
- Effective annual rate: 5% monthly = (1+0.05/12)^12-1 = 5.116% ("about 5.12"); 4.9% monthly = 5.012% ("about 5.01"); continuous 5% = e^0.05-1 = 5.127% ("about 5.13").
- Real return: 1.05/1.03-1 = 1.942% ("about 1.94"); quiz 1.06/1.04-1 = 1.923% ("1.92").
- Fed sets a short-term policy rate (standard fact, no current level quoted). Fee-as-compounding link: ep 4 example. Credit spread named, taught later (W18).
Terms repeated in quiz: coupon (ep 3).
- Critic round 1 (27 Nov): 5 FIX applied with the critic's exact text (inflation in what interest pays for; EAR disclosure wording; loan example compounding stated; pension funds 'many'; ending order). Gold revision: ep 5 notes recorded 3,605.20 from the data at the time (see ep 6 note above).
