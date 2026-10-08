"""Build the clip gallery from the captured scene manifest."""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "assets/scenes.json").read_text())
scenes = manifest["clips"]
version = manifest.get("media_version", manifest["captured"].replace("-", ""))
groups = [
    ("change", "2018 → 2025", {"image"}),
    ("editions", "Global FTW 1st edition → 2nd edition", {"edition"}),
    ("layers", "Probability masks → PMTiles", {"layers"}),
]
parts = []
for anchor, title, kinds in groups:
    parts.append(f'<section id="{anchor}"><h2>{title}</h2><div class="clips">')
    for scene in scenes:
        if scene["kind"] not in kinds:
            continue
        name = scene["id"]
        place = html.escape(scene["place"])
        detail = html.escape(scene["detail"])
        labels = html.escape(scene["before_label"] + " → " + scene["after_label"])
        parts.append(
            f"<article><h3>{place}</h3><p>{detail}</p>"
            f'<video controls muted loop playsinline preload="metadata" '
            f'poster="assets/media/{name}-poster.jpg?v={version}" aria-label="{place}: {detail}">'
            f'<source src="assets/media/{name}.mp4?v={version}" type="video/mp4"></video>'
            f'<p class="caption">{labels} · {scene["lat"]}, {scene["lon"]}</p>'
            f'<a href="assets/media/{name}.mp4?v={version}" download>Download MP4</a></article>'
        )
    parts.append("</div></section>")

page = (
    """<!doctype html>
<html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mapping the World as a Digital Public Good · clips</title>
<link rel="stylesheet" href="assets/fonts/fonts.css">
<link rel="stylesheet" href="assets/fonts/tg-fonts.css">
<style>
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f4eb;color:#3b1e1c;font:18px/1.5 'Space Grotesk',sans-serif}
main{max-width:1400px;margin:auto;padding:54px 40px}h1,h2,h3{font-family:'Space Grotesk',sans-serif;font-weight:500}
h1{font-size:clamp(36px,5vw,64px);line-height:1.1;max-width:1000px;margin:15px 0 25px}
h2{font-size:35px;border-top:1px solid #3b1e1c;padding-top:25px;margin:60px 0 30px}h3{font-size:26px;margin:0}
.eyebrow{font-size:14px;letter-spacing:.13em;text-transform:uppercase}.clips{display:grid;grid-template-columns:1fr 1fr;gap:44px 30px}
article p{margin:6px 0 14px}video{display:block;width:100%;aspect-ratio:16/9;background:#3b1e1c}.caption{font-size:13px;margin-top:12px;color:#675250}
a{color:#3b1e1c;text-underline-offset:4px}nav{display:flex;gap:30px;flex-wrap:wrap;margin:28px 0}footer{font-size:14px;border-top:1px solid;margin-top:60px;padding-top:20px}
@media(max-width:850px){.clips{grid-template-columns:1fr}main{padding:30px 20px}}
</style><main><div class="eyebrow">Taylor Geospatial · CNG Forum 2026</div>
<h1>Mapping the World<br>as a Digital Public Good</h1>
<p>13 FTW comparison clips · silent 10-second loops · 1280 × 720</p>
<nav><a href="index.html">Slide deck</a><a href="#change">2018 → 2025</a><a href="#editions">Edition comparisons</a><a href="#layers">Masks and polygons</a></nav>
"""
    + "\n".join(parts)
    + """
<footer>Global FTW 1st and 2nd edition comparisons. Sources and capture details are documented in MEDIA.md in the repository.</footer></main></html>
"""
)
(ROOT / "media.html").write_text(page)
