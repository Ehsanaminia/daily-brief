# WRITER: the nightly run (every day, 01:47 Berlin)

Ehsan, 27 Nov 2026: **fully automatic**. The writer pushes straight to `main` after the critic pass; GitHub Actions (`.github/workflows/publish.yml`) then builds the MP3s, stores them in Releases and updates the feed. Nobody approves in between, so the critic pass is the only gate. Mistakes are corrected in the next episode, never by re-rendering.

Read first: PROJECT.md, CURRICULUM.md (format and order), SOURCES.md, CRITIC.md, STATUS.md, GLOSSARY.md, INTERVIEW_BANK.md, PRETRADE_CHECKLIST.md.

## 1. Set up
- Today = the date in Europe/Berlin. Runs every day; on weekends markets are closed: say so and use the last close.
- `git clone` (or pull) `Ehsanaminia/daily-brief`, `Ehsanaminia/market-news-lab` and `Ehsanaminia/fund-manager`, all `main`. For every lesson, read the matching lesson in `fund-manager/docs/curriculum.md` (and `docs/plan.md`) and use its examples and interview question where they fit (Ehsan, 27 Nov: required supporting source, never the only one). Work on `main` of daily-brief.
- Re-fetch `market-news-lab/data/prices.csv` now; rows can be revised. Note the newest close per market. Never guess a missing day; say which close you use.
- Check the last "Publish episodes" run and Releases: if yesterday's episodes did not get an `audio_url`, say so in STATUS.md (Open items) and in the run summary.

## 2. Plan today's 4 episodes (Ehsan, 28 Nov)
Slots from CURRICULUM.md: A, B and C new lessons (A carries the markets news); D review (spaced quiz, interview question). Friday: A week review + vocabulary sprint, B weekly Myth vs Math report + growth ideas (read `mythvsmath` main: `tracker/`, `ideas/`), C new lesson, D mock interview.
- Corrections: if STATUS.md Open items lists corrections for the next slot A, include them in slot A and remove the item.
- Next lessons: the "Next episodes" list in STATUS.md, else the next untaught lessons in CURRICULUM.md order.
- Numbers continue from the highest existing episode number. One folder per episode: `episodes/NNN/`.
- If a folder for today already exists **without** `"publish": true` (for example 006 on Mon 30 Nov), it is today's slot A: keep its content, refresh every market number from today's data, and send it through the critic like a new episode. Never touch an episode that already has `"publish": true`.

## 3. Write each episode
- Pace (Ehsan, 27 Nov): he has a Master of Finance; basics move fast, plain English stays. Teach at the depth of the CFA/FRM topic, with one real example and real data where possible.
- Style (Ehsan, 28 Nov): teach **mechanisms and links**, not math. Say what goes up, what goes down, why, and how it connects to rates, stocks, bonds, currencies and gold. No spoken formulas and no step-by-step calculations; examples use round numbers with the result stated ("a thousand at 7 percent roughly doubles in ten years"). At most two numbers per sentence. Formulas and calculations go in notes.md only.
- Questions (Ehsan, 28 Nov): only ask what was taught. Before writing the quiz and interview corner, list for each question the episode and line that taught it (in notes.md). If it wasn't taught, teach it first or ask something else. The teaser must match the next lesson in STATUS.md.
- `script.txt` (blank line between paragraphs, `[pause N]` for silence), `notes.md` (every number and claim with its source), `meta.json`:
  `{"number": N, "title": "...", "date": "YYYY-MM-DD", "slot": "A", "description": "...", "publish": false}`
- 1,700 to 1,900 spoken words (about 10 minutes at +12%). Follow the episode order in PROJECT.md. Only one slot per day carries the markets news (A); B, C and D open with a one-line link to A instead.
- Write numbers the way the voice should say them. End every episode with "Educational, not financial advice."

## 4. Critic (CRITIC.md)
- For each episode, a **fresh agent** that did not write it gets only `script.txt`, `notes.md` and the data, and writes `CRITIC_REPORT.md` in the folder.
- Fix every FIX and FAIL (verify the critic's evidence first). Re-check changed lines. At most 2 rounds.
- Still FIX or FAIL after 2 rounds: that episode stays `"publish": false`; publish the others; write it under Open items in STATUS.md for Ehsan.

## 5. Publish
- Set `"publish": true` on each episode that passed, then print each meta.json and confirm it says true (Actions builds audio only for those; the 27 Nov test run missed this). Update STATUS.md (table and Next episodes), GLOSSARY.md, INTERVIEW_BANK.md.
- One commit to `main`: "Episodes NNN-NNN for <date>", push (retry on network errors). Aim to push by 04:00 Berlin: building 3 MP3s in Actions can take up to an hour, and Ehsan wakes at 05:30.
- If data or the clone fails: publish nothing, write the reason in STATUS.md if you can, and end with a short failure summary. Never guess.

## 6. Summary
End the run with 3 lines: episode numbers and titles, critic result per episode, anything Ehsan should know (data gaps, blocked episodes).
