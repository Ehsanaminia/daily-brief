# Daily Brief: a daily podcast to become a professional asset manager

Standing instructions (Ehsan, 23 and 27 Nov 2026). Read this, CURRICULUM.md, GLOSSARY.md and STATUS.md before making an episode.

## Goal
One weekday podcast for Ehsan's commute, on his **Android phone** (AntennaPod, auto-download). It takes him from complete beginner to **professional asset manager**: every asset class from the basics to professional level, how the classes interact, how to buy and sell them, and interview preparation. Episodes 1 to 5 (Week 1) are approved ("fine").

## Listener
Starts knowing nothing. Plain English, short sentences, each new word explained once with a real-life example. Gets steadily more detailed and professional (see CURRICULUM.md).

## Voice (Ehsan, 27 Nov)
edge-tts "Andrew", rate **+12%** (5 to 10% faster than eps 1 to 5, which used +4%). Length is right: about 10 minutes now; lessons may grow to 12 to 15.

## Order of every episode, Monday to Thursday
1. Opening and a 30-second recap of the last lesson.
2. **Markets news** from the News Lab data, with one "what to notice".
3. **Lesson** (one idea; this is the longest part).
4. **Interview corner**: one real interview question, a model answer, a pause to answer out loud.
5. **Quiz**: three or four questions with pauses; one repeats an older term.
6. Tomorrow's teaser and "Educational, not financial advice."
No Myth vs Math segment on these days (Ehsan, 27 Nov): the time goes to the lesson.

## Friday
News week in review, vocabulary and question review of the week, then **the weekly Myth vs Math report** (stats, comments, what worked) plus **growth ideas** (concrete: topic tests, hooks, posting, comments, cross-posting). Weekly, not daily.

## Content rules
- **Asset classes first**: each class is taught beginner to professional, then how it interacts with the others, then how to buy and sell it (where, which instruments, costs, liquidity, settlement, taxes) and what to consider before a transaction (use PRETRADE_CHECKLIST.md). Teach considerations, never "buy this now".
- **Interview questions inside** every lesson day; collect them in INTERVIEW_BANK.md.
- **Free tools only** (edge-tts, ffmpeg, GitHub Pages). No paid services.
- **Numbers**: market numbers come from `market-news-lab/data/prices.csv` (or a named source) and must match what is spoken. The data can be revised after the fact (the 20 Nov rows were): re-fetch before every episode and say the date of the data. If data is stale or missing, say so.
- **Never invent a reason.** A "why did it move" claim needs a published source; otherwise say price data tells what, not why.
- Anything that goes stale (rates, rules, index levels) is marked "as of <date>".
- Every episode has `notes.md` listing each number and claim with its source.
- Always end with "Educational, not financial advice." No tips on what to buy.
- No personal data in the feed or audio. The feed is public (unlisted link).
- Do not re-render finished episodes unless Ehsan asks. Corrections go into the next episode and notes.md.
- One thread (session) per episode, so Ehsan can comment on each. Concise answers, one step at a time.

## How an episode is made
Since 27 Nov 2026 a nightly scheduled run does this automatically (WRITER.md, AUTOMATION.md); audio and feed are built by GitHub Actions, not by hand. The steps below are for a manual episode.
1. Check STATUS.md and CURRICULUM.md for the next topic.
2. Re-fetch `prices.csv` (News Lab) and, on Fridays, the Myth vs Math `tracker/` and `ideas/` files from their `main` branches.
3. Write `episodes/NNN/script.txt` (blank line between paragraphs, `[pause 7]` for silence), `meta.json`, `notes.md`.
4. `python3 build/build_episode.py episodes/NNN` makes `audio/daily-brief-NNN.mp3`. It takes 5 to 10 minutes (the voice service is slow); run it in the background.
5. `python3 build/make_feed.py` rebuilds `feed.xml` (last 30 episodes) and `index.html`.
6. Update STATUS.md and GLOSSARY.md, commit, push, send the MP3 to Ehsan.

## Where the feed lives
`https://ehsanaminia.github.io/daily-brief/feed.xml` (GitHub Pages, serves the main branch of this repo).
