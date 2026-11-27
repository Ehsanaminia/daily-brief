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
      <itunes:image href="{BASE}/art/{m['number']:03d}.png"/>
    </item>""")
    rows.append(f'<a class="ep" href="{url}"><img src="art/{m["number"]:03d}.png" alt="" loading="lazy">'
                f'<span><b>{escape(title)}</b><small>{escape(m["date"])} · {secs // 60} min</small>{escape(m["description"])}</span></a>')

feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>Daily Brief</title>
    <link>{BASE}/</link>
    <language>en</language>
    <image><url>{BASE}/cover.png</url><title>Daily Brief</title><link>{BASE}/</link></image>
    <itunes:image href="{BASE}/cover.png"/>
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
    '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    '<title>Daily Brief</title><link rel="icon" href="cover.png"><link rel="apple-touch-icon" href="cover.png">'
    '<style>body{margin:0;background:#0b1b2b;color:#f5f7fa;font:16px/1.45 system-ui,sans-serif}'
    'main{max-width:720px;margin:auto;padding:16px}header{display:flex;gap:16px;align-items:center;overflow-wrap:anywhere}'
    'header img{width:120px;border-radius:12px}h1{margin:0;color:#f2b84b}a{color:#f2b84b}'
    '.ep{display:flex;gap:12px;padding:12px 0;border-top:1px solid #1e3c58;color:inherit;text-decoration:none}'
    '.ep img{width:88px;height:88px;border-radius:8px;flex:none}.ep b,.ep small{display:block}'
    '.ep small{color:#96afc6}footer{color:#96afc6;padding:24px 0}</style><main>'
    f'<header><img src="cover.png" alt="Daily Brief cover"><div><h1>Daily Brief</h1>'
    f'<p>Markets, lessons and interviews: from beginner to asset manager.<br><a href="feed.xml">Podcast feed (paste into AntennaPod)</a></p></div></header>'
    f'{"".join(rows)}<footer>Educational, not financial advice.</footer></main>')
print(f"feed.xml: {len(eps)} episodes in {OUT}")
