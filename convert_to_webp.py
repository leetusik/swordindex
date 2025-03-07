#!/usr/bin/env python3
import os
import sys

from PIL import Image


def convert_to_webp(input_file, quality=80):
    """
    Convert an image to WebP format

    Args:
        input_file (str): Path to the input image file
        quality (int): Quality of WebP image (0-100)

    Returns:
        str: Path to the output WebP file
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} does not exist")
        return None

    # Get the output file path
    output_file = os.path.splitext(input_file)[0] + ".webp"

    try:
        # Open the image
        img = Image.open(input_file)

        # Convert to RGB if RGBA and has no transparency
        if img.mode == "RGBA":
            # Check if the image has any transparent pixels
            if not any(pixel[3] < 255 for pixel in img.getdata()):
                img = img.convert("RGB")

        # Save as WebP
        img.save(output_file, "WEBP", quality=quality)
        print(f"Converted {input_file} to {output_file}")

        # Get file sizes for comparison
        original_size = os.path.getsize(input_file)
        webp_size = os.path.getsize(output_file)
        reduction = (1 - webp_size / original_size) * 100

        print(f"Original size: {original_size/1024:.2f} KB")
        print(f"WebP size: {webp_size/1024:.2f} KB")
        print(f"Size reduction: {reduction:.2f}%")

        return output_file

    except Exception as e:
        print(f"Error converting {input_file}: {e}")
        return None


def main():
    # Check if Pillow is installed
    try:
        import PIL

        print(f"Using Pillow version {PIL.__version__}")
    except ImportError:
        print("Pillow is not installed. Please install it with: pip install Pillow")
        sys.exit(1)

    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the paths to the carousel images
    carousel_dir = os.path.join(script_dir, "static", "img", "carousel")

    # Check if the directory exists
    if not os.path.exists(carousel_dir):
        print(f"Error: Carousel directory {carousel_dir} does not exist")
        sys.exit(1)

    # Convert the carousel images
    images_to_convert = [
        os.path.join(carousel_dir, "01.png"),
        os.path.join(carousel_dir, "02.png"),
    ]

    for image_path in images_to_convert:
        if os.path.exists(image_path):
            convert_to_webp(image_path)
        else:
            print(f"Warning: Image {image_path} does not exist")


if __name__ == "__main__":
    main()
