# Audit: were the questions taught first? Episodes 001 to 008

Critic: independent agent, 28 Nov 2026. Source: `daily-brief/episodes/00N/script.txt` (the spoken text), plus notes.md, GLOSSARY.md, INTERVIEW_BANK.md, CURRICULUM.md. Read only. Nothing in the repo was changed.

Rule checked: every quiz question, interview or "say it out loud" prompt, and every model answer should use only what was taught in the lesson of that episode or an earlier one.

## Summary

- Prompts checked: **54** (29 quiz questions incl. bonuses, 18 vocabulary-sprint words, 7 say-it-out-loud / interview / big-question prompts).
- **OK: 51. PARTLY: 3. NOT TAUGHT: 0.**
- Important finding about Ehsan's comment: **episode 008 has no question about projects or choosing.** The only project question is **episode 007, quiz question 3** (NPV, "is it a good project?"). Episodes 6, 7 and 8 were all released on Saturday 28 Nov, so this is very likely the one he meant. NPV *is* in the 007 lesson, but only as one dense, number-heavy paragraph. The decision rule gets one sentence, and the term "required rate" is never explained. **Choosing between two projects was never taught.** For a listener, "taught" in that sense is too thin, so it is rated PARTLY and has the most important correction below.
- Model answers using untaught words: "return" and "underlying assets" (ep 4, ep 5).
- Teasers: every "next episode" teaser was delivered. Four **long-range promises are now wrong** after curriculum v4 (week numbers for diversification, duration and active vs passive; inflation-linked bonds not in the curriculum).
- Calculation-heavy questions (Ehsan's second comment): 4 quiz questions in eps 6 to 8 test arithmetic rather than mechanism (listed below with mechanism-style replacements).
- INTERVIEW_BANK.md ep 6 model answer does not match the audio (reason 3 differs and was not taught).

## Per-question table

| Ep | Question (short) | Where taught | Verdict |
|---|---|---|---|
| 1 | Q1 What is an asset? Example | Ep 1: "An asset is anything that you own that has value, or that can make you money." | OK |
| 1 | Q2 What is an index? | Ep 1 markets: "An index is a score that tracks a group of companies, like a team average." | OK |
| 1 | Q3 Two of three jobs of an asset manager | Ep 1: "An asset manager does three things..." | OK |
| 1 | Q3b How are they paid? | Ep 1: "Usually through a fee... a small percentage of the money they manage" | OK |
| 2 | Say it out loud: what is a stock? | Ep 2 lesson (ownership, price + dividend, paid last); "bond" from ep 1 ("a loan you give to a government or a company") | OK |
| 2 | Q1 Using the bakery, what is a share? | Ep 2: "A share is a small piece of ownership in a company." | OK |
| 2 | Q2 Two ways to make money from a stock | Ep 2: price goes up; dividend | OK |
| 2 | Q3 Three jobs of an asset manager | Ep 1 | OK |
| 2 | Bonus: who gets paid first, shareholders or lenders? | Ep 2: "Shareholders are paid last. First the bakery pays... its lenders." | OK |
| 3 | Say it out loud: what is a bond? | Ep 3 lesson (loan, coupon, face value, maturity, credit risk, see-saw) | OK |
| 3 | Q1 Three words every bond has | Ep 3: "Face value, coupon, maturity." | OK |
| 3 | Q2 Rates up: price of your bond? | Ep 3: "when rates go up, the price of your existing bond goes down" | OK |
| 3 | Q3 Strong government or weaker company: who pays more, why? | Ep 3: "A higher rate is the price of higher risk." | OK |
| 3 | Bonus: two ways to make money from a stock | Ep 2 | OK |
| 4 | Say it out loud: what is an ETF? (model answer) | ETF, fee, market risk: ep 4. **"Return" and "underlying assets" never defined.** | PARTLY |
| 4 | Q1 What is a fund? | Ep 4: "A fund is a basket." | OK |
| 4 | Q2 Mutual fund vs ETF | Ep 4: "priced... once a day" / "trades on the stock exchange all day" | OK |
| 4 | Q3 Passive investing | Ep 4: "the fund simply copies an index" | OK |
| 4 | Q4 Volatility | Ep 4 markets segment: "Volatility is how much and how fast a price swings" (taught in the news part, not the lesson; acceptable) | OK |
| 4 | Bonus: rates up, bond price? | Ep 3 | OK |
| 5 | Sprint words 1 to 18 (asset, asset manager, asset allocation, risk, fee, index, share/stock, dividend, IPO, bond, face value, coupon, maturity, credit risk, fund, ETF, expense ratio, volatility) | All in eps 1 to 4 (IPO ep 2; credit risk ep 3; expense ratio ep 4) | OK x18 |
| 5 | Big question: what does an asset manager do, what do they invest in? | Eps 1 to 4. Model answer: "try to earn a **return**", again not defined | PARTLY (minor) |
| 6 | Interview: what is an interest rate, why does a manager care? | Ep 6 ("price of money over time"; safe rate as yardstick; real return) + ep 3 see-saw | OK (but see INTERVIEW_BANK mismatch) |
| 6 | Q1 1,000 at 5% compounded, after 2 years? | Ep 6: "Year two... fifty-two dollars and fifty cents" | OK (calculation-heavy) |
| 6 | Q2 Rule of 72 at 8% | Ep 6: "Divide seventy-two by the rate" | OK (light arithmetic) |
| 6 | Q3 6% return, 4% inflation: real return? | Ep 6: "the real return: roughly, the nominal return minus inflation". "Inflation" is only defined by context ("prices grow three percent"); fine for this listener | OK |
| 6 | Q4 What is a coupon? | Ep 3 | OK |
| 7 | Interview: one dollar in ten years, worth today? | Ep 7: "about sixty-one cents", discount rate = opportunity cost | OK |
| 7 | Q1 1,000 in 2 years at 5%: worth today? | Ep 7 PV formula | OK (calculation-heavy: dividing by 1.1025 in 6 seconds) |
| 7 | Q2 Discount rate up: PV up or down? | Ep 7: "the higher the discount rate, the lower the present value" | OK |
| 7 | **Q3 Project costs 1,000, PV of cash 1,050: NPV, good project?** | Ep 7, one paragraph only: "value in minus value out, all in today's money, is called the net present value. If it is positive, the project earns more than your required rate." Buried in a three-payment calculation. "Required rate" not defined (the lesson said "discount rate" and "opportunity cost"). **Choosing between projects not taught.** | **PARTLY** (the gap Ehsan reported) |
| 7 | Q4 Face value | Ep 3 | OK |
| 8 | Interview: value a never-ending stream; what can go wrong? | Ep 8: perpetuity, Gordon growth, "No company can grow faster than the whole economy forever", "checks how sensitive the answer is" | OK |
| 8 | Q1 Fixed 100 a year forever, investors want 4% | Ep 8: "payment divided by the rate" | OK (calculation-heavy) |
| 8 | Q2 Payments at start vs end: which is worth more? | Ep 8: annuity due, "every payment arrives one period earlier" | OK |
| 8 | Q3 200k at 6% monthly: first-month interest | Ep 8 mortgage: "three hundred thousand times four percent divided by twelve" | OK (calculation-heavy) |
| 8 | Q4 Name for 5.12% yearly rate | Ep 6: "effective annual rate" | OK |

## Teasers and promises

| From | Promise | Delivered? |
|---|---|---|
| Ep 1 | Next: what a stock is | Ep 2: yes |
| Ep 2 | Next: bonds; rate and price move opposite | Ep 3: yes |
| Ep 3 | Next: funds and ETFs | Ep 4: yes |
| Ep 4 | Next: Friday review and first big question | Ep 5: yes |
| Ep 5 | "On Monday... interest" | Ep 6 covers interest, but it came out **Saturday**, not Monday (schedule change, minor) |
| Ep 6 | Next: present value | Ep 7: yes |
| Ep 7 | Next: annuities, perpetuities, mortgage, consols | Ep 8: yes |
| Ep 8 | Next: returns, two methods (money vs time weighted) | Ep 9 not made yet; matches CURRICULUM W2 #4 |
| Ep 3 | "In week eight... duration" | **Wrong now**: duration is W17 (W8 is Economics I) |
| Ep 3, Ep 4 | Diversification "in week three" | **Wrong now**: W3 is Statistics; diversification is W5 #2 |
| Ep 4 | "In week nine, the evidence on whether active pays off" | **Wrong now**: W9 is Economics II; active vs passive is W26 (and W54 fees) |
| Ep 6 | "Inflation-linked bonds" in the bond weeks | **Not in CURRICULUM.md** (no inflation-linked bonds / TIPS lesson in W16 to W22) |
| Ep 6 | "Central banks get their own week" | Partly: it is one lesson (W8 #5), not a week. Minor |
| Ep 6 | Credit spread in the bond weeks | OK (W16 #7, W18) |
| Ep 7 | NPV again in corporate finance | OK (W12 #4) |
| Ep 8 | Gordon model in the equity weeks | OK (W24 #2) |

## Other finding: INTERVIEW_BANK.md does not match the audio (ep 6)

The audio's third reason is "it changes what clients really earn after inflation". The bank's third reason is "it sets how expensive borrowing is for companies, so it affects profits". The ep 6 lesson never taught that mechanism. Fix: align the bank with the audio, or teach the mechanism (correction 4).

## Calculation-heavy questions (Ehsan's second comment)

These are "taught", but they test mental arithmetic in a 6-second pause, not the mechanism. Suggested mechanism versions:

- Ep 6 Q1 (1,102.50). Better: "After two years of compounding, do you have a bit more or a bit less than 1,100, and why?" (A bit more, because the second year also earns on the first year's interest.)
- Ep 7 Q1 (about 907). Better: "Money promised in two years. Is it worth more or less today than the same money in ten years, and why?"
- Ep 8 Q1 (2,500). Better: "Investors suddenly want a higher return from a share that pays the same dividend forever. Does its price go up or down?" (Down.)
- Ep 8 Q3 (1,000 interest). Better: "In the first years of a mortgage, is most of your payment interest or repayment, and why does that change over time?"

## Suggested corrections (spoken style, for the next episode)

**1. NPV and choosing between projects (ep 7 Q3, Ehsan's report).**
"Net present value is a simple yes-or-no test. Bring all the money a project will pay you back to today's value, and compare it with what it costs today. If more comes back than goes in, it creates value. If less, it destroys value. When you must choose between two projects, take the one that adds more value in today's money, not the one with the bigger total payout. Money that arrives late shrinks the most, and the higher the rate, the harder it shrinks."
Add one line on the term: "The required rate is just the discount rate seen from the investor's side. It is what you could earn elsewhere for the same risk, so a project has to beat it."

**2. "Return" and "underlying assets" (ep 4 model answer, ep 5 model answer).**
"A return is simply what an investment earned for you, as a share of what you put in: the price change plus any income, like dividends or coupons. The underlying assets are the real stocks or bonds inside a fund. When they go up, the fund goes up, minus its fee." This fits well at the start of ep 9 (returns).

**3. Out-of-date week promises (eps 3 and 4).**
"A quick update to the plan. Earlier I said diversification would come in week three, duration in week eight, and the evidence on active funds in week nine. The course has been reorganised: diversification comes in the Risk and Return block, duration in the second bond block, and active versus passive in the equity portfolio block. Same topics, later slots." Also either add inflation-linked bonds to a bond week in CURRICULUM.md, or drop that promise.

**4. Rates and company profits (INTERVIEW_BANK ep 6), if kept.**
"When rates rise, companies pay more on their loans, so there is less profit left for shareholders. At the same time, future profits are discounted at a higher rate, so they are worth less today. Both push share prices the same way: down."

## Suggested process fix for the critic (CRITIC.md)

Add one check to every episode critic: "For each quiz, interview and say-it-out-loud prompt and each model answer, name the episode and line where every needed concept was taught. If a concept appears only inside a worked calculation, or in a single sentence, mark it PARTLY. Prefer questions about direction and mechanism (up or down, why) over exact numbers." This is cheap: one table per episode, using GLOSSARY.md (episode column) as the index.
