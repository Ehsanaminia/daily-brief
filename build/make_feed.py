"""Rebuild feed.xml and index.html from episodes/*/meta.json (newest 30 episodes). usage: make_feed.py [out_dir]
Audio comes from meta.json (audio_url/audio_bytes/audio_seconds, set by publish.py) or, for old episodes, audio/*.mp3.
Optional meta "slot": "A", "B" or "C" orders the 3 episodes of one day (A first)."""
import datetime as dt, email.utils, json, pathlib, subprocess, sys
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "https://ehsanaminia.github.io/daily-brief"
KEEP = 30


OUT = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT


def info(meta):
    """(url, bytes, seconds) or None if the episode has no audio yet."""
    if meta.get("audio_url"):
        return meta["audio_url"], meta["audio_bytes"], meta["audio_seconds"]
    mp3 = ROOT / "audio" / f"daily-brief-{meta['number']:03d}.mp3"
    if not mp3.exists():
        return None
    secs = int(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)])))
    return f"{BASE}/audio/{mp3.name}", mp3.stat().st_size, secs


eps = []
for p in sorted((ROOT / "episodes").glob("*/meta.json")):
    m = json.loads(p.read_text())
    got = info(m)
    if got:
        eps.append((m, *got))
eps.sort(key=lambda e: e[0]["number"], reverse=True)
eps, old = eps[:KEEP], eps[KEEP:]   # older episodes stay in GitHub Releases, just not in the feed

items, rows = [], []
for m, url, size, secs in eps:
    # 03:00 UTC on the episode date; slot A/B/C one minute apart so AntennaPod plays A, then B, then C
    when = dt.datetime.fromisoformat(m["date"]).replace(hour=3, minute="ABC".find(m.get("slot", "A")) % 3, tzinfo=dt.timezone.utc)
    title = f"{m['number']:03d}: {m['title']}"
    items.append(f"""    <item>
      <title>{escape(title)}</title>
      <description>{escape(m['description'])}</description>
      <pubDate>{email.utils.format_datetime(when)}</pubDate>
      <guid isPermaLink="false">daily-brief-{m['number']:03d}</guid>
      <enclosure url="{url}" length="{size}" type="audio/mpeg"/>
      <itunes:duration>{secs}</itunes:duration>
      <itunes:episode>{m['number']}</itunes:episode>
    </item>""")
    rows.append(f'<li><a href="{url}">{escape(title)}</a> ({secs//60} min)</li>')

feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>Daily Brief</title>
    <link>{BASE}/</link>
    <language>en</language>
    <description>A daily coaching podcast: markets news in plain English, one lesson on the way to a career in asset management, a quiz, and a Myth vs Math check-in. Educational, not financial advice.</description>
    <itunes:author>Daily Brief</itunes:author>
    <itunes:explicit>false</itunes:explicit>
    <itunes:category text="Business"/>
{chr(10).join(items)}
  </channel>
</rss>
"""
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "feed.xml").write_text(feed)
(OUT / "index.html").write_text(
    '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    f'<title>Daily Brief</title><h1>Daily Brief</h1><p>Podcast feed: <a href="feed.xml">{BASE}/feed.xml</a></p><ul>{"".join(rows)}</ul>'
    "<p>Educational, not financial advice.</p>")
print(f"feed.xml: {len(eps)} episodes in {OUT}")
