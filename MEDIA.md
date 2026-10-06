# Media sources and capture notes

The main deck contains 13 clips, all captured from real FTW data and satellite
imagery. Six edition comparisons and the Normandy probability/polygon example
use the refreshed 3 October stills. Six new change comparisons use the current
viewer’s curated examples. No satellite pixels or field geometries are generated.
Edition labels were updated on 6 October to “Global FTW 1st edition” and
“2nd edition.” The source imagery, boundaries, and wipe timing are unchanged.

## Current comparisons

| Example | Latitude, longitude | Zoom | Dates / quarter | Layers |
|---|---|---:|---|---|
| Sorriso, Brazil | -12.58, -55.72 | 13 | 2025 Q3 | Alpha / 2e PMTiles |
| Flevoland, Netherlands | 52.65, 5.68 | 14 | 2025 Q3 | Alpha / 2e PMTiles |
| Iowa, United States | 41.98, -93.72 | 13 | 2024 Q3 | Alpha / 2e PMTiles |
| Normandy, France | 48.88, -1.05 | 14 | 2025 Q3 | Alpha / 2e PMTiles; field probability / PMTiles |
| Overberg, South Africa | -34.25, 19.5 | 13.5 | 2025 Q3 | Alpha / 2e PMTiles |
| Mazovia, Poland | 52.10, 22.14 | 14 | 2025 Q3 | Alpha / 2e PMTiles |
| Matopiba, Brazil (G07) | -8.025, -44.245 | 13 | 2018 / 2025 Q3 | Annual GeoParquet outlines + imagery |
| Masindi, Uganda (G08) | 1.575, 31.926 | 13 | 2018 / 2025 Q1 | Annual GeoParquet outlines + imagery |
| Ili Valley, China (GN02) | 43.625, 81.198 | 13 | 2018 / 2025 Q3 | Annual GeoParquet outlines + imagery |
| Kura lowland, Azerbaijan (H04) | 39.625, 48.458 | 13 | 2018 / 2025 Q3 | Annual GeoParquet outlines + imagery |
| West Bahia, Brazil (BG1) | -13.325, -45.711 | 13 | 2018 / 2025 Q1 | Annual GeoParquet outlines + imagery |
| Al-Jawf, Saudi Arabia (LN06) | 30.525, 38.155 | 13 | 2018 / 2025 Q3 | Annual GeoParquet outlines + imagery |

The viewer’s curated examples use 2018 as the early year because its notes flag
under-detection in some 2017 and 2024 predictions. The first four change examples
show new field patterns. West Bahia shows rectangular fields replaced by center
pivots while the land remains agricultural. Al-Jawf shows fewer green pivots in
the later mosaic; the images do not establish permanent abandonment or its cause.
No crop type, hectare total, or causal explanation is inferred.

The curated example IDs, dates, and descriptions are snapshotted in
`assets/provenance/viewer-change-examples-2026-10-03.json`. Matopiba uses Q3 in
both years instead of the viewer preset’s Q1, which had visible cloud gaps.
All selected map views were checked for complete rendering. The change frames
wait for both raster rendering and GeoParquet outline loading before capture.
The earlier change scenes and additional mask comparisons are omitted from the
main deck and gallery. Their metadata remain in `assets/scenes-archive.json`
and their earlier notes in `assets/provenance/media-notes-earlier-2026-10-03.md`.

## Rendering and interpretation

Each pair preserves the camera, quarter, bands, and RGB stretch (0–3000
reflectance × 10,000). Each year uses its own Sentinel-2 quarterly mosaic and
annual outlines. Undated basemap fallback is disabled. The edition comparisons
use the same background image on both sides.

PMTiles uses TG periwinkle (`#80a0d8`), 1.4 CSS-pixel strokes, and 7% fill on
both sides. GeoParquet outlines retain the viewer’s 1.6-pixel strokes with the
same periwinkle and 7% fill. Geometry, scores, and selection thresholds are
unchanged. Field probability uses the viewer threshold of 128/255, about 0.5,
with a TG brown → periwinkle → light-blue ramp and the original raster opacity.

