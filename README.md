# Cloud colorizer

Cloud colorizer is a simple tool to colorize your point clouds from tiff images.

Special credits to [pnytko](https://github.com/pnytko) for the original idea.

## Requirements

* rasterio
* numpy
* tqdm

## Arguments

* -i, --input: path to the input point cloud
* -t, --tiff: path to the tiff image
* -o, --output: path to the output point cloud

## Usage

```bash
python cloud_colorizer.py -i input_cloud.las -t tiff_image.tif -o output_cloud.las
```


