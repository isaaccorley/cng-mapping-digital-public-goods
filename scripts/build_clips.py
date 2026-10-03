"""Encode labelled screenshot pairs as 12-second, silent H.264 wipe loops."""

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
scenes = json.loads((ROOT / "assets/scenes.json").read_text())["clips"]
for scene in scenes:
    name = scene["id"]
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue
    before = ROOT / f".capture/frames/{name}-before.jpg"
    after = ROOT / f".capture/frames/{name}-after.jpg"
    out = ROOT / f"assets/media/{name}.mp4"
    # First view 2 s; reveal second 2 s; hold second 5 s; return 2 s; hold 1 s.
    # Browser captures are full-range BT.601 JPEGs; export tagged BT.709 video.
    filt = (
        "[0:v]split=2[a][c];"
        "[a][1:v]xfade=transition=wiperight:duration=2:offset=2[ab];"
        "[ab][c]xfade=transition=wipeleft:duration=2:offset=9,"
        "scale=in_color_matrix=bt601:in_range=pc:out_color_matrix=bt709:out_range=tv,"
        "format=yuv420p[v]"
    )
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-loop",
            "1",
            "-framerate",
            "30",
            "-i",
            str(before),
            "-loop",
            "1",
            "-framerate",
            "30",
            "-i",
            str(after),
            "-filter_complex",
            filt,
            "-map",
            "[v]",
            "-t",
            "12",
            "-c:v",
            "libx264",
            "-preset",
            "slow",
            "-crf",
            "19",
            "-color_range",
            "tv",
            "-colorspace",
            "bt709",
            "-color_primaries",
            "bt709",
            "-color_trc",
            "bt709",
            "-movflags",
            "+faststart",
            "-an",
            str(out),
        ],
        check=True,
    )
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            "3",
            "-i",
            str(out),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(ROOT / f"assets/media/{name}-poster.jpg"),
        ],
        check=True,
    )
    print(f"{name}: encoded", flush=True)
