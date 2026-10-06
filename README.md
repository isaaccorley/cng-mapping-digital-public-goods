# Mapping the World as a Digital Public Good

Isaac Corley’s Taylor Geospatial overview for **CNG Forum 2026**, Snowbird.
The [agenda](https://2026.cloudnativegeo.org/#/agenda?day=3&lang=en) lists the slot
on **8 October at 15:33 America/Denver**. The plenary lightning-talk format is
**20 slides × 15 seconds = 5 minutes**, per the
[CNG presenter guidance](https://cloudnativegeo.org/blog/2026/04/share-your-work-at-cng-forum-2026/).
The agenda's seven-minute slot should not be used as the speaking duration.

[Live deck](https://isaac.earth/cng-mapping-digital-public-goods/) ·
[Clip gallery](https://isaac.earth/cng-mapping-digital-public-goods/media.html)

The Quarto deck has **20 slides with automatic advance**. The talk moves from
field mapping and agricultural change to reusable geographic representations
and model evaluation. FTW occupies 12 slides, including the quarterly mosaic
mirror, processing tools, formats, and access.
MIND the Gap and Planetary Feature Fields each have a dedicated 15-second slide.
The NeurIPS-accepted *No One Knows the State of the Art in Geospatial Foundation
Models* paper follows them, alongside Features of The World and Benchmarks of
The World. Project QR codes and open-source acknowledgements precede the closing
links. The final QR code opens the project links in manual mode.
Sources and attribution are in speaker notes instead of slide footers.

## Present and review

```sh
uv sync --frozen
uv run quarto preview index.qmd
```

The presentation clock starts when the deck opens. Each slide advances after
15 seconds, including slides with longer videos. Arrow-key navigation and video
controls do not disable the timer. The closing slide is reached at 4:45 and
remains visible; the deck does not loop. Open or reload the normal deck URL on cue.

For manual review, use
[?autoSlide=0](https://isaac.earth/cng-mapping-digital-public-goods/?autoSlide=0).
Use arrow keys to advance and press `S` for speaker notes. Every film restarts on
entry, loops silently, and pauses when its slide is left. Manual review disables
both the global timer and the explicit per-slide timings.

```sh
python3 scripts/build_gallery.py
node --test tests/playback.test.cjs
uv run quarto render index.qmd
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/docs/index.html` or
`http://127.0.0.1:8765/docs/media.html`. All maps, fonts, and videos are local.
Keep the whole `docs/` directory when copying the presentation. PDF exports
use posters; the HTML deck plays videos.

The MIND slide includes a local 30-second embedding-globe clip from the project
site. The PFF slide plays the supplied 22.3-second NDVI access demonstration.
Conference mode advances both slides at 15 seconds; manual review allows the
full clips to play. Clip timing and media files are unchanged.
[RESEARCH.md](RESEARCH.md) records the sources, figure attribution, and clip edit.

## Comparison library

**13 silent, 10-second H.264 loops**, 1280 × 720 at 30 fps.
Individual MP4s and posters are in `assets/media/`; the gallery groups them by
comparison and provides downloads.

| Comparison | Clips | Main-deck layout |
|---|---:|---|
| Global FTW 1st edition → 2nd edition | 6 | Two countries per slide, three slides |
| Probability mask → PMTiles | 1 | Normandy, France |
| 2018 → 2025 | 6 | Two examples per slide, three slides |

Change examples come from the current viewer’s curated list: Brazil, Uganda,
China, Azerbaijan, and Saudi Arabia. Each compares annual GeoParquet outlines
with the corresponding dated imagery. The viewer uses 2018 because it flags
under-detection in some 2017 predictions. The examples distinguish new fields,
changed field layout, and reduced crop activity; they do not claim area totals.

Wipes take 1.2 seconds, with holds before and after. Both videos receive a play
request on slide entry; one loading clip cannot block its neighbour. Playback
resumes after returning to the tab. Native controls provide a manual fallback
if the browser blocks autoplay. An open-source credits slide appears immediately
before the ending slide.

The mosaic slide links the [quarterly Sentinel-2 mirror](https://source.coop/tge-labs/sentinel-2-quarterly-cloudless-mosaics)
and highlights COG overviews and HTTP streaming. The processing-tools slide links
coarsen, contourrs, and fbp. The project-links slide points to the
[FTW pipeline and catalog](https://github.com/fieldsoftheworld/ftw-global-data-catalog),
alongside the datasets and research projects. Training code is in the companion
[ftw-baselines repository](https://github.com/fieldsoftheworld/ftw-baselines).

QR images are local files generated from `assets/project-links.json`:

```sh
uv run scripts/build_qr_codes.py
```

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
