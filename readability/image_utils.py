# image_utils.py

import cv2

def crop_region(image, region):
    return image[
        region.y : region.y + region.height,
        region.x : region.x + region.width,
    ]

def load_image(path: str):
    image = cv2.imread(path)

    if image is None:
        raise ValueError(f"Could not load image: {path}")

    return image