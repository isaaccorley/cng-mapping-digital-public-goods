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
- Animation: `planetary-feature-fields.gif`, supplied by Isaac Corley in `1-planetary-feature-fields.gif.zip` on 3 October 2026.
- Source preserved at `assets/research/pff-animation.gif`; SHA-256 `1a4d753ed49872b150fe6d508bb12ee3f8e10b29386afe44212f7fecd03b55dc`.
- On-image credits: Arjun Rao (`arjunashokrao.me`), Copernicus Sentinel-2, and Microsoft Planetary Computer.

The 22.3-second clip demonstrates NDVI mapping through Microsoft Planetary Computer and PFFs.
Conversion to H.264 preserves the supplied timing, including the existing “4× animation” label.
The crop removes the duplicated title above the two panels; it retains the comparison, progress labels, and author/data credits.
It plays silently, loops, and uses the same slide-entry playback controls as the other clips.

```sh
ffmpeg -y -i assets/research/pff-animation.gif \
  -vf 'crop=1200:760:0:160,fps=20' -an \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -movflags +faststart \
  assets/research/pff-animation.mp4
ffmpeg -y -ss 3 -i assets/research/pff-animation.mp4 \
  -frames:v 1 assets/research/pff-animation-poster.jpg
```

The compression and retained-performance statement follows the abstract.
Compression is relative to uncompressed source data.
Retained performance refers to the evaluated downstream tasks, not absolute prediction accuracy or a global deployment guarantee.
The NDVI access demonstration is separate from that result.

The previous static panels remain in `assets/research/` as reference material.
They came from [Figure 1, version 1](https://arxiv.org/html/2609.37784v1#S0.F1), under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), retrieved on 3 October 2026.
They show original and PFF-VM outputs for Sentinel-2 (2017), TESSERA (2021), and biomass (2022), at 53.389°N, 16.089°E.

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
