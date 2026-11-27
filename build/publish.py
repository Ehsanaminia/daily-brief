"""Studio step, run by GitHub Actions (.github/workflows/publish.yml).
For every episode whose meta.json says "publish": true and has no "audio_url" yet:
  1. build the MP3 (build_episode.py), or reuse audio/daily-brief-NNN.mp3 if it is already there,
  2. upload it to a GitHub Release named ep-NNN (keeps big files out of the repo),
  3. write audio_url, audio_bytes and audio_seconds back into meta.json.
Episodes without "publish": true are never built (a draft stays a draft).
Needs: GH_TOKEN and GITHUB_REPOSITORY (both set automatically inside Actions), ffmpeg, edge-tts."""
import json, os, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPO = os.environ["GITHUB_REPOSITORY"]


def run(*cmd):
    subprocess.run(cmd, check=True)


changed = 0
for meta_path in sorted((ROOT / "episodes").glob("*/meta.json")):
    meta = json.loads(meta_path.read_text())
    if not meta.get("publish") or meta.get("audio_url"):
        continue
    n = meta["number"]
    mp3 = ROOT / "audio" / f"daily-brief-{n:03d}.mp3"
    if not mp3.exists():
        run(sys.executable, str(ROOT / "build" / "build_episode.py"), str(meta_path.parent))
    secs = int(float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(mp3)])))
    tag = f"ep-{n:03d}"
    # create the release, or add the file to it if a previous run already created it
    if subprocess.run(["gh", "release", "view", tag, "-R", REPO], capture_output=True).returncode == 0:
        run("gh", "release", "upload", tag, str(mp3), "--clobber", "-R", REPO)
    else:
        run("gh", "release", "create", tag, str(mp3), "-R", REPO,
            "--title", f"Daily Brief {n:03d}: {meta['title']}", "--notes", meta["description"])
    meta.update(audio_url=f"https://github.com/{REPO}/releases/download/{tag}/{mp3.name}",
                audio_bytes=mp3.stat().st_size, audio_seconds=secs)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False) + "\n")
    changed += 1
    print(f"published {tag}: {secs // 60} min, {mp3.stat().st_size / 1e6:.1f} MB")
print(f"{changed} episode(s) published")
