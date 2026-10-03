# Mapping the World as a Digital Public Good

Isaac Corley’s Taylor Geospatial overview for **CNG Forum 2026**, Snowbird.
The [agenda](https://2026.cloudnativegeo.org/#/agenda?day=3&lang=en) lists a
**seven-minute talk, 8 October at 15:33 America/Denver**.

[Live deck](https://isaac.earth/cng-mapping-digital-public-goods/) ·
[Clip gallery](https://isaac.earth/cng-mapping-digital-public-goods/media.html)

The Quarto deck has **27 slides with manual advance**. FTW takes about three
quarters of the suggested speaking time. The opening covers Taylor Geospatial;
one slide groups Features of The World, Benchmarks of The World, and the
NeurIPS-accepted *No One Knows the State of the Art in Geospatial Foundation
Models* paper. Speaker notes include a seven-minute pacing guide.

## Present and review

```sh
uv sync --frozen
uv run quarto preview index.qmd
```

Use arrow keys to advance; press `S` for speaker notes. The slides never advance
automatically. Every film restarts on entry, loops silently, and pauses when
its slide is left. `?autoSlide=0` links from the earlier version still work.

```sh
python3 scripts/build_gallery.py
uv run quarto render index.qmd
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/docs/index.html` or
`http://127.0.0.1:8765/docs/media.html`. All maps, fonts, and videos are local.
Keep the whole `docs/` directory when copying the presentation. PDF exports
use posters; the HTML deck plays videos.

## Comparison library

**20 silent, 12-second H.264 loops**, 1280 × 720 at 30 fps.
Individual MP4s and posters are in `assets/media/`; the gallery groups them by
comparison and provides downloads.

| Comparison | Clips | Locations |
|---|---:|---|
| Original FTW → 2nd edition | 6 | Brazil, Netherlands, United States, France, South Africa, Poland |
| Probability/boundary masks → PMTiles | 5 | France (both raster bands), Netherlands, South Africa, Poland |
| 2017 → 2025 | 9 | Toshka and western Nile Delta, Egypt; Santa Cruz, Bolivia; Chaco, Paraguay; Hyderabad, India; Sorriso and Primavera do Leste, Brazil |

Seven change clips compare dated imagery; two compare annual field
probabilities. The Primavera sequence explicitly shows why a probability
change alone does not establish land-use change. Main slides include all
clips; skip individual examples if discussion takes longer than planned.

Exact camera positions, quarters, sources, thresholds, exclusions, and rebuild
steps are in [MEDIA.md](MEDIA.md) and [assets/scenes.json](assets/scenes.json).
The remaining data-access slides show actual COG, GeoParquet, PMTiles,
Source Cooperative, and Portolan screenshots.

## Preview status

This is a sneak peek. The viewer read `ftw/global-data-beta` at capture time;
`global-data-2e` was not populated. Source Cooperative marked the preview
unlisted. The Portolan screenshot shows the existing Global FTW catalog.
These selected examples are not a global accuracy or completeness assessment.

The GitHub Actions workflow renders and publishes on a push to `main`.
Local rendering alone does not publish anything.
