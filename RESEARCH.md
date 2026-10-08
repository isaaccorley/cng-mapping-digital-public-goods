# Research slides

The two research slides follow FTW's data-access slides.
MIND introduces reusable geospatial embeddings; PFFs extend the discussion to compact representations of multiple products over space and time.
The evaluation slide then asks how to compare the resulting models across tasks and regions.
These papers are separate research projects; the deck does not claim they generated the FTW release.

## MIND the Gap

- Paper: [Corley et al., A Geographic Implicit Neural Representation with Adjustable Spatial Scale](https://arxiv.org/abs/2609.25454).
- Project and embedding product: <https://research.taylorgeospatial.org/mind/>.
- Video: <https://research.taylorgeospatial.org/mind/assets/mind-linkedin-2160x2700.mp4>.
- Retrieved 3 October 2026; source SHA-256 `93f3eb510461284e1d9777b8ed565deb49a41c964f029e6bebb3b6130ecb76be`.

The 30-second project video cycles through PCA colors of successive 64-dimensional storage chunks.
The colors are fitted separately for each chunk; they are not land-cover classes or observations of change through time.
The slide crop retains the globe, embedding strip, and coarse/fine labels while removing the duplicated title and social-video footer.
The timing and geographic content are unchanged.

```sh
curl -L --fail https://research.taylorgeospatial.org/mind/assets/mind-linkedin-2160x2700.mp4 -o /tmp/mind-original.mp4
ffmpeg -y -i /tmp/mind-original.mp4 \
  -vf 'crop=1760:1700:200:720,scale=880:850' -an \
  -c:v libx264 -crf 20 -pix_fmt yuv420p -movflags +faststart \
  assets/research/mind-embedding.mp4
ffmpeg -y -ss 2 -i assets/research/mind-embedding.mp4 \
  -frames:v 1 assets/research/mind-embedding-poster.jpg
```

## Planetary Feature Fields

- Paper: [Rao et al., Planetary Feature Fields are Scalable Earth Representations](https://arxiv.org/abs/2609.37784).
- Current animation: `pff-forward-pass-sparse.gif`, supplied by Isaac Corley on 8 October 2026.
- Source preserved at `assets/research/pff-forward-pass-sparse.gif`; SHA-256 `04342ffa983b2b131d48ff8e1894fee4ad64eba8cda2a6501a8abdc1b6afd6ea`.
- The 2160 × 1260 animation shows the forward pass from space/time coordinates through explicit factors and product decoders to observations, embeddings, and maps.
- H.264 conversion preserves the full frame and supplied 3.8-second timing. Playback is silent and loops on slide entry.
- The previous NDVI access demonstration remains in `assets/research/pff-animation.gif` but is no longer used in the deck.

The compression and retained-performance statement follows the abstract.
Compression is relative to uncompressed source data.
Retained performance refers to the evaluated downstream tasks, not absolute prediction accuracy or a global deployment guarantee.
The architecture animation illustrates the method; it does not visualize those evaluation results.

The previous static panels remain in `assets/research/` as reference material.
They came from [Figure 1, version 1](https://arxiv.org/html/2609.37784v1#S0.F1), under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), retrieved on 3 October 2026.
They show original and PFF-VM outputs for Sentinel-2 (2017), TESSERA (2021), and biomass (2022), at 53.389°N, 16.089°E.

## Five-minute conference timing

The deck follows the [CNG plenary Ignite format](https://cloudnativegeo.org/blog/2026/04/share-your-work-at-cng-forum-2026/): 20 slides at 15 seconds each.
Every slide has an explicit `data-autoslide="15000"` attribute so Reveal does not extend the interval to finish longer videos.
The MIND and PFF clips retain their original media timing, but the slides advance at 15 seconds.
Use `?autoSlide=0` to review the complete clips and navigate manually.

| Section | Seconds |
| --- | ---: |
| Title and Taylor Geospatial | 30 |
| FTW product, quarterly mosaics, and edition comparisons | 90 |
| Three change-comparison slides | 45 |
| Processing tools, data formats, and access | 45 |
| MIND and PFFs | 30 |
| Features, benchmarks, and NeurIPS position paper | 30 |
| Open source and final project links | 30 |
| Total | 300 |

## Mosaic mirror and reusable tools

Added on 5 October 2026. The [mosaic mirror](https://source.coop/tge-labs/sentinel-2-quarterly-cloudless-mosaics)
contains 10 m RGB/NIR COGs with overviews. Its public README describes complete
2017–2025 quarters and a transferred 2026 Q2 outside the catalog, with Q1 incomplete
at the README's audit date. The slide uses the requested concise label
“2017–2026” and “2026 · Q1/Q2”; it makes no complete-2026 claim.
The catalog screenshot was captured from Source Cooperative.

The tools slide describes operations, without transferring benchmark speedups
to the FTW workload:

- [coarsen](https://research.taylorgeospatial.org/coarsen/): Rust geometry
  simplification with a Shapely interface; shared edges stay aligned for valid coverages.
- [contourrs](https://research.taylorgeospatial.org/contourrs/): Rust raster
  polygonization and contour bands, with Python and Arrow outputs.
- [fbp](https://github.com/fieldsoftheworld/fbp): field-instance postprocessing,
  including BoundaryVote and windowed processing.

The [global pipeline repository](https://github.com/fieldsoftheworld/ftw-global-data-catalog)
contains mosaic preparation, inference, postprocessing, map tiles, and publishing.
Training code is in [ftw-baselines](https://github.com/fieldsoftheworld/ftw-baselines).
The fbp repository and README are also public. The workflow spans these repositories;
the catalog repository is the main entry point linked from the slide.

`assets/project-links.json` records the QR destinations; `scripts/build_qr_codes.py`
generates them with a standard quiet zone and medium error correction.

## Position-paper first page

The dedicated NeurIPS paper slide shows the complete first page of
[arXiv:2605.12678v3](https://arxiv.org/pdf/2605.12678v3), dated 10 September 2026.
`assets/research/state-of-the-art-page1.png` was rendered directly from that PDF
with Poppler at 1800 pixels on the long edge. The image links to the PDF.
The acceptance label follows the author's conference-status confirmation.
