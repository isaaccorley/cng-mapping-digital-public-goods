# Research slides

The two research slides follow FTW's data-access slides.
MIND introduces reusable geographic embeddings; PFFs extend the discussion to compact representations of multiple products over space and time.
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
- Figures: [Figure 1, version 1](https://arxiv.org/html/2609.37784v1#S0.F1), reused under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- Retrieved 3 October 2026 from `https://arxiv.org/html/2609.37784v1/figures/data/teaser_panels/`.

The slide selects the original and PFF-VM columns for Sentinel-2 (2017), TESSERA (2021), and biomass (2022), at 53.389°N, 16.089°E.
Assets retain their source filenames with a `pff-` prefix.
Panels and colors are unchanged; labels and layout were adapted for the slide.
The biomass legend retains its 0–300 Mg/ha range.

The compression and retained-performance statement follows the abstract.
Compression is relative to uncompressed source data.
Retained performance refers to the evaluated downstream tasks, not absolute prediction accuracy or a global deployment guarantee.

## Seven-minute pacing

| Section | Seconds |
| --- | ---: |
| Title and Taylor Geospatial | 20 |
| FTW product and edition comparisons | 140 |
| Three change-comparison slides | 120 |
| Data formats and access | 40 |
| MIND and PFFs | 60 |
| Evaluation research | 20 |
| Open source and closing | 20 |
| Total | 420 |
