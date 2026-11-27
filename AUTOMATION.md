# How episodes reach your phone (no downloading)

Three parts, all free:

| Part | Who does it | When |
|---|---|---|
| Writer: fetch News Lab data, write the 3 scripts, critic pass, save to the repo | Scheduled Claude task (cloud) | Mon to Fri, about 03:30 Berlin |
| Studio: turn scripts into MP3s, store them in GitHub Releases, rebuild the feed, publish the site | GitHub Actions (`.github/workflows/publish.yml`) | Automatically, a few minutes after new scripts land on `main` |
| Player: download the new episodes overnight | AntennaPod on your phone | Checks the feed every hour |

Only episodes whose `meta.json` has `"publish": true` are ever built, so a draft never goes out by accident.
MP3s live in GitHub Releases (tag `ep-NNN`), not in the repo, so the repo stays small.

## One-time setup (you, about 5 minutes)

1. GitHub > daily-brief > Settings > General > Danger zone > Change visibility > **Public** (free Pages needs it).
2. Settings > Pages > Build and deployment > Source: **GitHub Actions**.
3. Merge the pull request that adds this file. The first run moves episodes 1 to 5 into Releases and publishes the feed.
4. AntennaPod: + > Add podcast by URL > `https://ehsanaminia.github.io/daily-brief/feed.xml`
5. AntennaPod > the Daily Brief podcast > settings (gear): **Auto download: on**.
   App Settings > Downloads: **Update interval: every hour**, and allow mobile data if you want it off Wi-Fi.

## Decided (27 Nov 2026)
- Fully automatic: the writer pushes straight to `main` after the critic pass (rules in WRITER.md). First run Mon 30 Nov.
- Feed live, subscribed in AntennaPod. Note: the repo's default branch is still `ccr-ce5adaa0-x8xpe2`; the `github-pages` environment has a rule allowing `main`.

## Next
- Phase 2: your own app (home-screen web app with player, show notes, quiz, glossary).

Educational, not financial advice.
