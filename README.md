# Mapping the World as a Digital Public Good

Isaac Corley’s Taylor Geospatial overview for **CNG Forum 2026**, Snowbird.
The [agenda](https://2026.cloudnativegeo.org/#/agenda?day=3&lang=en) lists a
**seven-minute talk, 8 October at 15:33 America/Denver**.

[Live deck](https://isaac.earth/cng-mapping-digital-public-goods/) ·
[Clip gallery](https://isaac.earth/cng-mapping-digital-public-goods/media.html)

The Quarto deck has **15 slides with manual advance**. FTW takes about three
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

**13 silent, 10-second H.264 loops**, 1280 × 720 at 30 fps.
Individual MP4s and posters are in `assets/media/`; the gallery groups them by
comparison and provides downloads.

| Comparison | Clips | Main-deck layout |
|---|---:|---|
| Original FTW → 2nd edition | 6 | Two countries per slide, three slides |
| Probability mask → PMTiles | 1 | Normandy, France |
| 2018 → 2025 | 6 | Two examples per slide, three slides |

Change examples come from the current viewer’s curated list: Brazil, Uganda,
China, Azerbaijan, and Saudi Arabia. Each compares annual GeoParquet outlines
with the corresponding dated imagery. The viewer uses 2018 because it flags
under-detection in some 2017 predictions. The examples distinguish new fields,
changed field layout, and reduced crop activity; they do not claim area totals.

Wipes take 1.2 seconds, with holds before and after. Paired videos wait until
both can play, then restart together on slide entry. An open-source credits
slide appears immediately before the ending slide.

Exact camera positions, quarters, sources, thresholds, exclusions, and rebuild
steps are in [MEDIA.md](MEDIA.md) and [assets/scenes.json](assets/scenes.json).
The data-access slides show actual COG, GeoParquet, PMTiles,
Source Cooperative, and Portolan screenshots.

## Preview status

This is a sneak peek. Figures were refreshed on 3 October 2026 from the
[new viewer](https://research.taylorgeospatial.org/global-ftw-2e/) and
[`ftw/global-data-2e`](https://source.coop/ftw/global-data-2e), including the
updated PMTiles and GeoParquet exports. All slides and clips use the Taylor
Geospatial palette. Source Cooperative still marks the product unlisted.
The Portolan screenshot shows the existing Global FTW catalog.
These selected examples are not a global accuracy or completeness assessment.

The GitHub Actions workflow renders, uploads a Pages artifact, and deploys
directly on a push to `main`. The repository's Pages source is GitHub Actions;
the legacy `gh-pages` branch is no longer the publishing source. Local
rendering alone does not publish anything.

## Open-source acknowledgements

The pipeline and viewer were inspected in
[`taylor-geospatial/global-ftw-2e`](https://github.com/taylor-geospatial/global-ftw-2e),
the renamed repository formerly known as `ftw-s2-quarterly`.
[OPEN_SOURCE.md](OPEN_SOURCE.md) records the dependency evidence and logo sources.
Logos remain in their official colors on the deck’s Taylor Geospatial background.