Archive simplification and extraction affect the edition comparison; the
pictures do not isolate model accuracy. Annual IDs are independent. Changes in
polygon coverage alone are not confirmed land-use changes. These selected
examples are not a global accuracy or completeness assessment.

## Sources and screenshots

- Viewer: https://research.taylorgeospatial.org/global-ftw-2e/web/
- Source repository: https://github.com/taylor-geospatial/global-ftw-2e
- Data product: https://source.coop/ftw/global-data-2e
- Annual PMTiles: `https://data.source.coop/ftw/global-data-2e/vector/{year}/fields-{year}.pmtiles`
- Annual GeoParquet: `https://data.source.coop/ftw/global-data-2e/vector/{year}/zone={zone}/utm{zone}.parquet`
- Raster index: https://data.source.coop/ftw/global-data-2e/index/raster-lite.parquet
- Vector index: https://data.source.coop/ftw/global-data-2e/index/vector.parquet
- Input mosaics: https://source.coop/tge-labs/sentinel-2-quarterly-cloudless-mosaics
- Alpha 2024: https://data.source.coop/ftw/global-data/predictions/vectors/alpha/2024_with_confidence.pmtiles
- Alpha 2025: https://data.source.coop/ftw/global-field-boundaries/pmtiles/ftw-global-fields-2025.pmtiles

FTW predictions are CC BY 4.0. Imagery credits are Sentinel-2 / Copernicus / CDSE,
hosted by Taylor Geospatial on Source Cooperative. The figures reflect the
updated PMTiles and GeoParquet exports with small holes filled. Object metadata
for the refreshed exports is in `assets/provenance/data-headers-2026-10-03.json`.

The format and distribution slides retain the verified screenshots:
`source-catalog.jpg` shows the 2e catalog; `geoparquet-table.jpg` is the portal’s
actual 2025 UTM 15 table preview; `pmtiles-overview.jpg` uses published coverage
values with unchanged breaks at 0, 2, 10, 25, 50, and 75 percent.
`portolan-registry.jpg` shows the existing Global FTW catalog at
https://www.portolan-sdi.org/registry, not confirmed registration of the 2e product.

## Rebuild

1. Run `python3 scripts/prepare_capture.py`. It snapshots the deployed viewer
   into ignored `.capture/web/`, with local presentation styling and loading
   diagnostics. It does not modify the public viewer or adjacent repository.
2. Serve this repository on port 8765. At 1280 × 720, navigate to
   `.capture/web/?kind=outlines&scene=UNIQUE#year=2018&q=Q3&z=13&lat=...&lon=...`.
   Use the manifest’s camera and `kind=alpha`, `pmtiles`, or `field` for those
   comparisons. Wait for `body[data-capture-ready=true]` and, for outlines,
   `body[data-outlines-ready=true]`; inspect the map, then save to `assets/stills/`.
3. Capture `scripts/frame.html?scene=CLIP_ID&side=before` and `side=after` after
   `body[data-ready=true]`, into `.capture/frames/CLIP_ID-before.jpg` and `-after.jpg`.
   Paired examples have large date/version labels, with location captions in the slide.
4. Run `python3 scripts/build_clips.py` and `python3 scripts/build_gallery.py`.
   The 10-second loops hold the first view for 2 seconds, wipe in 1.2 seconds,
   hold the second for 4.6 seconds, return in 1.2 seconds, then hold for 1 second.
   Video is silent H.264, 1280 × 720 at 30 fps, limited-range BT.709, with explicit metadata.
5. Render Quarto and inspect all changed slide layouts and paired playback.
   Bump `media_version` and slide media URLs when replacing cached assets.

Fonts are self-hosted Space Grotesk under OFL. TG brand assets come from its
brand bundle. Official open-source logos and dependency evidence are documented
in [OPEN_SOURCE.md](OPEN_SOURCE.md).
