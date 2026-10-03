# Open-source acknowledgements

The credits slide is based on an import, dependency, and pipeline scan of
[`taylor-geospatial/global-ftw-2e`](https://github.com/taylor-geospatial/global-ftw-2e)
at `cbda0b122f12509624d29f9a4ae04dae27485661`. The repository was formerly named
`ftw-s2-quarterly`. Evidence is saved in `assets/provenance/open-source-tools.json`.

| Work | Projects credited | Repository evidence |
|---|---|---|
| Model training and execution | PyTorch, TorchGeo, ONNX Runtime | `src/global_ftw/models.py`, `model.py`, `scripts/stream_infer.py`, `export_onnx.py` |
| Arrays and geospatial data | NumPy, GeoPandas, Rasterio, Shapely | `mosaic_dataset.py`, `polymetric.py`, `scripts/merge_polygons.py`, `cogify_scores.py` |
| Native geometry / raster foundations | GDAL, GEOS, PROJ | Rasterio and Shapely stack; `rust/coverage-simplify/src/native.rs` |
| Polygon extraction | BoundaryVote / fbp | `scripts/boundaryvote_tiles.py`, `bv_window.py` |
| Tables and catalogs | DuckDB, Apache Arrow / PyArrow, rustac | `scripts/fiboa_convert.py`, `publish_stac.py`, `build_stac_geoparquet.py` |
| Browser | OpenLayers, hyparquet, proj4js, ol-pmtiles / PMTiles | `web/vendor/package.json`, `web/js/vector.js`, `pmtiles.js` |
| PMTiles production | tylertoo | README pipeline description; production pipeline lives in `fieldsoftheworld/ftw-global-data-catalog` |

The standalone coarsen package was extracted from the coverage-simplification
code after that code produced the released years. The slide does not claim
that the standalone package produced these data. Other declared packages,
including contourrs, SimpleITK, Numba, scikit-image, Matplotlib, boto3, and W&B,
are recorded in the audit; a declaration alone is not proof of a specific
production step. Development tools include uv, Ruff, ty, pytest, and pre-commit.
The viewer vendor build uses esbuild. This slide is a selected acknowledgement,
not an exhaustive software bill of materials.

## Logos

Official files are stored locally, preserving their colors and proportions.
Only line endings and trailing whitespace were normalized.
Projects without a logo located in their official repository are credited by
name. Logo attribution does not imply sponsorship or endorsement.

| Project | Official source | Local file |
|---|---|---|
| torchgeo | [Project asset](https://github.com/torchgeo/torchgeo/blob/main/docs/_static/logo/logo-color.svg) | `assets/logos/torchgeo.svg` |
| gdal | [Project asset](https://github.com/OSGeo/gdal/blob/master/data/GDALLogoColor.svg) | `assets/logos/gdal.svg` |
| geopandas | [Project asset](https://github.com/geopandas/geopandas/blob/main/doc/source/_static/logo/geopandas_logo.svg) | `assets/logos/geopandas.svg` |
| duckdb | [Project asset](https://github.com/duckdb/duckdb-web/blob/main/images/duckdb_logo_dl.svg) | `assets/logos/duckdb.svg` |
| openlayers | [Project asset](https://github.com/openlayers/openlayers/blob/main/site/src/theme/img/logo-dark.svg) | `assets/logos/openlayers.svg` |
| onnxruntime | [Project asset](https://github.com/microsoft/onnxruntime/blob/main/docs/images/ONNX_Runtime_logo.png) | `assets/logos/onnxruntime.png` |
| numpy | [Project asset](https://github.com/numpy/numpy/blob/main/branding/logo/primary/numpylogo.svg) | `assets/logos/numpy.svg` |
| pytorch | [Project asset](https://github.com/pytorch/pytorch.github.io/blob/site/assets/images/logo-dark.svg) | `assets/logos/pytorch.svg` |
| arrow | [Project asset](https://arrow.apache.org/img/arrow-logo_horizontal_black-txt_transparent-bg.svg) | `assets/logos/arrow.svg` |

Additional usage references: [PyTorch](https://pytorch.org/brand-guidelines/),
[GeoPandas](https://docs.geopandas.org/en/latest/about/logo.html),
[DuckDB](https://duckdb.org/design/), and
[Apache Arrow](https://arrow.apache.org/visual_identity/).
