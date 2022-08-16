import sys
import argparse
from PIL import Image
from pathlib import Path


from image import (
    convert_to_greyscale,
    convert_to_jpg,
    resize_image,
    get_image_matrix,
    save_result_image,
    flip_image,
    rotate_90_deg_image,
)


def prepare_image(file_path):

    converted_img = convert_to_greyscale(Image.open(file_path))

    if not file_path.endswith(".jpg"):
        converted_img = convert_to_jpg(converted_img)

    resized_img = resize_image(converted_img)

    return get_image_matrix(resized_img)


def add_args(parser):
    parser.add_argument(
        "path",
        type=lambda p: Path(p).absolute(),
        default=Path(__file__).absolute().parent / "data",
        help="Path to the input image file",
    )

    parser.add_argument(
        "output_path",
        type=lambda p: Path(p).absolute(),
        default=Path(__file__).absolute().parent / "data",
        help="Path to the output image directory",
    )

    parser.add_argument(
        "--numpy",
        action="store_true",
        help="To use numpy matrix multiplication algorithm (crazy faster)",
    )

    parser.set_defaults(numpy=False)


def setup():
    parser = argparse.ArgumentParser(description="Command line interface")

    subparsers = parser.add_subparsers(dest="command", help="sub-command help")

    parser_flip = subparsers.add_parser("flip", help="Flips an image")

    add_args(parser_flip)

    parser_rotate = subparsers.add_parser("rotate", help="Rotates an image 90º left")

    add_args(parser_rotate)

    args = parser.parse_args()

    # if args is empty show help
    if not sys.argv[1:]:
        parser.print_help()
        return

    img_matrix = prepare_image(str(args.path))

    result = img_matrix

    if args.command == "flip":
        result = flip_image(img_matrix, args.numpy)
    elif args.command == "rotate":
        result = rotate_90_deg_image(img_matrix, args.numpy)

    save_result_image(result, f"{args.output_path}/{args.path.stem}_{args.command}.jpg")


def main():
    setup()
