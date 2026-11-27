"""Build one episode MP3 (free tools: edge-tts + ffmpeg).
usage: build_episode.py <episode_dir>
script.txt: paragraphs separated by a blank line; a line like `[pause 7]` inserts 7 s of silence (for quiz answers).
meta.json: {"number": 2, "title": "...", "date": "2026-11-24", "description": "..."}"""
import asyncio, json, os, pathlib, re, subprocess, sys, tempfile

import edge_tts

ROOT = pathlib.Path(__file__).resolve().parents[1]
VOICE = "en-US-AndrewMultilingualNeural"
RATE = "+12%"  # Ehsan, 27 Nov: 5 to 10% faster than the +4% used in eps 1-5
GAP = 0.45     # seconds of silence between paragraphs

if os.path.exists("/root/.ccr/ca-bundle.crt"):
    os.environ.setdefault("SSL_CERT_FILE", "/root/.ccr/ca-bundle.crt")
PROXY = os.environ.get("HTTPS_PROXY")  # edge-tts does not read it by itself


def silence(path, seconds):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono",
                    "-t", str(seconds), str(path)], check=True)


async def speak(text, mp3, tries=6):
    err = None
    for n in range(tries):
        try:
            await edge_tts.Communicate(text, VOICE, rate=RATE, proxy=PROXY).save(str(mp3))
            return
        except Exception as e:  # voice service sometimes rate-limits: back off and retry
            err = e
            await asyncio.sleep(3 * 2 ** n)
    raise err


def parse(text):
    items, para = [], []
    for line in text.splitlines() + [""]:
        m = re.fullmatch(r"\s*\[pause\s+([\d.]+)\]\s*", line)
        if m or not line.strip():
            if para:
                items.append(("s", " ".join(para))); para = []
            if m:
                items.append(("p", float(m.group(1))))
        else:
            para.append(line.strip())
    return items


async def main(ep):
    ep = pathlib.Path(ep).resolve()
    meta = json.loads((ep / "meta.json").read_text())
    items = parse((ep / "script.txt").read_text())
    work = pathlib.Path(tempfile.mkdtemp(prefix="brief-"))
    files = []
    for i, (kind, val) in enumerate(items):
        wav = work / f"{i:03d}.wav"
        if kind == "s":
            mp3 = work / f"{i:03d}.mp3"
            await speak(val, mp3)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp3), "-ar", "24000", "-ac", "1", str(wav)], check=True)
            files.append(wav)
            gap = work / f"{i:03d}g.wav"; silence(gap, GAP); files.append(gap)
        else:
            silence(wav, val); files.append(wav)
    lst = work / "list.txt"
    lst.write_text("".join(f"file '{f}'\n" for f in files))
    out = ROOT / "audio" / f"daily-brief-{meta['number']:03d}.mp3"
    out.parent.mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c:a", "libmp3lame", "-b:a", "48k", "-ac", "1",
                    "-metadata", f"title=Daily Brief {meta['number']:03d}: {meta['title']}", "-metadata", "artist=Daily Brief",
                    str(out)], check=True)
    secs = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)]))
    words = sum(len(v.split()) for k, v in items if k == "s")
    print(f"{out.name}: {secs/60:.1f} min, {out.stat().st_size/1e6:.1f} MB, {words} spoken words")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1]))
