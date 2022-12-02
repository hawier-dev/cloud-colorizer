"""
Cloud colorizer

This script is used to colorize a point cloud using from a tiff image.
"""
from functions import parse_args
from las_file import LasFile


def main():
    las_path, tiff_path, out_path = parse_args()
    las_file = LasFile(las_path)
    las_file.colorize_from_image(tiff_path)
    las_file.save(out_path)


if __name__ == "__main__":
    main()
