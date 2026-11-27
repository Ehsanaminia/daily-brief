"""Rebuild feed.xml and index.html from episodes/*/meta.json (newest 30 episodes). usage: make_feed.py"""
import datetime as dt, email.utils, json, pathlib, subprocess
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "https://ehsanaminia.github.io/daily-brief"
KEEP = 30


def info(meta):
    mp3 = ROOT / "audio" / f"daily-brief-{meta['number']:03d}.mp3"
    if not mp3.exists():
        return None
    secs = int(float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)])))
    return mp3, secs


eps = []
for p in sorted((ROOT / "episodes").glob("*/meta.json")):
    m = json.loads(p.read_text())
    got = info(m)
    if got:
        eps.append((m, *got))
eps.sort(key=lambda e: e[0]["number"], reverse=True)
eps, old = eps[:KEEP], eps[KEEP:]
for m, mp3, _ in old:
    mp3.unlink(missing_ok=True)   # keep the repo small: only the last 30 episodes stay

items, rows = [], []
for m, mp3, secs in eps:
    when = dt.datetime.fromisoformat(m["date"]).replace(hour=6, tzinfo=dt.timezone.utc)
    title = f"{m['number']:03d}: {m['title']}"
    url = f"{BASE}/audio/{mp3.name}"
    items.append(f"""    <item>
      <title>{escape(title)}</title>
      <description>{escape(m['description'])}</description>
      <pubDate>{email.utils.format_datetime(when)}</pubDate>
      <guid isPermaLink="false">daily-brief-{m['number']:03d}</guid>
      <enclosure url="{url}" length="{mp3.stat().st_size}" type="audio/mpeg"/>
      <itunes:duration>{secs}</itunes:duration>
      <itunes:episode>{m['number']}</itunes:episode>
    </item>""")
    rows.append(f'<li><a href="audio/{mp3.name}">{escape(title)}</a> ({secs//60} min)</li>')

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
(ROOT / "feed.xml").write_text(feed)
(ROOT / "index.html").write_text(
    '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    f'<title>Daily Brief</title><h1>Daily Brief</h1><p>Podcast feed: <a href="feed.xml">{BASE}/feed.xml</a></p><ul>{"".join(rows)}</ul>'
    "<p>Educational, not financial advice.</p>")
print(f"feed.xml: {len(eps)} episodes, removed {len(old)} old audio file(s)")
