# CRITIC: the two-force check for every Daily Brief episode (27 Nov 2026)

Ehsan, 27 Nov 2026: two forces work on everything. Force 1, the writer, finds the best material and makes sure it is correct. Force 2, the critic, tries to disprove it before anything is published, then the writer fixes every issue.

## Force 1: the writer
- Builds each lesson from authoritative material: CFA Program curriculum outlines, GARP FRM readings, standard textbooks (Hull, Fabozzi, Bodie-Kane-Marcus, Damodaran), central banks, regulators, BIS, IMF, peer-reviewed papers.
- Every number and claim goes into `notes.md` with its source. Market numbers come from News Lab `prices.csv`, re-fetched first.
- Every lesson has a plain definition, a real-life example, real data where it exists (dated and sourced), and quiz and interview questions.

## Force 2: the critic (a fresh agent that did not write the script)
It gets only `script.txt`, `notes.md` and the data. Its job is to try to prove the episode wrong.
1. **Facts and definitions.** Check every definition against at least one authoritative source, and against two for anything disputed. Flag simplifications that become wrong ("a bond is risk-free").
2. **Numbers.** Recompute every number from the raw data with its own script. Spoken number must equal the data (rounding included). Dates must say "as of".
3. **Causes.** Any "why the market moved" without a published source is a FAIL.
4. **Strongest counter-view.** Name the best-known scholar or practitioner view that disagrees and check if the script is fair to it.
5. **Teaching.** Is the example correct and clear for a beginner? Is a term used before it is taught?
6. **Language.** Grammar, typos, words the voice will mispronounce, numbers written so the voice reads them right.
7. **Rules.** No advice on what to buy, ends with "Educational, not financial advice", no personal data.

## Report: `CRITIC_REPORT.md` in the episode folder
| # | Claim or line | Check and source | Result (PASS / FIX / FAIL) | Exact fix |
Plus "not proven" objections (listed, they change nothing).

## Rules
- Any FIX or FAIL blocks the build. The writer fixes; the critic re-checks only the changed lines. At most 2 rounds; if they still disagree, Ehsan decides.
- The writer verifies the critic's counter-evidence before changing anything (the critic can be wrong too).
- Only after PASS: build MP3, rebuild the feed, publish.
- Curriculum changes go through the same check.
