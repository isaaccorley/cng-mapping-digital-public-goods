# Media sources and capture notes

Captured 2 October 2026. These are real map renders and website screenshots;
no generated satellite imagery or synthetic boundaries are used.

## Comparisons

| Scene | Latitude, longitude | Viewer zoom | Dates | Interpretation |
|---|---|---|---|---|
| Sorriso, Brazil | -12.58, -55.72 | 13 | 2025 | Large fields and an urban edge; selected edition comparison |
| Flevoland, Netherlands | 52.65, 5.68 | 14 | 2025 | Dense field network; selected edition comparison |
| Iowa, United States | 41.98, -93.72 | 13 | 2024 | Mixed field sizes; selected edition comparison |
| Toshka, Egypt | 22.70, 31.21 | 12.6 | 2017, 2025 | New circular irrigation fields visible in dated imagery |
| Sorriso, Brazil | -12.60, -55.735 | 14 | 2017, 2025 | New streets and buildings along the urban edge |
| Normandy, France | 48.88, -1.05 | 14 | 2025 | Irregular fields; edition, field probability, and boundary probability comparisons |
| Overberg, South Africa | -34.25, 19.5 | 13.5 | 2025 | Curved fields; edition and field probability comparisons |
| Mazovia, Poland | 52.10, 22.14 | 14 | 2025 | Narrow strip fields; edition and field probability comparisons |
| Western Desert, Egypt | 30.32, 29.5 | 12.5 | 2017, 2025 | New centre-pivot field patterns west of the Nile Delta |
| Santa Cruz, Bolivia | -16.97, -62.12 | 12.4 | 2017, 2025 | New field blocks along the agricultural edge |
| Chaco, Paraguay | -22.45, -60.2 | 12.7 | 2017, 2025 | New rectangular clearings; land use is not classified from these images |
| Hyderabad, India | 17.43, 78.3 | 13 | 2017, 2025 | Urban development; Q1 imagery in both years |
| Primavera do Leste, Brazil | -15.565, -54.275 | 13.8 | 2017, 2025 | Urban growth and annual probability changes that need imagery checks |

Backgrounds use **Q3 true-colour Sentinel-2 quarterly mosaics**, except
Hyderabad, which uses **Q1 in both years** because Q3 had cloud gaps. Identical
camera, quarter, band combination, and RGB stretch (0–3000 reflectance ×
10,000) within each pair. Year comparisons use each year's own mosaic.
Basemap fallback was disabled for all final captures, so undated Esri imagery
cannot masquerade as historical imagery. The initial wider Egypt view had
incomplete mosaic coverage; the final camera is within shared coverage.

Both edition overlays use the same yellow-green stroke (`#c0d85b`, 1.4 CSS
pixels) and fill (7% opacity). We did not change geometry, filter by score,
or change model thresholds. These are **PMTiles renderings**, including each
archive's own simplification and tiling choices; visual differences do not
isolate model accuracy or a particular pipeline change.

Field-probability clips use the live viewer's threshold (128/255, about
0.5) and color ramp. A change in probability is a candidate signal, not a
confirmed land-cover transition. Independent annual predictions have no
persistent cross-year field IDs. No area-change totals are claimed.

The five mask-to-PMTiles clips compare the same year, imagery, and camera.
Four use the field-interior band; Normandy's fifth clip uses the boundary
band, with display cutoff 64/255 (about 0.25). Raster overlays preserve the
viewer's color ramp and opacity; they are not binary ground-truth masks.
PMTiles polygons are the published extracted/simplified geometries, not
polygons traced from the screenshots. The raster and vector displays need
not coincide at every edge.

The two Primavera clips form an explicit check on change interpretation.
The large northeast field is visible in both years, although its predicted
probability differs substantially. Do not describe that as a new field.

### Examples not selected

The inspected Punjab (30.79, 75.79) and Ethiopia (8.84, 39.04) PMTiles views
were very sparse relative to visible agricultural texture. This was not
diagnosed as a model, vectorization, or publishing issue, and those scenes
are not presented as improvements. The Toshka probability layers included
large apparent false positives over bare land in 2017; only its dated
imagery is used in the final change clip. Regional validation remains needed.

Additional scouting found very sparse PMTiles at Punjab, Pakistan
(30.62, 72.96). Bolivia and Paraguay probability views contained conspicuous
rectangular false positives over wooded areas, and Hyderabad's probability
views were too sparse for an informative positive comparison. These raster
views were excluded; only their dated imagery is presented. The Bolivia and
Paraguay probability scouts are retained locally under ignored `.capture/`. No model or data
quality issue was diagnosed or fixed as part of making the presentation.

## Primary data sources

