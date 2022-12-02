import argparse
import os.path
import sys

import rasterio as rio


def error_message(title, message):
    print(f"\033[91m{title}\033[0m: {message}")
    sys.exit(1)


def warning_message(title, message):
    print(f"\033[93m{title}\033[0m: {message}")


def success_message(title, message):
    print(f"\033[92m{title}\033[0m: {message}")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="Path to las file"
    )
    parser.add_argument(
        "-t",
        "--tiff",
        type=str,
        required=True,
        help="Path to image file",
    )
    parser.add_argument(
        "-o", "--output", type=str, required=True, help="Path to output directory"
    )
    args = parser.parse_args()

    if not args.input.endswith(".las") and not args.input.endswith(".laz"):
        error_message(
            "Error",
            "Path must be a .las or .laz file",
        )

    if os.path.isdir(args.output):
        os.path.join(
            args.output,
            os.path.basename(args.input)
            .replace(".las", "_colorized.las")
            .replace(".laz", "_colorized.laz"),
        )

    return args.input, args.tiff, args.output
