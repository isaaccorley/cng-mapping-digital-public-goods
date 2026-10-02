"""Make a local, presentation-only copy of the live FTW viewer.

Run from the repo root. Browser screenshots are captured separately; this
script never changes the deployed viewer or the neighbouring checkout.
"""

import hashlib
import json
import pathlib
import re
import shutil
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
WEB = ROOT / ".capture/web"
SOURCE = "https://isaac.earth/ftw-s2-quarterly/web/"
VENDOR = ROOT.parent / "ftw-s2-quarterly/web/vendor"
WEB.mkdir(parents=True, exist_ok=True)
shutil.copytree(VENDOR, WEB / "vendor", dirs_exist_ok=True)
shutil.copytree(VENDOR.parent / "assets", WEB / "assets", dirs_exist_ok=True)
(WEB / "js").mkdir(exist_ok=True)
pending = ["index.html", "style.css", "js/main.js"]
snapshot = {}
while pending:
    name = pending.pop()
    if name in snapshot:
        continue
    data = urllib.request.urlopen(SOURCE + name).read()
    (WEB / name).write_bytes(data)
    snapshot[name] = hashlib.sha256(data).hexdigest()
    if name.endswith(".js"):
        pending.extend(
            "js/" + p for p in re.findall(r"from ['\"]\./([^'\"]+)", data.decode())
        )
(WEB.parent / "viewer-source-sha256.json").write_text(json.dumps(snapshot, indent=2))

# Only presentation state and symbology change. The original data URLs,
# geometries, probability thresholds and RGB stretch are preserved.
main = WEB / "js/main.js"
src = main.read_text()
src = src.replace(
    "  return view;",
    """
  const capture = new URLSearchParams(location.search);
  if (capture.has('kind')) {
    for (const key of Object.keys(state.show)) state.show[key] = false;
    state.show.mosaic = capture.get('base') !== 'esri';
    const kind = capture.get('kind');
    if (kind !== 'image') state.show[kind] = true;
  }
  return view;""",
)
main.write_text(src)
alpha = WEB / "js/alpha.js"
src = alpha.read_text().replace("COLORS.alpha, width: 1.2", "'#c0d85b', width: 1.4")
src = src.replace("COLORS.alphaFill", "'rgba(192,216,91,0.07)'")
alpha.write_text(src)
pm = WEB / "js/pmtiles.js"
src = pm.read_text().replace(
    "const FIELD_GREEN = '#33a02c';", "const FIELD_GREEN = '#c0d85b';"
)
src = src.replace("hexAlpha(FIELD_GREEN, 0.25)", "hexAlpha(FIELD_GREEN, 0.07)")
src = src.replace("FIELD_GREEN, width: 1", "FIELD_GREEN, width: 1.4")
pm.write_text(src)
map_file = WEB / "js/map.js"
src = map_file.read_text().replace(
    "  const view = new View({",
    "  if (new URLSearchParams(location.search).has('kind')) basemap.setVisible(false);\n  const view = new View({",
)
map_file.write_text(src)
with (WEB / "style.css").open("a") as f:
    f.write("""
/* Film capture: preserve the map scale; remove the temporary app chrome. */
#panel, .ol-zoom, .ol-attribution { display: none !important; }
#map { inset: 0 !important; width: 100vw !important; height: 100vh !important; }
.ol-scale-line { bottom: 22px !important; right: 24px !important; left: auto !important; }
#hint { font-size: 18px; }
""")
print("Capture viewer ready at .capture/web; serve repo on localhost:8765")
