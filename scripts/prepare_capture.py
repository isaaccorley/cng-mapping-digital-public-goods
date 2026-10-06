"""Make a local, presentation-only copy of the live FTW viewer.

Run from the repo root. Browser screenshots are captured separately; this
script never changes the deployed viewer or the neighbouring checkout.
"""

import hashlib
import json
import pathlib
import subprocess
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
WEB = ROOT / ".capture/web"
SOURCE = "https://research.taylorgeospatial.org/global-ftw-2e/"
WEB.mkdir(parents=True, exist_ok=True)
(WEB / "js").mkdir(exist_ok=True)
# Read the deployed modules; use its repository tree to enumerate bundled assets.
tree = json.loads(
    subprocess.check_output(
        [
            "gh",
            "api",
            "repos/taylor-geospatial/global-ftw-2e/git/trees/main?recursive=1",
        ],
        text=True,
    )
)["tree"]
pending = ["index.html", "style.css"] + [
    item["path"].removeprefix("web/")
    for item in tree
    if item["type"] == "blob"
    and item["path"].startswith(("web/js/", "web/vendor/", "web/assets/", "web/data/"))
]
snapshot = {}
while pending:
    name = pending.pop()
    if name in snapshot:
        continue
    url = SOURCE + (name if name == "index.html" else "web/" + name)
    data = urllib.request.urlopen(url, timeout=30).read()
    (WEB / name).parent.mkdir(parents=True, exist_ok=True)
    (WEB / name).write_bytes(data)
    snapshot[name] = hashlib.sha256(data).hexdigest()
(WEB.parent / "viewer-source-sha256.json").write_text(json.dumps(snapshot, indent=2))

# Only presentation state and styling change. Geometry, raster opacity,
# probability thresholds, and the RGB imagery stretch are preserved.
main = WEB / "js/main.js"
src = main.read_text()
src = src.replace(
    "  return view;",
    """
  const capture = new URLSearchParams(location.search);
  if (capture.has('kind')) {
    for (const key of Object.keys(state.show)) state.show[key] = false;
    state.show.mosaic = capture.get('base') !== 'none';
    const kind = capture.get('kind');
    if (kind !== 'image') state.show[kind] = true;
  }
  return view;""",
)
src = src.replace(
    "  const ready = () => sync();",
    """  document.body.dataset.captureReady = 'false';
  map.on('idle', () => {
    const rasterReady = !rasterOn() || (raster && last.tiles.length > 0 && raster.layers.inflight === 0 && raster.layers.errors.size === 0);
    const vectorsReady = (!state.show.pmtiles || pmtiles.ready) && (!state.show.outlines || document.body.dataset.outlinesReady === 'true');
    document.body.dataset.captureReady = String(rasterReady && vectorsReady && map.areTilesLoaded());
    document.body.dataset.captureState = JSON.stringify({year: state.year, quarter: state.quarter, show: state.show, center: map.getCenter(), zoom: webZoom(map.getZoom()), tiles: last.tiles, errors: raster?.layers.errors.size ?? 0, outlines: outlines?.count() ?? 0});
  });
  const ready = () => sync();""",
)
main.write_text(src)
vector = WEB / "js/vector.js"
src = vector.read_text().replace(
    "  async sync(state, tiles) {",
    "  async sync(state, tiles) {\n    document.body.dataset.outlinesReady = 'false';",
)
src = src.replace(
    "      await Promise.all(Array.from({ length: CONCURRENCY }, worker));",
    "      await Promise.all(Array.from({ length: CONCURRENCY }, worker));\n"
    "      if (token === this.token) { document.body.dataset.outlinesReady = 'true'; this.map.triggerRepaint(); }",
)
vector.write_text(src)
alpha = WEB / "js/alpha.js"
src = alpha.read_text().replace(
    "'line-color': COLORS.alpha, 'line-width': 1.2",
    "'line-color': '#80a0d8', 'line-width': 0.7",
)
src = src.replace("COLORS.alphaFill", "'rgba(128,160,216,0.07)'")
alpha.write_text(src)
pm = WEB / "js/pmtiles.js"
src = pm.read_text().replace(
    "const FIELD_GREEN = '#33a02c';", "const FIELD_GREEN = '#80a0d8';"
)
src = src.replace("const FIELD_FLAT_ALPHA = 0.25;", "const FIELD_FLAT_ALPHA = 0.07;")
src = src.replace(
    "'line-color': FIELD_GREEN, 'line-width': 1",
    "'line-color': FIELD_GREEN, 'line-width': 0.7",
)
pm.write_text(src)
config = WEB / "js/config.js"
src = config.read_text()
src = src.replace("fieldLow: [0, 71, 71]", "fieldLow: [59, 30, 28]")
src = src.replace("fieldMid: [34, 160, 112]", "fieldMid: [128, 160, 216]")
src = src.replace("fieldHigh: [192, 216, 91]", "fieldHigh: [167, 208, 220]")
src = src.replace("boundary: [255, 127, 65]", "boundary: [255, 79, 44]")
src = src.replace("outline: '#ff7f41'", "outline: '#80a0d8'")
src = src.replace(
    "outlineFill: 'rgba(255, 127, 65, 0.10)'",
    "outlineFill: 'rgba(128, 160, 216, 0.07)'",
)
src = src.replace(
    "[['#ffffd9', 0], ['#edf8b1', 2], ['#7fcdbb', 10], ['#41b6c4', 25], ['#225ea8', 50], ['#081d58', 75]]",
    "[['#f4f4eb', 0], ['#e1e7ed', 2], ['#b8cde2', 10], ['#80a0d8', 25], ['#4a78b5', 50], ['#24496d', 75]]",
)
config.write_text(src)
map_file = WEB / "js/map.js"
src = map_file.read_text().replace(
    "    style: baseStyle(),",
    "    style: {...baseStyle(), layers: []},",
)
src = src.replace(
    "antialias: true, alpha: true",
    "antialias: true, alpha: true, preserveDrawingBuffer: true",
)
map_file.write_text(src)
refstyle = WEB / "js/refstyle.js"
src = refstyle.read_text().replace(
    "?? REF_ANCHOR", "?? (map.getLayer(REF_ANCHOR) ? REF_ANCHOR : undefined)"
)
refstyle.write_text(src)
with (WEB / "style.css").open("a") as f:
    f.write("""
/* Film capture: preserve the map scale; remove the temporary app chrome. */
#panel, #hint, #stars, #halo, #globe-hint, .maplibregl-ctrl-top-right, .maplibregl-ctrl-attrib { display: none !important; }
#map { inset: 0 !important; width: 100vw !important; height: 100vh !important; }
.maplibregl-ctrl-bottom-right { bottom: 22px !important; right: 24px !important; }
#hint { font-size: 18px; }
body, #map { background: #3b1e1c !important; }
""")
index = WEB / "index.html"
index.write_text(
    index.read_text()
    .replace("web/", "")
    .replace('href="style.css"', 'href="style.css?capture=tg-20261006-data"')
)
print("Capture viewer ready at .capture/web; serve repo on localhost:8765")
