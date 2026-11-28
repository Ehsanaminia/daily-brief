# Daily Brief: status (28 Nov 2026)

| Ep | Date | Topic | Length | State |
|---|---|---|---|---|
| 001 | Sat 21 Nov (pilot) | What is an asset manager? | 5.9 min | Built (re-ordered, +4% speed; gold/oil corrected 26 Nov). Its Instagram numbers (32 followers) are old: 49 on 22 Nov. Ehsan listened to the first version and liked the voice |
| 002 | Tue 24 Nov | What is a stock? | 9.7 min | Built. Waiting for Ehsan's feedback |
| 003 | Wed 25 Nov | What is a bond? | 9.7 min | Built (made Tue 24 Nov with Friday's data). Waiting for Ehsan's feedback |
| 004 | Thu 26 Nov | Funds and ETFs | 10.1 min | Built with data to Wed 25 Nov |
| 005 | Fri 27 Nov | Week 1 review (vocabulary sprint) | 9.3 min | Built |
| 006 | Sat 28 Nov (A) | Interest, compounding and real returns | ~10 min | Published by the writer (test run 27 Nov night). Numbers refreshed (US stocks to Wed 25, Europe/gold/oil to Thu 26, crypto/FX to Fri 27). Critic: 5 FIX in round 1, PASS round 2 |
| 007 | Sat 28 Nov (B) | Present value, future value, discounting | ~10 min | Published. Critic: 2 FIX round 1, PASS round 2 |
| 008 | Sat 28 Nov (C) | Annuities and perpetuities (mortgage example) | ~10 min | Published. Critic: 1 FIX round 1, PASS round 2 |

## Decisions 27 Nov (Ehsan)
- Eps 1 to 5 approved. Voice 5 to 10% faster (now +12%). Length is good.
- Myth vs Math report weekly (Fridays) with growth ideas, not daily; lesson days get longer lessons.
- Curriculum v2: all asset classes beginner to professional, interactions, how to buy and sell, interview questions inside.
- Own project (own repo) for the podcast, and one thread (session) per episode.

## Next episodes
- Next run (Sun 29 Nov): A = 009 Return types and money- vs time-weighted return, B = 010 Benchmarks, C = 011 Mean, standard deviation, volatility (curriculum v4 W2 #4 to #6). Then W2 #7 distributions, #8 correlation/covariance/beta, then W3. Ep 008 teaser promises "returns" next.

## Open items
- **Corrections for the next slot A episode (Mon-Thu, from the 28 Nov audit of eps 1 to 8, AUDIT in project files):** teach these in a short "Fixing gaps" segment right after the news, in mechanism style, then delete this item.
  1. NPV and choosing between projects (ep 7 quiz asked it, lesson barely taught it): bring all future money back to today and compare with the cost today; more back than in creates value; between two projects take the one adding more value in today's money, not the bigger total payout; late money shrinks most, and more so at higher rates; the required rate is what you could earn elsewhere for the same risk.
  2. "Return" and "underlying assets" (used in eps 4 and 5, never defined): a return is what an investment earned as a share of what you put in, price change plus income; underlying assets are the real stocks or bonds inside a fund.
  3. Plan update: diversification is in the Risk and Return block (W5), duration in the second bond block (W17), the evidence on active funds in the equity portfolio block (W26), inflation-linked bonds in W20; earlier episodes gave older week numbers.
  4. How rates hit company profits and share prices (ep 6 interview model answer in the bank, not in the audio): higher rates mean bigger interest bills and future profits worth less today, both push share prices down.
- **Publish workflow (27 Nov 20:38 UTC run, commit 7117dba) failed at the Pages deploy step** ("No artifacts named github-pages were found"); the run before it succeeded with the same workflow, so it looks like a GitHub-side glitch. The 28 Nov push triggers a new run: check it built 006 to 008 and updated the feed.
- **Ep 5 correction told in ep 6:** gold Wed 25 Nov was 3,605.20 in the data when ep 5 was made, 3,535.80 now.
- **Data revisions (26 Nov):** the 20 Nov rows for Brent and gold changed in prices.csv after eps 1 and 3 were made. Both re-rendered with the corrected numbers. Check the data again before each episode (rows can be revised).
- **Feed live (27 Nov):** https://ehsanaminia.github.io/daily-brief/feed.xml, subscribed in AntennaPod. Nightly writer from Mon 30 Nov (WRITER.md).
- **News Lab data stopped at Fri 20 Nov** (plus weekend crypto on 21 Nov). Monday 23 Nov is missing: check the GitHub Actions run in market-news-lab.
- Instagram stats are from 26 Oct: Ehsan to send a profile screenshot.
- Episode length: aim 12 to 15 min; early Level 1 episodes are 8 to 10 min and will grow as the content gets deeper.