- Live viewer: https://isaac.earth/ftw-s2-quarterly/web/
- Second-edition preview: https://source.coop/ftw/global-data-beta
- Raster manifest: https://data.source.coop/ftw/global-data-beta/index/raster.parquet
- Vector manifest: https://data.source.coop/ftw/global-data-beta/index/vector.parquet
- Annual PMTiles: `https://data.source.coop/ftw/global-data-beta/vector/{year}/fields-{year}.pmtiles`
- Alpha 2024: https://data.source.coop/ftw/global-data/predictions/vectors/alpha/2024_with_confidence.pmtiles
- Alpha 2025: https://data.source.coop/ftw/global-field-boundaries/pmtiles/ftw-global-fields-2025.pmtiles
- Input mosaics: https://source.coop/tge-labs/sentinel-2-quarterly-cloudless-mosaics
- Mosaic bands: `https://data.source.coop/tge-labs/sentinel-2-quarterly-cloudless-mosaics/{year}/Q3/{tile_key}/{B04,B03,B02}.tif`
- Prediction COGs: hrefs resolved from the raster manifest; annual model uses four quarters, while the displayed background is Q3.
- FTW prediction license: CC BY 4.0. Imagery credits: Sentinel-2 / Copernicus / CDSE; hosted by Taylor Geospatial on Source Cooperative.

The live viewer's `config.js` explicitly uses `global-data-beta` during
migration. `global-data-2e/README.md` and `global-data-2e/catalog.json`
returned `NoSuchKey` at capture time. Do not silently rewrite the media's
source paths until the destination has been verified.

Snapshots of the catalog README, 2025 vector collection metadata, and SHA-256
hashes of the live viewer modules are saved in `assets/provenance/`.
Catalog counts are moving publication metadata; the talk does not use them
as measured accuracy or completeness results.

## Screenshots

- `source-catalog.jpg`: https://source.coop/ftw/global-data-beta, top of catalog.
- `geoparquet-table.jpg`: actual table preview of https://source.coop/ftw/global-data-beta/vector/2025/zone=15/utm15.parquet, captured from the portal's linked Parquet viewer. Cropped to its header and first rows; no row values altered.
- `cog-boundary.jpg`: Flevoland camera above, 2025 Q3 background with the COG boundary probability layer, live threshold 64/255.
- `pmtiles-overview.jpg`: 2025 coverage aggregates, lat 48, lon 6, zoom 5.5; viewer's published coverage ramp. The slide covers the irrelevant COG loading hint.
- `portolan.jpg`: https://www.portolan-sdi.org/ homepage.
- `portolan-registry.jpg`: https://www.portolan-sdi.org/registry, search “Fields”, cropped to the FTW result. This links to the existing `ftw/global-data/catalog.json`, not the second edition.

Portolan's own description of the FTW relationship:
https://www.portolan-sdi.org/blog/introducing-portolan

Context for agricultural expansion in Egypt:
https://science.nasa.gov/earth/earth-observatory/agriculture-in-egypts-western-desert-144383/
The actual 2017/2025 comparison in this deck is from the supplied FTW viewer,
not from NASA's figure.

## Rebuild media

1. Run `python3 scripts/prepare_capture.py` from the repo root. It snapshots
   the live viewer in ignored `.capture/`, using bundled browser dependencies
   from the neighbouring `../ftw-s2-quarterly/web/vendor` directory.
2. Serve the repository on localhost. Camera parameters are in
   `assets/scenes.json`. Use a unique `scene` query value on navigation;
   the upstream viewer reads the camera hash on initial page load only.
3. Navigate to `.capture/web/?kind=alpha&scene=...#year=...&q=Q3&z=...&lat=...&lon=...`
   and repeat with `kind=pmtiles`, `image`, `field`, or `boundary` as needed.
   Wait for imagery and vector tiles to render fully, inspect, and save
   1280 × 720 map screenshots to `assets/stills/` with the manifest's names.
4. Capture `scripts/frame.html?scene=CLIP_ID&side=before` and `side=after`
   after `body[data-ready=true]`, into `.capture/frames/CLIP_ID-before.jpg`
   and `-after.jpg`. This adds editable Sora/Manrope labels and source credits.
5. Run `python3 scripts/build_clips.py` (requires ffmpeg). Each clip holds the
   first frame, wipes to the second, holds, then returns; 12 seconds total.
6. Render Quarto and inspect playback. Scripts never modify the deployed
   viewer, data, or neighbouring checkout. Re-capture if source data change.

Pass clip IDs to `scripts/build_clips.py` to rebuild only selected clips.
Run `python3 scripts/build_gallery.py` after updating the scene manifest.

FTW logo and self-hosted Sora / Manrope fonts are from the FTW branding asset
bundle. Fonts are SIL Open Font License 1.1; see `assets/fonts/fonts.css`.
The Taylor Geospatial logo is from the TG brand bundle. The framing slides
use TG brown/ivory and Space Grotesk (the approved open slide substitute),
self-hosted from Google Fonts with its OFL in `assets/fonts/space-grotesk/`.

## Talk framing and broader research

- Exact agenda title: **Mapping the World as a Digital Public Good**.
- Seven-minute slot, 8 October 2026 at 15:33 America/Denver:
  https://2026.cloudnativegeo.org/#/agenda?day=3&lang=en
- The public session description is saved in
  `assets/provenance/cng-agenda-2026-10-02.txt`; no attendee profile data are included.
- Taylor Geospatial: https://taylorgeospatial.org/about-us/
- Features: https://taylorgeospatial.org/innovation-program/features-of-the-world/
- Benchmarks: https://taylorgeospatial.org/innovation-program/benchmarks-of-the-world/
- Paper: https://arxiv.org/abs/2605.12678 . NeurIPS 2026 acceptance was confirmed
  directly by Isaac for this talk. The slide avoids numerical audit claims
  from the older preprint while the accepted manuscript is being revised.
