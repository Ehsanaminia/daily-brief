# Step by step (I could not verify the exact button names in the claude.ai app, so follow the idea if a label differs)

## A. Create the project (you, 3 minutes)
1. claude.ai, left menu, Projects, Create project. Name: Daily Brief.
2. Paste the text from 01-name-and-description.md into the description.
3. Open "Set project instructions" and paste 02-project-instructions.md.
4. Add knowledge: files listed in 03-knowledge-files.md. If the project offers "Add from GitHub", connect GitHub (approve the Claude GitHub app on ehsanaminia/daily-brief and ehsanaminia/market-news-lab only, not all repos) and pick the files. Otherwise upload them from the repo.
5. Start thread "Main" and paste the handover text from 03-knowledge-files.md.

## B. Make the feed live (you, 2 minutes, GitHub website)
1. github.com/ehsanaminia/daily-brief, Pull requests, open a PR from ccr-ce5adaa0-x8xpe2 into main, merge it. (Ask me and I will open the PR.)
2. Settings, Pages: source = main branch, root. Wait a minute.
3. Feed link: https://ehsanaminia.github.io/daily-brief/feed.xml
4. AntennaPod (Android): Add podcast, paste the link, turn on auto-download. Episodes then arrive by themselves; no more downloading from Claude.
Note: the repo should be public for free GitHub Pages (or use an unlisted link). Check that nothing private is in it; PROJECT.md says no personal data in the feed or audio.

## C. Important limit (be honest about this)
A chat thread inside a Project cannot run edge-tts or ffmpeg or push to GitHub. The audio is built in a Claude Code session (cloud, like this one). So: planning and learning questions live in Project threads; the building is a Claude Code session or a scheduled task (see 06). Keep the two linked through the repo files (STATUS.md is the shared memory).
