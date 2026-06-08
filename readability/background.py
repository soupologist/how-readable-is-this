import cv2
import numpy as np


def background_luminance(region, mask):
    gray = cv2.cvtColor(
        region,
        cv2.COLOR_BGR2GRAY
    )

    pixels = gray[mask == 0]

    if len(pixels) == 0:
        return 0

    return float(np.mean(pixels))