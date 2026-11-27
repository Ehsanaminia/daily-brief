# Automatic delivery (goal: episode appears in AntennaPod, no manual download)
1. One-time: merge to main, enable GitHub Pages, subscribe in AntennaPod (see 04, part B).
2. Daily: a scheduled Claude Code task (cloud) runs each morning: re-fetch News Lab data, read STATUS.md, write script/notes, build the MP3, rebuild the feed, commit to main, push. The feed updates itself and AntennaPod downloads it.
   - Needs: edge-tts proxy access in the environment (already works), repo write access to main for that task (your decision: until you trust it, it pushes to a branch and I ask you to merge).
   - Risk: an unreviewed script may contain a mistake. Safer start: the task builds the episode and messages you; you merge with one tap.
3. Notification: the task sends a short message when the episode is ready. Optional.
4. Fallback: if data is stale or the build fails, the task says so and builds nothing rather than guessing.
I have not created any scheduled task. Say "set it up" in Main and I will create it, after you confirm the points in 2.
