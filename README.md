# Global FTW · 2nd edition sneak peek

A Quarto RevealJS lightning talk for the Cloud Native Geospatial Forum.
**20 slides × 15 seconds = 5 minutes**, plus an untimed cover and closing slide.

## Present and review

```sh
uv sync
uv run quarto preview index.qmd
```

Advance once from the cover to start the timed talk. For manual review, add
`?autoSlide=0` **before** the hash: `http://localhost:4200/?autoSlide=0#/slide-04`.
Press `S` for speaker notes. Each film restarts when its slide is entered.

```sh
uv run quarto render index.qmd
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/docs/index.html?autoSlide=0` for the rendered deck,
or `http://127.0.0.1:8765/docs/media.html` for the clip gallery.
All images, fonts, and videos are local. Keep the entire `docs/` directory
when copying the presentation to another machine. PDF exports show posters;
the HTML deck plays the videos.

## Media

Six silent, 12-second H.264 MP4 loops, 1280 × 720 at 30 fps, in
`assets/media/`. Their posters are suitable for a static export.

| Clip | Comparison |
|---|---|
| `brazil-editions.mp4` | Original alpha → 2nd edition, Sorriso, 2025 |
| `netherlands-editions.mp4` | Original alpha → 2nd edition, Flevoland, 2025 |
| `usa-editions.mp4` | Original alpha → 2nd edition, Iowa, 2024 |
| `egypt-change.mp4` | Toshka irrigation expansion, Q3 imagery, 2017 → 2025 |
| `brazil-change.mp4` | Sorriso urban expansion, Q3 imagery, 2017 → 2025 |
| `brazil-predictions.mp4` | Sorriso annual field probabilities, 2017 → 2025 |

Screenshots include the COG boundary layer, a real GeoParquet table, PMTiles
aggregates, Source Cooperative, and the Portolan registry. Exact camera
positions, sources, interpretation limits, and reconstruction steps are in
[MEDIA.md](MEDIA.md) and [assets/scenes.json](assets/scenes.json).

## Preview status

This is a sneak peek, not a release announcement or global accuracy claim.
On 2 October 2026 the viewer still read `ftw/global-data-beta`; the new
`global-data-2e` catalog path was not populated. The Source Cooperative
preview was unlisted. The Portolan screenshot shows the existing Global FTW
catalog, not a verified registration of the second edition.

The existing GitHub Actions workflow publishes on a push to `main`. Local
rendering does not publish anything.
