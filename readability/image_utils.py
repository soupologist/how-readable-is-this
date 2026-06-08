import cv2

def load_image(path: str):
    image = cv2.imread(path)

    if image is None:
        raise ValueError(f"Could not load {path}")

    return image


def crop_region(image, region):
    return image[
        region.y:region.y + region.height,
        region.x:region.x + region.width
    ]